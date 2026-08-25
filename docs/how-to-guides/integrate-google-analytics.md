---
description: "Learn how to integrate Google Analytics with your RevenueHunt quiz to track user engagement and minimize abandonment rates."
icon: material/google-analytics
---

# How to Track Quiz Performance with Google Analytics

=== "Shopify"

    Google Analytics shows you how customers use your quizzes. Linking the two can give you data on customer interactions, pinpoint engagement issues, and help minimize abandonment rates.

    The `💎 Built for Shopify` version of the RevenueHunt app has native GA4 event tracking built in.

    This article will guide you through the process of connecting your quiz to Google Analytics and tracking quiz events.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/8P-kANzya2g?si=L-rMRoSRsdbwSgof" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.



=== "Shopify (Legacy)"

    To track quiz performance with Google Analytics in Shopify (legacy), add custom JavaScript tracking. It reports quiz events and customer interactions.

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "WooCommerce"

    To track quiz performance with Google Analytics in WooCommerce, add custom JavaScript tracking. It reports quiz events and customer interactions.

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "Magento"

    To track quiz performance with Google Analytics in Magento, add custom JavaScript tracking. It reports quiz events and customer interactions.

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "BigCommerce"

    To track quiz performance with Google Analytics in BigCommerce, add custom JavaScript tracking. It reports quiz events and customer interactions.

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "Standalone"

    To track quiz performance with Google Analytics in a Standalone version of RevenueHunt app, add custom JavaScript tracking. It reports quiz events and customer interactions.

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.



## Connect quiz to Google Analytics

=== "Shopify"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instructions in [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) to set this up.

    1. Make sure you have set up the GA4 tracking on your website.

        !!! tip

            To connect your website to Google Analytics, or to find your GA tracking code, see the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).
    1. Go to your quiz and click on the [Integrations](/reference/quiz-builder/connect-integrations/) tab.
    2. Click on the `Activate` button in the Google Analytics section.
        ![how to integrate ga4 built for shopify revenuehunt app](/images/how_to_integrate_ga4_shopify_v2.png)
    3. Click `Save` to confirm the changes.
    4. Once activated the quiz will connect to the GA4 tracking code already present on your website. It can take up to 72 hours for the data to start appearing in your Meta portal.

    ??? tip "Optional: Add Custom Trackers"

        The native integration above already sends the standard events (quiz started, question viewed, choice answered, results viewed, product clicked, add to cart, and so on). To track **custom** events on top of those, use the quiz's built-in **Custom JS** section. It runs plain JavaScript (no `<script>` tags) and gives you a global `window.quiz` object.

        !!! warning

            The legacy `prqQuizCallback` and `prqSlideCallback` callbacks do **not** exist in the `💎 Built for Shopify` version. Use `window.quiz` instead. Custom JS only runs in the preview or live quiz, not inside the builder.

        **Prerequisite:** GA4 (`gtag.js`) must already be installed on your store, the same requirement as the native integration above.

        **Track every answer.** Open the **first question** in the quiz builder, expand its **Custom JS** section, and assign a handler to `window.quiz.onChange`. It fires after every answer and stays registered for the rest of the quiz:

        ```javascript
        // Fires after every answer the customer gives
        window.quiz.onChange = function (event) {
          gtag('event', 'quiz_question_answered', {
            event_category: 'quiz',
            question_ref: event.questionRef,
            // selectedLabel is the readable choice text - no choice-ID mapping needed
            answer: event.selectedLabel || event.value
          });
        };
        ```

        The `event` object contains: `questionRef`, `blockRef`, `type`, `choicesRefs`, `value`, `isValid`, `selectedIndex` and `selectedLabel`.

        **Track quiz completion.** Open the **results page** **Custom JS** section and call `gtag()` directly. It runs when the results page renders:

        ```javascript
        gtag('event', 'quiz_completed', { event_category: 'quiz' });
        ```

        **Monitor and adjust.** Check `Reports → Engagement → Events` (or `Realtime`) in GA4 to confirm your custom events are coming through.



