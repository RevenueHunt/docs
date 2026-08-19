---
description: "Measure the full paid-traffic funnel: ad click, landing page, quiz start, results page, purchase. Set up UTM parameters, GA4 quiz events, and per-response campaign attribution."
icon: material/filter-outline
---

# How to Track Your Ad to Purchase Funnel

You are paying for clicks and you want two answers: which ads produce orders, and where shoppers drop off. The path has four steps, and no single tool covers all four.

| Part of the funnel | What measures it | Setup |
|---|---|---|
| Ad click to landing page | UTM parameters plus your store analytics | 10 minutes, no code |
| Landing page to quiz start to results page | GA4 quiz events | One click, then a funnel exploration |
| Quiz to order | The app's [Analytics panel](/reference/quiz-builder/metrics/#analytics) | Already running |
| Ad campaign to an individual lead | Custom JS that captures UTMs into the response | Advanced, optional |

The last row is the one most stores skip, and the first three are enough for almost everyone. Follow the steps in order and stop when you have what you need.

Before you start:

- Publish the quiz on [its own page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page). One quiz per page keeps the funnel readable and is also how GA4 tracking works best.
- Install GA4 on your store. On Shopify, the Google & YouTube sales channel does this and sends the `purchase` event from checkout. You need that event for the last step of the funnel.

## Step 1: tag your ads with UTM parameters

UTM parameters are labels you add to the end of a link. Your analytics reads them and tells you which ad the shopper came from.

| Parameter | What to put in it | Example |
|---|---|---|
| `utm_source` | The platform | `facebook`, `google`, `tiktok` |
| `utm_medium` | The type of traffic | `cpc`, `paid_social` |
| `utm_campaign` | The campaign name | `hair_quiz_q3` |
| `utm_content` | The specific creative | `video_before_after` |
| `utm_term` | The keyword, search ads only | `hair+loss+treatment` |

1. Open Google's [Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/){target=_blank}.
2. Set the website URL to your quiz landing page.
3. Fill in `utm_source`, `utm_medium`, `utm_campaign` and `utm_content`.
4. Copy the generated URL and paste it into the ad.
5. Repeat for every creative, changing only `utm_content`.

!!! warning "One campaign per name, one creative per content"

    If every ad in a campaign shares the same `utm_content`, the reports collapse into a single row. You then cannot tell your creatives apart. Decide the naming scheme once, write it down, and use it everywhere. Lowercase, no spaces.

!!! tip "Do not tag your own internal links"

    UTM parameters are for traffic arriving from outside your site. Adding them to a link between two of your own pages restarts the session attribution. It then looks like the shopper arrived from an ad twice.

!!! info "Redirects keep the parameters"

    This applies to the `💎 Built for Shopify` version. If the quiz ends by [redirecting to another page](/how-to-guides/redirect-quiz-to-another-page/), the `utm_` parameters on the quiz page are carried through to the destination URL. Attribution survives the redirect, and parameters you set on the destination are never overwritten.

## Step 2: read ad to purchase in your store analytics

This is the outer measurement: what you spend against what you earn. It works as soon as the ads are tagged, with nothing else to configure.

=== "Shopify"

    1. In your Shopify admin, go to `Analytics → Reports`.
    2. Open **Sessions by UTM campaign** to see traffic per campaign.
    3. Open **Sales attributed to marketing** to see orders and revenue per campaign.
    4. Compare that revenue against your ad spend for the same period.

=== "Other platforms"

    1. In GA4, go to `Reports → Acquisition → Traffic acquisition`.
    2. Change the primary dimension to **Session campaign**.
    3. Add **Total revenue** and **Conversions** as columns.

At this point you know which ads make money. What you do not know is where the weaker ads lose shoppers. That is Step 3.

## Step 3: connect the quiz to Google Analytics

The quiz sends its own GA4 events, so the middle of the funnel becomes visible.

1. Open your quiz and go to the `Integrations` tab.
2. Click `Activate` in the Google Analytics section.
3. Click `Save`.
4. Take the quiz once, then check `Reports → Realtime` in GA4 to confirm the events arrive.

