---
icon: material/numeric-5
description: "Send automated quiz result emails and connect your SMTP email server with the RevenueHunt app for customer notifications."
---

# Sending Emails with the RevenueHunt App


=== "Shopify"


    In this tutorial you will learn how to send emails to customers and to yourself. It also covers connecting your own email server over SMTP, which stands for Simple Mail Transfer Protocol.

    !!! info "What you will learn"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP,
        - how to style emails with the help of AI tools.


    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/yQJBaheRWgw?si=NaiYYKOovWwDXlV4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


=== "Shopify (Legacy)"

    In this tutorial you will learn how to send emails to customers and to yourself. It also covers connecting your own email server over SMTP, which stands for Simple Mail Transfer Protocol.

    !!! info "What you will learn"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "WooCommerce"

    In this tutorial you will learn how to send emails to customers and to yourself. It also covers connecting your own email server over SMTP, which stands for Simple Mail Transfer Protocol.

    !!! info "What you will learn"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "Magento"

    In this tutorial you will learn how to send emails to customers and to yourself. It also covers connecting your own email server over SMTP, which stands for Simple Mail Transfer Protocol.

    !!! info "What you will learn"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "BigCommerce"

    In this tutorial you will learn how to send emails to customers and to yourself. It also covers connecting your own email server over SMTP, which stands for Simple Mail Transfer Protocol.

    !!! info "What you will learn"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "Standalone"

    In this tutorial you will learn how to send emails to customers and to yourself. It also covers connecting your own email server over SMTP, which stands for Simple Mail Transfer Protocol.

    !!! info "What you will learn"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.





## Sending emails to customers