=== "Shopify (Legacy)"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instructions in [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) to set this up.

    To track quiz events in Google Analytics, add custom JavaScript to your website, ideally on the page that holds the quiz.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: See [How to Use the Callback Function](/how-to-guides/use-callback-function/) for how it works and how it tracks custom events.

    2. **Embed the Custom Script**: Add the script below to the page that holds the quiz. To load it everywhere, put it in your theme's main template. Your GA4 `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`:
        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            gtag('event', 'quiz_completed', {
                event_category: 'quiz',
                quiz_name: quizResponse.quiz.attributes.name,
                quiz_id: quizResponse.quizid
            });
        }
        </script>
        ```

    3. **Customize Event Tracking**: That example fires once, on completion. To track each answer instead, add `prqSlideCallback`. It fires on every answered question. The snippet below also maps the selected choice IDs to readable labels. The choices and the selected values both live in the slide object:
        ```html
        <script>
        // Fires each time a customer answers a question
        function prqSlideCallback(event) {
            var slide = event && event.slide;
            if (!slide || !slide.attributes) return;

            var choices  = (slide.attributes.choices && slide.attributes.choices.data) || [];
            var selected = slide.attributes.values || [];

            // Turn selected choice IDs into readable labels
            // (text/number questions have no choices, so the raw value passes through)
            var labels = selected.map(function (val) {
                var match = choices.filter(function (c) { return c.id === val; })[0];
                return match ? match.attributes.label : val;
            });

            gtag('event', 'quiz_question_answered', {
                event_category: 'quiz',
                quiz_name: event.quiz.attributes.name,
                question_title: slide.attributes.title,
                answer: labels.join(', ')
            });
        }
        </script>
        ```

    4. **Monitor and Adjust**: Once implemented, regularly check your Google Analytics dashboard to ensure events are being tracked correctly. Adjust the tracking code as needed based on your specific requirements.


=== "WooCommerce"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instructions in [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) to set this up.

    To track quiz events in Google Analytics, add custom JavaScript to your website, ideally on the page that holds the quiz.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: See [How to Use the Callback Function](/how-to-guides/use-callback-function/) for how it works and how it tracks custom events.

    2. **Embed the Custom Script**: Add the script below to the page that holds the quiz. To load it everywhere, put it in your theme's main template. Your GA4 `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`:
        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            gtag('event', 'quiz_completed', {
                event_category: 'quiz',
                quiz_name: quizResponse.quiz.attributes.name,
                quiz_id: quizResponse.quizid
            });
        }
        </script>
        ```

    3. **Customize Event Tracking**: That example fires once, on completion. To track each answer instead, add `prqSlideCallback`. It fires on every answered question. The snippet below also maps the selected choice IDs to readable labels. The choices and the selected values both live in the slide object:
        ```html
        <script>
        // Fires each time a customer answers a question
        function prqSlideCallback(event) {
            var slide = event && event.slide;
            if (!slide || !slide.attributes) return;

            var choices  = (slide.attributes.choices && slide.attributes.choices.data) || [];
            var selected = slide.attributes.values || [];

            // Turn selected choice IDs into readable labels
            // (text/number questions have no choices, so the raw value passes through)
            var labels = selected.map(function (val) {
                var match = choices.filter(function (c) { return c.id === val; })[0];
                return match ? match.attributes.label : val;
            });

            gtag('event', 'quiz_question_answered', {
                event_category: 'quiz',
                quiz_name: event.quiz.attributes.name,
                question_title: slide.attributes.title,
                answer: labels.join(', ')
            });
        }
        </script>
        ```

    4. **Monitor and Adjust**: Once implemented, regularly check your Google Analytics dashboard to ensure events are being tracked correctly. Adjust the tracking code as needed based on your specific requirements.

