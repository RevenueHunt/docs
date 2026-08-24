#!/usr/bin/env python3
"""Check documentation pages against STYLE.md and docs/reference/glossary.md.

    python tools/style_check.py docs/how-to-guides/add-discount.md
    python tools/style_check.py docs/
    python tools/style_check.py docs/ --format json

Reports violations per 100 words, per file, with line numbers.

It checks mechanics only. It cannot tell you whether a step is really one
action, whether a term is used in the right sense, or whether the page is
accurate. A clean score does not mean the page is good.
"""
import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

# --------------------------------------------------------------------------
# tiers
# --------------------------------------------------------------------------
STRICT_DIRS = ('how-to-guides', 'tutorials', 'reference')
CLEAR_DIRS = ('customer-success',)


def tier_of(rel):
    top = rel.replace(os.sep, '/').split('/')[0]
    if os.path.basename(rel) == 'index.md':
        return 'CLEAR'
    if top in CLEAR_DIRS:
        return 'CLEAR'
    if top in STRICT_DIRS:
        return 'STRICT'
    return 'CLEAR'


# --------------------------------------------------------------------------
# rules
# --------------------------------------------------------------------------
TABS = ['Shopify', 'Shopify (Legacy)', 'WooCommerce', 'Magento', 'BigCommerce',
        'Standalone']

BANNED_LINK_TEXT = {
    'here', 'this', 'this link', 'this guide', 'this article', 'this section',
    'this page', 'guide', 'article', 'section', 'previous step',
    'previous tutorial', 'previous step-by-step tutorial', 'tutorial',
    'read more', 'learn more', 'step-by-step guide', 'documentation',
}
# words that carry no destination on their own. a label is banned when every
# word in it is one of these, so "first part of this article" is caught while
# "How to Add JavaScript" is not.
LINK_FILLER = {
    'a', 'an', 'the', 'this', 'that', 'these', 'our', 'your', 'my', 'in', 'of',
    'on', 'to', 'and', 'or', 'first', 'second', 'last', 'next', 'previous',
    'full', 'complete', 'detailed', 'more', 'here', 'link', 'links', 'guide',
    'guides', 'article', 'articles', 'section', 'sections', 'page', 'pages',
    'tutorial', 'tutorials', 'doc', 'docs', 'documentation', 'part', 'read',
    'learn', 'see', 'step', 'steps', 'by', 'step-by-step', 'one', 'it',
}
# generic link text is fine when the sentence already names the destination
LINK_TEXT_EXEMPT_IF_PRECEDED_BY = re.compile(
    r'(google analytics|shopify|klaviyo|mailchimp|woocommerce|magento|'
    r'bigcommerce|hubspot|omnisend|zapier|recharge|tiktok|meta)\s+$', re.I)

ADMONITIONS = {'tip', 'info', 'note', 'warning', 'example', 'success',
               'danger', 'question'}

COMPOUNDS = [
    (r'\bpop-ups?\b', 'popup'),
    (r'\beCommerce\b|\be-commerce\b|\bEcommerce\b', 'ecommerce'),
    (r'\breoccurring\b', 'recurring'),
    (r'\bdropoff\b', 'drop-off'),
    (r'\bBuiltin\b', 'Built-in'),
    (r'\bmultiple choice (question|slide|block|setting)', 'multiple-choice'),
]

VENDORS = [
    (r'\bMailChimp\b', 'Mailchimp'), (r'\bOmniSend\b', 'Omnisend'),
    (r'\bActivecampaign\b', 'ActiveCampaign'), (r'\bJavascript\b', 'JavaScript'),
    (r'\bWoocommerce\b', 'WooCommerce'), (r'\bBigcommerce\b', 'BigCommerce'),
    (r'\bHubspot\b', 'HubSpot'),
]

DEAD_PHRASING = [
    # covers allows to, allows you to, allowing the customer to, and so on.
    # us and me are here because allows us to reads as house voice, which
    # section 4 rules out anyway, and the phrasing is dead either way
    (r'\ballow(?:s|ing)?\s+(?:(?:you|the customer|customers|the merchant|'
     r'merchants|the user|users|us|me|them|him|her|it)\s+)?to\b',
     'lets you, or lets the customer'),
    # covers is possible to, is not possible to, are not possible to
    (r'\b(?:is|are)(?: not)? possible to\b', 'you can, or you cannot'),
    (r'\bpossibility to\b', 'you can'),
]

