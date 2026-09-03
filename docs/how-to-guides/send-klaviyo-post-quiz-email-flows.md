---
icon: material/lan
description: "Use quiz answers, customer tags and recommendations to build six automated Klaviyo emails that reach the customer in the weeks after the quiz."
---

# How to Build Post-Quiz Email Flows in Klaviyo

Most merchants stop at the results email. The quiz finishes, Klaviyo sends the recommendation, and that is the end of it. That email is worth building, but it reaches the customer once. This article covers the emails you can send in the weeks that follow.

The customer tells you their skin type, their main concern, their goal and their budget. No tracking pixel or purchase history gives you that. It is called [zero-party data](/how-to-guides/use-customer-tags/), because the customer gave it to you directly. Every answer is saved to a Klaviyo profile as soon as the quiz ends. You can filter a segment on any of those answers, then send a different email to each segment.

Across the RevenueHunt platform, **1 in 5 quiz-attributed orders is placed more than 30 days after the quiz**. A segmented Klaviyo send earns roughly **3x the revenue per recipient** of a generic one. The flows below are how you reach those customers.

!!! warning "You need two connections to Klaviyo, not one"

    These flows combine two data sources inside Klaviyo:

    1. **RevenueHunt → Klaviyo** sends the quiz *data*: answers, customer tags, recommended products. This is what you segment and personalize on.
    2. **Your store → Klaviyo** sends *what the customer does in your store*: `Started Checkout`, `Placed Order`, `Viewed Product`. These events start the cart, browse, reorder and cross-sell flows.

    You need both. The results email and the win-back flow need only connection 1. The other four flows need connection 2 as well. Set up connection 2 in Klaviyo, with your platform's own integration. See the prerequisites for your platform below.

## Prerequisites

