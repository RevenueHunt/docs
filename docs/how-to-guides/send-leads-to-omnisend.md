---
description: "Learn how to connect RevenueHunt quiz to Omnisend for targeted email and SMS campaigns."
icon: material/cellphone-message
---

# How to Send Leads to Omnisend

=== "Shopify"

    Connect your quiz to Omnisend and every quiz result is sent to your mailing list. You can then segment those contacts on their answers, and follow up with a campaign for each group.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=2rzG2V0Y8gio6CKx" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and send them their quiz results.


=== "Shopify (Legacy)"


    Connect your quiz to Omnisend and every quiz result is sent to your mailing list. You can then segment those contacts on their answers, and follow up with a campaign for each group.

    This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and email them their quiz results.


=== "WooCommerce"


    Connect your quiz to Omnisend and every quiz result is sent to your mailing list. You can then segment those contacts on their answers, and follow up with a campaign for each group.

    This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and send them their quiz results.

=== "Magento"

    Connect your quiz to Omnisend and every quiz result is sent to your mailing list. You can then segment those contacts on their answers, and follow up with a campaign for each group.

    This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and send them their quiz results.

=== "BigCommerce"


    Connect your quiz to Omnisend and every quiz result is sent to your mailing list. You can then segment those contacts on their answers, and follow up with a campaign for each group.

    This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and send them their quiz results.


=== "Standalone"

    Connect your quiz to Omnisend and every quiz result is sent to your mailing list. You can then segment those contacts on their answers, and follow up with a campaign for each group.

    This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and send them their quiz results.