# idiom. a non-native reader has to translate these twice, and they survive
# badly once a page is flattened for the support bot.
IDIOM = [
    (r'\bhead (?:over )?to\b', 'go to'),
    (r'\bcheck (?:it )?out\b', 'see'),
    (r'\breach out to\b', 'contact'),
]

RETIRED_TERMS = [
    (r'\bquiz takers?\b', 'customer'),
    (r'\bshoppers?\b', 'customer'),
    (r'\bvisitors?\b', 'customer'),
    (r'\bparticipants?\b', 'customer'),
    (r'\brespondents?\b', 'customer'),
    (r'\bresult pages?\b', 'results page'),
    (r'\bbranching logic\b', 'jump logic'),
]

# Feature names take sentence case inside a Shopify tab and Title Case inside
# the five legacy tabs, which document an older interface. Checked in body
# prose only: headings have their own rule, and backticks quote the screen.
FEATURE_NAMES = [
    'results page', 'results pages', 'quiz builder', 'jump logic',
    'skip logic', 'display logic', 'conditional logic', 'customer tags',
    'question settings', 'page settings', 'product block', 'slot block',
    'embed code', 'quiz settings', 'quiz design', 'block settings',
    'choice settings', 'success checklist', 'app settings', 'quiz leads',
    'quiz responses', 'quiz data', 'quiz results', 'logic rule',
    'email template', 'discount code', 'question types', 'exit intent',
]
FEATURE_TITLECASE = re.compile(
    '(' + '|'.join(
        ' '.join(w.capitalize() for w in t.split())
        for t in sorted(FEATURE_NAMES, key=len, reverse=True)) + ")")

MARKETING = ['powerful', 'seamless', 'seamlessly', 'effortless', 'amazing',
             'perfect', 'comprehensive', 'unlock', 'robust', 'streamline',
             'supercharge']

# filler immediately before an imperative verb, anywhere on the line. the
# earlier version only matched the first word of a list item, which missed
# indented continuation lines inside platform tabs.
IMPERATIVES = ('go|click|open|add|select|create|set|use|edit|save|navigate|'
               'enter|choose|check|follow|type|drag|scroll|head|press|tap|'
               'copy|paste|install|connect|publish|preview|link|remove|delete')
FILLER_BEFORE_INSTRUCTION = re.compile(
    r'\b(simply|just|easily)\s+(?:' + IMPERATIVES + r')\b', re.I)

# multi-word names that stay capitalised in a heading. checked before the
# per-word test, which cannot see that Analytics belongs to Google Analytics.
PROPER_PHRASES = [
    'Google Analytics', 'Google Merchant Center', 'Google Product Feed',
    'Built for Shopify', 'Product Recommendation Quiz', 'Shopify Flow',
    'Shopify Markets', 'Shopify Admin', 'Shopify Legacy', 'Shopify Experts',
    'Quiz Copilot', 'Meta Pixel', 'TikTok Pixel', 'Catalog Lookup Tag',
    'Storefront API', 'Content Dynamic Source', 'Information Recall',
    'Customer Tags', 'Shopify Customers', 'Success Checklist',
]