=== "Magento"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instructions in [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) to set this up.

    To track quiz events in Google Analytics, add custom JavaScript to your website, ideally on the page that holds the quiz.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: See [How to Use the Callback Function](/how-to-guides/use-callback-function/) for how it works and how it tracks custom events.

    2. **Embed the Custom Script**: Add the script below to the page that holds the quiz. To load it everywhere, put it in your theme's main template. Your GA4 `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`:
        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            gtag('event', 'quiz_completed', {
                event_category: 'quiz',
                quiz_name: quizResponse.quiz.attributes.name,
                quiz_id: quizResponse.quizid
            });
        }
        </script>
        ```

    3. **Customize Event Tracking**: That example fires once, on completion. To track each answer instead, add `prqSlideCallback`. It fires on every answered question. The snippet below also maps the selected choice IDs to readable labels. The choices and the selected values both live in the slide object:
        ```html
        <script>
        // Fires each time a customer answers a question
        function prqSlideCallback(event) {
            var slide = event && event.slide;
            if (!slide || !slide.attributes) return;

            var choices  = (slide.attributes.choices && slide.attributes.choices.data) || [];
            var selected = slide.attributes.values || [];

            // Turn selected choice IDs into readable labels
            // (text/number questions have no choices, so the raw value passes through)
            var labels = selected.map(function (val) {
                var match = choices.filter(function (c) { return c.id === val; })[0];
                return match ? match.attributes.label : val;
            });

            gtag('event', 'quiz_question_answered', {
                event_category: 'quiz',
                quiz_name: event.quiz.attributes.name,
                question_title: slide.attributes.title,
                answer: labels.join(', ')
            });
        }
        </script>
        ```

    4. **Monitor and Adjust**: Once implemented, regularly check your Google Analytics dashboard to ensure events are being tracked correctly. Adjust the tracking code as needed based on your specific requirements.

=== "BigCommerce"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instructions in [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) to set this up.

    To track quiz events in Google Analytics, add custom JavaScript to your website, ideally on the page that holds the quiz.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: See [How to Use the Callback Function](/how-to-guides/use-callback-function/) for how it works and how it tracks custom events.

    2. **Embed the Custom Script**: Add the script below to the page that holds the quiz. To load it everywhere, put it in your theme's main template. Your GA4 `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`:
        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            gtag('event', 'quiz_completed', {
                event_category: 'quiz',
                quiz_name: quizResponse.quiz.attributes.name,
                quiz_id: quizResponse.quizid
            });
        }
        </script>
        ```

    3. **Customize Event Tracking**: That example fires once, on completion. To track each answer instead, add `prqSlideCallback`. It fires on every answered question. The snippet below also maps the selected choice IDs to readable labels. The choices and the selected values both live in the slide object:
        ```html
        <script>
        // Fires each time a customer answers a question
        function prqSlideCallback(event) {
            var slide = event && event.slide;
            if (!slide || !slide.attributes) return;

            var choices  = (slide.attributes.choices && slide.attributes.choices.data) || [];
            var selected = slide.attributes.values || [];

            // Turn selected choice IDs into readable labels
            // (text/number questions have no choices, so the raw value passes through)
            var labels = selected.map(function (val) {
                var match = choices.filter(function (c) { return c.id === val; })[0];
                return match ? match.attributes.label : val;
            });

            gtag('event', 'quiz_question_answered', {
                event_category: 'quiz',
                quiz_name: event.quiz.attributes.name,
                question_title: slide.attributes.title,
                answer: labels.join(', ')
            });
        }
        </script>
        ```

    4. **Monitor and Adjust**: Once implemented, regularly check your Google Analytics dashboard to ensure events are being tracked correctly. Adjust the tracking code as needed based on your specific requirements.

