---
description: "Learn how to integrate Google Analytics with your RevenueHunt quiz to track user engagement and minimize abandonment rates."
icon: material/google-analytics
---

# How to Track Quiz Performance with Google Analytics

Google Analytics shows you how customers move through your quiz, and where they leave it.

=== "Shopify"

    The Built for Shopify version has GA4 event tracking built in. Turn it on in the quiz, and the events reach the GA4 property your store already uses.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/8P-kANzya2g?si=L-rMRoSRsdbwSgof" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "GA4 can drop events that fired correctly"

        Since Google moved from Universal Analytics to GA4, event tracking has become less reliable. The code can be right, and the events can fire, and GA4 can still fail to read, process or report them.

        If that happens, contact Google Support. The problem is usually on their side.

=== "Shopify (Legacy)"

    This version sends GA4 events once you connect the quiz to Google Analytics. You can add events of your own on top, with a custom script.

    !!! warning "GA4 can drop events that fired correctly"

        Since Google moved from Universal Analytics to GA4, event tracking has become less reliable. The code can be right, and the events can fire, and GA4 can still fail to read, process or report them.

        If that happens, contact Google Support. The problem is usually on their side.

=== "WooCommerce"

    This version sends GA4 events once you connect the quiz to Google Analytics. You can add events of your own on top, with a custom script.

    !!! warning "GA4 can drop events that fired correctly"

        Since Google moved from Universal Analytics to GA4, event tracking has become less reliable. The code can be right, and the events can fire, and GA4 can still fail to read, process or report them.

        If that happens, contact Google Support. The problem is usually on their side.

=== "Magento"

    This version sends GA4 events once you connect the quiz to Google Analytics. You can add events of your own on top, with a custom script.

    !!! warning "GA4 can drop events that fired correctly"

        Since Google moved from Universal Analytics to GA4, event tracking has become less reliable. The code can be right, and the events can fire, and GA4 can still fail to read, process or report them.

        If that happens, contact Google Support. The problem is usually on their side.

=== "BigCommerce"

    This version sends GA4 events once you connect the quiz to Google Analytics. You can add events of your own on top, with a custom script.

    !!! warning "GA4 can drop events that fired correctly"

        Since Google moved from Universal Analytics to GA4, event tracking has become less reliable. The code can be right, and the events can fire, and GA4 can still fail to read, process or report them.

        If that happens, contact Google Support. The problem is usually on their side.

=== "Standalone"

    This version sends GA4 events once you connect the quiz to Google Analytics. You can add events of your own on top, with a custom script.

    !!! warning "GA4 can drop events that fired correctly"

        Since Google moved from Universal Analytics to GA4, event tracking has become less reliable. The code can be right, and the events can fire, and GA4 can still fail to read, process or report them.

        If that happens, contact Google Support. The problem is usually on their side.

## Connect the quiz to Google Analytics

=== "Shopify"

    !!! note "Give the quiz its own page"

        GA4 tracking works best when the quiz sits on a page of its own. See [how to embed an inline quiz on your store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Set up GA4 on your website first.**

        !!! tip "Finding your GA4 tracking code"

            See the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).

    2. **Open your quiz and go to the [Integrations](/reference/quiz-builder/connect-integrations/) tab.**

    3. **Find the Google Analytics section and click `Activate`.**

        ![Activating Google Analytics in the Integrations tab](/images/how_to_integrate_ga4_shopify_v2.png)

    4. **Click `Save`.**

    5. **Take the quiz, then open `Realtime` in GA4 and check the quiz events arrive.**

    The quiz connects to the GA4 tracking code already on your website, so there is no Measurement ID to enter. Reports other than `Realtime` can take up to 72 hours to fill in.

=== "Shopify (Legacy)"

    !!! note "Give the quiz its own page"

        GA4 tracking works best when the quiz sits on a page of its own. See [how to embed an inline quiz on your store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Set up GA4 on your website first.**

        !!! tip "Finding your GA4 tracking code"

            See the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).

    2. **Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.** GA4 has to be ready before the quiz starts sending to it.

    3. **Open your quiz and go to the [Connect](/reference/quiz-builder/connect-integrations/) tab.**

    4. **Find Google Analytics and click `Connect`.**

    5. **Take the quiz, then open `Realtime` in GA4 and check the quiz events arrive.**

    The quiz sends to whichever GA4 property your `gtag.js` is configured with, so there is no Measurement ID to enter. Reports other than `Realtime` can take up to 72 hours to fill in.

=== "WooCommerce"

    !!! note "Give the quiz its own page"

        GA4 tracking works best when the quiz sits on a page of its own. See [how to embed an inline quiz on your store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Set up GA4 on your website first.**

        !!! tip "Finding your GA4 tracking code"

            See the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).

    2. **Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.** GA4 has to be ready before the quiz starts sending to it.

    3. **Open your quiz and go to the [Connect](/reference/quiz-builder/connect-integrations/) tab.**

    4. **Find Google Analytics and click `Connect`.**

    5. **Take the quiz, then open `Realtime` in GA4 and check the quiz events arrive.**

    The quiz sends to whichever GA4 property your `gtag.js` is configured with, so there is no Measurement ID to enter. Reports other than `Realtime` can take up to 72 hours to fill in.

=== "Magento"

    !!! note "Give the quiz its own page"

        GA4 tracking works best when the quiz sits on a page of its own. See [how to embed an inline quiz on your store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Set up GA4 on your website first.**

        !!! tip "Finding your GA4 tracking code"

            See the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).

    2. **Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.** GA4 has to be ready before the quiz starts sending to it.

    3. **Open your quiz and go to the [Connect](/reference/quiz-builder/connect-integrations/) tab.**

    4. **Find Google Analytics and click `Connect`.**

    5. **Take the quiz, then open `Realtime` in GA4 and check the quiz events arrive.**

    The quiz sends to whichever GA4 property your `gtag.js` is configured with, so there is no Measurement ID to enter. Reports other than `Realtime` can take up to 72 hours to fill in.

