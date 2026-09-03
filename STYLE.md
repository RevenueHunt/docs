# RevenueHunt Documentation Style Guide

How to write a page for docs.revenuehunt.com. MkDocs only builds `docs/`, so this file is not published.

If you are adding or editing a page in `docs/`, this is the standard it has to meet.

The single source of truth for **what things are called** is [`docs/reference/glossary.md`](docs/reference/glossary.md). This file tells you how to write; the glossary tells you which words to use.

---

## 1. Who we are writing for

Two audiences, both easy to forget:

1. **Merchants reading English as a second language.** Ecommerce store owners worldwide. Not technical.
2. **The ChatGPT support bot.** `generate_platform_docs.py` flattens every page into `shopify.txt`, `shopify-legacy.txt` and `woocommerce.txt`, and the bot answers merchant questions from those files. Flattening strips URLs, images and page context. A sentence that only makes sense on the page is a sentence the bot will answer with badly.

The structural rules here are adapted from ASD-STE100 Simplified Technical English, a controlled-English specification used in aerospace maintenance manuals.

---

## 2. Two tiers

| Tier | Applies to | Why |
|---|---|---|
| **STRICT** | `how-to-guides/` · `tutorials/` · `reference/` | A misread procedure means a broken quiz and a support ticket |
| **CLEAR** | `customer-success/` · index and hub pages | These pages argue and explain, so they need range |

**STRICT** means every rule in this file, enforced.

**CLEAR** means everything except the vocabulary lockdown and the imperative requirement. Sentence caps become guidance rather than limits.

---

## 3. Sentences

| Rule | Limit |
|---|---|
| Instruction | **20 words** |
| Descriptive sentence | **25 words** |
| Paragraph | **6 sentences** |

Caps are ceilings, not targets. Nothing rewards a nine-word sentence.

- **No semicolons.** Split the sentence.
- **No em dashes.** The house separator is a spaced hyphen: ` - `.
- **One idea per sentence.** If you need "and" twice, you need two sentences.
- **Keep verbs as verbs.** *Analyze the results*, not *perform an analysis of the results*.
- **No idiom.** A non-native reader has to translate these twice, and they
  survive badly once a page is flattened for the support bot.

  | Use | Not |
  |---|---|
  | see | check out |
  | contact | reach out to |
  | go to | head to, head over to |
  | if this happens | if you hit this |
  | have, or meet | run into |
  | ready, within the limit | good to go |
- **No contractions.** Write *do not*, not *don't*. Write *you will*, not
  *you'll*. Contractions are one of the first things a non-native reader
  misreads, and *won't* is easy to skim as *want*. Possessives are not
  contractions: *the customer's answer* and *Shopify's collections* are correct.
  Keep a contraction only when it sits inside a quoted app label.

---

## 4. Voice

| Situation | Voice | Example |
|---|---|---|
| A step to perform | Imperative, verb first | Open the Quiz builder. |
| A step where the goal is not obvious | Purpose clause, then imperative | To recommend a full routine, group products into slots. |
| Something the reader can choose to do | Second person | You can pre-fill responses. |
| Something the system does on its own | Impersonal | Responses are created when a customer completes the quiz. |
| Never | | One should open the Quiz builder. / The Quiz builder should then be opened. |

Address the reader as **you**. Never *the user*, *one*, or *we*.

**Prefer the imperative over "you can" in a step.** *Add a discount code* beats *You can add a discount code* when adding one is required. Keep *you can* for genuinely optional things.

