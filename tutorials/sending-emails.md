---
icon: material/numeric-5
---

# Sedning Emails with RevenueHunt app


=== "Shopify"


    In this tutorial, you’ll learn how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP (Simple Mail Transfer Protocol).

    !!! info "You’ll learn:"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP,
        - how to style emails with the help of AI tools.

    
    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/yQJBaheRWgw?si=NaiYYKOovWwDXlV4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


=== "Shopify (Legacy)"

    In these tutorials, you’ll learn how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP (Simple Mail Transfer Protocol) .

    !!! info "You’ll learn:"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "WooCommerce"

    In these tutorials, you’ll learn how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP (Simple Mail Transfer Protocol).

    !!! info "You’ll learn:"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "Magento"

    In these tutorials, you’ll learn how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP (Simple Mail Transfer Protocol).

    !!! info "You’ll learn:"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "BigCommerce"

    In these tutorials, you’ll learn how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP (Simple Mail Transfer Protocol).

    !!! info "You’ll learn:"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.

=== "Standalone"

    In these tutorials, you’ll learn how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP (Simple Mail Transfer Protocol).

    !!! info "You’ll learn:"

        - how to send quiz result emails to customers automatically,
        - how to receive a notification email when someone completes a quiz,
        - how to connect your own email server using SMTP.





## Sending Emails to Respondents


