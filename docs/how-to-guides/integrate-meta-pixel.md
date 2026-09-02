---
description: "Learn how to integrate Meta Pixel with your RevenueHunt quiz to track conversions and optimize your Facebook advertising performance."
icon: material/facebook
---

# How to Integrate Meta Pixel with Quiz

The Meta Pixel records what customers do in your quiz, so you can measure your Facebook ads against it and build audiences from the answers.

??? question "What is the Meta Pixel?"

    A small piece of code on your website. It records conversions from your ads, feeds later campaigns, and builds audiences out of the people who have already visited.

!!! note "Give the quiz its own page"

    Pixel tracking works best when the quiz sits on a page of its own. See [How to Embed an Inline Quiz on Your Store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

## Connect the Meta Pixel to your quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/qxcWFdfTZ_s?si=to_CqE57FATovIPS" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create a Meta Pixel, if you do not have one.** See the [Meta Pixel setup documentation](https://www.facebook.com/business/help/952192354843755?id=1205376682832142), then add it to your website.

    2. **In your Shopify admin, go to `Settings > Customer events` and check the Meta Pixel is there.** If it is not, add it with the [Facebook and Instagram app](https://apps.shopify.com/facebook-and-instagram-meta-app).

    3. **Open the Facebook and Instagram app, go to `Settings`, and set `Shared data` to `Maximum`.** Advanced and custom events are not sent at a lower setting.

    4. **Choose or create the data set that will receive the events.**

        ![Shared data and data set in the Facebook and Instagram app settings](/images/how_to_shopifyv2_integrate_meta_pixel_facebookappsettings.png)

        !!! tip "Creating a data set"

            Go to [business.facebook.com](https://business.facebook.com/), then `Ads Manager > Events Manager > Data sources > Create data source`.

    5. **Publish the quiz on your store.**

    6. **Open the [Integrations](/reference/quiz-builder/connect-integrations/) tab of your quiz, find Meta Pixel, and click `Activate`.**

        ![Activating the Meta Pixel in the Integrations tab](/images/how_to_integrate_fb_pixel_shopify_v2.png)

    7. **Click `Save`.** The quiz connects to the Pixel already on your website, so there is no Pixel ID to enter.

    8. **Open the Facebook and Instagram app, go to `Settings`, and open your data set to reach the Meta Events Manager.** Click `Test events`, enter your website URL, then take the quiz on your site. Events such as `ViewContent`, `Lead` and `RetakeQuiz` should appear as you go.

        ![Quiz events arriving in the Meta Events Manager](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        If they do, the Pixel is connected.

    9. **Review the custom events before you use them in an ad.** See [Review custom events](#review-custom-events).

=== "Shopify (Legacy)"

    1. **Create a Meta Pixel, if you do not have one.** See the [Meta Pixel setup documentation](https://www.facebook.com/business/help/952192354843755?id=1205376682832142), then add it to your website.

    2. **In your Shopify admin, go to `Settings > Customer events` and check the Meta Pixel is there.** If it is not, add it with the [Facebook and Instagram app](https://apps.shopify.com/facebook-and-instagram-meta-app).

    3. **Open the Facebook and Instagram app, go to `Settings`, and set `Shared data` to `Maximum`.** Advanced and custom events are not sent at a lower setting.

    4. **Choose or create the data set that will receive the events.**

        ![Shared data and data set in the Facebook and Instagram app settings](/images/how_to_shopifyv2_integrate_meta_pixel_facebookappsettings.png)

        !!! tip "Creating a data set"

            Go to [business.facebook.com](https://business.facebook.com/), then `Ads Manager > Events Manager > Data sources > Create data source`.

    5. **Publish the quiz on your store.**

    6. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, find Meta Pixel, and click `connect`.**

    7. **Enter your `Meta Pixel ID`.** It has to match the Pixel behind the data set you chose in the Facebook and Instagram app.

    8. **Open the Facebook and Instagram app, go to `Settings`, and open your data set to reach the Meta Events Manager.** Click `Test events`, enter your website URL, then take the quiz on your site. Events such as `ViewContent`, `Lead` and `RetakeQuiz` should appear as you go.

        ![Quiz events arriving in the Meta Events Manager](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        If they do, the Pixel is connected.

    9. **Review the custom events before you use them in an ad.** See [Review custom events](#review-custom-events).

=== "WooCommerce"

    1. **Create a Meta Pixel, if you do not have one.** See the [Meta Pixel setup documentation](https://www.facebook.com/business/help/952192354843755?id=1205376682832142), then add it to your website.

    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, find Meta Pixel, and click `connect`.**

    3. **Enter your `Meta Pixel ID`.**

    4. **Open the [Meta Events Manager](https://business.facebook.com/events/manager/).** Click `Test events`, enter your website URL, then take the quiz on your site. Events such as `ViewContent`, `Lead` and `RetakeQuiz` should appear as you go.

        ![Quiz events arriving in the Meta Events Manager](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        If they do, the Pixel is connected.

    5. **Review the custom events before you use them in an ad.** See [Review custom events](#review-custom-events).

=== "Magento"

    1. **Create a Meta Pixel, if you do not have one.** See the [Meta Pixel setup documentation](https://www.facebook.com/business/help/952192354843755?id=1205376682832142), then add it to your website.

    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, find Meta Pixel, and click `connect`.**

    3. **Enter your `Meta Pixel ID`.**

    4. **Open the [Meta Events Manager](https://business.facebook.com/events/manager/).** Click `Test events`, enter your website URL, then take the quiz on your site. Events such as `ViewContent`, `Lead` and `RetakeQuiz` should appear as you go.

        ![Quiz events arriving in the Meta Events Manager](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        If they do, the Pixel is connected.

    5. **Review the custom events before you use them in an ad.** See [Review custom events](#review-custom-events).

=== "BigCommerce"

    1. **Create a Meta Pixel, if you do not have one.** See the [Meta Pixel setup documentation](https://www.facebook.com/business/help/952192354843755?id=1205376682832142), then add it to your website.

    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, find Meta Pixel, and click `connect`.**

    3. **Enter your `Meta Pixel ID`.**

    4. **Open the [Meta Events Manager](https://business.facebook.com/events/manager/).** Click `Test events`, enter your website URL, then take the quiz on your site. Events such as `ViewContent`, `Lead` and `RetakeQuiz` should appear as you go.

        ![Quiz events arriving in the Meta Events Manager](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        If they do, the Pixel is connected.

    5. **Review the custom events before you use them in an ad.** See [Review custom events](#review-custom-events).

=== "Standalone"

    1. **Create a Meta Pixel, if you do not have one.** See the [Meta Pixel setup documentation](https://www.facebook.com/business/help/952192354843755?id=1205376682832142), then add it to your website.

    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, find Meta Pixel, and click `connect`.**

    3. **Enter your `Meta Pixel ID`.**

    4. **Open the [Meta Events Manager](https://business.facebook.com/events/manager/).** Click `Test events`, enter your website URL, then take the quiz on your site. Events such as `ViewContent`, `Lead` and `RetakeQuiz` should appear as you go.

        ![Quiz events arriving in the Meta Events Manager](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        If they do, the Pixel is connected.

    5. **Review the custom events before you use them in an ad.** See [Review custom events](#review-custom-events).

## What the Meta Pixel tracks

Once the Pixel is connected, the quiz sends an event at each step. They arrive in the Meta Events Manager, where you can build [Custom Audiences](https://www.facebook.com/business/learn/lessons/custom-audience-tips-with-facebook-pixel) and [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) from them.

![Quiz events in the Meta Events Manager](/images/how_to_fb_pixel_events.png)

Most of them are `ViewContent` events, told apart by their `content_category`. That covers starting the quiz, viewing a question, picking an answer, reaching the results page, and seeing a recommended product. The rest cover adding to the cart, going to the checkout, answering the email or phone question, and retaking the quiz.

| Trigger | fbq action | fbq event | fbq parameters |
|---|---|---|---|
| The customer starts a quiz | `track` | `ViewContent` | `{ content_name: quiz_name, content_category: 'quiz' }` |
| The customer views a question | `track` | `ViewContent` | `{ content_name: question_title, content_category: 'question' }` |
| The customer clicks a choice | `track` | `ViewContent` | `{ content_name: choice_text, content_category: 'choice' }` |
| The customer answers the email question | `trackCustom` | `EmailLead` | `{ content_name: quiz_name, content_category: 'lead' }` |
| The customer answers the phone question | `trackCustom` | `PhoneLead` | `{ content_name: quiz_name, content_category: 'lead' }` |
| The customer reaches the results page | `track` | `ViewContent` | `{ content_name: results_page_title, content_category: 'results' }` |
| The customer reaches the results page | `track` | `Lead` | `{}` |
| A product is recommended on the results page | `track` | `ViewContent` | `{ content_name: product_name, content_type: 'recommendation', content_ids: [sku_or_variant_id], value: product_price, currency: quiz_currency }` |
| The customer adds a product to the cart | `track` | `AddToCart` | `{ content_name: product_name, content_type: 'recommendation', content_ids: [sku_or_variant_id], value: product_price, currency: quiz_currency }` |
| The customer proceeds to the checkout | `track` | `InitiateCheckout` | `{ num_items: num_products_in_cart, currency: quiz_currency, value: value_of_products_in_cart }` |
| The customer retakes the quiz | `trackCustom` | `RetakeQuiz` | `{ content_name: quiz_name, content_category: 'quiz' }` |

## Review custom events

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/qxcWFdfTZ_s?si=s1XW819N9ub_Gv0j&amp;start=227" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Meta will not let a custom event drive an ads feature until you have reviewed it. The quiz sends two, `RetakeQuiz` and `EmailLead`, so review them once and they become usable in audiences.

1. **Open your Pixel data source in the Meta Events Manager.** New events appear there once the quiz is connected.

    | Kind | Events |
    |---|---|
    | Standard | `View Content`, `Page View`, `Lead` |
    | Custom | `Retake Quiz Action`, `Email Lead Action` |

    The data source shows the notice `Custom events can't be used with ads features.`

    ![The custom events notice in the Events Manager](/images/how_to_shopifyv2_integrate_meta_pixel_reviewcustomevents.png)

2. **Click `Review`.**

    ![The review dialog for custom events](/images/how_to_shopifyv2_integrate_meta_pixel_reviewcustomevents2.png)

3. **Click `Acknowledge`, then pick an action for each custom event.**

    ![Acknowledging the custom events](https://loom.com/i/6f49a0bcff394c7f85b35addc0cb4294?workflows_screenshot=true)

    Enable both `RetakeQuiz` and `EmailLead` to use either one in an audience.

4. **Click `Next`, then `Confirm`.**

    ![Confirming the custom events](https://loom.com/i/89174c089c514d7abc80f0e506581bbc?workflows_screenshot=true)

5. **Refresh the dashboard and check the notice has gone.** The custom events can then be used in your ads, custom audiences and lookalike audiences.

## Track your own events with code

=== "Shopify"

    The built-in integration sends the events listed on this page. To send an event of your own, write it in the `Custom JS` section of the results page or of a question.

    !!! warning "The callbacks do not exist in this version"

        `prqQuizCallback` belongs to the five older versions, not to Built for Shopify. Use `window.quiz` and the `quiz` context object here. See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

    1. **Open the results page and expand its `Custom JS` section.**

    2. **Call `fbq` with the event you want.** The `quiz` object holds the answers, the chosen results page and the recommended products.

        ```javascript
        // Runs when the results page renders
        window.fbq('trackCustom', 'QuizCompleted', {
          content_name: quiz.currentResult?.ref || '',
          content_category: 'quiz'
        });
        ```

    3. **Click the top-right `Save` button.**

    4. **Take the quiz, then check the event arrives in `Test events` in the Meta Events Manager.**

    !!! tip "Sending an event on every answer"

        Assign a handler to `window.quiz.onChange` in the `Custom JS` of the first question. It fires after every answer and stays registered for the rest of the quiz. See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

=== "Shopify (Legacy)"

    The built-in integration sends the events listed on this page. To send events of your own instead, use the [callback function](/how-to-guides/use-callback-function/) with `fbq`.

    1. **Turn the built-in integration off.** If you connected a Pixel in the [Connect](/reference/quiz-builder/connect-integrations/) tab, disconnect it and publish, so the same action is not counted twice.

    2. **Add the script to the page that holds the quiz.** To load it everywhere, put it in `theme.liquid`.

        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            window.fbq('trackCustom', 'QuizCompleted', {
                content_name: quizResponse.quiz.attributes.name,
                content_category: 'quiz'
            });
        }
        </script>
        ```

    3. **Change the event name and the parameters to whatever you want to record.** The first argument is the `fbq` action, `track` for a standard event or `trackCustom` for one of your own.

    4. **Take the quiz, then check the event arrives in `Test events` in the Meta Events Manager.**

    !!! tip "Sending an event on every answer"

        Add `prqSlideCallback` alongside it. It fires each time a customer answers a question. See [How to Use Callback Function](/how-to-guides/use-callback-function/).

=== "WooCommerce"

    The built-in integration sends the events listed on this page. To send events of your own instead, use the [callback function](/how-to-guides/use-callback-function/) with `fbq`.

    1. **Turn the built-in integration off.** If you connected a Pixel in the [Connect](/reference/quiz-builder/connect-integrations/) tab, disconnect it and publish, so the same action is not counted twice.

    2. **Add the script to the page that holds the quiz.** To load it everywhere, put it in your theme's main template.

        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            window.fbq('trackCustom', 'QuizCompleted', {
                content_name: quizResponse.quiz.attributes.name,
                content_category: 'quiz'
            });
        }
        </script>
        ```

    3. **Change the event name and the parameters to whatever you want to record.** The first argument is the `fbq` action, `track` for a standard event or `trackCustom` for one of your own.

    4. **Take the quiz, then check the event arrives in `Test events` in the Meta Events Manager.**

    !!! tip "Sending an event on every answer"

        Add `prqSlideCallback` alongside it. It fires each time a customer answers a question. See [How to Use Callback Function](/how-to-guides/use-callback-function/).

=== "Magento"

    The built-in integration sends the events listed on this page. To send events of your own instead, use the [callback function](/how-to-guides/use-callback-function/) with `fbq`.

    1. **Turn the built-in integration off.** If you connected a Pixel in the [Connect](/reference/quiz-builder/connect-integrations/) tab, disconnect it and publish, so the same action is not counted twice.

    2. **Add the script to the page that holds the quiz.** To load it everywhere, put it in your theme's main template.

        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            window.fbq('trackCustom', 'QuizCompleted', {
                content_name: quizResponse.quiz.attributes.name,
                content_category: 'quiz'
            });
        }
        </script>
        ```

    3. **Change the event name and the parameters to whatever you want to record.** The first argument is the `fbq` action, `track` for a standard event or `trackCustom` for one of your own.

    4. **Take the quiz, then check the event arrives in `Test events` in the Meta Events Manager.**

    !!! tip "Sending an event on every answer"

        Add `prqSlideCallback` alongside it. It fires each time a customer answers a question. See [How to Use Callback Function](/how-to-guides/use-callback-function/).

=== "BigCommerce"

    The built-in integration sends the events listed on this page. To send events of your own instead, use the [callback function](/how-to-guides/use-callback-function/) with `fbq`.

    1. **Turn the built-in integration off.** If you connected a Pixel in the [Connect](/reference/quiz-builder/connect-integrations/) tab, disconnect it and publish, so the same action is not counted twice.

    2. **Add the script to the page that holds the quiz.** To load it everywhere, put it in your theme's main template.

        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            window.fbq('trackCustom', 'QuizCompleted', {
                content_name: quizResponse.quiz.attributes.name,
                content_category: 'quiz'
            });
        }
        </script>
        ```

    3. **Change the event name and the parameters to whatever you want to record.** The first argument is the `fbq` action, `track` for a standard event or `trackCustom` for one of your own.

    4. **Take the quiz, then check the event arrives in `Test events` in the Meta Events Manager.**

    !!! tip "Sending an event on every answer"

        Add `prqSlideCallback` alongside it. It fires each time a customer answers a question. See [How to Use Callback Function](/how-to-guides/use-callback-function/).

=== "Standalone"

    The built-in integration sends the events listed on this page. To send events of your own instead, use the [callback function](/how-to-guides/use-callback-function/) with `fbq`.

    1. **Turn the built-in integration off.** If you connected a Pixel in the [Connect](/reference/quiz-builder/connect-integrations/) tab, disconnect it and publish, so the same action is not counted twice.

    2. **Add the script to the page that holds the quiz.** To load it everywhere, put it in your theme's main template.

        ```html
        <script>
        // Fires once, when the customer reaches the results page
        function prqQuizCallback(quizResponse){
            window.fbq('trackCustom', 'QuizCompleted', {
                content_name: quizResponse.quiz.attributes.name,
                content_category: 'quiz'
            });
        }
        </script>
        ```

    3. **Change the event name and the parameters to whatever you want to record.** The first argument is the `fbq` action, `track` for a standard event or `trackCustom` for one of your own.

    4. **Take the quiz, then check the event arrives in `Test events` in the Meta Events Manager.**

    !!! tip "Sending an event on every answer"

        Add `prqSlideCallback` alongside it. It fires each time a customer answers a question. See [How to Use Callback Function](/how-to-guides/use-callback-function/).

---

This article explains how to connect the Meta Pixel to your quiz, and which events the quiz then sends. It also covers sending events of your own.