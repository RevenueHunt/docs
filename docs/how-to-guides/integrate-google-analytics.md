---
description: "Learn how to integrate Google Analytics with your RevenueHunt quiz to track user engagement and minimize abandonment rates."
icon: material/google-analytics
---

# How to Track Quiz Performance with Google Analytics

=== "Shopify"

    Google Analytics offers a powerful way to gain insights into user engagement with your quizzes. Linking your quiz with Google Analytics can provide valuable data on user interaction, pinpoint engagement issues, and help minimize abandonment rates. 
    
    The `💎 Built for Shopify` version of RevenueHunt app includes native GA4 integration for comprehensive event tracking.

    This article will guide you through the process of connecting your quiz to Google Analytics and tracking quiz events.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/8P-kANzya2g?si=L-rMRoSRsdbwSgof" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.  
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.  

        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.



=== "Shopify (Legacy)"

    To track quiz performance with Google Analytics in Shopify (legacy), you'll need to implement custom JavaScript tracking. This allows you to monitor specific quiz events and user interactions. 

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.  
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.  
        
        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "WooCommerce"       

    To track quiz performance with Google Analytics in WooCommerce, you'll need to implement custom JavaScript tracking. This allows you to monitor specific quiz events and user interactions. 

    This article explains how to track quiz events and performance in Google Analytics. 


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.  
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.  
        
        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "Magento"

    To track quiz performance with Google Analytics in Magento, you'll need to implement custom JavaScript tracking. This allows you to monitor specific quiz events and user interactions. 

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.  
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.  
        
        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "BigCommerce"

    To track quiz performance with Google Analytics in BigCommerce, you'll need to implement custom JavaScript tracking. This allows you to monitor specific quiz events and user interactions. 

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.  
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.  
        
        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

=== "Standalone"

    To track quiz performance with Google Analytics in a Standalone version of RevenueHunt app, you'll need to implement custom JavaScript tracking. This allows you to monitor specific quiz events and user interactions. 

    This article explains how to track quiz events and performance in Google Analytics.


    !!! warning "GA4 Event Tracking Reliability"
        Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased.  
        The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately.  
        
        If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.



## Connect Quiz to Google Analytics