=== "Shopify"


    1. **Add Email Question**: Before you set up your result emails, you need to make sure that the quiz has an [email question](/reference/quiz-builder/questions/#email). To add an email question go to the [Quiz Builder > Questions](/reference/quiz-builder/questions/) and click `+ Add question`or `+ Add block`.
    2. **Activate Respondent Emails**: Go to [`Quiz Settings > Emails to respondents`](/reference/quiz-builder/notifications/#to-respondent) and check the `Send email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_shopifyV2_quizbuilder_notification_torespondent.png)
    3. **Edit Email Template - Email TO**: Choose an answer to which email question should be used to send the result emails to.
    4. **Edit Email Template -  REPLY-TO**: Choose what email the customers will be able to reply to once they recieve the results.
    5. **Edit Email Template - Email Subject**: Edit the title of the email that customers will receive. 
    6. **Edit Email Template - Email Liquid template**: Configure the email temaplate of the email that your customers will receive. 

        ![how to send result emails html template](https://loom.com/i/200e22c07c214de2a399b481d7720c80?workflows_screenshot=true)

        !!! warning
            Email template requires the knowledge of HTML and liquid to be edited. 

        - Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use liquid code to loop through and display recommended products or customize content based on quiz outcomes. 

        - The email liquid template uses metadata (such as response ID, quiz name, user's name and email, answers to quiz questions, tags and recommended products, content from the results page) to recall information from the quiz.

            !!! tip

                To learn more about the metadata, check out the [Quiz Response Metadata Structure](/how-to-guides/send-result-emails/#editing-email-templates).
        
        - You can find *useful code snippets* under the `Email Liquid Template` field and use them to insert specific data into the email template (e.g., 'Responses by Block' snippet to list user answers).
    
            !!! tip

                You can copy the useful code snippets and paste them into a large languge model like ChatGPT or Gemini to style the liquid email template.
        

        !!! note
            Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling and editing the Email templates [here](/how-to-guides/send-result-emails/#editing-email-templates).

    7. **Email Preview**: Use the Email preview section to check how the email will look like for different respondents.
    8. **`Recommended` Add Your SMTP Credentials**: Check the step by step instructions [here](#sending-emails-from-your-servers-smtp) to learn how to connect your own email server using SMTP.
    9. **Save the changes**: Remember to save the changes with the top-right `Save` button to update the preview/live quiz.
    10. **Preview the quiz**: Return to the dashboard and preview the quiz. Complete the quiz all the way to the results page to trigger the email notification.



=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](/how-to-guides/send-result-emails/#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](/how-to-guides/send-result-emails/#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](/how-to-guides/send-result-emails/#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](/how-to-guides/send-result-emails/#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/59f5f73b491545fe85b6a3aaeb025bf1?sid=e7fd0e9f-c795-460b-969b-5b94226c0876" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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
        - **Advanced HTML** email template requires the knowledge of HTML and [Handlebars helpers](https://github.com/helpers/handlebars-helpers) to be edited. Incorporate quiz response metadata like `{{first_name}}` to personalize emails. You can use Handlebars to loop through and display recommended products or customize content based on quiz outcomes. Note that HTML emails are not rendered the same in different email clients and that you should add styles inline, not as classes. You also can’t add JavaScript code since it won’t be executed by email clients. Read more about styling Advanced HTML Email temapltes [here](/how-to-guides/send-result-emails/#editing-email-templates).
        ![how to send result emails html template](/images/manual_quizbuilder_notifications_torespondent_active_html.png)
    6. **Publish the changes**: Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.




## Sending Emails to Yourself


=== "Shopify"


    2. **Activate Emails to Self**: Go to [`Quiz Settings > Emails to self`](/reference/quiz-builder/notifications/#to-self) and check the `Receive an email when someone completes the quiz` button to activate the emails.
        ![how to activate to respondent emails](/images/manual_shopifyV2_quizbuilder_notification_toself.png)
    3. **Edit Email template - Email to**: Choose what email adress should recieve the notification (e.g., company or personal email).
    4. **Edit Email template - Email Subject**: Edit the title of the email notifications will receive. 
    5. **Edit Email template - Email Liquid tempalte**: Configure the email your customers will receive. Edit the liquid email template. 
    
        - The default liquid template includes all customer answers from the quiz. You can edit this template to include additional information.
        - Use provided `useful code snippets` to add personal information from users. To add personal information, click to copy the template snippet and paste it at the top of your email liquid template.

            !!! tip

                You can copy the useful code snippets and paste them into a large languge model like ChatGPT or Gemini to style the liquid email template.
        

        - You can always reset the email template to default settings.

    6. **Email Preview**: Use the Email preview section to check how the email will look like for different respondents.
    7. **`Recommended` Add Your SMTP Credentials**: Check the step by step instructions [here](#sending-emails-from-your-servers-smtp) to learn how to connect your own email server using SMTP.
    8. **Save the changes**: Remember to save the changes with the top `Save` button.
    9. **Preview the quiz**: Return to the dashboard and preview the quiz. Complete the quiz all the way to the results page to trigger the email notification.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4f81409e7c704226baa5e7d57d3a5d00?sid=943b1e1b-9aee-4680-af9f-17707623df33" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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




## Sending Emails from Your Servers (SMTP)


=== "Shopify"

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).
    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        SMTP credentials vary by email provider. To find yours: 

        - Check your email provider's documentation by searching for 'SMTP'.
        - Refer to the Revenue Hunt documentation for links to common email providers.
        - Contact your email provider's support team for assistance.

        Fill in the following fields:

        ![how to set up smtp](/images/manual_shopifyV2_appsettings_smtp.png)

        - **SMTP From**: Enter the name (e.g., 'Revenue Hunt') and the provided email address.
        - **SMTP Server**: Copy the SMTP server address from your email provider's configuration (usually in the format `smtp.something`).
        - **SMTP Username**: Use the email address provided by your email provider.
        - **SMTP Password**: Copy the password provided by your email provider.
        - **SMTP Port**: Enter the correct SMTP port number from your email provider's configuration.
        - **SMTP Authentication**: Select 'Plain' for authentication method.
        - **Security Settings**: Adjust as necessary based on your service's requirements (e.g., uncheck options that are not needed).

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: After filling out the SMTP settings, click `Save` to test the connection. 
   
        If the connection fails, double-check all credentials, especially the SMTP port. 

        !!! tip
            If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).       
        
        Once successful, emails will be sent from your email server instead of Revenue Hunt's server.
    
        ![how to set up smtp success](/images/how_to_shopifyv2_smtp_success.png)




=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](#troubleshooting-common-smtp-connection-issues).


=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/4887d06413b84d0098f2c08c49f8ead9?sid=6eac3370-9976-4ea2-81c3-85a0691669a5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Settings**: Navigate to your quiz dashboard and open the [App Settings](/reference/app-settings/).
    2. **Locate SMTP Settings**: Select the [SMTP tab](/reference/app-settings/#smtp).

        ![how to set up smtp](/images/manual_appsettings_smtp.png)

    3. **Enter SMTP Details**: Fill in your SMTP server details. 

        Fill in the following fields:

        ![how to set up smtp filled in](/images/how_to_smtp_filledin.png)

        - **SMTP From Field**: Enter your email address in the format `name@revenuehunt.com`.
        - **SMTP Server**: Copy the host value from your email provider's configuration (usually in the format `smtp.something`).
        - **Username**: Use the username provided, usually your email address.
        - **SMTP Password**: Enter the password provided by your email provider. Note that some providers may require a special password for SMTP settings.
        - **SMTP Port**: Enter the port number (e.g., `587`) as specified by your email provider's configuration.

        SMTP settings vary by email provider. To find your settings:
        
        - Search your email provider's documentation for 'SMTP'.
        - Visit [Specific SMTP Configurations](/how-to-guides/send-result-emails-from-custom-server/#specific-smtp-configurations) for common email provider instructions.
        - Contact your email provider's support team for assistance.

        !!! note

            If you're not sure how to fill it in, try contacting your email service provider or check their documentation (search for "SMTP" on the documentation page).

    4. **Test and Activate**: Click on `test connection & activate`. If the test is succsefull, from now on all the emails will be sent from your server. 
    
        If there are errors, please check the [troubleshooting guidelines](/how-to-guides/send-result-emails-from-custom-server/#troubleshooting-common-smtp-connection-issues).


Congratulations! You've successfully set up emails with the RevenueHunt app!

---
This tutorial and video explain how to send emails to quiz respondents and yourself using the RevenueHunt app and how to connect your own email server using SMTP.



