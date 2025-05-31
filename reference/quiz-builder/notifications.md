# Notifications

=== "Shopify"

    In the Notifications tab of the Quiz Builder, you can activate and edit the emails that the customer or the store owner receives at the end of the quiz.

=== "Shopify V2"

    In the Notifications tab of the Quiz Builder, you can activate and edit the emails that the customer or the store owner receives at the end of the quiz.

=== "WooCommerce"

    In the Notifications tab of the Quiz Builder, you can activate and edit the emails that the customer or the store owner receives at the end of the quiz.

=== "Magento"

    In the Notifications tab of the Quiz Builder, you can activate and edit the emails that the customer or the store owner receives at the end of the quiz.

=== "BigCommerce"

    In the Notifications tab of the Quiz Builder, you can activate and edit the emails that the customer or the store owner receives at the end of the quiz.

=== "Standalone"

    In the Notifications tab of the Quiz Builder, you can activate and edit the emails that the customer or the store owner receives at the end of the quiz.

### To Respondent

=== "Shopify"

    ![quiz builder notifications to respondent inactive](/images/manual_quizbuilder_notifications_torespondent_inactive.png)

    You need to have one email question in order to send notifications to the respondents. Check the [Quiz Builder](questions/) section to add an email question to your quiz.

    To activate notification emails to the quiz takers, toggle the "Send email when someone completes the quiz" option on. Additional customization options will appear.

    ![quiz builder notifications to respondent active](/images/manual_quizbuilder_notifications_torespondent_active.png)

    TO RESPONDENT section displays the email settings on the left and the email preview on the right.

    ![quiz builder notifications to respondent preview](/images/manual_quizbuilder_notifications_torespondent_active_searchbar.png)

    Select a response from the list to preview how the email will look like.

    `Email REPLY_TO:` - Fill in the email address to which the customer will be able to send a reply.

    `Email TO:` - Select from which email question (in case of multiple email questions) the customer's address should be taken in order to send the results.

    `Email Subject:` - Type in the email subject that the customer will see in their inbox. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, answer to a specific question, etc.)

    `Email Text Message` - Edit the content of the email sent to the customer. You can choose between the Basic text email template (cannot be styled) or an advanced HTML email template (can be styled and allows to display product images).

    `switch to advanced HTML message` - Switches to the advanced HTML email template. Email can be edited with HTML and metadata can be included with [Handlebars](https://github.com/helpers/handlebars-helpers).

    ![quiz builder notifications HTML](/images/manual_quizbuilder_notifications_torespondent_active_html.png)

    `switch to basic text message` - Switched to the basic text email template. Email can be edited with regular text. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, recommended products, answers to questions, etc.).

    ![quiz builder notification basic](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)