=== "Standalone"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instructions in [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) to set this up.

    To track quiz events in Google Analytics, add custom JavaScript to your website, ideally on the page that holds the quiz.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: See [How to Use the Callback Function](/how-to-guides/use-callback-function/) for how it works and how it tracks custom events.

    2. **Embed the Custom Script**: Add the script below to the page that holds the quiz. To load it everywhere, put it in your theme's main template. Your GA4 `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`:
        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            gtag('event', 'quiz_completed', {
                event_category: 'quiz',
                quiz_name: quizResponse.quiz.attributes.name,
                quiz_id: quizResponse.quizid
            });
        }
        </script>
        ```

    3. **Customize Event Tracking**: That example fires once, on completion. To track each answer instead, add `prqSlideCallback`. It fires on every answered question. The snippet below also maps the selected choice IDs to readable labels. The choices and the selected values both live in the slide object:
        ```html
        <script>
        // Fires each time a customer answers a question
        function prqSlideCallback(event) {
            var slide = event && event.slide;
            if (!slide || !slide.attributes) return;

            var choices  = (slide.attributes.choices && slide.attributes.choices.data) || [];
            var selected = slide.attributes.values || [];

            // Turn selected choice IDs into readable labels
            // (text/number questions have no choices, so the raw value passes through)
            var labels = selected.map(function (val) {
                var match = choices.filter(function (c) { return c.id === val; })[0];
                return match ? match.attributes.label : val;
            });

            gtag('event', 'quiz_question_answered', {
                event_category: 'quiz',
                quiz_name: event.quiz.attributes.name,
                question_title: slide.attributes.title,
                answer: labels.join(', ')
            });
        }
        </script>
        ```

    4. **Monitor and Adjust**: Once implemented, regularly check your Google Analytics dashboard to ensure events are being tracked correctly. Adjust the tracking code as needed based on your specific requirements.


## Complete custom tracking script (GA4)

!!! info "For the Shopify (Legacy), WooCommerce, Magento, BigCommerce and Standalone versions"

    This script uses the [callback functions](/how-to-guides/use-callback-function/). The `💎 Built for Shopify` quiz does not use callbacks. Use its results page **Custom JS** and `window.quiz` object instead.

To send your own clearly named GA4 events rather than the built-in `view` and `click` events, use the script below. It tracks **quiz start**, **every answer**, the **results page**, each **recommended product**, and **add to cart**, each as its own GA4 event with descriptive parameters.

**Before you start:**

- Your GA4 `gtag.js` snippet must load **before** RevenueHunt's `embed.js`.
- Place the script on the page where the quiz is embedded (or sitewide in your theme).
- The built-in tracking and this script both fire when your GA Measurement ID is saved in the quiz backend. To avoid double counting, either leave the Measurement ID out and use this script alone, or remove the events you do not want.

```html
<script>
(function () {
  var quizStarted   = false;
  var productsBySku = {}; // captured on the results page, used to enrich add-to-cart

  // Fires every time a customer answers a question.
  // The first time it runs, it doubles as the "quiz started" signal.
  window.prqSlideCallback = function (event) {
    var slide = event && event.slide;
    if (!slide || !slide.attributes) return;

    if (!quizStarted) {
      quizStarted = true;
      gtag('event', 'quiz_start', { quiz_name: event.quiz.attributes.name });
    }

    var choices  = (slide.attributes.choices && slide.attributes.choices.data) || [];
    var selected = slide.attributes.values || [];

    // Map selected choice IDs to readable labels (raw value passes through for text/number questions)
    var labels = selected.map(function (val) {
      var match = choices.filter(function (c) { return c.id === val; })[0];
      return match ? match.attributes.label : val;
    });

    gtag('event', 'quiz_question_answered', {
      quiz_name:      event.quiz.attributes.name,
      // strip any unresolved recall token like {{slide:x1i0d83}} from the title
      question_title: (slide.attributes.title || '').replace(/\{\{slide:\w+\}\}/g, '').trim(),
      answer:         labels.join(', ')
    });
  };

  // Fires once, when the customer reaches the results page.
  window.prqQuizCallback = function (response) {
    var quizName   = response.quiz.attributes.name;
    var result     = response.response.attributes.selected_result;
    var resultName = (result && result.data) ? result.data.attributes.name : '';
    var products   = response.response.attributes.recommended_products || [];

    // One event for reaching the results page
    gtag('event', 'quiz_results', {
      quiz_name:     quizName,
      result_name:   resultName,
      product_count: products.length
    });

    // One event per recommended product (see the note below on why these are separate)
    products.forEach(function (p) {
      productsBySku[p.sku] = p; // stash for add-to-cart enrichment
      gtag('event', 'quiz_product_recommended', {
        quiz_name:     quizName,
        result_name:   resultName,
        product_name:  p.name,
        product_sku:   p.sku,
        product_price: p.price,
        product_id:    p.origin_id,
        variant_id:    p.variant_id
      });
    });
  };

  // Fires when a customer adds a recommended product to the cart from the results page.
  // The add-to-cart event carries sku / origin_id / variant_id; name & price are
  // enriched from the products captured above.
  window.prqAddOneToCartCallback = function (event) {
    var p = productsBySku[event.sku] || {};
    gtag('event', 'quiz_add_to_cart', {
      product_name:  p.name  || '',
      product_sku:   event.sku,
      product_price: p.price || '',
      product_id:    event.originId,
      variant_id:    event.variantId
    });
  };
})();
</script>
```

!!! note "Why `quiz_results` and `quiz_product_recommended` are separate"

    A results page can recommend more than one product. Firing the results event once (with `result_name`) and a separate per-product event keeps your "reached results" count accurate. If you instead fire a single combined event per product, your results count multiplies by the number of products shown.

The parameters above (`quiz_name`, `question_title`, `answer`, `product_name`, and so on) are standard GA4 event parameters. To use them in GA4 reports and Explorations, register the ones you need as **custom dimensions** under `Admin → Custom definitions`.

## Track customer behavior (events)

=== "Shopify"

    Quiz usage and customer behavior then appear in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_shopifyv2_events.png)

    !!! warning "Data may take up to 72 hours to appear"

        If the events do not appear, check the `View realtime` tab in GA4. Google Analytics can take up to 72 hours to process the data.

    An event fires at each step: quiz start, question view, choice, results page, add to cart, and cart or checkout. For more on a single event, click on the specific Event name.

    | Trigger                                                             | Event Name | Event Parameters    |
    |---------------------------------------------------------------------|------------|-----------------|
    | User starts a quiz (clicks on the button of the first question or the welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question                                               | question_viewed_{question_title} | question_title |
    | User clicks on a choice or selects an option from a dropdown        | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | User responds to the email question                                 | email_lead_{quiz_name} | quiz_name |
    | User responds to the phone question                                 | phone_lead_{quiz_name} | quiz_name |
    | User gets to results page                                           | results_page_viewed_{results_page_title} | results_page_title |
    | User completes the quiz (conversion event)                          | generate_lead | quiz_name |
    | Customer clicks on product (view product button or image)           | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart (via "add to cart" or "add all to cart" buttons) | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart/checkout                                  | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes quiz                                               | quiz_retake_quiz_{quiz_name} | quiz_name |


=== "Shopify (Legacy)"

    Customer events then appear in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_shopifyv2_events.png)

    **Built-in events (no script required).** Click `Activate` in your quiz's `Connect → Google Analytics` section. The quiz then sends GA4-native events to whichever GA4 property your store's `gtag.js` is configured with. No Measurement ID is needed. Your `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`. Each event name is built from its main parameter, so the value shows up directly in GA4's `Event name` report. To use the other parameters (like `question_title` or `question_ref`) as report columns, register them as **custom dimensions** under `Admin → Custom definitions`:

    | Trigger | Event Name | Event Parameters |
    |---------|------------|------------------|
    | User starts a quiz (clicks the button on the first / welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question | question_viewed_{question_title} | question_title |
    | User clicks a choice or selects a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | User answers the email question | email_lead_{quiz_name} | quiz_name |
    | User answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | User reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | User completes the quiz (conversion event) | generate_lead | quiz_name |
    | Customer clicks a product (view-product button or image) | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart ("add to cart" / "add all to cart") | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart / checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! note "Same events as the Built for Shopify version"

        This is the exact GA4 event catalog the `💎 Built for Shopify` quiz sends (see the Shopify tab above). The older `view` / `click` / `submit` / `recommendation` events (with `event_category` / `event_label`) are no longer sent.

    !!! info "`generate_lead` is a standard GA4 conversion event"

        Unlike the others, `generate_lead` keeps its plain name (no `_{…}` suffix) so GA4 can treat it as a conversion. Mark it as a **key event** under `Admin → Events` if you want it counted as a conversion.

    !!! warning "Question titles may contain a recall token"

        The `question_title` parameter, and the `question_viewed_{question_title}` event name, use the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token such as `{{slide:x1i0d83}}`. The token reaches GA4, not the answer. The token is stable. It never changes for a customer, or when you edit the quiz, so it works as a grouping key. It is not readable, though. The same applies to `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/). Strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If the events do not appear, check that your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.


