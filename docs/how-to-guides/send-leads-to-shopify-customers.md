---
description: "Learn how to automatically send RevenueHunt quiz leads to your Shopify Customers list."
icon: simple/shopify
---

# How to Send Quiz Leads to Shopify Customers

You can add new customers automatically to your Shopify Customers list every time someone completes the quiz. Once someone leaves their email in the quiz, their Shopify Customer profile will be updated with their name, email, phone number and [customer tags](/reference/quiz-builder/customer-tags/).

This article explains how to connect your quiz to Shopify Customers and tag each customer by their answers. It also covers building a Shopify Flow that acts on those tags.

## Link quiz to Shopify customers

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=73adkkO2JrAX-wY0&amp;start=75" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Before you begin"

        **Make sure your quiz has an email question.** Without one, the app cannot send anything to Shopify Customers or Shopify Flow.

        **(optional) Tag choices with customer tags.** Customer tags are copied to the Shopify Customer profile, where you can use them for retargeting.

    1. Navigate to [App settings](/reference/app-settings/) from the side menu.
    2. Click on the `Shopify Customers` tab.
    3. Toggle the `Enable pushing quiz leads to Shopify Customers` switch to enable the integration.

        ![manual_shopifyV2_appsettings_shopifycustomers](/images/manual_shopifyV2_appsettings_shopifycustomers.png)
    4. Click the `Save` button to save the changes.

    Newly captured leads will appear in your Shopify Customers List with their [Customer tags](/reference/quiz-builder/customer-tags/) added to their profile.

    ![how to send leads to shopify customers customer profile](/images/how_to_shopifyv2_send_leads_to_shopify_customers_customer_profile.png)

    !!! note

        This is a global setting that applies to all quizzes in your shop.

    !!! note

        If a profile with the same email already exists, it will simply be updated with the customer tags from the quiz.

        Customer tags are added every time a customer takes the quiz. Tags from previous attempts are kept, so a customer who retakes the quiz and picks different answers will hold the tags from both attempts.

    !!! note

        Customer tags are sent to Shopify exactly as you named them in the quiz builder, with no prefix added. A choice tagged `teen` appears on the Shopify profile as `teen`. Use that same name when you reference the tag in a Shopify Flow condition.




=== "Shopify (Legacy)"

    1. Open your quiz and click the [Connect](/reference/quiz-builder/connect-integrations/) tab at the top of the screen. It lists the third-party services you can connect to.
    2. Click the `Connect` button in the `Shopify Customers` section. This authorizes the app to write to your Shopify Customers list.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

    Newly captured leads will appear in your Shopify Customers List with their [Customer Tags](/reference/quiz-builder/customer-tags/) added to their profile.

    ![how to send leads to shopify customers customer profile](/images/how_to_send_leads_to_shopify_customers_customer_profile.png)

    !!! note

        If a profile with the same email already exists, it will simply be updated with the customer tags from the quiz.

        Customer tags are updated every time a customer takes the quiz.

    !!! note

        Tags coming from the quiz will have a `prq_` prefix added. So if you created a tag called `teen` in Shopify profile, it will be available as `prq_teen`.


=== "WooCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Magento"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Standalone"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).




## What data is sent to Shopify customers?

When someone completes the quiz and leaves their email address, the app creates or updates a customer in your Shopify admin with the data below.