## Link quiz to Omnisend

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=IIwZgRhppkbtGW_d&amp;start=37" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add an email question**: your quiz needs an [**email question**](/reference/quiz-builder/questions/#email-address) before it can send anything to Omnisend. Add one from the `+ Add Question` menu, or insert an email block into an existing question.
    2. **Generate an Omnisend API Key**: [generate a new API key in Omnisend](https://app.omnisend.com/integrations/api-keys).

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key for example `RevenueHunt API Key` and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: open the [Quiz builder](/reference/quiz-builder/), go to **Settings** > **Integrations** and select the **Omnisend** tab. Paste your `Omnisend API Key` into the field, then click `Save`.

    4. **Preview your quiz**: preview it all the way to the results page, to send the first contact. Use a sample email such as `alexa@example.com`, and give sample answers so the properties arrive in Omnisend.
    5. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (for example `Alexa RevenueHunt / alexa@example.com`) has been added. Click on the profile to view all custom properties from the quiz, including:

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.


    From now on, whenever a customer finishes your quiz, their contact details, answers and product recommendations are sent to your Omnisend account.

    The app sends every answer, every recommended product and the contact details to the customer’s Omnisend profile, where they appear as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_shopifyv2_omnisend_custom_properties.gif)


    To add anything else to the email template, your developer [pulls the matching custom properties off the profile](#use-quiz-data-in-omnisend-email-templates).


=== "Shopify (Legacy)"

    1. **Add an email question**: your quiz needs an [**email question**](/reference/quiz-builder/questions/#email-address) before it can send anything to Omnisend. Add one from the `+ Add Question` menu, or insert an email block into an existing question.
    2. **Generate an Omnisend API Key**: [generate a new API key in Omnisend](https://app.omnisend.com/integrations/api-keys).

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key for example `RevenueHunt API Key` and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. Paste your `Omnisend API Key` into the field that appears, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection.
    6. **Preview your quiz**: preview it all the way to the results page, to send the first contact. Use a sample email such as `alexa@example.com`, and give sample answers so the properties arrive in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (for example `Alexa RevenueHunt / alexa@example.com`) has been added. Click on the profile to view all custom properties from the quiz, including:

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    From now on, whenever a customer finishes your quiz, their contact details, answers and product recommendations are sent to your Omnisend account.

    The app sends every answer, every recommended product and the contact details to the customer’s Omnisend profile, where they appear as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    To add anything else to the email template, your developer [pulls the matching custom properties off the profile](#use-quiz-data-in-omnisend-email-templates).

=== "WooCommerce"


    1. **Add an email question**: your quiz needs an [**email question**](/reference/quiz-builder/questions/#email-address) before it can send anything to Omnisend. Add one from the `+ Add Question` menu, or insert an email block into an existing question.
    2. **Generate an Omnisend API Key**: [generate a new API key in Omnisend](https://app.omnisend.com/integrations/api-keys).

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key for example `RevenueHunt API Key` and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. Paste your `Omnisend API Key` into the field that appears, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection.
    6. **Preview your quiz**: preview it all the way to the results page, to send the first contact. Use a sample email such as `alexa@example.com`, and give sample answers so the properties arrive in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (for example `Alexa RevenueHunt / alexa@example.com`) has been added. Click on the profile to view all custom properties from the quiz, including:

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    From now on, whenever a customer finishes your quiz, their contact details, answers and product recommendations are sent to your Omnisend account.

    The app sends every answer, every recommended product and the contact details to the customer’s Omnisend profile, where they appear as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    To add anything else to the email template, your developer [pulls the matching custom properties off the profile](#use-quiz-data-in-omnisend-email-templates).


=== "Magento"

    1. **Add an email question**: your quiz needs an [**email question**](/reference/quiz-builder/questions/#email-address) before it can send anything to Omnisend. Add one from the `+ Add Question` menu, or insert an email block into an existing question.
    2. **Generate an Omnisend API Key**: [generate a new API key in Omnisend](https://app.omnisend.com/integrations/api-keys).

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key for example `RevenueHunt API Key` and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. Paste your `Omnisend API Key` into the field that appears, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection.
    6. **Preview your quiz**: preview it all the way to the results page, to send the first contact. Use a sample email such as `alexa@example.com`, and give sample answers so the properties arrive in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (for example `Alexa RevenueHunt / alexa@example.com`) has been added. Click on the profile to view all custom properties from the quiz, including:

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    From now on, whenever a customer finishes your quiz, their contact details, answers and product recommendations are sent to your Omnisend account.

    The app sends every answer, every recommended product and the contact details to the customer’s Omnisend profile, where they appear as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    To add anything else to the email template, your developer [pulls the matching custom properties off the profile](#use-quiz-data-in-omnisend-email-templates).


=== "BigCommerce"


    1. **Add an email question**: your quiz needs an [**email question**](/reference/quiz-builder/questions/#email-address) before it can send anything to Omnisend. Add one from the `+ Add Question` menu, or insert an email block into an existing question.
    2. **Generate an Omnisend API Key**: [generate a new API key in Omnisend](https://app.omnisend.com/integrations/api-keys).

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key for example `RevenueHunt API Key` and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. Paste your `Omnisend API Key` into the field that appears, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection.
    6. **Preview your quiz**: preview it all the way to the results page, to send the first contact. Use a sample email such as `alexa@example.com`, and give sample answers so the properties arrive in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (for example `Alexa RevenueHunt / alexa@example.com`) has been added. Click on the profile to view all custom properties from the quiz, including:

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    From now on, whenever a customer finishes your quiz, their contact details, answers and product recommendations are sent to your Omnisend account.

    The app sends every answer, every recommended product and the contact details to the customer’s Omnisend profile, where they appear as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    To add anything else to the email template, your developer [pulls the matching custom properties off the profile](#use-quiz-data-in-omnisend-email-templates).


=== "Standalone"

    1. **Add an email question**: your quiz needs an [**email question**](/reference/quiz-builder/questions/#email-address) before it can send anything to Omnisend. Add one from the `+ Add Question` menu, or insert an email block into an existing question.
    2. **Generate an Omnisend API Key**: [generate a new API key in Omnisend](https://app.omnisend.com/integrations/api-keys).

        - Log in to your Omnisend account.
        - Go to **Store Settings** > **API** and create a new API key.
        - Name the key for example `RevenueHunt API Key` and grant all permissions.
        - Copy the generated API key.

        ![how to send leads to omnisend api key generate](/images/how_to_omnisend_create_api_key.png){:width="500px"}

    3. **Connect to Omnisend**: Access the [Quiz Builder](/reference/quiz-builder/) and navigate to the [Connect/Integrations](/reference/quiz-builder/connect-integrations/) tab. Scroll to the Omnisend section and click on the `Connect` button to initiate the connection process.
    4. Paste your `Omnisend API Key` into the field that appears, then click `Save`.
    5. Update the preview/live quiz with the top-right `Publish` button to save the connection.
    6. **Preview your quiz**: preview it all the way to the results page, to send the first contact. Use a sample email such as `alexa@example.com`, and give sample answers so the properties arrive in Omnisend.
    7. **Check your profile**: Go back to the Omnisend platform and navigate to the **Dashboard** > **Audience** > **Contacts**. Check if the sample profile (for example `Alexa RevenueHunt / alexa@example.com`) has been added. Click on the profile to view all custom properties from the quiz, including:

        - Quiz answers
        - Recommended products
        - Quiz name
        - Product links, names, and images.



    From now on, whenever a customer finishes your quiz, their contact details, answers and product recommendations are sent to your Omnisend account.

    The app sends every answer, every recommended product and the contact details to the customer’s Omnisend profile, where they appear as `custom properties`.


    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    To add anything else to the email template, your developer [pulls the matching custom properties off the profile](#use-quiz-data-in-omnisend-email-templates).


## Custom properties sent to Omnisend

Every completed response is sent to Omnisend as `custom properties` on the contact profile. Property names include your quiz ID, so two quizzes never overwrite each other's data on the same contact.

=== "Shopify"

    Property names use the quiz **Short ID** (`[SQID]`) and the internal **references** (`[REF]`) of your questions, choices, tags and slots.

    !!! info "Hyphens become underscores"
        Omnisend does not accept a hyphen in a property name, so every ID is converted. A block reference of `qbc-485600ce` appears in Omnisend as `qbc_485600ce`.

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
        The email address is sent as an Omnisend identifier with `source: quiz-[SQID]` and a status of `subscribed` or `nonSubscribed`. A phone number, when provided, is sent as an identifier for SMS marketing. If the quiz block has Omnisend consent enabled, the status is set to `subscribed` along with a `statusDate`. See [how to ask for marketing consent](/how-to-guides/ask-for-marketing-consent/).

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
        Omnisend has strict naming rules. A question title, tag name or slot name is lowercased, underscored and sometimes truncated to become a property name.

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
        Omnisend has strict naming rules. A question title, tag name or slot name is lowercased, underscored and sometimes truncated to become a property name.

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
        Omnisend has strict naming rules. A question title, tag name or slot name is lowercased, underscored and sometimes truncated to become a property name.

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
        Omnisend has strict naming rules. A question title, tag name or slot name is lowercased, underscored and sometimes truncated to become a property name.

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
        Omnisend has strict naming rules. A question title, tag name or slot name is lowercased, underscored and sometimes truncated to become a property name.

        - A question titled "What is your skin type?" becomes `q_lvps1n_what_is_your_skin_type: Oily`
        - A tag named "Skin type: oily" becomes `t_lvps1n_skin_type_oily: true`

    !!! info "Identifiers and consent"
        The email address, and the phone number when provided, are sent as Omnisend identifiers with a status of `subscribed` on submission.

!!! tip "Cannot find a property in Omnisend?"

    Omnisend only lists properties it has already received, so take a test quiz first and try again.

    In the Built for Shopify version, a property name holds the reference of the block, choice or tag, not its title. Find that reference in the Quiz Builder, under the `Advanced` tab of the block or choice. Renaming a question therefore does not break your Omnisend setup. The legacy versions work the other way round: a property name is built from the question title, so renaming a question creates a new property.

??? info "Legacy vs Built for Shopify: property naming"

    If you migrated from the legacy app, your Omnisend segments and email templates need updating because the property names changed.

    | Data | Legacy | Built for Shopify |
    | :--- | :--- | :--- |
    | Key format | `[PROPERTY]_[ID]` | `quiz_[SQID]_[PROPERTY]` |
    | Answers | `q_[ID]_[QUESTION_TITLE]`, built from the sanitized question title | `quiz_[SQID]_answer_[BLOCK_REF]`, built from the block reference |
    | Variables | Not sent | `quiz_[SQID]_variable_[NAME]` and `quiz_[SQID]_highest_variable_ref` |
    | Products | Title, URL, price and image only | Adds slot headings and descriptions, currency, vendor, handle and item IDs |
    | Consent | Defaults to `subscribed` on submission | Follows the Omnisend consent setting on the quiz block |

## Send follow-up emails with Omnisend

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=zJTtTF4AcwpfJ18y&amp;start=135" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can set up a post-quiz email campaign in Omnisend. It sends the product recommendations, or any other offer, to everyone who finished the quiz.

    The instructions below cover building the segment, setting up an automation workflow, and putting the quiz results into the email.

    !!! warning

        Email templates and flows are not a one-click setup. Someone who knows Omnisend has to build them.

        The app sends the quiz data to Omnisend. You build the flows and the email templates in Omnisend, so ask Omnisend support about that part of the setup.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a segment**: in Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) holding everyone who finished the quiz. Filter on a `custom property` that only those contacts carry, such as `quiz_QUIZID_quiz_name`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Pick a property that only these contacts carry, such as `quiz_QUIZID_quiz_name`, and copy its name.
        - Go to `Audience` > `Segments` and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, for example `Skincare Quiz Basic Segment`, and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set up an automated workflow**: build an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) that starts when someone joins that segment. Omnisend then runs the email sequence for everyone in it.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Go to the `Automation` section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select `When someone enters the segment` and choose the segment you created, for example `Skincare Quiz Basic Segment`.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the email template**: putting the quiz results and product recommendations into an email takes HTML, CSS and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/). Start from one of Omnisend’s templates, add the quiz data as custom properties, and restyle it to match your brand.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject, for example `Your Quiz Results`, and add a subheading.
        - Edit the email content as needed, then save changes to access the email editor.

    5. **Include the quiz results**: add an `HTML` element to the email builder.

        - In the quiz builder, go to `Settings` > `Integrations` and generate an Omnisend email template.

            ![how to omnisend email template](/images/how_to_shopifyv2_omnisend_template.png){:width="500px"}
        - Copy the generated code and paste it into the HTML block of your email template in Omnisend.

            ![how to omnisend email template](/images/how_to_shopifyv2_omnisend_template_copy.png)
        - The code builds a ready-made email holding the quiz results and the recommended products. Edit it as you like.

        !!! warning "Omnisend email template"
            Some merchants have reported that the generated email template does not work as expected. If you hit this, please [contact the RevenueHunt support team](/how-to-guides/contact-customer-support/).

    6. **Preview and test the email**: preview it as one of the segment subscribers. Then finish any remaining steps in the workflow.
    7. **Save and start the workflow**: save your changes, then start the workflow.



=== "Shopify (Legacy)"

    You can set up a post-quiz email campaign in Omnisend. It sends the product recommendations, or any other offer, to everyone who finished the quiz.

    The instructions below cover building the segment, setting up an automation workflow, and putting the quiz results into the email.

    !!! warning

        Email templates and flows are not a one-click setup. Someone who knows Omnisend has to build them.

        The app sends the quiz data to Omnisend. You build the flows and the email templates in Omnisend, so ask Omnisend support about that part of the setup.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a segment**: in Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) holding everyone who finished the quiz. Filter on a `custom property` that only those contacts carry, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Pick a property that only these contacts carry, such as `permalink_quiz_id`, and copy its name.
        - Go to `Audience` > `Segments` and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, for example `Skincare Quiz Basic Segment`, and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set up an automated workflow**: build an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) that starts when someone joins that segment. Omnisend then runs the email sequence for everyone in it.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Go to the `Automation` section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select `When someone enters the segment` and choose the segment you created, for example `Skincare Quiz Basic Segment`.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject, for example `Your Quiz Results`, and add a subheading.
        - Edit the email content as needed, then save changes to access the email editor.

    5. Start from the [sample quiz results email templates](#email-templates) on this page. To build your own instead, use the [custom properties](#use-quiz-data-in-omnisend-email-templates) the quiz sends to Omnisend.
    6. **Preview and test the email**: preview it as one of the segment subscribers. Then finish any remaining steps in the workflow.
    7. **Save and start the workflow**: save your changes, then start the workflow.


=== "WooCommerce"


    You can set up a post-quiz email campaign in Omnisend. It sends the product recommendations, or any other offer, to everyone who finished the quiz.

    The instructions below cover building the segment, setting up an automation workflow, and putting the quiz results into the email.

    !!! warning

        Email templates and flows are not a one-click setup. Someone who knows Omnisend has to build them.

        The app sends the quiz data to Omnisend. You build the flows and the email templates in Omnisend, so ask Omnisend support about that part of the setup.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a segment**: in Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) holding everyone who finished the quiz. Filter on a `custom property` that only those contacts carry, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Pick a property that only these contacts carry, such as `permalink_quiz_id`, and copy its name.
        - Go to `Audience` > `Segments` and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, for example `Skincare Quiz Basic Segment`, and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set up an automated workflow**: build an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) that starts when someone joins that segment. Omnisend then runs the email sequence for everyone in it.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Go to the `Automation` section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select `When someone enters the segment` and choose the segment you created, for example `Skincare Quiz Basic Segment`.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject, for example `Your Quiz Results`, and add a subheading.
        - Edit the email content as needed, then save changes to access the email editor.

    5. Start from the [sample quiz results email templates](#email-templates) on this page. To build your own instead, use the [custom properties](#use-quiz-data-in-omnisend-email-templates) the quiz sends to Omnisend.
    6. **Preview and test the email**: preview it as one of the segment subscribers. Then finish any remaining steps in the workflow.
    7. **Save and start the workflow**: save your changes, then start the workflow.


=== "Magento"



    You can set up a post-quiz email campaign in Omnisend. It sends the product recommendations, or any other offer, to everyone who finished the quiz.

    The instructions below cover building the segment, setting up an automation workflow, and putting the quiz results into the email.

    !!! warning

        Email templates and flows are not a one-click setup. Someone who knows Omnisend has to build them.

        The app sends the quiz data to Omnisend. You build the flows and the email templates in Omnisend, so ask Omnisend support about that part of the setup.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a segment**: in Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) holding everyone who finished the quiz. Filter on a `custom property` that only those contacts carry, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Pick a property that only these contacts carry, such as `permalink_quiz_id`, and copy its name.
        - Go to `Audience` > `Segments` and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, for example `Skincare Quiz Basic Segment`, and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set up an automated workflow**: build an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) that starts when someone joins that segment. Omnisend then runs the email sequence for everyone in it.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Go to the `Automation` section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select `When someone enters the segment` and choose the segment you created, for example `Skincare Quiz Basic Segment`.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject, for example `Your Quiz Results`, and add a subheading.
        - Edit the email content as needed, then save changes to access the email editor.

    5. Start from the [sample quiz results email templates](#email-templates) on this page. To build your own instead, use the [custom properties](#use-quiz-data-in-omnisend-email-templates) the quiz sends to Omnisend.
    6. **Preview and test the email**: preview it as one of the segment subscribers. Then finish any remaining steps in the workflow.
    7. **Save and start the workflow**: save your changes, then start the workflow.


=== "BigCommerce"


    You can set up a post-quiz email campaign in Omnisend. It sends the product recommendations, or any other offer, to everyone who finished the quiz.

    The instructions below cover building the segment, setting up an automation workflow, and putting the quiz results into the email.

    !!! warning

        Email templates and flows are not a one-click setup. Someone who knows Omnisend has to build them.

        The app sends the quiz data to Omnisend. You build the flows and the email templates in Omnisend, so ask Omnisend support about that part of the setup.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a segment**: in Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) holding everyone who finished the quiz. Filter on a `custom property` that only those contacts carry, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Pick a property that only these contacts carry, such as `permalink_quiz_id`, and copy its name.
        - Go to `Audience` > `Segments` and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, for example `Skincare Quiz Basic Segment`, and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set up an automated workflow**: build an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) that starts when someone joins that segment. Omnisend then runs the email sequence for everyone in it.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Go to the `Automation` section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select `When someone enters the segment` and choose the segment you created, for example `Skincare Quiz Basic Segment`.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject, for example `Your Quiz Results`, and add a subheading.
        - Edit the email content as needed, then save changes to access the email editor.

    5. Start from the [sample quiz results email templates](#email-templates) on this page. To build your own instead, use the [custom properties](#use-quiz-data-in-omnisend-email-templates) the quiz sends to Omnisend.
    6. **Preview and test the email**: preview it as one of the segment subscribers. Then finish any remaining steps in the workflow.
    7. **Save and start the workflow**: save your changes, then start the workflow.



=== "Standalone"


    You can set up a post-quiz email campaign in Omnisend. It sends the product recommendations, or any other offer, to everyone who finished the quiz.

    The instructions below cover building the segment, setting up an automation workflow, and putting the quiz results into the email.

    !!! warning

        Email templates and flows are not a one-click setup. Someone who knows Omnisend has to build them.

        The app sends the quiz data to Omnisend. You build the flows and the email templates in Omnisend, so ask Omnisend support about that part of the setup.

    1. **Connect Your Quiz to Omnisend**: Refer to [Link Quiz to Omnisend](#link-quiz-to-omnisend) to ensure your quiz is correctly connected to Omnisend.
    2. **Create a segment**: in Omnisend, [create a segment](https://support.omnisend.com/en/articles/1400415-creating-segments) holding everyone who finished the quiz. Filter on a `custom property` that only those contacts carry, such as `permalink_quiz_id`.

        ![how to omnisend segment](/images/how_to_omnisend_create_segment.png)

        - Pick a property that only these contacts carry, such as `permalink_quiz_id`, and copy its name.
        - Go to `Audience` > `Segments` and create a new segment from scratch.
        - Add a filter using the copied property.
        - Name the segment something recognizable, for example `Skincare Quiz Basic Segment`, and save it.
        - Omnisend will automatically add profiles with this property to the segment.


    3. **Set up an automated workflow**: build an [automation workflow](https://support.omnisend.com/en/articles/3954813-omnisend-automation-workflow-settings) that starts when someone joins that segment. Omnisend then runs the email sequence for everyone in it.

        ![how to omnisend flow](https://loom.com/i/2e3ebc719c764822935b79d68c67456b?workflows_screenshot=true)

        - Go to the `Automation` section in Omnisend.
        - Explore existing workflows or create a new workflow from scratch.
        - Set a trigger for the workflow: select `When someone enters the segment` and choose the segment you created, for example `Skincare Quiz Basic Segment`.
        - Save the changes to initiate the workflow when users enter the segment.

    4. **Customize the Email Template**: Customizing the email template to include quiz results and product recommendations requires HTML, CSS, and [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) knowledge. Use Omnisend’s existing email templates as a base and modify them to incorporate the quiz data as custom properties. Ensure the template aligns with your brand’s style guide.

        - Drag and drop an email action below the trigger in the workflow.
        - Set the email subject, for example `Your Quiz Results`, and add a subheading.
        - Edit the email content as needed, then save changes to access the email editor.

    5. Start from the [sample quiz results email templates](#email-templates) on this page. To build your own instead, use the [custom properties](#use-quiz-data-in-omnisend-email-templates) the quiz sends to Omnisend.
    6. **Preview and test the email**: preview it as one of the segment subscribers. Then finish any remaining steps in the workflow.
    7. **Save and start the workflow**: save your changes, then start the workflow.



## Use quiz data in Omnisend email templates

See [Custom Properties Sent to Omnisend](#custom-properties-sent-to-omnisend) for the full list of properties you can pull into a template.

=== "Shopify"

    Use the `custom properties` the quiz sends to Omnisend to personalize your email templates.

    ![how to omnisend custom properties](/images/how_to_shopifyv2_omnisend_custom_properties.gif)

    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).


=== "Shopify (Legacy)"


    Use the `custom properties` the quiz sends to Omnisend to personalize your email templates.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "WooCommerce"

    Use the `custom properties` the quiz sends to Omnisend to personalize your email templates.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "Magento"

    Use the `custom properties` the quiz sends to Omnisend to personalize your email templates.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "BigCommerce"

    Use the `custom properties` the quiz sends to Omnisend to personalize your email templates.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

=== "Standalone"

    Use the `custom properties` the quiz sends to Omnisend to personalize your email templates.

    ![how to omnisend custom properties](/images/how_to_omnisend_custom_properties.gif)


    If you need to add any additional information to the email template, your developer can do so by [pulling the appropriate custom properties from the user profile](https://support.omnisend.com/en/articles/1061885-custom-properties-for-contacts).

### Pull customer answers into an email template

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AqwjMV21Q-I?si=PsgLwM2IkSiXHkUV&amp;start=300" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Pull a customer answer into an email template with the `custom properties` the quiz sends to Omnisend. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text.

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Preview the template against one profile, for example `Alexa RevenueHunt`. Check that the custom property shows the answers that customer gave.
    9. Save the email template.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Pull a customer answer into an email template with the `custom properties` the quiz sends to Omnisend. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text.

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Preview the template against one profile, for example `Alexa RevenueHunt`. Check that the custom property shows the answers that customer gave.
    9. Save the email template.


=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Pull a customer answer into an email template with the `custom properties` the quiz sends to Omnisend. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text.

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Preview the template against one profile, for example `Alexa RevenueHunt`. Check that the custom property shows the answers that customer gave.
    9. Save the email template.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Pull a customer answer into an email template with the `custom properties` the quiz sends to Omnisend. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text.

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Preview the template against one profile, for example `Alexa RevenueHunt`. Check that the custom property shows the answers that customer gave.
    9. Save the email template.


=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Pull a customer answer into an email template with the `custom properties` the quiz sends to Omnisend. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text.

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Preview the template against one profile, for example `Alexa RevenueHunt`. Check that the custom property shows the answers that customer gave.
    9. Save the email template.


=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1911ea75ad7d4531b3886b0fd5af01a7?sid=741a1bb2-72bb-41ee-be1b-390654e18369" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Pull a customer answer into an email template with the `custom properties` the quiz sends to Omnisend. This is done by using the `insert personalization tag` feature in Omnisend.

    1. Navigate to your Omnisend automation workflow. Select the email you want to edit. Begin editing the content to create a new template.
    2. Add a text element to your email template. Type a base message, e.g., "You said that your skin feels...".
    3. Access the text block settings to `insert personalization tag`.
    4. Use the personalization tag feature to browse available custom properties from quiz profiles.
    5. Search for the specific answer related to the quiz question (e.g., `quiz_LKKT6j_answer_qbc_485600ce`).

        ![how to omnisend insert personalization tag](/images/how_to_omnisend_insert_personalization_tag.png){:width="500px"}

    6. Insert the custom property into your text element. You can optionally provide default text.

        ![how to omnisend personalization tag](https://loom.com/i/69abdc33b47a4321b8b0001e5f1a57ba?workflows_screenshot=true)
    7. Save your changes to the email template.
    8. Preview the template against one profile, for example `Alexa RevenueHunt`. Check that the custom property shows the answers that customer gave.
    9. Save the email template.



### Display a link to the quiz results in an email


=== "Shopify"

    Use `quiz_QUIZID_response_id` to build a link to the quiz results page. Add `#response-{{ contact.custom.quiz_QUIZID_response_id }}` to the end of the `href` on any link to that page.


    !!! example

        `<a href="https://yourwebsite.com/#response-{{ contact.custom.quiz_lBJ9bk_response_id }}">View your quiz results</a>`

        where `lBJ9bk` is the quiz ID and

        - `{{ contact.custom.quiz_lBJ9bk_response_id }}` fetches the response ID, for example `eVgV0Y`.


=== "Shopify (Legacy)"

    Use the `permalink_koHP8VA` in your email template. This property already holds the full URL of the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`


=== "WooCommerce"

    Use the `permalink_koHP8VA` in your email template. This property already holds the full URL of the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "Magento"

    Use the `permalink_koHP8VA` in your email template. This property already holds the full URL of the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "BigCommerce"

    Use the `permalink_koHP8VA` in your email template. This property already holds the full URL of the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`

=== "Standalone"

    Use the `permalink_koHP8VA` in your email template. This property already holds the full URL of the quiz results page.

    !!! example

        `<a href="{{ contact.custom.permalink_koHP8VA }}">View your quiz results</a>`




### Customer tags in Omnisend

A customer profile is updated on every quiz take, with the new answers and product recommendations. Omnisend does not remove the tags from earlier sessions, though. The `tags_quizID` property holds the latest customer tags, so build your segments on that one.



### Email templates

=== "Shopify"

    In the [Integrations](/reference/quiz-builder/connect-integrations/) section, under `Omnisend`, you can find the `omnisend template`.

    ![how to shopifyv2 omnisend template](/images/how_to_shopifyv2_omnisend_template.png)

    Click on the button to receive and copy an HTML email template specifically tailored for the quiz.

    ![how to shopifyv2 omnisend template copy](/images/how_to_shopifyv2_omnisend_template_copy.png)

    You can use this template as a reference to create your own.

    !!! warning "Omnisend email template"
        Some merchants have reported that the generated email template does not work as expected. If you hit this, please [contact the RevenueHunt support team](/how-to-guides/contact-customer-support/).


=== "Shopify (Legacy)"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    These templates will not work if you paste them in unchanged, because they were written for a demo quiz. Your `quiz ID` differs, and so do the other property names. Your developer edits the `custom properties` in the template to match the ones your quiz sends, then inserts the code as a `custom HTML block` in the Omnisend email template.

=== "WooCommerce"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    These templates will not work if you paste them in unchanged, because they were written for a demo quiz. Your `quiz ID` differs, and so do the other property names. Your developer edits the `custom properties` in the template to match the ones your quiz sends, then inserts the code as a `custom HTML block` in the Omnisend email template.

=== "Magento"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    These templates will not work if you paste them in unchanged, because they were written for a demo quiz. Your `quiz ID` differs, and so do the other property names. Your developer edits the `custom properties` in the template to match the ones your quiz sends, then inserts the code as a `custom HTML block` in the Omnisend email template.


=== "BigCommerce"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    These templates will not work if you paste them in unchanged, because they were written for a demo quiz. Your `quiz ID` differs, and so do the other property names. Your developer edits the `custom properties` in the template to match the ones your quiz sends, then inserts the code as a `custom HTML block` in the Omnisend email template.

=== "Standalone"

    Here are some email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://docs.google.com/document/d/1wy-_nb0nGyU0_NsWB6YZMiXbXiA2sMyrGu6ks7TqzjQ/edit?usp=sharing)
    - [Advanced Slots Template (Morning & Night Routine)](https://docs.google.com/document/d/1RIXL2zF0ErGbUX5IwCRXjnr8bNV3wXuZQuuy3NmbL_I/edit?usp=sharing)
    - [Products List Template (Coffee Recommendations)](https://docs.google.com/document/d/175YmJpZ_iTahGFip46MGb6fcn5cupNsCEuZFxMnFCAg/edit?usp=sharing)

    These templates will not work if you paste them in unchanged, because they were written for a demo quiz. Your `quiz ID` differs, and so do the other property names. Your developer edits the `custom properties` in the template to match the ones your quiz sends, then inserts the code as a `custom HTML block` in the Omnisend email template.


---
This article explains how to connect your quiz to Omnisend, build a segment from the customers who finished it, and email them their quiz results.