=== "WooCommerce"

    Customer events then appear in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    **Built-in events (no script required).** Click `Activate` in your quiz's `Connect → Google Analytics` section. The quiz then sends GA4-native events to whichever GA4 property your store's `gtag.js` is configured with. No Measurement ID is needed. Your `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`. Each event name is built from its main parameter, so the value shows up directly in GA4's `Event name` report. To use the other parameters (like `question_title` or `question_ref`) as report columns, register them as **custom dimensions** under `Admin → Custom definitions`:

    | Trigger | Event Name | Event Parameters |
    |---------|------------|------------------|
    | User starts a quiz (clicks the button on the first / welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question | question_viewed_{question_title} | question_title |
    | User clicks a choice or selects a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | User answers the email question | email_lead_{quiz_name} | quiz_name |
    | User answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | User reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | User completes the quiz (conversion event) | generate_lead | quiz_name |
    | Customer clicks a product (view-product button or image) | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart ("add to cart" / "add all to cart") | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart / checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! note "Same events as the Built for Shopify version"

        This is the exact GA4 event catalog the `💎 Built for Shopify` quiz sends (see the Shopify tab above). The older `view` / `click` / `submit` / `recommendation` events (with `event_category` / `event_label`) are no longer sent.

    !!! info "`generate_lead` is a standard GA4 conversion event"

        Unlike the others, `generate_lead` keeps its plain name (no `_{…}` suffix) so GA4 can treat it as a conversion. Mark it as a **key event** under `Admin → Events` if you want it counted as a conversion.

    !!! warning "Question titles may contain a recall token"

        The `question_title` parameter, and the `question_viewed_{question_title}` event name, use the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token such as `{{slide:x1i0d83}}`. The token reaches GA4, not the answer. The token is stable. It never changes for a customer, or when you edit the quiz, so it works as a grouping key. It is not readable, though. The same applies to `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/). Strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If the events do not appear, check that your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

=== "Magento"

    Customer events then appear in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    **Built-in events (no script required).** Click `Activate` in your quiz's `Connect → Google Analytics` section. The quiz then sends GA4-native events to whichever GA4 property your store's `gtag.js` is configured with. No Measurement ID is needed. Your `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`. Each event name is built from its main parameter, so the value shows up directly in GA4's `Event name` report. To use the other parameters (like `question_title` or `question_ref`) as report columns, register them as **custom dimensions** under `Admin → Custom definitions`:

    | Trigger | Event Name | Event Parameters |
    |---------|------------|------------------|
    | User starts a quiz (clicks the button on the first / welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question | question_viewed_{question_title} | question_title |
    | User clicks a choice or selects a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | User answers the email question | email_lead_{quiz_name} | quiz_name |
    | User answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | User reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | User completes the quiz (conversion event) | generate_lead | quiz_name |
    | Customer clicks a product (view-product button or image) | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart ("add to cart" / "add all to cart") | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart / checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! note "Same events as the Built for Shopify version"

        This is the exact GA4 event catalog the `💎 Built for Shopify` quiz sends (see the Shopify tab above). The older `view` / `click` / `submit` / `recommendation` events (with `event_category` / `event_label`) are no longer sent.

    !!! info "`generate_lead` is a standard GA4 conversion event"

        Unlike the others, `generate_lead` keeps its plain name (no `_{…}` suffix) so GA4 can treat it as a conversion. Mark it as a **key event** under `Admin → Events` if you want it counted as a conversion.

    !!! warning "Question titles may contain a recall token"

        The `question_title` parameter, and the `question_viewed_{question_title}` event name, use the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token such as `{{slide:x1i0d83}}`. The token reaches GA4, not the answer. The token is stable. It never changes for a customer, or when you edit the quiz, so it works as a grouping key. It is not readable, though. The same applies to `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/). Strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If the events do not appear, check that your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