=== "BigCommerce"

    !!! note "Give the quiz its own page"

        GA4 tracking works best when the quiz sits on a page of its own. See [how to embed an inline quiz on your store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Set up GA4 on your website first.**

        !!! tip "Finding your GA4 tracking code"

            See the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).

    2. **Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.** GA4 has to be ready before the quiz starts sending to it.

    3. **Open your quiz and go to the [Connect](/reference/quiz-builder/connect-integrations/) tab.**

    4. **Find Google Analytics and click `Connect`.**

    5. **Take the quiz, then open `Realtime` in GA4 and check the quiz events arrive.**

    The quiz sends to whichever GA4 property your `gtag.js` is configured with, so there is no Measurement ID to enter. Reports other than `Realtime` can take up to 72 hours to fill in.

=== "Standalone"

    !!! note "Give the quiz its own page"

        GA4 tracking works best when the quiz sits on a page of its own. See [how to embed an inline quiz on your store](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Set up GA4 on your website first.**

        !!! tip "Finding your GA4 tracking code"

            See the [Google Analytics setup documentation](https://support.google.com/analytics/answer/1008080).

    2. **Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.** GA4 has to be ready before the quiz starts sending to it.

    3. **Open your quiz and go to the [Connect](/reference/quiz-builder/connect-integrations/) tab.**

    4. **Find Google Analytics and click `Connect`.**

    5. **Take the quiz, then open `Realtime` in GA4 and check the quiz events arrive.**

    The quiz sends to whichever GA4 property your `gtag.js` is configured with, so there is no Measurement ID to enter. Reports other than `Realtime` can take up to 72 hours to fill in.

## Track customer behavior (events)

Once the quiz is connected, an event fires at each step of the quiz. They appear in Google Analytics under `Reports > View user engagement and retention > Events`. Click an event name to open it.

=== "Shopify"

    ![Quiz events in Google Analytics](/images/how_to_shopifyv2_events.png)

    | Trigger | Event name | Event parameters |
    |---|---|---|
    | The customer starts a quiz, by clicking the button on the first or welcome question | quiz_started_{quiz_name} | quiz_name |
    | The customer views a question | question_viewed_{question_title} | question_title |
    | The customer clicks a choice, or picks a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | The customer answers the email question | email_lead_{quiz_name} | quiz_name |
    | The customer answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | The customer reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | The customer completes the quiz | generate_lead | quiz_name |
    | The customer clicks a product, by its image or its view-product button | product_clicked_{product_name} | product_name |
    | The customer adds a product to the cart, by `Add to cart` or `Add all to cart` | product_added_to_cart_{product_name} | product_name |
    | The customer proceeds to the cart or the checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | The customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! info "Reading the event names"

        Each name carries its main parameter, so the value shows up in the GA4 `Event name` report without any setup. To use the other parameters as report columns, such as `question_title` or `question_ref`, register them as custom dimensions under `Admin > Custom definitions`.

    !!! info "generate_lead is a standard GA4 conversion event"

        It is the one name with no `_{...}` suffix, so that GA4 can treat it as a conversion. Mark it as a key event under `Admin > Events` to count it as one.

    !!! warning "A question title can hold an unresolved recall token"

        `question_title`, and the `question_viewed_{question_title}` event name, carry the raw title. If a question recalls an earlier answer, the raw title holds a token such as `{{slide:x1i0d83}}`, and that token reaches GA4 rather than the answer.

        The token is stable. It does not change for a customer, or when you edit the quiz, so it groups correctly. It is just not readable.

    !!! note "The older event names are gone"

        `view`, `click`, `submit` and `recommendation`, with their `event_category` and `event_label` parameters, are no longer sent. The quiz sends the events listed here instead.

    !!! warning "Give the data time to appear"

        Check `Realtime` in GA4 first. The other reports can take up to 72 hours to process the data.

=== "Shopify (Legacy)"

    ![Quiz events in Google Analytics](/images/how_to_shopifyv2_events.png)

    | Trigger | Event name | Event parameters |
    |---|---|---|
    | The customer starts a quiz, by clicking the button on the first or welcome question | quiz_started_{quiz_name} | quiz_name |
    | The customer views a question | question_viewed_{question_title} | question_title |
    | The customer clicks a choice, or picks a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | The customer answers the email question | email_lead_{quiz_name} | quiz_name |
    | The customer answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | The customer reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | The customer completes the quiz | generate_lead | quiz_name |
    | The customer clicks a product, by its image or its view-product button | product_clicked_{product_name} | product_name |
    | The customer adds a product to the cart, by `Add to cart` or `Add all to cart` | product_added_to_cart_{product_name} | product_name |
    | The customer proceeds to the cart or the checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | The customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! info "Reading the event names"

        Each name carries its main parameter, so the value shows up in the GA4 `Event name` report without any setup. To use the other parameters as report columns, such as `question_title` or `question_ref`, register them as custom dimensions under `Admin > Custom definitions`.

    !!! info "generate_lead is a standard GA4 conversion event"

        It is the one name with no `_{...}` suffix, so that GA4 can treat it as a conversion. Mark it as a key event under `Admin > Events` to count it as one.

    !!! warning "A question title can hold an unresolved recall token"

        `question_title`, and the `question_viewed_{question_title}` event name, carry the raw title. If a question recalls an earlier answer, the raw title holds a token such as `{{slide:x1i0d83}}`, and that token reaches GA4 rather than the answer.

        The token is stable. It does not change for a customer, or when you edit the quiz, so it groups correctly. It is just not readable.

    !!! note "The older event names are gone"

        `view`, `click`, `submit` and `recommendation`, with their `event_category` and `event_label` parameters, are no longer sent. The quiz sends the events listed here instead.

    !!! warning "Give the data time to appear"

        Check `Realtime` in GA4 first. The other reports can take up to 72 hours to process the data.

    !!! tip "No events at all"

        Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.

=== "WooCommerce"

    ![Quiz events in Google Analytics](/images/how_to_shopifyv2_events.png)

    | Trigger | Event name | Event parameters |
    |---|---|---|
    | The customer starts a quiz, by clicking the button on the first or welcome question | quiz_started_{quiz_name} | quiz_name |
    | The customer views a question | question_viewed_{question_title} | question_title |
    | The customer clicks a choice, or picks a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | The customer answers the email question | email_lead_{quiz_name} | quiz_name |
    | The customer answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | The customer reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | The customer completes the quiz | generate_lead | quiz_name |
    | The customer clicks a product, by its image or its view-product button | product_clicked_{product_name} | product_name |
    | The customer adds a product to the cart, by `Add to cart` or `Add all to cart` | product_added_to_cart_{product_name} | product_name |
    | The customer proceeds to the cart or the checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | The customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! info "Reading the event names"

        Each name carries its main parameter, so the value shows up in the GA4 `Event name` report without any setup. To use the other parameters as report columns, such as `question_title` or `question_ref`, register them as custom dimensions under `Admin > Custom definitions`.

    !!! info "generate_lead is a standard GA4 conversion event"

        It is the one name with no `_{...}` suffix, so that GA4 can treat it as a conversion. Mark it as a key event under `Admin > Events` to count it as one.

    !!! warning "A question title can hold an unresolved recall token"

        `question_title`, and the `question_viewed_{question_title}` event name, carry the raw title. If a question recalls an earlier answer, the raw title holds a token such as `{{slide:x1i0d83}}`, and that token reaches GA4 rather than the answer.

        The token is stable. It does not change for a customer, or when you edit the quiz, so it groups correctly. It is just not readable.

    !!! note "The older event names are gone"

        `view`, `click`, `submit` and `recommendation`, with their `event_category` and `event_label` parameters, are no longer sent. The quiz sends the events listed here instead.

    !!! warning "Give the data time to appear"

        Check `Realtime` in GA4 first. The other reports can take up to 72 hours to process the data.

    !!! tip "No events at all"

        Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.

=== "Magento"

    ![Quiz events in Google Analytics](/images/how_to_shopifyv2_events.png)

    | Trigger | Event name | Event parameters |
    |---|---|---|
    | The customer starts a quiz, by clicking the button on the first or welcome question | quiz_started_{quiz_name} | quiz_name |
    | The customer views a question | question_viewed_{question_title} | question_title |
    | The customer clicks a choice, or picks a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | The customer answers the email question | email_lead_{quiz_name} | quiz_name |
    | The customer answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | The customer reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | The customer completes the quiz | generate_lead | quiz_name |
    | The customer clicks a product, by its image or its view-product button | product_clicked_{product_name} | product_name |
    | The customer adds a product to the cart, by `Add to cart` or `Add all to cart` | product_added_to_cart_{product_name} | product_name |
    | The customer proceeds to the cart or the checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | The customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! info "Reading the event names"

        Each name carries its main parameter, so the value shows up in the GA4 `Event name` report without any setup. To use the other parameters as report columns, such as `question_title` or `question_ref`, register them as custom dimensions under `Admin > Custom definitions`.

    !!! info "generate_lead is a standard GA4 conversion event"

        It is the one name with no `_{...}` suffix, so that GA4 can treat it as a conversion. Mark it as a key event under `Admin > Events` to count it as one.

    !!! warning "A question title can hold an unresolved recall token"

        `question_title`, and the `question_viewed_{question_title}` event name, carry the raw title. If a question recalls an earlier answer, the raw title holds a token such as `{{slide:x1i0d83}}`, and that token reaches GA4 rather than the answer.

        The token is stable. It does not change for a customer, or when you edit the quiz, so it groups correctly. It is just not readable.

    !!! note "The older event names are gone"

        `view`, `click`, `submit` and `recommendation`, with their `event_category` and `event_label` parameters, are no longer sent. The quiz sends the events listed here instead.

    !!! warning "Give the data time to appear"

        Check `Realtime` in GA4 first. The other reports can take up to 72 hours to process the data.

    !!! tip "No events at all"

        Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.

=== "BigCommerce"

    ![Quiz events in Google Analytics](/images/how_to_shopifyv2_events.png)

    | Trigger | Event name | Event parameters |
    |---|---|---|
    | The customer starts a quiz, by clicking the button on the first or welcome question | quiz_started_{quiz_name} | quiz_name |
    | The customer views a question | question_viewed_{question_title} | question_title |
    | The customer clicks a choice, or picks a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | The customer answers the email question | email_lead_{quiz_name} | quiz_name |
    | The customer answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | The customer reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | The customer completes the quiz | generate_lead | quiz_name |
    | The customer clicks a product, by its image or its view-product button | product_clicked_{product_name} | product_name |
    | The customer adds a product to the cart, by `Add to cart` or `Add all to cart` | product_added_to_cart_{product_name} | product_name |
    | The customer proceeds to the cart or the checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | The customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! info "Reading the event names"

        Each name carries its main parameter, so the value shows up in the GA4 `Event name` report without any setup. To use the other parameters as report columns, such as `question_title` or `question_ref`, register them as custom dimensions under `Admin > Custom definitions`.

    !!! info "generate_lead is a standard GA4 conversion event"

        It is the one name with no `_{...}` suffix, so that GA4 can treat it as a conversion. Mark it as a key event under `Admin > Events` to count it as one.

    !!! warning "A question title can hold an unresolved recall token"

        `question_title`, and the `question_viewed_{question_title}` event name, carry the raw title. If a question recalls an earlier answer, the raw title holds a token such as `{{slide:x1i0d83}}`, and that token reaches GA4 rather than the answer.

        The token is stable. It does not change for a customer, or when you edit the quiz, so it groups correctly. It is just not readable.

    !!! note "The older event names are gone"

        `view`, `click`, `submit` and `recommendation`, with their `event_category` and `event_label` parameters, are no longer sent. The quiz sends the events listed here instead.

    !!! warning "Give the data time to appear"

        Check `Realtime` in GA4 first. The other reports can take up to 72 hours to process the data.

    !!! tip "No events at all"

        Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.

=== "Standalone"

    ![Quiz events in Google Analytics](/images/how_to_shopifyv2_events.png)

    | Trigger | Event name | Event parameters |
    |---|---|---|
    | The customer starts a quiz, by clicking the button on the first or welcome question | quiz_started_{quiz_name} | quiz_name |
    | The customer views a question | question_viewed_{question_title} | question_title |
    | The customer clicks a choice, or picks a dropdown option | block_answered_{choice_text} | choice_text, question_title, question_ref |
    | The customer answers the email question | email_lead_{quiz_name} | quiz_name |
    | The customer answers the phone question | phone_lead_{quiz_name} | quiz_name |
    | The customer reaches the results page | results_page_viewed_{results_page_title} | results_page_title |
    | The customer completes the quiz | generate_lead | quiz_name |
    | The customer clicks a product, by its image or its view-product button | product_clicked_{product_name} | product_name |
    | The customer adds a product to the cart, by `Add to cart` or `Add all to cart` | product_added_to_cart_{product_name} | product_name |
    | The customer proceeds to the cart or the checkout | proceed_to_checkout_{quiz_name} | quiz_name |
    | The customer retakes the quiz | quiz_retake_quiz_{quiz_name} | quiz_name |

    !!! info "Reading the event names"

        Each name carries its main parameter, so the value shows up in the GA4 `Event name` report without any setup. To use the other parameters as report columns, such as `question_title` or `question_ref`, register them as custom dimensions under `Admin > Custom definitions`.

    !!! info "generate_lead is a standard GA4 conversion event"

        It is the one name with no `_{...}` suffix, so that GA4 can treat it as a conversion. Mark it as a key event under `Admin > Events` to count it as one.

    !!! warning "A question title can hold an unresolved recall token"

        `question_title`, and the `question_viewed_{question_title}` event name, carry the raw title. If a question recalls an earlier answer, the raw title holds a token such as `{{slide:x1i0d83}}`, and that token reaches GA4 rather than the answer.

        The token is stable. It does not change for a customer, or when you edit the quiz, so it groups correctly. It is just not readable.

    !!! note "The older event names are gone"

        `view`, `click`, `submit` and `recommendation`, with their `event_category` and `event_label` parameters, are no longer sent. The quiz sends the events listed here instead.

    !!! warning "Give the data time to appear"

        Check `Realtime` in GA4 first. The other reports can take up to 72 hours to process the data.

    !!! tip "No events at all"

        Check that your `gtag.js` snippet loads before the RevenueHunt `embed.js` snippet.

## Add your own events

The events above arrive without any code. Add a script only for something they do not cover.

=== "Shopify"

    The quiz gives your code a `window.quiz` object, in the `Custom JS` section of a question or of the results page. It takes plain JavaScript, with no `<script>` tags, and runs in the preview and the live quiz but not in the builder.

    !!! warning "The callbacks do not exist in this version"

        `prqQuizCallback` and `prqSlideCallback` belong to the five older versions, not to Built for Shopify. Use `window.quiz` here.

    **Track every answer.** Open the first question, expand its `Custom JS` section, and assign a handler to `window.quiz.onChange`. It fires after every answer, and stays registered for the rest of the quiz.

    ```javascript
    // Fires after every answer the customer gives
    window.quiz.onChange = function (event) {
      gtag('event', 'quiz_question_answered', {
        event_category: 'quiz',
        question_ref: event.questionRef,
        // selectedLabel is the readable choice text, so no choice-ID mapping is needed
        answer: event.selectedLabel || event.value
      });
    };
    ```

    The `event` object holds `questionRef`, `blockRef`, `type`, `choicesRefs`, `value`, `isValid`, `selectedIndex` and `selectedLabel`.

    **Track quiz completion.** Open the `Custom JS` section of the results page and call `gtag()` directly. It runs when the results page renders.

    ```javascript
    gtag('event', 'quiz_completed', { event_category: 'quiz' });
    ```

    **Check it works.** Take the quiz, then look under `Reports > Engagement > Events` in GA4, or in `Realtime`.

=== "Shopify (Legacy)"

    Your own events come from the [callback functions](/how-to-guides/use-callback-function/), in a script on the page that holds the quiz. To load it everywhere, put it in your theme's main template.

    !!! warning "Before you paste it in"

        - Your GA4 `gtag.js` snippet must load before the RevenueHunt `embed.js` snippet.
        - The built-in events and this script both fire once the quiz is connected. To avoid counting twice, either disconnect the built-in integration and use the script alone, or delete the events you do not want from the script.

    **Only quiz completion.** If all you need is to know that a customer finished, one callback does it.

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

    **Everything the quiz does.** The script below sends the quiz start, every answer, the results page, each recommended product, and each add to cart, as its own GA4 event. It replaces the completion-only callback rather than sitting alongside it.

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
      // The add-to-cart event carries sku / origin_id / variant_id; name and price are
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

    !!! note "Why quiz_results and quiz_product_recommended are separate"

        A results page can recommend more than one product. Firing the results event once, and a per-product event alongside it, keeps the count of customers who reached the results page accurate. Fire one combined event per product instead and that count multiplies by the number of products shown.

    !!! tip "Using the parameters in reports"

        `quiz_name`, `question_title`, `answer`, `product_name` and the rest are ordinary GA4 event parameters. Register the ones you need as custom dimensions under `Admin > Custom definitions`.

    **Check it works.** Take the quiz, then look under `Reports > Engagement > Events` in GA4, or in `Realtime`.

=== "WooCommerce"

    Your own events come from the [callback functions](/how-to-guides/use-callback-function/), in a script on the page that holds the quiz. To load it everywhere, put it in your theme's main template.

    !!! warning "Before you paste it in"

        - Your GA4 `gtag.js` snippet must load before the RevenueHunt `embed.js` snippet.
        - The built-in events and this script both fire once the quiz is connected. To avoid counting twice, either disconnect the built-in integration and use the script alone, or delete the events you do not want from the script.

    **Only quiz completion.** If all you need is to know that a customer finished, one callback does it.

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

    **Everything the quiz does.** The script below sends the quiz start, every answer, the results page, each recommended product, and each add to cart, as its own GA4 event. It replaces the completion-only callback rather than sitting alongside it.

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
      // The add-to-cart event carries sku / origin_id / variant_id; name and price are
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

    !!! note "Why quiz_results and quiz_product_recommended are separate"

        A results page can recommend more than one product. Firing the results event once, and a per-product event alongside it, keeps the count of customers who reached the results page accurate. Fire one combined event per product instead and that count multiplies by the number of products shown.

    !!! tip "Using the parameters in reports"

        `quiz_name`, `question_title`, `answer`, `product_name` and the rest are ordinary GA4 event parameters. Register the ones you need as custom dimensions under `Admin > Custom definitions`.

    **Check it works.** Take the quiz, then look under `Reports > Engagement > Events` in GA4, or in `Realtime`.

=== "Magento"

    Your own events come from the [callback functions](/how-to-guides/use-callback-function/), in a script on the page that holds the quiz. To load it everywhere, put it in your theme's main template.

    !!! warning "Before you paste it in"

        - Your GA4 `gtag.js` snippet must load before the RevenueHunt `embed.js` snippet.
        - The built-in events and this script both fire once the quiz is connected. To avoid counting twice, either disconnect the built-in integration and use the script alone, or delete the events you do not want from the script.

    **Only quiz completion.** If all you need is to know that a customer finished, one callback does it.

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

    **Everything the quiz does.** The script below sends the quiz start, every answer, the results page, each recommended product, and each add to cart, as its own GA4 event. It replaces the completion-only callback rather than sitting alongside it.

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
      // The add-to-cart event carries sku / origin_id / variant_id; name and price are
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

    !!! note "Why quiz_results and quiz_product_recommended are separate"

        A results page can recommend more than one product. Firing the results event once, and a per-product event alongside it, keeps the count of customers who reached the results page accurate. Fire one combined event per product instead and that count multiplies by the number of products shown.

    !!! tip "Using the parameters in reports"

        `quiz_name`, `question_title`, `answer`, `product_name` and the rest are ordinary GA4 event parameters. Register the ones you need as custom dimensions under `Admin > Custom definitions`.

    **Check it works.** Take the quiz, then look under `Reports > Engagement > Events` in GA4, or in `Realtime`.

=== "BigCommerce"

    Your own events come from the [callback functions](/how-to-guides/use-callback-function/), in a script on the page that holds the quiz. To load it everywhere, put it in your theme's main template.

    !!! warning "Before you paste it in"

        - Your GA4 `gtag.js` snippet must load before the RevenueHunt `embed.js` snippet.
        - The built-in events and this script both fire once the quiz is connected. To avoid counting twice, either disconnect the built-in integration and use the script alone, or delete the events you do not want from the script.

    **Only quiz completion.** If all you need is to know that a customer finished, one callback does it.

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

    **Everything the quiz does.** The script below sends the quiz start, every answer, the results page, each recommended product, and each add to cart, as its own GA4 event. It replaces the completion-only callback rather than sitting alongside it.

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
      // The add-to-cart event carries sku / origin_id / variant_id; name and price are
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

    !!! note "Why quiz_results and quiz_product_recommended are separate"

        A results page can recommend more than one product. Firing the results event once, and a per-product event alongside it, keeps the count of customers who reached the results page accurate. Fire one combined event per product instead and that count multiplies by the number of products shown.

    !!! tip "Using the parameters in reports"

        `quiz_name`, `question_title`, `answer`, `product_name` and the rest are ordinary GA4 event parameters. Register the ones you need as custom dimensions under `Admin > Custom definitions`.

    **Check it works.** Take the quiz, then look under `Reports > Engagement > Events` in GA4, or in `Realtime`.

=== "Standalone"

    Your own events come from the [callback functions](/how-to-guides/use-callback-function/), in a script on the page that holds the quiz. To load it everywhere, put it in your theme's main template.

    !!! warning "Before you paste it in"

        - Your GA4 `gtag.js` snippet must load before the RevenueHunt `embed.js` snippet.
        - The built-in events and this script both fire once the quiz is connected. To avoid counting twice, either disconnect the built-in integration and use the script alone, or delete the events you do not want from the script.

    **Only quiz completion.** If all you need is to know that a customer finished, one callback does it.

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

    **Everything the quiz does.** The script below sends the quiz start, every answer, the results page, each recommended product, and each add to cart, as its own GA4 event. It replaces the completion-only callback rather than sitting alongside it.

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
      // The add-to-cart event carries sku / origin_id / variant_id; name and price are
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

    !!! note "Why quiz_results and quiz_product_recommended are separate"

        A results page can recommend more than one product. Firing the results event once, and a per-product event alongside it, keeps the count of customers who reached the results page accurate. Fire one combined event per product instead and that count multiplies by the number of products shown.

    !!! tip "Using the parameters in reports"

        `quiz_name`, `question_title`, `answer`, `product_name` and the rest are ordinary GA4 event parameters. Register the ones you need as custom dimensions under `Admin > Custom definitions`.

    **Check it works.** Take the quiz, then look under `Reports > Engagement > Events` in GA4, or in `Realtime`.

## Track quiz revenue

GA4 does not tie quiz events to purchases on its own. Build a segment of the customers who started a quiz, then read the purchase revenue for that segment.

=== "Shopify"

    **Compare quiz customers with everyone else**

    ![A Free form exploration comparing quiz users with all users](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)

    ![The revenue and purchase columns of that exploration](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Build the quiz segment.** In the `Variables` panel, under `Segments`, click `+` and choose `User segment`. Include users where `Event name` `contains` `quiz_started`, or use `matches regex` with `^quiz_started_.*$`. Name it `Quiz Users`, then click `Save and apply`.

    3. **Add the default `All Users` segment too**, so you have something to compare against.

    4. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count`, `Purchases` and `Total revenue` under `Metrics`.

    5. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users` and `Quiz Users` |
        | `Rows` | `Event name` |
        | `Columns` | Leave empty, or set `Segment` for a side-by-side comparison |
        | `Values` | `Event count`, `Purchases`, `Total revenue` |
        | `Filters` | `Event name` contains `quiz_started` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    6. **Read the table.** It shows the revenue and purchases from customers who triggered `quiz_started`, next to the figures for everyone.

    7. **Rename the exploration**, to something like `Quiz Revenue`, **then star or share it** so your teammates can find it.

    !!! tip "Narrowing it further"

        - **One quiz at a time.** Set `Filters` to `Event name` contains that quiz, such as `quiz_started_skincare_quiz_usa`.
        - **One quiz page.** If the quiz has a page of its own, build the segment on `Page location` contains that path instead, such as `/pages/skin-quiz`.

    **Attribute revenue with UTM parameters**

    Tag the links into your quiz with `utm_source=quiz` or `utm_campaign=quiz_name`. Revenue then appears in the GA4 `Advertising > Attribution > Model comparison` report, and under `Engagement > Conversions > Event name > purchase`.

    ![The purchase event in the GA4 conversions report](/images/how_to_ga_revenue2.png)

    Add a `Source` column beside the default channel grouping, then look for the rows with the `revenuehunt` source.

    ![The source column showing revenuehunt](/images/how_to_ga_events.png)

    !!! tip "More from Google"

        See the Google Analytics documentation on [tracking revenue from events](https://support.google.com/analytics/answer/9216061?hl=en).

=== "Shopify (Legacy)"

    **Compare quiz customers with everyone else**

    ![A Free form exploration comparing quiz users with all users](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)

    ![The revenue and purchase columns of that exploration](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Build the quiz segment.** In the `Variables` panel, under `Segments`, click `+` and choose `User segment`. Include users where `Event name` `contains` `quiz_started`, or use `matches regex` with `^quiz_started_.*$`. Name it `Quiz Users`, then click `Save and apply`.

    3. **Add the default `All Users` segment too**, so you have something to compare against.

    4. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count`, `Purchases` and `Total revenue` under `Metrics`.

    5. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users` and `Quiz Users` |
        | `Rows` | `Event name` |
        | `Columns` | Leave empty, or set `Segment` for a side-by-side comparison |
        | `Values` | `Event count`, `Purchases`, `Total revenue` |
        | `Filters` | `Event name` contains `quiz_started` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    6. **Read the table.** It shows the revenue and purchases from customers who triggered `quiz_started`, next to the figures for everyone.

    7. **Rename the exploration**, to something like `Quiz Revenue`, **then star or share it** so your teammates can find it.

    !!! tip "Narrowing it further"

        - **One quiz at a time.** Set `Filters` to `Event name` contains that quiz, such as `quiz_started_skincare_quiz_usa`.
        - **One quiz page.** If the quiz has a page of its own, build the segment on `Page location` contains that path instead, such as `/pages/skin-quiz`.

    **Attribute revenue with UTM parameters**

    Tag the links into your quiz with `utm_source=quiz` or `utm_campaign=quiz_name`. Revenue then appears in the GA4 `Advertising > Attribution > Model comparison` report, and under `Engagement > Conversions > Event name > purchase`.

    ![The purchase event in the GA4 conversions report](/images/how_to_ga_revenue2.png)

    Add a `Source` column beside the default channel grouping, then look for the rows with the `revenuehunt` source.

    ![The source column showing revenuehunt](/images/how_to_ga_events.png)

    !!! tip "More from Google"

        See the Google Analytics documentation on [tracking revenue from events](https://support.google.com/analytics/answer/9216061?hl=en).

=== "WooCommerce"

    **Compare quiz customers with everyone else**

    ![A Free form exploration comparing quiz users with all users](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)

    ![The revenue and purchase columns of that exploration](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Build the quiz segment.** In the `Variables` panel, under `Segments`, click `+` and choose `User segment`. Include users where `Event name` `contains` `quiz_started`, or use `matches regex` with `^quiz_started_.*$`. Name it `Quiz Users`, then click `Save and apply`.

    3. **Add the default `All Users` segment too**, so you have something to compare against.

    4. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count`, `Purchases` and `Total revenue` under `Metrics`.

    5. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users` and `Quiz Users` |
        | `Rows` | `Event name` |
        | `Columns` | Leave empty, or set `Segment` for a side-by-side comparison |
        | `Values` | `Event count`, `Purchases`, `Total revenue` |
        | `Filters` | `Event name` contains `quiz_started` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    6. **Read the table.** It shows the revenue and purchases from customers who triggered `quiz_started`, next to the figures for everyone.

    7. **Rename the exploration**, to something like `Quiz Revenue`, **then star or share it** so your teammates can find it.

    !!! tip "Narrowing it further"

        - **One quiz at a time.** Set `Filters` to `Event name` contains that quiz, such as `quiz_started_skincare_quiz_usa`.
        - **One quiz page.** If the quiz has a page of its own, build the segment on `Page location` contains that path instead, such as `/pages/skin-quiz`.

    **Attribute revenue with UTM parameters**

    Tag the links into your quiz with `utm_source=quiz` or `utm_campaign=quiz_name`. Revenue then appears in the GA4 `Advertising > Attribution > Model comparison` report, and under `Engagement > Conversions > Event name > purchase`.

    ![The purchase event in the GA4 conversions report](/images/how_to_ga_revenue2.png)

    Add a `Source` column beside the default channel grouping, then look for the rows with the `revenuehunt` source.

    ![The source column showing revenuehunt](/images/how_to_ga_events.png)

    !!! tip "More from Google"

        See the Google Analytics documentation on [tracking revenue from events](https://support.google.com/analytics/answer/9216061?hl=en).

=== "Magento"

    **Compare quiz customers with everyone else**

    ![A Free form exploration comparing quiz users with all users](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)

    ![The revenue and purchase columns of that exploration](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Build the quiz segment.** In the `Variables` panel, under `Segments`, click `+` and choose `User segment`. Include users where `Event name` `contains` `quiz_started`, or use `matches regex` with `^quiz_started_.*$`. Name it `Quiz Users`, then click `Save and apply`.

    3. **Add the default `All Users` segment too**, so you have something to compare against.

    4. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count`, `Purchases` and `Total revenue` under `Metrics`.

    5. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users` and `Quiz Users` |
        | `Rows` | `Event name` |
        | `Columns` | Leave empty, or set `Segment` for a side-by-side comparison |
        | `Values` | `Event count`, `Purchases`, `Total revenue` |
        | `Filters` | `Event name` contains `quiz_started` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    6. **Read the table.** It shows the revenue and purchases from customers who triggered `quiz_started`, next to the figures for everyone.

    7. **Rename the exploration**, to something like `Quiz Revenue`, **then star or share it** so your teammates can find it.

    !!! tip "Narrowing it further"

        - **One quiz at a time.** Set `Filters` to `Event name` contains that quiz, such as `quiz_started_skincare_quiz_usa`.
        - **One quiz page.** If the quiz has a page of its own, build the segment on `Page location` contains that path instead, such as `/pages/skin-quiz`.

    **Attribute revenue with UTM parameters**

    Tag the links into your quiz with `utm_source=quiz` or `utm_campaign=quiz_name`. Revenue then appears in the GA4 `Advertising > Attribution > Model comparison` report, and under `Engagement > Conversions > Event name > purchase`.

    ![The purchase event in the GA4 conversions report](/images/how_to_ga_revenue2.png)

    Add a `Source` column beside the default channel grouping, then look for the rows with the `revenuehunt` source.

    ![The source column showing revenuehunt](/images/how_to_ga_events.png)

    !!! tip "More from Google"

        See the Google Analytics documentation on [tracking revenue from events](https://support.google.com/analytics/answer/9216061?hl=en).

=== "BigCommerce"

    **Compare quiz customers with everyone else**

    ![A Free form exploration comparing quiz users with all users](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)

    ![The revenue and purchase columns of that exploration](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Build the quiz segment.** In the `Variables` panel, under `Segments`, click `+` and choose `User segment`. Include users where `Event name` `contains` `quiz_started`, or use `matches regex` with `^quiz_started_.*$`. Name it `Quiz Users`, then click `Save and apply`.

    3. **Add the default `All Users` segment too**, so you have something to compare against.

    4. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count`, `Purchases` and `Total revenue` under `Metrics`.

    5. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users` and `Quiz Users` |
        | `Rows` | `Event name` |
        | `Columns` | Leave empty, or set `Segment` for a side-by-side comparison |
        | `Values` | `Event count`, `Purchases`, `Total revenue` |
        | `Filters` | `Event name` contains `quiz_started` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    6. **Read the table.** It shows the revenue and purchases from customers who triggered `quiz_started`, next to the figures for everyone.

    7. **Rename the exploration**, to something like `Quiz Revenue`, **then star or share it** so your teammates can find it.

    !!! tip "Narrowing it further"

        - **One quiz at a time.** Set `Filters` to `Event name` contains that quiz, such as `quiz_started_skincare_quiz_usa`.
        - **One quiz page.** If the quiz has a page of its own, build the segment on `Page location` contains that path instead, such as `/pages/skin-quiz`.

    **Attribute revenue with UTM parameters**

    Tag the links into your quiz with `utm_source=quiz` or `utm_campaign=quiz_name`. Revenue then appears in the GA4 `Advertising > Attribution > Model comparison` report, and under `Engagement > Conversions > Event name > purchase`.

    ![The purchase event in the GA4 conversions report](/images/how_to_ga_revenue2.png)

    Add a `Source` column beside the default channel grouping, then look for the rows with the `revenuehunt` source.

    ![The source column showing revenuehunt](/images/how_to_ga_events.png)

    !!! tip "More from Google"

        See the Google Analytics documentation on [tracking revenue from events](https://support.google.com/analytics/answer/9216061?hl=en).

=== "Standalone"

    **Compare quiz customers with everyone else**

    ![A Free form exploration comparing quiz users with all users](/images/how_to_shopifyv2_ga4_exploration1revenue1.png)

    ![The revenue and purchase columns of that exploration](/images/how_to_shopifyv2_ga4_exploration1revenue2.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Build the quiz segment.** In the `Variables` panel, under `Segments`, click `+` and choose `User segment`. Include users where `Event name` `contains` `quiz_started`, or use `matches regex` with `^quiz_started_.*$`. Name it `Quiz Users`, then click `Save and apply`.

    3. **Add the default `All Users` segment too**, so you have something to compare against.

    4. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count`, `Purchases` and `Total revenue` under `Metrics`.

    5. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users` and `Quiz Users` |
        | `Rows` | `Event name` |
        | `Columns` | Leave empty, or set `Segment` for a side-by-side comparison |
        | `Values` | `Event count`, `Purchases`, `Total revenue` |
        | `Filters` | `Event name` contains `quiz_started` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    6. **Read the table.** It shows the revenue and purchases from customers who triggered `quiz_started`, next to the figures for everyone.

    7. **Rename the exploration**, to something like `Quiz Revenue`, **then star or share it** so your teammates can find it.

    !!! tip "Narrowing it further"

        - **One quiz at a time.** Set `Filters` to `Event name` contains that quiz, such as `quiz_started_skincare_quiz_usa`.
        - **One quiz page.** If the quiz has a page of its own, build the segment on `Page location` contains that path instead, such as `/pages/skin-quiz`.

    **Attribute revenue with UTM parameters**

    Tag the links into your quiz with `utm_source=quiz` or `utm_campaign=quiz_name`. Revenue then appears in the GA4 `Advertising > Attribution > Model comparison` report, and under `Engagement > Conversions > Event name > purchase`.

    ![The purchase event in the GA4 conversions report](/images/how_to_ga_revenue2.png)

    Add a `Source` column beside the default channel grouping, then look for the rows with the `revenuehunt` source.

    ![The source column showing revenuehunt](/images/how_to_ga_events.png)

    !!! tip "More from Google"

        See the Google Analytics documentation on [tracking revenue from events](https://support.google.com/analytics/answer/9216061?hl=en).

## Use GA4 explorations

Standard GA4 reports show the trend. An exploration answers a specific question about how customers use your quiz.

=== "Shopify"

    An exploration lets you:

    - **Compare quiz customers with everyone else.** See how much revenue comes from the customers who start a quiz.
    - **Break the results down by quiz.** If you run several, see which brings in the most purchases.
    - **Build a funnel.** Follow `quiz_started` to `results_page_viewed` to `product_added_to_cart` to `purchase`, and find where customers drop out.
    - **Follow customer paths.** See what a customer does after the quiz, such as opening a recommended product or going straight to the checkout.
    - **Build an audience.** Save the quiz customers as an audience for later analysis, or for remarketing in Google Ads.

    **Find your most clicked choices**

    ![A Free form exploration of the block_answered events](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count` under `Metrics`.

    3. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users`, or `Quiz Users` to count only the customers who took a quiz |
        | `Rows` | `Event name` |
        | `Values` | `Event count` |
        | `Filters` | `Event name` contains `block_answered` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    4. **Read the table.** Each `block_answered` row is one choice, and the event count is how often customers picked it.

    5. **Rename the exploration**, to something like `Most Clicked Choices`, **then star or share it** so your teammates can find it.

    !!! tip "More on explorations"

        See the Google Analytics documentation on [GA4 explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Shopify (Legacy)"

    An exploration lets you:

    - **Compare quiz customers with everyone else.** See how much revenue comes from the customers who start a quiz.
    - **Break the results down by quiz.** If you run several, see which brings in the most purchases.
    - **Build a funnel.** Follow `quiz_started` to `results_page_viewed` to `product_added_to_cart` to `purchase`, and find where customers drop out.
    - **Follow customer paths.** See what a customer does after the quiz, such as opening a recommended product or going straight to the checkout.
    - **Build an audience.** Save the quiz customers as an audience for later analysis, or for remarketing in Google Ads.

    **Find your most clicked choices**

    ![A Free form exploration of the block_answered events](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count` under `Metrics`.

    3. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users`, or `Quiz Users` to count only the customers who took a quiz |
        | `Rows` | `Event name` |
        | `Values` | `Event count` |
        | `Filters` | `Event name` contains `block_answered` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    4. **Read the table.** Each `block_answered` row is one choice, and the event count is how often customers picked it.

    5. **Rename the exploration**, to something like `Most Clicked Choices`, **then star or share it** so your teammates can find it.

    !!! tip "More on explorations"

        See the Google Analytics documentation on [GA4 explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "WooCommerce"

    An exploration lets you:

    - **Compare quiz customers with everyone else.** See how much revenue comes from the customers who start a quiz.
    - **Break the results down by quiz.** If you run several, see which brings in the most purchases.
    - **Build a funnel.** Follow `quiz_started` to `results_page_viewed` to `product_added_to_cart` to `purchase`, and find where customers drop out.
    - **Follow customer paths.** See what a customer does after the quiz, such as opening a recommended product or going straight to the checkout.
    - **Build an audience.** Save the quiz customers as an audience for later analysis, or for remarketing in Google Ads.

    **Find your most clicked choices**

    ![A Free form exploration of the block_answered events](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count` under `Metrics`.

    3. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users`, or `Quiz Users` to count only the customers who took a quiz |
        | `Rows` | `Event name` |
        | `Values` | `Event count` |
        | `Filters` | `Event name` contains `block_answered` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    4. **Read the table.** Each `block_answered` row is one choice, and the event count is how often customers picked it.

    5. **Rename the exploration**, to something like `Most Clicked Choices`, **then star or share it** so your teammates can find it.

    !!! tip "More on explorations"

        See the Google Analytics documentation on [GA4 explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Magento"

    An exploration lets you:

    - **Compare quiz customers with everyone else.** See how much revenue comes from the customers who start a quiz.
    - **Break the results down by quiz.** If you run several, see which brings in the most purchases.
    - **Build a funnel.** Follow `quiz_started` to `results_page_viewed` to `product_added_to_cart` to `purchase`, and find where customers drop out.
    - **Follow customer paths.** See what a customer does after the quiz, such as opening a recommended product or going straight to the checkout.
    - **Build an audience.** Save the quiz customers as an audience for later analysis, or for remarketing in Google Ads.

    **Find your most clicked choices**

    ![A Free form exploration of the block_answered events](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count` under `Metrics`.

    3. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users`, or `Quiz Users` to count only the customers who took a quiz |
        | `Rows` | `Event name` |
        | `Values` | `Event count` |
        | `Filters` | `Event name` contains `block_answered` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    4. **Read the table.** Each `block_answered` row is one choice, and the event count is how often customers picked it.

    5. **Rename the exploration**, to something like `Most Clicked Choices`, **then star or share it** so your teammates can find it.

    !!! tip "More on explorations"

        See the Google Analytics documentation on [GA4 explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "BigCommerce"

    An exploration lets you:

    - **Compare quiz customers with everyone else.** See how much revenue comes from the customers who start a quiz.
    - **Break the results down by quiz.** If you run several, see which brings in the most purchases.
    - **Build a funnel.** Follow `quiz_started` to `results_page_viewed` to `product_added_to_cart` to `purchase`, and find where customers drop out.
    - **Follow customer paths.** See what a customer does after the quiz, such as opening a recommended product or going straight to the checkout.
    - **Build an audience.** Save the quiz customers as an audience for later analysis, or for remarketing in Google Ads.

    **Find your most clicked choices**

    ![A Free form exploration of the block_answered events](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count` under `Metrics`.

    3. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users`, or `Quiz Users` to count only the customers who took a quiz |
        | `Rows` | `Event name` |
        | `Values` | `Event count` |
        | `Filters` | `Event name` contains `block_answered` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    4. **Read the table.** Each `block_answered` row is one choice, and the event count is how often customers picked it.

    5. **Rename the exploration**, to something like `Most Clicked Choices`, **then star or share it** so your teammates can find it.

    !!! tip "More on explorations"

        See the Google Analytics documentation on [GA4 explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

=== "Standalone"

    An exploration lets you:

    - **Compare quiz customers with everyone else.** See how much revenue comes from the customers who start a quiz.
    - **Break the results down by quiz.** If you run several, see which brings in the most purchases.
    - **Build a funnel.** Follow `quiz_started` to `results_page_viewed` to `product_added_to_cart` to `purchase`, and find where customers drop out.
    - **Follow customer paths.** See what a customer does after the quiz, such as opening a recommended product or going straight to the checkout.
    - **Build an audience.** Save the quiz customers as an audience for later analysis, or for remarketing in Google Ads.

    **Find your most clicked choices**

    ![A Free form exploration of the block_answered events](/images/how_to_shopifyv2_ga4_exploration2choices.png)

    1. **In GA4, go to `Explore`, click `+`, and choose `Free form`.**

    2. **Add the dimensions and metrics.** In the `Variables` panel, add `Event name` under `Dimensions`, and `Event count` under `Metrics`.

    3. **Fill in the `Tab Settings` panel.**

        | Field | Value |
        |---|---|
        | `Segments` | `All Users`, or `Quiz Users` to count only the customers who took a quiz |
        | `Rows` | `Event name` |
        | `Values` | `Event count` |
        | `Filters` | `Event name` contains `block_answered` |
        | `Visualization` | `Table`, or `Bar chart` |
        | `Date range` | `Last 28 days` |

    4. **Read the table.** Each `block_answered` row is one choice, and the event count is how often customers picked it.

    5. **Rename the exploration**, to something like `Most Clicked Choices`, **then star or share it** so your teammates can find it.

    !!! tip "More on explorations"

        See the Google Analytics documentation on [GA4 explorations](https://support.google.com/analytics/answer/7579450?hl=en#zippy=%2Cin-this-article).

---

This article explains how to connect a quiz to Google Analytics, and which events it then sends. It also covers adding events of your own, and reading the revenue back out.