=== "Shopify V2"

    ![manual_shopifyV2_quizbuilder_notification_torespondent](/images/manual_shopifyV2_quizbuilder_notification_torespondent.png)

    `Send an email when someone completes the quiz` - Activate this option to send notification/results email to the customer email address when they completes the quiz (reaches the results page).

    `Email-to:` - Select a slide that contains the email questions from the dropdown.

    `Reply-to:` - Add an email address to which the notification should be sent.

    `Email subject:` - Add the title of the notification email.

    `Email liquid template` - Add a liquid email template. The template can be built based on the Metadata provided.

    `Useful code snippets:` - Click on an item below  to copy the code snippets to customize the Liquid email template.

    `Items list snippet` - Lists all the recomended products.

    `Responses by block snippet` - Lists all the customer answers.

    `Metadata` - Lists all the metadata provided by the customer.

    `Expand all` - Expands all the metadata.

    `Copy to clipboard` - Copies the selected metadata to the clipboard.

    !!! info "Quiz Response Metadata Structure"

        ![manual_shopifyV2_quizbuilder_notification_metadata](/images/manual_shopifyV2_quizbuilder_notification_metadata.png){width=50%}
        
        This object contains all the data generated when a user completes a quiz — including responses, product recommendations, and result content. It is used to power dynamic result pages, follow-up emails, and custom workflows.

        ---

        **Basic Information**

        `responseId` - Unique ID for this specific quiz response

        `resultRef` - Internal reference to the results layout

        `quizId` - ID of the quiz that was completed

        `quizName` - Name of the quiz

        `firstName / fullName` - Name entered by the user

        `email` - Email address submitted

        `createdAt` - Timestamp of quiz completion (ISO format)

        ---

        **User Answers (`answersByBlock`)**

        ```json
        "answersByBlock": {
        "qbc-485600ce": {
        "type": "picture_choice",
        "value": "Dry and tight all over",
        "choicesRefs": ["qbcc-30928613"]
        }
        }
        ```

        Each quiz question block is mapped to the user's response.

        Fields inside each entry:

        `type` - The kind of question (e.g. multiple_choice, picture_choice, email)

        `value` - The answer selected or typed by the user

        `choicesRefs` - List of selected choice references (used internally)

        Example: `qbc-485600ce` → `type: picture_choice`, `value: "Dry and tight all over"`, `choicesRefs: ["qbcc-30928613"]`
    
        ---

        **Tags**

        ```json
        "tags": []
        ```

        `tags` - A list of tags to assign to the respondent. Often used for segmentation. Empty if unused.

        ---

        **Product Recommendations (`recommendationsBySlot`)**

        ```json
        "recommendationsBySlot": {
        "rsbss-33464eed": {
        "type": "product",
        "value": "Ordinary Serum",
        "variants": [
        ```

        Each result "slot" contains one or more product recommendations.

        Each product object includes: id, title, vendor, handle: Shopify product metadata

        `variants` - Variant ID, price, and image per product

        `slotHeading / slotDescription` - Rich text HTML displayed on result pages

        `image` - URL for the main product image

        `price` - Object with amount and currencyCode

        Example: `rsbss-33464eed` → contains "Ordinary Serum", $45 USD

        ---

        **Variable Scores (`variableScores`)**

        ```json
        "variableScores": { "score": 0 }
        ```

        Used only if the quiz has a scoring logic. Contains numerical results or score breakdowns.

        --- 

        **Result Sections (`resultSections`)**

        ```json
        "resultSections": [
        "rsbh-273d9ef6": {
        "type": "heading",
        "content": "<p>Here's what your skin wants!</p>"
        }
        ]
        ```

        An ordered array of blocks that make up the results page. Each block can be:

        `heading`

        `text`

        `products`

        `button`

        Products blocks have a slots array that contains product lists grouped by slot reference.

        ---

        **Rendered Result Content (`resultContentByBlock`)**

        ```json
        "rsbh-273d9ef6": {
        "type": "heading",
        "content": "<p>Here's what your skin wants!</p>"
        }       
        ```

        A lookup table of rendered content for each block (used in external templates like email).

        Each entry is keyed by the block reference and contains:

        `type` - Type of block (text, heading, products, etc.)

        `content or slots` - The rendered HTML or product data

    !!! info "Use Cases"

        This metadata allows you to:

        - Personalize result pages based on user answers

        - Send dynamic follow-up emails with relevant product suggestions

        - Store quiz responses for analytics and customer profiling

        - Integrate with marketing tools like Klaviyo or HubSpot using dynamic fields





=== "WooCommerce"

    ![quiz builder notifications to respondent inactive](/images/manual_quizbuilder_notifications_torespondent_inactive.png)

    You need to have one email question in order to send notifications to the respondents. Check the [Quiz Builder](questions/) section to add an email question to your quiz.

    To activate notification emails to the quiz takers, toggle the "Send email when someone completes the quiz" option on. Additional customization options will appear.

    ![quiz builder notifications to respondent active](/images/manual_quizbuilder_notifications_torespondent_active.png)

    TO RESPONDENT section displays the email settings on the left and the email preview on the right.

    ![quiz builder notifications to respondent preview](/images/manual_quizbuilder_notifications_torespondent_active_searchbar.png)

    Select a response from the list to preview how the email will look like.

    `Email REPLY_TO:` - Fill in the email address to which the customer will be able to send a reply.

    `Email TO:` - Select from which email question (in case of multiple email questions) the customer's address should be taken in order to send the results.

    `Email Subject:` - Type in the email subject that the customer will see in their inbox. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, answer to a specific question, etc.)

    `Email Text Message` - Edit the content of the email sent to the customer. You can choose between the Basic text email template (cannot be styled) or an advanced HTML email template (can be styled and allows to display product images).

    `switch to advanced HTML message` - Switches to the advanced HTML email template. Email can be edited with HTML and metadata can be included with [Handlebars](https://github.com/helpers/handlebars-helpers).

    ![quiz builder notifications HTML](/images/manual_quizbuilder_notifications_torespondent_active_html.png)

    `switch to basic text message` - Switched to the basic text email template. Email can be edited with regular text. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, recommended products, answers to questions, etc.).

    ![quiz builder notification basic](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)