=== "BigCommerce"

    Customer events then appear in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    **Built-in events (no script required).** Click `Activate` in your quiz's `Connect → Google Analytics` section. The quiz then sends GA4-native events to whichever GA4 property your store's `gtag.js` is configured with. No Measurement ID is needed. Your `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`. Each event name is built from its main parameter, so the value shows up directly in GA4's `Event name` report. To use the other parameters (like `question_title` or `question_ref`) as report columns, register them as **custom dimensions** under `Admin → Custom definitions`:

    | Trigger | Event Name | Event Parameters |
    |---------|------------|------------------|
    | User starts a quiz (clicks the button on the first / welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question | question_viewed_{question_title} | question_title |
    | User clicks a choice or selects a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | User answers the email question | email_lead_{quiz_name} | quiz_name |
    | User answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | User reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | User completes the quiz (conversion event) | generate_lead | quiz_name |
    | Customer clicks a product (view-product button or image) | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart ("add to cart" / "add all to cart") | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart / checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! note "Same events as the Built for Shopify version"

        This is the exact GA4 event catalog the `💎 Built for Shopify` quiz sends (see the Shopify tab above). The older `view` / `click` / `submit` / `recommendation` events (with `event_category` / `event_label`) are no longer sent.

    !!! info "`generate_lead` is a standard GA4 conversion event"

        Unlike the others, `generate_lead` keeps its plain name (no `_{…}` suffix) so GA4 can treat it as a conversion. Mark it as a **key event** under `Admin → Events` if you want it counted as a conversion.

    !!! warning "Question titles may contain a recall token"

        The `question_title` parameter, and the `question_viewed_{question_title}` event name, use the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token such as `{{slide:x1i0d83}}`. The token reaches GA4, not the answer. The token is stable. It never changes for a customer, or when you edit the quiz, so it works as a grouping key. It is not readable, though. The same applies to `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/). Strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If the events do not appear, check that your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

=== "Standalone"

    Customer events then appear in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    **Built-in events (no script required).** Click `Activate` in your quiz's `Connect → Google Analytics` section. The quiz then sends GA4-native events to whichever GA4 property your store's `gtag.js` is configured with. No Measurement ID is needed. Your `gtag.js` snippet has to load **before** RevenueHunt's `embed.js`. Each event name is built from its main parameter, so the value shows up directly in GA4's `Event name` report. To use the other parameters (like `question_title` or `question_ref`) as report columns, register them as **custom dimensions** under `Admin → Custom definitions`:

    | Trigger | Event Name | Event Parameters |
    |---------|------------|------------------|
    | User starts a quiz (clicks the button on the first / welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question | question_viewed_{question_title} | question_title |
    | User clicks a choice or selects a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | User answers the email question | email_lead_{quiz_name} | quiz_name |
    | User answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | User reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | User completes the quiz (conversion event) | generate_lead | quiz_name |
    | Customer clicks a product (view-product button or image) | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart ("add to cart" / "add all to cart") | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart / checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! note "Same events as the Built for Shopify version"

        This is the exact GA4 event catalog the `💎 Built for Shopify` quiz sends (see the Shopify tab above). The older `view` / `click` / `submit` / `recommendation` events (with `event_category` / `event_label`) are no longer sent.

    !!! info "`generate_lead` is a standard GA4 conversion event"

        Unlike the others, `generate_lead` keeps its plain name (no `_{…}` suffix) so GA4 can treat it as a conversion. Mark it as a **key event** under `Admin → Events` if you want it counted as a conversion.

    !!! warning "Question titles may contain a recall token"

        The `question_title` parameter, and the `question_viewed_{question_title}` event name, use the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token such as `{{slide:x1i0d83}}`. The token reaches GA4, not the answer. The token is stable. It never changes for a customer, or when you edit the quiz, so it works as a grouping key. It is not readable, though. The same applies to `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/). Strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If the events do not appear, check that your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