=== "Shopify"


    1. **Add an email question.** Your quiz needs an [email question](/reference/quiz-builder/questions/#email-address) before you set up result emails. Go to [Quiz builder > Questions](/reference/quiz-builder/questions/) and click `+ Add question` or `+ Add block`.
    2. **Activate the email to customers.** Go to [`Quiz settings > Emails to respondents`](/reference/quiz-builder/notifications/#to-respondent) and check `Send email when someone completes the quiz`.
        ![Emails to respondents setting activated](/images/manual_shopifyV2_quizbuilder_notification_torespondent.png)
    3. **Set `Email TO`.** Choose which email question supplies the address that the result email is sent to.
    4. **Set `REPLY-TO`.** Choose the address that the customer replies to.
    5. **Set the `Email Subject`.** Edit the title of the email that customers will receive.
    6. **Build the `Email Liquid Template`.** Configure the email template of the email that your customers will receive.

        ![how to send result emails html template](https://loom.com/i/200e22c07c214de2a399b481d7720c80?workflows_screenshot=true)

        !!! warning
            Email template requires the knowledge of HTML and Liquid to be edited.

        - Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Liquid code to loop through and display recommended products or customize content based on quiz outcomes.

        - The email Liquid template recalls quiz information through metadata. That covers the response ID, the quiz name, the customer's name and email, the answers, tags, recommended products and results page content.

            !!! tip

                To learn more about the metadata, see [Editing email templates](/how-to-guides/send-result-emails/#editing-email-templates).

        - The `Email Liquid Template` field has *useful code snippets* below it. Use them to insert quiz data, such as the `Responses by Block` snippet that lists the answers.

            !!! tip

                You can copy the useful code snippets and paste them into a large language model like ChatGPT or Gemini to style the Liquid email template.


        !!! note
            HTML emails do not render the same way in every email client, so add styles inline rather than as classes. Email clients do not run JavaScript, so JavaScript code has no effect. Read more in [Editing email templates](/how-to-guides/send-result-emails/#editing-email-templates).

    7. **Check the email preview.** Use the Email preview section to see how the email looks for different customers.
    8. **Add your SMTP credentials (recommended).** Check [Sending Emails from Your Servers (SMTP)](#sending-emails-from-your-servers-smtp) to learn how to connect your own email server using SMTP.
    9. **Save the changes.** Remember to save the changes with the top-right `Save` button to update the preview/live quiz.
    10. **Preview the quiz**: Return to the dashboard and preview the quiz. Complete the quiz all the way to the results page to trigger the email notification.



=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            Once the RevenueHunt app is connected to your SMTP server, the follow-up emails with quiz results are sent from your own email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Add Email Question**: Your quiz needs an email question before you set up result emails. Add one in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the email to customers.** Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![Emails to respondents setting activated](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they receive the results.
    5. **Email TO**: Choose which email question supplies the address. With only one email question in the quiz, it is selected for you.
    6. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    7. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template. Type the text you want the customer to see in the `Email Text Message` field. Add dynamic elements with `@`, or with an [Information Recall](/how-to-guides/use-information-recalls/), to pull in the customer name, email, phone number, quiz name, answers and recommended products. The basic template shows no images and no color, and has the best deliverability.
        ![Basic text email template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template. Editing it needs HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers). Use quiz response metadata such as `{{first_name}}` to personalize an email, and use Handlebars to loop over recommended products. HTML emails do not render the same way in every email client, so add styles inline rather than as classes. Email clients do not run JavaScript. Read more in [Editing Email Templates](/how-to-guides/send-result-emails/#editing-email-templates).
        ![Advanced HTML email template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: Publish the changes with the top-right `Publish` button to update the preview and the live quiz.


=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            Once the RevenueHunt app is connected to your SMTP server, the follow-up emails with quiz results are sent from your own email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Add Email Question**: Your quiz needs an email question before you set up result emails. Add one in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the email to customers.** Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![Emails to respondents setting activated](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they receive the results.
    5. **Email TO**: Choose which email question supplies the address. With only one email question in the quiz, it is selected for you.
    6. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    7. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template. Type the text you want the customer to see in the `Email Text Message` field. Add dynamic elements with `@`, or with an [Information Recall](/how-to-guides/use-information-recalls/), to pull in the customer name, email, phone number, quiz name, answers and recommended products. The basic template shows no images and no color, and has the best deliverability.
        ![Basic text email template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template. Editing it needs HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers). Use quiz response metadata such as `{{first_name}}` to personalize an email, and use Handlebars to loop over recommended products. HTML emails do not render the same way in every email client, so add styles inline rather than as classes. Email clients do not run JavaScript. Read more in [Editing Email Templates](/how-to-guides/send-result-emails/#editing-email-templates).
        ![Advanced HTML email template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: Publish the changes with the top-right `Publish` button to update the preview and the live quiz.


=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            Once the RevenueHunt app is connected to your SMTP server, the follow-up emails with quiz results are sent from your own email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Add Email Question**: Your quiz needs an email question before you set up result emails. Add one in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the email to customers.** Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![Emails to respondents setting activated](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they receive the results.
    5. **Email TO**: Choose which email question supplies the address. With only one email question in the quiz, it is selected for you.
    6. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    7. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template. Type the text you want the customer to see in the `Email Text Message` field. Add dynamic elements with `@`, or with an [Information Recall](/how-to-guides/use-information-recalls/), to pull in the customer name, email, phone number, quiz name, answers and recommended products. The basic template shows no images and no color, and has the best deliverability.
        ![Basic text email template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template. Editing it needs HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers). Use quiz response metadata such as `{{first_name}}` to personalize an email, and use Handlebars to loop over recommended products. HTML emails do not render the same way in every email client, so add styles inline rather than as classes. Email clients do not run JavaScript. Read more in [Editing Email Templates](/how-to-guides/send-result-emails/#editing-email-templates).
        ![Advanced HTML email template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: Publish the changes with the top-right `Publish` button to update the preview and the live quiz.


=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            Once the RevenueHunt app is connected to your SMTP server, the follow-up emails with quiz results are sent from your own email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Add Email Question**: Your quiz needs an email question before you set up result emails. Add one in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the email to customers.** Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![Emails to respondents setting activated](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they receive the results.
    5. **Email TO**: Choose which email question supplies the address. With only one email question in the quiz, it is selected for you.
    6. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    7. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template. Type the text you want the customer to see in the `Email Text Message` field. Add dynamic elements with `@`, or with an [Information Recall](/how-to-guides/use-information-recalls/), to pull in the customer name, email, phone number, quiz name, answers and recommended products. The basic template shows no images and no color, and has the best deliverability.
        ![Basic text email template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template. Editing it needs HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers). Use quiz response metadata such as `{{first_name}}` to personalize an email, and use Handlebars to loop over recommended products. HTML emails do not render the same way in every email client, so add styles inline rather than as classes. Email clients do not run JavaScript. Read more in [Editing Email Templates](/how-to-guides/send-result-emails/#editing-email-templates).
        ![Advanced HTML email template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: Publish the changes with the top-right `Publish` button to update the preview and the live quiz.


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            Once the RevenueHunt app is connected to your SMTP server, the follow-up emails with quiz results are sent from your own email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Add Email Question**: Your quiz needs an email question before you set up result emails. Add one in the [Quiz Builder](/reference/quiz-builder/questions/).
    3. **Activate the email to customers.** Go to [`Notifications > TO RESPONDENT`](/reference/quiz-builder/notifications/#to-respondent) and toggle `Send email when someone completes the quiz`.
        ![Emails to respondents setting activated](/images/manual_quizbuilder_notifications_torespondent_active.png)
    4. **Edit REPLY-TO**: Choose what email the customers will be able to reply to once they receive the results.
    5. **Email TO**: Choose which email question supplies the address. With only one email question in the quiz, it is selected for you.
    6. **Email Subject**: Edit the title of the email that customers will receive. You can use `@` to [recall information](/how-to-guides/use-information-recalls/) such as the customer name or the quiz name in the title field.
    7. **Edit Email Content**: Configure the email your customers will receive. You can choose between a **Basic (text)** email format or **Advanced (HTML)** email format. You can switch between the two by clicking `switch to advanced HTML message` or `switch to basic text message` in the `Email Text Message` field.
        - **Basic text** email template. Type the text you want the customer to see in the `Email Text Message` field. Add dynamic elements with `@`, or with an [Information Recall](/how-to-guides/use-information-recalls/), to pull in the customer name, email, phone number, quiz name, answers and recommended products. The basic template shows no images and no color, and has the best deliverability.
        ![Basic text email template](/images/manual_quizbuilder_notifications_torespondent_active_basic.png)
        - **Advanced HTML** email template. Editing it needs HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers). Use quiz response metadata such as `{{first_name}}` to personalize an email, and use Handlebars to loop over recommended products. HTML emails do not render the same way in every email client, so add styles inline rather than as classes. Email clients do not run JavaScript. Read more in [Editing Email Templates](/how-to-guides/send-result-emails/#editing-email-templates).
        ![Advanced HTML email template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    8. **Publish the changes**: Publish the changes with the top-right `Publish` button to update the preview and the live quiz.




## Sending emails to yourself


=== "Shopify"


    1. **Activate the email to yourself.** Go to [`Quiz settings > Emails to self`](/reference/quiz-builder/notifications/#to-self) and check `Receive an email when someone completes the quiz`.
        ![Emails to self setting activated](/images/manual_shopifyV2_quizbuilder_notification_toself.png)
    2. **Set the address that receives it.** Choose the address that receives the notification, such as a company or personal email.
    3. **Set the `Email Subject`.** Edit the subject line of the notification email.
    4. **Build the `Email Liquid Template`.** Configure the email you receive. Edit the Liquid email template.

        - The default Liquid template includes all customer answers from the quiz. You can edit this template to include additional information.
        - Use the `useful code snippets` to add customer information. Click a snippet to copy it, then paste it at the top of your email Liquid template.

            !!! tip

                You can copy the useful code snippets and paste them into a large language model like ChatGPT or Gemini to style the Liquid email template.


        - You can always reset the email template to default settings.

    5. **Email Preview**: Use the Email preview section to see how the email looks for different customers.
    6. **`Recommended` Add Your SMTP Credentials**: To connect your own email server, see [Sending Emails from Your Servers (SMTP)](#sending-emails-from-your-servers-smtp).
    7. **Save the changes**: Save the changes with the top `Save` button.
    8. **Preview the quiz**: Return to the dashboard and preview the quiz. Complete it all the way to the results page to trigger the email notification.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate Notifications**: Toggle the button to activate the emails. You can get an email for each quiz completion, and for each cart or checkout.
        ![Emails to self setting activated](/images/manual_quizbuilder_notifications_toself_active.png)
    4. **Add your email address in the `Send email notification to` field.**
    5. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate Notifications**: Toggle the button to activate the emails. You can get an email for each quiz completion, and for each cart or checkout.
        ![Emails to self setting activated](/images/manual_quizbuilder_notifications_toself_active.png)
    4. **Add your email address in the `Send email notification to` field.**
    5. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate Notifications**: Toggle the button to activate the emails. You can get an email for each quiz completion, and for each cart or checkout.
        ![Emails to self setting activated](/images/manual_quizbuilder_notifications_toself_active.png)
    4. **Add your email address in the `Send email notification to` field.**
    5. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate Notifications**: Toggle the button to activate the emails. You can get an email for each quiz completion, and for each cart or checkout.
        ![Emails to self setting activated](/images/manual_quizbuilder_notifications_toself_active.png)
    4. **Add your email address in the `Send email notification to` field.**
    5. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Your SMTP Credentials**: Go to [`App Settings > SMTP`](/reference/app-settings/#smtp) and enter your SMTP credentials. See [how to send result emails from your own server](/how-to-guides/send-result-emails-from-custom-server/) for the setup.

        ![manual_appsettings_smtp](/images/manual_appsettings_smtp.png)

        !!! note

            SMTP stands for Simple Mail Transfer Protocol. SMTP is a connection protocol that enables third-party apps (e.g. RevenueHunt) to send emails through your email server.

            When you connect the RevenueHunt app to your SMTP Server, the notification emails to admin will be sent from your email account.

            **If you are not sure which credentials to use, check your email provider's documentation for "SMTP", or contact their support.**

    2. **Open Notifications**: Navigate to [`Notifications > TO SELF`](/reference/quiz-builder/notifications/#to-self) in your quiz dashboard.
    3. **Activate Notifications**: Toggle the button to activate the emails. You can get an email for each quiz completion, and for each cart or checkout.
        ![Emails to self setting activated](/images/manual_quizbuilder_notifications_toself_active.png)
    4. **Add your email address in the `Send email notification to` field.**
    5. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button.




## Sending emails from your servers (SMTP)


=== "Shopify"

    1. **Open [App settings](/reference/app-settings/) from the side menu.**
    2. **Open [`SMTP settings`](/reference/app-settings/#smtp).**
    3. **Fill in your SMTP server details.**

        SMTP credentials vary by email provider. To find yours:

        - Check your email provider's documentation by searching for `SMTP`.
        - See [Specific SMTP configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email providers.
        - Contact your email provider's support team for assistance.

        Fill in the following fields:

        ![how to set up smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.
        - `SMTP Authentication`: pick your provider's method from the dropdown, usually `plain`.
        - `Encryption`: choose `STARTTLS` or `SSL/TLS`, whichever your provider asks for. STARTTLS usually runs on port 587, and SSL/TLS on port 465.

        !!! note

            If you are not sure what to enter, contact your email service provider or search their documentation for `SMTP`.

    4. **Click `Test connection`.** The app sends a test email and reports `SMTP connection successful`, with the subject, the recipient and the timestamp.

        If the test fails, check every credential again, the port first. See the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

        ![A successful SMTP connection test](/images/how_to_shopifyv2_smtp_success.png)

    5. **Tick `Enable sending emails using your own SMTP server`.** The checkbox stays greyed out until a test passes. From then on, both quiz emails leave your own server rather than the RevenueHunt one.




=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open [App Settings](/reference/app-settings/) from your quiz dashboard.**
    2. **Open the [`SMTP`](/reference/app-settings/#smtp) tab.**

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Fill in your SMTP server details.**

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are not sure what to enter, contact your email service provider or search their documentation for `SMTP`.

    4. **Test and Activate**: Click `test connection & activate`. Once the test passes, all emails are sent from your server.

        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open [App Settings](/reference/app-settings/) from your quiz dashboard.**
    2. **Open the [`SMTP`](/reference/app-settings/#smtp) tab.**

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Fill in your SMTP server details.**

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are not sure what to enter, contact your email service provider or search their documentation for `SMTP`.

    4. **Test and Activate**: Click `test connection & activate`. Once the test passes, all emails are sent from your server.

        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open [App Settings](/reference/app-settings/) from your quiz dashboard.**
    2. **Open the [`SMTP`](/reference/app-settings/#smtp) tab.**

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Fill in your SMTP server details.**

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are not sure what to enter, contact your email service provider or search their documentation for `SMTP`.

    4. **Test and Activate**: Click `test connection & activate`. Once the test passes, all emails are sent from your server.

        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open [App Settings](/reference/app-settings/) from your quiz dashboard.**
    2. **Open the [`SMTP`](/reference/app-settings/#smtp) tab.**

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Fill in your SMTP server details.**

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are not sure what to enter, contact your email service provider or search their documentation for `SMTP`.

    4. **Test and Activate**: Click `test connection & activate`. Once the test passes, all emails are sent from your server.

        If there are errors, see the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open [App Settings](/reference/app-settings/) from your quiz dashboard.**
    2. **Open the [`SMTP`](/reference/app-settings/#smtp) tab.**

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Fill in your SMTP server details.**

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - `SMTP From`: the name and address the customer sees. Use the format `"Full Name" <name@company.com>`.
        - `SMTP Server`: the server address from your provider, such as `smtp.example.com`.
        - `SMTP Username`: usually the email address your provider gave you.
        - `SMTP Password`: the password for that username. Some providers issue a separate password for SMTP.
        - `SMTP Port`: the port your provider specifies, usually `25`, `465`, `587` or `2525`.

        SMTP settings vary by email provider. To find your settings:

        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you are not sure what to enter, contact your email service provider or search their documentation for `SMTP`.

    4. **Test and Activate**: Click `test connection & activate`. Once the test passes, all emails are sent from your server.

        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).


You have set up emails with the RevenueHunt app.

---
This tutorial and video explain how to send emails to customers and to yourself, and how to connect your own email server over SMTP.



