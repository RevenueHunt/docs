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

To enable customer syncing:

1. In RevenueHunt, go to **App Settings**.
2. Open **Shopify Customers**.
3. Turn on **Enable pushing quiz leads to Shopify Customers**.
4. Save your changes.

For more information about customer syncing, see [How to Send Quiz Leads to Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/).

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

- **Active** means Shopify has reported that a workflow using the **Quiz Completed** trigger from Product Recommendation Quiz is turned on.
- **Inactive** means a workflow was detected but is not currently turned on.
- **Not detected** means Shopify has not reported a workflow using this trigger yet.

Shopify may take a short time to report a workflow status change. The lifecycle timestamp shows when RevenueHunt last received an update from Shopify.

## Test the workflow

1. Complete the published quiz with an email address.
2. In Shopify Flow, open the workflow and review its recent runs.
3. Confirm that the expected conditions and actions completed successfully.

If no run appears, confirm that customer syncing and the workflow are both enabled, then complete the quiz again with an email address.

!!! note

    The **Quiz Completed** trigger is different from workflows that start with Shopify's **Customer created** trigger and filter by customer tags. Use **Quiz Completed** when you want the workflow to run directly from the Product Recommendation Quiz completion event.