=== "Magento"

    ![quiz builder notifications to respondent inactive](/images/manual_quizbuilder_notifications_torespondent_inactive.png)

    You need to have one email question in order to send notifications to the respondents. Check the [Quiz Builder](questions/) section to add an email question to your quiz.

    To activate notification emails to the quiz takers, toggle the "Send email when someone completes the quiz" option on. Additional customization options will appear.

    ![quiz builder notifications to respondent active](/images/manual_quizbuilder_notifications_torespondent_active.png)

    TO RESPONDENT section displays the email settings on the left and the email preview on the right.

    ![quiz builder notifications to respondent preview](/images/manual_quizbuilder_notifications_torespondent_active_searchbar.png)

    Select a response from the list to preview how the email will look like.

    `Email REPLY_TO:` - Fill in the email address to which the customer will be able to send a reply.

    `Email TO:` - Select from which email question (in case of multiple email questions) the customer's address should be taken in order to send the results.

    `Email Subject:` - Type in the email subject that the customer will see in their inbox. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, answer to a specific question, etc.)

    `Email Text Message` - Edit the content of the email sent to the customer. You can choose between the Basic text email template (cannot be styled) or an advanced HTML email template (can be styled and allows to display product images).

    `switch to advanced HTML message` - Switches to the advanced HTML email template. Email can be edited with HTML and metadata can be included with [Handlebars](https://github.com/helpers/handlebars-helpers).

    ![quiz builder notifications HTML](/images/manual_quizbuilder_notifications_torespondent_active_html.png)

    `switch to basic text message` - Switched to the basic text email template. Email can be edited with regular text. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, recommended products, answers to questions, etc.).

    ![quiz builder notification basic](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)

=== "BigCommerce"

    ![quiz builder notifications to respondent inactive](/images/manual_quizbuilder_notifications_torespondent_inactive.png)

    You need to have one email question in order to send notifications to the respondents. Check the [Quiz Builder](questions/) section to add an email question to your quiz.

    To activate notification emails to the quiz takers, toggle the "Send email when someone completes the quiz" option on. Additional customization options will appear.

    ![quiz builder notifications to respondent active](/images/manual_quizbuilder_notifications_torespondent_active.png)

    TO RESPONDENT section displays the email settings on the left and the email preview on the right.

    ![quiz builder notifications to respondent preview](/images/manual_quizbuilder_notifications_torespondent_active_searchbar.png)

    Select a response from the list to preview how the email will look like.

    `Email REPLY_TO:` - Fill in the email address to which the customer will be able to send a reply.

    `Email TO:` - Select from which email question (in case of multiple email questions) the customer's address should be taken in order to send the results.

    `Email Subject:` - Type in the email subject that the customer will see in their inbox. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, answer to a specific question, etc.)

    `Email Text Message` - Edit the content of the email sent to the customer. You can choose between the Basic text email template (cannot be styled) or an advanced HTML email template (can be styled and allows to display product images).

    `switch to advanced HTML message` - Switches to the advanced HTML email template. Email can be edited with HTML and metadata can be included with [Handlebars](https://github.com/helpers/handlebars-helpers).

    ![quiz builder notifications HTML](/images/manual_quizbuilder_notifications_torespondent_active_html.png)

    `switch to basic text message` - Switched to the basic text email template. Email can be edited with regular text. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, recommended products, answers to questions, etc.).

    ![quiz builder notification basic](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)

