---
description: "Step-by-step guide to connect RevenueHunt quiz to Zapier for integration with 5000+ apps."
icon: simple/zapier
---

# How to Send Leads to Zapier

Zapier connects to thousands of apps, including most CRMs and mailing lists. Send your quiz leads to Zapier, and Zapier passes them on to any service it supports.

This article explains how to connect your quiz to Zapier, what data is sent, and how to build a sample Zap.

=== "Shopify"

    The `💎 Built for Shopify` version of the RevenueHunt app integrates directly with Zapier.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Us6QCQpfFf0?si=mvOj4x8rnRRdiT0-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! info "What connecting the quiz to Zapier gives you"

        - Send quiz data to an app the RevenueHunt app does not integrate with directly.
        - Send quiz leads to Google Sheets.
        - Send follow-up emails directly from Zapier.


=== "Shopify (Legacy)"

    !!! info "What connecting the quiz to Zapier gives you"

        - Send quiz data to an app the RevenueHunt app does not integrate with directly.
        - Send follow-up emails directly from Zapier.

    !!! note "Before you start"

        You need:

        - An active Zapier account.
        - Access to the quiz you want to connect.
        - Access to your CRM or mailing list.

=== "WooCommerce"

    !!! info "What connecting the quiz to Zapier gives you"

        - Send quiz data to an app the RevenueHunt app does not integrate with directly.
        - Send follow-up emails directly from Zapier.

    !!! note "Before you start"

        You need:

        - An active Zapier account.
        - Access to the quiz you want to connect.
        - Access to your CRM or mailing list.

=== "Magento"

    !!! info "What connecting the quiz to Zapier gives you"

        - Send quiz data to an app the RevenueHunt app does not integrate with directly.
        - Send follow-up emails directly from Zapier.

    !!! note "Before you start"

        You need:

        - An active Zapier account.
        - Access to the quiz you want to connect.
        - Access to your CRM or mailing list.

=== "BigCommerce"

    !!! info "What connecting the quiz to Zapier gives you"

        - Send quiz data to an app the RevenueHunt app does not integrate with directly.
        - Send follow-up emails directly from Zapier.

    !!! note "Before you start"

        You need:

        - An active Zapier account.
        - Access to the quiz you want to connect.
        - Access to your CRM or mailing list.

=== "Standalone"

    !!! info "What connecting the quiz to Zapier gives you"

        - Send quiz data to an app the RevenueHunt app does not integrate with directly.
        - Send follow-up emails directly from Zapier.

    !!! note "Before you start"

        You need:

        - An active Zapier account.
        - Access to the quiz you want to connect.
        - Access to your CRM or mailing list.


