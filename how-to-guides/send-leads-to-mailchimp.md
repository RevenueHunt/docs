---
description: "Learn how to connect your RevenueHunt quiz to Mailchimp and send quiz leads to your audience for segmentation and follow-up emails."
icon: simple/mailchimp
---

# How to Send Leads to Mailchimp

Connect your quiz to Mailchimp and every contact from the quiz is added to your Mailchimp audience. You can then segment those contacts and follow up by email.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=9MBKK4JCdMCrlx9y" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to connect your RevenueHunt account to Mailchimp and send each contact to your audience. It also covers tagging them by their answers, and building segments and automations from those tags.

    !!! warning "Before you begin"

        **Make sure your quiz collects email addresses.** Open your quiz in the [Quiz builder](/reference/quiz-builder/questions/) and look for an [email question](/reference/quiz-builder/questions/#email-address) block. If there is none, click `Add Question` and select `Email Address` from the question types. You can also add it to an existing question from the `Add Block` menu.

        **(optional) Ask for marketing consent.** Add a marketing consent checkbox directly below the email field. A customer can then agree to receive marketing emails, which is useful for GDPR compliance. See [how to ask for marketing consent](/how-to-guides/ask-for-marketing-consent/).

    !!! info "What data is sent to Mailchimp"

        Mailchimp receives the contact's email, first name, last name and phone number when provided. Quiz [customer tags](/reference/quiz-builder/customer-tags/) and result tags are also synced to the contact's profile in Mailchimp as contact tags.

        Full quiz answers and product recommendations are not synced to Mailchimp. To learn more about how Mailchimp handles contact data fields, see the [Mailchimp merge fields documentation](https://mailchimp.com/help/manage-audience-signup-form-fields/).

        If you need the full answers and recommended products in your email templates, use [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) instead, or check the [alternative ways to send quiz leads to Mailchimp](#alternative-ways-to-send-quiz-leads-to-mailchimp).


=== "Shopify (Legacy)"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Send your quiz leads to Mailchimp and you can segment your audience on what each customer answered. Each group then gets the email that suits it.

    !!! warning "What Mailchimp can and cannot receive"

        - **Limited data transfer**: the Mailchimp integration sends only the email, the name and the customer tags. If you need more than that, such as the recommended products, use a different service.
        - **Alternative services**: [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/) carry the full quiz data, so they personalize a follow-up email much further.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A quiz in the RevenueHunt app that you want to connect to Mailchimp.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Send your quiz leads to Mailchimp and you can segment your audience on what each customer answered. Each group then gets the email that suits it.

    !!! warning "What Mailchimp can and cannot receive"

        - **Limited data transfer**: the Mailchimp integration sends only the email, the name and the customer tags. If you need more than that, such as the recommended products, use a different service.
        - **Alternative services**: [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/) carry the full quiz data, so they personalize a follow-up email much further.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A quiz in the RevenueHunt app that you want to connect to Mailchimp.

=== "Magento"



    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Send your quiz leads to Mailchimp and you can segment your audience on what each customer answered. Each group then gets the email that suits it.

    !!! warning "What Mailchimp can and cannot receive"

        - **Limited data transfer**: the Mailchimp integration sends only the email, the name and the customer tags. If you need more than that, such as the recommended products, use a different service.
        - **Alternative services**: [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/) carry the full quiz data, so they personalize a follow-up email much further.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A quiz in the RevenueHunt app that you want to connect to Mailchimp.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Send your quiz leads to Mailchimp and you can segment your audience on what each customer answered. Each group then gets the email that suits it.

    !!! warning "What Mailchimp can and cannot receive"

        - **Limited data transfer**: the Mailchimp integration sends only the email, the name and the customer tags. If you need more than that, such as the recommended products, use a different service.
        - **Alternative services**: [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/) carry the full quiz data, so they personalize a follow-up email much further.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A quiz in the RevenueHunt app that you want to connect to Mailchimp.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Send your quiz leads to Mailchimp and you can segment your audience on what each customer answered. Each group then gets the email that suits it.

    !!! warning "What Mailchimp can and cannot receive"

        - **Limited data transfer**: the Mailchimp integration sends only the email, the name and the customer tags. If you need more than that, such as the recommended products, use a different service.
        - **Alternative services**: [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/) carry the full quiz data, so they personalize a follow-up email much further.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A quiz in the RevenueHunt app that you want to connect to Mailchimp.

## Link quiz to Mailchimp

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=5_4RnWu8rxpX-0kR&amp;start=125" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    The Mailchimp integration uses OAuth to securely connect your RevenueHunt account to Mailchimp. The connection is made once for the whole account. Every quiz in it then gains the option to send leads to Mailchimp.

    **Connect your account to Mailchimp**

    1. **Open the RevenueHunt app and open any quiz.**
    2. **Go to [`Quiz settings > Integrations`](/reference/quiz-builder/connect-integrations/).**
    3. **Scroll to `Mailing & CRMs` and find the Mailchimp card.**
    4. **Click `Connect`.**
    5. **Log in to Mailchimp and click `Allow`.** The app sends you to a Mailchimp authentication page first.
    6. **Check the Mailchimp card back in the quiz settings.** It now shows a `Connected` badge.

    **Enable Mailchimp for each quiz**

    Connecting through OAuth links your whole RevenueHunt account. It does not start sending leads on its own, so switch it on for each quiz.

    1. **Open [`Quiz settings > Integrations`](/reference/quiz-builder/connect-integrations/) on each quiz you want to send data from.**
    2. **Find the Mailchimp section and tick `Send Quiz Leads to Mailchimp`.**
    3. **Click the top `Save` button.**

    !!! tip "Stop sending data from a single quiz"

        To stop one quiz sending data to Mailchimp, uncheck its `Send Quiz Leads to Mailchimp` checkbox and save. You do not need to disconnect Mailchimp entirely. See [Disconnect Mailchimp](#disconnect-mailchimp) for the account-level option.

    **Test the connection**

    1. **`Preview` your quiz and complete it with a test name and email address.** Go all the way through to the results page.
    2. **Open `Audience` in Mailchimp and search for your test email.** It may take a moment to appear, so refresh the page if needed.
    3. **Check the new contact and its tags.** It carries one tag per answer chosen. A general tag such as `revenuehunt` is there too, if you applied one to every answer in a question.

    !!! tip

        You can use your real email with a `+test1`, `+test2` suffix to test different answering routes. For example, `youremail+test1@email.com` or `youremail+test2@email.com`.

=== "Shopify (Legacy)"

    To connect your quiz to Mailchimp:

    1. **Open your quiz and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    2. **Find the Mailchimp section and click `Connect`.** A Mailchimp login page opens in a new tab.
        ![The Mailchimp section on the Connect tab](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. **Log in to your Mailchimp account and click `Allow`.**
        ![Authorizing the app in Mailchimp](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. **Look for the confirmation message.** Mailchimp shows `Mailchimp got connected, please close this windows to go back to the dashboard.`
    5. **Close that window.** Your quiz is connected, and you can now link it to a mailing list.
        ![The connected Mailchimp integration](/images/how_to_send_leads_to_mailchimp_settings.png)

    6. **Return to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz.** You may need to refresh the page for the status to update.
    7. **Select the Mailchimp list to send your quiz results to.**

=== "WooCommerce"


    To connect your quiz to Mailchimp:

    1. **Open your quiz and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    2. **Find the Mailchimp section and click `Connect`.** A Mailchimp login page opens in a new tab.
        ![The Mailchimp section on the Connect tab](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. **Log in to your Mailchimp account and click `Allow`.**
        ![Authorizing the app in Mailchimp](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. **Look for the confirmation message.** Mailchimp shows `Mailchimp got connected, please close this windows to go back to the dashboard.`
    5. **Close that window.** Your quiz is connected, and you can now link it to a mailing list.
        ![The connected Mailchimp integration](/images/how_to_send_leads_to_mailchimp_settings.png)

    6. **Return to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz.** You may need to refresh the page for the status to update.
    7. **Select the Mailchimp list to send your quiz results to.**

=== "Magento"


    To connect your quiz to Mailchimp:

    1. **Open your quiz and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    2. **Find the Mailchimp section and click `Connect`.** A Mailchimp login page opens in a new tab.
        ![The Mailchimp section on the Connect tab](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. **Log in to your Mailchimp account and click `Allow`.**
        ![Authorizing the app in Mailchimp](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. **Look for the confirmation message.** Mailchimp shows `Mailchimp got connected, please close this windows to go back to the dashboard.`
    5. **Close that window.** Your quiz is connected, and you can now link it to a mailing list.
        ![The connected Mailchimp integration](/images/how_to_send_leads_to_mailchimp_settings.png)

    6. **Return to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz.** You may need to refresh the page for the status to update.
    7. **Select the Mailchimp list to send your quiz results to.**

=== "BigCommerce"


    To connect your quiz to Mailchimp:

    1. **Open your quiz and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    2. **Find the Mailchimp section and click `Connect`.** A Mailchimp login page opens in a new tab.
        ![The Mailchimp section on the Connect tab](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. **Log in to your Mailchimp account and click `Allow`.**
        ![Authorizing the app in Mailchimp](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. **Look for the confirmation message.** Mailchimp shows `Mailchimp got connected, please close this windows to go back to the dashboard.`
    5. **Close that window.** Your quiz is connected, and you can now link it to a mailing list.
        ![The connected Mailchimp integration](/images/how_to_send_leads_to_mailchimp_settings.png)

    6. **Return to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz.** You may need to refresh the page for the status to update.
    7. **Select the Mailchimp list to send your quiz results to.**

=== "Standalone"


    To connect your quiz to Mailchimp:

    1. **Open your quiz and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    2. **Find the Mailchimp section and click `Connect`.** A Mailchimp login page opens in a new tab.
        ![The Mailchimp section on the Connect tab](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. **Log in to your Mailchimp account and click `Allow`.**
        ![Authorizing the app in Mailchimp](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. **Look for the confirmation message.** Mailchimp shows `Mailchimp got connected, please close this windows to go back to the dashboard.`
    5. **Close that window.** Your quiz is connected, and you can now link it to a mailing list.
        ![The connected Mailchimp integration](/images/how_to_send_leads_to_mailchimp_settings.png)

    6. **Return to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz.** You may need to refresh the page for the status to update.
    7. **Select the Mailchimp list to send your quiz results to.**


## Add quiz contacts to a Mailchimp audience

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=rX05ADDlIhLWPAbb&amp;start=185" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    Once your account is connected, you choose which Mailchimp audience each customer is added to. The audience selector sits inside the email question block.

    1. **Check that your account is [connected to Mailchimp](#link-quiz-to-mailchimp) and that `Send Quiz Leads to Mailchimp` is ticked for the quiz.**
    2. **Open the [Quiz builder](/reference/quiz-builder/) and select the [email question](/reference/quiz-builder/questions/#email-address) block.** The `Email input settings` panel opens.
    3. **Open the `Mailchimp Audience` dropdown and pick the audience to add each customer to.**
    4. **Click the top `Save` button.**

    !!! tip "Per-quiz audiences"

        To feed a different audience from each quiz, set the audience on the email question block of each quiz separately.

=== "Shopify (Legacy)"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "WooCommerce"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "Magento"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "BigCommerce"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "Standalone"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link quiz to Mailchimp](#link-quiz-to-mailchimp) section.

## Use customer tags for segmentation in Mailchimp

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=K9vLKxpsVk1Ugva9&amp;start=257" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    Full quiz answers do not sync to Mailchimp, so use the [Customer tags](/reference/quiz-builder/customer-tags/) field on each answer choice instead. When a customer picks that answer, the choice's customer tag reaches Mailchimp as a contact tag. Build your segments from those tags.

    **Tag your answer choices**

    1. **Open your quiz in the [Quiz builder](/reference/quiz-builder/) and select an answer choice.** Its [Choice settings](/reference/quiz-builder/questions/#choice-settings) open.
    2. **Under `Customer tags`, create a tag that describes that choice.** For a skin type question, tag the `Oily` choice with `skin-oily` and the `Dry` choice with `skin-dry`.

        ![Customer tags in the Built for Shopify choice settings](/images/how_to_shiopifyv2_send_leads_to_mailchimp_tags.png)
    3. **Repeat for the remaining choices you want to segment on.**
    4. **Tag every answer in at least one question with a general tag**, such as `revenuehunt` or `quiz`. Everyone who finishes the quiz then carries it, which makes a segment of all quiz finishers easy to build.
    5. **Click the top `Save` button.**

    **Build a segment in Mailchimp**

    Once contacts start arriving with tags, you can build segments in Mailchimp based on those tags.

    1. **In Mailchimp, go to `Audience > Segments` and click `Create Segment`.**
    2. **Set the condition to `Contact Tag` and select the tag you want to target.**
    3. **Save the segment.**

    Build one segment from the general `revenuehunt` tag to reach everyone, and more segments for particular answer combinations.

=== "Shopify (Legacy)"

    With [customer tags](/reference/quiz-builder/customer-tags/), you can segment your audience within Mailchimp based on their quiz responses:

    1. **Check that the quiz is connected to Mailchimp.**
    2. **Create [customer tags](/reference/quiz-builder/customer-tags/) in the RevenueHunt app and link them to your answer choices.**

        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. **Click `Publish`** to send the changes to the preview and the live quiz.
    4. **Open the `Audience` section in your Mailchimp account.**
    5. **Build segments or groups from the customer tags**, so each campaign matches the quiz outcome.

=== "WooCommerce"


    With [customer tags](/reference/quiz-builder/customer-tags/), you can segment your audience within Mailchimp based on their quiz responses:

    1. **Check that the quiz is connected to Mailchimp.**
    2. **Create [customer tags](/reference/quiz-builder/customer-tags/) in the RevenueHunt app and link them to your answer choices.**

        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. **Click `Publish`** to send the changes to the preview and the live quiz.
    4. **Open the `Audience` section in your Mailchimp account.**
    5. **Build segments or groups from the customer tags**, so each campaign matches the quiz outcome.

=== "Magento"


    With [customer tags](/reference/quiz-builder/customer-tags/), you can segment your audience within Mailchimp based on their quiz responses:

    1. **Check that the quiz is connected to Mailchimp.**
    2. **Create [customer tags](/reference/quiz-builder/customer-tags/) in the RevenueHunt app and link them to your answer choices.**

        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. **Click `Publish`** to send the changes to the preview and the live quiz.
    4. **Open the `Audience` section in your Mailchimp account.**
    5. **Build segments or groups from the customer tags**, so each campaign matches the quiz outcome.

=== "BigCommerce"


    With [customer tags](/reference/quiz-builder/customer-tags/), you can segment your audience within Mailchimp based on their quiz responses:

    1. **Check that the quiz is connected to Mailchimp.**
    2. **Create [customer tags](/reference/quiz-builder/customer-tags/) in the RevenueHunt app and link them to your answer choices.**

        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. **Click `Publish`** to send the changes to the preview and the live quiz.
    4. **Open the `Audience` section in your Mailchimp account.**
    5. **Build segments or groups from the customer tags**, so each campaign matches the quiz outcome.

=== "Standalone"


    With [customer tags](/reference/quiz-builder/customer-tags/), you can segment your audience within Mailchimp based on their quiz responses:

    1. **Check that the quiz is connected to Mailchimp.**
    2. **Create [customer tags](/reference/quiz-builder/customer-tags/) in the RevenueHunt app and link them to your answer choices.**

        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. **Click `Publish`** to send the changes to the preview and the live quiz.
    4. **Open the `Audience` section in your Mailchimp account.**
    5. **Build segments or groups from the customer tags**, so each campaign matches the quiz outcome.


### Carry the answers across as tags

=== "Shopify"

    Mailchimp cannot receive the full quiz data, so use `customer tags` to carry the answers instead.

    1. **Create a [customer tag](/reference/quiz-builder/customer-tags/) for each possible answer.** Plan the tags first, so each one names its answer clearly.

        ![Customer tags in the Built for Shopify choice settings](/images/how_to_shiopifyv2_send_leads_to_mailchimp_tags.png)
    2. **Take a test quiz and open the contact in Mailchimp.** It carries every tag the chosen answers held, and together those tags spell out the answers.


=== "Shopify (Legacy)"

    Mailchimp cannot receive the full quiz data, so use `customer tags` to carry the answers instead.

    1. **Create a [customer tag](/reference/quiz-builder/customer-tags/) for each possible answer.** Plan the tags first, so each one names its answer clearly.
        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. **Take a test quiz and open the contact in Mailchimp.** It carries every tag the chosen answers held, and together those tags spell out the answers.

=== "WooCommerce"

    Mailchimp cannot receive the full quiz data, so use `customer tags` to carry the answers instead.

    1. **Create a [customer tag](/reference/quiz-builder/customer-tags/) for each possible answer.** Plan the tags first, so each one names its answer clearly.
        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. **Take a test quiz and open the contact in Mailchimp.** It carries every tag the chosen answers held, and together those tags spell out the answers.

=== "Magento"

    Mailchimp cannot receive the full quiz data, so use `customer tags` to carry the answers instead.

    1. **Create a [customer tag](/reference/quiz-builder/customer-tags/) for each possible answer.** Plan the tags first, so each one names its answer clearly.
        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. **Take a test quiz and open the contact in Mailchimp.** It carries every tag the chosen answers held, and together those tags spell out the answers.

=== "BigCommerce"

    Mailchimp cannot receive the full quiz data, so use `customer tags` to carry the answers instead.

    1. **Create a [customer tag](/reference/quiz-builder/customer-tags/) for each possible answer.** Plan the tags first, so each one names its answer clearly.
        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. **Take a test quiz and open the contact in Mailchimp.** It carries every tag the chosen answers held, and together those tags spell out the answers.

=== "Standalone"

    Mailchimp cannot receive the full quiz data, so use `customer tags` to carry the answers instead.

    1. **Create a [customer tag](/reference/quiz-builder/customer-tags/) for each possible answer.** Plan the tags first, so each one names its answer clearly.
        ![Customer tags on an answer choice](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. **Take a test quiz and open the contact in Mailchimp.** It carries every tag the chosen answers held, and together those tags spell out the answers.

## Set up a post-quiz email flow with Mailchimp

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=Rb0FoVucJgbOscRf&amp;start=294" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    To send a follow-up email after the quiz, build a Mailchimp automation that triggers on the tags the quiz sends.

    1. **Connect and tag.** Make sure your quiz is [connected to Mailchimp](#link-quiz-to-mailchimp) and that your answer choices are [tagged with customer tags](#use-customer-tags-for-segmentation-in-mailchimp).
    2. **Create the automation.** In Mailchimp, go to `Automations` and create a new flow.
    3. **Set the trigger.** Set the flow to trigger when a contact receives one of the tags applied through the quiz.
    4. **Add an email step.** Add an email step and design your message.
    5. **Personalize with tags.** Full quiz answers and product recommendations do not sync to Mailchimp. Personalize on the tags on each contact's profile instead. Mailchimp's dynamic content visibility settings show different text for different tags.
    6. **Publish.** Continue building your automation, then publish it once it is ready.

    !!! example

        Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as "Oily Skin," "Dry Skin," etc.

        In Mailchimp, you create an email series targeting these tags. For instance:

        - Day 1: Introduction to products suitable for oily skin.
        - Day 3: Customer testimonials and reviews for oily skin products.
        - Day 7: Special discount on recommended products for oily skin.

    !!! tip

        Preview the quiz and leave a sample email address, to send the first data to Mailchimp and test the flow. Add a `+test1` or `+test2` suffix to your own address to test different routes through the quiz, for example `youremail+test1@email.com`.

=== "Shopify (Legacy)"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To set up a post-quiz email flow with Mailchimp:

    1. **Connect your quiz to Mailchimp.** Follow [Link quiz to Mailchimp](#link-quiz-to-mailchimp).

        !!! tip

            Take a test quiz and leave a sample email address, to send the first data to Mailchimp and test the connection. Add a `+test1` or `+test2` suffix to your own address to test different routes through the quiz, for example `youremail+test1@email.com`.
    2. **Use customer tags for segmentation.** Decide what the quiz should send to Mailchimp. For example:

        - [Create customer tags in your quiz](/reference/quiz-builder/customer-tags/) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - When a customer finishes the quiz, Mailchimp receives every tag their choices carried.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            The Mailchimp API accepts only the email, the name and the customer tags from the quiz. Mailchimp cannot receive the full quiz data, so use customer tags to carry the answers instead.
    3. **Design email campaigns.** Once every answer carries a customer tag, that data starts arriving in Mailchimp. You can then build your campaigns.

        - Set up an Automation, which is an automated email flow, to trigger on a specific tag or on quiz completion.
        - Then build one Mailchimp email template per quiz outcome or flow.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as "Oily Skin," "Dry Skin," etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin.
            - Day 3: Customer testimonials and reviews for oily skin products.
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and improve.** Send yourself a test email, then adjust the campaigns based on what you see.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To set up a post-quiz email flow with Mailchimp:

    1. **Connect your quiz to Mailchimp.** Follow [Link quiz to Mailchimp](#link-quiz-to-mailchimp).

        !!! tip

            Take a test quiz and leave a sample email address, to send the first data to Mailchimp and test the connection. Add a `+test1` or `+test2` suffix to your own address to test different routes through the quiz, for example `youremail+test1@email.com`.
    2. **Use customer tags for segmentation.** Decide what the quiz should send to Mailchimp. For example:

        - [Create customer tags in your quiz](/reference/quiz-builder/customer-tags/) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - When a customer finishes the quiz, Mailchimp receives every tag their choices carried.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            The Mailchimp API accepts only the email, the name and the customer tags from the quiz. Mailchimp cannot receive the full quiz data, so use customer tags to carry the answers instead.
    3. **Design email campaigns.** Once every answer carries a customer tag, that data starts arriving in Mailchimp. You can then build your campaigns.

        - Set up an Automation, which is an automated email flow, to trigger on a specific tag or on quiz completion.
        - Then build one Mailchimp email template per quiz outcome or flow.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as "Oily Skin," "Dry Skin," etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin.
            - Day 3: Customer testimonials and reviews for oily skin products.
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and improve.** Send yourself a test email, then adjust the campaigns based on what you see.


=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To set up a post-quiz email flow with Mailchimp:

    1. **Connect your quiz to Mailchimp.** Follow [Link quiz to Mailchimp](#link-quiz-to-mailchimp).

        !!! tip

            Take a test quiz and leave a sample email address, to send the first data to Mailchimp and test the connection. Add a `+test1` or `+test2` suffix to your own address to test different routes through the quiz, for example `youremail+test1@email.com`.
    2. **Use customer tags for segmentation.** Decide what the quiz should send to Mailchimp. For example:

        - [Create customer tags in your quiz](/reference/quiz-builder/customer-tags/) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - When a customer finishes the quiz, Mailchimp receives every tag their choices carried.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            The Mailchimp API accepts only the email, the name and the customer tags from the quiz. Mailchimp cannot receive the full quiz data, so use customer tags to carry the answers instead.
    3. **Design email campaigns.** Once every answer carries a customer tag, that data starts arriving in Mailchimp. You can then build your campaigns.

        - Set up an Automation, which is an automated email flow, to trigger on a specific tag or on quiz completion.
        - Then build one Mailchimp email template per quiz outcome or flow.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as "Oily Skin," "Dry Skin," etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin.
            - Day 3: Customer testimonials and reviews for oily skin products.
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and improve.** Send yourself a test email, then adjust the campaigns based on what you see.


=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To set up a post-quiz email flow with Mailchimp:

    1. **Connect your quiz to Mailchimp.** Follow [Link quiz to Mailchimp](#link-quiz-to-mailchimp).

        !!! tip

            Take a test quiz and leave a sample email address, to send the first data to Mailchimp and test the connection. Add a `+test1` or `+test2` suffix to your own address to test different routes through the quiz, for example `youremail+test1@email.com`.
    2. **Use customer tags for segmentation.** Decide what the quiz should send to Mailchimp. For example:

        - [Create customer tags in your quiz](/reference/quiz-builder/customer-tags/) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - When a customer finishes the quiz, Mailchimp receives every tag their choices carried.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            The Mailchimp API accepts only the email, the name and the customer tags from the quiz. Mailchimp cannot receive the full quiz data, so use customer tags to carry the answers instead.
    3. **Design email campaigns.** Once every answer carries a customer tag, that data starts arriving in Mailchimp. You can then build your campaigns.

        - Set up an Automation, which is an automated email flow, to trigger on a specific tag or on quiz completion.
        - Then build one Mailchimp email template per quiz outcome or flow.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as "Oily Skin," "Dry Skin," etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin.
            - Day 3: Customer testimonials and reviews for oily skin products.
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and improve.** Send yourself a test email, then adjust the campaigns based on what you see.


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To set up a post-quiz email flow with Mailchimp:

    1. **Connect your quiz to Mailchimp.** Follow [Link quiz to Mailchimp](#link-quiz-to-mailchimp).

        !!! tip

            Take a test quiz and leave a sample email address, to send the first data to Mailchimp and test the connection. Add a `+test1` or `+test2` suffix to your own address to test different routes through the quiz, for example `youremail+test1@email.com`.
    2. **Use customer tags for segmentation.** Decide what the quiz should send to Mailchimp. For example:

        - [Create customer tags in your quiz](/reference/quiz-builder/customer-tags/) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - When a customer finishes the quiz, Mailchimp receives every tag their choices carried.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            The Mailchimp API accepts only the email, the name and the customer tags from the quiz. Mailchimp cannot receive the full quiz data, so use customer tags to carry the answers instead.
    3. **Design email campaigns.** Once every answer carries a customer tag, that data starts arriving in Mailchimp. You can then build your campaigns.

        - Set up an Automation, which is an automated email flow, to trigger on a specific tag or on quiz completion.
        - Then build one Mailchimp email template per quiz outcome or flow.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as "Oily Skin," "Dry Skin," etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin.
            - Day 3: Customer testimonials and reviews for oily skin products.
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and improve.** Send yourself a test email, then adjust the campaigns based on what you see.


## Disconnect Mailchimp

=== "Shopify"

    **Stop sending data from one quiz**

    Uncheck the `Send Quiz Leads to Mailchimp` checkbox in that specific quiz's [`Quiz settings > Integrations`](/reference/quiz-builder/connect-integrations/) tab and click `Save`. Other quizzes in the account keep sending data to Mailchimp.

    **Disconnect Mailchimp from your account**

    1. **Go to [`Quiz settings > Integrations`](/reference/quiz-builder/connect-integrations/).**
    2. **Scroll to the Mailchimp card and click `Disconnect`.**
    3. **Confirm the action.**

    No more quiz data will flow to Mailchimp from any quiz in the account.

=== "Shopify (Legacy)"

    Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and click `Disconnect`. Then click the `Publish` button to update the preview and the live quiz.

=== "WooCommerce"

    Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and click `Disconnect`. Then click the `Publish` button to update the preview and the live quiz.

=== "Magento"

    Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and click `Disconnect`. Then click the `Publish` button to update the preview and the live quiz.

=== "BigCommerce"

    Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and click `Disconnect`. Then click the `Publish` button to update the preview and the live quiz.

=== "Standalone"

    Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and click `Disconnect`. Then click the `Publish` button to update the preview and the live quiz.

## Alternative ways to send quiz leads to Mailchimp

=== "Shopify"

    The built-in integration does not send the full quiz answers or the recommended products. To pass those to Mailchimp, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Mailchimp.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Mailchimp.

=== "Shopify (Legacy)"

    To control exactly which data reaches Mailchimp, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Mailchimp.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Mailchimp.

=== "WooCommerce"

    To control exactly which data reaches Mailchimp, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Mailchimp.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Mailchimp.


=== "Magento"


    To control exactly which data reaches Mailchimp, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Mailchimp.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Mailchimp.

=== "BigCommerce"


    To control exactly which data reaches Mailchimp, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Mailchimp.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Mailchimp.

=== "Standalone"


    To control exactly which data reaches Mailchimp, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Mailchimp.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Mailchimp.

---
This article explains how to send quiz leads to Mailchimp, and how to segment them on the answers with customer tags.
