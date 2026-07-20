---
icon: material/lan
description: "Turn quiz answers, customer tags and recommendations into a system of automated Klaviyo lifecycle flows that keep selling long after the quiz ends."
---

# How to Build Post-Quiz Email Flows in Klaviyo

Most merchants stop at the results email: the quiz finishes, Klaviyo sends the recommendation, done. That email is worth building, but it captures only the first session. The bigger opportunity is everything that happens *after*.

Your quiz collects [zero-party data](/how-to-guides/use-customer-tags/) that no pixel or purchase history can match: the customer told you their skin type, their main concern, their goal, their budget. Every one of those answers lands on a Klaviyo profile the moment the quiz ends. Each answer becomes a segment filter. Each filter becomes a personalized flow. And each flow becomes a revenue moment timed to what the customer actually does next.

This is the difference between using your quiz as a conversion tool and using it as **retention infrastructure**. Across the RevenueHunt platform, **1 in 5 quiz-attributed orders lands more than 30 days after the quiz**, and segmented Klaviyo sends earn roughly **3x the revenue per recipient** of generic ones. The flows in this guide are how you capture that long tail.

!!! warning "You need two connections to Klaviyo, not one"

    These flows combine two data sources inside Klaviyo:

    1. **RevenueHunt → Klaviyo** sends the quiz *data*: answers, customer tags, recommended products. This is what you segment and personalize on.
    2. **Your store → Klaviyo** sends the *behavioral events*: `Started Checkout`, `Placed Order`, `Viewed Product`. This is what triggers the cart, browse, replenishment and cross-sell flows.

    Both must be connected. The results-delivery and win-back flows only need connection 1. The four behavior-triggered flows need connection 2 as well. Connection 2 is set up in Klaviyo using your platform's native integration (see the prerequisites for your platform below).

## Prerequisites

=== "Shopify"

    1. Your quiz has an [email question](/reference/quiz-builder/questions/#email) and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) via OAuth with `Send Quiz Leads to Klaviyo Profiles` enabled.
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/) so answers arrive on the profile as customer tags.
    3. **Your Shopify store is connected to Klaviyo** through Klaviyo's native Shopify integration, so events like `Started Checkout`, `Placed Order` and `Viewed Product` reach Klaviyo. Without this the four behavior-triggered flows have nothing to trigger on.

=== "Shopify (Legacy)"

    1. Your quiz has an email question and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) with your **Public API Key** (and a **Private API Key** if you also add contacts to a list).
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/).
    3. **Your Shopify store is connected to Klaviyo** through Klaviyo's native Shopify integration, so `Started Checkout`, `Placed Order` and `Viewed Product` events reach Klaviyo.

    !!! info "Legacy quizzes send different property names"

        A legacy Shopify quiz sends the older Klaviyo property format (`PERMALINK`, `Q-`, `SLOT-`, `T-`), which changes the segment, trigger filters and personalization tokens below. Consider [migrating to Built for Shopify](/how-to-guides/migrate-shopify-legacy-quiz/) for the modern property set and one-click OAuth.

=== "WooCommerce"

    1. Your quiz has an email question and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) with your **Public API Key** (and a **Private API Key** for lists).
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/).
    3. **Your WooCommerce store is connected to Klaviyo** through Klaviyo's WooCommerce integration (the Klaviyo plugin), so `Started Checkout`, `Placed Order` and `Viewed Product` events reach Klaviyo.

=== "Magento"

    1. Your quiz has an email question and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) with your **Public API Key** (and a **Private API Key** for lists).
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/).
    3. **Your Magento (Adobe Commerce) store is connected to Klaviyo** through Klaviyo's Magento extension, so `Started Checkout`, `Placed Order` and `Viewed Product` events reach Klaviyo.

