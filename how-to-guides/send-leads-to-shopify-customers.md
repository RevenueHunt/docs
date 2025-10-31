# How to Send Quiz Leads to Shopify Customers

You can add new customers automatically to your Shopify Customers list every time someone completes the quiz. Once someone leaves their email in the quiz, their Shopify Customer profile will be updated with their name, email, phone number and [customer tags](/reference/quiz-builder/link-collections/#customer-tags).

This article explains how to connect your quiz to Shopify Customers and build a Shopify Flow targeted at quiz takers.

## Link Quiz to Shopify Customers

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Lg6Ikql0kpE?si=slsLm93N-0Ce2uch" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Go to your quiz and click on the [Integrations](/reference/quiz-builder/connect-integrations/) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    ![how to integrate shopify customers built for shopify revenuehunt app](/images/how_to_integrate_shopify_customers_shopify_v2.png)
    3. Click the `Save` button to save the changes and update the preview/live quiz with new settings.

    Newly captured leads will appear in your Shopify Customers List with their [Customer Tags](/reference/quiz-builder/link-collections/#customer-tags) added to their profile.

    ![how to send leads to shopify customers customer profile](/images/how_to_shopifyv2_send_leads_to_shopify_customers_customer_profile.png)

    !!! note

        If a profile with the same email already exists, it will simply be updated with the customer tags from the quiz.
        
        Customer tags are updated every time a customer takes the quiz.




=== "Shopify (Legacy)"

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab on the top of the screen. This will open a tab where you can connect your quiz with multiple third-party services.
    2. Then click on the `Connect` button in the `Shopify Customers` section. This will authorize our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

    Newly captured leads will appear in your Shopify Customers List with their [Customer Tags](/reference/quiz-builder/link-collections/#customer-tags) added to their profile.

    ![how to send leads to shopify customers customer profile](/images/how_to_send_leads_to_shopify_customers_customer_profile.png)

    !!! note

        If a profile with the same email already exists, it will simply be updated with the customer tags from the quiz.
        
        Customer tags are updated every time a customer takes the quiz.

    !!! note

        Tags coming from the quiz will have a `prq_` prefix added. So if you created a tag called `teen` in Shopify profile, it will be available as `prq_teen`.


=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable. 




## Change subscribed/consent status for email and phone questions

=== "Shopify"

    By default, all the contacts added to the Shopify Customers list via the quiz **will be marked as subscribed** and their consent to receiving marketing information was given. It is not possible to change the default consent state.

    However, there are many ways you can ask the customer for marketing consent directly in the quiz. 
    
    !!! tip

        Check [this article](/how-to-guides/ask-for-marketing-consent/) to learn how to ask for marketing consent directly in the quiz.


=== "Shopify (Legacy)"

    By default, all the contacts added to the list via the quiz **will be marked as subscribed** and their consent to receiving marketing information was given. You can change that in the email and phone questions settings.

    1. To change the default Consent state and Opt-in level, go to the email or phone question in the [Quiz Builder](/reference/quiz-builder/questions/).
    2. Open the [question settings](/reference/quiz-builder/questions/#question-settings).

        ![how_to_send_leads_to_shopify_customers_consent.png](/images/how_to_send_leads_to_shopify_customers_consent.png)

        - Under `Consent state`, you can select either `subscribed` or `non-subscribed`.

        - Under `Opt-in level`, you can select either `confirmed_opt_in` or `single_opt_in` (pick this option if you only want to send the one results email to the customer).

    3. Click the `Publish` button to update the preview/live quiz with new settings.

=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

## Tag Quiz Choices to Segment Shopify Customers

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Lg6Ikql0kpE?si=gylWum-a-LN689cv&amp;start=103" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    You can use [Customer Tags](/reference/quiz-builder/link-collections/#customer-tags) to send quiz answers that the customer provided in the quiz to their Shopify Customer's profile.

    Follow these steps to add tags to your quiz choices and test the setup:

    1. **Adding Tags to Quiz Choices**: To add tags to your quiz choices, follow these steps:

        - Open the Revenue Hunt Quizzes app and select your quiz.
        - Navigate to the choice settings section.
        - Under [Customer Tags](/reference/quiz-builder/customer-tags/), create new tags for each choice. For example, create a tag called `teen` and assign it to the relevant choice.
        - Repeat this process for other choices, adding appropriate tags as needed (e.g., `30s`).
        - Additionally, add a common tag (e.g., `quiz`) to all choices in one of the questions to identify participants from the product recommendation quiz. Anyone who takes the quiz will be tagged with this common tag.
    2. **Saving Changes**: After adding the desired tags, click `Save` to save your changes.
    3. **Test the quiz**: `Preview` the quiz using the same or a new email to test the tagging functionality.
    4. **Refresh the Shopify Customers list**: Once participants complete the quiz, refresh the Shopify Customers list to see the leads being added.
    5. **View the customer tags**: Open the profile of a participant to view their name, email, and the associated customer tags from the quiz.

    ![how to send leads to shopify customers customer profile](/images/how_to_shopifyv2_send_leads_to_shopify_customers_customer_profile.png)

    You can then use these tags to [create a Shopify email Flow](#set-up-shopify-automation-flow).



=== "Shopify (Legacy)"

    You can use [Customer Tags](/reference/quiz-builder/link-collections/#customer-tags) to send quiz answers that the customer provided in the quiz to their Shopify Customer's profile.

    Follow these steps to add tags to your quiz choices and test the setup:

    1. **Adding Tags to Quiz Choices**: To add tags to your quiz choices, follow these steps:

        - Open the Revenue Hunt Quizzes app and select your quiz.
        - Navigate to the [Customer Tags](/reference/quiz-builder/customer-tags/) section.
        - Create new tags for each choice. For example, create a tag called `teen` and assign it to the relevant choice.
        - Repeat this process for other choices, adding appropriate tags as needed (e.g., `30s`, `40s`, `50s`, `60s`, `dry skin`, `oily skin`, etc.).
        - Additionally, add a common tag (e.g., `quiz`) to all choices in one of the questions to identify participants from the product recommendation quiz. Anyone who takes the quiz will be tagged with this common tag.

    2. **Saving Changes**: After adding the desired tags, click `Publish` to save your changes.
    3. **Test the quiz**: `Preview` the quiz using the same or a new email to test the tagging functionality.
    4. **Refresh the Shopify Customers list**: Once participants complete the quiz, refresh the Shopify Customers list to see the leads being added.
    5. **View the customer tags**: Open the profile of a participant to view their name, email, and the associated customer tags from the quiz.

    !!! note

        Tags coming from the quiz will have a `prq_` prefix added. So if you created a tag called `teen` in Shopify profile, it will be available as `prq_teen`.

    ![how to send leads to shopify customers customer profile](/images/how_to_send_leads_to_shopify_customers_customer_profile.png)

    You can then use these tags to [create a Shopify email Flow](#set-up-shopify-automation-flow).

=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

## Set up Shopify Automation Flow

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Lg6Ikql0kpE?si=uRcEl8jXzgtMkgnN&amp;start=174" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to shopify customers automation full cycle](/images/how_to_shopifyv2_customers_automation_full_cycle.png)

    1. To set up a post-quiz automation head to your `Shopify dashboard > Marketing > Automations`, click `View templates`.
    2. Select a `Create custom automation` automation:
        ![/how to send leads to shopify customers automation1](/images/how_to_send_leads_to_shopify_customers_automation1.png)
    3. **Add a trigger**: Click anywhere and select the first trigger to be `Customer created`.
        ![how to send leads to shopify customers automation2](/images/how_to_send_leads_to_shopify_customers_automation2.png)
    4. **Select a condition**: Add a `Condition` action after the trigger. Click `Add variable` and from the list look for `customer` and then `tags`. Then, set up the condition as follows: 
    
        **At least one customer / tags** `includes` tags_item  `quiz`.

        ![how to send leads to shopify customers automation3](/images/how_to_shopify_customers_flow_add_conditon.gif)

        ![how to send leads to shopify customers automation4](/images/how_to_shopifyv2_send_leads_to_shopify_customers_automation4.png)

    5. **Set up an email**: To send a follow-up email to all the quiz contacts that contain the `prq_ tag`(right after the tag is added to their profile), click `Then > Action` and from the list select `Send marketing email`. Next, select the email template you want to use.
        ![how to send leads to shopify customers automation6](/images/how_to_shopify_customers_flow_add_email.gif)
    6. **Save**: Remember to `Turn on workflow` once you're done with making the changes.
        ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    Now, all the quiz takers with a specific `tag` like `quiz` will be sent the marketing email.

    To learn more about Shopify Automations, check their [FAQ page](https://help.shopify.com/it//manual/promoting-marketing/create-marketing/create-marketing-automations).


=== "Shopify (Legacy)"

    <iframe class="alignnone size-full" title="YouTube video player" src="https://www.youtube.com/embed/GcxUgLyZUZc?si=TdE6-D4EAckWkgCj" width="100%" height="400px" frameborder="0" allowfullscreen="allowfullscreen"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start">﻿</span></iframe>

    ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    1. To set up a post-quiz automation head to your `Shopify dashboard > Marketing > Automations`, click `View templates`.
    2. Select a `Create custom automation` automation:
        ![/how to send leads to shopify customers automation1](/images/how_to_send_leads_to_shopify_customers_automation1.png)
    3. **Add a trigger**: Click anywhere and select the first trigger to be `Customer created`.
        ![how to send leads to shopify customers automation2](/images/how_to_send_leads_to_shopify_customers_automation2.png)
    4. **Select a condition**: Add a `Condition` action after the trigger. Click `Add variable` and from the list look for `customer` and then `tags`. Then, set up the condition as follows: 
    
        **At least one customer / tags** `includes` tags_item  `prq_quiz`.

        ![how to send leads to shopify customers automation3](/images/how_to_shopify_customers_flow_add_conditon.gif)

        !!! note
            You need to add the full name of the tag. For example, `prq_oilyskin` or `prq_Oily Skin`.

        ![how to send leads to shopify customers automation4](/images/how_to_send_leads_to_shopify_customers_automation4.png)

    5. **Set up an email**: To send a follow-up email to all the quiz contacts that contain the `prq_ tag`(right after the tag is added to their profile), click `Then > Action` and from the list select `Send marketing email`. Next, select the email template you want to use.
        ![how to send leads to shopify customers automation6](/images/how_to_shopify_customers_flow_add_email.gif)
    6. **Save**: Remember to `Turn on workflow` once you're done with making the changes.
        ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    Now, all the quiz takers with a specific `prq_ tag` will be sent the marketing email.

    To learn more about Shopify Automations, check their [FAQ page](https://help.shopify.com/it//manual/promoting-marketing/create-marketing/create-marketing-automations).

=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

---
By following this article, you can learn how to connect your quiz to Shopify Customers and set up your post-quiz email flow with Shopify Flows.