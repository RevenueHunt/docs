---
description: "Learn how to connect RevenueHunt quiz to Omnisend for targeted email and SMS campaigns."
icon: material/cellphone-message
---

# How to Send Leads to Omnisend

=== "Shopify"

    Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=2rzG2V0Y8gio6CKx" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results to your mailing list.


=== "Shopify (Legacy)"


    Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

    This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results via email in Omnisend.


=== "WooCommerce"


    Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

    This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results to your mailing list.

=== "Magento"

    Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

    This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results to your mailing list.

=== "BigCommerce"


    Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

    This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results to your mailing list.


=== "Standalone"

    Apart from giving your customers a personalized product recommendation, you can connect Product Recommendation Quiz to your Omnisend account so that the quiz results are sent automatically to your mailing list. This way you can segment them based on their responses and follow up with targeted campaigns.

    This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results to your mailing list.



## Link Quiz to Omnisend

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=IIwZgRhppkbtGW_d&amp;start=37" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add an email question**: Ensure your quiz includes an [**email question**](/reference/quiz-builder/questions/#email), as this is essential for sending data to Omnisend. If an email question is missing, you can add one from the `+ Add Question` menu or insert an email block into an existing question.
    2. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). 

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key (e.g., 'Skincare Basic API Key for Quiz', 'RevenueHunt API Key', etc.) and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to **Settings** > **Integrations** and select the **Omnisend** tab. In the field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `Save`.

    4. **Preview your quiz**: After connecting to Omnisend, preview your quiz all the way to the results page to send the first contact. Use a sample email (e.g., 'alexa@example.com') and provide sample answers to populate properties in Omnisend.
    5. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (e.g., 'Alexa RevenueHunt / alexa@example.com') has been added. Click on the profile to view all custom properties from the quiz, including: 

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.


    Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_shopifyv2_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](#use-quiz-data-in-omnisend-email-templates).


=== "Shopify (Legacy)"

    1. **Add an email question**: Ensure your quiz includes an [**email question**](/reference/quiz-builder/questions/#email), as this is essential for sending data to Omnisend. If an email question is missing, you can add one from the `+ Add Question` menu or insert an email block into an existing question.
    2. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). 

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key (e.g., 'Skincare Basic API Key for Quiz', 'RevenueHunt API Key', etc.) and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. In the popup/field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection. 
    6. **Preview your quiz**: After connecting to Omnisend, preview your quiz all the way to the results page to send the first contact. Use a sample email (e.g., 'alexa@example.com') and provide sample answers to populate properties in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (e.g., 'Alexa RevenueHunt / alexa@example.com') has been added. Click on the profile to view all custom properties from the quiz, including: 

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](#use-quiz-data-in-omnisend-email-templates).

=== "WooCommerce"


    1. **Add an email question**: Ensure your quiz includes an [**email question**](/reference/quiz-builder/questions/#email), as this is essential for sending data to Omnisend. If an email question is missing, you can add one from the `+ Add Question` menu or insert an email block into an existing question.
    2. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). 

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key (e.g., 'Skincare Basic API Key for Quiz', 'RevenueHunt API Key', etc.) and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. In the popup/field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection. 
    6. **Preview your quiz**: After connecting to Omnisend, preview your quiz all the way to the results page to send the first contact. Use a sample email (e.g., 'alexa@example.com') and provide sample answers to populate properties in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (e.g., 'Alexa RevenueHunt / alexa@example.com') has been added. Click on the profile to view all custom properties from the quiz, including: 

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](#use-quiz-data-in-omnisend-email-templates).


=== "Magento"

    1. **Add an email question**: Ensure your quiz includes an [**email question**](/reference/quiz-builder/questions/#email), as this is essential for sending data to Omnisend. If an email question is missing, you can add one from the `+ Add Question` menu or insert an email block into an existing question.
    2. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). 

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key (e.g., 'Skincare Basic API Key for Quiz', 'RevenueHunt API Key', etc.) and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. In the popup/field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection. 
    6. **Preview your quiz**: After connecting to Omnisend, preview your quiz all the way to the results page to send the first contact. Use a sample email (e.g., 'alexa@example.com') and provide sample answers to populate properties in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (e.g., 'Alexa RevenueHunt / alexa@example.com') has been added. Click on the profile to view all custom properties from the quiz, including: 

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](#use-quiz-data-in-omnisend-email-templates).


=== "BigCommerce"


    1. **Add an email question**: Ensure your quiz includes an [**email question**](/reference/quiz-builder/questions/#email), as this is essential for sending data to Omnisend. If an email question is missing, you can add one from the `+ Add Question` menu or insert an email block into an existing question.
    2. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). 

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key (e.g., 'Skincare Basic API Key for Quiz', 'RevenueHunt API Key', etc.) and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. In the popup/field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection. 
    6. **Preview your quiz**: After connecting to Omnisend, preview your quiz all the way to the results page to send the first contact. Use a sample email (e.g., 'alexa@example.com') and provide sample answers to populate properties in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (e.g., 'Alexa RevenueHunt / alexa@example.com') has been added. Click on the profile to view all custom properties from the quiz, including: 

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](#use-quiz-data-in-omnisend-email-templates).


=== "Standalone"

    1. **Add an email question**: Ensure your quiz includes an [**email question**](/reference/quiz-builder/questions/#email), as this is essential for sending data to Omnisend. If an email question is missing, you can add one from the `+ Add Question` menu or insert an email block into an existing question.
    2. **Generate Omnisend API Key**: First, you'll have to [generate a new API Key in Omnisend](https://app.omnisend.com/integrations/api-keys). 

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key (e.g., 'Skincare Basic API Key for Quiz', 'RevenueHunt API Key', etc.) and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. In the popup/field that appears, you'll need to enter your `Omnisend API Key` into the input field, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection. 
    6. **Preview your quiz**: After connecting to Omnisend, preview your quiz all the way to the results page to send the first contact. Use a sample email (e.g., 'alexa@example.com') and provide sample answers to populate properties in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (e.g., 'Alexa RevenueHunt / alexa@example.com') has been added. Click on the profile to view all custom properties from the quiz, including: 

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    Following these steps ensures that every time a customer completes your quiz, their contact details, quiz responses, and product recommendations are automatically sent to your Omnisend account. 

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Omnisend profile. This information will appear in the customer’s profile as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](#use-quiz-data-in-omnisend-email-templates).

 
## Custom Properties Sent to Omnisend

Every completed response is sent to Omnisend as `custom properties` on the contact profile. Property names include your quiz ID, so two quizzes never overwrite each other's data on the same contact.

=== "Shopify"

    Property names use the quiz **Short ID** (`[SQID]`) and the internal **references** (`[REF]`) of your questions, choices, tags and slots.

    !!! info "Hyphens become underscores"
        Omnisend doesn't accept hyphens in property names, so every ID is converted. A block reference of `qbc-485600ce` appears in Omnisend as `qbc_485600ce`.

    | Property | Value |
    | --- | --- |
    | `quiz_[SQID]_response_id` | Unique ID of that quiz session. |
    | `quiz_[SQID]_quiz_name` | The name of the quiz. |
    | `quiz_[SQID]_result_ref` | Reference or URL of the results page shown. |
    | `quiz_[SQID]_market_id` | The market or locale ID, if you use multiple markets. |
    | `quiz_[SQID]_answer_[BLOCK_REF]` | The text of the answer given to that question. |
    | `quiz_[SQID]_choice_[CHOICE_REF]` | `true` for every choice selected. Best option for segmenting. |
    | `quiz_[SQID]_tag_[TAG_NAME]` | `true` for every [tag](/how-to-guides/use-customer-tags/) assigned. |
    | `quiz_[SQID]_variable_[VARIABLE_NAME]` | The numerical score of that [variable](/how-to-guides/set-up-scoring-quiz/). |
    | `quiz_[SQID]_highest_variable_ref` | Reference of the top-scoring variable. |
    | `quiz_[SQID]_products` | Comma-separated list of all recommended product titles. |
    | `quiz_[SQID]_products_count` | Total number of recommended products. |
    | `quiz_[SQID]_currency` | The store currency code, for example `USD`. |
    | `quiz_[SQID]_slot_[SLOT_REF]_heading` | Title of that [slot](/reference/quiz-builder/results-page/). |
    | `quiz_[SQID]_slot_[SLOT_REF]_description` | Description text of that slot. |
    | `quiz_[SQID]_slot_[SLOT_REF]_products` | Comma-separated product titles in that slot. |
    | `quiz_[SQID]_slot_[SLOT_REF]_count` | Number of products in that slot. |
    | `quiz_[SQID]_slot_[SLOT_REF]_[TYPE]_[INDEX]_[FIELD]` | The details of each recommended item, one property per field. |

    !!! info "Item `[FIELD]` values"
        `title`, `handle`, `id`, `price`, `url`, `image`, `vendor` and `currency`. `[TYPE]` is `product`, `variant` or `collection`, and `[INDEX]` starts at `0`.

    !!! info "Identifiers and consent"
        The email address is sent as an Omnisend identifier with `source: quiz-[SQID]` and a status of `subscribed` or `nonSubscribed`. A phone number, when provided, is sent as an identifier for SMS marketing. If the quiz block has Omnisend consent enabled, the status is set to `subscribed` along with a `statusDate`. See [How to Ask for Marketing Consent](/how-to-guides/ask-for-marketing-consent/).

=== "Shopify (Legacy)"

    Property names use the quiz **Hash ID** (`[ID]`), for example `LVPS1n`.

    | Property | Value |
    | --- | --- |
    | `firstName` | First name captured in the quiz. |
    | `lastName` | Last name captured in the quiz, when available. |
    | `tags` | Omnisend's standard tags field, populated with the quiz tags. |
    | `permalink_[ID]` | Link to the customer's results page. |
    | `permalink_hash_[ID]` | Unique hash of those results. |
    | `tags_[ID]` | Comma-separated string of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `result_page_name_[ID]` | Name of the results page, for quizzes with multiple results. |
    | `products_[ID]` | Comma-separated string of recommended product titles. Set to `NO RECOMMENDED PRODUCTS` when the quiz recommends nothing. |
    | `q_[ID]_[QUESTION_TITLE]` | The text of the selected answer. |
    | `t_[ID]_[TAG_NAME]` | `true` for every individual tag assigned. |
    | `slot_[ID]_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The recommended products, one property per field. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price` and `image_url`. `[INDEX]` starts at `0`.

    !!! info "Property names are sanitized"
        Omnisend has strict naming rules, so question titles, tag names and slot names are lowercased, underscored and sometimes truncated when they are turned into property names.

        - A question titled "What is your skin type?" becomes `q_lvps1n_what_is_your_skin_type: Oily`
        - A tag named "Skin type: oily" becomes `t_lvps1n_skin_type_oily: true`

    !!! info "Identifiers and consent"
        The email address, and the phone number when provided, are sent as Omnisend identifiers with a status of `subscribed` on submission.

=== "WooCommerce"

    Property names use the quiz **Hash ID** (`[ID]`), for example `LVPS1n`.

    | Property | Value |
    | --- | --- |
    | `firstName` | First name captured in the quiz. |
    | `lastName` | Last name captured in the quiz, when available. |
    | `tags` | Omnisend's standard tags field, populated with the quiz tags. |
    | `permalink_[ID]` | Link to the customer's results page. |
    | `permalink_hash_[ID]` | Unique hash of those results. |
    | `tags_[ID]` | Comma-separated string of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `result_page_name_[ID]` | Name of the results page, for quizzes with multiple results. |
    | `products_[ID]` | Comma-separated string of recommended product titles. Set to `NO RECOMMENDED PRODUCTS` when the quiz recommends nothing. |
    | `q_[ID]_[QUESTION_TITLE]` | The text of the selected answer. |
    | `t_[ID]_[TAG_NAME]` | `true` for every individual tag assigned. |
    | `slot_[ID]_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The recommended products, one property per field. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price` and `image_url`. `[INDEX]` starts at `0`.

    !!! info "Property names are sanitized"
        Omnisend has strict naming rules, so question titles, tag names and slot names are lowercased, underscored and sometimes truncated when they are turned into property names.

        - A question titled "What is your skin type?" becomes `q_lvps1n_what_is_your_skin_type: Oily`
        - A tag named "Skin type: oily" becomes `t_lvps1n_skin_type_oily: true`

    !!! info "Identifiers and consent"
        The email address, and the phone number when provided, are sent as Omnisend identifiers with a status of `subscribed` on submission.

=== "Magento"

    Property names use the quiz **Hash ID** (`[ID]`), for example `LVPS1n`.

    | Property | Value |
    | --- | --- |
    | `firstName` | First name captured in the quiz. |
    | `lastName` | Last name captured in the quiz, when available. |
    | `tags` | Omnisend's standard tags field, populated with the quiz tags. |
    | `permalink_[ID]` | Link to the customer's results page. |
    | `permalink_hash_[ID]` | Unique hash of those results. |
    | `tags_[ID]` | Comma-separated string of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `result_page_name_[ID]` | Name of the results page, for quizzes with multiple results. |
    | `products_[ID]` | Comma-separated string of recommended product titles. Set to `NO RECOMMENDED PRODUCTS` when the quiz recommends nothing. |
    | `q_[ID]_[QUESTION_TITLE]` | The text of the selected answer. |
    | `t_[ID]_[TAG_NAME]` | `true` for every individual tag assigned. |
    | `slot_[ID]_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The recommended products, one property per field. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price` and `image_url`. `[INDEX]` starts at `0`.

    !!! info "Property names are sanitized"
        Omnisend has strict naming rules, so question titles, tag names and slot names are lowercased, underscored and sometimes truncated when they are turned into property names.

        - A question titled "What is your skin type?" becomes `q_lvps1n_what_is_your_skin_type: Oily`
        - A tag named "Skin type: oily" becomes `t_lvps1n_skin_type_oily: true`

    !!! info "Identifiers and consent"
        The email address, and the phone number when provided, are sent as Omnisend identifiers with a status of `subscribed` on submission.

=== "BigCommerce"

    Property names use the quiz **Hash ID** (`[ID]`), for example `LVPS1n`.

    | Property | Value |
    | --- | --- |
    | `firstName` | First name captured in the quiz. |
    | `lastName` | Last name captured in the quiz, when available. |
    | `tags` | Omnisend's standard tags field, populated with the quiz tags. |
    | `permalink_[ID]` | Link to the customer's results page. |
    | `permalink_hash_[ID]` | Unique hash of those results. |
    | `tags_[ID]` | Comma-separated string of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `result_page_name_[ID]` | Name of the results page, for quizzes with multiple results. |
    | `products_[ID]` | Comma-separated string of recommended product titles. Set to `NO RECOMMENDED PRODUCTS` when the quiz recommends nothing. |
    | `q_[ID]_[QUESTION_TITLE]` | The text of the selected answer. |
    | `t_[ID]_[TAG_NAME]` | `true` for every individual tag assigned. |
    | `slot_[ID]_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The recommended products, one property per field. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price` and `image_url`. `[INDEX]` starts at `0`.

    !!! info "Property names are sanitized"
        Omnisend has strict naming rules, so question titles, tag names and slot names are lowercased, underscored and sometimes truncated when they are turned into property names.

        - A question titled "What is your skin type?" becomes `q_lvps1n_what_is_your_skin_type: Oily`
        - A tag named "Skin type: oily" becomes `t_lvps1n_skin_type_oily: true`

    !!! info "Identifiers and consent"
        The email address, and the phone number when provided, are sent as Omnisend identifiers with a status of `subscribed` on submission.

=== "Standalone"

    Property names use the quiz **Hash ID** (`[ID]`), for example `LVPS1n`.

    | Property | Value |
    | --- | --- |
    | `firstName` | First name captured in the quiz. |
    | `lastName` | Last name captured in the quiz, when available. |
    | `tags` | Omnisend's standard tags field, populated with the quiz tags. |
    | `permalink_[ID]` | Link to the customer's results page. |
    | `permalink_hash_[ID]` | Unique hash of those results. |
    | `tags_[ID]` | Comma-separated string of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `result_page_name_[ID]` | Name of the results page, for quizzes with multiple results. |
    | `products_[ID]` | Comma-separated string of recommended product titles. Set to `NO RECOMMENDED PRODUCTS` when the quiz recommends nothing. |
    | `q_[ID]_[QUESTION_TITLE]` | The text of the selected answer. |
    | `t_[ID]_[TAG_NAME]` | `true` for every individual tag assigned. |
    | `slot_[ID]_[SLOT_NAME]_product_[INDEX]_[FIELD]` | The recommended products, one property per field. |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `price` and `image_url`. `[INDEX]` starts at `0`.

    !!! info "Property names are sanitized"
        Omnisend has strict naming rules, so question titles, tag names and slot names are lowercased, underscored and sometimes truncated when they are turned into property names.

        - A question titled "What is your skin type?" becomes `q_lvps1n_what_is_your_skin_type: Oily`
        - A tag named "Skin type: oily" becomes `t_lvps1n_skin_type_oily: true`

    !!! info "Identifiers and consent"
        The email address, and the phone number when provided, are sent as Omnisend identifiers with a status of `subscribed` on submission.

!!! tip "Can't find a property in Omnisend?"

    Omnisend only lists properties it has already received, so take a test quiz first and try again.

    In the Built for Shopify version, property names contain the reference of the block, choice or tag rather than its title, which you'll find in the Quiz Builder under the `Advanced` tab of that block or choice. Renaming a question therefore doesn't break your Omnisend setup. In the legacy versions the opposite is true: property names are built from the question title, so renaming a question creates a new property.

??? info "Legacy vs Built for Shopify: property naming"

    If you migrated from the legacy app, your Omnisend segments and email templates need updating because the property names changed.

    | Data | Legacy | Built for Shopify |
    | :--- | :--- | :--- |
    | Key format | `[PROPERTY]_[ID]` | `quiz_[SQID]_[PROPERTY]` |
    | Answers | `q_[ID]_[QUESTION_TITLE]`, built from the sanitized question title | `quiz_[SQID]_answer_[BLOCK_REF]`, built from the block reference |
    | Variables | Not sent | `quiz_[SQID]_variable_[NAME]` and `quiz_[SQID]_highest_variable_ref` |
    | Products | Title, URL, price and image only | Adds slot headings and descriptions, currency, vendor, handle and item IDs |
    | Consent | Defaults to `subscribed` on submission | Follows the Omnisend consent setting on the quiz block |

## Send Follow-up Emails with Omnisend

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=zJTtTF4AcwpfJ18y&amp;start=135" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    It’s possible to set up a post-quiz email campaign in Omnisend to send the product recommendations or other offers to the quiz participants. 
    
    Below you’ll find some basic instructions that you can follow to set up an email flow in Omnisend. It covers creating a segment for quiz takers, setting up an automation workflow, and customizing email content with quiz results.

    !!! warning

        Email templates and flows are not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend.

        Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a Segment for Quiz Participants**: In Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `quiz_QUIZID_quiz_name`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Use the custom properties to create a segment for users who took the quiz. Select a property (e.g., `quiz_QUIZID_quiz_name`) and copy it.
        - Go to 'Audience' > 'Segments' and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, e.g., 'Skincare Quiz Basic Segment' and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set Up an Automated Workflow**: Develop an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Navigate to the 'Automation' section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select 'When someone enters the segment' and choose the segment you created, e.g., 'Skincare Quiz Basic Segment'.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject (e.g., 'Your Quiz Results') and add a subheader.
        - Edit the email content as needed, then save changes to access the email editor.

    5. **Include Quiz Results in the Email**: To include quiz results in the email, add an HTML element to the email builder.

        - In the quiz builder, navigate to 'Settings' > 'Integrations' and generate an Omnisend email template.

            ![how to omnisend email template](/images/how_to_shopifyv2_omnisend_template.png){:width="500px"}
        - Copy the generated code and paste it into the HTML block of your email template in Omnisend.

            ![how to omnisend email template](/images/how_to_shopifyv2_omnisend_template_copy.png)
        - This code will create a pre-formatted email with quiz results and recommended products, which can be further edited as needed.

        !!! warning "Omnisend email template"
            Some users have reported that the generated email template is not working as expected. If you are experiencing this issue, please [contact support](/how-to-guides/contact-support/).

    6. **Preview and test the email**: Preview and test the email as one of the segment subscribers. Complete any additional follow-up steps in the workflow.
    7. **Save all changes and start the workflow**: Save all changes and start the workflow to activate the automation for quiz takers.



=== "Shopify (Legacy)"   

    It’s possible to set up a post-quiz email campaign in Omnisend to send the product recommendations or other offers to the quiz participants. 
    
    Below you’ll find some basic instructions that you can follow to set up an email flow in Omnisend. It covers creating a segment for quiz takers, setting up an automation workflow, and customizing email content with quiz results.

    !!! warning

        Email templates and flows are not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend.

        Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a Segment for Quiz Participants**: In Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Use the custom properties to create a segment for users who took the quiz. Select a property (e.g., `permalink_quiz_id`) and copy it.
        - Go to 'Audience' > 'Segments' and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, e.g., 'Skincare Quiz Basic Segment' and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set Up an Automated Workflow**: Develop an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Navigate to the 'Automation' section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select 'When someone enters the segment' and choose the segment you created, e.g., 'Skincare Quiz Basic Segment'.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject (e.g., 'Your Quiz Results') and add a subheader.
        - Edit the email content as needed, then save changes to access the email editor.

    5. To get you started, you can use the [Sample Quiz Results Email Templates](#email-templates) we provide or [use the custom properties](#use-quiz-data-in-omnisend-email-templates) we sent to your Omnisend account to build your own email template.
    6. **Preview and test the email**: Preview and test the email as one of the segment subscribers. Complete any additional follow-up steps in the workflow.
    7. **Save all changes and start the workflow**: Save all changes and start the workflow to activate the automation for quiz takers.


=== "WooCommerce" 


    It’s possible to set up a post-quiz email campaign in Omnisend to send the product recommendations or other offers to the quiz participants. 
    
    Below you’ll find some basic instructions that you can follow to set up an email flow in Omnisend. It covers creating a segment for quiz takers, setting up an automation workflow, and customizing email content with quiz results.

    !!! warning

        Email templates and flows are not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend.

        Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a Segment for Quiz Participants**: In Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Use the custom properties to create a segment for users who took the quiz. Select a property (e.g., `permalink_quiz_id`) and copy it.
        - Go to 'Audience' > 'Segments' and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, e.g., 'Skincare Quiz Basic Segment' and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set Up an Automated Workflow**: Develop an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Navigate to the 'Automation' section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select 'When someone enters the segment' and choose the segment you created, e.g., 'Skincare Quiz Basic Segment'.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject (e.g., 'Your Quiz Results') and add a subheader.
        - Edit the email content as needed, then save changes to access the email editor.

    5. To get you started, you can use the [Sample Quiz Results Email Templates](#email-templates) we provide or [use the custom properties](#use-quiz-data-in-omnisend-email-templates) we sent to your Omnisend account to build your own email template.
    6. **Preview and test the email**: Preview and test the email as one of the segment subscribers. Complete any additional follow-up steps in the workflow.
    7. **Save all changes and start the workflow**: Save all changes and start the workflow to activate the automation for quiz takers.


=== "Magento" 



    It’s possible to set up a post-quiz email campaign in Omnisend to send the product recommendations or other offers to the quiz participants. 
    
    Below you’ll find some basic instructions that you can follow to set up an email flow in Omnisend. It covers creating a segment for quiz takers, setting up an automation workflow, and customizing email content with quiz results.

    !!! warning

        Email templates and flows are not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend.

        Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a Segment for Quiz Participants**: In Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Use the custom properties to create a segment for users who took the quiz. Select a property (e.g., `permalink_quiz_id`) and copy it.
        - Go to 'Audience' > 'Segments' and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, e.g., 'Skincare Quiz Basic Segment' and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set Up an Automated Workflow**: Develop an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Navigate to the 'Automation' section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select 'When someone enters the segment' and choose the segment you created, e.g., 'Skincare Quiz Basic Segment'.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject (e.g., 'Your Quiz Results') and add a subheader.
        - Edit the email content as needed, then save changes to access the email editor.

    5. To get you started, you can use the [Sample Quiz Results Email Templates](#email-templates) we provide or [use the custom properties](#use-quiz-data-in-omnisend-email-templates) we sent to your Omnisend account to build your own email template.
    6. **Preview and test the email**: Preview and test the email as one of the segment subscribers. Complete any additional follow-up steps in the workflow.
    7. **Save all changes and start the workflow**: Save all changes and start the workflow to activate the automation for quiz takers.


=== "BigCommerce"


    It’s possible to set up a post-quiz email campaign in Omnisend to send the product recommendations or other offers to the quiz participants. 
    
    Below you’ll find some basic instructions that you can follow to set up an email flow in Omnisend. It covers creating a segment for quiz takers, setting up an automation workflow, and customizing email content with quiz results.

    !!! warning

        Email templates and flows are not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend.

        Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a Segment for Quiz Participants**: In Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Use the custom properties to create a segment for users who took the quiz. Select a property (e.g., `permalink_quiz_id`) and copy it.
        - Go to 'Audience' > 'Segments' and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, e.g., 'Skincare Quiz Basic Segment' and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set Up an Automated Workflow**: Develop an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Navigate to the 'Automation' section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select 'When someone enters the segment' and choose the segment you created, e.g., 'Skincare Quiz Basic Segment'.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject (e.g., 'Your Quiz Results') and add a subheader.
        - Edit the email content as needed, then save changes to access the email editor.

    5. To get you started, you can use the [Sample Quiz Results Email Templates](#email-templates) we provide or [use the custom properties](#use-quiz-data-in-omnisend-email-templates) we sent to your Omnisend account to build your own email template.
    6. **Preview and test the email**: Preview and test the email as one of the segment subscribers. Complete any additional follow-up steps in the workflow.
    7. **Save all changes and start the workflow**: Save all changes and start the workflow to activate the automation for quiz takers.



=== "Standalone" 


    It’s possible to set up a post-quiz email campaign in Omnisend to send the product recommendations or other offers to the quiz participants. 
    
    Below you’ll find some basic instructions that you can follow to set up an email flow in Omnisend. It covers creating a segment for quiz takers, setting up an automation workflow, and customizing email content with quiz results.

    !!! warning

        Email templates and flows are not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Omnisend.

        Once the quiz is connected to Omnisend (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Omnisend.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a Segment for Quiz Participants**: In Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) specifically for users who have completed the quiz. This can be done by filtering for a `custom property` that only quiz participants will have, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Use the custom properties to create a segment for users who took the quiz. Select a property (e.g., `permalink_quiz_id`) and copy it.
        - Go to 'Audience' > 'Segments' and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, e.g., 'Skincare Quiz Basic Segment' and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set Up an Automated Workflow**: Develop an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) in Omnisend that triggers when someone is added to the newly created segment of quiz participants. This step involves configuring Omnisend to automatically start the email campaign sequence for users in this segment.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Navigate to the 'Automation' section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select 'When someone enters the segment' and choose the segment you created, e.g., 'Skincare Quiz Basic Segment'.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject (e.g., 'Your Quiz Results') and add a subheader.
        - Edit the email content as needed, then save changes to access the email editor.

    5. To get you started, you can use the [Sample Quiz Results Email Templates](#email-templates) we provide or [use the custom properties](#use-quiz-data-in-omnisend-email-templates) we sent to your Omnisend account to build your own email template.
    6. **Preview and test the email**: Preview and test the email as one of the segment subscribers. Complete any additional follow-up steps in the workflow.
    7. **Save all changes and start the workflow**: Save all changes and start the workflow to activate the automation for quiz takers.



## Use Quiz Data In Omnisend Email Templates

See [Custom Properties Sent to Omnisend](#custom-properties-sent-to-omnisend) for the full list of properties you can pull into a template.

=== "Shopify"

    You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

    ![how to omnisend custom properties](/images/how_to_shopifyv2_omnisend_custom_properties.gif)

    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).


=== "Shopify (Legacy)"


    You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "WooCommerce"

    You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "Magento"

    You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "BigCommerce"

    You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "Standalone"

    You can use the quiz data in your Omnisend email templates by using the `custom properties` that are passed from the quiz to your Omnisend account.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

### Pull Customer Answers into an Email Template

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=PsgLwM2IkSiXHkUV&amp;start=300" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can pull the customer answers into an email template by using the `custom properties` that are passed from the quiz to your Omnisend account. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.    
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text. 

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Use the preview feature to test the template with a specific profile (e.g., Alexa Revenue Hunt). Confirm that the custom property is correctly displayed in the email content, reflecting the user's quiz response.
    9. Save the email template.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can pull the customer answers into an email template by using the `custom properties` that are passed from the quiz to your Omnisend account. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.    
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text. 

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Use the preview feature to test the template with a specific profile (e.g., Alexa Revenue Hunt). Confirm that the custom property is correctly displayed in the email content, reflecting the user's quiz response.
    9. Save the email template.


=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can pull the customer answers into an email template by using the `custom properties` that are passed from the quiz to your Omnisend account. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.    
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text. 

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Use the preview feature to test the template with a specific profile (e.g., Alexa Revenue Hunt). Confirm that the custom property is correctly displayed in the email content, reflecting the user's quiz response.
    9. Save the email template.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can pull the customer answers into an email template by using the `custom properties` that are passed from the quiz to your Omnisend account. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.    
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text. 

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Use the preview feature to test the template with a specific profile (e.g., Alexa Revenue Hunt). Confirm that the custom property is correctly displayed in the email content, reflecting the user's quiz response.
    9. Save the email template.


=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can pull the customer answers into an email template by using the `custom properties` that are passed from the quiz to your Omnisend account. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.    
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text. 

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Use the preview feature to test the template with a specific profile (e.g., Alexa Revenue Hunt). Confirm that the custom property is correctly displayed in the email content, reflecting the user's quiz response.
    9. Save the email template.


=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can pull the customer answers into an email template by using the `custom properties` that are passed from the quiz to your Omnisend account. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.    
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text. 

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Use the preview feature to test the template with a specific profile (e.g., Alexa Revenue Hunt). Confirm that the custom property is correctly displayed in the email content, reflecting the user's quiz response.
    9. Save the email template.



### Display a Link to the Quiz Results in an email


=== "Shopify"

    Use the `quiz_QUIZID_response_id` to create a link to the quiz results page. Just add `#response-{{ person|lookup:'quiz_QUIZID_response_id' }}` to the end of your results page href attribute in any link or URL. 


    !!! example

        `<a href="https://yourwebsite.com/#response-{{ contact.custom.quiz_lBJ9bk_response_id }}">View your quiz results</a>` 

        where `lBJ9bk` is the quiz ID and

        - `{{ contact.custom.quiz_lBJ9bk_response_id }}` fetches the dynamic response ID (e.g., eVgV0Y).


=== "Shopify (Legacy)"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`


=== "WooCommerce"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "Magento"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "BigCommerce"   

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "Standalone"

    Use the `permalink_koHP8VA` in your email template. This property already contains a full url to the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`




### Customer Tags in Omnisend

Note that while customer profiles are updated with new quiz takes—including answers and product recommendations—Omnisend does not automatically remove unselected tags from previous sessions. A `tags_quizID` property is used to track the latest customer tags, which can be utilized to create segmented audiences for targeted marketing efforts.



### Email Templates

=== "Shopify"

    In the [Integrations](/reference/quiz-builder/connect-integrations/) section, under `Omnisend`, you can find the `omnisend template`. 
    
    ![how to shopifyv2 omnisend template](/images/how_to_shopifyv2_omnisend_template.png)
    
    Click on the button to receive and copy an HTML email template specifically tailored for the quiz.
    
    ![how to shopifyv2 omnisend template copy](/images/how_to_shopifyv2_omnisend_template_copy.png)

    You can use this template as a reference to create your own.

    !!! warning "Omnisend email template"
        Some users have reported that the generated email template is not working as expected. If you are experiencing this issue, please [contact support](/how-to-guides/contact-support/).


=== "Shopify (Legacy)"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

=== "WooCommerce"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

=== "Magento"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.     


=== "BigCommerce"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.

=== "Standalone"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    Bear in mind that the templates won’t work by just copy/pasting. These templates were created for our demo quiz. Your developer will have to modify the `custom properties` in these templates to match the ones that are passed from the quiz to your Omnisend account. The `quiz ID` is different, so are other property names. After the changes are made, your developer can insert the code as a `custom HTML block` on the Omnisend email template.


---
This article explains how to connect your quiz to Omnisend, create a segment for quiz participants and how to send the quiz results via email in Omnisend. 
