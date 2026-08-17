---
description: "Learn how to connect your RevenueHunt quiz to Mailchimp and send quiz leads to your audience for segmentation and follow-up emails."
icon: simple/mailchimp
---

# How to Send Leads to Mailchimp

Apart from giving your customers personalized product recommendations, you can connect your quiz to Mailchimp. This way all the contacts coming from the quiz are added to your Mailchimp audience, where you can segment them and follow up with targeted campaigns.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=9MBKK4JCdMCrlx9y" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to connect your RevenueHunt account to Mailchimp, send quiz taker contacts to your audience, tag them based on their answers and build segments and automations around those tags.

    !!! warning "Before you begin"

        **Make sure your quiz collects email addresses.** Open your quiz in the [Quiz builder](/reference/quiz-builder/questions/) and check for an [email question](/reference/quiz-builder/questions/#email) block. If there isn't one, click `Add Question` and select `Email Address` from the question types. You can also add it to an existing slide from the `Add Block` menu.

        **(optional) Ask for marketing consent.** Add a marketing consent checkbox directly below the email field. This lets quiz takers agree to receive marketing emails, which is useful for GDPR compliance. See [How to Ask for Marketing Consent](/how-to-guides/ask-for-marketing-consent/).

    !!! info "What data is sent to Mailchimp"

        Mailchimp receives the contact's **email**, **first name**, **last name** and **phone number** when provided. Quiz [customer tags](/reference/quiz-builder/link-collections/#customer-tags) and result tags are also synced to the contact's profile in Mailchimp as contact tags.

        Full quiz answers and product recommendations are **not** synced to Mailchimp directly. To learn more about how Mailchimp handles contact data fields, see the [Mailchimp merge fields documentation](https://mailchimp.com/help/manage-audience-signup-form-fields/).

        If you need the full answers and recommended products in your email templates, use [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) instead, or check the [alternative ways to send quiz leads to Mailchimp](#alternative-ways-to-send-quiz-leads-to-mailchimp).


=== "Shopify (Legacy)"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Automating the transfer of quiz leads to your Mailchimp account can help you improve your email marketing campaigns by segmenting your audience and sending them personalized follow-up emails. 

    !!! warning "Important Considerations"

        - **Limited Data Transfer**: Mailchimp integration only supports email, name, and customer tags to be send from the quiz. For more complex emailing/data needs, including direct product recommendations, consider using a different service.
        - **Alternative Services**: For functionality beyond basic data transfer, platforms like [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) are recommended. These services offer more robust integration options for personalized follow-ups.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A RevenueHunt Product Recommendation Quiz that you wish to connect with Mailchimp.
    
=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Automating the transfer of quiz leads to your Mailchimp account can help you improve your email marketing campaigns by segmenting your audience and sending them personalized follow-up emails. 

    !!! warning "Important Considerations"

        - **Limited Data Transfer**: Mailchimp integration only supports email, name, and customer tags to be send from the quiz. For more complex emailing/data needs, including direct product recommendations, consider using a different service.
        - **Alternative Services**: For functionality beyond basic data transfer, platforms like [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) are recommended. These services offer more robust integration options for personalized follow-ups.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A RevenueHunt Product Recommendation Quiz that you wish to connect with Mailchimp.

=== "Magento"



    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Automating the transfer of quiz leads to your Mailchimp account can help you improve your email marketing campaigns by segmenting your audience and sending them personalized follow-up emails. 

    !!! warning "Important Considerations"

        - **Limited Data Transfer**: Mailchimp integration only supports email, name, and customer tags to be send from the quiz. For more complex emailing/data needs, including direct product recommendations, consider using a different service.
        - **Alternative Services**: For functionality beyond basic data transfer, platforms like [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) are recommended. These services offer more robust integration options for personalized follow-ups.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A RevenueHunt Product Recommendation Quiz that you wish to connect with Mailchimp.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Automating the transfer of quiz leads to your Mailchimp account can help you improve your email marketing campaigns by segmenting your audience and sending them personalized follow-up emails. 

    !!! warning "Important Considerations"

        - **Limited Data Transfer**: Mailchimp integration only supports email, name, and customer tags to be send from the quiz. For more complex emailing/data needs, including direct product recommendations, consider using a different service.
        - **Alternative Services**: For functionality beyond basic data transfer, platforms like [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) are recommended. These services offer more robust integration options for personalized follow-ups.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A RevenueHunt Product Recommendation Quiz that you wish to connect with Mailchimp.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to send leads to Mailchimp from your quiz.

    Automating the transfer of quiz leads to your Mailchimp account can help you improve your email marketing campaigns by segmenting your audience and sending them personalized follow-up emails. 

    !!! warning "Important Considerations"

        - **Limited Data Transfer**: Mailchimp integration only supports email, name, and customer tags to be send from the quiz. For more complex emailing/data needs, including direct product recommendations, consider using a different service.
        - **Alternative Services**: For functionality beyond basic data transfer, platforms like [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) or [Omnisend](/how-to-guides/send-leads-to-omnisend/) are recommended. These services offer more robust integration options for personalized follow-ups.

    Before you begin, ensure you have:

    - An active Mailchimp account.
    - A RevenueHunt Product Recommendation Quiz that you wish to connect with Mailchimp.

## Link Quiz to Mailchimp

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=5_4RnWu8rxpX-0kR&amp;start=125" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    The Mailchimp integration uses OAuth to securely connect your RevenueHunt account to Mailchimp. This connection is made at the **account level**, meaning once connected, all quizzes in that account gain the option to send leads to Mailchimp.

    **Connect your account to Mailchimp**

    1. Open the RevenueHunt app and navigate to any quiz.
    2. Go to the [`Quiz Settings > Integrations`](/reference/quiz-builder/connect-integrations/) tab.
    3. Scroll down to the `Mailing & CRMs` section and find the Mailchimp card.
    4. Click the `Connect` button.
    5. You will be redirected to a Mailchimp authentication page. Log in to your Mailchimp account and click `Allow` to grant access.
    6. Once authenticated, you will be redirected back to the quiz settings, where Mailchimp will now show a `Connected` badge.

    **Enable Mailchimp for each quiz**

    Connecting via OAuth links your entire RevenueHunt account, but it does **not** automatically start sending leads from every quiz. You need to enable it individually per quiz.

    1. For each quiz you want to send data from, open that quiz's [`Quiz Settings > Integrations`](/reference/quiz-builder/connect-integrations/) tab.
    2. Find the Mailchimp section and check the `Send Quiz Leads to Mailchimp` checkbox.
    3. Click the top `Save` button to save your changes.

    !!! tip "Stop sending data from a single quiz"

        If you want to stop data from a specific quiz flowing to Mailchimp, simply uncheck the `Send Quiz Leads to Mailchimp` checkbox in that quiz and save. You do not need to disconnect Mailchimp entirely. See [Disconnect Mailchimp](#disconnect-mailchimp) for the account-level option.

    **Test the connection**

    1. `Preview` your quiz and complete it with a test name and email address, all the way through to the results page.
    2. Go to Mailchimp and open `Audience`, then search for your test email. It may take a moment to appear, so refresh the page if needed.
    3. You should see the new contact with any tags that were applied based on the answer choices they selected. If you tagged all answers in one question with a general tag like `revenuehunt` or `quiz`, you should see that tag on the profile as well.

    !!! tip

        You can use your real email with a `+test1`, `+test2` suffix to test different answering routes. For example, `youremail+test1@email.com` or `youremail+test2@email.com`.

=== "Shopify (Legacy)"

    Connecting your quiz to Mailchimp allows for the seamless transfer of leads:

    1. Locate your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the interface.
    2. Find the Mailchimp section and click on the `Connect` button. This action will redirect you to a Mailchimp login page in a new tab.
        ![how to send leads to mailchimp authorize1](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. Log into your Mailchimp account and authorize the app by clicking on `Allow`.
        ![how to send leads to mailchimp authorize2](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. If the connection was successful, you'll see a `Mailchimp got connected, please close this windows to go back to the dashboard.` message.
    4. After authorization, your quiz is connected to Mailchimp, and you can proceed to link it to a specific mailing list.
        ![how to send leads to mailchimp settings](/images/how_to_send_leads_to_mailchimp_settings.png)

    5. Return to the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz platform. You may need to refresh the page to update the connection status.
    6. Follow the prompts to select the Mailchimp list you wish to send your quiz results to from the dropdown.

=== "WooCommerce"


    Connecting your quiz to Mailchimp allows for the seamless transfer of leads:

    1. Locate your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the interface.
    2. Find the Mailchimp section and click on the `Connect` button. This action will redirect you to a Mailchimp login page in a new tab.
        ![how to send leads to mailchimp authorize1](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. Log into your Mailchimp account and authorize the app by clicking on `Allow`.
        ![how to send leads to mailchimp authorize2](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. If the connection was successful, you'll see a `Mailchimp got connected, please close this windows to go back to the dashboard.` message.
    4. After authorization, your quiz is connected to Mailchimp, and you can proceed to link it to a specific mailing list.
        ![how to send leads to mailchimp settings](/images/how_to_send_leads_to_mailchimp_settings.png)

    5. Return to the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz platform. You may need to refresh the page to update the connection status.
    6. Follow the prompts to select the Mailchimp list you wish to send your quiz results to from the dropdown.

=== "Magento"


    Connecting your quiz to Mailchimp allows for the seamless transfer of leads:

    1. Locate your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the interface.
    2. Find the Mailchimp section and click on the `Connect` button. This action will redirect you to a Mailchimp login page in a new tab.
        ![how to send leads to mailchimp authorize1](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. Log into your Mailchimp account and authorize the app by clicking on `Allow`.
        ![how to send leads to mailchimp authorize2](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. If the connection was successful, you'll see a `Mailchimp got connected, please close this windows to go back to the dashboard.` message.
    4. After authorization, your quiz is connected to Mailchimp, and you can proceed to link it to a specific mailing list.
        ![how to send leads to mailchimp settings](/images/how_to_send_leads_to_mailchimp_settings.png)

    5. Return to the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz platform. You may need to refresh the page to update the connection status.
    6. Follow the prompts to select the Mailchimp list you wish to send your quiz results to from the dropdown.

=== "BigCommerce"


    Connecting your quiz to Mailchimp allows for the seamless transfer of leads:

    1. Locate your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the interface.
    2. Find the Mailchimp section and click on the `Connect` button. This action will redirect you to a Mailchimp login page in a new tab.
        ![how to send leads to mailchimp authorize1](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. Log into your Mailchimp account and authorize the app by clicking on `Allow`.
        ![how to send leads to mailchimp authorize2](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. If the connection was successful, you'll see a `Mailchimp got connected, please close this windows to go back to the dashboard.` message.
    4. After authorization, your quiz is connected to Mailchimp, and you can proceed to link it to a specific mailing list.
        ![how to send leads to mailchimp settings](/images/how_to_send_leads_to_mailchimp_settings.png)

    5. Return to the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz platform. You may need to refresh the page to update the connection status.
    6. Follow the prompts to select the Mailchimp list you wish to send your quiz results to from the dropdown.

=== "Standalone"


    Connecting your quiz to Mailchimp allows for the seamless transfer of leads:

    1. Locate your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the interface.
    2. Find the Mailchimp section and click on the `Connect` button. This action will redirect you to a Mailchimp login page in a new tab.
        ![how to send leads to mailchimp authorize1](/images/how_to_send_leads_to_mailchimp_authorize1.png)

    3. Log into your Mailchimp account and authorize the app by clicking on `Allow`.
        ![how to send leads to mailchimp authorize2](/images/how_to_send_leads_to_mailchimp_authorize2.png)

    4. If the connection was successful, you'll see a `Mailchimp got connected, please close this windows to go back to the dashboard.` message.
    4. After authorization, your quiz is connected to Mailchimp, and you can proceed to link it to a specific mailing list.
        ![how to send leads to mailchimp settings](/images/how_to_send_leads_to_mailchimp_settings.png)

    5. Return to the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz platform. You may need to refresh the page to update the connection status.
    6. Follow the prompts to select the Mailchimp list you wish to send your quiz results to from the dropdown.


## Add Quiz Contacts to a Mailchimp Audience

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=rX05ADDlIhLWPAbb&amp;start=185" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    Once your account is connected, you can choose which Mailchimp **audience** quiz takers are added to. The audience selector lives inside the email question block.

    1. Make sure your account is [connected to Mailchimp](#link-quiz-to-mailchimp) and that the `Send Quiz Leads to Mailchimp` checkbox is enabled for the quiz.
    2. In the RevenueHunt app, open the [Quiz builder](/reference/quiz-builder/) and click on the [email question](/reference/quiz-builder/questions/#email) block to open its settings.
    3. Under the `Mailchimp Audience` dropdown, select the audience you want quiz takers added to.
    4. Click the top `Save` button to save your changes.

    !!! tip "Per-quiz audiences"

        If you have multiple quizzes and want each to feed a different audience, open the email question block of each quiz individually and select the appropriate audience there.

=== "Shopify (Legacy)"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "WooCommerce"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "Magento"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "BigCommerce"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

=== "Standalone"

    The Mailchimp list is selected in the [Connect](/reference/quiz-builder/connect-integrations/) tab, as described in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

## Use Customer Tags for Segmentation in Mailchimp

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=K9vLKxpsVk1Ugva9&amp;start=257" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    Because full quiz answers don't sync to Mailchimp, we recommend using the [Customer tags](/reference/quiz-builder/customer-tags/) field on each quiz answer choice. When a quiz taker selects an answer, that choice's customer tag is sent to Mailchimp as a contact tag, which you can then use to build your own segmentation rules.

    **Tag your answer choices**

    1. Open your quiz in the [Quiz builder](/reference/quiz-builder/) and click on an answer choice to open its [Choice settings](/reference/quiz-builder/questions/#choice-settings).
    2. Under `Customer tags`, create a tag that describes that choice. For example, if a question asks about skin type, tag the `Oily` choice with `skin-oily` and the `Dry` choice with `skin-dry`.

        ![how to send leads to mailchimp customer tags built for shopify](/images/how_to_shiopifyv2_send_leads_to_mailchimp_tags.png)
    3. Repeat for the remaining choices you want to segment on.
    4. Tag **every** answer in at least one question with a general tag like `revenuehunt` or `quiz`. This creates a universal tag for every person who completed the quiz, making it easy to build a Mailchimp segment for all quiz takers.
    5. Click the top `Save` button to save your changes.

    **Build a segment in Mailchimp**

    Once contacts start arriving with tags, you can build segments in Mailchimp based on those tags.

    1. In Mailchimp, go to `Audience`, then `Segments`, and click `Create Segment`.
    2. Set the condition to `Contact Tag` and select the tag you want to target.
    3. Save the segment.

    You can create one segment for all quiz takers using your general `revenuehunt` tag, and additional segments for specific answer combinations.

=== "Shopify (Legacy)"

    With [customer tags](/reference/quiz-builder/link-collections/#customer-tags), you can segment your audience within Mailchimp based on their quiz responses:

    1. Make sure the quiz is connected to Mailchimp. 
    2. Create [customer tags](/reference/quiz-builder/link-collections/#customer-tags) in the RevenueHunt app and link them to choices.

        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. Once done, click the `Publish` button to update the preview/live quiz with new changes.
    4. Navigate to the `Audience` section in your Mailchimp account.
    5. Use the customer tags to create segmented lists or groups, allowing for targeted campaign efforts based on the quiz outcomes.

=== "WooCommerce"


    With [customer tags](/reference/quiz-builder/link-collections/#customer-tags), you can segment your audience within Mailchimp based on their quiz responses:

    1. Make sure the quiz is connected to Mailchimp. 
    2. Create [customer tags](/reference/quiz-builder/link-collections/#customer-tags) in the RevenueHunt app and link them to choices.

        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. Once done, click the `Publish` button to update the preview/live quiz with new changes.
    4. Navigate to the `Audience` section in your Mailchimp account.
    5. Use the customer tags to create segmented lists or groups, allowing for targeted campaign efforts based on the quiz outcomes.

=== "Magento"


    With [customer tags](/reference/quiz-builder/link-collections/#customer-tags), you can segment your audience within Mailchimp based on their quiz responses:

    1. Make sure the quiz is connected to Mailchimp. 
    2. Create [customer tags](/reference/quiz-builder/link-collections/#customer-tags) in the RevenueHunt app and link them to choices.

        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. Once done, click the `Publish` button to update the preview/live quiz with new changes.
    4. Navigate to the `Audience` section in your Mailchimp account.
    5. Use the customer tags to create segmented lists or groups, allowing for targeted campaign efforts based on the quiz outcomes.

=== "BigCommerce"


    With [customer tags](/reference/quiz-builder/link-collections/#customer-tags), you can segment your audience within Mailchimp based on their quiz responses:

    1. Make sure the quiz is connected to Mailchimp. 
    2. Create [customer tags](/reference/quiz-builder/link-collections/#customer-tags) in the RevenueHunt app and link them to choices.

        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. Once done, click the `Publish` button to update the preview/live quiz with new changes.
    4. Navigate to the `Audience` section in your Mailchimp account.
    5. Use the customer tags to create segmented lists or groups, allowing for targeted campaign efforts based on the quiz outcomes.

=== "Standalone"


    With [customer tags](/reference/quiz-builder/link-collections/#customer-tags), you can segment your audience within Mailchimp based on their quiz responses:

    1. Make sure the quiz is connected to Mailchimp. 
    2. Create [customer tags](/reference/quiz-builder/link-collections/#customer-tags) in the RevenueHunt app and link them to choices.

        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)
    3. Once done, click the `Publish` button to update the preview/live quiz with new changes.
    4. Navigate to the `Audience` section in your Mailchimp account.
    5. Use the customer tags to create segmented lists or groups, allowing for targeted campaign efforts based on the quiz outcomes.


### Hack: Send Quiz Answers to Mailchimp

=== "Shopify"

    To override Mailchimp's limitation on pushing detailed custom quiz data, you can use `customer tags` to represent customer responses.

    1. For each possible quiz answer, create a corresponding [customer tag](/reference/quiz-builder/link-collections/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.

        ![how to send leads to mailchimp customer tags built for shopify](/images/how_to_shiopifyv2_send_leads_to_mailchimp_tags.png)
    2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.


=== "Shopify (Legacy)"

    To override Mailchimp's limitation on pushing detailed quiz data, you can use `customer tags` to represent customer responses.

    1. For each possible quiz answer, create a corresponding [customer tag](/reference/quiz-builder/link-collections/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.
        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.

=== "WooCommerce"

    To override Mailchimp's limitation on pushing detailed quiz data, you can use `customer tags` to represent customer responses.

    1. For each possible quiz answer, create a corresponding [customer tag](/reference/quiz-builder/link-collections/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.
        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.

=== "Magento"

    To override Mailchimp's limitation on pushing detailed quiz data, you can use `customer tags` to represent customer responses.

    1. For each possible quiz answer, create a corresponding [customer tag](/reference/quiz-builder/link-collections/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.
        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.

=== "BigCommerce"

    To override Mailchimp's limitation on pushing detailed quiz data, you can use `customer tags` to represent customer responses.

    1. For each possible quiz answer, create a corresponding [customer tag](/reference/quiz-builder/link-collections/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.
        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.

=== "Standalone"

    To override Mailchimp's limitation on pushing detailed quiz data, you can use `customer tags` to represent customer responses.

    1. For each possible quiz answer, create a corresponding [customer tag](/reference/quiz-builder/link-collections/#customer-tags) within your quiz setup. This requires planning to ensure each tag accurately represents the quiz responses.
        ![how to send leads to mailchimp tags](/images/how_to_send_leads_to_mailchimp_tags.png)

    2. Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.

## Set up Post-Quiz Email Flow with Mailchimp

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WBFtvGuhDoQ?si=Rb0FoVucJgbOscRf&amp;start=294" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    To send follow-up emails to quiz takers, build an automation in Mailchimp that is triggered by the tags coming from the quiz.

    1. **Connect and tag.** Make sure your quiz is [connected to Mailchimp](#link-quiz-to-mailchimp) and that your answer choices are [tagged with customer tags](#use-customer-tags-for-segmentation-in-mailchimp).
    2. **Create the automation.** In Mailchimp, go to `Automations` and create a new flow.
    3. **Set the trigger.** Set the flow to trigger when a contact receives one of the tags applied through the quiz.
    4. **Add an email step.** Add an email step and design your message.
    5. **Personalize with tags.** Because full quiz answers and product recommendations do not sync to Mailchimp, email personalization is based on the tags added to each contact's profile. Use Mailchimp's dynamic content visibility settings to display different text depending on the tags assigned to each contact.
    6. **Publish.** Continue building your automation, then publish it once it is ready.

    !!! example

        Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as “Oily Skin,” “Dry Skin,” etc.

        In Mailchimp, you create an email series targeting these tags. For instance:

        - Day 1: Introduction to products suitable for oily skin. 
        - Day 3: Customer testimonials and reviews for oily skin products. 
        - Day 7: Special discount on recommended products for oily skin.

    !!! tip

        Remember to preview the quiz leaving a sample email address in order to send the first data to Mailchimp and test the flow. You can use your real email with a `+test1`, `+test2` suffix to test different answering routes. For example, `youremail+test1@email.com` or `youremail+test2@email.com`.

=== "Shopify (Legacy)"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    If you want to set up a post-quiz email flow with Mailchimp, you can follow the steps below:

    1. **Connect Your Quiz to Mailchimp.** Follow the instructions in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

        !!! tip

            Remember to take a test quiz/preview the quiz leaving a sample email address in order to send first data to Mailchimp and test the connection. You can use your real email with a +test1, +test2 to test different answering routes. For example, youremail+test1@email.com or youremail+test2@email.com.
    2. **Use Customer Tags for Segmentation.** Once your quiz is connected you should consider what data you want to send to Mailchimp from the quiz. You can, for example:
    
        - [Create customer tags in your quiz](/reference/quiz-builder/link-collections/#customer-tags) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            Mailchimp API only supports email, name, and customer tags to be send from the quiz. To override Mailchimp’s limitation on pushing detailed quiz data, you can use customer tags to represent customer responses.
    3. **Design Email Campaigns.** Once the quiz answers are covered with customer tags, all the information you need about your customer will start flowing into Mailchimp. That’s when you can set up your email campaigns. 
        
        - You can start by setting up Automations (automated email flows) to trigger based on specific tags or quiz completions.
        - Then, create different email templates in Mailchimp that correspond to different quiz outcomes or automation flows.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as “Oily Skin,” “Dry Skin,” etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin. 
            - Day 3: Customer testimonials and reviews for oily skin products. 
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and Optimize.** After setting up your email campaigns, test them with a test email and optimize them based on the results.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    If you want to set up a post-quiz email flow with Mailchimp, you can follow the steps below:

    1. **Connect Your Quiz to Mailchimp.** Follow the instructions in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

        !!! tip

            Remember to take a test quiz/preview the quiz leaving a sample email address in order to send first data to Mailchimp and test the connection. You can use your real email with a +test1, +test2 to test different answering routes. For example, youremail+test1@email.com or youremail+test2@email.com.
    2. **Use Customer Tags for Segmentation.** Once your quiz is connected you should consider what data you want to send to Mailchimp from the quiz. You can, for example:
    
        - [Create customer tags in your quiz](/reference/quiz-builder/link-collections/#customer-tags) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            Mailchimp API only supports email, name, and customer tags to be send from the quiz. To override Mailchimp’s limitation on pushing detailed quiz data, you can use customer tags to represent customer responses.
    3. **Design Email Campaigns.** Once the quiz answers are covered with customer tags, all the information you need about your customer will start flowing into Mailchimp. That’s when you can set up your email campaigns. 
        
        - You can start by setting up Automations (automated email flows) to trigger based on specific tags or quiz completions.
        - Then, create different email templates in Mailchimp that correspond to different quiz outcomes or automation flows.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as “Oily Skin,” “Dry Skin,” etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin. 
            - Day 3: Customer testimonials and reviews for oily skin products. 
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and Optimize.** After setting up your email campaigns, test them with a test email and optimize them based on the results.


=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    If you want to set up a post-quiz email flow with Mailchimp, you can follow the steps below:

    1. **Connect Your Quiz to Mailchimp.** Follow the instructions in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

        !!! tip

            Remember to take a test quiz/preview the quiz leaving a sample email address in order to send first data to Mailchimp and test the connection. You can use your real email with a +test1, +test2 to test different answering routes. For example, youremail+test1@email.com or youremail+test2@email.com.
    2. **Use Customer Tags for Segmentation.** Once your quiz is connected you should consider what data you want to send to Mailchimp from the quiz. You can, for example:
    
        - [Create customer tags in your quiz](/reference/quiz-builder/link-collections/#customer-tags) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            Mailchimp API only supports email, name, and customer tags to be send from the quiz. To override Mailchimp’s limitation on pushing detailed quiz data, you can use customer tags to represent customer responses.
    3. **Design Email Campaigns.** Once the quiz answers are covered with customer tags, all the information you need about your customer will start flowing into Mailchimp. That’s when you can set up your email campaigns. 
        
        - You can start by setting up Automations (automated email flows) to trigger based on specific tags or quiz completions.
        - Then, create different email templates in Mailchimp that correspond to different quiz outcomes or automation flows.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as “Oily Skin,” “Dry Skin,” etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin. 
            - Day 3: Customer testimonials and reviews for oily skin products. 
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and Optimize.** After setting up your email campaigns, test them with a test email and optimize them based on the results.


=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    If you want to set up a post-quiz email flow with Mailchimp, you can follow the steps below:

    1. **Connect Your Quiz to Mailchimp.** Follow the instructions in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

        !!! tip

            Remember to take a test quiz/preview the quiz leaving a sample email address in order to send first data to Mailchimp and test the connection. You can use your real email with a +test1, +test2 to test different answering routes. For example, youremail+test1@email.com or youremail+test2@email.com.
    2. **Use Customer Tags for Segmentation.** Once your quiz is connected you should consider what data you want to send to Mailchimp from the quiz. You can, for example:
    
        - [Create customer tags in your quiz](/reference/quiz-builder/link-collections/#customer-tags) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            Mailchimp API only supports email, name, and customer tags to be send from the quiz. To override Mailchimp’s limitation on pushing detailed quiz data, you can use customer tags to represent customer responses.
    3. **Design Email Campaigns.** Once the quiz answers are covered with customer tags, all the information you need about your customer will start flowing into Mailchimp. That’s when you can set up your email campaigns. 
        
        - You can start by setting up Automations (automated email flows) to trigger based on specific tags or quiz completions.
        - Then, create different email templates in Mailchimp that correspond to different quiz outcomes or automation flows.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as “Oily Skin,” “Dry Skin,” etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin. 
            - Day 3: Customer testimonials and reviews for oily skin products. 
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and Optimize.** After setting up your email campaigns, test them with a test email and optimize them based on the results.


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/PoLkSjl628o?si=iiIQVsgUgd46BJbu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    If you want to set up a post-quiz email flow with Mailchimp, you can follow the steps below:

    1. **Connect Your Quiz to Mailchimp.** Follow the instructions in the [Link Quiz to Mailchimp](#link-quiz-to-mailchimp) section.

        !!! tip

            Remember to take a test quiz/preview the quiz leaving a sample email address in order to send first data to Mailchimp and test the connection. You can use your real email with a +test1, +test2 to test different answering routes. For example, youremail+test1@email.com or youremail+test2@email.com.
    2. **Use Customer Tags for Segmentation.** Once your quiz is connected you should consider what data you want to send to Mailchimp from the quiz. You can, for example:
    
        - [Create customer tags in your quiz](/reference/quiz-builder/link-collections/#customer-tags) to represent different quiz responses.
        - Link these tags to specific answers in your quiz.
        - Upon completion of the quiz by a participant, Mailchimp will receive all the tags that the customer picked based on their choices.
        - In Mailchimp, you can use these tags to segment your audience and tailor your email campaigns.

        !!! warning

            Mailchimp API only supports email, name, and customer tags to be send from the quiz. To override Mailchimp’s limitation on pushing detailed quiz data, you can use customer tags to represent customer responses.
    3. **Design Email Campaigns.** Once the quiz answers are covered with customer tags, all the information you need about your customer will start flowing into Mailchimp. That’s when you can set up your email campaigns. 
        
        - You can start by setting up Automations (automated email flows) to trigger based on specific tags or quiz completions.
        - Then, create different email templates in Mailchimp that correspond to different quiz outcomes or automation flows.

        !!! example

            Imagine you run a skincare ecommerce store. Your quiz asks customers about their skin type and concerns. Based on their answers, you tag them as “Oily Skin,” “Dry Skin,” etc.

            In Mailchimp, you create an email series targeting these tags. For instance:

            - Day 1: Introduction to products suitable for oily skin. 
            - Day 3: Customer testimonials and reviews for oily skin products. 
            - Day 7: Special discount on recommended products for oily skin.

    4. **Test and Optimize.** After setting up your email campaigns, test them with a test email and optimize them based on the results.


## Disconnect Mailchimp

=== "Shopify"

    **Stop sending data from one quiz**

    Uncheck the `Send Quiz Leads to Mailchimp` checkbox in that specific quiz's [`Quiz Settings > Integrations`](/reference/quiz-builder/connect-integrations/) tab and click `Save`. Other quizzes in the account keep sending data to Mailchimp.

    **Disconnect Mailchimp from your account**

    1. Go to [`Quiz Settings > Integrations`](/reference/quiz-builder/connect-integrations/).
    2. Scroll to the Mailchimp card and click `Disconnect`.
    3. Confirm the action.

    No more quiz data will flow to Mailchimp from any quiz in the account.

=== "Shopify (Legacy)"

    Open the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and remove the connection. Then click the `Publish` button to update the preview/live quiz with the new settings.

=== "WooCommerce"

    Open the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and remove the connection. Then click the `Publish` button to update the preview/live quiz with the new settings.

=== "Magento"

    Open the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and remove the connection. Then click the `Publish` button to update the preview/live quiz with the new settings.

=== "BigCommerce"

    Open the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and remove the connection. Then click the `Publish` button to update the preview/live quiz with the new settings.

=== "Standalone"

    Open the [Connect](/reference/quiz-builder/connect-integrations/) tab in your quiz, scroll to the Mailchimp section and remove the connection. Then click the `Publish` button to update the preview/live quiz with the new settings.

## Alternative Ways to Send Quiz Leads to Mailchimp

=== "Shopify"

    Sometimes, you would like a bit more control over the data that is sent to Mailchimp, for example to pass full quiz answers or recommended products, which the native integration doesn't sync. In that case there are a few alternatives you can use.

    - **Using Shopify Customers**: You can use Shopify Customers to send quiz leads to Mailchimp. Just connect your quiz to Shopify Customers following [this guide](/how-to-guides/send-leads-to-shopify-customers/). Then, use a native Shopify - Mailchimp integration to send the quiz leads to Mailchimp.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Mailchimp. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Mailchimp.
    - **Manually adding the quiz leads to Mailchimp**: You can manually add the quiz leads to Mailchimp by uploading a CSV file generated from the quiz [responses](/reference/quiz-builder/metrics/#responses) section.

=== "Shopify (Legacy)"

    Sometimes, you would like a bit more control over the data that is sent to Mailchimp. In that case there are a few alternatives you can use to send quiz leads to Mailchimp.

    - **Using Shopify Customers**: You can use Shopify Customers to send quiz leads to Mailchimp. Just connect your quiz to Shopify Customers following [this guide](/how-to-guides/send-leads-to-shopify-customers/). Then, use a native Shopify - Mailchimp integration to send the quiz leads to Mailchimp.
    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to Mailchimp. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to Mailchimp.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Mailchimp. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Mailchimp.
    - **Manually adding the quiz leads to Mailchimp**: You can manually add the quiz leads to Mailchimp by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.
    
=== "WooCommerce"

    Sometimes, you would like a bit more control over the data that is sent to Mailchimp. In that case there are a few alternatives you can use to send quiz leads to Mailchimp.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to Mailchimp. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to Mailchimp.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Mailchimp. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Mailchimp.
    - **Manually adding the quiz leads to Mailchimp**: You can manually add the quiz leads to Mailchimp by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.


=== "Magento"


    Sometimes, you would like a bit more control over the data that is sent to Mailchimp. In that case there are a few alternatives you can use to send quiz leads to Mailchimp.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to Mailchimp. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to Mailchimp.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Mailchimp. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Mailchimp.
    - **Manually adding the quiz leads to Mailchimp**: You can manually add the quiz leads to Mailchimp by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

=== "BigCommerce"


    Sometimes, you would like a bit more control over the data that is sent to Mailchimp. In that case there are a few alternatives you can use to send quiz leads to Mailchimp.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to Mailchimp. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to Mailchimp.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Mailchimp. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Mailchimp.
    - **Manually adding the quiz leads to Mailchimp**: You can manually add the quiz leads to Mailchimp by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

=== "Standalone"


    Sometimes, you would like a bit more control over the data that is sent to Mailchimp. In that case there are a few alternatives you can use to send quiz leads to Mailchimp.

    - **Using Zapier**: You can use out native Zapier integration to send quiz leads to Mailchimp. Just connect your quiz to Zapier following [this guide](/how-to-guides/send-leads-to-zapier/). Then, in Zapier set up a redirection of selected data to Mailchimp.
    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Mailchimp. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Mailchimp.
    - **Manually adding the quiz leads to Mailchimp**: You can manually add the quiz leads to Mailchimp by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

---
This article explains how to send leads to Mailchimp from your quiz created in the RevenueHunt app.
