---
icon: material/email-heart-outline
---

# Setting Up Result Emails with Product Recommendation Quiz

Email results notifications enhance customer engagement by following up with participants of your Product Recommendation Quiz. 

This guide covers setting up email results for both [quiz respondents](#email-quiz-results-via-shop-quiz-app) and [administartors](#activate-email-notifications-to-admin) and well as sending results emails via an [external CRM service](/how-to-guides/send-leads-to-crm/).


!!! warning

    We recently encountered issues with our previous email provider and switched to a new service. Unfortunately, some emails were affected by this change, and not all messages have been going through as expected. 

    Starting on <b>November 29th, 2024</b>, we kindly ask you to [configure your SMTP settings](/how-to-guides/send-result-emails-from-custom-server/) to continue sending result emails through the app. Notification emails will now be sent from your email address ensuring deliverabilty and consistent branding.



## Email Quiz Results via RevenueHunt app

Result emails can be sent directly from the RevenueHunt app to the email provided by the customer. 

Follow the step by step instructions below to active and edit the result emails sent with the app:

=== "Shopify"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](/reference/quiz-builder/questions/).
    2. **Activate Respondent Emails**: Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    4. **Email TO**: If you have more than one email question in your quiz, choose an answer to which email question should be used to send the result emails. If you have only one email question, it will be selected by default.
    5. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    5. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template is easy to use. Type the text that you want the customer to see in the `Email Text Message` field. You can personalize the email subject and content. You can add dynamic elements with `@`. Use `@` / [Information Recalls](/how-to-guides/use-information-recalls/) to recall quiz information in the email body. You can recall data such as customer name, email, phone number, quiz name, question responses, recommended products and more. Basic email template does not allow the display of images or color customization but offers maximum deliverability.
        ![how to send result emails basic tempalte](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "Shopify V2"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](/reference/quiz-builder/questions/).
    2. **Activate Respondent Emails**: Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and check the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_shopifyV2_quizbuilder_notification_torespondent.png)
    3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    4. **Email TO**: Choose an answer to which email question should be used to send the result emails to.
    5. **Email Subject**: Edit the title of the email that customers will receive. 
    5. **Edit Email Content**: Configure the email your customers will receive. Email template requires the knowledge of HTML and liquid to be edited. You can find *useful code snippets* in a field below. Click on an item below to copy the code snippets to customize the Liquid email template. For example, you can use the `items list snippet` to display the recommended products in the email or the `responses by block snippet` to display the customer answers. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use liquid code to loop through and display recommended products or customize content based on quiz outcomes. 

        !!! note
            Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).

        !!! tip

            You can copy the useful code snippets and paste them into a large languge model like ChatGPT or Gemini to style the liquid email template.
   
    6. **Save the changes**: Remember to save the changes with the top-right `save` button to update the preview/live quiz.


