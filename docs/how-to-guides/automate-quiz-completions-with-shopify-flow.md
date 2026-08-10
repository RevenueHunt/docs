---
description: "Use the Quiz Completed trigger from Product Recommendation Quiz to automate actions in Shopify Flow."
icon: material/sitemap
---

# Automate Quiz Completions with Shopify Flow

Shopify Flow can run an automation every time someone completes your quiz, so you can follow up, segment, or update your store based on what they answered.

How the workflow starts depends on which version of the app you use. The Built for Shopify version provides a **Quiz Completed** trigger that carries the whole completion with it, so your actions can use the response, answers, customer tags, recommendations and variable scores. On the legacy version you build the same kind of automation on Shopify's **Customer created** trigger with a condition on customer tags.

=== "Shopify"

    ## Before you start

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=yEPUcXlyNLd0ecug" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The trigger runs on a Shopify customer record, not on an anonymous quiz session. RevenueHunt matches a respondent to that record using the email address they type into the quiz, which is why the first two steps below matter.

    1. **Add an email question to your quiz.** Without one, no customer record is created or updated and the trigger never fires. A phone number is not enough. Make the question required if you want every completion to start a workflow run.
    2. **Turn on customer syncing.** In RevenueHunt, go to **App Settings > Shopify Customers**, turn on **Enable pushing quiz leads to Shopify Customers**, and save. The **Shopify Flow** section sits on the same page, directly below that checkbox.
    3. **Install [Shopify Flow](https://admin.shopify.com/apps/flow)** if your store does not have it. It is free.
    4. **Publish the quiz.**

    For more on customer syncing, including how marketing consent is recorded, see [How to Send Quiz Leads to Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/).

    ## Create the workflow

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=MPGpEBEql9qPmdQ9&amp;start=132" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. [Open Shopify Flow](https://admin.shopify.com/apps/flow).
    2. Select **Create workflow**.
    3. Select **Select a trigger**.
    4. Choose **Product Recommendation Quiz** and then **Quiz Completed**.
    5. Add the conditions and actions you want to run after a quiz completion.
    6. Select **Turn on workflow**.

    The trigger carries the Shopify customer along with the full quiz completion. See [What data is sent](#what-data-is-sent) for every available field.

    !!! tip

        If you are not sure how to assemble a workflow, describe what you want in plain language and let Shopify Sidekick draft it for you in Flow.

    ## What data is sent

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=FwZ2euofue1jPKxc&amp;start=163" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    When a customer completes a quiz, RevenueHunt sends a structured payload to Shopify Flow using the `quiz-completed` trigger. The payload has two top level fields:

    - `customer_id`, the numeric Shopify customer ID; and
    - `Quiz completion`, an object holding everything about the completion.

    Under **Add variable** in any action, the quiz data is nested under `Quiz completion`. The fields you actually see depend on what the respondent submitted and how the quiz is configured.

    ### Completion fields

    | Field | Description |
    | --- | --- |
    | `eventId` | A stable ID for deduplication, in the form `quiz-completed:<response-sqid>` |
    | `schemaVersion` | The payload schema version, currently `1.0` |
    | `responseId`, `quizId` | Internal RevenueHunt identifiers |
    | `quizName` | The name of the quiz |
    | `completedAt` | ISO 8601 UTC timestamp of the completion |
    | `email` | The customer's email address. Always present, since the trigger requires it |
    | `phone`, `firstName`, `lastName`, `fullName` | Contact details, when the quiz captured them |
    | `resultRef`, `resultName` | Identifiers for the specific quiz result the respondent reached |
    | `tags` | A list of all customer tags associated with the response |
    | `marketId` | The market identifier |
    | `highestVariableRef` | The reference of the variable with the highest score |
    | `recommendationsIncomplete` | `true` when product data was partially missing at delivery |

    ### `answers`

    A list with one object per answered question.

    | Field | Description |
    | --- | --- |
    | `questionRef`, `questionTitle` | Reference and title of the question |
    | `blockRef`, `answerType` | Reference of the block and the type of answer it collects |
    | `value` | The answer itself, stringified |
    | `choiceRefs`, `choiceLabels` | The choices picked, for multiple choice questions |
    | `position` | Order of the question in the quiz |

    ### `recommendations`

    A list of the recommended products or items.

    | Field | Description |
    | --- | --- |
    | `slotRef` | The slot identifier |
    | `itemId`, `productId`, `variantId` | Product identifiers |
    | `title`, `url` | The product title and link |
    | `rank`, `score` | Position in the recommendation list and its matching score |
    | `price`, `currency` | The price and its currency |

    ### `variableScores`

    A list of the calculated [variable](/tutorials/conditional-logic/) scores.

    | Field | Description |
    | --- | --- |
    | `variableRef` | The reference of the variable |
    | `score` | Its calculated score |

    !!! warning "Limits and eligibility"

        - **The trigger fires only when the response has an email address and the Shopify customer was created or updated successfully.** Completions without an email produce no workflow run.
        - **The payload is capped at 45 KB**, to stay inside Shopify's 50 KB limit. If a completion would exceed that, data is pruned automatically in this order: first the recommendation metadata (URLs and prices), then the oldest answers, and finally `recommendationsIncomplete` is set to `true`. A long quiz with many recommendations is the usual cause, so do not rely on every optional field being present in every run.

    ## Example 1: Email your team after every quiz completion

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=DWLjT4VJK--eRFyR&amp;start=188" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This is the fastest way to prove the whole chain works, because you control both ends and you see the quiz data arrive in your inbox.

    1. Create a workflow with the **Quiz Completed** trigger.
    2. Under the trigger, select the **+** button and choose **Action**.
    3. Search for `Send internal email` and select it.
    4. In **Email address**, type the address that should receive the notification, for example your own. To notify several people, separate the addresses with commas.

        !!! warning

            The recipient must be a fixed address. Shopify does not let you insert a variable here, so you cannot use this action to email the quiz respondent. It is built for notifying staff.

    5. In **Subject**, type the static part of your subject line, for example `Quiz completed by`.
    6. Place your cursor where the dynamic part should go, select **Add variable**, and pick the field you want. To identify the respondent and the quiz, insert the customer's first name and the quiz name.
    7. In **Message**, write the body of the email the same way, mixing text with **Add variable**. This is where the quiz completion data is worth using, for example the product recommendations, so the email lists the recommended product titles with their price or URL.
    8. Select **Turn on workflow**.
    9. Complete your published quiz with a real email address and check your inbox.

    The result is an email such as *"Skincare Quiz completed by Anna"*, listing the products the quiz recommended to her.

    !!! tip

        Formatting in the message body is up to you. Add line breaks and labels around the variables so the email stays readable once several fields are filled in.

    ## Example 2: Branch on a quiz answer

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=HhUhmbUvsSC7awe4&amp;start=233" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Most workflows should not treat every respondent the same. Use a condition to split the workflow based on what someone answered, then run a different action on each side.

    The cleanest thing to branch on is a [customer tag](/reference/quiz-builder/link-collections/#customer-tags), because you decide in the quiz builder exactly which answers produce which tag.

    **First, tag the choices you want to branch on**

    1. Open the RevenueHunt app and select your quiz.
    2. Click the choice you want to tag to open its settings.
    3. Under [Customer Tags](/reference/quiz-builder/customer-tags/), create a new tag or pick an existing one. For example, tag the dry skin choice with `dry skin`.
    4. Repeat for the other choices you want to identify later.
    5. Add a common tag such as `quiz` to every choice in one of the questions, so that all participants carry it.
    6. Click `Save`.

    Every tag attached to the choices a respondent picks is written to their Shopify customer profile, and arrives with the trigger.

    **Then build the condition**

    1. Under the trigger, select the **+** button and choose **Condition**.
    2. Select **Add variable**.
    3. Search for `tags` and select the tags field belonging to the quiz completion. Flow lists variables in dot notation, so read the full path before selecting, since several unrelated `tags` fields exist.
    4. Because tags are a list, set the list operator to **At least one of**.
    5. Leave the field operator as **Equal to** and type the tag exactly as you named it in the quiz builder, for example `dry skin`.

        !!! note

            Tags are sent to Shopify with no prefix, so the value here is the same string you typed into the quiz builder. Match the spelling and the spacing.

    6. Check the plain language summary Flow displays above the condition. It should read as the rule you intended.
    7. Attach an action to the **True** branch, for example an email about your dry skin range.
    8. Attach a different action to the **False** branch, or leave it empty to end the workflow there.
    9. Select **Turn on workflow**.

    To test both sides, complete the quiz twice, once choosing the answer that carries the tag and once choosing an answer that does not.

    ## Send a marketing email to the respondent

    **Send internal email** cannot email the person who took the quiz. To do that you need a marketing email action, and that action is not built into Shopify Flow. It is contributed by whichever email app you have installed, so the name you search for depends on your setup, for example Shopify Messaging, Klaviyo, or Seguno.

    !!! warning

        Marketing emails only reach customers who are subscribed to marketing. If the respondent is not subscribed, the action fails for that run. Quiz leads are marked as subscribed by default, as described in [Change subscribed/consent status for email and phone questions](/how-to-guides/send-leads-to-shopify-customers/#change-subscribedconsent-status-for-email-and-phone-questions).

    !!! info "Shopify's own email automations moved"

        Since 24 March 2026, marketing automations that use Shopify Messaging emails are managed in the **Shopify Messaging** app, under **Apps > Messaging > Automations**. Automations whose marketing action comes from another app stay in Shopify Flow. Existing automations kept working through the move, so nothing needs rebuilding.

    To add one:

    1. Under the trigger or on a condition branch, select the **+** button and choose **Action**.
    2. Search for the sending action provided by your email app.
    3. Select the template or campaign you want to send.
    4. Select **Turn on workflow**.

    ## Other actions worth combining with the trigger

    Everything below is built into Shopify Flow, so it is available without installing anything else.

    | Action | Typical use with quiz data |
    | --- | --- |
    | **Add customer tags** | Build a segment from a quiz answer, or mark that someone has taken a particular quiz |
    | **Remove customer tags** | Clear a previous answer when a customer retakes the quiz |
    | **Update customer note** or a customer metafield | Store the recommended products on the profile so your team, or your theme, can read them later |
    | **Send HTTP request** or **Send Admin API request** | Pass the completion to a system that has no Flow app |
    | **Wait** | Delay a follow-up, for example send a reminder three days after the quiz |
    | **Condition** | Branch on tags, answers, or quiz variable scores, as in Example 2 |

    !!! note

        Storing the recommendations in a metafield makes them available to your theme, but displaying them on the storefront is theme work that Flow itself does not do.

    ## Check the connection in RevenueHunt

    Return to **RevenueHunt > App Settings > Shopify Customers** and find the **Shopify Flow** section.

    ![Shopify Flow section in RevenueHunt App Settings, showing the Flow not detected status and setup steps](/images/how_to_automate_quiz_completions_with_shopify_flow_settings.png)

    - **Flow active** means Shopify has reported that a workflow using the **Quiz Completed** trigger from Product Recommendation Quiz is turned on.
    - **Flow inactive** means a workflow was detected but is not currently turned on.
    - **Flow not detected** means Shopify has not reported a workflow using this trigger yet.

    !!! note

        Shopify may take a short time to report a workflow status change. The lifecycle timestamp shows when RevenueHunt last received an update from Shopify.

    ## Test the workflow

    1. Complete the published quiz with an email address.
    2. In Shopify Flow, open the workflow and review its recent runs.
    3. Confirm that the expected conditions and actions completed successfully.

    If no run appears, one of the setup steps is usually the cause. Check, in this order, that you filled in the email question during the test, that customer syncing is on, and that the workflow itself is turned on. Then complete the quiz again.

    !!! note

        The **Quiz Completed** trigger is different from workflows that start with Shopify's **Customer created** trigger and filter by customer tags. Use **Quiz Completed** when you want the workflow to run directly from the Product Recommendation Quiz completion event.

=== "Shopify (Legacy)"

    !!! warning

        The **Quiz Completed** trigger is **not available** in the legacy version of the app. It is provided by the Built for Shopify version of RevenueHunt only.

    You can still automate what happens after a quiz, using Shopify's own `Customer created` trigger with a condition on customer tags. The workflow starts when the quiz creates a new customer, rather than on the quiz completion itself, so quiz answers, recommendations and variable scores are not available inside the actions.

    <iframe class="alignnone size-full" title="YouTube video player" src="https://www.youtube.com/embed/hPtJ5VxCM2M?si=YGAUsV3-zNMjQZWK&amp;start=279" width="100%" height="400px" frameborder="0" allowfullscreen="allowfullscreen"><span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce_SELRES_start">﻿</span></iframe>

    ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    **Step 1: Connect the quiz to Shopify Customers**

    Your quiz must contain an email question. Without one, no customer is created and the automation has nothing to run on.

    1. Go to your quiz and click on the [Connect](/reference/quiz-builder/connect-integrations/) tab on the top of the screen.
    2. Click the `Connect` button in the `Shopify Customers` section. This authorizes our app to connect with your Shopify Customers List.
    3. Click the `Publish` button to save the changes and update the preview/live quiz with new settings.

    **Step 2: Tag your quiz choices**

    1. Open your quiz and navigate to the [Customer Tags](/reference/quiz-builder/customer-tags/) section.
    2. Create a tag for each choice you want to identify later. For example, create a tag called `teen` and assign it to the relevant choice.
    3. Add a common tag such as `quiz` to all choices in one of the questions, so that everyone who takes the quiz carries it.
    4. Click `Publish` to save your changes.

    !!! note

        Tags coming from the quiz will have a `prq_` prefix added. So if you created a tag called `teen`, in the Shopify profile it will be available as `prq_teen`.

    **Step 3: Build the automation**

    1. To set up a post-quiz automation head to `Apps > Messaging > Automations` in your Shopify admin and click `Create automation`. Older stores may still reach the same screen from `Marketing > Automations > View templates`.
    2. Select a `Create custom automation` automation:
        ![/how to send leads to shopify customers automation1](/images/how_to_send_leads_to_shopify_customers_automation1.png)
    3. **Add a trigger**: Click anywhere and select the first trigger to be `Customer created`.
        ![how to send leads to shopify customers automation2](/images/how_to_send_leads_to_shopify_customers_automation2.png)

        !!! warning

            This fires only for brand new customers. A respondent who already exists in your Shopify Customers list is updated rather than created, so the automation does not run for them.
    4. **Select a condition**: Add a `Condition` action after the trigger. Click `Add variable` and from the list look for `customer` and then `tags`. Then, set up the condition as follows:

        **At least one customer / tags** `includes` tags_item  `prq_quiz`.

        ![how to send leads to shopify customers automation3](/images/how_to_shopify_customers_flow_add_conditon.gif)

        !!! note

            You need to add the full name of the tag. For example, `prq_oilyskin` or `prq_Oily Skin`.

        ![how to send leads to shopify customers automation4](/images/how_to_send_leads_to_shopify_customers_automation4.png)

    5. **Set up an email**: To send a follow-up email to all the quiz contacts that contain the `prq_ tag` (right after the tag is added to their profile), click `Then > Action` and from the list select `Send marketing email`. Next, select the email template you want to use.
        ![how to send leads to shopify customers automation6](/images/how_to_shopify_customers_flow_add_email.gif)
    6. **Save**: Remember to `Turn on workflow` once you're done with making the changes.
        ![how to shopify customers automation full cycle](/images/how_to_shopify_customers_automation_full_cycle.png)

    **Step 4: Test it**

    Complete your published quiz with an email address that does not exist in your Shopify Customers list yet, then open the automation and check its recent runs.

    Now, all the quiz takers with a specific `prq_ tag` will be sent the marketing email.

    To learn more about Shopify Automations, check their [FAQ page](https://help.shopify.com/it//manual/promoting-marketing/create-marketing/create-marketing-automations).

    !!! tip

        Upgrading to the Built for Shopify version of the app gives you the **Quiz Completed** trigger, drops the `prq_` prefix from your tags, and makes the full quiz completion available to your workflow actions. See [Migrate a Legacy Quiz to Built for Shopify](/how-to-guides/migrate-shopify-legacy-quiz/).

    For the same walkthrough in context, see the **Shopify (Legacy)** tab of [Set up Shopify Flow](/how-to-guides/send-leads-to-shopify-customers/#set-up-shopify-flow).

=== "WooCommerce"

    Not applicable. Shopify Flow is a Shopify product.

    To automate follow-ups on WooCommerce, connect your quiz to an email or CRM service instead. See [How to Send Quiz Leads to Your CRM](/how-to-guides/send-leads-to-crm/).

=== "Magento"

    Not applicable. Shopify Flow is a Shopify product.

    To automate follow-ups on Magento, connect your quiz to an email or CRM service instead. See [How to Send Quiz Leads to Your CRM](/how-to-guides/send-leads-to-crm/).

=== "BigCommerce"

    Not applicable. Shopify Flow is a Shopify product.

    To automate follow-ups on BigCommerce, connect your quiz to an email or CRM service instead. See [How to Send Quiz Leads to Your CRM](/how-to-guides/send-leads-to-crm/).

=== "Standalone"

    Not applicable. Shopify Flow is a Shopify product.

    To automate follow-ups on a Standalone quiz, connect it to an email or CRM service instead. See [How to Send Quiz Leads to Your CRM](/how-to-guides/send-leads-to-crm/).