=== "Shopify"


    !!! note

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

    1. Make sure you have set up the GA4 tracking on your website. 

        !!! tip

            Don't know how to connect your website to Google Analytics or find your GA tracking code? [Check this link](https://support.google.com/analytics/answer/1008080).
    1. Head to your quiz and click on the [Integrations](/reference/quiz-builder/connect-integrations/) tab.
    2. Click on the `Activate` button in the Google Analytics section.
        ![how to integrate ga4 built for shopify revenuehunt app](/images/how_to_integrate_ga4_shopify_v2.png)
    3. Click `Save` to confirm the changes.
    4. Once activated the quiz will connect to the GA4 tracking code already present on your website. It can take up to 72 hours for the data to start appearing in your Meta portal.

    ??? tip "Optional: Add Custom Trackers"

        The native integration above already sends the standard events (quiz started, question viewed, choice answered, results viewed, product clicked, add to cart, and so on). To track **custom** events on top of those, use the quiz's built-in **Custom JS** section. It runs plain JavaScript (no `<script>` tags) and gives you a global `window.quiz` object.

        !!! warning

            The legacy `prqQuizCallback` / `prqSlideCallback` callbacks do **not** exist in the `💎 Built for Shopify` version. Use `window.quiz` instead, as shown below. Custom JS only runs in the preview or live quiz, not inside the builder.

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

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

    To track quiz events and performance in Google Analytics, you'll need to implement custom JavaScript tracking to your website, preferably the page where the quiz is embeded.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) to learn how our callback function works and how it can be used for tracking custom events.

    2. **Embed the Custom Script**: Add the following script to the page where the quiz is embedded (or sitewide in your theme's main template file). Make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`:
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

    3. **Customize Event Tracking**: The example above fires once on completion. To track each answer as the customer makes it, add `prqSlideCallback`, which fires every time a question is answered. The snippet below also maps the selected choice IDs to their human-readable labels (both the choices and the selected values live in the slide object):
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

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

    To track quiz events and performance in Google Analytics, you'll need to implement custom JavaScript tracking to your website, preferably the page where the quiz is embeded.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) to learn how our callback function works and how it can be used for tracking custom events.

    2. **Embed the Custom Script**: Add the following script to the page where the quiz is embedded (or sitewide in your theme's main template file). Make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`:
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

    3. **Customize Event Tracking**: The example above fires once on completion. To track each answer as the customer makes it, add `prqSlideCallback`, which fires every time a question is answered. The snippet below also maps the selected choice IDs to their human-readable labels (both the choices and the selected values live in the slide object):
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

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

    To track quiz events and performance in Google Analytics, you'll need to implement custom JavaScript tracking to your website, preferably the page where the quiz is embeded.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) to learn how our callback function works and how it can be used for tracking custom events.

    2. **Embed the Custom Script**: Add the following script to the page where the quiz is embedded (or sitewide in your theme's main template file). Make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`:
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

    3. **Customize Event Tracking**: The example above fires once on completion. To track each answer as the customer makes it, add `prqSlideCallback`, which fires every time a question is answered. The snippet below also maps the selected choice IDs to their human-readable labels (both the choices and the selected values live in the slide object):
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

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

    To track quiz events and performance in Google Analytics, you'll need to implement custom JavaScript tracking to your website, preferably the page where the quiz is embeded.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) to learn how our callback function works and how it can be used for tracking custom events.

    2. **Embed the Custom Script**: Add the following script to the page where the quiz is embedded (or sitewide in your theme's main template file). Make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`:
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

    3. **Customize Event Tracking**: The example above fires once on completion. To track each answer as the customer makes it, add `prqSlideCallback`, which fires every time a question is answered. The snippet below also maps the selected choice IDs to their human-readable labels (both the choices and the selected values live in the slide object):
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

        Google Analytics GA4 tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

    To track quiz events and performance in Google Analytics, you'll need to implement custom JavaScript tracking to your website, preferably the page where the quiz is embeded.

    To implement custom event tracking for your quiz, follow these steps:

    1. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) to learn how our callback function works and how it can be used for tracking custom events.

    2. **Embed the Custom Script**: Add the following script to the page where the quiz is embedded (or sitewide in your theme's main template file). Make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`:
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

    3. **Customize Event Tracking**: The example above fires once on completion. To track each answer as the customer makes it, add `prqSlideCallback`, which fires every time a question is answered. The snippet below also maps the selected choice IDs to their human-readable labels (both the choices and the selected values live in the slide object):
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


## Track Customer Behavior (Events)

=== "Shopify"

    You'll be able to see quiz usage and customer behavior in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_shopifyv2_events.png)

    !!! warning "Data may take up to 72 hours to appear"

        If you don't see the events, check the `View realtime` tab in GA4 or wait a day or two for the data to appear. Google Analytics can take up to 72 hours to process the data.

    Events are triggered every time a customer starts a quiz, views a question, picks a choice, gets to the results page, adds a product to the cart, and proceeds to the cart/checkout. You can check more data about unique events by clicking on the specific Event name.

    | Trigger                                                             | Event Name | Event Parameters    |
    |---------------------------------------------------------------------|------------|-----------------|
    | User starts a quiz (clicks on the button of the first question or the welcome question) | quiz_started_{quiz_name} | quiz_name |
    | User views a question                                               | question_viewed_{question_title} | question_title |
    | User clicks on a choice or selects an option from a dropdown        | block_answered_{choice_text} | choice_text |
    | User responds to the email question                                 | email_lead_{quiz_name} | quiz_name |
    | User responds to the phone question                                 | phone_lead_{quiz_name} | quiz_name |
    | User gets to results page                                           | results_page_viewed_{results_title} | results_title |
    | A certain product is recommended in the results page                | product_recommended_{product_name} | product_name |
    | Customer clicks on product (view product button or image)           | product_clicked_{product_name} | product_name |
    | Customer adds a product to cart (via "add to cart" or "add all to cart" buttons) | product_added_to_cart_{product_name} | product_name |
    | Customer proceeds to cart/checkout                                  | proceed_to_checkout_{quiz_name} | quiz_name |
    | Customer retakes quiz                                               | retake_quiz_{quiz_name} | quiz_name |


=== "Shopify (Legacy)"

    Once set up, you'll be able to see customer events in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_shopifyv2_events.png)

    **Built-in events (no script required).** As soon as your GA4 tracking code is saved in the quiz's `Connect → Google Analytics` section (and your `gtag.js` snippet loads before `embed.js`), the quiz sends its own events automatically. They are named by **action**, with the detail carried in the `event_category` and `event_label` parameters:

    | Trigger | Event name | event_category | event_label |
    |---------|------------|----------------|-------------|
    | Quiz started (first / welcome question) | `view` | `start` | quiz name |
    | Question viewed | `view` | `question` | question title |
    | Choice selected | `click` | `choice` | choice label |
    | Email captured | `submit` | `email` | quiz name |
    | Phone captured | `submit` | `phone` | quiz name |
    | Results page viewed | `view` | `results` | quiz name |
    | Product recommended | `recommendation` | `product` | product name |
    | Product clicked | `view` | `product` | product name |
    | Product added to cart | `click` | `addCart` | product name |
    | Product removed from cart | `click` | `removeCart` | product name |
    | Proceed to cart / checkout | `click` | `checkoutButton` | quiz name |
    | Retake quiz | `click` | `retakeQuiz` | quiz name |

    !!! note "These names look generic on purpose"

        In GA4 the quiz produces only four event names: `view`, `click`, `submit` and `recommendation`. `submit` and `recommendation` aren't native GA4 events, so seeing them confirms the quiz is tracking. To tell the `view` and `click` events apart in standard reports, register `event_category` and `event_label` as **custom dimensions** under `Admin → Custom definitions` (otherwise GA4 lumps every question under the same `view` row).

    !!! warning "Different from the Built for Shopify version"

        The richer event names listed in the Shopify tab (`quiz_started_{quiz_name}`, `question_viewed_{question_title}`, and so on) only apply to the `💎 Built for Shopify` quiz. On this version the events are named by action as shown above.

    !!! warning "Question titles may contain a recall token"

        The `event_label` on a `view` / `question` event is the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token like `{{slide:x1i0d83}}`, and the token (not the answer) is what reaches GA4. The token is stable, it never changes per visitor or when you edit the quiz, so it's safe as a grouping key, but it isn't human-readable. The same applies if you read `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/); strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If you're not seeing the events, make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.


=== "WooCommerce"

    Once set up, you'll be able to see customer events in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_woocommerce_events.png)

    **Built-in events (no script required).** As soon as your GA4 tracking code is saved in the quiz's `Connect → Google Analytics` section (and your `gtag.js` snippet loads before `embed.js`), the quiz sends its own events automatically. They are named by **action**, with the detail carried in the `event_category` and `event_label` parameters:

    | Trigger | Event name | event_category | event_label |
    |---------|------------|----------------|-------------|
    | Quiz started (first / welcome question) | `view` | `start` | quiz name |
    | Question viewed | `view` | `question` | question title |
    | Choice selected | `click` | `choice` | choice label |
    | Email captured | `submit` | `email` | quiz name |
    | Phone captured | `submit` | `phone` | quiz name |
    | Results page viewed | `view` | `results` | quiz name |
    | Product recommended | `recommendation` | `product` | product name |
    | Product clicked | `view` | `product` | product name |
    | Product added to cart | `click` | `addCart` | product name |
    | Product removed from cart | `click` | `removeCart` | product name |
    | Proceed to cart / checkout | `click` | `checkoutButton` | quiz name |
    | Retake quiz | `click` | `retakeQuiz` | quiz name |

    !!! note "These names look generic on purpose"

        In GA4 the quiz produces only four event names: `view`, `click`, `submit` and `recommendation`. `submit` and `recommendation` aren't native GA4 events, so seeing them confirms the quiz is tracking. To tell the `view` and `click` events apart in standard reports, register `event_category` and `event_label` as **custom dimensions** under `Admin → Custom definitions` (otherwise GA4 lumps every question under the same `view` row).

    !!! warning "Different from the Built for Shopify version"

        The richer event names listed in the Shopify tab (`quiz_started_{quiz_name}`, `question_viewed_{question_title}`, and so on) only apply to the `💎 Built for Shopify` quiz. On WooCommerce the events are named by action as shown above.

    !!! warning "Question titles may contain a recall token"

        The `event_label` on a `view` / `question` event is the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token like `{{slide:x1i0d83}}`, and the token (not the answer) is what reaches GA4. The token is stable, it never changes per visitor or when you edit the quiz, so it's safe as a grouping key, but it isn't human-readable. The same applies if you read `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/); strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If you're not seeing the events, make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

=== "Magento"

    Once set up, you'll be able to see customer events in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_magento_events.png)

    **Built-in events (no script required).** As soon as your GA4 tracking code is saved in the quiz's `Connect → Google Analytics` section (and your `gtag.js` snippet loads before `embed.js`), the quiz sends its own events automatically. They are named by **action**, with the detail carried in the `event_category` and `event_label` parameters:

    | Trigger | Event name | event_category | event_label |
    |---------|------------|----------------|-------------|
    | Quiz started (first / welcome question) | `view` | `start` | quiz name |
    | Question viewed | `view` | `question` | question title |
    | Choice selected | `click` | `choice` | choice label |
    | Email captured | `submit` | `email` | quiz name |
    | Phone captured | `submit` | `phone` | quiz name |
    | Results page viewed | `view` | `results` | quiz name |
    | Product recommended | `recommendation` | `product` | product name |
    | Product clicked | `view` | `product` | product name |
    | Product added to cart | `click` | `addCart` | product name |
    | Product removed from cart | `click` | `removeCart` | product name |
    | Proceed to cart / checkout | `click` | `checkoutButton` | quiz name |
    | Retake quiz | `click` | `retakeQuiz` | quiz name |

    !!! note "These names look generic on purpose"

        In GA4 the quiz produces only four event names: `view`, `click`, `submit` and `recommendation`. `submit` and `recommendation` aren't native GA4 events, so seeing them confirms the quiz is tracking. To tell the `view` and `click` events apart in standard reports, register `event_category` and `event_label` as **custom dimensions** under `Admin → Custom definitions` (otherwise GA4 lumps every question under the same `view` row).

    !!! warning "Different from the Built for Shopify version"

        The richer event names listed in the Shopify tab (`quiz_started_{quiz_name}`, `question_viewed_{question_title}`, and so on) only apply to the `💎 Built for Shopify` quiz. On this version the events are named by action as shown above.

    !!! warning "Question titles may contain a recall token"

        The `event_label` on a `view` / `question` event is the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token like `{{slide:x1i0d83}}`, and the token (not the answer) is what reaches GA4. The token is stable, it never changes per visitor or when you edit the quiz, so it's safe as a grouping key, but it isn't human-readable. The same applies if you read `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/); strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If you're not seeing the events, make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

=== "BigCommerce"

    Once set up, you'll be able to see customer events in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_bigcommerce_events.png)

    **Built-in events (no script required).** As soon as your GA4 tracking code is saved in the quiz's `Connect → Google Analytics` section (and your `gtag.js` snippet loads before `embed.js`), the quiz sends its own events automatically. They are named by **action**, with the detail carried in the `event_category` and `event_label` parameters:

    | Trigger | Event name | event_category | event_label |
    |---------|------------|----------------|-------------|
    | Quiz started (first / welcome question) | `view` | `start` | quiz name |
    | Question viewed | `view` | `question` | question title |
    | Choice selected | `click` | `choice` | choice label |
    | Email captured | `submit` | `email` | quiz name |
    | Phone captured | `submit` | `phone` | quiz name |
    | Results page viewed | `view` | `results` | quiz name |
    | Product recommended | `recommendation` | `product` | product name |
    | Product clicked | `view` | `product` | product name |
    | Product added to cart | `click` | `addCart` | product name |
    | Product removed from cart | `click` | `removeCart` | product name |
    | Proceed to cart / checkout | `click` | `checkoutButton` | quiz name |
    | Retake quiz | `click` | `retakeQuiz` | quiz name |

    !!! note "These names look generic on purpose"

        In GA4 the quiz produces only four event names: `view`, `click`, `submit` and `recommendation`. `submit` and `recommendation` aren't native GA4 events, so seeing them confirms the quiz is tracking. To tell the `view` and `click` events apart in standard reports, register `event_category` and `event_label` as **custom dimensions** under `Admin → Custom definitions` (otherwise GA4 lumps every question under the same `view` row).

    !!! warning "Different from the Built for Shopify version"

        The richer event names listed in the Shopify tab (`quiz_started_{quiz_name}`, `question_viewed_{question_title}`, and so on) only apply to the `💎 Built for Shopify` quiz. On this version the events are named by action as shown above.

    !!! warning "Question titles may contain a recall token"

        The `event_label` on a `view` / `question` event is the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token like `{{slide:x1i0d83}}`, and the token (not the answer) is what reaches GA4. The token is stable, it never changes per visitor or when you edit the quiz, so it's safe as a grouping key, but it isn't human-readable. The same applies if you read `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/); strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If you're not seeing the events, make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

=== "Standalone"

    Once set up, you'll be able to see customer events in your Google Analytics dashboard, under `Reports > View user engagement and retention > Events`.

    ![how to ga events](/images/how_to_standalone_events.png)

    **Built-in events (no script required).** As soon as your GA4 tracking code is saved in the quiz's `Connect → Google Analytics` section (and your `gtag.js` snippet loads before `embed.js`), the quiz sends its own events automatically. They are named by **action**, with the detail carried in the `event_category` and `event_label` parameters:

    | Trigger | Event name | event_category | event_label |
    |---------|------------|----------------|-------------|
    | Quiz started (first / welcome question) | `view` | `start` | quiz name |
    | Question viewed | `view` | `question` | question title |
    | Choice selected | `click` | `choice` | choice label |
    | Email captured | `submit` | `email` | quiz name |
    | Phone captured | `submit` | `phone` | quiz name |
    | Results page viewed | `view` | `results` | quiz name |
    | Product recommended | `recommendation` | `product` | product name |
    | Product clicked | `view` | `product` | product name |
    | Product added to cart | `click` | `addCart` | product name |
    | Product removed from cart | `click` | `removeCart` | product name |
    | Proceed to cart / checkout | `click` | `checkoutButton` | quiz name |
    | Retake quiz | `click` | `retakeQuiz` | quiz name |

    !!! note "These names look generic on purpose"

        In GA4 the quiz produces only four event names: `view`, `click`, `submit` and `recommendation`. `submit` and `recommendation` aren't native GA4 events, so seeing them confirms the quiz is tracking. To tell the `view` and `click` events apart in standard reports, register `event_category` and `event_label` as **custom dimensions** under `Admin → Custom definitions` (otherwise GA4 lumps every question under the same `view` row).

    !!! warning "Different from the Built for Shopify version"

        The richer event names listed in the Shopify tab (`quiz_started_{quiz_name}`, `question_viewed_{question_title}`, and so on) only apply to the `💎 Built for Shopify` quiz. On this version the events are named by action as shown above.

    !!! warning "Question titles may contain a recall token"

        The `event_label` on a `view` / `question` event is the **raw** question title. If a question pipes in a previous answer, the title holds an unresolved recall token like `{{slide:x1i0d83}}`, and the token (not the answer) is what reaches GA4. The token is stable, it never changes per visitor or when you edit the quiz, so it's safe as a grouping key, but it isn't human-readable. The same applies if you read `slide.attributes.title` in a [custom callback](/how-to-guides/use-callback-function/); strip it with `slide.attributes.title.replace(/\{\{slide:\w+\}\}/g, '').trim()`.

    If you're not seeing the events, make sure your GA4 `gtag.js` snippet loads **before** RevenueHunt's `embed.js`.

## Track Quiz Revenue

=== "Shopify"


    GA4 doesn’t “automatically” tie custom events to purchases. But you can segment/filter by those events and then look at purchase revenue. 
    
    Here are some options:

    ### Option 1 - Create Free Form Exploration

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

        You’ll now see a table showing revenue and purchases from quiz users (people who triggered a quiz_started event) compared to all users.

    5. **Save and Reuse**. Rename your exploration (e.g. `Quiz Revenue`). Use the star or share option so teammates can find it easily.

        !!! tip "Optional Variations"

            - Compare specific quizzes: Use `Filters` → `Event name` contains your quiz ID/text  
                (e.g., `quiz_started_skincare_quiz_usa`).

            - If your quiz is on a dedicated page: Create a **Session/User segment**: include users where **Page location contains `/pages/skin-quiz`**.
                This shows revenue for anyone visiting that quiz page.

    ### Option 2 – Attribution via Source/Medium

    If you’re tagging quiz entry points with UTM parameters (like `utm_source=quiz` or `utm_campaign=quiz_name`), GA4’s `Advertising → Attribution → Model comparison` will show revenue attributed to those.

    You'll see revenue attributed to the quiz in `Engagement > Conversions > Event name > purchase`. Click on the `purchase` event.

    ![how to ga revenue2](/images/how_to_ga_revenue2.png)

    Add a `Source` column next to the default channel grouping and look for the rows which include the `revenuehunt` source.

    ![how to ga events](/images/how_to_ga_events.png)


=== "Shopify (Legacy)"

    Depending on the custom events that you've programed in the [first step](/how-to-guides/integrate-google-analytics/#connect-the-quiz-to-google-analytics), you may be able to see quiz revenue in your Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or expolre the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "WooCommerce"


    Depending on the custom events that you've programed in the [first step](#connect-the-quiz-to-google-analytics), you may be able to see quiz revenue in your Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or expolre the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Magento"


    Depending on the custom events that you've programed in the [first step](#connect-the-quiz-to-google-analytics), you may be able to see quiz revenue in your Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or expolre the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "BigCommerce"


    Depending on the custom events that you've programed in the [first step](#connect-the-quiz-to-google-analytics), you may be able to see quiz revenue in your Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or expolre the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Standalone"


    Depending on the custom events that you've programed in the [first step](#connect-the-quiz-to-google-analytics), you may be able to see quiz revenue in your Google Analytics.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/9216061?hl=en) for more information on how to track revenue from custom events or expolre the GA4 [Explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).



## Use GA4 Explorations


=== "Shopify"

    Google Analytics 4 (GA4) offers **Explorations**, a powerful tool for digging deeper into your quiz data. Standard reports show you high-level trends, but Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz users vs. all users**. See how much revenue is generated by customers who start a quiz compared to those who don’t.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze user paths**. Discover what customers do after completing your quiz—do they view recommended products, add to cart, or head straight to checkout?

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

    ### Example 1: Most Clicked Choices

    You can build an exploration to see which choices are most popular.

    ![how to ga exploration](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. Go to `Explore → + → Free form`.
    2. Add Dimensions and Metrics. In the Variables panel:

        - `Dimensions` → `+` → add: `Event name`
        - `Metrics` → `+` → add: `Event count`  

    3. Configure the Tab Settings. In the Tab Settings panel:

        - `Segments`: select `All Users` (or add `Quiz Users` if you want to limit results to quiz participants)
        - `Rows`: `Event name`
        - `Columns`: leave empty
        - `Values`: `Event count`
        - `Filters`: `Event name contains block_answered`
        - `Visualization`: `Table` (or Bar chart)
        - `Date range`: e.g. `Last 28 days`

        You’ll now see a table showing which quiz answers (`block_answered` events) were clicked most often, giving you a clear view of the most popular choices.

    5. **Save and Reuse**. Rename your exploration (e.g. `Most Clicked Choices`). Use the star or share option so teammates can find it easily.



    ### Example 2: Track Revenue from Quizzes
    
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

        You’ll now see a table showing revenue and purchases from quiz users (people who triggered a quiz_started event) compared to all users.

    5. **Save and Reuse**. Rename your exploration (e.g. `Quiz Revenue`). Use the star or share option so teammates can find it easily.

        !!! tip "Optional Variations"

            - Compare specific quizzes: Use `Filters` → `Event name` contains your quiz ID/text  
                (e.g., `quiz_started_skincare_quiz_usa`).

            - If your quiz is on a dedicated page: Create a **Session/User segment**: include users where **Page location contains `/pages/skin-quiz`**.
                This shows revenue for anyone visiting that quiz page.



=== "Shopify (Legacy)"

    Google Analytics 4 (GA4) offers **Explorations**, a powerful tool for digging deeper into your quiz data. Standard reports show you high-level trends, but Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz users vs. all users**. See how much revenue is generated by customers who start a quiz compared to those who don’t.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze user paths**. Discover what customers do after completing your quiz—do they view recommended products, add to cart, or head straight to checkout?

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "WooCommerce"

    Google Analytics 4 (GA4) offers **Explorations**, a powerful tool for digging deeper into your quiz data. Standard reports show you high-level trends, but Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz users vs. all users**. See how much revenue is generated by customers who start a quiz compared to those who don’t.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze user paths**. Discover what customers do after completing your quiz—do they view recommended products, add to cart, or head straight to checkout?

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "Magento"

    Google Analytics 4 (GA4) offers **Explorations**, a powerful tool for digging deeper into your quiz data. Standard reports show you high-level trends, but Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz users vs. all users**. See how much revenue is generated by customers who start a quiz compared to those who don’t.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze user paths**. Discover what customers do after completing your quiz—do they view recommended products, add to cart, or head straight to checkout?

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "BigCommerce"

    Google Analytics 4 (GA4) offers **Explorations**, a powerful tool for digging deeper into your quiz data. Standard reports show you high-level trends, but Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz users vs. all users**. See how much revenue is generated by customers who start a quiz compared to those who don’t.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze user paths**. Discover what customers do after completing your quiz—do they view recommended products, add to cart, or head straight to checkout?

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.

=== "Standalone"

    Google Analytics 4 (GA4) offers **Explorations**, a powerful tool for digging deeper into your quiz data. Standard reports show you high-level trends, but Explorations let you ask more specific questions about how customers interact with your quiz and how it impacts revenue.

    With Explorations, you can:

    - **Compare quiz users vs. all users**. See how much revenue is generated by customers who start a quiz compared to those who don’t.

    - **Break down results by quiz**. If you run multiple quizzes, use Explorations to see which quiz names bring in the most purchases and revenue.

    - **Build funnels**. Visualize the full journey from *quiz\_started* → *results\_page\_viewed* → *product\_added\_to\_cart* → *purchase*, and spot where users drop off.

    - **Analyze user paths**. Discover what customers do after completing your quiz—do they view recommended products, add to cart, or head straight to checkout?

    - **Create segments and audiences**. Build an audience of “Quiz Users” for ongoing analysis or remarketing in Google Ads.

    Refer to the Google Analytics [documentation](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article) for more information on how to use GA4 Explorations.



---
This article explains how to connect the quiz to Google Analytics and track quiz performance in GA4.