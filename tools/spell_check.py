#!/usr/bin/env python3
"""Spellcheck the prose in documentation pages.

    python tools/spell_check.py docs/how-to-guides/add-discount.md
    python tools/spell_check.py docs/
    python tools/spell_check.py docs/ --list

Separate from tools/style_check.py on purpose. The style checker is about
mechanics that STYLE.md defines, and it needs no dictionary. This one needs
pyspellchecker and an allowlist that grows as the product does, so mixing the
two would make a clean style score depend on how current the word list is.

What it does not check: anything inside backticks. STYLE.md section 7 says an
app label is quoted verbatim and never corrected, so a misspelling on screen
has to stay on the page. Fenced code, HTML, link targets, image paths,
attr_list blocks and icon names are stripped for the same reason.

Words that are correct but absent from a general English dictionary go in
tools/spell_allow.txt, one per line, lowercase. Add a word there only when it
is genuinely correct. If the word is a product term, put it in the glossary
first.
"""
import argparse
import io
import os
import re
import sys

try:
    from spellchecker import SpellChecker
except ImportError:
    sys.exit('pyspellchecker is not installed. Run: pip install -r '
             'requirements.txt')

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOW_FILE = os.path.join(HERE, 'spell_allow.txt')

# tails that are real contractions or possessives. anything else after an
# apostrophe is a typo hiding behind a word the dictionary knows, as in It'sd
REAL_TAILS = ('s', 't', 'd', 're', 've', 'll', 'm')

WORD = re.compile(u"[A-Za-z][A-Za-z'’-]*")


def load_allow():
    if not os.path.exists(ALLOW_FILE):
        return set()
    words = set()
    with io.open(ALLOW_FILE, encoding='utf-8') as fh:
        for line in fh:
            line = line.split('#')[0].strip().lower()
            if line:
                words.add(line)
    return words


def blank(m):
    """Give back the same number of newlines, so line numbers still match.

    Padded with spaces, or removing an inline span would glue the words on
    either side of it into one token that no dictionary knows.
    """
    return ' ' + '\n' * m.group(0).count('\n') + ' '


def prose_of(text):
    s = text
    s = re.sub(r'^---\n.*?\n---\n', blank, s, flags=re.S)   # front matter
    s = re.sub(r'```.*?```', blank, s, flags=re.S)          # fenced code
    s = re.sub(r'<[^>]+>', blank, s, flags=re.S)            # raw html
    # confined to one line on purpose. a single stray backtick anywhere in a
    # page would otherwise flip the pairing for everything after it, and the
    # spans that then match are the prose between two labels
    s = re.sub(r'`[^`\n]*`', blank, s)                      # app labels
    s = re.sub(r'\]\([^)]*\)', '] ', s)                     # link targets
    s = re.sub(r'!\[[^\]]*\]', ' ', s)                      # image alt text
    s = re.sub(r'\{[^{}]*\}', ' ', s)                       # attr_list
    s = re.sub(r':[a-z0-9_-]+:', ' ', s)                    # icon names
    s = re.sub(r'https?://\S+', ' ', s)                     # bare urls
    s = re.sub(r'#[0-9a-fA-F]{3,8}\b', ' ', s)              # hex colors
    s = re.sub(r'\.[a-z]{2,}-[a-z0-9-]+', ' ', s)           # css class names
    return s


def check_file(path, sp, allow, root):
    rel = os.path.relpath(path, os.path.dirname(root.rstrip(os.sep)) or '.')
    raw = io.open(path, encoding='utf-8').read()
    out = []
    for i, line in enumerate(prose_of(raw).split('\n'), 1):
        for token in WORD.findall(line):
            for w in token.split('-'):
                base = w.replace(u'’', "'").strip("'-")
                # acronyms, including plurals such as URLs
                if len(base) < 3 or base.rstrip('s').isupper():
                    continue
                low = base.lower()
                # doesn't splits to a head of doesn, which no dictionary has.
                # the style checker already reports contractions, so all this
                # has to do is not report them a second time as misspellings
                if low.endswith("n't"):
                    low = low[:-3]
                head, _, tail = low.partition("'")
                if tail and tail not in REAL_TAILS:
                    out.append((i, base))
                    continue
                if head in allow or head.rstrip('s') in allow:
                    continue
                if head in sp:
                    continue
                if head.endswith('s') and head[:-1] in sp:
                    continue
                out.append((i, base))
    return rel.replace(os.sep, '/'), out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('target')
    ap.add_argument('--root', default='docs')
    ap.add_argument('--list', action='store_true',
                    help='print one bare word per line, to seed the allowlist')
    args = ap.parse_args()

    target = args.target
    if os.path.isdir(target):
        paths = sorted(os.path.join(d, f)
                       for d, _, fs in os.walk(target)
                       for f in fs if f.endswith('.md'))
    else:
        paths = [target]

    sp = SpellChecker()
    allow = load_allow()

    seen = {}
    for path in paths:
        rel, hits = check_file(path, sp, allow, args.root)
        for ln, word in hits:
            seen.setdefault(word, []).append('%s:%d' % (rel, ln))

    if args.list:
        for word in sorted(seen, key=lambda x: x.lower()):
            print(word.lower())
        return 0

    for word in sorted(seen, key=lambda x: (-len(seen[x]), x.lower())):
        locs = seen[word]
        tail = ' ...' if len(locs) > 3 else ''
        print('%-24s %3d  %s' % (word, len(locs),
                                 ', '.join(locs[:3]) + tail))

    print('\n%d files checked, %d unknown words, %d occurrences'
          % (len(paths), len(seen), sum(len(v) for v in seen.values())))
    print('Not every unknown word is wrong. A correct word that the dictionary '
          'does not have belongs in tools/spell_allow.txt.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