=== "Shopify"

    1. Your quiz has an [email question](/reference/quiz-builder/questions/#email-address) and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) via OAuth with `Send Quiz Leads to Klaviyo Profiles` enabled.
    2. You have [tagged your quiz answers](/how-to-guides/use-customer-tags/) so answers arrive on the profile as customer tags.
    3. **Your Shopify store is connected to Klaviyo** through Klaviyo's native Shopify integration, so events like `Started Checkout`, `Placed Order` and `Viewed Product` reach Klaviyo. Without it, the other four flows have nothing to start them.

=== "Shopify (Legacy)"

    1. Your quiz has an email question, and you [connected RevenueHunt to Klaviyo](/how-to-guides/send-leads-to-klaviyo/#link-your-quiz-to-klaviyo) with your **Public API Key**. A **Private API Key** is also needed to add contacts to a list.
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

        A standalone quiz has no ecommerce platform feeding purchase and cart events into Klaviyo. Unless you send those events yourself through [Klaviyo's Track API](https://developers.klaviyo.com/en/reference/create_event), four of the flows have nothing to start them: cart, browse, reorder and cross-sell. On Standalone, build the **results email** and the **win-back** flow, which need only the RevenueHunt sync.

New to Klaviyo automations? Read Klaviyo's [Getting started with flows](https://help.klaviyo.com/hc/en-us/articles/115002774932) first.

## How the six emails fit together

Every quiz needs the **results email**, sent the moment the quiz finishes. **Five more emails** follow, and each one is sent when the customer does something specific. You do not need all six on day one. Build the results email first, then add the flows that matter most for your category. See [Which flows to build first, by industry](#which-flows-to-build-first-by-industry).

| Flow | Klaviyo trigger | When it fires | Needs store→Klaviyo? |
|------|-----------------|---------------|----------------------|
| [Results delivery](#1-results-email) | Added to segment (or list) | Immediately | No |
| [Cart abandonment](#2-abandoned-cart) | Metric: `Started Checkout` | 1-4h, 24h, 72h | Yes |
| [Browse abandonment](#3-viewed-but-did-not-add-to-cart) | Metric: `Viewed Product` | 4h, optional +3 days | Yes |
| [Replenishment](#4-time-to-reorder) | Metric: `Placed Order` | N days before run-out | Yes |
| [Cross-sell](#5-complete-the-routine) | Metric: `Placed Order` | 7-14 days after | Yes |
| [Win-back](#6-win-back-a-quiet-customer) | Added to segment | 60-120 days inactive | No |

Every flow reads the same quiz answers. Only two things change from one flow to the next: what starts it, and when it is sent.

## Set up once

These steps are the same for every flow.

### Know what the quiz sends

Every completion writes a set of `custom properties` to the Klaviyo profile. You reference these in segment definitions, conditional splits and email templates. The exact names include your quiz ID, so they are unique to your quiz.

=== "Shopify"

    Your quiz sends these custom properties:

    - `ANSWER_BY_BLOCK-<blockRef>-<QuizID>`: the answer to one question. Overwritten on each retake.
    - `ANSWERS_BY_BLOCK-<QuizID>`: present on every customer who finished the quiz. Use it to detect them.
    - `TAG-<TagName>-<QuizID>`: `true` for each customer tag your quiz logic applied. Your main segmentation lever.
    - `CHOICE-<choiceRef>-<QuizID>`: `true` for each choice the customer selected. The reference calls this the best property to segment on, because it does not change when you reword a choice.
    - `RECOMMENDATIONS_BY_SLOT-<QuizID>`: recommended products (title, price, image, URL). JSON object, appended on each retake.
    - `RESPONSE_ID-<QuizID>`: the unique response ID. Use it to link back to the results page.
    - `QUIZ_NAME-<QuizID>`: the quiz name. Handy in subject lines.

=== "Shopify (Legacy)"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every customer who finished the quiz. Use it to detect them.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `url`, `image_url`, `price`, `sku`, `id` or `variant_id`), where `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag. Present on the profile when that tag was applied.

=== "WooCommerce"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every customer who finished the quiz. Use it to detect them.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `url`, `image_url`, `price`, `sku`, `id` or `variant_id`), where `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag. Present on the profile when that tag was applied.

=== "Magento"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every customer who finished the quiz. Use it to detect them.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `url`, `image_url`, `price`, `sku`, `id` or `variant_id`), where `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag. Present on the profile when that tag was applied.

=== "BigCommerce"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every customer who finished the quiz. Use it to detect them.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `url`, `image_url`, `price`, `sku`, `id` or `variant_id`), where `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag. Present on the profile when that tag was applied.

=== "Standalone"

    Your quiz sends these custom properties:

    - `PERMALINK-<QuizID>`: present on every customer who finished the quiz. Use it to detect them.
    - `Q-<QuizID> <blockId>: <question text>`: the answer to one question.
    - `SLOT-<QuizID>: <slot name> - product_<n>_<field>`: a recommended product's field (`name`, `url`, `image_url`, `price`, `sku`, `id` or `variant_id`), where `<n>` starts at 0.
    - `T-<QuizID>: <tag>`: a customer tag. Present on the profile when that tag was applied.

!!! tip "Find your exact property names on a test profile"

    Do this before you build anything. Property names have changed between app versions, and the list above is a guide rather than a promise.

    Take a test quiz with a sample email, then open `Klaviyo > Audience > Profiles` and search for it. The profile shows every property your quiz sends, with the exact block references, slot names and quiz ID. Copy the names from there. See [Use Quiz Data in Klaviyo Email Templates](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates) for the full reference and the `{{ person|lookup:'...' }}` syntax.

### Create your `Quiz customers` segment

Every flow below uses this segment. It holds everyone who finished the quiz. Two flows use it as a trigger, results delivery and win-back, and the rest use it as a filter.

=== "Shopify"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `ANSWERS_BY_BLOCK-<QuizID>`, and set the condition to `is set`.
    3. Save. A new customer joins automatically.

    !!! tip "Segment on a specific answer or tag"

        To target some of those customers rather than all of them, filter on a specific value instead, for example `TAG-Color-Treated-<QuizID>` `is set`, or `ANSWER_BY_BLOCK-<blockRef>-<QuizID>` `equals` `Oily`. That is how you build a version of any flow below for one group of customers.

=== "Shopify (Legacy)"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. A new customer joins automatically.

    !!! tip "Segment on a specific answer or tag"

        To target some of those customers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. That is how you build a version of any flow below for one group of customers.

=== "WooCommerce"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. A new customer joins automatically.

    !!! tip "Segment on a specific answer or tag"

        To target some of those customers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. That is how you build a version of any flow below for one group of customers.

=== "Magento"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. A new customer joins automatically.

    !!! tip "Segment on a specific answer or tag"

        To target some of those customers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. That is how you build a version of any flow below for one group of customers.

=== "BigCommerce"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. A new customer joins automatically.

    !!! tip "Segment on a specific answer or tag"

        To target some of those customers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. That is how you build a version of any flow below for one group of customers.

=== "Standalone"

    1. In Klaviyo go to `Audience > Lists & Segments` and click `Create New > Segment`.
    2. Set the definition to `Properties about someone`, choose `PERMALINK-<QuizID>`, and set the condition to `is set`.
    3. Save. A new customer joins automatically.

    !!! tip "Segment on a specific answer or tag"

        To target some of those customers rather than all of them, filter on a specific value instead, for example `T-<QuizID>: Color-Treated` `is set`. That is how you build a version of any flow below for one group of customers.

### The three Klaviyo controls

Every flow below uses three Klaviyo controls. Each one reads different data, so pick the right one or the flow sends to the wrong people.

- **Trigger filter** is checked once, when someone enters the flow. It reads only the event that started the flow, so it exists only on flows started by an event. Use it to narrow the event itself, for example to enter the reorder flow only when the customer ordered one specific product.
- **Flow filter** is checked again before every step. It reads the profile and what the person has done before. Use it to keep the flow to customers who finished the quiz: require your quiz-completion property to be `set`. See [Know what the quiz sends](#know-what-the-quiz-sends). It also removes people who no longer qualify, such as anyone who has since placed an order.
- **Conditional split** sends people down two different paths. It reads a profile property, a past action, or list membership. Use it to send one group a personalized email and everyone else a standard one, from the same starting point.

!!! note "Time delays behave differently with a set send-time"

    Two steps with nothing between them are sent at the same time, so put a `Time delay` step between every email. A plain delay counts in 24-hour blocks. A delay set to a time of day counts in calendar days. Remember this when you schedule the 1 hour, 24 hour and 72 hour emails.

## The flows

!!! info "Flows 2 to 5 need your store connected to Klaviyo"

    The cart, browse, replenishment and cross-sell flows trigger on `Started Checkout`, `Viewed Product` and `Placed Order`, which come from your store's native Klaviyo integration, not from RevenueHunt. Confirm connection 2 from the [prerequisites](#prerequisites) is in place. On Standalone these events are not available by default.

### 1. Results email

**Recommended for:** every quiz, in every industry. No store should skip this one.

This email confirms the quiz result within seconds. It carries the recommendation and a link back to the results page, where the customer adds a product to the cart in one click.

- **Trigger:** `Added to segment` → your `Quiz customers` segment. (If you route contacts to a Klaviyo list from the [email question's list selector](/how-to-guides/send-leads-to-klaviyo/#adding-quiz-contacts-to-klaviyo-list), you can trigger on the list instead.)
- **Reentry:** let a returning customer get a fresh result email on every completion. The exact reentry setup differs by platform, so follow the method in [Send Email with Each Quiz Retake](/tutorials/follow-up-emails-klaviyo/#send-email-with-each-quiz-retake).
- **Personalize:** pull the recommendation and link to the results page using the tokens in [Personalizing every flow](#personalizing-every-flow-with-quiz-data). Use an [information recall](/how-to-guides/use-information-recalls/) style subject line: *"Your [skin type] routine is ready."*

<svg viewBox="0 0 360 230" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">RESULTS EMAIL</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Added to segment: Quiz customers</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#2563eb"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#bfdbfe" letter-spacing="0.8">EMAIL · IMMEDIATE</text>
<text x="180" y="150" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Deliver results + cart link</text>
<line x1="180" y1="160" x2="180" y2="176" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,184 174,176 186,176" fill="#cbd5e1"/>
<rect x="95" y="184" width="170" height="34" rx="17" fill="#dcfce7" stroke="#16a34a"/>
<text x="180" y="205" text-anchor="middle" font-size="12" font-weight="600" fill="#166534">Back to results page</text>
</svg>

[Sending Follow-up Emails via Klaviyo](/how-to-guides/send-leads-to-klaviyo/#sending-follow-up-emails-via-klaviyo) covers this flow from start to finish, and includes an HTML template you can download. The five flows below are built on top of it.

!!! tip "Turn off the app's built-in result email"

    Once this flow is live, deactivate the app's [result email notifications](/how-to-guides/send-result-emails/) so a customer does not get two.

### 2. Abandoned cart

**Recommended for:** Fashion, Cosmetics, and any store where customers think before they buy. It is worth building in every industry.

A customer added a recommended product to cart but did not complete the checkout. A plain "your cart is waiting" email works. An email that repeats their quiz answers works better, because it reminds them *why* the product suits them.

- **Trigger:** metric `Started Checkout` (from your store's Klaviyo integration, where some integrations label it `Checkout Started`).
- **Add the quiz data, in one of two ways:**
    - **Dedicated flow:** add a **flow filter** requiring your quiz-completion property `is set`, so only customers who finished the quiz stay in.
    - **Branch an existing flow:** if you already run a store-wide cart flow, add a `Conditional split` on your quiz-completion property `is set`. A customer who finished the quiz takes the personalized (YES) path. Everyone else keeps the standard copy. This avoids maintaining two flows.
- **Flow filter:** has not `Placed Order` since starting the flow (zero times), so buyers stop receiving it.
- **Timing:** three emails at roughly 1-4 hours, 24 hours, 72 hours.
- **Personalize:** start with the quiz answers rather than the cart. Add a discount to the 72-hour email, to win back a customer who is watching the price. For example: *"Your skin is oily and breaks out, so [Product X] is still your best match."*

<svg viewBox="0 0 360 446" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">CART ABANDONMENT</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Started Checkout</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Customer · no order yet</text>
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

### 3. Viewed but did not add to cart

**Recommended for:** Fashion, and any store with a large catalog, where customers browse for a while before they buy.

A customer viewed a recommended product but never added it to the cart. This is a gentler reminder than the abandoned cart email.

- **Trigger:** metric `Viewed Product` (or `Active on Site`).
- **Flow filter:** your quiz-completion property `is set` (only customers who finished the quiz), and has not `Placed Order` or `Added to Cart` since starting the flow.
- **Timing:** one email at ~4 hours, an optional second at ~3 days.
- **Personalize:** add a `Conditional split` on a customer tag from the quiz so a customer never gets a recommendation that contradicts a different quiz answer. Reference both the viewed product and the stated need, for example *"You said you wanted lightweight coverage. Here is a closer look at the matte finish."*

<svg viewBox="0 0 360 384" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">VIEWED, NOT ADDED TO CART</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Viewed Product</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Customer · no cart/order</text>
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

### 4. Time to reorder

**Recommended for:** Skincare, Haircare, Supplements, Food & drink, Pets, and any product a customer uses up on a predictable schedule.

If you sell a product that runs out, this flow returns the most revenue. It brings the customer back just before they need more.

- **Trigger:** metric `Placed Order`.
- **Trigger filter:** the ordered item is the consumable product (or in a product tag/collection). This reads the order event, so it belongs in the trigger filter.
- **Flow filter:** your quiz-completion property `is set` (only customers who finished the quiz), and has not `Placed Order` for that product again since starting the flow.
- **Timing:** set a `Time delay` to about 80% of the time the product lasts, so the email arrives before the customer runs out. A 30-day product sends around day 22 to 24. A 60-day supply sends around day 48 to 50.
- **Personalize:** reference the product they bought and their quiz concern. If your quiz asked about usage frequency, split on that answer to set a different delay per profile. For example: *"Ready to restock your [concern] routine before it runs out?"*

<svg viewBox="0 0 360 432" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">TIME TO REORDER</text>
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
<text x="180" y="222" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Customer · no re-order</text>
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

    If the quiz captured "wash frequency", or "how often do you use this", split the flow on that answer property. Give each branch its own delay. Someone who uses the product every day runs out sooner than someone who uses it once a week. The quiz already told you which they are.

### 5. Complete the routine

**Recommended for:** Skincare and Haircare, where products are sold as a routine or a bundle. Skip it for Fashion, where a first purchase rarely points to a matching second one.

After the first purchase, offer the rest of the routine. A customer who bought the cleanser for oily skin gets the serum and the moisturizer that match the same answers. This works better than a general bundle offer, because the recommendation comes from what the customer told you.

- **Trigger:** metric `Placed Order`.
- **Flow filter:** your quiz-completion property `is set` (only customers who finished the quiz). Optionally exclude anyone who has already `Ordered Product` the item you are about to recommend.
- **Timing:** a `Time delay` of 7-14 days.
- **Branch by tag:** add a `Conditional split` on a customer tag to recommend the complementary product that matches their profile.

<svg viewBox="0 0 360 442" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">COMPLETE THE ROUTINE</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · METRIC</text>
<text x="180" y="78" text-anchor="middle" font-size="12.5" font-weight="600" fill="#fff">Placed Order</text>
<line x1="180" y1="88" x2="180" y2="104" stroke="#cbd5e1" stroke-width="2"/><polygon points="180,112 174,104 186,104" fill="#cbd5e1"/>
<rect x="60" y="112" width="240" height="48" rx="8" fill="#fff" stroke="#cbd5e1"/>
<text x="180" y="132" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="0.8">FLOW FILTER</text>
<text x="180" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">Customer · not already bought</text>
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

### 6. Win back a quiet customer

**Recommended for:** every industry. Only the timing changes: about 60 days where customers buy on impulse, about 120 days where they take longer to decide.

Re-engage customers who have stopped buying. The quiz tag lets you name what they wanted, rather than only asking them to come back.

- **Build the segment:** combine two conditions:
    - `Properties about someone` → your quiz-completion property `is set` (they took the quiz), and
    - `What someone has done` → `Placed Order` `zero times` in the last 60 to 120 days, so they have gone quiet.
- **Trigger:** `Added to segment` → this segment of quiet customers.
- **Branch by tag:** a `Conditional split` on a customer tag so a `Curly + Dry` profile and a `Volume + Anti-Frizz` profile get different copy.
- **Timing:** one email when they join the segment, a second about 14 days later with a discount.

<svg viewBox="0 0 360 384" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:360px;height:auto;display:block;margin:18px auto 26px;border:1px solid #e2e8f0;border-radius:8px;background:#fff;font-family:system-ui,-apple-system,sans-serif;">
<text x="180" y="24" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b" letter-spacing="1.2">WIN BACK A QUIET CUSTOMER</text>
<rect x="60" y="40" width="240" height="48" rx="8" fill="#16161D"/>
<text x="180" y="60" text-anchor="middle" font-size="10" font-weight="700" fill="#94a3b8" letter-spacing="0.8">TRIGGER · SEGMENT</text>
<text x="180" y="78" text-anchor="middle" font-size="11.5" font-weight="600" fill="#fff">Inactive customers (60-120d)</text>
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

The set of flows is the same for every store. What changes is the order you build them in, and how often you send. Start with the results email, then add the two flows that matter most for your category. Add the rest as your traffic grows.

| Industry | Build first (after results email) | Why |
|----------|-----------------------------------|-----|
| Skincare | Cross-sell + replenishment | Customers reorder routines and refills |
| Haircare | Replenishment (6-8 week cycle) + cross-sell | Products run out on a predictable cycle |
| Supplements & wellness | Replenishment (30-day cycle) + win-back | Offer a subscription in the reorder email |
| Cosmetics & makeup | Cart abandonment + seasonal cross-sell | Customers decide fast, and abandon more carts |
| Fashion & apparel | Cart abandonment + browse abandonment | Customers buy on impulse, so skip cross-sell |
| Food & drink | Replenishment + subscription offer | Customers finish the product on a predictable schedule |
| Pets | Replenishment (food cycle) + cross-sell (accessories) | Food is reordered, and accessories sell alongside it |

**If you sell consumables, build replenishment and cross-sell first. If customers buy on impulse, build cart and browse abandonment first.** Every store benefits from win-back.

## Personalizing every flow with quiz data

Every flow personalizes the same way, with these lookups inside an `HTML` block.

=== "Shopify"

    - **Answer:** `{{ person|lookup:'ANSWER_BY_BLOCK-<blockRef>-<QuizID>' }}`
    - **Recommended product:** `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-<QuizID>'|lookup:'<slot>'|lookup:'0'|lookup:'title' }}` (swap `title` for `description`, `price`, `onlineUrl`, or `image`)
    - **Link to their results:** `#response-{{ person|lookup:'RESPONSE_ID-<QuizID>' }}`
    - **Branch on a tag:** in a `Conditional split`, `TAG-<TagName>-<QuizID>` `is set`

    !!! tip "Let Quiz Copilot build it"

        Paste any template into [Quiz Copilot](/how-to-guides/use-quiz-copilot/) and ask it to restyle or trim the code for you, no developer required.

=== "Shopify (Legacy)"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url` or `_image_url`, and note the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "WooCommerce"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url` or `_image_url`, and note the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "Magento"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url` or `_image_url`, and note the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "BigCommerce"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url` or `_image_url`, and note the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

=== "Standalone"

    - **Answer:** `{{ person|lookup:'Q-<QuizID> <blockId>: <question text>'|default:'' }}`
    - **Recommended product:** `{{ person|lookup:'SLOT-<QuizID>: <slot name> - product_0_name'|default:'' }}` (swap `product_0_name` for `_price`, `_sku`, `_url` or `_image_url`, and note the count starts at 0)
    - **Branch on a tag:** in a `Conditional split`, `T-<QuizID>: <tag>` `is set`, or in a template `{% if person|lookup:'T-<QuizID>: <tag>' %}...{% endif %}`

The full token reference, the downloadable Klaviyo template, and worked examples are in [Use Quiz Data in Klaviyo Email Templates](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates).

## Common pitfalls

!!! warning "Watch for these"

    - **Two connections, not one.** RevenueHunt supplies the quiz properties and tags. `Started Checkout`, `Placed Order` and `Viewed Product` come from your store platform's own connection to Klaviyo. Without both, flows 2 to 5 have nothing to trigger on. On Standalone, those events do not exist by default.
    - **Confirm your exact property names.** They include your quiz ID. Take a test quiz and read the property names off the resulting Klaviyo profile before you build.
    - **Decide who can enter a flow twice.** The results email should be sent again when a customer retakes the quiz. The other five flows usually should not, or the customer gets too many emails.
    - **Filter every flow to customers who finished the quiz.** Otherwise the copy reaches people who never took it, and the `lookup` tokens render empty.
    - **Lists must be Single Opt-in.** Quiz contacts can only be added to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) Klaviyo list.
    - **New profiles and accented characters.** A new profile can take a few minutes to appear. Accented characters (è, é, ê) can stop the data from arriving.

## Related reading

- [How to send quiz leads to Klaviyo](/how-to-guides/send-leads-to-klaviyo/): the connection, segment and email-template mechanics in full.
- [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/): the step-by-step tutorial for your first flow.
- [Use Customer Tags](/how-to-guides/use-customer-tags/): how answers become the tags every flow segments on.
- [Ask for Marketing Consent](/how-to-guides/ask-for-marketing-consent/): capture consent in the quiz so you can email compliantly.

---
This article explains the six emails you can send after a quiz, what starts each one, and which to build first for your industry.
