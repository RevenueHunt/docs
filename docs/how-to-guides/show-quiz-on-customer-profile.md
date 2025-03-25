---
icon: material/account-file-text-outline
---

# How to Show Quiz on a Shopify Customer Profile

Integrating quiz results into a customer's profile on your Shopify store can personalize the shopping experience. 

This guide will walk you through the steps to show the quiz on a customer profile in Shopify.

!!! warning

    This guide is meant for developers and Shopify Partners. If you're not familiar with Shopify liquid, it is advised to ask for help from a professional to implement this. You can find/hire a developer [here](https://experts.shopify.com/).

!!! note

    This method works only for Shopify accounts using our [RevenueHunt](https://revenuehunt.com/product-recommendation-quiz-shopify/) app. Unfortunately, we don't have a solution yet on how to show the quiz on a customer profile in WooCommerce, Magento or BigCommerce.

## Step 1: Connect Your Quiz to Shopify's Customer List

To ensure quiz results are associated with the correct customer profile, the first step involves linking your quiz tool with [Shopify's Customer List](https://docs.revenuehunt.com/how-to-guides/send-leads-to-shopify-customers/). Follow the instructions in [this article](https://docs.revenuehunt.com/how-to-guides/send-leads-to-shopify-customers/) to check if the quiz was connected correctly.

## Step 2: Edit the customers/account.liquid File

When a respondent completes the quiz, we will send a `metafield` to their profile, which includes the `response/recommendations` they just got.

When you navigate to Your `Shopify Theme -> Actions -> Edit code`, you can find this metafield within the Templates liquid code of the customer profile:

```html
customer.metafields.prq.response_permalink
```

This is how it looks like within customer/account.liquid file in Shopify:

![how to show quiz on customer profile](/images/how_to_show_quiz_on_customer_profile.png)

## Step 3: Embed the Quiz Results

To render the whole results page within an iframe on a profile,  you will need to first embed our `embed.js` file (as you can see on line 67):

```html
<script src="https://admin.revenuehunt.com/embed.js" async></script>
```

Then, [generate an embed code](https://docs.revenuehunt.com/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) from the [Share](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the quiz and insert the quiz iframe code (as you can see on line 68):

```html
<iframe src="{{ customer.metafields.prq.response_permalink }}" style="width:100%; border: none; margin-bottom: 30px; position: absolute; left: 0;" />
```

Here’s how it can look on your customer’s profile:

![how to show quiz on customer profile rendered](/images/how_to_show_quiz_on_customer_profile_rendered.png)

---
This guide provides instructions for developers on showing the quiz on a customer profile in Shopify.