PROPER = set("""shopify woocommerce magento bigcommerce standalone klaviyo mailchimp
omnisend activecampaign hubspot zapier revenuehunt stripe wordpress google meta
tiktok facebook instagram gempages pagefly recharge handlebars github javascript
markdown liquid copilot legacy i gdpr ccpa api apis crm smtp csv html css js json
url urls id ids seo bmi ui ux faq faqs pdf ai b2b b2c xml dns tls ssl ga4 ga sku
skus cta ctas aov ltv roas dkim spf dmarc ip http https rss qr otp saas rtl""".split())


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------
# contractions. an explicit map, never a bare apostrophe sweep: possessives
# such as Shopify's and the customer's answer must not be touched.
CONTRACTIONS = {
    "cannot": ["can't"], "do not": ["don't"],
    "does not": ["doesn't"], "did not": ["didn't"],
    "will not": ["won't"], "is not": ["isn't"],
    "are not": ["aren't"], "was not": ["wasn't"],
    "were not": ["weren't"], "has not": ["hasn't"],
    "have not": ["haven't"], "had not": ["hadn't"],
    "should not": ["shouldn't"], "would not": ["wouldn't"],
    "could not": ["couldn't"], "must not": ["mustn't"],
    "you will": ["you'll"], "we will": ["we'll"],
    "they will": ["they'll"], "it will": ["it'll"],
    "you are": ["you're"], "we are": ["we're"],
    "they are": ["they're"], "you have": ["you've"],
    "we have": ["we've"], "they have": ["they've"],
    "you would": ["you'd"], "we would": ["we'd"],
    "they would": ["they'd"], "it is": ["it's"],
    "that is": ["that's"], "here is": ["here's"],
    "there is": ["there's"], "what is": ["what's"],
    "let us": ["let's"],
    "I am": ["I'm"], "I will": ["I'll"],
    "I have": ["I've"], "I would": ["I'd"],
    "it would": ["it'd"], "that will": ["that'll"],
    "there will": ["there'll"], "should have": ["should've"],
    "would have": ["would've"], "could have": ["could've"],
    "who is": ["who's"], "where is": ["where's"],
    "how is": ["how's"], "he is": ["he's"],
    "she is": ["she's"],
}
CONTRACTION_RE = re.compile(
    "\\b(?:[A-Za-z]+n['’]t|[A-Za-z]+['’](?:ll|re|ve|d|m)|(?:it|that|here|there|what|let|who|where|how|he|she)['’]s)\\b", re.I)
EXPAND = {v[0].lower(): k for k, v in CONTRACTIONS.items()}

# the company is RevenueHunt, one word. adjacent path or domain characters
# mean a literal identifier we do not control, such as the Magento namespace
# Revenuehunt\\ProductQuiz or the UTM value revenuehunt/quiz.
# marketplace listing names. legitimate only in the install article, where
# the reader must match what they search for in the marketplace.
LISTING_NAMES = [
    'RevenueHunt Product Quiz Maker',
    'Product Recommendation Quiz for WooCommerce',
    'Quiz Builder for WooCommerce – Product Recommendations',
    'Quiz Builder for WooCommerce',
    'Product Recommendation Quiz for Magento',
    'Standalone product recommendation quiz',
    'RevenueHunt Product Recommendation Quiz',
]
LISTING_RE = re.compile('(' + '|'.join(re.escape(n) for n in LISTING_NAMES) + ')')
LISTING_EXEMPT = 'install-app.md'

# our own docs site. mkdocs --strict cannot validate an absolute URL, so a
# typo in one ships as a live 404. internal links must be relative.
DOCS_HOST = 'https://docs.revenuehunt.com'

COMPANY_RE = re.compile(r'\bRevenue\s?Hunt\b', re.I)
COMPANY_SKIP = set('/\\.@-')
# transposed or dropped letters, such as RevneuHunt, which COMPANY_RE misses
MISSPELL_RE = re.compile(r'\b[Rr][Ee][Vv][A-Za-z]{5,12}\b')
# real names that sit close to RevenueHunt and must not be flagged
NOT_MISSPELLINGS = {'revenuecat'}


