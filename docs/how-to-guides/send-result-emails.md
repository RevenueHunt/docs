---
icon: material/email-heart-outline
description: "Complete guide to setting up RevenueHunt quiz result emails and admin notifications."
---

# Setting Up Result Emails with Product Recommendation Quiz

A result email brings the customer back to their recommendations, which recovers sales that would otherwise be lost. The RevenueHunt app sends these emails itself, so you do not need an external CRM service, though you can use one.

This article covers the email your [customer receives](#email-quiz-results-via-revenuehunt-app), the notification your [administrators receive](#activate-email-notifications-to-admin), and sending result emails through an [external CRM service](/how-to-guides/send-leads-to-crm/).

!!! tip "Two kinds of email"

    The app sends two kinds of email:

    - The result email your customer receives, holding their answers and recommendations.
    - A notification to an address you choose, on every quiz completion.


!!! tip "Recommended: send from your own address"

    Result emails leave from the RevenueHunt servers by default. [Connect your own SMTP server](/how-to-guides/send-result-emails-from-custom-server/) to send them from your own address instead. Deliverability improves, and the email carries your branding.



## Email quiz results via RevenueHunt app

Result emails can be sent directly from the RevenueHunt app to the email provided by the customer.

Follow the instructions below to activate and edit the result emails the app sends:

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/3AWbHe1aTac?si=vBYdeOUlrVtb5m6H" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add an email question**: your quiz needs one before it can send a result email. Add it in the [Quiz builder](/reference/quiz-builder/questions/).
    2. **Activate the customer email**: go to [`Quiz settings > Emails to respondents`](/reference/quiz-builder/notifications/#to-respondent) and check `Send email when someone completes the quiz`.
        ![how to activate to respondent emails](/images/manual_shopifyV2_quizbuilder_notification_torespondent.png)
    3. **Email TO**: choose which email question supplies the address to send to.
    4. **Edit REPLY-TO**: choose the address your customer replies to.
    5. **Email Subject**: edit the title of the email your customer receives.
    6. **Edit Email Content**: set up the template for that email.

        ![how to send result emails html template](https://loom.com/i/200e22c07c214de2a399b481d7720c80?workflows_screenshot=true)

        !!! warning
            Editing the email template takes HTML and Liquid.

        - Personalize the email with quiz metadata such as `{{first_name}}`. Liquid can loop through the recommended products, or change the content based on the quiz outcome.

        - The template reads the quiz metadata: the response ID, the quiz name, the customer's details, their answers, tags, recommended products and results page content.

            !!! tip

                See [Editing email templates](#editing-email-templates) for the full list.

        - Ready-made snippets sit under the `Email Liquid Template` field. Use `Responses by Block`, for example, to list the answers.

            !!! tip

                Paste a snippet into a large language model such as ChatGPT or Gemini and ask it to style the Liquid template for you.


        !!! note
            Email clients render HTML differently, so write your styles inline rather than as classes. JavaScript does not run in an email client, so leave it out. See [Editing email templates](#editing-email-templates).


    7. **Add your SMTP credentials (recommended)**: result emails leave from the RevenueHunt servers by default. Connect your own instead, for better deliverability and your own branding. Go to [`App settings > SMTP settings`](/reference/app-settings/#smtp) and enter your credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        !!! note

            SMTP, or Simple Mail Transfer Protocol, is the protocol that lets an app such as RevenueHunt send email through your own mail server.

            Connect the app to your SMTP server and the result emails leave from your own account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**
    8. **Save the changes**: click the top-right `Save` button to update the preview and the live quiz.
    9. **Preview the quiz**: take it through to the results page, which triggers the email.



=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP, or Simple Mail Transfer Protocol, is the protocol that lets an app such as RevenueHunt send email through your own mail server.

            Connect the app to your SMTP server and the result emails leave from your own account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Add an email question**: your quiz needs one before it can send a result email. Add it in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the customer email**: go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: choose the address your customer replies to.
    5. **Email TO**: with more than one email question in the quiz, choose which one supplies the address. With only one, it is selected for you.
    6. **Email Subject**: edit the subject line your customer sees. Type `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name.
    7. **Edit Email Content**: set up the email your customer receives. Choose either the **Basic (text)** or the **Advanced (HTML)** format, and switch between them with `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - The **Basic text** template is the simpler one. Type what the customer should read into the `Email Text Message` field. Type `@` to pull in [recalled information](/how-to-guides/use-information-recalls/): the customer name, email, phone number, quiz name, their answers, the recommended products and more. It cannot show images or colors, but it has the best deliverability.
        ![how to send result emails basic template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - The **Advanced HTML** template takes HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to edit. Personalize it with quiz metadata such as `{{first_name}}`, and use Handlebars to loop through the recommended products or change the content by quiz outcome. Email clients render HTML differently, so write your styles inline rather than as classes. JavaScript does not run in an email client, so leave it out. See [Editing email templates](#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.


=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP, or Simple Mail Transfer Protocol, is the protocol that lets an app such as RevenueHunt send email through your own mail server.

            Connect the app to your SMTP server and the result emails leave from your own account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Add an email question**: your quiz needs one before it can send a result email. Add it in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the customer email**: go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: choose the address your customer replies to.
    5. **Email TO**: with more than one email question in the quiz, choose which one supplies the address. With only one, it is selected for you.
    6. **Email Subject**: edit the subject line your customer sees. Type `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name.
    7. **Edit Email Content**: set up the email your customer receives. Choose either the **Basic (text)** or the **Advanced (HTML)** format, and switch between them with `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - The **Basic text** template is the simpler one. Type what the customer should read into the `Email Text Message` field. Type `@` to pull in [recalled information](/how-to-guides/use-information-recalls/): the customer name, email, phone number, quiz name, their answers, the recommended products and more. It cannot show images or colors, but it has the best deliverability.
        ![how to send result emails basic template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - The **Advanced HTML** template takes HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to edit. Personalize it with quiz metadata such as `{{first_name}}`, and use Handlebars to loop through the recommended products or change the content by quiz outcome. Email clients render HTML differently, so write your styles inline rather than as classes. JavaScript does not run in an email client, so leave it out. See [Editing email templates](#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.


=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP, or Simple Mail Transfer Protocol, is the protocol that lets an app such as RevenueHunt send email through your own mail server.

            Connect the app to your SMTP server and the result emails leave from your own account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Add an email question**: your quiz needs one before it can send a result email. Add it in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the customer email**: go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: choose the address your customer replies to.
    5. **Email TO**: with more than one email question in the quiz, choose which one supplies the address. With only one, it is selected for you.
    6. **Email Subject**: edit the subject line your customer sees. Type `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name.
    7. **Edit Email Content**: set up the email your customer receives. Choose either the **Basic (text)** or the **Advanced (HTML)** format, and switch between them with `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - The **Basic text** template is the simpler one. Type what the customer should read into the `Email Text Message` field. Type `@` to pull in [recalled information](/how-to-guides/use-information-recalls/): the customer name, email, phone number, quiz name, their answers, the recommended products and more. It cannot show images or colors, but it has the best deliverability.
        ![how to send result emails basic template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - The **Advanced HTML** template takes HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to edit. Personalize it with quiz metadata such as `{{first_name}}`, and use Handlebars to loop through the recommended products or change the content by quiz outcome. Email clients render HTML differently, so write your styles inline rather than as classes. JavaScript does not run in an email client, so leave it out. See [Editing email templates](#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.


=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP, or Simple Mail Transfer Protocol, is the protocol that lets an app such as RevenueHunt send email through your own mail server.

            Connect the app to your SMTP server and the result emails leave from your own account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Add an email question**: your quiz needs one before it can send a result email. Add it in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the customer email**: go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: choose the address your customer replies to.
    5. **Email TO**: with more than one email question in the quiz, choose which one supplies the address. With only one, it is selected for you.
    6. **Email Subject**: edit the subject line your customer sees. Type `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name.
    7. **Edit Email Content**: set up the email your customer receives. Choose either the **Basic (text)** or the **Advanced (HTML)** format, and switch between them with `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - The **Basic text** template is the simpler one. Type what the customer should read into the `Email Text Message` field. Type `@` to pull in [recalled information](/how-to-guides/use-information-recalls/): the customer name, email, phone number, quiz name, their answers, the recommended products and more. It cannot show images or colors, but it has the best deliverability.
        ![how to send result emails basic template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - The **Advanced HTML** template takes HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to edit. Personalize it with quiz metadata such as `{{first_name}}`, and use Handlebars to loop through the recommended products or change the content by quiz outcome. Email clients render HTML differently, so write your styles inline rather than as classes. JavaScript does not run in an email client, so leave it out. See [Editing email templates](#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP, or Simple Mail Transfer Protocol, is the protocol that lets an app such as RevenueHunt send email through your own mail server.

            Connect the app to your SMTP server and the result emails leave from your own account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Add an email question**: your quiz needs one before it can send a result email. Add it in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the customer email**: go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![how to activate to respondent emails](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: choose the address your customer replies to.
    5. **Email TO**: with more than one email question in the quiz, choose which one supplies the address. With only one, it is selected for you.
    6. **Email Subject**: edit the subject line your customer sees. Type `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name.
    7. **Edit Email Content**: set up the email your customer receives. Choose either the **Basic (text)** or the **Advanced (HTML)** format, and switch between them with `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - The **Basic text** template is the simpler one. Type what the customer should read into the `Email Text Message` field. Type `@` to pull in [recalled information](/how-to-guides/use-information-recalls/): the customer name, email, phone number, quiz name, their answers, the recommended products and more. It cannot show images or colors, but it has the best deliverability.
        ![how to send result emails basic template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - The **Advanced HTML** template takes HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to edit. Personalize it with quiz metadata such as `{{first_name}}`, and use Handlebars to loop through the recommended products or change the content by quiz outcome. Email clients render HTML differently, so write your styles inline rather than as classes. JavaScript does not run in an email client, so leave it out. See [Editing email templates](#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.

## Sending result emails with your CRM

Your own CRM can send the result emails instead. Connect your quiz to one of the [available integrations](/how-to-guides/send-leads-to-crm/), and the quiz data reaches your CRM as soon as the customer sees the results page. You then build the email sequence in the CRM itself, following that service's own guide.

## Activate email notifications to admin

The app can email you every time someone completes the quiz or goes through to the checkout. Send it to whichever address should track the quiz.

!!! tip "Recommended: send from your own address"

    Notification emails leave from the RevenueHunt servers by default. [Connect your own SMTP server](/how-to-guides/send-result-emails-from-custom-server/) to send them from your own address instead, which improves deliverability.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/XdPgnR8W4fg?si=TivtkA2wCiHaFQYg" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Activate Emails to self**: go to [`Quiz settings > Emails to self`](/reference/quiz-builder/notifications/#to-self) and check the `Receive an email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_shopifyV2_quizbuilder_notification_toself.png)
    2. **Edit Email to**: choose which address receives the notification, such as a company or a personal one.
    3. **Edit Email Subject**: edit the subject line of the notification.
    4. **Edit Email Content**: edit the Liquid template for the notification you receive.

        - The default liquid template includes all customer answers from the quiz. You can edit this template to include additional information.
        - Use provided `useful code snippets` to add personal information from users. To add personal information, click to copy the template snippet and paste it at the top of your email liquid template.

        - You can always reset the email template to default settings.

    5. **Add your SMTP credentials (recommended)**: notification emails leave from the RevenueHunt servers by default. Connect your own instead, for better deliverability and your own branding. Go to [`App settings > SMTP settings`](/reference/app-settings/#smtp) and enter your credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**
    6. **Save the changes**: click the top `Save` button.
    7. **Preview the quiz**: take it through to the results page, which triggers the notification.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Open Notifications**: go to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate the notifications**: toggle the button. Choose an email on each quiz completion, on each cart or checkout, or both.
        ![how to send result emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. **Add your email address in the `Send email notification to` field.**
    4. **Publish the changes**: click the top-right `Publish` button.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Open Notifications**: go to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate the notifications**: toggle the button. Choose an email on each quiz completion, on each cart or checkout, or both.
        ![how to send result emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. **Add your email address in the `Send email notification to` field.**
    4. **Publish the changes**: click the top-right `Publish` button.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Open Notifications**: go to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate the notifications**: toggle the button. Choose an email on each quiz completion, on each cart or checkout, or both.
        ![how to send result emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. **Add your email address in the `Send email notification to` field.**
    4. **Publish the changes**: click the top-right `Publish` button.

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Open Notifications**: go to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate the notifications**: toggle the button. Choose an email on each quiz completion, on each cart or checkout, or both.
        ![how to send result emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. **Add your email address in the `Send email notification to` field.**
    4. **Publish the changes**: click the top-right `Publish` button.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add your SMTP credentials**: go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. Follow [how to send result emails from your server using SMTP](/how-to-guides/send-result-emails-from-custom-server/) to learn how to set this up.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are unsure what credentials to use, search your email provider's documentation for `SMTP`, or ask their support team.**

    2. **Open Notifications**: go to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate the notifications**: toggle the button. Choose an email on each quiz completion, on each cart or checkout, or both.
        ![how to send result emails to self](/images/manual_quizbuilder_notifications_toself_active.png)
    3. **Add your email address in the `Send email notification to` field.**
    4. **Publish the changes**: click the top-right `Publish` button.


## Editing email templates

=== "Shopify"

    **Using metadata**

    !!! note

        This guide explains how to use quiz metadata like `answersByBlock`, `recommendationsBySlot`, and `resultContentByBlock` in a Liquid-compatible email template.

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_shopifyv2_sendemails_metadata.png){width="50%"}

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    **Understanding the data structure**

    When a customer finishes a quiz, you receive structured metadata with:

    - `firstName`, `fullName`, `email`: basic user info
    - `answersByBlock`: customer's answers to quiz questions
    - `recommendationsBySlot`: products recommended by the quiz
    - `resultContentByBlock`: dynamic text, tips, and headings from the results page



    !!! info "Quiz Response Metadata Structure"

        ![manual_shopifyV2_quizbuilder_notification_metadata](/images/manual_shopifyV2_quizbuilder_notification_metadata.png){width=50%}

        This object holds everything a quiz completion generates: the answers, the product recommendations and the result content. It drives the results page, the follow-up emails and any custom workflow.

        ---

        **Basic information**

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

        `tags` - The tags assigned to the customer, often used for segmentation. Empty when none are set.

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

        `slotHeading / slotDescription` - Rich text HTML displayed on results pages

        `image` - URL for the main product image

        `price` - Object with `amount` and `currencyCode`

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


    **Using metadata in a Liquid template**

    Display Their First Name: `Hi {{ person.firstName | default: 'there' }},` or `Hi {{ person.answersByBlock.qbi-6c4248f5.value | default: 'there' }},`

    Display Their Answers: `You mentioned your skin is mostly: <strong>{{ person.answersByBlock['qbc-485600ce'].value }}</strong>`

    !!! tip

        You can loop through all answers dynamically too:

        ```liquid
        {% for question_id, block in person.answersByBlock %}
        <p><strong>Answer:</strong> {{ block.value }}</p>
        {% endfor %}
        ```

    Show a link to the quiz results page: add `#response-{{ responseId }}` to the end of your results page URL.

    ```liquid
    <a href="https://yourwebsite.com/#response-{{ responseId }}">View your quiz results</a>
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

    Show Custom Headings from Results page: You can also pull headings or tips from `resultContentByBlock` by using a code like `{{ person.resultContentByBlock['rsbt-159c2a74'].content }}` or loop through result content blocks:

    ```liquid
    {% for block_id, block in person.resultContentByBlock %}
    {% if block.type == 'text' %}
        {{ block.content }}
    {% endif %}
    {% endfor %}
    ```



=== "Shopify (Legacy)"

    **Using metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: use the `{{first_name}}` handlebar to display the customer's name.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```

    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Using Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Built-in Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
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

    - **List recommended products separated by Slot Blocks**: use this code to recommend a Morning and a Night routine separately. Change the block IDs `A4TeY9` and `PPT2PG` to the ones in your quiz.
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


=== "WooCommerce"

    **Using metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: use the `{{first_name}}` handlebar to display the customer's name.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```

    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Using Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Built-in Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
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

    - **List recommended products separated by Slot Blocks**: use this code to recommend a Morning and a Night routine separately. Change the block IDs `A4TeY9` and `PPT2PG` to the ones in your quiz.
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

    **Using metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: use the `{{first_name}}` handlebar to display the customer's name.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```

    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Using Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Built-in Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
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

    - **List recommended products separated by Slot Blocks**: use this code to recommend a Morning and a Night routine separately. Change the block IDs `A4TeY9` and `PPT2PG` to the ones in your quiz.
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

    **Using metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: use the `{{first_name}}` handlebar to display the customer's name.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```

    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Using Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Built-in Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
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

    - **List recommended products separated by Slot Blocks**: use this code to recommend a Morning and a Night routine separately. Change the block IDs `A4TeY9` and `PPT2PG` to the ones in your quiz.
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

    **Using metadata**

    Each quiz response has metadata which can be used in your emails to personalize them. You can see the `metadata` from the quiz response on the right hand side of each notification:

    ![how to send result emails metadata](/images/how_to_send_result_emails_metadata.png)

    The metadata from a quiz response can include various details that are useful for personalizing email communications.

    For example:

    - **Show Customer Name**: use the `{{first_name}}` handlebar to display the customer's name.
        ```html
        <p>Hello {{first_name}},</p>
        ```

        It should render as:

        ```
        Hello Alex,
        ```

    - **Recommended Products in Metadata**: The most recommended products are listed within the metadata JSON under the `products` property.

    **Using Handlebars**

    You can use Handlebars to add more functionality to your HTML email template.

    For more detailed guidance on using handlebars in your HTML email templates, refer to the following resources:

    - Handlebars Built-in Helpers: [Handlebars Built-in Helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
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

    - **List recommended products separated by Slot Blocks**: use this code to recommend a Morning and a Night routine separately. Change the block IDs `A4TeY9` and `PPT2PG` to the ones in your quiz.
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
This article explains how the RevenueHunt app sends result emails to your customers, and notifications to an address you choose.