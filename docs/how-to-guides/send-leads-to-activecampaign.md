---
description: "Learn how to send RevenueHunt quiz leads to ActiveCampaign via webhooks or CSV export."
icon: material/bullhorn-outline
---

# How to Send Leads to ActiveCampaign

=== "Shopify"


    The Built for Shopify version of the RevenueHunt app does not connect to ActiveCampaign directly yet. There are three ways around it.

    You can forward the quiz data through [Zapier](/how-to-guides/send-leads-to-zapier/) or [Webhooks](/how-to-guides/send-leads-to-webhooks/), or you can export your responses as a CSV file and upload that file to ActiveCampaign. This article covers all three.

    Zapier is the shortest route, because it has a ready-made ActiveCampaign connector and you build the link by picking fields on screen.


=== "Shopify (Legacy)"

    Connect your quiz to ActiveCampaign and every response becomes a contact there, with the customer's answers attached.

    This article explains how to make that connection, and how to use the answers to follow up by email.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration sends the raw quiz data to ActiveCampaign. Build the flows and the custom events from that data in ActiveCampaign itself.


=== "WooCommerce"


    Connect your quiz to ActiveCampaign and every response becomes a contact there, with the customer's answers attached.

    This article explains how to make that connection, and how to use the answers to follow up by email.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration sends the raw quiz data to ActiveCampaign. Build the flows and the custom events from that data in ActiveCampaign itself.


=== "Magento"


    Connect your quiz to ActiveCampaign and every response becomes a contact there, with the customer's answers attached.

    This article explains how to make that connection, and how to use the answers to follow up by email.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration sends the raw quiz data to ActiveCampaign. Build the flows and the custom events from that data in ActiveCampaign itself.


=== "BigCommerce"


    Connect your quiz to ActiveCampaign and every response becomes a contact there, with the customer's answers attached.

    This article explains how to make that connection, and how to use the answers to follow up by email.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration sends the raw quiz data to ActiveCampaign. Build the flows and the custom events from that data in ActiveCampaign itself.


=== "Standalone"


    Connect your quiz to ActiveCampaign and every response becomes a contact there, with the customer's answers attached.

    This article explains how to make that connection, and how to use the answers to follow up by email.

    Before you begin, ensure you have:

    - An active ActiveCampaign account.
    - A quiz built on the RevenueHunt platform.

    !!! note

        The integration sends the raw quiz data to ActiveCampaign. Build the flows and the custom events from that data in ActiveCampaign itself.


## Link quiz to ActiveCampaign