The events you get, without writing any code:

| Step in the funnel | Event name |
|---|---|
| Quiz started | `quiz_started_{quiz_name}` |
| Question viewed | `question_viewed_{question_title}` |
| Choice picked | `block_answered_{choice_text}` |
| Email submitted | `email_lead_{quiz_name}` and `generate_lead` |
| Results page reached | `results_page_viewed_{results_page_title}` |
| Product clicked | `product_clicked_{product_name}` |
| Product added to cart | `product_added_to_cart_{product_name}` |
| Checkout started | `proceed_to_checkout_{quiz_name}` |

!!! warning "The event name includes the quiz name"

    Events arrive as `quiz_started_my_quiz`, not as a plain `quiz_started`. Search by the prefix under `Reports → Engagement → Events`. This is deliberate: it lets you read per-quiz numbers straight from the Event name report without registering custom dimensions.

Full setup details, including the legacy and non-Shopify platforms, custom dimensions, and custom events: [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

## Step 4: build the funnel in GA4

1. In GA4, go to `Explore` and create a new **Funnel exploration**.
2. Step 1: `page_view`, with a condition on the landing page path.
3. Step 2: `quiz_started_{your_quiz_name}`.
4. Step 3: `results_page_viewed_{your_results_page_title}`.
5. Step 4: `purchase`.
6. Set **Breakdown** to **Session campaign** so the funnel splits by ad.
7. Switch on **Show elapsed time** to see where shoppers stall, not only where they leave.

The drop between each pair of steps is the number you act on. The `purchase` event comes from your store's own GA4 setup, not from the quiz, so if step 4 is empty check that first.

!!! warning "GA4 event tracking reliability"

    Since Google moved from Universal Analytics to GA4, event tracking reliability has dropped. The implementation can be correct and the events can fire as expected, and GA4 can still fail to read, process, or report them accurately. If that happens, contact Google Support: the issue is on their end.

## Step 5: attach the campaign to each individual response (optional)

Steps 1 to 4 give you totals per campaign. This step puts the campaign on each individual quiz response, so you can tell which ad produced a specific lead.

1. Open the first question of your quiz and expand its `Custom JS` section.
2. Paste the following. No `<script>` tags.

```javascript
const p = new URLSearchParams(window.location.search);
actions.setAnswers({
  'hidden-utm-source': p.get('utm_source') || '',
  'hidden-utm-campaign': p.get('utm_campaign') || '',
  'hidden-utm-content': p.get('utm_content') || '',
  'hidden-full-url': window.location.href
});
```

These values travel with the response and arrive in your [webhook](/how-to-guides/send-leads-to-webhooks/) payload under `answersByBlock`. That is where you join campaign to lead in your own reporting.

Guides: [Add JavaScript](/how-to-guides/add-javascript/) and [Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/).

## Reading the funnel: what each drop means

| Where the drop is | Likely cause | Where to look |
|---|---|---|
| Clicks, but few `page_view` | Slow page, or a redirect stripping the parameters | [Check quiz loading speed](/how-to-guides/check-quiz-loading-speed/) |
| Page views, but few `quiz_started` | The quiz is too far down the page, or the call to action is weak | [Get more quiz engagement](/customer-success/how-to-get-more-quiz-engagement/) |
| Quiz starts, but few `results_page_viewed` | Too many questions, or one question is causing the drop | The `Drop-off` panel in [Metrics](/reference/quiz-builder/metrics/), and [Reduce drop-off](/customer-success/reduce-dropoff/) |
| Results reached, but few orders | The recommendations or the offer, not the funnel | [Why your quiz is not converting](/customer-success/quiz-not-converting/) |

## Related

- [Track Quiz Revenue](/how-to-guides/track-quiz-revenue/): the quiz to order half, native and already running.
- [Integrate Meta Pixel](/how-to-guides/integrate-meta-pixel/): the same events sent to Meta, for optimising the ads themselves.
- [Use Quiz Data to Lower Your Ad Costs](/customer-success/use-quiz-data-for-ads/): what to do with the data once you can read it.
