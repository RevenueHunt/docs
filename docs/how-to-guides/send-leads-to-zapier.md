# How to Send Leads to Zapier

=== "Shopify"

    The `💎 Built for Shopify` version of the RevenueHunt app integrates directly with Zapier. 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Us6QCQpfFf0?si=mvOj4x8rnRRdiT0-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! info "Connecting the Quiz to Zapier allows you to:"

        - Connect the quiz to other apps (that RevenueHunt does not yet integrate with) and send quiz data to there automatically.
        - Send quiz leads to Zapier.
        - Send quiz leads to Google Sheets.
        - Send follow-up emails directly from Zapier.

    This guide explain how you can send quiz data to Zapier, what data is sent and how to set up a sample Zap using RevenueHunt as a trigger.

=== "Shopify (Legacy)"

    Automating the transfer of leads from your quizzes to your Customer Relationship Management (CRM) system or mailing list not only saves time but also allows for more targeted follow-up campaigns. 

    This guide will walk you through connecting your quiz to Zapier, a platform that enables integration with thousands of apps, including popular CRMs.

    !!! info "Connecting the Quiz to Zapier allows you to:"

        - Send quiz leads to Zapier.
        - Send follow-up emails directly from Zapier.
        - Connect the quiz to other apps (that RevenueHunt does not yet integrate with) and send quiz data to there automatically.

    Before beginning, ensure you have:

    - An active Zapier account.
    - Access to the quiz you wish to connect.
    - Access to your CRM or mailing list platform.

=== "WooCommerce"

    Automating the transfer of leads from your quizzes to your Customer Relationship Management (CRM) system or mailing list not only saves time but also allows for more targeted follow-up campaigns. 

    This guide will walk you through connecting your quiz to Zapier, a platform that enables integration with thousands of apps, including popular CRMs.

    !!! info "Connecting the Quiz to Zapier allows you to:"
    
        - Send quiz leads to Zapier.
        - Send follow-up emails directly from Zapier.
        - Connect the quiz to other apps (that RevenueHunt does not yet integrate with) and send quiz data to there automatically.

    Before beginning, ensure you have:

    - An active Zapier account.
    - Access to the quiz you wish to connect.
    - Access to your CRM or mailing list platform.

=== "Magento"

    Automating the transfer of leads from your quizzes to your Customer Relationship Management (CRM) system or mailing list not only saves time but also allows for more targeted follow-up campaigns. 

    This guide will walk you through connecting your quiz to Zapier, a platform that enables integration with thousands of apps, including popular CRMs.

    !!! info "Connecting the Quiz to Zapier allows you to:"
    
        - Send quiz leads to Zapier.
        - Send follow-up emails directly from Zapier.
        - Connect the quiz to other apps (that RevenueHunt does not yet integrate with) and send quiz data to there automatically.

    Before beginning, ensure you have:

    - An active Zapier account.
    - Access to the quiz you wish to connect.
    - Access to your CRM or mailing list platform.

=== "BigCommerce"

    Automating the transfer of leads from your quizzes to your Customer Relationship Management (CRM) system or mailing list not only saves time but also allows for more targeted follow-up campaigns. 

    This guide will walk you through connecting your quiz to Zapier, a platform that enables integration with thousands of apps, including popular CRMs.

    !!! info "Connecting the Quiz to Zapier allows you to:"
    
        - Send quiz leads to Zapier.
        - Send follow-up emails directly from Zapier.
        - Connect the quiz to other apps (that RevenueHunt does not yet integrate with) and send quiz data to there automatically.

    Before beginning, ensure you have:

    - An active Zapier account.
    - Access to the quiz you wish to connect.
    - Access to your CRM or mailing list platform.

=== "Standalone"

    Automating the transfer of leads from your quizzes to your Customer Relationship Management (CRM) system or mailing list not only saves time but also allows for more targeted follow-up campaigns. 

    This guide will walk you through connecting your quiz to Zapier, a platform that enables integration with thousands of apps, including popular CRMs.

    !!! info "Connecting the Quiz to Zapier allows you to:"
    
        - Send quiz leads to Zapier.
        - Send follow-up emails directly from Zapier.
        - Connect the quiz to other apps (that RevenueHunt does not yet integrate with) and send quiz data to there automatically.

    Before beginning, ensure you have:

    - An active Zapier account.
    - Access to the quiz you wish to connect.
    - Access to your CRM or mailing list platform.