=== "Shopify"

    You cannot link a quiz to ActiveCampaign from the Built for Shopify version of the app yet.

    See [Alternative ways to send quiz leads to ActiveCampaign](#alternative-ways-to-send-quiz-leads-to-activecampaign) for the two ways around it.


=== "Shopify (Legacy)"

    To integrate your quiz with ActiveCampaign:

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    3. **Find ActiveCampaign in the integration list and copy `Your API Token`.** You need it in step 6.
        ![how to send leads to activecampaign](/images/how_to_send_leads_to_activecampaign.png)
    4. **Click the `Connect` button in the ActiveCampaign section.**
    5. **Click `Add an account`.** ActiveCampaign opens the `Create Contacts From Quiz Responses` setup, which runs in three steps: `Connect`, `Select the Quiz` and `Mapping`.
        ![how to send leads to activecampaign step1](/images/how_to_send_leads_to_activecampaign_step1.png)

    6. **Paste the token into the `Token` field and click `Connect`.**
        ![how to send leads to activecampaign step2](/images/how_to_send_leads_to_activecampaign_step2.png)

    7. **Select the quiz you want to integrate, then click `Continue`.**
        ![how to send leads to activecampaign step3](/images/how_to_send_leads_to_activecampaign_step3.png)

    8. **Map your quiz responses to the matching fields in ActiveCampaign.** You may need to add new field mappings.
        ![how to activecampaign connect](/images/how_to_activecampaign_connect.png)

    Your quiz is now connected. Change the settings or update the integration from the same screen.

    ![how to send leads to activecampaign step final](/images/how_to_send_leads_to_activecampaign_step_final.png)

    You can also start the connection from inside ActiveCampaign:

    1. **Go to the `Apps` menu in ActiveCampaign and search for `Product Recommendation Quiz`.**

        !!! warning

            If you cannot see the Apps page, ActiveCampaign branding is probably turned off for your account. In your account settings, turn the ActiveCampaign branding setting off and then back on. Then check whether the Apps page appears.

    2. **Select the quiz icon and follow the setup instructions.** You will be asked for a `Token`, which links the quiz data to your ActiveCampaign account. This is the app's own API token, not an ActiveCampaign one. Find it under `Your API Token` in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section.

    !!! note

        The quiz only sends the raw data. Build any flow or custom event from that data in ActiveCampaign itself. Ask the ActiveCampaign support team about that part of the setup.

=== "WooCommerce"


    To integrate your quiz with ActiveCampaign:

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    3. **Find ActiveCampaign in the integration list and copy `Your API Token`.** You need it in step 6.
        ![how to send leads to activecampaign](/images/how_to_send_leads_to_activecampaign.png)
    4. **Click the `Connect` button in the ActiveCampaign section.**
    5. **Click `Add an account`.** ActiveCampaign opens the `Create Contacts From Quiz Responses` setup, which runs in three steps: `Connect`, `Select the Quiz` and `Mapping`.
        ![how to send leads to activecampaign step1](/images/how_to_send_leads_to_activecampaign_step1.png)

    6. **Paste the token into the `Token` field and click `Connect`.**
        ![how to send leads to activecampaign step2](/images/how_to_send_leads_to_activecampaign_step2.png)

    7. **Select the quiz you want to integrate, then click `Continue`.**
        ![how to send leads to activecampaign step3](/images/how_to_send_leads_to_activecampaign_step3.png)

    8. **Map your quiz responses to the matching fields in ActiveCampaign.** You may need to add new field mappings.
        ![how to activecampaign connect](/images/how_to_activecampaign_connect.png)

    Your quiz is now connected. Change the settings or update the integration from the same screen.

    ![how to send leads to activecampaign step final](/images/how_to_send_leads_to_activecampaign_step_final.png)

    You can also start the connection from inside ActiveCampaign:

    1. **Go to the `Apps` menu in ActiveCampaign and search for `Product Recommendation Quiz`.**

        !!! warning

            If you cannot see the Apps page, ActiveCampaign branding is probably turned off for your account. In your account settings, turn the ActiveCampaign branding setting off and then back on. Then check whether the Apps page appears.

    2. **Select the quiz icon and follow the setup instructions.** You will be asked for a `Token`, which links the quiz data to your ActiveCampaign account. This is the app's own API token, not an ActiveCampaign one. Find it under `Your API Token` in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section.

    !!! note

        The quiz only sends the raw data. Build any flow or custom event from that data in ActiveCampaign itself. Ask the ActiveCampaign support team about that part of the setup.


=== "Magento"


    To integrate your quiz with ActiveCampaign:

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    3. **Find ActiveCampaign in the integration list and copy `Your API Token`.** You need it in step 6.
        ![how to send leads to activecampaign](/images/how_to_send_leads_to_activecampaign.png)
    4. **Click the `Connect` button in the ActiveCampaign section.**
    5. **Click `Add an account`.** ActiveCampaign opens the `Create Contacts From Quiz Responses` setup, which runs in three steps: `Connect`, `Select the Quiz` and `Mapping`.
        ![how to send leads to activecampaign step1](/images/how_to_send_leads_to_activecampaign_step1.png)

    6. **Paste the token into the `Token` field and click `Connect`.**
        ![how to send leads to activecampaign step2](/images/how_to_send_leads_to_activecampaign_step2.png)

    7. **Select the quiz you want to integrate, then click `Continue`.**
        ![how to send leads to activecampaign step3](/images/how_to_send_leads_to_activecampaign_step3.png)

    8. **Map your quiz responses to the matching fields in ActiveCampaign.** You may need to add new field mappings.
        ![how to activecampaign connect](/images/how_to_activecampaign_connect.png)

    Your quiz is now connected. Change the settings or update the integration from the same screen.

    ![how to send leads to activecampaign step final](/images/how_to_send_leads_to_activecampaign_step_final.png)

    You can also start the connection from inside ActiveCampaign:

    1. **Go to the `Apps` menu in ActiveCampaign and search for `Product Recommendation Quiz`.**

        !!! warning

            If you cannot see the Apps page, ActiveCampaign branding is probably turned off for your account. In your account settings, turn the ActiveCampaign branding setting off and then back on. Then check whether the Apps page appears.

    2. **Select the quiz icon and follow the setup instructions.** You will be asked for a `Token`, which links the quiz data to your ActiveCampaign account. This is the app's own API token, not an ActiveCampaign one. Find it under `Your API Token` in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section.

    !!! note

        The quiz only sends the raw data. Build any flow or custom event from that data in ActiveCampaign itself. Ask the ActiveCampaign support team about that part of the setup.

=== "BigCommerce"


    To integrate your quiz with ActiveCampaign:

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    3. **Find ActiveCampaign in the integration list and copy `Your API Token`.** You need it in step 6.
        ![how to send leads to activecampaign](/images/how_to_send_leads_to_activecampaign.png)
    4. **Click the `Connect` button in the ActiveCampaign section.**
    5. **Click `Add an account`.** ActiveCampaign opens the `Create Contacts From Quiz Responses` setup, which runs in three steps: `Connect`, `Select the Quiz` and `Mapping`.
        ![how to send leads to activecampaign step1](/images/how_to_send_leads_to_activecampaign_step1.png)

    6. **Paste the token into the `Token` field and click `Connect`.**
        ![how to send leads to activecampaign step2](/images/how_to_send_leads_to_activecampaign_step2.png)

    7. **Select the quiz you want to integrate, then click `Continue`.**
        ![how to send leads to activecampaign step3](/images/how_to_send_leads_to_activecampaign_step3.png)

    8. **Map your quiz responses to the matching fields in ActiveCampaign.** You may need to add new field mappings.
        ![how to activecampaign connect](/images/how_to_activecampaign_connect.png)

    Your quiz is now connected. Change the settings or update the integration from the same screen.

    ![how to send leads to activecampaign step final](/images/how_to_send_leads_to_activecampaign_step_final.png)

    You can also start the connection from inside ActiveCampaign:

    1. **Go to the `Apps` menu in ActiveCampaign and search for `Product Recommendation Quiz`.**

        !!! warning

            If you cannot see the Apps page, ActiveCampaign branding is probably turned off for your account. In your account settings, turn the ActiveCampaign branding setting off and then back on. Then check whether the Apps page appears.

    2. **Select the quiz icon and follow the setup instructions.** You will be asked for a `Token`, which links the quiz data to your ActiveCampaign account. This is the app's own API token, not an ActiveCampaign one. Find it under `Your API Token` in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section.

    !!! note

        The quiz only sends the raw data. Build any flow or custom event from that data in ActiveCampaign itself. Ask the ActiveCampaign support team about that part of the setup.

=== "Standalone"


    To integrate your quiz with ActiveCampaign:

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the screen.**
    3. **Find ActiveCampaign in the integration list and copy `Your API Token`.** You need it in step 6.
        ![how to send leads to activecampaign](/images/how_to_send_leads_to_activecampaign.png)
    4. **Click the `Connect` button in the ActiveCampaign section.**
    5. **Click `Add an account`.** ActiveCampaign opens the `Create Contacts From Quiz Responses` setup, which runs in three steps: `Connect`, `Select the Quiz` and `Mapping`.
        ![how to send leads to activecampaign step1](/images/how_to_send_leads_to_activecampaign_step1.png)

    6. **Paste the token into the `Token` field and click `Connect`.**
        ![how to send leads to activecampaign step2](/images/how_to_send_leads_to_activecampaign_step2.png)

    7. **Select the quiz you want to integrate, then click `Continue`.**
        ![how to send leads to activecampaign step3](/images/how_to_send_leads_to_activecampaign_step3.png)

    8. **Map your quiz responses to the matching fields in ActiveCampaign.** You may need to add new field mappings.
        ![how to activecampaign connect](/images/how_to_activecampaign_connect.png)

    Your quiz is now connected. Change the settings or update the integration from the same screen.

    ![how to send leads to activecampaign step final](/images/how_to_send_leads_to_activecampaign_step_final.png)

    You can also start the connection from inside ActiveCampaign:

    1. **Go to the `Apps` menu in ActiveCampaign and search for `Product Recommendation Quiz`.**

        !!! warning

            If you cannot see the Apps page, ActiveCampaign branding is probably turned off for your account. In your account settings, turn the ActiveCampaign branding setting off and then back on. Then check whether the Apps page appears.

    2. **Select the quiz icon and follow the setup instructions.** You will be asked for a `Token`, which links the quiz data to your ActiveCampaign account. This is the app's own API token, not an ActiveCampaign one. Find it under `Your API Token` in the [`Connect`](/reference/quiz-builder/connect-integrations/) > ActiveCampaign section.

    !!! note

        The quiz only sends the raw data. Build any flow or custom event from that data in ActiveCampaign itself. Ask the ActiveCampaign support team about that part of the setup.


## Alternative ways to send quiz leads to ActiveCampaign

=== "Shopify"

    To control exactly which data reaches ActiveCampaign, use one of these methods instead.

    - **Using Zapier**: connect your quiz to Zapier, as described in [how to send leads to Zapier](/how-to-guides/send-leads-to-zapier/). Then, in Zapier, add ActiveCampaign as the action and map the quiz fields to contact fields.
    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to ActiveCampaign.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to ActiveCampaign.


=== "Shopify (Legacy)"

    To control exactly which data reaches ActiveCampaign, use one of these methods instead.

    - **Using Zapier**: connect your quiz to Zapier, as described in [how to send leads to Zapier](/how-to-guides/send-leads-to-zapier/). Then, in Zapier, forward the data you want to ActiveCampaign.
    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to ActiveCampaign.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to ActiveCampaign.

=== "WooCommerce"

    To control exactly which data reaches ActiveCampaign, use one of these methods instead.

    - **Using Zapier**: connect your quiz to Zapier, as described in [how to send leads to Zapier](/how-to-guides/send-leads-to-zapier/). Then, in Zapier, forward the data you want to ActiveCampaign.
    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to ActiveCampaign.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to ActiveCampaign.


=== "Magento"


    To control exactly which data reaches ActiveCampaign, use one of these methods instead.

    - **Using Zapier**: connect your quiz to Zapier, as described in [how to send leads to Zapier](/how-to-guides/send-leads-to-zapier/). Then, in Zapier, forward the data you want to ActiveCampaign.
    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to ActiveCampaign.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to ActiveCampaign.

=== "BigCommerce"


    To control exactly which data reaches ActiveCampaign, use one of these methods instead.

    - **Using Zapier**: connect your quiz to Zapier, as described in [how to send leads to Zapier](/how-to-guides/send-leads-to-zapier/). Then, in Zapier, forward the data you want to ActiveCampaign.
    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to ActiveCampaign.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to ActiveCampaign.

=== "Standalone"


    To control exactly which data reaches ActiveCampaign, use one of these methods instead.

    - **Using Zapier**: connect your quiz to Zapier, as described in [how to send leads to Zapier](/how-to-guides/send-leads-to-zapier/). Then, in Zapier, forward the data you want to ActiveCampaign.
    - **Using Webhooks**: connect your quiz to Webhooks, as described in [how to send leads to webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to ActiveCampaign.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to ActiveCampaign.


## Adding custom information to the contact profile

=== "Shopify"


    Once the quiz is connected through [one of the methods above](#alternative-ways-to-send-quiz-leads-to-activecampaign), you can add quiz data to each contact profile.

    These are the fields you can add:

    - Email
    - First Name
    - Full Name
    - Quiz ID
    - Quiz Name
    - Response ID
    - Tags
    - Permalink
    - Permalink Hash
    - Recommended Product IDs

    !!! warning

        These methods give you full control over what reaches ActiveCampaign. The list above holds only the most common fields.

        The exact payload is the one carried by the method you pick, so see [what data is sent to Zapier?](/how-to-guides/send-leads-to-zapier/#what-data-is-sent-to-zapier) or [what data is sent to webhook?](/how-to-guides/send-leads-to-webhooks/#what-data-is-sent-to-webhook) for the full field list.

        For more about using this data on a contact profile, see the [ActiveCampaign documentation](https://help.activecampaign.com/hc/en-us/articles/115001374664-How-to-manage-custom-contact-fields).

    To forward only the data you want, connect your quiz to [Zapier](/how-to-guides/send-leads-to-zapier/) and map the fields there.

    The other option is [Webhooks](/how-to-guides/send-leads-to-webhooks/). Set up the forwarding on the ActiveCampaign side, using [their webhooks documentation](https://developers.activecampaign.com/page/webhooks).


=== "Shopify (Legacy)"

    Once the quiz is connected, you can add the quiz data to each contact profile.

    Quiz data is added to the contact as **custom fields**, and quiz tags are added as native ActiveCampaign tags.

    !!! warning "Create the custom fields in ActiveCampaign first"

        ActiveCampaign does not create fields for you. Add each field in your ActiveCampaign dashboard first, or the sync has nowhere to write. The field's **Personalization Tag**, which is its unique key, must match the internal name in the field table. For an answer field, that is the slide hash ID.

    | Field | Value |
    | --- | --- |
    | `email` | The contact's primary identifier. |
    | `first_name`, `last_name`, `full_name` | The contact's name, as captured in the quiz. |
    | `phone_number` | All captured phone numbers, joined by `/`. |
    | `quiz_id` | The quiz Hash ID, for example `wnHR8G`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `products_ids` | Comma-separated list of the recommended product IDs. |
    | `[SLIDE_HASHID]` | One field per question, keyed by the slide's internal hash ID. The value is the text of the answer selected. |
    | `tags` | All [tags](/how-to-guides/use-customer-tags/) assigned, joined into a single field. |

    !!! info "Tags are also sent natively"
        Besides the `tags` custom field, quiz tags are pushed to ActiveCampaign's own tag system, so they appear as real tags on the contact profile. That makes them the easiest way to start an automation, using the `Tag Added` trigger.

    !!! info "Answer keys and date questions"
        Answer fields are keyed by the slide's internal hash ID, not by the question title, so renaming a question does not break your field mapping. Answers to date questions are sent in ISO8601 format.

    !!! warning "Products are sent as IDs only"
        The legacy integration sends recommended products as a list of IDs in `products_ids`, without titles, prices or images. If you need full product details, use [Zapier](/how-to-guides/send-leads-to-zapier/) or [Webhooks](/how-to-guides/send-leads-to-webhooks/) instead.

    To add these fields to a new profile:

    1. **In ActiveCampaign, go to `Lists > Manage fields` and click `Add Field`.**
        ![how to send leads to activecampaign new field1](/images/how_to_send_leads_to_activecampaign_new_field1.png)
    2. **Give each field a name.**
        ![how to send leads to activecampaign new field2](/images/how_to_send_leads_to_activecampaign_new_field2.png)
    3. **Find the new fields under `General Details`.** ActiveCampaign files them there.
        ![how to send leads to activecampaign new field3](/images/how_to_send_leads_to_activecampaign_new_field3.png)
    4. **Return to the `Product Recommendation Quiz` app in ActiveCampaign and map the new fields.** Every later contact from the quiz then carries this data.
        ![how to activecampaign mapping](/images/how_to_activecampaign_mapping.png)

    From then on, every new contact from the quiz carries the extra fields.

    ![how to activecampaign profile](/images/how_to_activecampaign_profile.png)


=== "WooCommerce"


    Once the quiz is connected, you can add the quiz data to each contact profile.

    Quiz data is added to the contact as **custom fields**, and quiz tags are added as native ActiveCampaign tags.

    !!! warning "Create the custom fields in ActiveCampaign first"

        ActiveCampaign does not create fields for you. Add each field in your ActiveCampaign dashboard first, or the sync has nowhere to write. The field's **Personalization Tag**, which is its unique key, must match the internal name in the field table. For an answer field, that is the slide hash ID.

    | Field | Value |
    | --- | --- |
    | `email` | The contact's primary identifier. |
    | `first_name`, `last_name`, `full_name` | The contact's name, as captured in the quiz. |
    | `phone_number` | All captured phone numbers, joined by `/`. |
    | `quiz_id` | The quiz Hash ID, for example `wnHR8G`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `products_ids` | Comma-separated list of the recommended product IDs. |
    | `[SLIDE_HASHID]` | One field per question, keyed by the slide's internal hash ID. The value is the text of the answer selected. |
    | `tags` | All [tags](/how-to-guides/use-customer-tags/) assigned, joined into a single field. |

    !!! info "Tags are also sent natively"
        Besides the `tags` custom field, quiz tags are pushed to ActiveCampaign's own tag system, so they appear as real tags on the contact profile. That makes them the easiest way to start an automation, using the `Tag Added` trigger.

    !!! info "Answer keys and date questions"
        Answer fields are keyed by the slide's internal hash ID, not by the question title, so renaming a question does not break your field mapping. Answers to date questions are sent in ISO8601 format.

    !!! warning "Products are sent as IDs only"
        The legacy integration sends recommended products as a list of IDs in `products_ids`, without titles, prices or images. If you need full product details, use [Zapier](/how-to-guides/send-leads-to-zapier/) or [Webhooks](/how-to-guides/send-leads-to-webhooks/) instead.

    To add these fields to a new profile:

    1. **In ActiveCampaign, go to `Lists > Manage fields` and click `Add Field`.**
        ![how to send leads to activecampaign new field1](/images/how_to_send_leads_to_activecampaign_new_field1.png)
    2. **Give each field a name.**
        ![how to send leads to activecampaign new field2](/images/how_to_send_leads_to_activecampaign_new_field2.png)
    3. **Find the new fields under `General Details`.** ActiveCampaign files them there.
        ![how to send leads to activecampaign new field3](/images/how_to_send_leads_to_activecampaign_new_field3.png)
    4. **Return to the `Product Recommendation Quiz` app in ActiveCampaign and map the new fields.** Every later contact from the quiz then carries this data.
        ![how to activecampaign mapping](/images/how_to_activecampaign_mapping.png)

    From then on, every new contact from the quiz carries the extra fields.

    ![how to activecampaign profile](/images/how_to_activecampaign_profile.png)


=== "Magento"


    Once the quiz is connected, you can add the quiz data to each contact profile.

    Quiz data is added to the contact as **custom fields**, and quiz tags are added as native ActiveCampaign tags.

    !!! warning "Create the custom fields in ActiveCampaign first"

        ActiveCampaign does not create fields for you. Add each field in your ActiveCampaign dashboard first, or the sync has nowhere to write. The field's **Personalization Tag**, which is its unique key, must match the internal name in the field table. For an answer field, that is the slide hash ID.

    | Field | Value |
    | --- | --- |
    | `email` | The contact's primary identifier. |
    | `first_name`, `last_name`, `full_name` | The contact's name, as captured in the quiz. |
    | `phone_number` | All captured phone numbers, joined by `/`. |
    | `quiz_id` | The quiz Hash ID, for example `wnHR8G`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `products_ids` | Comma-separated list of the recommended product IDs. |
    | `[SLIDE_HASHID]` | One field per question, keyed by the slide's internal hash ID. The value is the text of the answer selected. |
    | `tags` | All [tags](/how-to-guides/use-customer-tags/) assigned, joined into a single field. |

    !!! info "Tags are also sent natively"
        Besides the `tags` custom field, quiz tags are pushed to ActiveCampaign's own tag system, so they appear as real tags on the contact profile. That makes them the easiest way to start an automation, using the `Tag Added` trigger.

    !!! info "Answer keys and date questions"
        Answer fields are keyed by the slide's internal hash ID, not by the question title, so renaming a question does not break your field mapping. Answers to date questions are sent in ISO8601 format.

    !!! warning "Products are sent as IDs only"
        The legacy integration sends recommended products as a list of IDs in `products_ids`, without titles, prices or images. If you need full product details, use [Zapier](/how-to-guides/send-leads-to-zapier/) or [Webhooks](/how-to-guides/send-leads-to-webhooks/) instead.

    To add these fields to a new profile:

    1. **In ActiveCampaign, go to `Lists > Manage fields` and click `Add Field`.**
        ![how to send leads to activecampaign new field1](/images/how_to_send_leads_to_activecampaign_new_field1.png)
    2. **Give each field a name.**
        ![how to send leads to activecampaign new field2](/images/how_to_send_leads_to_activecampaign_new_field2.png)
    3. **Find the new fields under `General Details`.** ActiveCampaign files them there.
        ![how to send leads to activecampaign new field3](/images/how_to_send_leads_to_activecampaign_new_field3.png)
    4. **Return to the `Product Recommendation Quiz` app in ActiveCampaign and map the new fields.** Every later contact from the quiz then carries this data.
        ![how to activecampaign mapping](/images/how_to_activecampaign_mapping.png)

    From then on, every new contact from the quiz carries the extra fields.

    ![how to activecampaign profile](/images/how_to_activecampaign_profile.png)


=== "BigCommerce"


    Once the quiz is connected, you can add the quiz data to each contact profile.

    Quiz data is added to the contact as **custom fields**, and quiz tags are added as native ActiveCampaign tags.

    !!! warning "Create the custom fields in ActiveCampaign first"

        ActiveCampaign does not create fields for you. Add each field in your ActiveCampaign dashboard first, or the sync has nowhere to write. The field's **Personalization Tag**, which is its unique key, must match the internal name in the field table. For an answer field, that is the slide hash ID.

    | Field | Value |
    | --- | --- |
    | `email` | The contact's primary identifier. |
    | `first_name`, `last_name`, `full_name` | The contact's name, as captured in the quiz. |
    | `phone_number` | All captured phone numbers, joined by `/`. |
    | `quiz_id` | The quiz Hash ID, for example `wnHR8G`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `products_ids` | Comma-separated list of the recommended product IDs. |
    | `[SLIDE_HASHID]` | One field per question, keyed by the slide's internal hash ID. The value is the text of the answer selected. |
    | `tags` | All [tags](/how-to-guides/use-customer-tags/) assigned, joined into a single field. |

    !!! info "Tags are also sent natively"
        Besides the `tags` custom field, quiz tags are pushed to ActiveCampaign's own tag system, so they appear as real tags on the contact profile. That makes them the easiest way to start an automation, using the `Tag Added` trigger.

    !!! info "Answer keys and date questions"
        Answer fields are keyed by the slide's internal hash ID, not by the question title, so renaming a question does not break your field mapping. Answers to date questions are sent in ISO8601 format.

    !!! warning "Products are sent as IDs only"
        The legacy integration sends recommended products as a list of IDs in `products_ids`, without titles, prices or images. If you need full product details, use [Zapier](/how-to-guides/send-leads-to-zapier/) or [Webhooks](/how-to-guides/send-leads-to-webhooks/) instead.

    To add these fields to a new profile:

    1. **In ActiveCampaign, go to `Lists > Manage fields` and click `Add Field`.**
        ![how to send leads to activecampaign new field1](/images/how_to_send_leads_to_activecampaign_new_field1.png)
    2. **Give each field a name.**
        ![how to send leads to activecampaign new field2](/images/how_to_send_leads_to_activecampaign_new_field2.png)
    3. **Find the new fields under `General Details`.** ActiveCampaign files them there.
        ![how to send leads to activecampaign new field3](/images/how_to_send_leads_to_activecampaign_new_field3.png)
    4. **Return to the `Product Recommendation Quiz` app in ActiveCampaign and map the new fields.** Every later contact from the quiz then carries this data.
        ![how to activecampaign mapping](/images/how_to_activecampaign_mapping.png)

    From then on, every new contact from the quiz carries the extra fields.

    ![how to activecampaign profile](/images/how_to_activecampaign_profile.png)


=== "Standalone"


    Once the quiz is connected, you can add the quiz data to each contact profile.

    Quiz data is added to the contact as **custom fields**, and quiz tags are added as native ActiveCampaign tags.

    !!! warning "Create the custom fields in ActiveCampaign first"

        ActiveCampaign does not create fields for you. Add each field in your ActiveCampaign dashboard first, or the sync has nowhere to write. The field's **Personalization Tag**, which is its unique key, must match the internal name in the field table. For an answer field, that is the slide hash ID.

    | Field | Value |
    | --- | --- |
    | `email` | The contact's primary identifier. |
    | `first_name`, `last_name`, `full_name` | The contact's name, as captured in the quiz. |
    | `phone_number` | All captured phone numbers, joined by `/`. |
    | `quiz_id` | The quiz Hash ID, for example `wnHR8G`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `products_ids` | Comma-separated list of the recommended product IDs. |
    | `[SLIDE_HASHID]` | One field per question, keyed by the slide's internal hash ID. The value is the text of the answer selected. |
    | `tags` | All [tags](/how-to-guides/use-customer-tags/) assigned, joined into a single field. |

    !!! info "Tags are also sent natively"
        Besides the `tags` custom field, quiz tags are pushed to ActiveCampaign's own tag system, so they appear as real tags on the contact profile. That makes them the easiest way to start an automation, using the `Tag Added` trigger.

    !!! info "Answer keys and date questions"
        Answer fields are keyed by the slide's internal hash ID, not by the question title, so renaming a question does not break your field mapping. Answers to date questions are sent in ISO8601 format.

    !!! warning "Products are sent as IDs only"
        The legacy integration sends recommended products as a list of IDs in `products_ids`, without titles, prices or images. If you need full product details, use [Zapier](/how-to-guides/send-leads-to-zapier/) or [Webhooks](/how-to-guides/send-leads-to-webhooks/) instead.

    To add these fields to a new profile:

    1. **In ActiveCampaign, go to `Lists > Manage fields` and click `Add Field`.**
        ![how to send leads to activecampaign new field1](/images/how_to_send_leads_to_activecampaign_new_field1.png)
    2. **Give each field a name.**
        ![how to send leads to activecampaign new field2](/images/how_to_send_leads_to_activecampaign_new_field2.png)
    3. **Find the new fields under `General Details`.** ActiveCampaign files them there.
        ![how to send leads to activecampaign new field3](/images/how_to_send_leads_to_activecampaign_new_field3.png)
    4. **Return to the `Product Recommendation Quiz` app in ActiveCampaign and map the new fields.** Every later contact from the quiz then carries this data.
        ![how to activecampaign mapping](/images/how_to_activecampaign_mapping.png)

    From then on, every new contact from the quiz carries the extra fields.

    ![how to activecampaign profile](/images/how_to_activecampaign_profile.png)


## Sending follow-up emails with ActiveCampaign

=== "Shopify"


    To send an automatic follow-up email after the quiz, set up an automation in ActiveCampaign:

    1. **In ActiveCampaign, open the `Automations` menu and create a new automation.**
    2. **Set a trigger on one of the custom fields your chosen route added to the contact profile.**
    3. **Design your email template.** To personalize it, add `custom properties` to your text blocks, such as a direct link to the quiz responses.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)


=== "Shopify (Legacy)"

    To send an automatic follow-up email after the quiz, set up an automation in ActiveCampaign:

    1. **In ActiveCampaign, open the `Automations` menu and create a new automation.**
    2. **Set the trigger by selecting your quiz under `Apps`.**
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. **Design your email template.** To personalize it, add `custom properties` to your text blocks, such as a direct link to the quiz responses.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "WooCommerce"


    To send an automatic follow-up email after the quiz, set up an automation in ActiveCampaign:

    1. **In ActiveCampaign, open the `Automations` menu and create a new automation.**
    2. **Set the trigger by selecting your quiz under `Apps`.**
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. **Design your email template.** To personalize it, add `custom properties` to your text blocks, such as a direct link to the quiz responses.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "Magento"


    To send an automatic follow-up email after the quiz, set up an automation in ActiveCampaign:

    1. **In ActiveCampaign, open the `Automations` menu and create a new automation.**
    2. **Set the trigger by selecting your quiz under `Apps`.**
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. **Design your email template.** To personalize it, add `custom properties` to your text blocks, such as a direct link to the quiz responses.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "BigCommerce"


    To send an automatic follow-up email after the quiz, set up an automation in ActiveCampaign:

    1. **In ActiveCampaign, open the `Automations` menu and create a new automation.**
    2. **Set the trigger by selecting your quiz under `Apps`.**
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. **Design your email template.** To personalize it, add `custom properties` to your text blocks, such as a direct link to the quiz responses.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

=== "Standalone"


    To send an automatic follow-up email after the quiz, set up an automation in ActiveCampaign:

    1. **In ActiveCampaign, open the `Automations` menu and create a new automation.**
    2. **Set the trigger by selecting your quiz under `Apps`.**
        ![how to activecampaign automation](/images/how_to_activecampaign_automation.gif)
    3. **Design your email template.** To personalize it, add `custom properties` to your text blocks, such as a direct link to the quiz responses.
        ![how to activecampaign add custom properties](/images/how_to_activecampaign_add_custom_properties.gif)

### Adding recommended products to emails

=== "Shopify"


    The route you chose decides what is available. The [Zapier](/how-to-guides/send-leads-to-zapier/#what-data-is-sent-to-zapier) and [Webhooks](/how-to-guides/send-leads-to-webhooks/#what-data-is-sent-to-webhook) payloads both carry each recommended product's `title`, `price`, `image` and `url`. Map those to ActiveCampaign contact fields, and the email can show real product details.

    ActiveCampaign's own product blocks are the other option. Connect ActiveCampaign to Shopify, and a product block displays products from a chosen collection. You can then show or hide each block based on the recommended product ID. This has not been tested thoroughly.


=== "Shopify (Legacy)"


    The only product information the app sends to ActiveCampaign is the recommended product IDs. That is not enough to display the full list of recommended products.

    To show any product in an ActiveCampaign email, first connect ActiveCampaign to Shopify. A product block can then display products from a chosen collection. You may be able to add several product blocks, and show or hide each one based on the recommended product ID. This has not been tested thoroughly.

=== "WooCommerce"


    The only product information the app sends to ActiveCampaign is the recommended product IDs. That is not enough to display the full list of recommended products.

    To show any product in an ActiveCampaign email, first connect ActiveCampaign to WooCommerce. A product block can then display products from a chosen collection. You may be able to add several product blocks, and show or hide each one based on the recommended product ID. This has not been tested thoroughly.

=== "Magento"


    The only product information the app sends to ActiveCampaign is the recommended product IDs. That is not enough to display the full list of recommended products.

    To show any product in an ActiveCampaign email, first connect ActiveCampaign to Magento. A product block can then display products from a chosen collection. You may be able to add several product blocks, and show or hide each one based on the recommended product ID. This has not been tested thoroughly.

=== "BigCommerce"


    The only product information the app sends to ActiveCampaign is the recommended product IDs. That is not enough to display the full list of recommended products.

    To show any product in an ActiveCampaign email, first connect ActiveCampaign to BigCommerce. A product block can then display products from a chosen collection. You may be able to add several product blocks, and show or hide each one based on the recommended product ID. This has not been tested thoroughly.

=== "Standalone"


    The only product information the app sends to ActiveCampaign is the recommended product IDs. That is not enough to display the full list of recommended products.

    To show any product in an ActiveCampaign email, first connect ActiveCampaign to your Google Product Catalog.