def _lev(a, b):
    """Levenshtein distance, small strings only."""
    prev = list(range(len(b) + 1))
    for x, ca in enumerate(a, 1):
        cur = [x]
        for y, cb in enumerate(b, 1):
            cur.append(min(prev[y] + 1, cur[y - 1] + 1,
                           prev[y - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


FENCE = re.compile(r'^\s*```')
TAB_MARK = re.compile(r'^(\s*)===\+?\s+"([^"]+)"\s*$')
ADM_MARK = re.compile(r'^\s*(!!!|\?\?\?\+?)\s+([a-z-]+)')
HEADING = re.compile(r'^(\s*)(#{1,6})\s+(.+?)\s*$')
LINK = re.compile(r'\[([^\]]*)\]\(([^)]*)\)')
IMG = re.compile(r'!\[([^\]]*)\]\(([^)]*)\)')


def prose_of(line):
    """Strip everything a wording rule must not see: code spans, images,
    link targets AND link text, urls, icons, html.

    Link text is excluded on purpose. By the style guide it is the
    destination page's own heading or a UI label, so it is a quoted string,
    not authored prose. Scanning it produced false positives such as the UI
    tab named Emails to respondents."""
    s = IMG.sub(' ', line)
    s = re.sub(r'`[^`]*`', ' ', s)
    # attr_list blocks such as { #to-respondent } or {width="500"} are
    # identifiers and attributes, not authored prose
    s = re.sub(r'\{[^{}]*\}', ' ', s)
    s = LINK.sub(' ', s)
    s = re.sub(r'https?://\S+', ' ', s)
    s = re.sub(r':[a-z0-9_+-]+:', ' ', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    return s


def sentences(text):
    for part in re.split(r'(?<=[.!?])\s+', text):
        part = ' '.join(part.split())
        if part:
            yield part


class Finding:
    __slots__ = ('line', 'rule', 'detail', 'level')

    def __init__(self, line, rule, detail, level='error'):
        self.line, self.rule, self.detail, self.level = line, rule, detail, level


def check_file(path, root):
    rel = os.path.relpath(path, root).replace(os.sep, '/')
    tier = tier_of(rel)
    raw = open(path, encoding='utf-8', errors='ignore').read()
    lines = raw.split('\n')

    findings = []
    words = 0
    in_fence = False
    in_example = None            # indent of an open example admonition
    in_frontmatter = False
    cur_tab = None
    seen_tab_bodies = set()          # dedup identical platform-tab content
    tab_groups = defaultdict(list)

    for i, line in enumerate(lines, 1):
        if i == 1 and line.strip() == '---':
            in_frontmatter = True
            continue
        if in_frontmatter:
            if line.strip() == '---':
                in_frontmatter = False
            continue
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        m = TAB_MARK.match(line)
        if m:
            cur_tab = (len(m.group(1)), m.group(2))
            tab_groups[i].append(m.group(2))
            if m.group(2) not in TABS:
                findings.append(Finding(i, 'tab-label',
                                        f'{m.group(2)!r} is not one of the six canonical labels'))
            continue
        if cur_tab is not None:
            if line.strip() and (len(line) - len(line.lstrip())) <= cur_tab[0]:
                cur_tab = None

        # an example admonition holds illustrative content the merchant would
        # write, not our instructions, so voice rules do not apply inside it
        if in_example is not None and line.strip() and (
                len(line) - len(line.lstrip())) <= in_example:
            in_example = None
        a_pre = ADM_MARK.match(line)
        if a_pre and a_pre.group(2) == 'example':
            in_example = len(line) - len(line.lstrip())

        # deduplicate repeated tab bodies: report a line once per page
        # normalise before deduping: two tabs often differ only by a trailing
        # full stop, which used to defeat the check and double every count
        key = re.sub(r'[\s.,;:]+$', '', line.strip())
        if cur_tab is not None and key:
            if key in seen_tab_bodies:
                continue
            seen_tab_bodies.add(key)

        prose = prose_of(line)
        words += len(prose.split())

        # ---- admonition type -------------------------------------------
        a = ADM_MARK.match(line)
        if a and a.group(2) not in ADMONITIONS:
            findings.append(Finding(i, 'admonition',
                                    f'{a.group(2)!r} is not an approved type'))

        # ---- links ------------------------------------------------------
        for lm in LINK.finditer(line):
            text = re.sub(r'[*`]', '', lm.group(1)).strip().lower()
            wordset = [w for w in re.findall(r"[a-z-]+", text)]
            all_filler = bool(wordset) and all(w in LINK_FILLER for w in wordset)
            if text in BANNED_LINK_TEXT or all_filler:
                before = line[:lm.start()]
                if not LINK_TEXT_EXEMPT_IF_PRECEDED_BY.search(before):
                    findings.append(Finding(i, 'link-text',
                                            f'link text {lm.group(1)!r} does not name its destination'))

        # ---- broken local images ---------------------------------------
        for im in IMG.finditer(line):
            tgt = im.group(2).split()[0] if im.group(2) else ''
            if tgt.startswith('/images/'):
                if not os.path.exists(os.path.join(root, tgt.lstrip('/'))):
                    findings.append(Finding(i, 'broken-image', tgt))

        # internal links must be relative, never absolute
        for lm in LINK.finditer(line):
            tgt = lm.group(2).split()[0] if lm.group(2) else ''
            if not tgt.startswith(DOCS_HOST):
                continue
            rest = '/' + tgt[len(DOCS_HOST):].lstrip('/')
            findings.append(Finding(i, 'absolute-link',
                                    "use the relative path " + rest))

        # ---- punctuation ------------------------------------------------
        # CLEAR pages argue and explain, so punctuation is guidance there
        # a table cell is a fragment, not a sentence. a semicolon there is a
        # list separator, and cell text is not measured for sentence length.
        is_table_row = line.lstrip().startswith('|')
        punct_level = 'error' if tier == 'STRICT' else 'warn'
        if ';' in prose and not is_table_row:
            findings.append(Finding(i, 'semicolon', 'use two sentences', punct_level))
        if '—' in prose:
            findings.append(Finding(i, 'em-dash', 'use a spaced hyphen', punct_level))

        # contractions are a known trip hazard for non-native readers
        for m in CONTRACTION_RE.finditer(prose):
            got = m.group(0).replace(chr(0x2019), chr(39))
            # an all-caps run is quoted sample content, such as a merchant
            # question title. our own prose is never shouted.
            if len(got) > 3 and got == got.upper():
                continue
            full = EXPAND.get(got.lower())
            hint = ("write " + full) if full else "write it out in full"
            findings.append(Finding(i, 'contraction',
                                    repr(got).strip(chr(39)) + " - " + hint,
                                    punct_level))

        # company name
        for m in COMPANY_RE.finditer(prose):
            got = m.group(0)
            if got == 'RevenueHunt':
                continue
            before = prose[m.start() - 1] if m.start() else ' '
            after = prose[m.end()] if m.end() < len(prose) else ' '
            if before in COMPANY_SKIP or after in COMPANY_SKIP:
                continue
            findings.append(Finding(i, 'company-name',
                                    repr(got).strip(chr(39))
                                    + " - the company is RevenueHunt"))

        # misspellings COMPANY_RE cannot see, such as transposed letters
        for m in MISSPELL_RE.finditer(prose):
            got = m.group(0)
            low = got.lower()
            if low == 'revenuehunt' or COMPANY_RE.fullmatch(got):
                continue
            if low in NOT_MISSPELLINGS:
                continue
            if not 0 < _lev(low, 'revenuehunt') <= 3:
                continue
            before = prose[m.start() - 1] if m.start() else ' '
            after = prose[m.end()] if m.end() < len(prose) else ' '
            if before in COMPANY_SKIP or after in COMPANY_SKIP:
                continue
            findings.append(Finding(i, 'company-name',
                                    got + " - the company is RevenueHunt"))

        # marketplace listing names belong only in the install article
        if not rel.endswith(LISTING_EXEMPT):
            for m in LISTING_RE.finditer(prose):
                findings.append(Finding(i, 'app-name',
                                        m.group(0)
                                        + " - write the RevenueHunt app"))

        # only a cross-reference counts. "shown above the dropdown" describes
        # where something sits on screen, which is fine.
        for w in ('below', 'above'):
            if re.search(r'\b(see|in|the table|the section|described|shown)\s+\w*\s*'
                         + w + r'\b(?!\s+(?:the|a|an|your|this|that|each|any|it)\b)',
                         prose, re.I):
                findings.append(Finding(i, 'positional-ref',
                                        f'{w!r} breaks when the page is chunked; name the section'))

        # ---- wording ----------------------------------------------------
        for pat, want in COMPOUNDS + VENDORS:
            for mm in re.finditer(pat, prose):
                findings.append(Finding(i, 'compound-or-vendor',
                                        f'{mm.group(0)!r} should be {want!r}'))
        for pat, want in DEAD_PHRASING:
            for mm in re.finditer(pat, prose, re.I):
                findings.append(Finding(i, 'dead-phrasing',
                                        f'{mm.group(0)!r} should be {want!r}'))
        for pat, want in IDIOM:
            for mm in re.finditer(pat, prose, re.I):
                findings.append(Finding(i, 'idiom',
                                        f'{mm.group(0)!r} should be {want!r}'))
        for pat, want in RETIRED_TERMS:
            for mm in re.finditer(pat, prose, re.I):
                findings.append(Finding(i, 'retired-term',
                                        f'{mm.group(0)!r} should be {want!r}'))

        if tier == 'STRICT' and in_example is None:
            for w in MARKETING:
                if re.search(r'\b' + w + r'\b', prose, re.I):
                    findings.append(Finding(i, 'marketing', f'{w!r} in a STRICT page'))
            fm = FILLER_BEFORE_INSTRUCTION.search(prose)
            if fm:
                findings.append(Finding(i, 'filler',
                                        f'{fm.group(0)!r} promises the step is easy'))

        # ---- feature-name case, Shopify tab only ------------------------
        if cur_tab is not None and cur_tab[1] == 'Shopify' and not HEADING.match(line):
            for fm in FEATURE_TITLECASE.finditer(prose):
                want = fm.group(0).split()[0] + " " + " ".join(
                    w.lower() for w in fm.group(0).split()[1:])
                findings.append(Finding(i, 'feature-case',
                                        f"{fm.group(0)!r} should be {want!r} in a Shopify tab"))

        # ---- headings ----------------------------------------------------
        h = HEADING.match(line)
        if h:
            level, text = len(h.group(2)), h.group(3)
            bare = re.sub(r'`[^`]*`|:[a-z0-9_+-]+:|[*_]', '', text)
            bare = LINK.sub(lambda m: m.group(1), bare)
            # remove multi-word proper nouns before testing word by word
            for _ph in PROPER_PHRASES:
                bare = bare.replace(_ph, ' ')
            # all-caps category headings are an accepted house pattern, used to
            # group the block types in the questions reference
            all_caps = bool(bare.strip()) and bare.strip() == bare.strip().upper()
            if not all_caps:
                # judge on the words after the first, because the first word is
                # capitalised in sentence case and Title Case alike. skip short
                # words, which are lowercase in Title Case too, and skip proper
                # nouns, which are capitalised whatever the heading style is.
                # with nothing judgeable left there is no evidence either way,
                # so say nothing rather than guess.
                hwords = [w for w in bare.split() if w.isalpha()]
                rest = [w for w in hwords[1:]
                        if len(w) > 3 and w.lower() not in PROPER]
                caps = [w for w in rest if w[0].isupper()]
                if level == 1 and rest and not caps:
                    findings.append(Finding(i, 'heading-case',
                                            'H1 should be Title Case', 'warn'))
                if level >= 2 and caps:
                    findings.append(Finding(i, 'heading-case',
                                            f'H{level} should be sentence case: {caps[:3]}'))

        # ---- sentence length, STRICT only ---------------------------------
        if tier == 'STRICT' and in_example is None and not is_table_row:
            is_step = bool(re.match(r'^\s*\d+\.\s', line))
            cap = 20 if is_step else 25
            for s in sentences(prose):
                n = len(s.split())
                if n > cap:
                    findings.append(Finding(
                        i, 'sentence-length',
                        f'{n} words, cap is {cap} for '
                        f'{"an instruction" if is_step else "a descriptive sentence"}'))

    # tab groups must use the canonical six, in order
    return rel, tier, words, findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('--format', choices=['text', 'json'], default='text')
    ap.add_argument('--root', default='docs')
    ap.add_argument('--rule', help='show only this rule')
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    target = os.path.abspath(args.target)
    paths = ([target] if os.path.isfile(target)
             else sorted(os.path.join(d, f)
                         for d, _, fs in os.walk(target)
                         for f in fs if f.endswith('.md')))

    results = []
    for p in paths:
        rel, tier, words, findings = check_file(p, root)
        if args.rule:
            findings = [f for f in findings if f.rule == args.rule]
        score = round(100.0 * len(findings) / words, 2) if words else 0.0
        results.append((rel, tier, words, score, findings))

    if args.format == 'json':
        print(json.dumps([{
            'file': r, 'tier': t, 'words': w, 'score': s,
            'findings': [{'line': f.line, 'rule': f.rule,
                          'detail': f.detail, 'level': f.level} for f in fs],
        } for r, t, w, s, fs in results], indent=2))
        return 0

    total = 0
    for rel, tier, words, score, fs in sorted(results, key=lambda x: -x[3]):
        if not fs:
            continue
        total += len(fs)
        print(f'\n{rel}  [{tier}]  {words} words  score {score} per 100 words  '
              f'{len(fs)} findings')
        by_rule = Counter(f.rule for f in fs)
        print('  ' + '  '.join(f'{k}:{v}' for k, v in by_rule.most_common()))
        for f in sorted(fs, key=lambda x: x.line)[:40]:
            print(f'    {rel}:{f.line}  {f.rule}  {f.detail}')
        if len(fs) > 40:
            print(f'    ... and {len(fs) - 40} more')

    print(f'\n{len(results)} files checked, {total} findings')
    print('Mechanics only. This does not check whether a step is one action, '
          'whether a term is used in the right sense, or whether the page is '
          'accurate.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