=== "WooCommerce"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](/reference/quiz-builder/questions/).
    2. **Activate Respondent Emails**: Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    4. **Email TO**: If you have more than one email question in your quiz, choose an answer to which email question should be used to send the result emails. If you have only one email question, it will be selected by default.
    5. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    5. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template is easy to use. Type the text that you want the customer to see in the `Email Text Message` field. You can personalize the email subject and content. You can add dynamic elements with `@`. Use `@` / [Information Recalls](/how-to-guides/use-information-recalls/) to recall quiz information in the email body. You can recall data such as customer name, email, phone number, quiz name, question responses, recommended products and more. Basic email template does not allow the display of images or color customization but offers maximum deliverability.
        ![how to send result emails basic tempalte](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "Magento"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](/reference/quiz-builder/questions/).
    2. **Activate Respondent Emails**: Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    4. **Email TO**: If you have more than one email question in your quiz, choose an answer to which email question should be used to send the result emails. If you have only one email question, it will be selected by default.
    5. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    5. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template is easy to use. Type the text that you want the customer to see in the `Email Text Message` field. You can personalize the email subject and content. You can add dynamic elements with `@`. Use `@` / [Information Recalls](/how-to-guides/use-information-recalls/) to recall quiz information in the email body. You can recall data such as customer name, email, phone number, quiz name, question responses, recommended products and more. Basic email template does not allow the display of images or color customization but offers maximum deliverability.
        ![how to send result emails basic tempalte](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "BigCommerce"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](/reference/quiz-builder/questions/).
    2. **Activate Respondent Emails**: Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    4. **Email TO**: If you have more than one email question in your quiz, choose an answer to which email question should be used to send the result emails. If you have only one email question, it will be selected by default.
    5. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    5. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template is easy to use. Type the text that you want the customer to see in the `Email Text Message` field. You can personalize the email subject and content. You can add dynamic elements with `@`. Use `@` / [Information Recalls](/how-to-guides/use-information-recalls/) to recall quiz information in the email body. You can recall data such as customer name, email, phone number, quiz name, question responses, recommended products and more. Basic email template does not allow the display of images or color customization but offers maximum deliverability.
        ![how to send result emails basic tempalte](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "Standalone"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the follow-up emails with the quiz results that are sent to your customers will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an email question. To add an email question go to the [Quiz Builder](/reference/quiz-builder/questions/).
    2. **Activate Respondent Emails**: Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    3. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    4. **Email TO**: If you have more than one email question in your quiz, choose an answer to which email question should be used to send the result emails. If you have only one email question, it will be selected by default.
    5. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    5. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template is easy to use. Type the text that you want the customer to see in the `Email Text Message` field. You can personalize the email subject and content. You can add dynamic elements with `@`. Use `@` / [Information Recalls](/how-to-guides/use-information-recalls/) to recall quiz information in the email body. You can recall data such as customer name, email, phone number, quiz name, question responses, recommended products and more. Basic email template does not allow the display of images or color customization but offers maximum deliverability.
        ![how to send result emails basic tempalte](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](#advanced-html-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

## Sending Result Emails with Your CRM

You can automate the process of sending quiz result emails using your own CRM platform. Connect your quiz to one of our [available integrations](/how-to-guides/send-leads-to-crm/), and the quiz data will be transmitted to your CRM as soon as the customer completes the quiz and reaches the results page. This allows you to set up your own email sequences directly within your CRM. For guidance on connecting the quiz to our integrations, refer to the [documentation provided for each integration](/how-to-guides/send-leads-to-crm/).

## Activate Email Notifications To Admin

You can receive an email notification every time someone completes the quiz or proceeds to checkout. This allows the quiz admin/responsible to stay up to date with quiz engagments. 

!!! warning

    We recently encountered issues with our previous email provider and switched to a new service. Unfortunately, some emails were affected by this change, and not all TO-SELF notifications have been going through as expected. 

    Starting on <b>November 29th, 2024</b>, we kindly ask you to [configure your SMTP settings](/how-to-guides/send-result-emails-from-custom-server/) to continue receiving notification emails through the app. Notification emails will now be sent from your email address ensuring deliverabilty.

=== "Shopify"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    2. **Activate Notifications**: Toggle the button to activate the emails. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.
        ![how to send resutl emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. Add your email address in the `Send email notification to` field.
    4. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "Shopify V2"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    2. **Activate Notifications**: Check the `Receive an email when someone completes the quiz ` filed to activate the emails.
        ![how to send resutl emails to self](/images/manual_shopifyV2_quizbuilder_notification_toself.png)
    3. Add your email address in the `Email to` field and add the email subject in the `Subject` field.
    4. Edit the liquid email template. You can use the useful code snippets to customize the email template.
    4. **Save the changes**: Remember to save the changes with the top-right `Save` button.

=== "WooCommerce"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    2. **Activate Notifications**: Toggle the button to activate the emails. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.
        ![how to send resutl emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. Add your email address in the `Send email notification to` field.
    4. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "Magento"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    2. **Activate Notifications**: Toggle the button to activate the emails. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.
        ![how to send resutl emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. Add your email address in the `Send email notification to` field.
    4. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "BigCommerce"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    2. **Activate Notifications**: Toggle the button to activate the emails. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.
        ![how to send resutl emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. Add your email address in the `Send email notification to` field.
    4. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "Standalone"

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and provide your email SMTP credentials. Follow [these instruction](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            <b>If you're unsure what credentials to use, check your email provider's documentation (look for "SMTP") or contact their customer support.</b>

    1. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    2. **Activate Notifications**: Toggle the button to activate the emails. Here, you can opt to receive an email for each quiz completion and/or when someone proceeds to the cart or checkout.
        ![how to send resutl emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. Add your email address in the `Send email notification to` field.
    4. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.


## Advanced HTML Email Templates

=== "Shopify"

    **Using Metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: If you wish to display the respondent’s name, you can use the `{{first_name}}` handlebar in your code.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```
        
    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Usign Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Builtin Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
    - GitHub Handlebars Helpers: [Handlebars Helpers on GitHub](https://github.com/helpers/handlebars-helpers)

    The format for helpers in Notifications might slightly differ from those on GitHub. For instance, to truncate a product name to 7 characters, you should write:

    ```handlebars
    {{truncate product.name 7}}
    ```

    If you want to present specific metadata you should use a special property `{{#eq}} ... {{/eq}}`

    - To target all slot blocks:

    ```handlebars
    {{#eq block.type "SlotsBlock"}} ... {{/eq}}
    ```

    - To target a specific block, for example, a block with the ID `A4TeY9`:

    ```handlebars
    {{#eq block.id "A4TeY9"}} … {{/eq}}
    ```

    Specific use cases:

    - **List the Recommended Products**: If you want to loop through the most recommended products, you can do so like this:
        ```html
            {{#each products as | product |}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        ```

    - **List recommended products with Slot Titles**: If you want to list the most recommended product with Slot titles, you can do so like this:
        ```html
        {{#each blocks as |block|}}
        {{#eq block.type "SlotsBlock"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/each}}
        {{/eq}}
        {{#eq block.type "ProductsBlock"}}
        {{#each block.products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

    - **List recommended products separated by Slot Blocks**: If you want to recommend a Morning and Night slot routine separately you can use the following code. Make sure to change the block IDs (“A4TeY9” and “PPT2PG”) to the ones in your quiz.
        ```html
        <h3>Let’s start with your morning routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "A4TeY9"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        <br>
        <h3>Finish the day with your night routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "PPT2PG"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        ```


=== "Shopify V2"

    **Using Metadata**

    !!! note

        This guide explains how to use quiz metadata like `answersByBlock`, `recommendationsBySlot`, and `resultContentByBlock` in a Liquid-compatible email template.

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_shopifyv2_sendemails_metadata.png){width="50%"}

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    **Understanding the Data Structure**

    When a customer finishes a quiz, you receive structured metadata with:

    - `firstName`, `fullName`, `email`: basic user info
    - `answersByBlock`: customer’s answers to quiz questions
    - `recommendationsBySlot`: products recommended by the quiz
    - `resultContentByBlock`: dynamic text, tips, and headings from the result page

    **How to Use Metadata in Liquid Templates**

    Display Their First Name: `Hi {{ person.firstName | default: 'there' }},` or `Hi {{ person.answersByBlock.qbi-6c4248f5.value | default: 'there' }},`

    Display Their Answers: `You mentioned your skin is mostly: <strong>{{ person.answersByBlock['qbc-485600ce'].value }}</strong>`

    !!! tip

        You can loop through all answers dynamically too:

        ```liquid
        {% for question_id, block in person.answersByBlock %}
        <p><strong>Answer:</strong> {{ block.value }}</p>
        {% endfor %}
        ```

    Show Recommended Products: If your quiz sends recommended products under `recommendationsBySlot`, you can display them like this:

    ```liquid
    {% assign products = person.recommendationsBySlot['rsbss-ca4fba94'] %}
    {% for product in products %}
    <div style="margin-bottom: 30px;">
        <img src="{{ product.image.url }}" alt="{{ product.title }}" width="200" />
        <h3>{{ product.vendor }} - {{ product.title }}</h3>
        <p>{{ product.description }}</p>
        <p><strong>{{ product.price.amount }} {{ product.price.currencyCode }}</strong></p>
        <a href="https://yourstore.com/products/{{ product.handle }}">Shop now</a>
    </div>
    {% endfor %}
    ```

    Show Custom Headings from Results Page: You can also pull headings or tips from `resultContentByBlock` by using a code like `{{ person.resultContentByBlock['rsbt-159c2a74'].content }}` or loop through result content blocks:

    ```liquid
    {% for block_id, block in person.resultContentByBlock %}
    {% if block.type == 'text' %}
        {{ block.content }}
    {% endif %}
    {% endfor %}
    ```


=== "WooCommerce"

    **Using Metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: If you wish to display the respondent’s name, you can use the `{{first_name}}` handlebar in your code.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```
        
    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Usign Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Builtin Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
    - GitHub Handlebars Helpers: [Handlebars Helpers on GitHub](https://github.com/helpers/handlebars-helpers)

    The format for helpers in Notifications might slightly differ from those on GitHub. For instance, to truncate a product name to 7 characters, you should write:

    ```handlebars
    {{truncate product.name 7}}
    ```

    If you want to present specific metadata you should use a special property `{{#eq}} ... {{/eq}}`

    - To target all slot blocks:

    ```handlebars
    {{#eq block.type "SlotsBlock"}} ... {{/eq}}
    ```

    - To target a specific block, for example, a block with the ID `A4TeY9`:

    ```handlebars
    {{#eq block.id "A4TeY9"}} … {{/eq}}
    ```

    Specific use cases:

    - **List the Recommended Products**: If you want to loop through the most recommended products, you can do so like this:
        ```html
            {{#each products as | product |}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        ```

    - **List recommended products with Slot Titles**: If you want to list the most recommended product with Slot titles, you can do so like this:
        ```html
        {{#each blocks as |block|}}
        {{#eq block.type "SlotsBlock"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/each}}
        {{/eq}}
        {{#eq block.type "ProductsBlock"}}
        {{#each block.products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

    - **List recommended products separated by Slot Blocks**: If you want to recommend a Morning and Night slot routine separately you can use the following code. Make sure to change the block IDs (“A4TeY9” and “PPT2PG”) to the ones in your quiz.
        ```html
        <h3>Let’s start with your morning routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "A4TeY9"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        <br>
        <h3>Finish the day with your night routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "PPT2PG"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

=== "Magento"

    **Using Metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: If you wish to display the respondent’s name, you can use the `{{first_name}}` handlebar in your code.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```
        
    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Usign Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Builtin Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
    - GitHub Handlebars Helpers: [Handlebars Helpers on GitHub](https://github.com/helpers/handlebars-helpers)

    The format for helpers in Notifications might slightly differ from those on GitHub. For instance, to truncate a product name to 7 characters, you should write:

    ```handlebars
    {{truncate product.name 7}}
    ```

    If you want to present specific metadata you should use a special property `{{#eq}} ... {{/eq}}`

    - To target all slot blocks:

    ```handlebars
    {{#eq block.type "SlotsBlock"}} ... {{/eq}}
    ```

    - To target a specific block, for example, a block with the ID `A4TeY9`:

    ```handlebars
    {{#eq block.id "A4TeY9"}} … {{/eq}}
    ```

    Specific use cases:

    - **List the Recommended Products**: If you want to loop through the most recommended products, you can do so like this:
        ```html
            {{#each products as | product |}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        ```

    - **List recommended products with Slot Titles**: If you want to list the most recommended product with Slot titles, you can do so like this:
        ```html
        {{#each blocks as |block|}}
        {{#eq block.type "SlotsBlock"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/each}}
        {{/eq}}
        {{#eq block.type "ProductsBlock"}}
        {{#each block.products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

    - **List recommended products separated by Slot Blocks**: If you want to recommend a Morning and Night slot routine separately you can use the following code. Make sure to change the block IDs (“A4TeY9” and “PPT2PG”) to the ones in your quiz.
        ```html
        <h3>Let’s start with your morning routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "A4TeY9"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        <br>
        <h3>Finish the day with your night routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "PPT2PG"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        ```


=== "BigCommerce"

    **Using Metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: If you wish to display the respondent’s name, you can use the `{{first_name}}` handlebar in your code.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```
        
    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Usign Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Builtin Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
    - GitHub Handlebars Helpers: [Handlebars Helpers on GitHub](https://github.com/helpers/handlebars-helpers)

    The format for helpers in Notifications might slightly differ from those on GitHub. For instance, to truncate a product name to 7 characters, you should write:

    ```handlebars
    {{truncate product.name 7}}
    ```

    If you want to present specific metadata you should use a special property `{{#eq}} ... {{/eq}}`

    - To target all slot blocks:

    ```handlebars
    {{#eq block.type "SlotsBlock"}} ... {{/eq}}
    ```

    - To target a specific block, for example, a block with the ID `A4TeY9`:

    ```handlebars
    {{#eq block.id "A4TeY9"}} … {{/eq}}
    ```

    Specific use cases:

    - **List the Recommended Products**: If you want to loop through the most recommended products, you can do so like this:
        ```html
            {{#each products as | product |}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        ```

    - **List recommended products with Slot Titles**: If you want to list the most recommended product with Slot titles, you can do so like this:
        ```html
        {{#each blocks as |block|}}
        {{#eq block.type "SlotsBlock"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/each}}
        {{/eq}}
        {{#eq block.type "ProductsBlock"}}
        {{#each block.products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

    - **List recommended products separated by Slot Blocks**: If you want to recommend a Morning and Night slot routine separately you can use the following code. Make sure to change the block IDs (“A4TeY9” and “PPT2PG”) to the ones in your quiz.
        ```html
        <h3>Let’s start with your morning routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "A4TeY9"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        <br>
        <h3>Finish the day with your night routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "PPT2PG"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        ```


=== "Standalone"

    **Using Metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: If you wish to display the respondent’s name, you can use the `{{first_name}}` handlebar in your code.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```
        
    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Usign Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Builtin Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
    - GitHub Handlebars Helpers: [Handlebars Helpers on GitHub](https://github.com/helpers/handlebars-helpers)

    The format for helpers in Notifications might slightly differ from those on GitHub. For instance, to truncate a product name to 7 characters, you should write:

    ```handlebars
    {{truncate product.name 7}}
    ```

    If you want to present specific metadata you should use a special property `{{#eq}} ... {{/eq}}`

    - To target all slot blocks:

    ```handlebars
    {{#eq block.type "SlotsBlock"}} ... {{/eq}}
    ```

    - To target a specific block, for example, a block with the ID `A4TeY9`:

    ```handlebars
    {{#eq block.id "A4TeY9"}} … {{/eq}}
    ```

    Specific use cases:

    - **List the Recommended Products**: If you want to loop through the most recommended products, you can do so like this:
        ```html
            {{#each products as | product |}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        ```

    - **List recommended products with Slot Titles**: If you want to list the most recommended product with Slot titles, you can do so like this:
        ```html
        {{#each blocks as |block|}}
        {{#eq block.type "SlotsBlock"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/each}}
        {{/eq}}
        {{#eq block.type "ProductsBlock"}}
        {{#each block.products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

    - **List recommended products separated by Slot Blocks**: If you want to recommend a Morning and Night slot routine separately you can use the following code. Make sure to change the block IDs (“A4TeY9” and “PPT2PG”) to the ones in your quiz.
        ```html
        <h3>Let’s start with your morning routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "A4TeY9"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        <br>
        <h3>Finish the day with your night routine</h3>
        {{#each blocks as |block|}}
        {{#eq block.id "PPT2PG"}}
        {{#each block.slots as |slot|}}
        <b>{{slot.title}}</b><br>
        {{#each products as |product|}}
        <div style="overflow:hidden; margin-bottom: 10px;">
        <img src="{{product.image_url}}" alt="{{product.name}}" width="48" height="48" style="float:left; margin-right: 10px;"/>
        <span style="height:48px;float:left">
        <a href="{{product.url}}" target="_blank">{{product.name}}</a>
        <br>{{product.price}} USD</span>
        </div>
        {{/each}} 
        {{/each}}
        {{/eq}}
        {{/each}}
        ```

---
By folowing this guide, you'll learn how to set up result emails for your Product Recommendation Quiz.