This matches [Microsoft](https://learn.microsoft.com/en-us/style-guide/grammar/person), [Google](https://developers.google.com/style/person) and [Shopify Polaris](https://polaris.shopify.com/foundations/content/voice-and-tone).

---

## 5. Terminology

**Use the [glossary](docs/reference/glossary.md).** It defines every product term, split by platform where the platforms differ.

Rules that bind everywhere:

| Use | Not |
|---|---|
| **RevenueHunt** (one word, capital R and H) | Revenue Hunt, Revenuehunt, revenuehunt |
| **results page** (always plural) | result page |
| **popup** | pop-up, pop up |
| **ecommerce** | eCommerce, e-commerce |
| **multiple-choice** as an adjective | multiple choice question |
| **drop-off** as a noun, **drop off** as a verb | dropoff |
| **recurring** | reoccurring |
| **lets you** (the merchant acts) | allows to, allows you to |
| **lets the customer** (the customer acts) | allows to, allows the customer to |
| **you can** | you have the possibility to, it is possible to |
| Mailchimp, Omnisend, ActiveCampaign, WooCommerce, HubSpot, JavaScript | MailChimp, OmniSend, Activecampaign, Javascript |

**RevenueHunt is the company name and never varies.** The only places the
other spellings are correct are literal identifiers that we do not control:
the Magento namespace `Revenuehunt\ProductQuiz`, the Composer package
`Revenuehunt/module-productquiz`, the UTM value `revenuehunt/quiz`, and
anything inside a domain such as `admin.revenuehunt.com`. Quote those as they are.

### Naming the app

Call it **the RevenueHunt app**, or **the app** once context is established.

Add a qualifier only when two platforms are contrasted in the same sentence,
or when the legacy version must be distinguished:

- **RevenueHunt app for WooCommerce**
- **Legacy version of the RevenueHunt app for Shopify**

Inside a platform tab the qualifier is usually redundant, because the reader
already knows which platform they are in. Do not repeat it in every tab.

**Never write V2 or V1.** They are internal names for the two app versions and
a merchant never sees either string. Write **the `💎Built for Shopify` version
of the RevenueHunt app** and **the legacy app**. When a sentence has already
named the version, "this integration" or "the app" carries it.

The one exception is `(Imported from V1)`, the literal suffix the app writes
into the name of a migrated quiz. That is what the merchant sees on screen, so
it is quoted, not our terminology.

**Never use a marketplace listing name as the subject of a sentence.** Listing
names are marketplace search strings, they change without notice, and
*Quiz Builder for WooCommerce* collides with **Quiz builder**, our own term for
where you build a quiz.

**One exception: the install article.** In `how-to-guides/install-app.md` the
reader must visually match what they search for in the marketplace, so quote
the listing name verbatim there, inside its platform tab. Everywhere after
that, it is the RevenueHunt app.

### The hyphen rule

A compound modifier is hyphenated **before** a noun and open **after** it. The noun form of a phrasal verb takes a hyphen; the verb form stays open.

| Hyphenated | Open |
|---|---|
| a follow-up email | capture the email and follow up |
| a step-by-step guide | build it step by step |
| per-question drop-off | three to six choices per question |
| text-based choices | custom text based on choices |

These are already correct throughout. Do not "fix" them.

### Marketing language

Never in STRICT pages: **powerful · seamless · effortless · amazing · perfect · comprehensive · unlock · robust · streamline · supercharge**.

Never **simply**, **just** or **easily** before an instruction. When the step is easy they add nothing; when it is hard they tell a struggling merchant the problem is them.

---

## 6. Capitalisation

Throughout this file, **the legacy tabs** means these five: **Shopify (Legacy)**, **WooCommerce**, **Magento**, **BigCommerce**, **Standalone**. The **Shopify** tab is the Built for Shopify version and behaves differently.

| Where | Style | Example |
|---|---|---|
| Feature names, in the **Shopify** tab | sentence case | Open **Results page**, set **Jump logic** |
| Feature names, in the five legacy tabs | Title Case | Open **Results Page**, set **Jump Logic** |
| Feature names, in prose outside any tab | Title Case | unchanged for now |
| H1 | Title Case | `# How to Add a Discount` |
| H2 and below | sentence case | `## Add a discount code` |

The Shopify tab follows [Polaris](https://polaris-react.shopify.com/content/grammar-and-mechanics), which specifies sentence case for interface labels. The five legacy tabs document an older app whose interface uses Title Case, so they keep it.

**Capitalised names a control; lowercase names the idea.** *Go to Results page* is the tab. *shown on the results page* is the screen.

In headings, keep brand names, acronyms (GDPR, API, A/B, RTL), multi-word product names (Built for Shopify), and the pronoun I. Sentence-case each part of a hyphenated word: `Top-level container structure`, not `Top-Level`.

Changing heading capitalisation does not break links. MkDocs lowercases the anchors it generates.

---

## 7. Quoting the app

**Anything in backticks quotes the screen and is never restyled.**

```
`+ Add Jump Logic`      `Jump Logic ▼`      `Automatic Popup Quiz (Block)`
`Pass attribute information to result page`
```

If an app label is wrong or inconsistent with this guide, that is a product fix. Raise it. Never silently correct a quote, because the merchant has to find that exact string on screen.

---

## 8. Links

**Link text names its destination.** The docs are flattened for the support bot and the URL is dropped, so the text has to stand on its own.

```
Wrong:  Check out [this article](/how-to-guides/add-javascript/) for more information
Right:  Check out [How to Add JavaScript](/how-to-guides/add-javascript/) for more information
```

Never use as link text: **here · this · this link · this guide · this article · this section · this page · guide · article · section · previous step · previous tutorial · read more · learn more**.

Take the label from the destination page's own H1 or heading.

**Exception:** if the sentence already names the destination, generic text is fine. *Refer to the Google Analytics [documentation](...)* works, because the flattened sentence still means something.

**Internal links must be relative.** Write `/how-to-guides/sync-catalog/`, never
`https://docs.revenuehunt.com/how-to-guides/sync-catalog/`. The build validates
relative links and silently ignores absolute ones, so a typo in an absolute
link ships as a live 404. Full URLs are for genuinely external destinations.

**Avoid `below` and `above`** as cross-references. They break once a page is chunked for the bot. Name the section instead.

---

## 9. Admonitions

Six types, each with one job. Do not use others.

| Type | Means |
|---|---|
| `tip` | A pointer to another page, or an optional improvement |
| `info` | Context the reader needs in place |
| `note` | Platform availability or feature status |
| `warning` | Doing this wrong breaks something |
| `example` | A worked case |
| `success` / `danger` | The matched 📈 / 📉 pair, customer-success vertical pages only |

Use `??? question` (collapsible) for FAQ entries.

- **Every callout that only points somewhere else is a `tip`.** Not info, not note.
- **`note` is reserved** for platform availability and status. It is not a general aside.
- **`danger` is not a general risk marker.** That is `warning`.

---

## 10. Procedure steps

### Numbered lists are procedures

Every numbered step is one action, in the imperative.

**One list per procedure, numbered straight through.** Never group steps under a
bold `**Step 1:**` heading that restarts the numbering at 1. A reader following
the page with the app open loses their place the moment the numbers repeat.
Fifteen steps numbered 1 to 15 beat five groups of three.

**Open each step with a bold imperative sentence.** Any detail follows it in
plain text on the same line:

```
9. **Link the products in the Choice settings.** Every choice needs at least one product or collection.
```

The bold half is what the reader does. The plain half is the caveat, the
consequence or the reason. Sub-bullets under a step carry parameters and
options, never further actions.

**Do not put a heading inside a platform tab** to group steps. It repeats six
times in the table of contents. The numbered list is the grouping.

**A leading location or context phrase is fine, and often better:**

```
Good:  In Shopify Admin, go to Settings > Checkout
Good:  From the app Dashboard, find your quiz and click Edit
```

Do not rewrite these to force the verb first.

**These are not steps.** Move them into surrounding prose or an admonition:

```
Your changes will be saved automatically.              a result, not an action
Once this option is active, the block will show...     a consequence
You can also adjust the opacity with the slider.       an optional extra, use a tip
If your store uses Shopify Markets...                  a condition
```

### Bulleted lists are not procedures

Bullets carry reference definitions and prose lists. They stay descriptive:

```
- **Image Opacity** - A slider which lets you adjust the opacity of the uploaded image.
```

Do not make these imperative, and do not apply step rules to them.

---

## 11. Platform tabs and images

### Tabs

The canonical order, on every page that has them:

```
Shopify · Shopify (Legacy) · WooCommerce · Magento · BigCommerce · Standalone
```

Label them exactly like that. A mismatched label renders as a separate orphan tab group, with no error.

**Write shared content once.** Only tab a section when the platforms genuinely differ. Copying the same text into all six tabs guarantees the copies drift apart later.

### Images

- Filenames have no spaces and no typos. Filename, alt text and prose should agree.
- Alt text describes the screenshot. If a file is renamed, update the alt text with it.
- Every referenced image must exist.
- Images hosted outside the repo cannot be renamed from here. Fix those at source.

---

## 12. Things that break

| Trap | What happens |
|---|---|
| **Find and replace without guards** | A sweep that ignores link targets, fenced code, inline backticks, icon names (`:material-wifi:`) and image filenames will silently corrupt links. Always exclude those first. |
| **Platform tabs multiply every count** | Content repeats up to six times, so a search hit count is roughly six times the number of real sentences. Deduplicate before estimating work. |
| **Word boundaries miss inflected forms** | Searching for `available` will not find `unavailable`. Check prefixed and suffixed variants separately. |