## Link quiz to Zapier

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Us6QCQpfFf0?si=mvOj4x8rnRRdiT0-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Prepare your quiz**: add a `Name`, `Phone Number` or `Email` question, so you can identify each lead.

        - To do this, use the `+Add Question` or `+Add Block` options in the [Questions](/reference/quiz-builder/questions/) section of the Quiz builder.
        - Click `Save` when you have added them.

    2. **Connecting to Zapier**: From the dashboard, navigate to [`quiz settings`](/reference/quiz-builder/quiz-settings/).

        - Go to the [`Integrations`](/reference/quiz-builder/connect-integrations/) section and find `Zapier Integration`.
        - Click `Connect` to open the Zapier login page.
        - Log in with your credentials.

    3. **Find your RevenueHunt API key**: the authentication page asks for it.

        ![how_to_shopifyv2_send_leads_to_zapier_provide_api_key](/images/how_to_shopifyv2_send_leads_to_zapier_provide_api_key.png)

        - Go back to the app and click `Copy Zapier API Key`. Copy the key to your clipboard.

        ![zapier api key](https://loom.com/i/4b7c034e3028417784d5cc5090caff21?workflows_screenshot=true)

    4. **Paste the API key**: paste it into the authentication page and select `Yes, Continue to Revenue Hunt 2.0.0`. Zapier returns you to the integrations page, now connected.
    5. **Test the connection**: `Preview` the quiz and complete it with sample answers, including an email address. Close the quiz once you reach the results page.
    6. **Create a New Zap**: Log in to Zapier and click `+ Create Zap` to create a new Zap.

        - Select `RevenueHunt 2.0.0` as App.
        - Select `New Response` as the trigger event.
        - Select `RevenueHunt 2.0.0` as Account.
        - Click `Continue`.
        - Choose the quiz to receive responses from, for example `Skincare Quiz`.

        ![how_to_shopifyv2_send_leads_to_zapier_create_new_zap](/images/how_to_shopifyv2_send_leads_to_zapier_create_new_zap.png)

    7. **Test the trigger**: check that the data arrives correctly:

        - Zapier will retrieve the latest quiz responses.
        - Verify that all relevant information (response ID, quiz ID, answers) is populated correctly.

        ![how_to_shopifyv2_send_leads_to_zapier_test_response](/images/how_to_shopifyv2_send_leads_to_zapier_test_response.png)

        !!! info "What data is sent to Zapier?"

            Check [What data is sent to Zapier?](#what-data-is-sent-to-zapier) to see what data is sent to Zapier from your RevenueHunt quiz.

    8. **Decide what happens to the quiz leads**: with the integration working, choose what Zapier does with the data. It offers many integrations, including:

        - Sending responses to a Google Sheet.
        - Filtering responses based on specific conditions.
        - Sending emails through Zapier's own email integration.

        !!! tip
            Explore various options available in Zapier to utilize the quiz data effectively.

            ![zapier integrations](https://loom.com/i/116796e9e4aa4cba96bb555a3b890beb?workflows_screenshot=true)

        When you have finished, **Publish** the Zap.

    9. To see the active Zaps connected to your quiz:

        - Navigate to the app's [`Integrations`](/reference/quiz-builder/connect-integrations/) page.
        - Find the `Zapier` section.
        - Here, you will find a list of all active Zaps associated with the quiz.

        ![how_to_shopifyv2_send_leads_to_zapier_active_zaps](/images/how_to_shopifyv2_send_leads_to_zapier_active_zaps.png)

=== "Shopify (Legacy)"

    To connect the quiz to your CRM through Zapier:

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll down to Zapier and copy your `Zapier API Key`. You need it in a moment.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. In the [Connect](/reference/quiz-builder/connect-integrations/) tab, click the Zapier `Connect` button.
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In Zapier, search for `RevenueHunt` and select version 1.1.1.
    7. Follow the on-screen instructions to build your Zap. You choose the triggers and actions that suit what you want done with the quiz data.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select `RevenueHunt` from the app list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New connection added**: a `New Connection Added` banner appears. Use the connection to set up your email flow.

=== "WooCommerce"

    To connect the quiz to your CRM through Zapier:

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll down to Zapier and copy your `Zapier API Key`. You need it in a moment.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. In the [Connect](/reference/quiz-builder/connect-integrations/) tab, click the Zapier `Connect` button.
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In Zapier, search for `RevenueHunt` and select version 1.1.1.
    7. Follow the on-screen instructions to build your Zap. You choose the triggers and actions that suit what you want done with the quiz data.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select `RevenueHunt` from the app list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New connection added**: a `New Connection Added` banner appears. Use the connection to set up your email flow.

=== "Magento"

    To connect the quiz to your CRM through Zapier:

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll down to Zapier and copy your `Zapier API Key`. You need it in a moment.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. In the [Connect](/reference/quiz-builder/connect-integrations/) tab, click the Zapier `Connect` button.
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In Zapier, search for `RevenueHunt` and select version 1.1.1.
    7. Follow the on-screen instructions to build your Zap. You choose the triggers and actions that suit what you want done with the quiz data.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select `RevenueHunt` from the app list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New connection added**: a `New Connection Added` banner appears. Use the connection to set up your email flow.

=== "BigCommerce"

    To connect the quiz to your CRM through Zapier:

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll down to Zapier and copy your `Zapier API Key`. You need it in a moment.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. In the [Connect](/reference/quiz-builder/connect-integrations/) tab, click the Zapier `Connect` button.
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In Zapier, search for `RevenueHunt` and select version 1.1.1.
    7. Follow the on-screen instructions to build your Zap. You choose the triggers and actions that suit what you want done with the quiz data.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select `RevenueHunt` from the app list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New connection added**: a `New Connection Added` banner appears. Use the connection to set up your email flow.

=== "Standalone"

    To connect the quiz to your CRM through Zapier:

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll down to Zapier and copy your `Zapier API Key`. You need it in a moment.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. In the [Connect](/reference/quiz-builder/connect-integrations/) tab, click the Zapier `Connect` button.
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In Zapier, search for `RevenueHunt` and select version 1.1.1.
    7. Follow the on-screen instructions to build your Zap. You choose the triggers and actions that suit what you want done with the quiz data.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select `RevenueHunt` from the app list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New connection added**: a `New Connection Added` banner appears. Use the connection to set up your email flow.


## Alternative ways to send quiz leads to Zapier

=== "Shopify"

    To control exactly which data reaches Zapier, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [How to Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Zapier.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Zapier.



=== "Shopify (Legacy)"

    To control exactly which data reaches Zapier, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [How to Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Zapier.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Zapier.

=== "WooCommerce"

    To control exactly which data reaches Zapier, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [How to Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Zapier.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Zapier.


=== "Magento"


    To control exactly which data reaches Zapier, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [How to Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Zapier.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Zapier.

=== "BigCommerce"


    To control exactly which data reaches Zapier, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [How to Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Zapier.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Zapier.

=== "Standalone"


    To control exactly which data reaches Zapier, use one of these methods instead.

    - **Using Webhooks**: connect your quiz to Webhooks, as described in [How to Send Leads to Webhooks](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks, forward the data you want to Zapier.
    - **Uploading a CSV file**: export your quiz [responses](/reference/quiz-builder/metrics/#responses) as a CSV file and upload it to Zapier.

## What data is sent to Zapier?

=== "Shopify"

    Once you have [linked your quiz to Zapier](#link-quiz-to-zapier), your Zap receives the full response after every quiz completion.

    ![how_to_shopifyv2_send_leads_to_zapier_test_response](/images/how_to_shopifyv2_send_leads_to_zapier_test_response.png)

    Zapier receives a JSON object, the same payload the [Webhooks integration](/how-to-guides/send-leads-to-webhooks/) sends. Each trigger contains:

    | Field | Value |
    | --- | --- |
    | `responseId` | Unique ID of the response. |
    | `quizId` | Short ID of the quiz. |
    | `quizName` | The name of the quiz. |
    | `createdAt` | ISO8601 timestamp of the response. |
    | `marketId` | The market or locale ID. |
    | `firstName`, `lastName`, `fullName` | The customer's name. |
    | `email` | The customer's email address. |
    | `phone` | The customer's phone number. |
    | `answersByBlock` | Nested object keyed by block reference, each with the answer `value` and question `type`. |
    | `tags` | Array of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `variableScores` | All [variables](/how-to-guides/set-up-scoring-quiz/) and their final scores. |
    | `highestVariableRef` | Reference of the top-scoring variable. |
    | `resultRef` | Reference of the results page shown. |
    | `recommendationsBySlot` | The recommended items, organized by [slot](/reference/quiz-builder/results-page/) reference. |
    | `resultSections` | The results page sections that were visible to the customer. |
    | `resultContentByBlock` | The full content (text, images and slots) of each result block. |

    !!! info "Inside `recommendationsBySlot`"
        Each recommended item carries: `id`, `handle`, `title`, `description`, `price`, `image`, `onlineStoreUrl` and `vendor`.

    !!! tip "Map your Zap to block references"
        Answers are keyed by the block reference, such as `qbc-123`, not by the question title. You can therefore rename a question without breaking your Zap. Each reference sits under the `Advanced` tab of its block in the Quiz builder.


    ??? example "Example User Data"

        ```json
        "responseId": "DFaJbO",
        "quizId": "jGzry2",
        "quizName": "Skincare Quiz",
        "firstName": "Loretta",
        "email": "loretta@revenuehunt.com",
        "createdAt": "2025-10-14T06:38:21Z",
        "tags": ["30s", "dry_skin"]
        ```

    ??? example "Example Answer Structure"

        Each question block in the quiz is represented in the `answersByBlock` object, including the question type, value, and choices selected.

        ```json
        "answersByBlock": {
        "qbi-6c4248f5": {
            "type": "first_name",
            "value": "Loretta"
        },
        "qbc-e8cf3180": {
            "type": "multiple_choice",
            "value": [
            "Fine lines and wrinkles",
            "Hyperpigmentation and discoloration",
            "Enlarged pores"
            ]
        }
        }
        ```


    ??? example "Example Tags"

        Tags are automatically generated based on quiz logic or answers:

        ```json
        "tags": ["30s", "dry_skin"]
        ```

        You can use them to segment leads or filter automations in Zapier.

    ??? example "Product Recommendations"

        If your quiz includes product recommendation logic, these are sent in the `recommendationsBySlot` field, grouped by result sections or slots:

        ```json
        "recommendationsBySlot": {
        "rsbs-520511f2": [
            "gid://shopify/Product/9634315436325",
            "gid://shopify/Product/9634314584357"
        ]
        }
        ```

    ??? example "Results page Content"

        The quiz’s results page content is included in two sections:

        `resultSections` → Organized view of all result blocks (headings, text, products, etc.)

        `resultContentByBlock`→ Flattened key-value pairs for each block reference

        Example:

        ```json
        "recommendationsBySlot": {
        "rsbs-520511f2": [
            "gid://shopify/Product/9634315436325",
            "gid://shopify/Product/9634314584357"
        ]
        }
        ```


=== "Shopify (Legacy)"

    During setup you can check what Zapier receives:

    - The customer's email address.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

    **What the Payload Contains**

    The legacy payload is flat, and property names are not prefixed with the quiz ID. That makes it easy to reuse a Zap across quizzes that share the same structure.

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, or several joined by commas if the quiz collects more than one. |
    | `name` | The customer's full name. |
    | `phone` | The customer's phone number. |
    | `legal` | Any legal or consent text the customer accepted. |
    | `quiz_id` | The quiz Hash ID, for example `LVPS1n`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `created_at` | ISO8601 timestamp of the response. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `[SLIDE_TITLE]` | One property per question, keyed by the slide title. For example `What is your skin type?: Oily`. |
    | `[TAG_NAME]` | One property per [tag](/how-to-guides/use-customer-tags/) assigned, with a value of `true`. For example `Skin Type: Oily: true`. |
    | `tags` | Comma-separated list of all tags assigned. |
    | `products` | Comma-separated list of all recommended product titles. |
    | `product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `slot_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The same products grouped by [slot](/reference/quiz-builder/results-page/), when your results page uses them. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price`, `image_url` and `sku`. The slot-based properties carry `name`, `url`, `price` and `image_url`.

    !!! warning "Renaming a question breaks your Zap"
        Answer keys are built from the slide titles. Editing a question title in the Quiz Builder changes the key sent to Zapier, so you have to re-map that field in your Zap.

=== "WooCommerce"


    During setup you can check what Zapier receives:

    - The customer's email address.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

    **What the Payload Contains**

    The legacy payload is flat, and property names are not prefixed with the quiz ID. That makes it easy to reuse a Zap across quizzes that share the same structure.

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, or several joined by commas if the quiz collects more than one. |
    | `name` | The customer's full name. |
    | `phone` | The customer's phone number. |
    | `legal` | Any legal or consent text the customer accepted. |
    | `quiz_id` | The quiz Hash ID, for example `LVPS1n`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `created_at` | ISO8601 timestamp of the response. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `[SLIDE_TITLE]` | One property per question, keyed by the slide title. For example `What is your skin type?: Oily`. |
    | `[TAG_NAME]` | One property per [tag](/how-to-guides/use-customer-tags/) assigned, with a value of `true`. For example `Skin Type: Oily: true`. |
    | `tags` | Comma-separated list of all tags assigned. |
    | `products` | Comma-separated list of all recommended product titles. |
    | `product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `slot_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The same products grouped by [slot](/reference/quiz-builder/results-page/), when your results page uses them. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price`, `image_url` and `sku`. The slot-based properties carry `name`, `url`, `price` and `image_url`.

    !!! warning "Renaming a question breaks your Zap"
        Answer keys are built from the slide titles. Editing a question title in the Quiz Builder changes the key sent to Zapier, so you have to re-map that field in your Zap.

=== "Magento"


    During setup you can check what Zapier receives:

    - The customer's email address.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

    **What the Payload Contains**

    The legacy payload is flat, and property names are not prefixed with the quiz ID. That makes it easy to reuse a Zap across quizzes that share the same structure.

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, or several joined by commas if the quiz collects more than one. |
    | `name` | The customer's full name. |
    | `phone` | The customer's phone number. |
    | `legal` | Any legal or consent text the customer accepted. |
    | `quiz_id` | The quiz Hash ID, for example `LVPS1n`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `created_at` | ISO8601 timestamp of the response. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `[SLIDE_TITLE]` | One property per question, keyed by the slide title. For example `What is your skin type?: Oily`. |
    | `[TAG_NAME]` | One property per [tag](/how-to-guides/use-customer-tags/) assigned, with a value of `true`. For example `Skin Type: Oily: true`. |
    | `tags` | Comma-separated list of all tags assigned. |
    | `products` | Comma-separated list of all recommended product titles. |
    | `product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `slot_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The same products grouped by [slot](/reference/quiz-builder/results-page/), when your results page uses them. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price`, `image_url` and `sku`. The slot-based properties carry `name`, `url`, `price` and `image_url`.

    !!! warning "Renaming a question breaks your Zap"
        Answer keys are built from the slide titles. Editing a question title in the Quiz Builder changes the key sent to Zapier, so you have to re-map that field in your Zap.

=== "BigCommerce"


    During setup you can check what Zapier receives:

    - The customer's email address.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

    **What the Payload Contains**

    The legacy payload is flat, and property names are not prefixed with the quiz ID. That makes it easy to reuse a Zap across quizzes that share the same structure.

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, or several joined by commas if the quiz collects more than one. |
    | `name` | The customer's full name. |
    | `phone` | The customer's phone number. |
    | `legal` | Any legal or consent text the customer accepted. |
    | `quiz_id` | The quiz Hash ID, for example `LVPS1n`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `created_at` | ISO8601 timestamp of the response. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `[SLIDE_TITLE]` | One property per question, keyed by the slide title. For example `What is your skin type?: Oily`. |
    | `[TAG_NAME]` | One property per [tag](/how-to-guides/use-customer-tags/) assigned, with a value of `true`. For example `Skin Type: Oily: true`. |
    | `tags` | Comma-separated list of all tags assigned. |
    | `products` | Comma-separated list of all recommended product titles. |
    | `product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `slot_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The same products grouped by [slot](/reference/quiz-builder/results-page/), when your results page uses them. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price`, `image_url` and `sku`. The slot-based properties carry `name`, `url`, `price` and `image_url`.

    !!! warning "Renaming a question breaks your Zap"
        Answer keys are built from the slide titles. Editing a question title in the Quiz Builder changes the key sent to Zapier, so you have to re-map that field in your Zap.

=== "Standalone"


    During setup you can check what Zapier receives:

    - The customer's email address.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

    **What the Payload Contains**

    The legacy payload is flat, and property names are not prefixed with the quiz ID. That makes it easy to reuse a Zap across quizzes that share the same structure.

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, or several joined by commas if the quiz collects more than one. |
    | `name` | The customer's full name. |
    | `phone` | The customer's phone number. |
    | `legal` | Any legal or consent text the customer accepted. |
    | `quiz_id` | The quiz Hash ID, for example `LVPS1n`. |
    | `quiz_name` | The name of the quiz. |
    | `response_id` | Unique hash ID of this response. |
    | `permalink` | URL of the customer's results page. |
    | `permalink_hash` | The unique hash part of that URL. |
    | `created_at` | ISO8601 timestamp of the response. |
    | `result_page_name` | Name of the results page, for quizzes with multiple results. |
    | `[SLIDE_TITLE]` | One property per question, keyed by the slide title. For example `What is your skin type?: Oily`. |
    | `[TAG_NAME]` | One property per [tag](/how-to-guides/use-customer-tags/) assigned, with a value of `true`. For example `Skin Type: Oily: true`. |
    | `tags` | Comma-separated list of all tags assigned. |
    | `products` | Comma-separated list of all recommended product titles. |
    | `product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `slot_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The same products grouped by [slot](/reference/quiz-builder/results-page/), when your results page uses them. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price`, `image_url` and `sku`. The slot-based properties carry `name`, `url`, `price` and `image_url`.

    !!! warning "Renaming a question breaks your Zap"
        Answer keys are built from the slide titles. Editing a question title in the Quiz Builder changes the key sent to Zapier, so you have to re-map that field in your Zap.


??? info "Legacy vs Built for Shopify: payload format"

    | Feature | Legacy | Built for Shopify |
    | :--- | :--- | :--- |
    | Data format | Flattened key-value pairs | Nested, structured JSON |
    | Keys | Slide titles, for example `What is your skin type?` | Internal references, for example `qbc-123` |
    | Stability | Renaming a question breaks the Zap mapping | Renaming a question is safe |
    | Product data | Flattened numbered fields like `product_[INDEX]_name` | Full item objects inside `recommendationsBySlot` |

## Sending follow-up emails directly from Zapier

=== "Shopify"

    With the quiz connected, you can build an email flow in Zapier. It sends a follow-up email as soon as the customer finishes the quiz.

    ![how_to_shopifyv2_send_leads_to_zapier_example_flow](/images/how_to_shopifyv2_send_leads_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.


=== "Shopify (Legacy)"

    You can build an email flow in Zapier. It sends a follow-up email as soon as the customer finishes the quiz.

    ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "WooCommerce"

    You can build an email flow in Zapier. It sends a follow-up email as soon as the customer finishes the quiz.

    ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "Magento"

    You can build an email flow in Zapier. It sends a follow-up email as soon as the customer finishes the quiz.

        ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "BigCommerce"

    You can build an email flow in Zapier. It sends a follow-up email as soon as the customer finishes the quiz.

    ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "Standalone"

    You can build an email flow in Zapier. It sends a follow-up email as soon as the customer finishes the quiz.

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

---
This article explains how to send quiz leads to Zapier from the RevenueHunt app. 