## Link Quiz to Zapier

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Us6QCQpfFf0?si=mvOj4x8rnRRdiT0-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Prepare your quiz**: Before connecting to Zapier, you may want to add a `Name`, `Phone Number`, or `Email` question to your quiz in order to identify your leads. 

        - To do this, use the `+Add Question`or `+Add Block` options in the [Questions](/reference/quiz-builder/questions/) section of the Quiz Builder.
        - Once you’ve added your lead fields, click `Save` to save the changes.

    2. **Connecting to Zapier**: From the dashboard, navigate to [`quiz settings`](/reference/quiz-builder/quiz-settings/).

        - Go to the [`Integrations`](/reference/quiz-builder/connect-integrations/) section and find 'Zapier Integration'.
        - Click `Connect`to be directed to the Zapier login page.
        - Log in with your credentials.

    3. **Find RevenueHunt API Key**: On the authentication page, provide your Revenue Hunt API key. 

        ![how_to_shopifyv2_send_leads_to_zapier_provide_api_key](/images/how_to_shopifyv2_send_leads_to_zapier_provide_api_key.png)
    
        - Go back to the app and click `Copy Zapier API Key`. Copy the key to your clipboard.

        ![zapier api key](https://loom.com/i/4b7c034e3028417784d5cc5090caff21?workflows_screenshot=true)

    4. **Paste API Key**: Paste the key into the authentication page and select `Yes, Continue to Revenue Hunt 2.0.0`. If successful, you will be redirected back to the integrations page with Zapier connected to your quiz.
    5. **Test the connection**: `Preview` the quiz from the dashboard and complete it with sample information, including an email address. After reaching the results page, close the quiz.
    6. **Create a New Zap**: Log in to Zapier and click `+ Create Zap` to create a new Zap.

        - Select `RevnueHunt 2.0.0` as App.
        - Select `New Response` as the trigger event.
        - Select `RevnueHunt 2.0.0` as Account.
        - Click `Continue`.
        - Choose the quiz from which to receive responses (e.g., 'Skincare Quiz').

        ![how_to_shopifyv2_send_leads_to_zapier_create_new_zap](/images/how_to_shopifyv2_send_leads_to_zapier_create_new_zap.png)

    7. **Test the trigger**: Test the trigger to ensure data is sent correctly: 

        - Zapier will retrieve the latest quiz responses.
        - Verify that all relevant information (response ID, quiz ID, answers) is populated correctly.

        ![how_to_shopifyv2_send_leads_to_zapier_test_response](/images/how_to_shopifyv2_send_leads_to_zapier_test_response.png)

        !!! info "What data is sent to Zapier?"

            Check [this section](#what-data-is-sent-to-zapier) to see what data is sent to Zapier from your RevenueHunt quiz.

    8. **Set up what happends to Quiz Leads**: After confirming the integration is successful, you can decide how to use the data. Zapier offers plenty of integrations including:

        - Sending responses to a Google Sheet.
        - Filtering responses based on specific conditions.
        - Sending emails through Zapier'snative  email integration.
        
        !!! tip 
            Explore various options available in Zapier to utilize the quiz data effectively.

            ![zapier integrations](https://loom.com/i/116796e9e4aa4cba96bb555a3b890beb?workflows_screenshot=true)

        After you're done, make sure to **Publish** the zap.

    9. After successfully creating and publishing your Zap in Zapier, you can view the active Zaps connected to your quiz by following these steps:

        - Navigate to the app's [`Integrations`](/reference/quiz-builder/connect-integrations/) page.
        - Look for the section labeled 'Zapier'.
        - Here, you will find a list of all active Zaps associated with the quiz.

        ![how_to_shopifyv2_send_leads_to_zapier_active_zaps](/images/how_to_shopifyv2_send_leads_to_zapier_active_zaps.png)

=== "Shopify (Legacy)"

    How to connect the quiz to your CRM via Zapier
    It’s quite simple to set up:

    1. Head to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll-down to find Zapier and copy your `Zapier API Key`. You'll need this for the connection process.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. Within the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, click on the Zapier `Connect` button. 
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In the Zapier interface, search for "RevenueHunt" (or the quiz platform you're using) and select the version 1.1.1.
    7. Follow the on-screen instructions to continue building your Zap. This process will involve selecting the specific actions and triggers that match how you want your quiz data to be handled.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select Revenuehunt from the App list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New Connection Added** You should see a `New Connection Added` banner. Then you can use this connection to set up your email flow.

=== "WooCommerce"

    How to connect the quiz to your CRM via Zapier
    It’s quite simple to set up:

    1. Head to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll-down to find Zapier and copy your `Zapier API Key`. You'll need this for the connection process.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. Within the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, click on the Zapier `Connect` button. 
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In the Zapier interface, search for "RevenueHunt" (or the quiz platform you're using) and select the version 1.1.1.
    7. Follow the on-screen instructions to continue building your Zap. This process will involve selecting the specific actions and triggers that match how you want your quiz data to be handled.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select Revenuehunt from the App list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New Connection Added** You should see a `New Connection Added` banner. Then you can use this connection to set up your email flow.

=== "Magento"

    How to connect the quiz to your CRM via Zapier
    It’s quite simple to set up:

    1. Head to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll-down to find Zapier and copy your `Zapier API Key`. You'll need this for the connection process.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. Within the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, click on the Zapier `Connect` button. 
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In the Zapier interface, search for "RevenueHunt" (or the quiz platform you're using) and select the version 1.1.1.
    7. Follow the on-screen instructions to continue building your Zap. This process will involve selecting the specific actions and triggers that match how you want your quiz data to be handled.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select Revenuehunt from the App list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New Connection Added** You should see a `New Connection Added` banner. Then you can use this connection to set up your email flow.

=== "BigCommerce"

    How to connect the quiz to your CRM via Zapier
    It’s quite simple to set up:

    1. Head to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll-down to find Zapier and copy your `Zapier API Key`. You'll need this for the connection process.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. Within the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, click on the Zapier `Connect` button. 
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In the Zapier interface, search for "RevenueHunt" (or the quiz platform you're using) and select the version 1.1.1.
    7. Follow the on-screen instructions to continue building your Zap. This process will involve selecting the specific actions and triggers that match how you want your quiz data to be handled.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select Revenuehunt from the App list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New Connection Added** You should see a `New Connection Added` banner. Then you can use this connection to set up your email flow.

=== "Standalone"

    How to connect the quiz to your CRM via Zapier
    It’s quite simple to set up:

    1. Head to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll-down to find Zapier and copy your `Zapier API Key`. You'll need this for the connection process.
        ![how to send leads to zapier api key](/images/how_to_send_leads_to_zapier_api_key.png)

    3. Within the [Connect](/reference/quiz-builder/connect-integrations/) tab of your quiz, click on the Zapier `Connect` button. 
    4. On the prompt, select `Accept Invite & Build a Zap` to proceed to Zapier's website.
    5. Once redirected to Zapier, click on `Make a Zap`.
    6. In the Zapier interface, search for "RevenueHunt" (or the quiz platform you're using) and select the version 1.1.1.
    7. Follow the on-screen instructions to continue building your Zap. This process will involve selecting the specific actions and triggers that match how you want your quiz data to be handled.

    **OR**

    Set up the connection via Zapier:

    1. **Add Connection** Go to Zapier > Apps and click `+ Add Connection`.
    ![send leads to zapier connect1](/images/send_leads_to_zapier_connect1.png)
    2. Select Revenuehunt from the App list.
    ![send leads to zapier connect2](/images/send_leads_to_zapier_connect2.png)
    3. **Copy API Key** Copy your API Key from the Quiz Builder > Connect > Zapier tab:
    ![send leads to zapier connect3](/images/send_leads_to_zapier_connect3.png)
    And paste it in the window that pops up:
    ![send leads to zapier connect4](/images/send_leads_to_zapier_connect4.png)
    Confirm with `Yes, Continue to RevenueHunt`.
    4. **New Connection Added** You should see a `New Connection Added` banner. Then you can use this connection to set up your email flow.


## Alternative Ways to Send Quiz Leads to Zapier

=== "Shopify"

    Sometimes, you would like a bit more control over the data that is sent to Zapier. In that case there are a few alternatives you can use to send quiz leads to Zapier.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Zapier. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Zapier.
    - **Manually adding the quiz leads to Zapier**: You can manually add the quiz leads to Zapier by uploading a CSV file generated from the quiz [responses](/reference/quiz-builder/metrics/#responses) section.



=== "Shopify (Legacy)"

    Sometimes, you would like a bit more control over the data that is sent to Zapier. In that case there are a few alternatives you can use to send quiz leads to Zapier.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Zapier. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Zapier.
    - **Manually adding the quiz leads to Zapier**: You can manually add the quiz leads to Zapier by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.
    
=== "WooCommerce"

    Sometimes, you would like a bit more control over the data that is sent to Zapier. In that case there are a few alternatives you can use to send quiz leads to Zapier.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Zapier. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Zapier.
    - **Manually adding the quiz leads to Zapier**: You can manually add the quiz leads to Zapier by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.


=== "Magento"


    Sometimes, you would like a bit more control over the data that is sent to Zapier. In that case there are a few alternatives you can use to send quiz leads to Zapier.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Zapier. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Zapier.
    - **Manually adding the quiz leads to Zapier**: You can manually add the quiz leads to Zapier by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

=== "BigCommerce"


    Sometimes, you would like a bit more control over the data that is sent to Zapier. In that case there are a few alternatives you can use to send quiz leads to Zapier.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Zapier. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Zapier.
    - **Manually adding the quiz leads to Zapier**: You can manually add the quiz leads to Zapier by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

=== "Standalone"


    Sometimes, you would like a bit more control over the data that is sent to Zapier. In that case there are a few alternatives you can use to send quiz leads to Zapier.

    - **Using Webhooks**: You can use our Webhooks integration to send quiz leads to Zapier. Just connect your quiz to Webhooks following [this guide](/how-to-guides/send-leads-to-webhooks/). Then, in Webhooks set up a redirection of selected data to Zapier.
    - **Manually adding the quiz leads to Zapier**: You can manually add the quiz leads to Zapier by uploading a CSV file generated from the quiz [metrics > responses](/reference/quiz-builder/metrics/#responses) section.

## What Data is Sent to Zapier?

=== "Shopify"

    Once you've [Linked your quiz to Zapier](#link-quiz-to-zapier), your Zap will recevie the all the response information after each quiz completion. 

    ![how_to_shopifyv2_send_leads_to_zapier_test_response](/images/how_to_shopifyv2_send_leads_to_zapier_test_response.png)
    
    Each Zap trigger includes structured quiz response data, such as:

    | Category                | Example Fields                                                                      |
    | ----------------------- | ----------------------------------------------------------------------------------- |
    | **General Information** | `responseId`, `quizId`, `quizName`, `createdAt`                                     |
    | **User Information**    | `firstName`, `fullName`, `email`, `phone`                                           |
    | **Tags & Segments**     | Auto-generated tags like `30s`, `dry_skin`, `oily_skin`, etc.                       |
    | **Answers by Block**    | Includes each question, answer value, and reference IDs                             |
    | **Recommendations**     | Product recommendations per result slot                                             |
    | **Variable Scores**     | Numeric values used in advanced recommendation logic                                |
    | **Result Sections**     | Structured blocks from the quiz results page (text, heading, image, products, etc.) |


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

        If your quiz includes product recommendation logic, these are sent in the recommendationsBySlot field, grouped by result sections or slots:

        ```json
        "recommendationsBySlot": {
        "rsbs-520511f2": [
            "gid://shopify/Product/9634315436325",
            "gid://shopify/Product/9634314584357"
        ]
        }
        ```

    ??? example "Result Page Content"

        The quiz’s result page content is included in two sections:

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

    During the setup, you can check the quiz data that Zapier will receive from the quiz. This includes:

    - Email addresses of quiz participants.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

=== "WooCommerce"


    During the setup, you can check the quiz data that Zapier will receive from the quiz. This includes:

    - Email addresses of quiz participants.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

=== "Magento"


    During the setup, you can check the quiz data that Zapier will receive from the quiz. This includes:

    - Email addresses of quiz participants.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

=== "BigCommerce"


    During the setup, you can check the quiz data that Zapier will receive from the quiz. This includes:

    - Email addresses of quiz participants.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)

=== "Standalone"


    During the setup, you can check the quiz data that Zapier will receive from the quiz. This includes:

    - Email addresses of quiz participants.
    - Recommended products.
    - Responses to quiz questions.

    ![how to zapier data example2](/images/how_to_zapier_data_example2.png)

    After configuring the triggers, you can test the connection in Zapier's `Test trigger` section to ensure the correct data is being captured.

    ![how to zapier data example1](/images/how_to_zapier_data_example1.png)


## Sending Follow-up Emails Directly from Zapier

=== "Shopify"

    Once you have connected your quiz to Zapier you can build an email flow directly in Zapier to send customized follow-up emails right after the customer completes the quiz.

    ![how_to_shopifyv2_send_leads_to_zapier_example_flow](/images/how_to_shopifyv2_send_leads_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.


=== "Shopify (Legacy)"

    You can build an email flow directly in Zapier to send customized follow-up emails right after the customer completes the quiz.

    ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "WooCommerce"

    You can build an email flow directly in Zapier to send customized follow-up emails right after the customer completes the quiz.

    ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "Magento"

    You can build an email flow directly in Zapier to send customized follow-up emails right after the customer completes the quiz.

        ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "BigCommerce"

    You can build an email flow directly in Zapier to send customized follow-up emails right after the customer completes the quiz.
    
    ![how to zapier example flow](/images/how_to_zapier_example_flow.png)

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

=== "Standalone"

    You can build an email flow directly in Zapier to send customized follow-up emails right after the customer completes the quiz.

    !!! tip

        Check [this Zapier article](https://zapier.com/help/create/email-and-text-messages/send-emails-in-zaps) for more information.

---
This article explains how to send quiz leads to Zapier from the RevenueHunt app. 