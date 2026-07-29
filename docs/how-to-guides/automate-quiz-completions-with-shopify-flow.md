---
description: "Use the Quiz Completed trigger from Product Recommendation Quiz to automate actions in Shopify Flow."
icon: material/sitemap
---

# Automate Quiz Completions with Shopify Flow

The **Quiz Completed** trigger from Product Recommendation Quiz starts a Shopify Flow workflow when an identified customer completes a quiz. You can use the quiz response, answers, customer tags, recommendations, and other completion data in subsequent workflow actions.

## Before you start

The trigger runs on a Shopify customer record, not on an anonymous quiz session. RevenueHunt matches a respondent to that record using the email address they type into the quiz, which is why the first two steps below matter.

1. **Add an email question to your quiz.** Without one, no customer record is created or updated and the trigger never fires. A phone number is not enough. Make the question required if you want every completion to start a workflow run.
2. **Turn on customer syncing.** In RevenueHunt, go to **App Settings > Shopify Customers**, turn on **Enable pushing quiz leads to Shopify Customers**, and save. The **Shopify Flow** section sits on the same page, directly below that checkbox.
3. **Install [Shopify Flow](https://admin.shopify.com/apps/flow)** if your store does not have it. It is free.
4. **Publish the quiz.**

For more on customer syncing, including how marketing consent is recorded, see [How to Send Quiz Leads to Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/).

## Create the workflow

1. [Open Shopify Flow](https://admin.shopify.com/apps/flow).
2. Select **Create workflow**.
3. Select **Select a trigger**.
4. Choose **Product Recommendation Quiz** and then **Quiz Completed**.
5. Add the conditions and actions you want to run after a quiz completion.
6. Select **Turn on workflow**.

The trigger provides the Shopify customer and quiz completion data, including:

- quiz and response identifiers;
- quiz and result names;
- contact details and customer tags;
- quiz answers;
- product recommendations; and
- quiz variable scores.

The fields available in an action depend on what the customer submitted and how the quiz is configured.

!!! tip

    If you are not sure how to assemble a workflow, describe what you want in plain language and let Shopify Sidekick draft it for you in Flow.

## Example 1: Email your team after every quiz completion

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

Most workflows should not treat every respondent the same. Use a condition to split the workflow based on what someone answered, then run a different action on each side.

The cleanest thing to branch on is a [customer tag](/reference/quiz-builder/link-collections/#customer-tags), because you decide in the quiz builder exactly which answers produce which tag.

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

Before you build it, two constraints are worth knowing:

- **Marketing emails only reach subscribed customers.** If the respondent is not subscribed to marketing, the action fails for that run. Quiz leads are marked as subscribed by default, as described in [Change subscribed/consent status for email and phone questions](/how-to-guides/send-leads-to-shopify-customers/#change-subscribedconsent-status-for-email-and-phone-questions).
- **Shopify's own email automations moved.** Since 24 March 2026, marketing automations that use Shopify Messaging emails are managed in the **Shopify Messaging** app, under **Apps > Messaging > Automations**. Automations whose marketing action comes from another app stay in Shopify Flow. Existing automations kept working through the move, so nothing needs rebuilding.

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

Storing the recommendations in a metafield makes them available to your theme, but displaying them on the storefront is theme work that Flow itself does not do.

## Check the connection in RevenueHunt

Return to **RevenueHunt > App Settings > Shopify Customers** and find the **Shopify Flow** section.

![Shopify Flow section in RevenueHunt App Settings, showing the Flow not detected status and setup steps](/images/how_to_automate_quiz_completions_with_shopify_flow_settings.png)

- **Flow active** means Shopify has reported that a workflow using the **Quiz Completed** trigger from Product Recommendation Quiz is turned on.
- **Flow inactive** means a workflow was detected but is not currently turned on.
- **Flow not detected** means Shopify has not reported a workflow using this trigger yet.

Shopify may take a short time to report a workflow status change. The lifecycle timestamp shows when RevenueHunt last received an update from Shopify.

## Test the workflow

1. Complete the published quiz with an email address.
2. In Shopify Flow, open the workflow and review its recent runs.
3. Confirm that the expected conditions and actions completed successfully.

If no run appears, one of the setup steps is usually the cause. Check, in this order, that you filled in the email question during the test, that customer syncing is on, and that the workflow itself is turned on. Then complete the quiz again.

!!! note

    The **Quiz Completed** trigger is different from workflows that start with Shopify's **Customer created** trigger and filter by customer tags. Use **Quiz Completed** when you want the workflow to run directly from the Product Recommendation Quiz completion event.
