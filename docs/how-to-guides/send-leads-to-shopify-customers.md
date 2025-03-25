# How to Send Quiz Leads to Shopify Customers

You can add new customers automatically to your Shopify Customers list every time someone completes the quiz. Once someone leaves their email in the quiz, their Shopify Customer profile will be updated with their name, email, phone number and [customer tags](https://docs.revenuehunt.com/reference/quiz-builder/#customer-tags).

This article explains how to connect your quiz to Shopify Customers and build a Shopify Flow targeted at quiz takers.

## Link Quiz to Shopify Customers

=== "Shopify"

    1. Go to your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

=== "Shopify V2"

    1. Go to your quiz and click on the [Integrations](https://docs.revenuehunt.com/reference/quiz-builder/#connect-integrations) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    ![how to integrate shopify customers shopify v2](/images/how_to_integrate_shopify_customers_shopify_v2.png)
    3. Click the `Save` button to save the changes and update the preview/live quiz with new settings.

=== "WooCommerce"

    1. Go to your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

=== "Magento"

    1. Go to your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

=== "BigCommerce"

    1. Go to your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

=== "Standalone"

    1. Go to your quiz and click on the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

Newly captured leads will appear in your Shopify Customers List with their [Customer Tags](https://docs.revenuehunt.com/reference/quiz-builder/#customer-tags) added to their profile.

![how to send leads to shopify customers customer profile](/images/how_to_send_leads_to_shopify_customers_customer_profile.png)

!!! note

    If a profile with the same email already exists, it will simply be updated with the customer tags from the quiz.
    
    Customer tags are updated every time a customer takes the quiz.


## Change subscribed/consent status for email and phone questions

By default, all the contacts added to the list via the quiz will be marked as subscribed and their consent to receiving marketing information was given. You can change that in the email and phone questions settings.

1. To change the default Consent state and Opt-in level, go to the email or phone question in the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1).
2. Open the [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).

    ![how_to_send_leads_to_shopify_customers_consent.png](/images/how_to_send_leads_to_shopify_customers_consent.png)

    - Under `Consent state`, you can select either `subscribed` or `non-subscribed`.

    - Under `Opt-in level`, you can select either `confirmed_opt_in` or `single_opt_in` (pick this option if you only want to send the one results email to the customer).

3. Click the `Publish` button to update the preview/live quiz with new settings.

## Set up Shopify Automation Flow

<iframe class="alignnone size-full" title="YouTube video player" src="https://www.youtube.com/embed/GcxUgLyZUZc?si=TdE6-D4EAckWkgCj" width="100%" height="400px" frameborder="0" allowfullscreen="allowfullscreen"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start">﻿</span></iframe>


![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

1. To set up a post-quiz automation head to your `Shopify dashboard > Marketing > Automations` and click `Create Automation`.
2. Select a `Custom marketing` automation:
    ![/how to send leads to shopify customers automation1](/images/how_to_send_leads_to_shopify_customers_automation1.png)
3. **Add a trigger**: Click anywhere and select the first trigger to be `Customer created`.
    ![how to send leads to shopify customers automation2](/images/how_to_send_leads_to_shopify_customers_automation2.png)
4. **Select a condition**: Then, set up a `Condition` that `If all conditions are met > Add criteria > Customer > tags` and set up the following page with the tag that you created in the quiz (that is added to Shopify customer profiles after completing the quiz). 

    ![how to send leads to shopify customers automation3](/images/how_to_send_leads_to_shopify_customers_automation3.gif)

    !!! note

        You need to add the full name of the tag. For example, `prq_oilyskin` or `prq_Oily Skin`.

    ![how to send leads to shopify customers automation4](/images/how_to_send_leads_to_shopify_customers_automation4.png)

5. **Set up an email**: To send a follow-up email to all the quiz contacts that contain the `prq_ tag`(right after the tag is added to their profile), click `Then > Action` and from the list select `Send marketing email`. Next, select the email template you want to use.
    ![how to send leads to shopify customers automation6](/images/how_to_send_leads_to_shopify_customers_automation6.gif)
6. **Save**: Remember to save the changes.
    ![how to send leads to shopify customers automation7](/images/how_to_send_leads_to_shopify_customers_automation7.png)

Now, all the quiz takers with a specific `prq_ tag` will be sent the marketing email.

To learn more about Shopify Automations, check their [FAQ page](https://help.shopify.com/it//manual/promoting-marketing/create-marketing/create-marketing-automations).

---
By following this article, you can set up your post-quiz email flow with Shopify Flows.