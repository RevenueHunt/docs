---
description: "Complete guide to integrate RevenueHunt quiz with Klaviyo for targeted email follow-up campaigns."
---

# How to Send Quiz Leads to Klaviyo

Apart from giving your customers personalized product recommendations, you can connect your quiz to Klaviyo. This way all the contacts coming from the quiz will be added to your Klaviyo account and you can create targeted email campaigns to upsell them.

This article walks you through the process of connecting your quiz to Klaviyo and setting up post-quiz email flow. You can also follow our step-by-step [tutorial](/tutorials/follow-up-emails-klaviyo/).


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=xQ5-t5vueGKlDL4q" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "Tutorial"
        You can also follow our step-by-step tutorial to learn how to connect your quiz to Klaviyo and send leads to Klaviyo: [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/)


=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    !!! tip "Tutorial"
        You can also follow our step-by-step tutorial to learn how to connect your quiz to Klaviyo and send leads to Klaviyo: [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/)

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    !!! tip "Tutorial"
        You can also follow our step-by-step tutorial to learn how to connect your quiz to Klaviyo and send leads to Klaviyo: [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/)

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


    !!! tip "Tutorial"
        You can also follow our step-by-step tutorial to learn how to connect your quiz to Klaviyo and send leads to Klaviyo: [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/)

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


    !!! tip "Tutorial"
        You can also follow our step-by-step tutorial to learn how to connect your quiz to Klaviyo and send leads to Klaviyo: [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/)

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


    !!! tip "Tutorial"
        You can also follow our step-by-step tutorial to learn how to connect your quiz to Klaviyo and send leads to Klaviyo: [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/)