## Track quiz revenue

=== "Shopify"


    GA4 does not tie custom events to purchases on its own. You can segment or filter by those events, then look at the purchase revenue.

    Here are some options:

    ### Option 1 - create free form exploration

    You can measure how much revenue your quiz generates directly in GA4 using an **Exploration**. This walkthrough shows how to build a Free form table comparing **quiz users** with **all users**.

    ![how to ga revenue](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)
    ![how to ga revenue](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)


    1. Go to `Explore → + → Free form`.
    2. **Create the “Quiz Users” segment**. In the Variables panel, under Segments, click +. Choose User segment. Set the condition: Include users where `Event name` → `contains` → `quiz_started` (or use `matches regex` → `^quiz_started_.*$`). Name it `Quiz Users` → `Save and apply`. Also add the default `All Users` segment for comparison.

    3. **Add Dimensions and Metrics**. In the Variables panel:

        - `Dimensions` → `+` → add: `Event name`
        - `Metrics` → `+` → add: `Event count`, `Purchases`, `Total revenue`
    4. **Configure the Tab Settings**. In the Tab Settings panel:

        - `Segments`: select `All Users` and `Quiz Users`

        - `Rows`: `Event name`

        - `Columns`: leave empty, or set to `Segment` for side-by-side comparison

        - `Values`: `Event count`, `Purchases`, `Total revenue`

        - `Filters`: `Event name contains quiz_started`

        - `Visualization`: `Table` (or Bar chart)

        - `Date range`: e.g. `Last 28 days`

        The table then shows revenue and purchases from customers who triggered a `quiz_started` event, next to the figures for everyone.

    5. **Save and Reuse**. Rename your exploration (e.g. `Quiz Revenue`). Use the star or share option so teammates can find it easily.

        !!! tip "Optional Variations"

            - Compare specific quizzes: Use `Filters` → `Event name` contains your quiz ID/text
                (e.g., `quiz_started_skincare_quiz_usa`).

            - If your quiz is on a dedicated page: Create a **Session/User segment**: include users where **Page location contains `/pages/skin-quiz`**.
                This shows revenue for anyone visiting that quiz page.

    ### Option 2 – attribution via source/medium

    If you tag quiz entry points with UTM parameters such as `utm_source=quiz` or `utm_campaign=quiz_name`, the GA4 `Advertising → Attribution → Model comparison` report shows revenue attributed to those.

    Revenue attributed to the quiz appears in `Engagement > Conversions > Event name > purchase`. Click the `purchase` event.

    ![how to ga revenue2](/images/how_to_ga_revenue2.png)

    Add a `Source` column next to the default channel grouping and look for the rows which include the `revenuehunt` source.

    ![how to ga events](/images/how_to_ga_events.png)


