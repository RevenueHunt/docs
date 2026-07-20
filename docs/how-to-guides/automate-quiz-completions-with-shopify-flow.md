---
description: "Use the Quiz Completed trigger from Product Recommendation Quiz to automate actions in Shopify Flow."
---

# Automate Quiz Completions with Shopify Flow

The **Quiz Completed** trigger from Product Recommendation Quiz starts a Shopify Flow workflow when an identified customer completes a quiz. You can use the quiz response, answers, customer tags, recommendations, and other completion data in subsequent workflow actions.

## Before you start

You need:

- the RevenueHunt app for Shopify;
- [Shopify Flow](https://admin.shopify.com/apps/flow) installed on your store;
- Shopify Customers syncing enabled in RevenueHunt; and
- a published quiz that collects an email address.

The last two are the requirements merchants most often miss. Both are explained below.

### Why the trigger only fires for identified customers

The **Quiz Completed** trigger runs on a Shopify customer record, not on an anonymous quiz session. A quiz respondent becomes an *identified customer* when RevenueHunt can match their submission to a Shopify customer — which it does using the email address they enter in the quiz.

This has two practical consequences:

- **Your quiz must contain an email question.** Without one, RevenueHunt has nothing to match on, no customer record is created or updated, and the trigger never fires. A phone number alone is not enough.
- **Respondents who skip the email question will not trigger the workflow.** If the email question is optional, only the respondents who actually fill it in will start a workflow run. Make the email question required if you want every completion to trigger Flow.

If you are testing and no workflow run appears, this is the first thing to check.

### Requirement: enable customer syncing

The trigger depends on RevenueHunt pushing quiz respondents into Shopify as customers. If that setting is off, quizzes still work and responses are still recorded in RevenueHunt, but nothing reaches Shopify Flow.

To enable customer syncing:

1. In RevenueHunt, go to **App Settings**.
2. Open **Shopify Customers**.
3. Turn on **Enable pushing quiz leads to Shopify Customers**.
4. Save your changes.

The **Shopify Flow** section lives on this same page, directly below the checkbox.

For more information about customer syncing, including how marketing consent is recorded, see [How to Send Quiz Leads to Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/).

### Requirements at a glance

| Requirement | Where to set it | What happens if it is missing |
| --- | --- | --- |
| An email question in the quiz | Quiz builder | No customer is identified, so the trigger never fires |
| Respondent enters their email | Quiz respondent | That particular completion does not start a workflow run |
| **Enable pushing quiz leads to Shopify Customers** | App Settings > Shopify Customers | Nothing is sent to Shopify at all |
| A workflow using the **Quiz Completed** trigger, turned on | Shopify Flow | RevenueHunt reports **Flow not detected** |

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

## Check the connection in RevenueHunt

Return to **RevenueHunt > App Settings > Shopify Customers** and find the **Shopify Flow** section.

![Shopify Flow section in RevenueHunt App Settings, showing the Flow not detected status and setup steps](/images/how_to_automate_quiz_completions_with_shopify_flow_settings.png)

- **Active** means Shopify has reported that a workflow using the **Quiz Completed** trigger from Product Recommendation Quiz is turned on.
- **Inactive** means a workflow was detected but is not currently turned on.
- **Flow not detected** means Shopify has not reported a workflow using this trigger yet.

Shopify may take a short time to report a workflow status change. The lifecycle timestamp shows when RevenueHunt last received an update from Shopify.

## Test the workflow

1. Complete the published quiz with an email address.
2. In Shopify Flow, open the workflow and review its recent runs.
3. Confirm that the expected conditions and actions completed successfully.

If no run appears, work through these in order:

1. Confirm the quiz contains an email question and that you filled it in when testing.
2. Confirm **Enable pushing quiz leads to Shopify Customers** is turned on and saved.
3. Confirm the workflow itself is turned on in Shopify Flow.
4. Complete the quiz again with an email address.

!!! note

    The **Quiz Completed** trigger is different from workflows that start with Shopify's **Customer created** trigger and filter by customer tags. Use **Quiz Completed** when you want the workflow to run directly from the Product Recommendation Quiz completion event.