=== "BigCommerce"

    1. Your quiz has an email question and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) with your **Public API Key** (and a **Private API Key** for lists).
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/).
    3. **Your BigCommerce store is connected to Klaviyo** through Klaviyo's BigCommerce integration, so `Started Checkout`, `Placed Order` and `Viewed Product` events reach Klaviyo.

=== "Standalone"

    1. Your quiz has an email question and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) with your **Public API Key** (and a **Private API Key** for lists).
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/).

    !!! warning "No native store events on Standalone"

        A standalone quiz has no ecommerce platform feeding purchase and cart events into Klaviyo. Unless you push those events yourself through [Klaviyo's Track API](https://developers.klaviyo.com/en/reference/create_event), the four behavior-triggered flows (cart, browse, replenishment, cross-sell) will not have events to fire on. On Standalone, focus on the **results-delivery** and **win-back** flows, which only need the RevenueHunt sync.

New to Klaviyo automations? Read Klaviyo's [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932) first.

## The architecture: one universal email, then five behavior-triggered flows

Every quiz needs **one universal email**: the results delivery, sent the moment the quiz finishes. On top of that sit **five flows that fire based on what the customer does next**. You don't need all six on day one. Build the results email first, then add the flows your category leans on hardest (see the [industry table](#which-flows-to-build-first-by-industry) below).

| Flow | Klaviyo trigger | When it fires | Needs store→Klaviyo? |
|------|-----------------|---------------|----------------------|
| [Results delivery](#1-results-delivery-universal) | Added to segment (or list) | Immediately | No |
| [Cart abandonment](#2-cart-abandonment-recommendation-aware) | Metric: `Started Checkout` | 1-4h, 24h, 72h | Yes |
| [Browse abandonment](#3-browse-abandonment-tag-conditional) | Metric: `Viewed Product` | 4h, optional +3 days | Yes |
| [Replenishment](#4-replenishment-cycle-timed) | Metric: `Placed Order` | N days before run-out | Yes |
| [Cross-sell](#5-cross-sell-routine-completion) | Metric: `Placed Order` | 7-14 days after | Yes |
| [Win-back](#6-win-back-segment-conditional) | Added to segment | 60-120 days inactive | No |

The important idea: **the setup is shared, the trigger is what diverges.** Every flow reads the same quiz-derived properties. What changes from one flow to the next is the Klaviyo *trigger* (a segment, a checkout event, an order) and the *timing*.

## Set this up once (shared foundation)

These steps are the same no matter which flows you build.

### Know what the quiz sends

Every completion writes a set of `custom properties` to the Klaviyo profile. You reference these in segment definitions, conditional splits and email templates. The exact names include your quiz ID, so they are unique to your quiz.

=== "Shopify"

    Your quiz sends these custom properties:

    - `ANSWER_BY_BLOCK-<blockRef>-<QuizID>`: the answer to one question. Overwritten on each retake.
    - `ANSWERS_BY_BLOCK-<QuizID>`: present on every quiz taker. This is the property you use to detect quiz takers.
    - `TAGS-<QuizID>`: the customer tags from your quiz logic. Your main segmentation lever.
    - `RECOMMENDATIONS_BY_SLOT-<QuizID>`: recommended products (title, price, image, URL). JSON object, appended on each retake.
    - `RESPONSE_ID-<QuizID>`: the unique response ID. Use it to link back to the results page.
    - `QUIZ_NAME-<QuizID>`: the quiz name. Handy in subject lines.

=== "Shopify (Legacy)"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every quiz taker. This is the property you use to detect quiz takers.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `price`, `sku`, `url`, `image_url`), where `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag. Present on the profile when that tag was applied.

=== "WooCommerce"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every quiz taker. Use it to detect quiz takers.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `price`, `sku`, `url`, `image_url`), `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag, present when applied.

=== "Magento"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every quiz taker. Use it to detect quiz takers.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `price`, `sku`, `url`, `image_url`), `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag, present when applied.

=== "BigCommerce"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every quiz taker. Use it to detect quiz takers.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `price`, `sku`, `url`, `image_url`), `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag, present when applied.

=== "Standalone"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every quiz taker. Use it to detect quiz takers.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `price`, `sku`, `url`, `image_url`), `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag, present when applied.

!!! tip "Find your exact property names on a test profile"

    Take a test quiz with a sample email, then open `Klaviyo > Audience > Profiles` and search for it. The profile shows every property your quiz sends, with the exact block references, slot names and quiz ID. Copy the names from there. See [Use Quiz Data in Klaviyo Email Templates](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates) for the full reference and the `{{ person|lookup:'...' }}` syntax.

### Create your "Quiz Takers" segment

This segment is the backbone. It defines everyone who finished the quiz, and you use it both as a trigger (results delivery, win-back) and as a filter inside behavior-triggered flows.

=== "Shopify"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `ANSWERS_BY_BLOCK-<QuizID>`, and set the condition to `is set`.
    3. Save. New quiz takers join automatically.

    !!! tip "Segment on a specific answer or tag"

        To target a slice of quiz takers rather than all of them, filter on a specific value instead, for example `TAGS-<QuizID>` `contains` `Color-Treated`, or `ANSWER_BY_BLOCK-<blockRef>-<QuizID>` `equals` `Oily`. This is how you build audience-specific versions of any flow below.

=== "Shopify (Legacy)"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. New quiz takers join automatically.

    !!! tip "Segment on a specific answer or tag"

        To target a slice of quiz takers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. This is how you build audience-specific versions of any flow below.

=== "WooCommerce"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. New quiz takers join automatically.

    !!! tip "Segment on a specific answer or tag"

        To target a slice of quiz takers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. This is how you build audience-specific versions of any flow below.

=== "Magento"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. New quiz takers join automatically.

    !!! tip "Segment on a specific answer or tag"

        To target a slice of quiz takers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. This is how you build audience-specific versions of any flow below.

=== "BigCommerce"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. New quiz takers join automatically.

    !!! tip "Segment on a specific answer or tag"

        To target a slice of quiz takers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. This is how you build audience-specific versions of any flow below.

=== "Standalone"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. New quiz takers join automatically.

    !!! tip "Segment on a specific answer or tag"

        To target a slice of quiz takers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. This is how you build audience-specific versions of any flow below.

### Learn the three controls you will reuse

Every flow below is built from three Klaviyo controls. They evaluate different data, so using the right one is what keeps a flow accurate.

- **Trigger filter** is checked once, at entry, and evaluates *only the triggering event's data* (so it exists only on metric-triggered flows). Use it to narrow the event itself, for example only enter the replenishment flow when the ordered item is a specific product.
- **Flow filter** (profile filter) is re-checked before every step and evaluates *profile properties and past actions*. Use it to keep a flow to quiz takers only (require your quiz-completion property to be `set`, the property flagged in [Know what the quiz sends](#know-what-the-quiz-sends) as present on every quiz taker) and to drop people who no longer qualify (has not `Placed Order` since starting the flow).
- **Conditional split** branches the path based on a profile property, a past action, or list membership. Use it to send one profile down a personalized path and everyone else down another, from the same trigger.

!!! note "Time delays behave differently with a set send-time"

    Back-to-back steps in Klaviyo fire at the same time, so you need explicit `Time delay` steps between emails. A plain delay counts in 24-hour blocks; a delay set to a specific time of day counts in calendar days. Keep this in mind when you schedule the 1h / 24h / 72h cadence.

## The flows

!!! info "Flows 2 to 5 need your store connected to Klaviyo"

    The cart, browse, replenishment and cross-sell flows trigger on `Started Checkout`, `Viewed Product` and `Placed Order`, which come from your store's native Klaviyo integration, not from RevenueHunt. Confirm connection 2 from the [prerequisites](#prerequisites) is in place. On Standalone these events are not available by default.

### 1. Results delivery (universal)

**Recommended for:** every quiz, every industry. This is the one flow no store should skip.

The transactional email that confirms the quiz result within seconds. It delivers the recommendation and links straight back to the results page, where products add to cart in one click.

- **Trigger:** `Added to segment` → your Quiz Takers segment. (If you route contacts to a Klaviyo list from the [email question's list selector](/how-to-guides/send-leads-to-klaviyo/#adding-quiz-contacts-to-klaviyo-list), you can trigger on the list instead.)
- **Reentry:** allow a returning quiz taker to get a fresh result email on every completion. The exact reentry setup differs by platform, so follow the method in [Send Email with Each Quiz Retake](/tutorials/follow-up-emails-klaviyo/#send-email-with-each-quiz-retake).
- **Personalize:** pull the recommendation and link to the results page using the tokens in [Personalizing every flow](#personalizing-every-flow-with-quiz-data). Use an [information recall](/how-to-guides/use-information-recalls/) style subject line: *"Your [skin type] routine is ready."*

<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">RESULTS DELIVERY · UNIVERSAL</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Added to segment: Quiz Takers</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · IMMEDIATE</text>
<text x="180" y="150" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Deliver results + cart link</text>
<line x1="180" y1="160" x2="180" y2="176" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,184 174,176 186,176" fill="#cbd5e1"/>
<rect x="95" y="184" width="170" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="205" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">Back to results page</text>
</svg>

This flow is covered end to end, including the downloadable HTML template, in [Sending Follow-up Emails via Klaviyo](/how-to-guides/send-leads-to-klaviyo/#sending-follow-up-emails-via-klaviyo). The rest of the flows below are what you build *on top* of it.

!!! tip "Turn off the app's built-in result email"

    Once this flow is live, deactivate the app's [result email notifications](/how-to-guides/send-result-emails/) so customers don't get two.

### 2. Cart abandonment (recommendation-aware)

**Recommended for:** Fashion, Cosmetics, and any store with a considered purchase. High value everywhere.

A quiz taker added a recommended product to cart but didn't check out. A generic "your cart is waiting" works; a quiz-aware version works better because it reframes the cart around *why* the product fits them.

- **Trigger:** metric `Started Checkout` (from your store's Klaviyo integration; some integrations label it `Checkout Started`).
- **Make it quiz-aware, two options:**
    - **Dedicated flow:** add a **flow filter** requiring your quiz-completion property `is set`, so only quiz takers stay in.
    - **Branch an existing flow:** if you already run a store-wide cart flow, add a `Conditional split` on your quiz-completion property `is set`. Quiz takers take the personalized (YES) path; everyone else keeps the standard copy. This avoids maintaining two flows.
- **Flow filter:** has not `Placed Order` since starting the flow (zero times), so buyers stop receiving it.
- **Timing:** three emails at roughly 1-4 hours, 24 hours, 72 hours.
- **Personalize:** open with the quiz angle instead of the cart, for example *"Based on your oily, breakout-prone profile, [Product X] is still your best match."* Pair the 72-hour email with a discount to recover price-sensitive shoppers.

<svg viewBox="0 0 360 446" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">CART ABANDONMENT</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Started Checkout</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Quiz taker · no order yet</text>
<line x1="180" y1="160" x2="180" y2="176" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,184 174,176 186,176" fill="#cbd5e1"/>
<rect x="60" y="184" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · 1-4h</text>
<text x="180" y="222" text-anchor="middle" font-size="12" font-weight="600" fill="#fff">Reference quiz answers</text>
<line x1="180" y1="232" x2="180" y2="248" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,256 174,248 186,248" fill="#cbd5e1"/>
<rect x="60" y="256" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="276" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · 24h</text>
<text x="180" y="294" text-anchor="middle" font-size="12" font-weight="600" fill="#fff">Reinforce the match</text>
<line x1="180" y1="304" x2="180" y2="320" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,328 174,320 186,320" fill="#cbd5e1"/>
<rect x="60" y="328" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="348" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · 72h</text>
<text x="180" y="366" text-anchor="middle" font-size="12" font-weight="600" fill="#fff">Add a discount</text>
<line x1="180" y1="376" x2="180" y2="392" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,400 174,392 186,392" fill="#cbd5e1"/>
<rect x="105" y="400" width="150" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="421" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">Cart recovered</text>
</svg>

### 3. Browse abandonment (tag-conditional)

**Recommended for:** Fashion and catalog-heavy stores where shoppers browse a lot before buying.

A quiz taker viewed a recommended product but never added it to cart. Lighter touch than cart abandonment.

- **Trigger:** metric `Viewed Product` (or `Active on Site`).
- **Flow filter:** your quiz-completion property `is set` (only quiz takers), and has not `Placed Order` or `Added to Cart` since starting the flow.
- **Timing:** one email at ~4 hours, an optional second at ~3 days.
- **Personalize:** add a `Conditional split` on a customer tag from the quiz so a customer never gets a recommendation that contradicts a different quiz answer. Reference both the viewed product and the stated need: *"You said you wanted lightweight coverage; here's a closer look at the matte finish."*

<svg viewBox="0 0 360 384" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">BROWSE ABANDONMENT</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Viewed Product</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Quiz taker · no cart/order</text>
<line x1="180" y1="160" x2="180" y2="176" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,184 174,176 186,176" fill="#cbd5e1"/>
<rect x="60" y="184" width="240" height="48" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
<text x="180" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">CONDITIONAL SPLIT</text>
<text x="180" y="222" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Split on customer tag</text>
<line x1="180" y1="232" x2="99" y2="256" stroke="#cbd5e1" stroke-width="2"/><polygon points="99,264 93,256 105,256" fill="#cbd5e1"/>
<line x1="180" y1="232" x2="261" y2="256" stroke="#cbd5e1" stroke-width="2"/><polygon points="261,264 255,256 267,256" fill="#cbd5e1"/>
<rect x="24" y="264" width="150" height="48" rx="8" fill="#2563eb"/>
<text x="99" y="284" text-anchor="middle" font-size="9" font-weight="700" fill="#bfdbfe" letter-spacing="0.6">EMAIL · 4h</text>
<text x="99" y="301" text-anchor="middle" font-size="11" font-weight="600" fill="#fff">Tag-matched pick</text>
<rect x="186" y="264" width="150" height="48" rx="8" fill="#2563eb"/>
<text x="261" y="284" text-anchor="middle" font-size="9" font-weight="700" fill="#bfdbfe" letter-spacing="0.6">EMAIL · 4h</text>
<text x="261" y="301" text-anchor="middle" font-size="11" font-weight="600" fill="#fff">Other tag pick</text>
<line x1="99" y1="312" x2="180" y2="330" stroke="#cbd5e1" stroke-width="2"/>
<line x1="261" y1="312" x2="180" y2="330" stroke="#cbd5e1" stroke-width="2"/>
<polygon points="180,336 174,328 186,328" fill="#cbd5e1"/>
<rect x="105" y="336" width="150" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="357" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">Re-engaged</text>
</svg>

### 4. Replenishment (cycle-timed)

**Recommended for:** Skincare, Haircare, Supplements, Food & drink, Pets, and any consumable with a predictable run-out.

The single highest-leverage flow for consumables: bring the customer back right before they run out.

- **Trigger:** metric `Placed Order`.
- **Trigger filter:** the ordered item is the consumable product (or in a product tag/collection). This reads the order event, so it belongs in the trigger filter.
- **Flow filter:** your quiz-completion property `is set` (only quiz takers), and has not `Placed Order` for that product again since starting the flow.
- **Timing:** a `Time delay` of roughly the consumption cycle × 0.8, so you land before they run out. A 30-day product triggers the email around day 22-24; a 60-day supply around day 48-50.
- **Personalize:** reference the product they bought and their quiz concern, for example *"Ready to restock your [concern] routine before it runs out?"* If your quiz asked about usage frequency, add a `Conditional split` on that answer to set different delays per profile.

<svg viewBox="0 0 360 432" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">REPLENISHMENT</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Placed Order</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">TRIGGER FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Ordered = consumable</text>
<line x1="180" y1="160" x2="180" y2="176" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,184 174,176 186,176" fill="#cbd5e1"/>
<rect x="60" y="184" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="222" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Quiz taker · no re-order</text>
<line x1="180" y1="232" x2="180" y2="248" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,256 174,248 186,248" fill="#cbd5e1"/>
<rect x="80" y="256" width="200" height="34" rx="17" fill="#fef3c7" stroke="#f59e0b"/>
<text x="180" y="277" text-anchor="middle" font-size="12" font-weight="600" fill="#92400e">Wait cycle × 0.8</text>
<line x1="180" y1="290" x2="180" y2="306" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,314 174,306 186,306" fill="#cbd5e1"/>
<rect x="60" y="314" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="334" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · BEFORE RUN-OUT</text>
<text x="180" y="352" text-anchor="middle" font-size="12" font-weight="600" fill="#fff">Reorder your [concern] routine</text>
<line x1="180" y1="362" x2="180" y2="378" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,386 174,378 186,378" fill="#cbd5e1"/>
<rect x="100" y="386" width="160" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="407" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">Repeat purchase</text>
</svg>

!!! tip "Use the quiz answer to time the delay"

    If the quiz captured "wash frequency" or "how often do you use this," split the flow on that answer property and give each branch its own delay. A daily user runs out faster than a weekly one, and the quiz already told you which they are.

### 5. Cross-sell / routine completion

**Recommended for:** Skincare and Haircare (routine and bundle categories). Skip it for Fashion, where a first purchase rarely implies a matching second.

After the first quiz-driven purchase, complete the routine. The customer who bought the cleanser for oily skin gets the matching serum and moisturizer for the same profile. It outperforms a generic bundle pitch because the recommendation comes from the customer's own answers.

- **Trigger:** metric `Placed Order`.
- **Flow filter:** your quiz-completion property `is set` (only quiz takers). Optionally exclude anyone who has already `Ordered Product` the item you're about to recommend.
- **Timing:** a `Time delay` of 7-14 days.
- **Branch by tag:** add a `Conditional split` on a customer tag to recommend the complementary product that matches their profile.

<svg viewBox="0 0 360 442" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">CROSS-SELL · ROUTINE COMPLETION</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Placed Order</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Quiz taker · not already bought</text>
<line x1="180" y1="160" x2="180" y2="176" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,184 174,176 186,176" fill="#cbd5e1"/>
<rect x="95" y="184" width="170" height="34" rx="17" fill="#fef3c7" stroke="#f59e0b"/>
<text x="180" y="205" text-anchor="middle" font-size="12" font-weight="600" fill="#92400e">Wait 7-14 days</text>
<line x1="180" y1="218" x2="180" y2="234" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,242 174,234 186,234" fill="#cbd5e1"/>
<rect x="60" y="242" width="240" height="48" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
<text x="180" y="262" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">CONDITIONAL SPLIT</text>
<text x="180" y="280" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Split on customer tag</text>
<line x1="180" y1="290" x2="99" y2="314" stroke="#cbd5e1" stroke-width="2"/><polygon points="99,322 93,314 105,314" fill="#cbd5e1"/>
<line x1="180" y1="290" x2="261" y2="314" stroke="#cbd5e1" stroke-width="2"/><polygon points="261,322 255,314 267,314" fill="#cbd5e1"/>
<rect x="24" y="322" width="150" height="48" rx="8" fill="#2563eb"/>
<text x="99" y="342" text-anchor="middle" font-size="9" font-weight="700" fill="#bfdbfe" letter-spacing="0.6">EMAIL</text>
<text x="99" y="359" text-anchor="middle" font-size="11" font-weight="600" fill="#fff">Matching product A</text>
<rect x="186" y="322" width="150" height="48" rx="8" fill="#2563eb"/>
<text x="261" y="342" text-anchor="middle" font-size="9" font-weight="700" fill="#bfdbfe" letter-spacing="0.6">EMAIL</text>
<text x="261" y="359" text-anchor="middle" font-size="11" font-weight="600" fill="#fff">Matching product B</text>
<line x1="99" y1="370" x2="180" y2="388" stroke="#cbd5e1" stroke-width="2"/>
<line x1="261" y1="370" x2="180" y2="388" stroke="#cbd5e1" stroke-width="2"/>
<polygon points="180,394 174,386 186,386" fill="#cbd5e1"/>
<rect x="105" y="394" width="150" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="415" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">AOV lift</text>
</svg>

### 6. Win-back (segment-conditional)

**Recommended for:** every industry. Only the timing shifts: ~60 days for impulse categories, ~120 for considered purchases.

Re-engage quiz takers who have gone quiet. The quiz tag is what makes a win-back feel personal instead of pleading.

- **Build the segment:** combine two conditions:
    - `Properties about someone` → your quiz-completion property `is set` (they took the quiz), and
    - `What someone has done` → `Placed Order` `zero times` in the last 60-120 days (they've gone quiet).
- **Trigger:** `Added to segment` → this inactive-quiz-takers segment.
- **Branch by tag:** a `Conditional split` on a customer tag so a `Curly + Dry` profile and a `Volume + Anti-Frizz` profile get different copy.
- **Timing:** one email on entry, a second ~14 days later with an incentive.

<svg viewBox="0 0 360 384" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">WIN-BACK</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · SEGMENT</text>
<text x="180" y="78" text-anchor="middle" font-size="11.5" font-weight="600" fill="#fff">Inactive quiz takers (60-120d)</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#f1f5f9" stroke="#94a3b8"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">CONDITIONAL SPLIT</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Split on customer tag</text>
<line x1="180" y1="160" x2="99" y2="184" stroke="#cbd5e1" stroke-width="2"/><polygon points="99,192 93,184 105,184" fill="#cbd5e1"/>
<line x1="180" y1="160" x2="261" y2="184" stroke="#cbd5e1" stroke-width="2"/><polygon points="261,192 255,184 267,184" fill="#cbd5e1"/>
<rect x="24" y="192" width="150" height="48" rx="8" fill="#2563eb"/>
<text x="99" y="212" text-anchor="middle" font-size="9" font-weight="700" fill="#bfdbfe" letter-spacing="0.6">EMAIL · ENTRY</text>
<text x="99" y="229" text-anchor="middle" font-size="11" font-weight="600" fill="#fff">Re-engage, tag A</text>
<rect x="186" y="192" width="150" height="48" rx="8" fill="#2563eb"/>
<text x="261" y="212" text-anchor="middle" font-size="9" font-weight="700" fill="#bfdbfe" letter-spacing="0.6">EMAIL · ENTRY</text>
<text x="261" y="229" text-anchor="middle" font-size="11" font-weight="600" fill="#fff">Re-engage, tag B</text>
<line x1="99" y1="240" x2="180" y2="258" stroke="#cbd5e1" stroke-width="2"/>
<line x1="261" y1="240" x2="180" y2="258" stroke="#cbd5e1" stroke-width="2"/>
<polygon points="180,264 174,256 186,256" fill="#cbd5e1"/>
<rect x="60" y="264" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="284" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · +14 DAYS</text>
<text x="180" y="302" text-anchor="middle" font-size="12" font-weight="600" fill="#fff">Incentive to return</text>
<line x1="180" y1="312" x2="180" y2="328" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,336 174,328 186,328" fill="#cbd5e1"/>
<rect x="105" y="336" width="150" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="357" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">Won back</text>
</svg>

## Which flows to build first, by industry

The architecture is universal; the cadence and priority shift by category. Start with the results email, then add the two flows your category leans on hardest. Layer the rest in as traffic grows.

| Industry | Build first (after results email) | Why |
|----------|-----------------------------------|-----|
| Skincare | Cross-sell + replenishment | Routines and refills drive repeat revenue |
| Haircare | Replenishment (6-8 week cycle) + cross-sell | Products run out on a predictable cycle |
| Supplements & wellness | Replenishment (30-day cycle) + win-back | Add a subscription nudge to the replenishment email |
| Cosmetics & makeup | Cart abandonment + seasonal cross-sell | Faster decision, more cart drop-off |
| Fashion & apparel | Cart abandonment + browse abandonment | Impulse buying, skip cross-sell |
| Food & drink | Replenishment + subscription nudge | Predictable consumption |
| Pets | Replenishment (food cycle) + cross-sell (accessories) | Recurring food, adjacent products |

The pattern: **consumables lean on replenishment and cross-sell; impulse categories lean on cart and browse abandonment.** Win-back matters everywhere.

## Personalizing every flow with quiz data

Whatever the flow, the personalization comes from the same lookups inside an `HTML` block.

=== "Shopify"

    - **Answer:** `{{ person|lookup:'ANSWER_BY_BLOCK-<blockRef>-<QuizID>' }}`
    - **Recommended product:** `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-<QuizID>'|lookup:'<slot>'|lookup:'0'|lookup:'title' }}` (swap `title` for `description`, `price`, `onlineUrl`, or `image`)
    - **Link to their results:** `#response-{{ person|lookup:'RESPONSE_ID-<QuizID>' }}`
    - **Branch on a tag:** in a `Conditional split`, `TAGS-<QuizID>` `contains` `<tag>`

    !!! tip "Let Quiz Copilot build it"

        Paste any template into [Quiz Copilot](/how-to-guides/use-quiz-copilot/) and ask it to restyle or trim the code for you, no developer required.

=== "Shopify (Legacy)"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url`, `_image_url`; the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "WooCommerce"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url`, `_image_url`; the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "Magento"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url`, `_image_url`; the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "BigCommerce"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url`, `_image_url`; the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "Standalone"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url`, `_image_url`; the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

The full token reference, the downloadable Klaviyo template, and worked examples are in [Use Quiz Data in Klaviyo Email Templates](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates).

## Common pitfalls

!!! warning "Watch for these"

    - **Two connections, not one.** RevenueHunt supplies the quiz properties and tags; `Started Checkout`, `Placed Order` and `Viewed Product` come from your store platform's own connection to Klaviyo. Without both, flows 2 to 5 have nothing to trigger on. On Standalone, those events do not exist by default.
    - **Confirm your exact property names.** Take a test quiz and check the resulting Klaviyo profile for the exact property names before you build, since they include your quiz ID.
    - **Set reentry deliberately.** The results email should re-send on retakes; behavior-triggered flows usually should not, to avoid over-emailing.
    - **Filter every behavior flow to quiz takers.** Otherwise your personalized copy reaches people who never took the quiz and the `lookup` tokens render empty.
    - **Lists must be Single Opt-in.** Quiz contacts can only be added to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) Klaviyo list.
    - **Special characters and delay.** New profiles can take a few minutes to appear, and accented characters (è, é, ê) can interfere with data transmission.

## Related reading

- [How to Send Quiz Leads to Klaviyo](/how-to-guides/send-leads-to-klaviyo/): the connection, segment and email-template mechanics in full.
- [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/): the step-by-step tutorial for your first flow.
- [Use Customer Tags](/how-to-guides/use-customer-tags/): how answers become the tags every flow segments on.
- [Ask for Marketing Consent](/how-to-guides/ask-for-marketing-consent/): capture consent in the quiz so you can email compliantly.