=== "Shopify"

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, used to match or create the profile. |
    | `firstName` | The customer's first name. |
    | `lastName` | The customer's last name. |
    | `phone` | The customer's phone number. |
    | Tags | All [tags](/reference/quiz-builder/customer-tags/) assigned in the quiz, added to the customer's Shopify tags. |
    | `emailMarketingConsent` | Set to `SUBSCRIBED` when the customer gives email marketing consent in the quiz. |
    | `smsMarketingConsent` | Set to `SUBSCRIBED` when a phone number is provided and the customer gives SMS consent. |

    !!! info "Opt-in level"
        Whether the subscription is recorded as single or confirmed opt-in depends on your settings in the quiz editor. See [Change subscribed/consent status](#change-subscribedconsent-status-for-email-and-phone-questions) and [how to ask for marketing consent](/how-to-guides/ask-for-marketing-consent/).

    !!! tip "Shopify Flow receives much more"
        The customer profile holds identity, tags and consent only. The `Quiz Completed` trigger for [Shopify Flow](/how-to-guides/automate-quiz-completions-with-shopify-flow/) carries the whole response. That means every answer with its question title, block reference and choice references. It also carries the variable scores, the results page, and each recommended product with its product and variant GIDs, price, URL, rank and slot. See [What data is sent](/how-to-guides/automate-quiz-completions-with-shopify-flow/#what-data-is-sent) for the complete field list.

=== "Shopify (Legacy)"

    | Field | Value |
    | --- | --- |
    | `email` | The customer's email address, used to match or create the profile. |
    | `first_name` | The customer's first name. |
    | `last_name` | The customer's last name. |
    | `phone` | The customer's phone number. |
    | Tags | All [tags](/reference/quiz-builder/customer-tags/) assigned in the quiz, appended with the `prq_` prefix, for example `prq_Oily-Skin`. |
    | `accepts_marketing` | Set to `true`. |
    | Metafield `prq.response_permalink` | URL of the customer's most recent results page. |

    !!! info "Quiz tags are refreshed on every completion"
        The app finds the existing tags carrying the `prq_` prefix and replaces them with the tags from the newest response. The profile therefore holds the customer's most recent answers, rather than the tags from every retake.

    !!! warning "No native Shopify Flow trigger"
        The legacy version has no `Quiz Completed` trigger. To automate on quiz completions you have two options:

        - **Trigger on customer tags.** Use Shopify's `Customer tags added` trigger and match one of the `prq_` tags. See [Set up Shopify Flow](#set-up-shopify-flow).
        - **Use Zapier.** Connect the quiz to [Zapier](/how-to-guides/send-leads-to-zapier/), which receives the full response and can act on it or push data back to Shopify.

=== "WooCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Magento"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Standalone"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

??? info "Legacy vs Built for Shopify: what reaches Shopify"

    | Feature | Legacy | Built for Shopify |
    | :--- | :--- | :--- |
    | Customer tags | Appended with the `prq_` prefix, and old prefixed tags are reset on each completion | Appended directly, with no prefix |
    | Metafields | Saves the results permalink to the `prq.response_permalink` metafield | Does not write to metafields |
    | Shopify Flow | No native trigger, so trigger on customer tags or use Zapier | Native `Quiz Completed` trigger carrying the full response |
    | Consent | Simple `accepts_marketing: true` | `SUBSCRIBED` status for email and SMS, with opt-in levels |

## Change subscribed/consent status for email and phone questions

=== "Shopify"

    Every contact the quiz adds to the Shopify Customers list is **marked as subscribed**, with consent to marketing recorded. You cannot change that default.

    You can still ask the customer for marketing consent inside the quiz.

    !!! tip

        Check [how to ask for marketing/data processing consent](/how-to-guides/ask-for-marketing-consent/) to learn how to ask for marketing consent directly in the quiz.


=== "Shopify (Legacy)"

    Every contact the quiz adds to the list is **marked as subscribed**, with consent to marketing recorded. Change that in the email and phone question settings.

    1. To change the default Consent state and Opt-in level, go to the email or phone question in the [Quiz Builder](/reference/quiz-builder/questions/).
    2. Open the [question settings](/reference/quiz-builder/questions/#question-settings).

        ![how_to_send_leads_to_shopify_customers_consent.png](/images/how_to_send_leads_to_shopify_customers_consent.png)

        - Under `Consent state`, you can select either `subscribed` or `non-subscribed`.

        - Under `Opt-in level`, you can select either `confirmed_opt_in` or `single_opt_in` (pick this option if you only want to send the one results email to the customer).

    3. Click the `Publish` button to update the preview/live quiz with new settings.

=== "WooCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Magento"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Standalone"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

## Tag quiz choices to segment Shopify customers

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=Bpvc82ZhqPbLf5kL&amp;start=38" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    Use [Customer tags](/reference/quiz-builder/customer-tags/) to carry a customer's answers onto their Shopify Customer profile.

    Follow these steps to add tags to your quiz choices and test the setup:

    1. **Adding Tags to Quiz Choices**: To add tags to your quiz choices, follow these steps:

        - Open the RevenueHunt app and select your quiz.
        - Navigate to the choice settings section.
        - Under [Customer tags](/reference/quiz-builder/customer-tags/), create new tags for each choice. For example, create a tag called `teen` and assign it to the relevant choice.
        - Repeat for the other choices, for example tagging another with `30s`.
        - Add one common tag, such as `quiz`, to every choice in a single question. Everyone who finishes the quiz then carries that tag.
    2. **Saving Changes**: After adding the desired tags, click `Save` to save your changes.
    3. **Test the quiz**: `Preview` the quiz using the same or a new email to test the tagging functionality.
    4. **Refresh the Shopify Customers list**: refresh it to see the new leads arrive.
    5. **View the customer tags**: open a customer's profile to see their name, email and the tags from the quiz.

    ![how to send leads to shopify customers customer profile](/images/how_to_shopifyv2_send_leads_to_shopify_customers_customer_profile.png)

    You can then use these tags to [create a Shopify email Flow](#set-up-shopify-flow).



=== "Shopify (Legacy)"

    Use [Customer Tags](/reference/quiz-builder/customer-tags/) to carry a customer's answers onto their Shopify Customer profile.

    Follow these steps to add tags to your quiz choices and test the setup:

    1. **Adding Tags to Quiz Choices**: To add tags to your quiz choices, follow these steps:

        - Open the RevenueHunt app and select your quiz.
        - Navigate to the [Customer Tags](/reference/quiz-builder/customer-tags/) section.
        - Create new tags for each choice. For example, create a tag called `teen` and assign it to the relevant choice.
        - Repeat for the other choices, tagging them `30s`, `40s`, `50s`, `60s`, `dry skin`, `oily skin` and so on.
        - Add one common tag, such as `quiz`, to every choice in a single question. Everyone who finishes the quiz then carries that tag.

    2. **Saving Changes**: After adding the desired tags, click `Publish` to save your changes.
    3. **Test the quiz**: `Preview` the quiz using the same or a new email to test the tagging functionality.
    4. **Refresh the Shopify Customers list**: refresh it to see the new leads arrive.
    5. **View the customer tags**: open a customer's profile to see their name, email and the tags from the quiz.

    !!! note

        Tags coming from the quiz will have a `prq_` prefix added. So if you created a tag called `teen` in Shopify profile, it will be available as `prq_teen`.

    ![how to send leads to shopify customers customer profile](/images/how_to_send_leads_to_shopify_customers_customer_profile.png)

    You can then use these tags to [create a Shopify email Flow](#set-up-shopify-flow).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Magento"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Standalone"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

## Set up Shopify Flow

=== "Shopify"

    Shopify Flow runs an automation after someone takes your quiz. There are two ways to start that workflow.

    ### Start from the quiz completion (recommended)

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=pPXKYHlVQqxMywSt&amp;start=132" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The `Quiz Completed` trigger starts a workflow every time a customer finishes the quiz and leaves an email address. It carries the quiz data with it. Your conditions and actions can therefore read the answers, the recommended products, the customer tags and the variable scores.

    1. Make sure your quiz has an email question, and that `Enable pushing quiz leads to Shopify Customers` is turned on. See [Link quiz to Shopify Customers](#link-quiz-to-shopify-customers). Without both, nothing reaches Flow.
    2. Install [Shopify Flow](https://admin.shopify.com/apps/flow) if your store does not have it yet. It is free.
    3. Open Shopify Flow and click `Create workflow`.
    4. Click `Select a trigger`, choose `Product Recommendation Quiz`, then `Quiz Completed`.
    5. Add the conditions and actions you want to run after a completion. Wherever a field accepts a variable, click `Add variable` to pull in the quiz data.

        !!! info

            For every field the trigger makes available, including the answers, recommendations and variable scores, see [What data is sent](/how-to-guides/automate-quiz-completions-with-shopify-flow/#what-data-is-sent).

    6. Click `Turn on workflow`.
    7. Complete your published quiz with an email address, then reopen the workflow and check its recent runs.

    RevenueHunt reports whether Shopify has seen an active workflow in `App Settings > Shopify Customers > Shopify Flow`.

    !!! tip

        For worked examples, see [Automate Quiz Completions with Shopify Flow](/how-to-guides/automate-quiz-completions-with-shopify-flow/). It covers emailing your team with the quiz results in the message, and branching on a customer tag.

    ### Start from a customer tag (alternative)

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=XKMU11jhdcuCgDYc&amp;start=280" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to shopify customers automation full cycle](/images/how_to_shopifyv2_customers_automation_full_cycle.png)

    This is the older approach. It uses Shopify's `Customer created` trigger with a condition on [customer tags](/reference/quiz-builder/customer-tags/). It therefore runs only for brand new customers, and it cannot read the quiz answers or recommendations. Use it to act on first-time customers only, or when you already have an automation built this way that still does what you need.

    1. **Open the automations list**: go to `Apps > Messaging > Automations` in your Shopify admin and click `Create automation`. Older stores may still reach the same screen from `Marketing > Automations > View templates`.
    2. Select a `Create custom automation` automation:
        ![/how to send leads to shopify customers automation1](/images/how_to_send_leads_to_shopify_customers_automation1.png)
    3. **Add a trigger**: Click anywhere and select the first trigger to be `Customer created`.
        ![how to send leads to shopify customers automation2](/images/how_to_send_leads_to_shopify_customers_automation2.png)

        This fires only for brand new customers. A customer who already exists in your Shopify Customers list is updated rather than created, so the automation does not run for them.
    4. **Select a condition**: Add a `Condition` action after the trigger. Click `Add variable` and from the list look for `customer` and then `tags`. Then, set up the condition as follows:

        **At least one customer / tags** `includes` `tags_item` `quiz`.

        ![how to send leads to shopify customers automation3](/images/how_to_shopify_customers_flow_add_conditon.gif)

        Type the tag exactly as you named it in the quiz builder.

        ![how to send leads to shopify customers automation4](/images/how_to_shopifyv2_send_leads_to_shopify_customers_automation4.png)

    5. **Set up an email**: click `Then > Action` and select `Send marketing email`. Then pick the email template you want. The email goes to every contact carrying the tag, as soon as the tag lands on their profile.
        ![how to send leads to shopify customers automation6](/images/how_to_shopify_customers_flow_add_email.gif)
    6. **Save**: click `Turn on workflow` when you have finished.
        ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)
    7. **Test it**: complete your published quiz with an email address that is not yet in your Shopify Customers list. Then open the automation and check its recent runs.

    Every customer carrying that tag is then sent the marketing email.

    !!! note

        Since 24 March 2026, marketing automations that use Shopify Messaging emails are managed in the **Shopify Messaging** app, under `Apps > Messaging > Automations`. Automations whose marketing action comes from another email app, such as Klaviyo or Seguno, remain in the **Shopify Flow** app. Existing automations kept working through the move, so you do not need to rebuild anything.

        `Send marketing email` is not a built-in Shopify Flow action. Your installed email app provides it, and it reaches only customers subscribed to marketing. Quiz leads are subscribed by default. See [Change subscribed and consent status](#change-subscribedconsent-status-for-email-and-phone-questions).

    To learn more about Shopify Automations, check their [FAQ page](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/create-marketing-automations).


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=XKMU11jhdcuCgDYc&amp;start=280" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    1. To set up a post-quiz automation, go to `Apps > Messaging > Automations` in your Shopify admin and click `Create automation`. Older stores may still reach the same screen from `Marketing > Automations > View templates`.
    2. Select a `Create custom automation` automation:
        ![/how to send leads to shopify customers automation1](/images/how_to_send_leads_to_shopify_customers_automation1.png)
    3. **Add a trigger**: Click anywhere and select the first trigger to be `Customer created`.
        ![how to send leads to shopify customers automation2](/images/how_to_send_leads_to_shopify_customers_automation2.png)
    4. **Select a condition**: Add a `Condition` action after the trigger. Click `Add variable` and from the list look for `customer` and then `tags`. Then, set up the condition as follows:

        **At least one customer / tags** `includes` `tags_item` `prq_quiz`.

        ![how to send leads to shopify customers automation3](/images/how_to_shopify_customers_flow_add_conditon.gif)

        !!! note
            You need to add the full name of the tag. For example, `prq_oilyskin` or `prq_Oily Skin`.

        ![how to send leads to shopify customers automation4](/images/how_to_send_leads_to_shopify_customers_automation4.png)

    5. **Set up an email**: click `Then > Action` and select `Send marketing email`. Then pick the email template you want. The email goes to every contact carrying the `prq_` tag, as soon as the tag lands on their profile.
        ![how to send leads to shopify customers automation6](/images/how_to_shopify_customers_flow_add_email.gif)
    6. **Save**: click `Turn on workflow` when you have finished.
        ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    Every customer carrying that `prq_` tag is then sent the marketing email.

    To learn more about Shopify Automations, check their [FAQ page](https://help.shopify.com/en/manual/promoting-marketing/create-marketing/create-marketing-automations).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Magento"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

=== "Standalone"

    !!! note "Not available on this platform"

        Shopify Customers is a Shopify feature, so this platform has no such list for the quiz to write to. To collect quiz leads here, connect a CRM or a mailing list instead. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/).

---
This article explains how to connect your quiz to Shopify Customers and set up a post-quiz email flow with Shopify Flow.

See also: [Automate Quiz Completions with Shopify Flow](/how-to-guides/automate-quiz-completions-with-shopify-flow/).