=== "Shopify (Legacy)"

    Depending on the custom events you programmed in [Connect quiz to Google Analytics](#connect-quiz-to-google-analytics), you may see quiz revenue in Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or explore the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "WooCommerce"


    Depending on the custom events you programmed in [Connect quiz to Google Analytics](#connect-quiz-to-google-analytics), you may see quiz revenue in Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or explore the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Magento"


    Depending on the custom events you programmed in [Connect quiz to Google Analytics](#connect-quiz-to-google-analytics), you may see quiz revenue in Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or explore the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "BigCommerce"


    Depending on the custom events you programmed in [Connect quiz to Google Analytics](#connect-quiz-to-google-analytics), you may see quiz revenue in Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or explore the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Standalone"


    Depending on the custom events you programmed in [Connect quiz to Google Analytics](#connect-quiz-to-google-analytics), you may see quiz revenue in Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or explore the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).



## Use GA4 explorations


=== "Shopify"

    Google Analytics 4 (GA4) has **Explorations**, for digging deeper into your quiz data. Standard reports show high-level trends. Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz customers with everyone else**. See how much revenue comes from customers who start a quiz.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze customer paths**. See what a customer does after the quiz: view a recommended product, add to cart, or go straight to checkout.

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

    ### Example 1: most clicked choices

    You can build an exploration to see which choices are most popular.

    ![how to ga exploration](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. Go to `Explore → + → Free form`.
    2. Add Dimensions and Metrics. In the Variables panel:

        - `Dimensions` → `+` → add: `Event name`
        - `Metrics` → `+` → add: `Event count`

    3. Configure the Tab Settings. In the Tab Settings panel:

        - `Segments`: select `All Users`, or add `Quiz Users` to limit the results to customers who took a quiz.
        - `Rows`: `Event name`
        - `Columns`: leave empty
        - `Values`: `Event count`
        - `Filters`: `Event name contains block_answered`
        - `Visualization`: `Table` (or Bar chart)
        - `Date range`: e.g. `Last 28 days`

        The table then shows which quiz answers, the `block_answered` events, were clicked most often.

    5. **Save and Reuse**. Rename your exploration (e.g. `Most Clicked Choices`). Use the star or share option so teammates can find it easily.



    ### Example 2: track revenue from quizzes

    You can measure how much revenue your quiz generates directly in GA4 using an **Exploration**. This walkthrough shows how to build a Free form table comparing **quiz users** with **all users**.

    ![how to ga revenue](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)
    ![how to ga revenue](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. Go to `Explore → + → Free form`.
    2. **Create the “Quiz Users” segment**. In the Variables panel, under Segments, click +. Choose User segment. Set the condition: Include users where `Event name` → `contains` → `quiz_started` (or use `matches regex` → `^quiz_started_.*$`). Name it `Quiz Users` → `Save and apply`. Also add the default `All Users` segment for comparison.

    3. **Add Dimensions and Metrics**. In the Variables panel:

        - `Dimensions` → `+` → add: `Event name`
        - `Metrics` → `+` → add: `Event count`, `Purchases`, `Total revenue`
    4. **Configure the Tab Settings**. In the Tab Settings panel:

        - `Segments`: select `All Users` and `Quiz Users`

        - `Rows`: `Event name`

        - `Columns`: leave empty, or set to `Segment` for side-by-side comparison

        - `Values`: `Event count`, `Purchases`, `Total revenue`

        - `Filters`: `Event name contains quiz_started`

        - `Visualization`: `Table` (or Bar chart)

        - `Date range`: e.g. `Last 28 days`

        The table then shows revenue and purchases from customers who triggered a `quiz_started` event, next to the figures for everyone.

    5. **Save and Reuse**. Rename your exploration (e.g. `Quiz Revenue`). Use the star or share option so teammates can find it easily.

        !!! tip "Optional Variations"

            - Compare specific quizzes: Use `Filters` → `Event name` contains your quiz ID/text
                (e.g., `quiz_started_skincare_quiz_usa`).

            - If your quiz is on a dedicated page: Create a **Session/User segment**: include users where **Page location contains `/pages/skin-quiz`**.
                This shows revenue for anyone visiting that quiz page.



=== "Shopify (Legacy)"

    Google Analytics 4 (GA4) has **Explorations**, for digging deeper into your quiz data. Standard reports show high-level trends. Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz customers with everyone else**. See how much revenue comes from customers who start a quiz.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze customer paths**. See what a customer does after the quiz: view a recommended product, add to cart, or go straight to checkout.

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "WooCommerce"

    Google Analytics 4 (GA4) has **Explorations**, for digging deeper into your quiz data. Standard reports show high-level trends. Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz customers with everyone else**. See how much revenue comes from customers who start a quiz.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze customer paths**. See what a customer does after the quiz: view a recommended product, add to cart, or go straight to checkout.

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "Magento"

    Google Analytics 4 (GA4) has **Explorations**, for digging deeper into your quiz data. Standard reports show high-level trends. Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz customers with everyone else**. See how much revenue comes from customers who start a quiz.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze customer paths**. See what a customer does after the quiz: view a recommended product, add to cart, or go straight to checkout.

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "BigCommerce"

    Google Analytics 4 (GA4) has **Explorations**, for digging deeper into your quiz data. Standard reports show high-level trends. Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz customers with everyone else**. See how much revenue comes from customers who start a quiz.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze customer paths**. See what a customer does after the quiz: view a recommended product, add to cart, or go straight to checkout.

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "Standalone"

    Google Analytics 4 (GA4) has **Explorations**, for digging deeper into your quiz data. Standard reports show high-level trends. Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz customers with everyone else**. See how much revenue comes from customers who start a quiz.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze customer paths**. See what a customer does after the quiz: view a recommended product, add to cart, or go straight to checkout.

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.



---
This article explains how to connect the quiz to Google Analytics and track quiz performance in GA4.