## Link Your Quiz to Klaviyo

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=CtsHul93EE3HbY8K&amp;start=38" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The Klaviyo integration uses OAuth to securely connect your store to Klaviyo. This connection is made at the **store level**, meaning once connected, you can enable Klaviyo for any of your quizzes.

    1. Open the RevenueHunt app and navigate to any quiz.
    2. Go to `Quiz Settings > Integrations` tab.
    3. Scroll to the `Mailing & CRMs` section and find the Klaviyo card.
    4. Click the `Connect` button.
    5. You will be redirected to Klaviyo's authorization page. Log in to your Klaviyo account if prompted.
    6. Select the Klaviyo account you want to connect and review the permissions requested, then click `Allow` to authorize the connection.
    7. You will be redirected back to the RevenueHunt app. The Klaviyo card will now show as `Connected`, with your account name and Site ID displayed.
    8. Klaviyo is automatically **enabled** for the quiz you initiated the connection from. You can enable it for other quizzes individually by opening `Quiz Settings > Integrations` and toggling `Send quiz leads to Klaviyo`.

    9. Publish the changes with the top `Save` button.
    10. Test the quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Klaviyo account.
    11. To verify the test, open `Klaviyo > Audience > Profiles`. If a new profile was added the integration was successful.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    !!! tip "Reconnecting"
        If you previously connected Klaviyo and need to refresh permissions or switch accounts, click `Reconnect` on the Klaviyo card. Use `Disconnect` to revoke the connection entirely.

    !!! info "Legacy API key setup"
        Stores that configured Klaviyo before the OAuth integration still work using their saved Public and Private API keys. We recommend reconnecting via OAuth for the cleaner setup and automatic token management.

    **Custom Properties**

    Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer Profiles. These properties are instrumental in personalizing Klaviyo email templates.

    ![how to send leads to klaviyo customer profile](/images/how_to_klaviyo_shopify_v2_customer_profile.png)


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you’ll have to provide your Klaviyo **Public API Key**. Public API Key is essential because it allows us to send information to Klaviyo Profiles.

    2. To find your Public Key login to your Klaviyo account. In account `Settings` open the `API Keys` tab and copy the public API Key. You can get your Klaviyo Public API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo public api key](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    3. Navigate back to the RevenueHunt app. 
    4. In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection. Paste your Public API Key and save.
        ![how to send leads to klaviyo public api key provided1](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![how to send leads to klaviyo public api key provided2](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    5. Publish the changes with the top-right `Publish` button.
    6. Test quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.
    7. To verify the test, open `Kalviyo > Audeince > Profiles` section. If a new profile was added the integration was successful.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom Properties**

    Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer Profiles. These properties are instrumental in personalizing Klaviyo email templates.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you’ll have to provide your Klaviyo **Public API Key**. Public API Key is essential because it allows us to send information to Klaviyo Profiles.

    2. To find your Public Key login to your Klaviyo account. In account `Settings` open the `API Keys` tab and copy the public API Key. You can get your Klaviyo Public API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo public api key](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    3. Navigate back to the RevenueHunt app. 
    4. In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection. Paste your Public API Key and save.
        ![how to send leads to klaviyo public api key provided1](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![how to send leads to klaviyo public api key provided2](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    5. Publish the changes with the top-right `Publish` button.
    6. Test quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.
    7. To verify the test, open `Kalviyo > Audeince > Profiles` section. If a new profile was added the integration was successful.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer Profiles. These properties are instrumental in personalizing Klaviyo email templates.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you’ll have to provide your Klaviyo **Public API Key**. Public API Key is essential because it allows us to send information to Klaviyo Profiles.

    2. To find your Public Key login to your Klaviyo account. In account `Settings` open the `API Keys` tab and copy the public API Key. You can get your Klaviyo Public API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo public api key](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    3. Navigate back to the RevenueHunt app. 
    4. In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection. Paste your Public API Key and save.
        ![how to send leads to klaviyo public api key provided1](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![how to send leads to klaviyo public api key provided2](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    5. Publish the changes with the top-right `Publish` button.
    6. Test quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.
    7. To verify the test, open `Kalviyo > Audeince > Profiles` section. If a new profile was added the integration was successful.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom Properties**

    Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer Profiles. These properties are instrumental in personalizing Klaviyo email templates.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you’ll have to provide your Klaviyo **Public API Key**. Public API Key is essential because it allows us to send information to Klaviyo Profiles.

    2. To find your Public Key login to your Klaviyo account. In account `Settings` open the `API Keys` tab and copy the public API Key. You can get your Klaviyo Public API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo public api key](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    3. Navigate back to the RevenueHunt app. 
    4. In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection. Paste your Public API Key and save.
        ![how to send leads to klaviyo public api key provided1](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![how to send leads to klaviyo public api key provided2](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    5. Publish the changes with the top-right `Publish` button.
    6. Test quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.
    7. To verify the test, open `Kalviyo > Audeince > Profiles` section. If a new profile was added the integration was successful.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom Properties**

    Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer Profiles. These properties are instrumental in personalizing Klaviyo email templates.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you’ll have to provide your Klaviyo **Public API Key**. Public API Key is essential because it allows us to send information to Klaviyo Profiles.

    2. To find your Public Key login to your Klaviyo account. In account `Settings` open the `API Keys` tab and copy the public API Key. You can get your Klaviyo Public API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo public api key](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    3. Navigate back to the RevenueHunt app. 
    4. In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection. Paste your Public API Key and save.
        ![how to send leads to klaviyo public api key provided1](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![how to send leads to klaviyo public api key provided2](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    5. Publish the changes with the top-right `Publish` button.
    6. Test quiz all the way to the results. Make sure to provide a sample email that doesn’t already exist in your Kalviyo account.
    7. To verify the test, open `Kalviyo > Audeince > Profiles` section. If a new profile was added the integration was successful.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom Properties**

    Following these steps ensures that every quiz participant's contact information, alongside their responses and product recommendations, are forwarded to your Klaviyo account, registering as `custom properties` within Klaviyo customer Profiles. These properties are instrumental in personalizing Klaviyo email templates.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

??? warning "Klaviyo Limitations"

    **Processing Time**: Klaviyo may have some delay in displaying new leads.

    **Character Limitations**: Special characters (e.g., è, é, ê) may impede data transmission.

## Sending Follow-up Emails via Klaviyo

It’s possible to send the product recommendation follow-up emails via Klaviyo, although this is not something that’s a one-click install. It should be built by someone with technical knowledge and experience in Klaviyo. 

Below you’ll find some basic instructions that can be forwarded to a developer.

!!! tip "Go beyond the results email"

    This section covers the single results-delivery flow. To turn quiz data into a full revenue system (cart abandonment, browse abandonment, replenishment, cross-sell and win-back flows, each segmented by quiz answers and tags), see [How to Build Post-Quiz Email Flows in Klaviyo](/how-to-guides/send-klaviyo-post-quiz-email-flows/).

??? warning "RevenueHunt Support Scope"

    Once the quiz is connected to Klaviyo (and the data is sent there), it’s out of our app’s scope, and any particular questions on how to set up the flows and how to build the email templates should be directed to Klaviyo.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=KsRYtyVaGyDNuoSs&amp;start=187" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list.

        !!! tip

            You can [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [this section](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo. 

        1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `Create New > New Segment`.
        2. Name the segment and set up the definition. 
        3. Segment definition: Select `Properties about someone` and add a property that will be unique for profiles coming from the quiz. This can be any of the [custom properties](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates) that RevenueHunt sends to Klaviyo Profiles.
            
            !!! example "Example"
            
                - `ANSWERS_BY_BLOCK-QuizID` property is unique for profiles coming from the quiz.  

                - If you don't see the `ANSWERS_BY_BLOCK-QuizID` property in the dropdown menu, you may need to take a test quiz and try again.

        4. Segment definition: As segment definition set up a rule that follows this format: `Custom property from the Quiz` `is set` Type: `text`.

            !!! example "Example"

                - `ANSWERS_BY_BLOCK-QuizID` `is set` Type: `text`.

        5. Click `Create a segment` and wait for Klaviyo to load all the contacts that match the segment definition. This may take a few minutes.
        6. Once the agent finishes loading, all the profiles that already match the segment definition will be added to the segment. New contacts coming from the quiz will be added to the segment automatically.

    4. **Create an Email Flow**: You’ll have to create a flow that is triggered when someone gets added to the segment we created in the previous step. This is the trickiest part, the emails you send have to be custom-built in Klaviyo. 

        **Trigger the Flow**

        1. To create an email flow that includes only quiz takers open the `Flows` tab in Klaviyo. 
        2. Click `Create flow` and then `Build from scratch`.
        3. Name the flow and click `Create flow`.
        4. Next, you'll be asked to set up a flow trigger.
        5. Choose the trigger to be `Added to a segment` and select the segment created in the previous step. Set the `Reentry criteria` to `Allow reentry` so quiz takers receive an email every time they complete the quiz. Click `Confirm` and `Confirm and save`.

            !!! tip "Alternative: trigger from a Klaviyo list"
                Instead of triggering from a segment, you can trigger the flow when a contact is added to a specific Klaviyo list. This is useful if you're using the `Klaviyo list` selector in your quiz's email question block to send contacts directly to a list (see [Adding Quiz Contacts to Klaviyo List](#adding-quiz-contacts-to-klaviyo-list)).

        **Optional: Update Marketing Consent**

        If you've [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), you can update it in the Klaviyo email flow. Just follw these steps:

        1. Right below the flow trigger, add a `Profile property update` action.
        2. Click `+ Step`.
        3. A menu will appear letting up set up the profile property update.
        4. Select to `Update existing property`, from the Select property dropdown menu select `Accepts marketing` and set the value to `true`.
        5. Turn this action `LIVE`.

    6. **Edit the Email**: In the next steps, you should edit the email template.

        **Add Email Action**

        ![how to send leads to klaviyo built for shopify revenuehunt app create email flow](https://loom.com/i/01df24e93900407b9141998dfb070a2e?workflows_screenshot=true)


        1. Grab the `EMAIL` action and drop it below the flow trigger.

        **Edit the Email Template**

        2. In `Email details` section edit the Subject.
        3. Then, click `Select template`. You'll be taken to the Templates section in Klaviyo.
        4. To create a new email template, click `Create`. You'll be redirected to the Klaviyo email builder.
        5. In the Klaviyo email builder you can use pre-designed blocs to add images or text to your template. 
        6. To add the quiz content and quiz recommended products you'll need to add an `HTML` block. Drag and drop the `HTML` block to the email builder.
        7. In the `Quiz Settings > Integrations` section, you'll find a button to download a `Klaviyo Template`. Click the `Klaviyo Template` button and a new window will open. There, click `Copy code` to copy the existing template.
            
            !!! info "Klaviyo Template"

                ![how to send leads to klaviyo email tempalte download1](/images/how_to_shopifyv2_klaviyo_shopify_v2_get_template.png)
                ![how to send leads to klaviyo email tempalte download2](/images/how_to_shopifyv2_klaviyo_shopify_v2_copy_template.png)

                The code contains several ready-to-use code snippets that allow you to display: 

                - **Dynamic Results Page**: Display dynamic result page content that loops through sections and blocks. A Dynamic Results Page content that contains all the elements of your results page and replaces content upon each quiz retake. This is the recommended approach for production templates as it adapts to quiz structure changes.
                - **Static Results Page**: Display the complete result page content using static lookups. Static Results Page content that contains all the elements of your results page and adds content upon each quiz retake. Use this approach for understanding the data structure and for simple implementations.
                - **Individual recommendations**: Display individual product recommendations by slot. Use this to show specific recommended items with their details like title, description, price, and images.
                - **Question answers**: Display quiz information and individual question answers. Use this to show personal data and specific responses from quiz questions.

        8. Paste the code in the `HTML` block in Klaviyo email.

            ![how to send leads to klaviyo built for shopify revenuehunt app example template in klaviyo](https://loom.com/i/04a9f5a3d3a040d2a97c2b393fc18c41?workflows_screenshot=true)
        9. Next, `Preview` the email as one of your segment subscribers to check what information is displayed.
        10. You can freely edit the email template to your liking. For example, you can remove sections of the code that you don't need and restyle the rest to match your branding.

            !!! tip "Let Quiz Copilot edit and style your Klaviyo template"
                You don't need a developer to customize the Klaviyo HTML template. Just paste the template code into [Quiz Copilot](/how-to-guides/use-quiz-copilot/) and ask it to:

                - remove sections you don't need (e.g. keep only recommended products or only question answers),
                - restyle the template to match your brand colors, fonts, and spacing,
                - rearrange blocks or change the layout,
                - explain what each part of the template does.

                Once Quiz Copilot returns the updated code, paste it back into the `HTML` block in your Klaviyo template.

            ??? info "Create your own email template"

                Check the [Use quiz data in Klaviyo email templates](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates) article to learn how to customize your Klaviyo email template with quiz properties.

        11. Once you're happy with the email template, click `Exit` then `Done` and return to your flow.
        12. Turn your email `LIVE`.

        From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

    8. **Re-trigger the flow**: The easiest way to send an email with each quiz retake is to set the **reentry criteria** when you configure the flow trigger:

        1. Open the flow trigger (`Added to a segment`).
        2. Set the `Reentry criteria` to `Allow reentry`.
        3. Save the trigger.

        This way, quiz takers will receive an email every time they complete the quiz.

        !!! tip "Alternative method"
            You can also achieve this by adding a `Profile property update` action at the end of the flow that **deletes** the segment property (for example, `ANSWERS_BY_BLOCK-QuizID`). Each time a quiz taker completes the quiz, the property is re-added and they re-enter the segment, triggering the flow again.

            ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_shopifyv2_klaviyo_resend_email_with_each_quiz_retake.png)



=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [this](#link-your-quiz-to-klaviyo) section to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo. 

        1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `Create New > New Segment`.
        2. Name the segment and set up the definition.
        3. The `Permalink-QuizID`  property is unique for profiles coming from the quiz.
        4. If you don't see the permalink property in the dropdown menu, you may need to take a test quiz and try again.
        5. Click `Create a segment`.

    5. **Create an Email Flow**: You’ll have to create a flow that is triggered when someone gets added to the segment we created in the previous step. This is the trickiest part, the emails you send have to be custom-built in Klaviyo. 

        **Trigger Flow**

        1. To create an email flow that includes only quiz takers open the `Flows` tab in Klaviyo. 
        2. Click `Create flow` and then `Build from scratch`.
        3. Name the flow and click `Create flow`.
        4. Next, you'll be asked to set up a flow trigger.
        5. Choose the trigger to be `Added to a segment` and select the segment created in the [previous step](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-takers). Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.    

        **Optional: Update Marketing Consent**

        If you've [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), you can update it in the Klaviyo email flow. Just follw these steps:

        1. Right below the flow trigger, add a `Profile property update` action.
        2. Click `+ Step`.
        3. A menu will appear letting up set up the profile property update.
        4. Select to `Update existing property`, from the Select property dropdown menu select `Accepts marketing` and set the value to `true`.
        5. Turn this action `LIVE`.



    6. **Edit the Email**: In the next steps, you should edit the email template.

        **Add Email Action**

        7. Click on the `three dots` and edit the email.
        8. Edit the name/subject/email to your liking and select the `HTML email template`.
        9. From the `Connect >  Klaviyo` tab you can download a ready-to-use email template. 
        
            ![how to send leads to klaviyo email tempalte download1](/images/how_to_send_leads_to_klaviyo_email_tempalte_download1.png)
            ![how to send leads to klaviyo email tempalte download2](/images/how_to_send_leads_to_klaviyo_email_tempalte_download2.png)

            !!! tip

                If you would rather create your own email template, check [this section](#use-quiz-data-in-klaviyo-email-templates) for more details.

        10. Copy the code and go back to Klaviyo.
        11. Open the `HTML email template` and remove the existing code.
        12. Paste the new template code.
        13. You can then `preview` the email as one of your segment subscribers.
        14. Make sure to `Save` the changes and click `Done`.
        15. Return to your flow and turn your email `LIVE`.

        From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

    7. **Re-trigger the flow**: If you want to send an email with each quiz retake, you can do that by adding a `Profile property update` action at the end of the flow. Follow these steps:

        1. Add a `Profile property update` action at the end of the flow.
        2. Click `+ Step`.
        3. Select `Delete existing property`.
        4. From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps. 

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`. 

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, you need to set up a segment based on the `PERMALINK-{{quiz_id}}` property to filter quiz takers. Once the segment is created, you can build a flow that triggers when users are added to this segment, sends them their quiz results via email, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile** to allow for re-entry if they retake the quiz.

                For example:

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. Save the changes and turn the action `LIVE`.

        This way, each time a quiz taker takes the quiz again, they will be re-added to the segment and will trigger the email flow again.

    ??? tip "Deactive App Emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up. 



=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [this](#link-your-quiz-to-klaviyo) section to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo. 

        1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `Create New > New Segment`.
        2. Name the segment and set up the definition.
        3. The `Permalink-QuizID`  property is unique for profiles coming from the quiz.
        4. If you don't see the permalink property in the dropdown menu, you may need to take a test quiz and try again.
        5. Click `Create a segment`.

    5. **Create an Email Flow**: You’ll have to create a flow that is triggered when someone gets added to the segment we created in the previous step. This is the trickiest part, the emails you send have to be custom-built in Klaviyo. 

        **Trigger Flow**

        1. To create an email flow that includes only quiz takers open the `Flows` tab in Klaviyo. 
        2. Click `Create flow` and then `Build from scratch`.
        3. Name the flow and click `Create flow`.
        4. Next, you'll be asked to set up a flow trigger.
        5. Choose the trigger to be `Added to a segment` and select the segment created in the [previous step](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-takers). Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.    

        **Optional: Update Marketing Consent**

        If you've [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), you can update it in the Klaviyo email flow. Just follw these steps:

        1. Right below the flow trigger, add a `Profile property update` action.
        2. Click `+ Step`.
        3. A menu will appear letting up set up the profile property update.
        4. Select to `Update existing property`, from the Select property dropdown menu select `Accepts marketing` and set the value to `true`.
        5. Turn this action `LIVE`.



    6. **Edit the Email**: In the next steps, you should edit the email template.

        **Add Email Action**

        7. Click on the `three dots` and edit the email.
        8. Edit the name/subject/email to your liking and select the `HTML email template`.
        9. From the `Connect >  Klaviyo` tab you can download a ready-to-use email template. 
        
            ![how to send leads to klaviyo email tempalte download1](/images/how_to_send_leads_to_klaviyo_email_tempalte_download1.png)
            ![how to send leads to klaviyo email tempalte download2](/images/how_to_send_leads_to_klaviyo_email_tempalte_download2.png)

            !!! tip

                If you would rather create your own email template, check [this section](#use-quiz-data-in-klaviyo-email-templates) for more details.

        10. Copy the code and go back to Klaviyo.
        11. Open the `HTML email template` and remove the existing code.
        12. Paste the new template code.
        13. You can then `preview` the email as one of your segment subscribers.
        14. Make sure to `Save` the changes and click `Done`.
        15. Return to your flow and turn your email `LIVE`.

        From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

    7. **Re-trigger the flow**: If you want to send an email with each quiz retake, you can do that by adding a `Profile property update` action at the end of the flow. Follow these steps:

        1. Add a `Profile property update` action at the end of the flow.
        2. Click `+ Step`.
        3. Select `Delete existing property`.
        4. From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps. 

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`. 

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, you need to set up a segment based on the `PERMALINK-{{quiz_id}}` property to filter quiz takers. Once the segment is created, you can build a flow that triggers when users are added to this segment, sends them their quiz results via email, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile** to allow for re-entry if they retake the quiz.

                For example:

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. Save the changes and turn the action `LIVE`.

        This way, each time a quiz taker takes the quiz again, they will be re-added to the segment and will trigger the email flow again.

    ??? tip "Deactive App Emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up. 


=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [this](#link-your-quiz-to-klaviyo) section to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo. 

        1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `Create New > New Segment`.
        2. Name the segment and set up the definition.
        3. The `Permalink-QuizID`  property is unique for profiles coming from the quiz.
        4. If you don't see the permalink property in the dropdown menu, you may need to take a test quiz and try again.
        5. Click `Create a segment`.

    5. **Create an Email Flow**: You’ll have to create a flow that is triggered when someone gets added to the segment we created in the previous step. This is the trickiest part, the emails you send have to be custom-built in Klaviyo. 

        **Trigger Flow**

        1. To create an email flow that includes only quiz takers open the `Flows` tab in Klaviyo. 
        2. Click `Create flow` and then `Build from scratch`.
        3. Name the flow and click `Create flow`.
        4. Next, you'll be asked to set up a flow trigger.
        5. Choose the trigger to be `Added to a segment` and select the segment created in the [previous step](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-takers). Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.    

        **Optional: Update Marketing Consent**

        If you've [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), you can update it in the Klaviyo email flow. Just follw these steps:

        1. Right below the flow trigger, add a `Profile property update` action.
        2. Click `+ Step`.
        3. A menu will appear letting up set up the profile property update.
        4. Select to `Update existing property`, from the Select property dropdown menu select `Accepts marketing` and set the value to `true`.
        5. Turn this action `LIVE`.



    6. **Edit the Email**: In the next steps, you should edit the email template.

        **Add Email Action**

        7. Click on the `three dots` and edit the email.
        8. Edit the name/subject/email to your liking and select the `HTML email template`.
        9. From the `Connect >  Klaviyo` tab you can download a ready-to-use email template. 
        
            ![how to send leads to klaviyo email tempalte download1](/images/how_to_send_leads_to_klaviyo_email_tempalte_download1.png)
            ![how to send leads to klaviyo email tempalte download2](/images/how_to_send_leads_to_klaviyo_email_tempalte_download2.png)

            !!! tip

                If you would rather create your own email template, check [this section](#use-quiz-data-in-klaviyo-email-templates) for more details.

        10. Copy the code and go back to Klaviyo.
        11. Open the `HTML email template` and remove the existing code.
        12. Paste the new template code.
        13. You can then `preview` the email as one of your segment subscribers.
        14. Make sure to `Save` the changes and click `Done`.
        15. Return to your flow and turn your email `LIVE`.

        From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

    7. **Re-trigger the flow**: If you want to send an email with each quiz retake, you can do that by adding a `Profile property update` action at the end of the flow. Follow these steps:

        1. Add a `Profile property update` action at the end of the flow.
        2. Click `+ Step`.
        3. Select `Delete existing property`.
        4. From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps. 

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`. 

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, you need to set up a segment based on the `PERMALINK-{{quiz_id}}` property to filter quiz takers. Once the segment is created, you can build a flow that triggers when users are added to this segment, sends them their quiz results via email, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile** to allow for re-entry if they retake the quiz.

                For example:

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. Save the changes and turn the action `LIVE`.

        This way, each time a quiz taker takes the quiz again, they will be re-added to the segment and will trigger the email flow again.

    ??? tip "Deactive App Emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up. 


=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [this](#link-your-quiz-to-klaviyo) section to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo. 

        1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `Create New > New Segment`.
        2. Name the segment and set up the definition.
        3. The `Permalink-QuizID`  property is unique for profiles coming from the quiz.
        4. If you don't see the permalink property in the dropdown menu, you may need to take a test quiz and try again.
        5. Click `Create a segment`.

    5. **Create an Email Flow**: You’ll have to create a flow that is triggered when someone gets added to the segment we created in the previous step. This is the trickiest part, the emails you send have to be custom-built in Klaviyo. 

        **Trigger Flow**

        1. To create an email flow that includes only quiz takers open the `Flows` tab in Klaviyo. 
        2. Click `Create flow` and then `Build from scratch`.
        3. Name the flow and click `Create flow`.
        4. Next, you'll be asked to set up a flow trigger.
        5. Choose the trigger to be `Added to a segment` and select the segment created in the [previous step](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-takers). Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.    

        **Optional: Update Marketing Consent**

        If you've [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), you can update it in the Klaviyo email flow. Just follw these steps:

        1. Right below the flow trigger, add a `Profile property update` action.
        2. Click `+ Step`.
        3. A menu will appear letting up set up the profile property update.
        4. Select to `Update existing property`, from the Select property dropdown menu select `Accepts marketing` and set the value to `true`.
        5. Turn this action `LIVE`.



    6. **Edit the Email**: In the next steps, you should edit the email template.

        **Add Email Action**

        7. Click on the `three dots` and edit the email.
        8. Edit the name/subject/email to your liking and select the `HTML email template`.
        9. From the `Connect >  Klaviyo` tab you can download a ready-to-use email template. 
        
            ![how to send leads to klaviyo email tempalte download1](/images/how_to_send_leads_to_klaviyo_email_tempalte_download1.png)
            ![how to send leads to klaviyo email tempalte download2](/images/how_to_send_leads_to_klaviyo_email_tempalte_download2.png)

            !!! tip

                If you would rather create your own email template, check [this section](#use-quiz-data-in-klaviyo-email-templates) for more details.

        10. Copy the code and go back to Klaviyo.
        11. Open the `HTML email template` and remove the existing code.
        12. Paste the new template code.
        13. You can then `preview` the email as one of your segment subscribers.
        14. Make sure to `Save` the changes and click `Done`.
        15. Return to your flow and turn your email `LIVE`.

        From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

    7. **Re-trigger the flow**: If you want to send an email with each quiz retake, you can do that by adding a `Profile property update` action at the end of the flow. Follow these steps:

        1. Add a `Profile property update` action at the end of the flow.
        2. Click `+ Step`.
        3. Select `Delete existing property`.
        4. From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps. 

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`. 

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, you need to set up a segment based on the `PERMALINK-{{quiz_id}}` property to filter quiz takers. Once the segment is created, you can build a flow that triggers when users are added to this segment, sends them their quiz results via email, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile** to allow for re-entry if they retake the quiz.

                For example:

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. Save the changes and turn the action `LIVE`.

        This way, each time a quiz taker takes the quiz again, they will be re-added to the segment and will trigger the email flow again.

    ??? tip "Deactive App Emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up. 


=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [this](#link-your-quiz-to-klaviyo) section to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo. 

        1. To create a new segment in Klaviyo go to  `Audience > List & Segements` and click `Create New > New Segment`.
        2. Name the segment and set up the definition.
        3. The `Permalink-QuizID`  property is unique for profiles coming from the quiz.
        4. If you don't see the permalink property in the dropdown menu, you may need to take a test quiz and try again.
        5. Click `Create a segment`.

    5. **Create an Email Flow**: You’ll have to create a flow that is triggered when someone gets added to the segment we created in the previous step. This is the trickiest part, the emails you send have to be custom-built in Klaviyo. 

        **Trigger Flow**

        1. To create an email flow that includes only quiz takers open the `Flows` tab in Klaviyo. 
        2. Click `Create flow` and then `Build from scratch`.
        3. Name the flow and click `Create flow`.
        4. Next, you'll be asked to set up a flow trigger.
        5. Choose the trigger to be `Added to a segment` and select the segment created in the [previous step](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-takers). Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.    

        **Optional: Update Marketing Consent**

        If you've [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), you can update it in the Klaviyo email flow. Just follw these steps:

        1. Right below the flow trigger, add a `Profile property update` action.
        2. Click `+ Step`.
        3. A menu will appear letting up set up the profile property update.
        4. Select to `Update existing property`, from the Select property dropdown menu select `Accepts marketing` and set the value to `true`.
        5. Turn this action `LIVE`.



    6. **Edit the Email**: In the next steps, you should edit the email template.

        **Add Email Action**

        7. Click on the `three dots` and edit the email.
        8. Edit the name/subject/email to your liking and select the `HTML email template`.
        9. From the `Connect >  Klaviyo` tab you can download a ready-to-use email template. 
        
            ![how to send leads to klaviyo email tempalte download1](/images/how_to_send_leads_to_klaviyo_email_tempalte_download1.png)
            ![how to send leads to klaviyo email tempalte download2](/images/how_to_send_leads_to_klaviyo_email_tempalte_download2.png)

            !!! tip

                If you would rather create your own email template, check [this section](#use-quiz-data-in-klaviyo-email-templates) for more details.

        10. Copy the code and go back to Klaviyo.
        11. Open the `HTML email template` and remove the existing code.
        12. Paste the new template code.
        13. You can then `preview` the email as one of your segment subscribers.
        14. Make sure to `Save` the changes and click `Done`.
        15. Return to your flow and turn your email `LIVE`.

        From that moment on, all the quiz takers, who leave their email, will be automatically added to your Kalviyo Segment and will be sent a follow-up email. 

    7. **Re-trigger the flow**: If you want to send an email with each quiz retake, you can do that by adding a `Profile property update` action at the end of the flow. Follow these steps:

        1. Add a `Profile property update` action at the end of the flow.
        2. Click `+ Step`.
        3. Select `Delete existing property`.
        4. From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps. 

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`. 

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, you need to set up a segment based on the `PERMALINK-{{quiz_id}}` property to filter quiz takers. Once the segment is created, you can build a flow that triggers when users are added to this segment, sends them their quiz results via email, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile** to allow for re-entry if they retake the quiz.

                For example:

                ![how to send leads to klaviyo resend email with each quiz retake](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. Save the changes and turn the action `LIVE`.

        This way, each time a quiz taker takes the quiz again, they will be re-added to the segment and will trigger the email flow again.

    ??? tip "Deactive App Emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up. 


## Adding Quiz Contacts to Klaviyo List

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=G8fIYtPfLkZjmy8I&amp;start=114" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    With the OAuth connection in place, you can add contacts from the quiz directly to a **list** in Klaviyo. No additional API keys are needed — the list selector lives inside the email question block.

    1. First, make sure that you have a Klaviyo list ready to add contacts to. If you don't have one, you can create a new one in `Klaviyo > Audience > Lists & Segments`. In the list settings, make sure to set it to `Single Opt-in`.

        !!! warning
            Quiz contacts can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) list in Klaviyo.

    2. Make sure your RevenueHunt account is [connected to Klaviyo via OAuth](#link-your-quiz-to-klaviyo) and that the `Send Quiz Leads to Klaviyo Profiles` checkbox is enabled in the quiz's `Quiz Settings > Integrations` section.
    3. In the RevenueHunt app, open the [Quiz Builder](/reference/quiz-builder/) and click on the email question block to open its settings.
    4. Under the `Klaviyo list` dropdown, select the list you want quiz takers added to.
    5. Set the `subscription status` (for example, `Subscribed`).

        ![how to klaviyo built for shopify revenuehunt app email question settings](/images/how_to_klaviyo_shopify_v2_email_question_settings.png)
    6. Save your quiz changes with the top-right `Save` button.

        !!! tip "Per-quiz lists"
            If you have multiple quizzes and want each to feed a different Klaviyo list, configure the email question block of each quiz individually and select the appropriate list there.

    7. `Preview` the quiz and complete it with a sample email to verify the connection.
    8. In Klaviyo, go to `Audience > Lists & Segments` and open the list to confirm the test contact was added as `Subscribed`.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt app allows you to add contacts from the quiz directly to a list in Klaviyo. 

    1. To do that you’ll need to provide a **Private API Key**.
    2. To create a new Private Key for the RevenueHunt app login to your Klaviyo account.
    3. In account `Settings` open the `API Keys` tab and create a new Private API Key. For list-specific contact additions, you can get your Klaviyo Private API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo private api key](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. Allow `Full access`.
    5. Copy the private key.
    6. In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.
    7. Paste your Private API Key.
    8. Choose to `mark all profiles as true` and select a list that contacts should be added to.

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    10. Save the changes and publish them with the top-right `Publish` button.
    11. Remember to test the connection with a sample email.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt app allows you to add contacts from the quiz directly to a list in Klaviyo. 

    1. To do that you’ll need to provide a **Private API Key**.
    2. To create a new Private Key for the RevenueHunt app login to your Klaviyo account.
    3. In account `Settings` open the `API Keys` tab and create a new Private API Key. For list-specific contact additions, you can get your Klaviyo Private API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo private api key](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. Allow `Full access`.
    5. Copy the private key.
    6. In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.
    7. Paste your Private API Key.
    8. Choose to `mark all profiles as true` and select a list that contacts should be added to.

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    10. Save the changes and publish them with the top-right `Publish` button.
    11. Remember to test the connection with a sample email.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt app allows you to add contacts from the quiz directly to a list in Klaviyo. 

    1. To do that you’ll need to provide a **Private API Key**.
    2. To create a new Private Key for the RevenueHunt app login to your Klaviyo account.
    3. In account `Settings` open the `API Keys` tab and create a new Private API Key. For list-specific contact additions, you can get your Klaviyo Private API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo private api key](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. Allow `Full access`.
    5. Copy the private key.
    6. In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.
    7. Paste your Private API Key.
    8. Choose to `mark all profiles as true` and select a list that contacts should be added to.

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    10. Save the changes and publish them with the top-right `Publish` button.
    11. Remember to test the connection with a sample email.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt app allows you to add contacts from the quiz directly to a list in Klaviyo. 

    1. To do that you’ll need to provide a **Private API Key**.
    2. To create a new Private Key for the RevenueHunt app login to your Klaviyo account.
    3. In account `Settings` open the `API Keys` tab and create a new Private API Key. For list-specific contact additions, you can get your Klaviyo Private API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo private api key](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. Allow `Full access`.
    5. Copy the private key.
    6. In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.
    7. Paste your Private API Key.
    8. Choose to `mark all profiles as true` and select a list that contacts should be added to.

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    10. Save the changes and publish them with the top-right `Publish` button.
    11. Remember to test the connection with a sample email.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt app allows you to add contacts from the quiz directly to a list in Klaviyo. 

    1. To do that you’ll need to provide a **Private API Key**.
    2. To create a new Private Key for the RevenueHunt app login to your Klaviyo account.
    3. In account `Settings` open the `API Keys` tab and create a new Private API Key. For list-specific contact additions, you can get your Klaviyo Private API Key [here](https://www.klaviyo.com/account#api-keys-tab).
        ![how to send leads to klaviyo private api key](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. Allow `Full access`.
    5. Copy the private key.
    6. In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.
    7. Paste your Private API Key.
    8. Choose to `mark all profiles as true` and select a list that contacts should be added to.

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [**Single Opt-in**](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.
            
    10. Save the changes and publish them with the top-right `Publish` button.
    11. Remember to test the connection with a sample email.

??? tip "Tip: Segmented Campaigns Work Better"

    It is possible to add contacts to Klaviyo List but there may be a better way: instead of adding them to a general list you can create **dynamic segments** based on your customers’ responses to send them hyper-targeted campaigns. Highly segmented campaigns return more than 3X the revenue per recipient as unsegmented campaigns.

    With Klaviyo you can create segments to filter your leads and assign email flows to each segment. [Read more](#sending-follow-up-emails-via-klaviyo) about how to create and use segments on Klaviyo.

## Use Quiz Data In Klaviyo Email Templates

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/6650ebf870714d9eaf450ea51439b0af?sid=91c5c125-318f-4b07-8233-350d1c7272c5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    If you need to modify our Klaviyo email template to match your brand’s style guide, you’ll need a developer because email templates in Klaviyo are built using HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) system.

    **Custom Properties in Klaviyo**

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Klaviyo profile. This information will appear in the customer’s profile as `custom properties`.

    ![how to send leads to klaviyo customer profile](/images/how_to_klaviyo_shopify_v2_customer_profile.png)

    If you need to add any additional information to the email template, your developer can do so by pulling the appropriate `custom properties` from the user profile.

    ??? info "Learn the person|lookup function"

        To build your own email template based on the custom properties we send to Klaviyo, you should familiarize yourself with the [message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731) in Klaviyo, aka the `{{ person|lookup:"..." }}` function.

    ??? warning "Overwriting or Appending Custom Properties"	

        Some custom properties sent to Klaviyo from the quiz such as `ANSWER_BY_BLOCK`, `CHOICE`, `RESPONSE_ID`, `RESULT_REF`, `RESULT_SECTIONS` or `TAGS` are sent as an array, meaning that their values get **overwritten** with new data upon each quiz completion.

        However, properties such as `RECOMMENDATIONS_BY_SLOT` or `RESULT_CONTENT_BY_BLOCK` are sent as a JSON object, meaning that their values get **appended** to the existing data upon each quiz completion. 

        If you want to make sure that in your Klaviyo template, the **values get overwritten** with new data upon each quiz completion and you want to use our pre-defined Klaviyo email tempalte which you can download from [Integrations](/reference/quiz-builder/connect-integrations/) tab, make sure to only use the code snippet that starts with the following comment:
        
        
        ```html
        {# ================================================================= #}
        {# DYNAMIC RESULT PAGE CONTENT (LOOPS THROUGH RESULT_SECTIONS-lBJ9bk) #}
        {# This template loops through the result sections and blocks          #}
        {# It will adapt if you change the results page structure in the quiz editor #}
        {# ================================================================= #}
        ```




=== "Shopify (Legacy)"

    If you need to modify our Klaviyo email template to match your brand’s style guide, you’ll need a developer because email templates in Klaviyo are built using HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) system.

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Klaviyo profile. This information will appear in the customer’s profile as `custom properties`.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    If you need to add any additional information to the email template, your developer can do so by pulling the appropriate `custom properties` from the user profile.


=== "WooCommerce"

    If you need to modify our Klaviyo email template to match your brand’s style guide, you’ll need a developer because email templates in Klaviyo are built using HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) system.

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Klaviyo profile. This information will appear in the customer’s profile as `custom properties`.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    If you need to add any additional information to the email template, your developer can do so by pulling the appropriate `custom properties` from the user profile.

=== "Magento"

    If you need to modify our Klaviyo email template to match your brand’s style guide, you’ll need a developer because email templates in Klaviyo are built using HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) system.

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Klaviyo profile. This information will appear in the customer’s profile as `custom properties`.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    If you need to add any additional information to the email template, your developer can do so by pulling the appropriate `custom properties` from the user profile.

=== "BigCommerce"

    If you need to modify our Klaviyo email template to match your brand’s style guide, you’ll need a developer because email templates in Klaviyo are built using HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) system.

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Klaviyo profile. This information will appear in the customer’s profile as `custom properties`.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    If you need to add any additional information to the email template, your developer can do so by pulling the appropriate `custom properties` from the user profile.


=== "Standalone"

    If you need to modify our Klaviyo email template to match your brand’s style guide, you’ll need a developer because email templates in Klaviyo are built using HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/1.8/ref/templates/builtins/) system.

    We send all the responses to the quiz and the recommended products along with the contact information to the customer’s Klaviyo profile. This information will appear in the customer’s profile as `custom properties`.

    ![how to send leads to klaviyo customer profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    If you need to add any additional information to the email template, your developer can do so by pulling the appropriate `custom properties` from the user profile.

### Example Email Templates

=== "Shopify"

    ### Use Copilot to generate Klaviyo Email Template

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/645cfa070ef5454f812d851908572cdb?sid=f8c3a497-b077-4c81-bfb6-863320a127cb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    QuizCopilot can assist in creating Klaviyo email templates for your quiz email flow.

    1. [Open the Quiz Copilot](#how-to-use-quiz-copilot) or start a new conversation by clicking the `New conversation` button in the top-right corner of the pop-up window, or head over to the [Quiz Settings](/reference/quiz-settings/)  > [Integrations](/reference/quiz-settings/integrations/) page, find the `Klaviyo` integration and click on the `Edit template with AI` button.
    2. Paste your desired layout message, and Quiz Copilot will generate the template code.

        ![QuizCopilot Building Klaviyo Templates](https://loom.com/i/0bac7b225d8e44dbad1db2b7748c19f5?workflows_screenshot=true)
    3. The generated code for the Klaviyo email template can be copied by clicking the `Copy` icon.
    4. Paste the generated code directly into an HTML block in your Klaviyo email template.


    ### Example 1 - Display Recommended Products

    In this example, a quiz with ID `YN5L9G` recommends a simple list of products.

    !!! example "Example: List of Recommended Products in Klaviyo Template"

        ![how_to_shipifyv2_klaviyo_template_productlist1](/images/how_to_shipifyv2_klaviyo_template_productlist1.png){width="300"}

    1. To show the recommended products in the email, you can use the following code copied from the Klaviyo template in the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab:

        ![how_to_shopifyv2_klaviyo_shopify_v2_get_template](/images/how_to_shopifyv2_klaviyo_shopify_v2_get_template.png)

        ??? example "Example: Code from QuizIntegrations tab"

            ```html
            {# ======================================== #}
            {# INDIVIDUAL ITEM RECOMMENDATIONS BY SLOT  #}
            {# ======================================== #}
            <p>
            <b>Display recommendation of item 0 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'image'|lookup:'url' }}
            </p>

            <p>
            <b>Display recommendation of item 1 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'image'|lookup:'url' }}
            </p>

            <p>
            <b>Display recommendation of item 2 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'image'|lookup:'url' }}
            </p>

            <p>
            <b>Display recommendation of item 3 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'image'|lookup:'url' }}
            </p>h3>
            ```
    2. If you paste this code into an HTML block in a Klaviyo template and preview the email as one of the quiz subscribers, you will see the recommended products.

        ![how_to_shipifyv2_klaviyo_template_productlist2](/images/how_to_shipifyv2_klaviyo_template_productlist2.png)

    3. To style the recommended products, your developer will need to add CSS classes to the HTML code and style it the way you want. 
    
        For example, this is a styled version of the code above:

        ??? example "Example: Styled version of the code above"

            In Klaviyo, it will look like this:

            ![how_to_shipifyv2_klaviyo_template_productlist3](/images/how_to_shipifyv2_klaviyo_template_productlist3.png)

            ```html
            <!-- Two-Column Product Grid for Klaviyo Email -->

            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" align="center" style="font-family: sans-serif;">
            <tr>
                <!-- Product 0 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'image'|lookup:'url' }}" alt="Product 0" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>

                <!-- Product 1 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'image'|lookup:'url' }}" alt="Product 1" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>
            </tr>

            <tr>
                <!-- Product 2 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'image'|lookup:'url' }}" alt="Product 2" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>

                <!-- Product 3 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'image'|lookup:'url' }}" alt="Product 3" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>
            </tr>
            </table>
            ```

        ??? tip "Tip: Use Copilot or AI to style the code"

            You can use [Quiz Copilot](/how-to-guides/use-quiz-copilot/) or another AI agent like ChatGPT or Gemini to generate a styled version of the code.

    4. You can use elements of the code in your Klaviyo template elements. 


        !!! example "Example: Display Product Title in Text Block"
        
        
            For example, you can use the `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}` to display the title of the first product in a text block.

            ![how_to_shipifyv2_klaviyo_template_productlist4](/images/how_to_shipifyv2_klaviyo_template_productlist4.png)

        !!! info "Sample Product Object Structure"

            In this example, here's a product object structure that was sent to Klaviyo:

            - Display recommendation of **item 0** for **slot rsbss-ca4fba94**
            - Title: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}`
            - Description: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'description' }}`	
            - Price: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'currencyCode' }}`
            - Online URL: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'onlineUrl' }}`
            - Image URL: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'image'|lookup:'url' }}`


    ### Example 2 - Display Quiz Answers


    A Skincare Quiz with ID `YN5L9G` wants to display all customer answers in the email. 
    
    1. To do this, you can use the following code copied from the Klaviyo template in the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab:

    
        ![how_to_shopifyv2_klaviyo_shopify_v2_get_template](/images/how_to_shopifyv2_klaviyo_shopify_v2_get_template.png)


        ??? example "Example: Code from Quiz Integrations tab"

            ```html
            {# ======================================= #}
            {# INFORMATION GATHERED FROM THE QUESTIONS #}
            {# ======================================= #}
            <p>
            <p>
            <b>Display quiz name</b>
            <br>
            Quiz name: {{ person|lookup:'QUIZ_NAME-YN5L9G' }}
            </p>
            <p>
            <b>Display personal information</b>
            <br>
            First name: {{ person.first_name }}
            <br>
            Last name: {{ person.last_name }}
            </p>
            </p><p><b>Display all answers for a specific block</b>
            <br>

            {# Display answer for a block of type input and ref qbi-6c4248f5 #}
            Q2: BEFORE WE BEGIN
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbi-6c4248f5-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-dd744cf3 #}
            Q3: AGE GROUP
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-dd744cf3-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-485600ce #}
            Q4: SKIN TYPE
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-485600ce-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-e8cf3180 #}
            Q9: SKIN CONCERNS
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-e8cf3180-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-329aaeff #}
            Q10: ALERGIES
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-329aaeff-YN5L9G' }}
            <br>

            {# Display answer for a block of type input and ref qbi-29f016cf #}
            Q11: WE'VE GOT YOUR RESULTS - #1 [email]
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbi-29f016cf-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-cb601cf6 #}
            Q11: WE'VE GOT YOUR RESULTS - #2 [multiple_choice]
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-cb601cf6-YN5L9G' }}
            <br>
            </p>
            ```
        
    2. When this code is copied into an HTML block in a Klaviyo template and previewd as one of the quiz subscribes is will display a full list of all the answers.

        ![how_to_shipifyv2_klaviyo_template_answerslist1](/images/how_to_shipifyv2_klaviyo_template_answerslist1.png)

    3. If you want to show specific answers in your email template, you can copy parts of the code. 
    
        !!! example "Example: Display Answer for Q3: AGE GROUP"

            For example, you can use `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-dd744cf3-YN5L9G' }}` to  display answer for Q3: AGE GROUP (ref qbc-dd744cf3).

            Here's how to use it in a Klaviyo template text block:

            ![how_to_shipifyv2_klaviyo_template_answerslist2](/images/how_to_shipifyv2_klaviyo_template_answerslist2.png)

        !!! info "Sample Answer Object Structure"

            In this example, here's how to get answers for a specific question:

            Quiz name: `{{ person|lookup:'QUIZ_NAME-YN5L9G' }}`

            First name: `{{ person.first_name }}`

            Last name: `{{ person.last_name }}`

            Q2: BEFORE WE BEGIN: `{{ person|lookup:'ANSWER_BY_BLOCK-qbi-6c4248f5-YN5L9G' }}`

            Q3: AGE GROUP: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-dd744cf3-YN5L9G' }}`

            Q4: SKIN TYPE: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-485600ce-YN5L9G' }}`

            Q9: SKIN CONCERNS: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-e8cf3180-YN5L9G' }}`

            Q10: ALERGIES: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-329aaeff-YN5L9G' }}`

            Q11: WE'VE GOT YOUR RESULTS - #1 [email]: `{{ person|lookup:'ANSWER_BY_BLOCK-qbi-29f016cf-YN5L9G' }}`
            
            Q11: WE'VE GOT YOUR RESULTS - #2 [multiple_choice]: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-cb601cf6-YN5L9G' }}`

    ### Example 3 - Display Link to Quiz Results

    Use the `RESPONSE_ID-QuizID` to create a link to the quiz results page. 
    
    1. Just add `#response-{{ person|lookup:'RESPONSE_ID-QuizID' }}` to the end of your results page href attribute in any link or URL. 

        !!! example "Example: Link to Quiz Results"

            `<a href="https://yourwebsite.com/#response-{{ person|lookup:'RESPONSE_ID-Gli0KD' }}">View your quiz results</a>`

            where `Gli0KD` is the quiz ID and

            - `{{ person|lookup:'RESPONSE_ID-Gli0KD' }}` fetches the dynamic response ID (e.g., eVgV0Y).




=== "Shopify (Legacy)"

    In this example, we’re using our quiz ID `dbqHqN`, which you’ll need to replace for your quiz ID. Here is the code for reference:

    ??? example "Example: Basic Slots Template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example demonstrated that you can not only include custom properties that are passed from the quiz to your Klaviyo account, but you can also use `IF-ELSE` conditional statements to show/hide content based on the customer’s responses to the quiz.

    !!! note "Note: Counting Products"

        Note that when looping through the products, the **count starts in 0 (zero)**, so for example, if you were to display the name of 3 products in a slot you’d have to do it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-dbqHqN) & enter your email to see a demo.
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing) – take [this quiz](https://skincarequiz.myshopify.com/#quiz-rkHm6Y) & enter your email to see a demo.
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-aMnHBw) & enter your email to see a demo.

    !!! warning "Note: These templates won’t work as is"

        Bear in mind that these templates (unlike the one generated from the Connect > Klaviyo tab) won’t work as is. They were created for a sample quiz. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "WooCommerce"

    In this example, we’re using our quiz ID `dbqHqN`, which you’ll need to replace for your quiz ID. Here is the code for reference:

    ??? example "Example: Basic Slots Template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example demonstrated that you can not only include custom properties that are passed from the quiz to your Klaviyo account, but you can also use `IF-ELSE` conditional statements to show/hide content based on the customer’s responses to the quiz.

    !!! note "Note: Counting Products"

        Note that when looping through the products, the **count starts in 0 (zero)**, so for example, if you were to display the name of 3 products in a slot you’d have to do it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-dbqHqN) & enter your email to see a demo.
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing) – take [this quiz](https://skincarequiz.myshopify.com/#quiz-rkHm6Y) & enter your email to see a demo.
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-aMnHBw) & enter your email to see a demo.

    !!! warning "Note: These templates won’t work as is"

        Bear in mind that these templates (unlike the one generated from the Connect > Klaviyo tab) won’t work as is. They were created for a sample quiz. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "Magento"

    In this example, we’re using our quiz ID `dbqHqN`, which you’ll need to replace for your quiz ID. Here is the code for reference:

    ??? example "Example: Basic Slots Template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example demonstrated that you can not only include custom properties that are passed from the quiz to your Klaviyo account, but you can also use `IF-ELSE` conditional statements to show/hide content based on the customer’s responses to the quiz.

    !!! note "Note: Counting Products"

        Note that when looping through the products, the **count starts in 0 (zero)**, so for example, if you were to display the name of 3 products in a slot you’d have to do it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-dbqHqN) & enter your email to see a demo.
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing) – take [this quiz](https://skincarequiz.myshopify.com/#quiz-rkHm6Y) & enter your email to see a demo.
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-aMnHBw) & enter your email to see a demo.

    !!! warning "Note: These templates won’t work as is"

        Bear in mind that these templates (unlike the one generated from the Connect > Klaviyo tab) won’t work as is. They were created for a sample quiz. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "BigCommerce"

    In this example, we’re using our quiz ID `dbqHqN`, which you’ll need to replace for your quiz ID. Here is the code for reference:

    ??? example "Example: Basic Slots Template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example demonstrated that you can not only include custom properties that are passed from the quiz to your Klaviyo account, but you can also use `IF-ELSE` conditional statements to show/hide content based on the customer’s responses to the quiz.

    !!! note "Note: Counting Products"

        Note that when looping through the products, the **count starts in 0 (zero)**, so for example, if you were to display the name of 3 products in a slot you’d have to do it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-dbqHqN) & enter your email to see a demo.
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing) – take [this quiz](https://skincarequiz.myshopify.com/#quiz-rkHm6Y) & enter your email to see a demo.
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-aMnHBw) & enter your email to see a demo.

    !!! warning "Note: These templates won’t work as is"

        Bear in mind that these templates (unlike the one generated from the Connect > Klaviyo tab) won’t work as is. They were created for a sample quiz. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "Standalone"

    In this example, we’re using our quiz ID `dbqHqN`, which you’ll need to replace for your quiz ID. Here is the code for reference:

    ??? example "Example: Basic Slots Template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example demonstrated that you can not only include custom properties that are passed from the quiz to your Klaviyo account, but you can also use `IF-ELSE` conditional statements to show/hide content based on the customer’s responses to the quiz.

    !!! note "Note: Counting Products"

        Note that when looping through the products, the **count starts in 0 (zero)**, so for example, if you were to display the name of 3 products in a slot you’d have to do it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-dbqHqN) & enter your email to see a demo.
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing) – take [this quiz](https://skincarequiz.myshopify.com/#quiz-rkHm6Y) & enter your email to see a demo.
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing) – take [this quiz](https://revenuehunt.com/faqs/sending-leads-to-klaviyo-account/#quiz-aMnHBw) & enter your email to see a demo.

    !!! warning "Note: These templates won’t work as is"

        Bear in mind that these templates (unlike the one generated from the Connect > Klaviyo tab) won’t work as is. They were created for a sample quiz. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

### Pull Product Information Directly from Shopify

There’s a feature in Klaviyo that allows you to pull the product information directly from Shopify by providing the id. This way you don’t need to use the `description` or `image_url` that is provided by revenuehunt, but can pull it directly from Shopify by providing the origin_id of the product. More information about this function can be found [here](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag).

## Disconnect Klaviyo

=== "Shopify"

    There are two ways to stop sending quiz data to Klaviyo, depending on whether you want to stop a single quiz or disconnect Klaviyo from your entire RevenueHunt account.

    **Option 1: Disconnect a single quiz**

    If you only want one specific quiz to stop sending data to Klaviyo (while other quizzes in your account keep working):

    1. Open the [Quiz Settings](/reference/quiz-builder/quiz-settings/) of the quiz you want to disconnect.
    2. Go to the `Integrations` tab, find the Klaviyo section, and uncheck the `Send Quiz Leads to Klaviyo Profiles` checkbox.
    3. Save your changes.

    No more quiz data will flow from that specific quiz to Klaviyo. Other quizzes in your account will continue to send data normally.

    **Option 2: Disconnect Klaviyo from your entire RevenueHunt account**

    If you want to completely revoke the Klaviyo connection across your whole RevenueHunt account:

    1. Open [Quiz Settings](/reference/quiz-builder/quiz-settings/) and go to the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab.
    2. Scroll to Klaviyo and click `Disconnect`.
    3. Confirm the action.

    The changes will save automatically. No more quiz data will flow to Klaviyo from any quiz in your account. To reconnect later, simply click `Connect` again and complete the OAuth flow.

=== "Shopify (Legacy)"

=== "WooCommerce"

=== "Magento"

=== "BigCommerce"

=== "Standalone"

---
By following this article, you can set up your post-quiz email flow with Klaviyo.