=== "Standalone"

    ![quiz builder notifications to respondent inactive](/images/manual_quizbuilder_notifications_torespondent_inactive.png)

    You need to have one email question in order to send notifications to the respondents. Check the [Quiz Builder](questions/) section to add an email question to your quiz.

    To activate notification emails to the quiz takers, toggle the "Send email when someone completes the quiz" option on. Additional customization options will appear.

    ![quiz builder notifications to respondent active](/images/manual_quizbuilder_notifications_torespondent_active.png)

    TO RESPONDENT section displays the email settings on the left and the email preview on the right.

    ![quiz builder notifications to respondent preview](/images/manual_quizbuilder_notifications_torespondent_active_searchbar.png)

    Select a response from the list to preview how the email will look like.

    `Email REPLY_TO:` - Fill in the email address to which the customer will be able to send a reply.

    `Email TO:` - Select from which email question (in case of multiple email questions) the customer's address should be taken in order to send the results.

    `Email Subject:` - Type in the email subject that the customer will see in their inbox. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, answer to a specific question, etc.)

    `Email Text Message` - Edit the content of the email sent to the customer. You can choose between the Basic text email template (cannot be styled) or an advanced HTML email template (can be styled and allows to display product images).

    `switch to advanced HTML message` - Switches to the advanced HTML email template. Email can be edited with HTML and metadata can be included with [Handlebars](https://github.com/helpers/handlebars-helpers).

    ![quiz builder notifications HTML](/images/manual_quizbuilder_notifications_torespondent_active_html.png)

    `switch to basic text message` - Switched to the basic text email template. Email can be edited with regular text. You can use [Information Recalls](/how-to-guides/use-information-recalls/) to recall information in this text field (for example customer name, quiz name, recommended products, answers to questions, etc.).

    ![quiz builder notification basic](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)

### To Self

=== "Shopify"

    ![quiz builder notifications to self inactive](/images/manual_quizbuilder_notifications_toself_inactive.png)

    `Get email when someone completes the quiz` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page. This email template cannot be edited.

    `Get email when someone proceedes to checkout` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page and proceeds to checkout/cart. This email template cannot be edited.

    ![quiz builder notifications to self active](/images/manual_quizbuilder_notifications_toself_active.png)

=== "Shopify V2"

    ![manual_shopifyV2_quizbuilder_notification_toself](/images/manual_shopifyV2_quizbuilder_notification_toself.png)

    `Receive an email when someone completes the quiz` - Activate this option to recieve notifications to your specified email address when someone completes the quiz (reaches the results page).

    `Email TO:` - Add an email address to which the notification should be sent.

    `Email subject:` - Add the title of the notification email.

    `Email liquid template` - Add liquid email template. The template can be built based on the Metadata provided.

    `Useful code snippets:` - Click on an item below  to copy the code snippets to customize the Liquid email template.

    `Personal information template` - Lists all the personal infomation provided by the user.

    `Responses by block snippet` - Lists all the customer answers.

=== "WooCommerce"

    ![quiz builder notifications to self inactive](/images/manual_quizbuilder_notifications_toself_inactive.png)

    `Get email when someone completes the quiz` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page. This email template cannot be edited.

    `Get email when someone proceedes to checkout` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page and proceeds to checkout/cart. This email template cannot be edited.

    ![quiz builder notifications to self active](/images/manual_quizbuilder_notifications_toself_active.png)

=== "Magento"

    ![quiz builder notifications to self inactive](/images/manual_quizbuilder_notifications_toself_inactive.png)

    `Get email when someone completes the quiz` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page. This email template cannot be edited.

    `Get email when someone proceedes to checkout` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page and proceeds to checkout/cart. This email template cannot be edited.

    ![quiz builder notifications to self active](/images/manual_quizbuilder_notifications_toself_active.png)

=== "BigCommerce"

    ![quiz builder notifications to self inactive](/images/manual_quizbuilder_notifications_toself_inactive.png)

    `Get email when someone completes the quiz` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page. This email template cannot be edited.

    `Get email when someone proceedes to checkout` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page and proceeds to checkout/cart. This email template cannot be edited.

    ![quiz builder notifications to self active](/images/manual_quizbuilder_notifications_toself_active.png)

=== "Standalone"

    ![quiz builder notifications to self inactive](/images/manual_quizbuilder_notifications_toself_inactive.png)

    `Get email when someone completes the quiz` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page. This email template cannot be edited.

    `Get email when someone proceedes to checkout` - You'll receive an email as shown on the preview to the provided email address whenever someone reaches the results page and proceeds to checkout/cart. This email template cannot be edited.

    ![quiz builder notifications to self active](/images/manual_quizbuilder_notifications_toself_active.png)


---

← [Back to Quiz Builder Index](/reference/quiz-builder/)


← Previous: [Results Page](/reference/quiz-builder/results-page/)
Next: [Quiz Settings](/reference/quiz-builder/quiz-settings/) →
