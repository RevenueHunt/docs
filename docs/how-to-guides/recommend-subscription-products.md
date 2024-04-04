---
icon: material/calendar-sync
---

# How to Recommend Subscription Products

Recommending subscription products via the Shop Quiz can significantly enhance your e-commerce strategy by providing a steady revenue stream and fostering long-term customer relationships. With the integration of [ReCharge Subscriptions](https://apps.shopify.com/subscription-payments?surface_intra_position=1&surface_type=partners&surface_version=redesign) into your product recommendation strategy, you can create a seamless shopping experience for your customers. 

![how to recommend subscription products sample product](/images/how to recommend subscription products sample product.png)

This guide explains how to integrate and recommend subscription products with Shop Quiz.

## ReCharge Subscriptions

Here’s how to connect your ReCharge subscriptions to your Shop Quiz:

1. **Open the Shop Quiz App:** Start by accessing your account on the app.
   
2. **Navigate and Connect:** In your quiz dashboard, select the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) tab. Scroll down to the **ReCharge** section and click on the `connect` button.

3. **Sync the store**: Go to your dashboard > [success checklist](https://docs.revenuehunt.com/reference/dashboard/#success-checklist) and run a [catalog sync](https://docs.revenuehunt.com/how-to-guides/sync-catalog/). The sync can take up to 30 - 60 minutes.

4. **Link Products to Quiz Choices:** In the [Link Products](https://docs.revenuehunt.com/reference/quiz-builder/#link-products) tab, associate your ReCharge subscription products with the corresponding choices. 

5. **Publish Your Changes:** After linking the products, don’t forget to hit the `Publish` button to update the preview/live quiz.

Integrating ReCharge with Shopify enhances your ability to recommend subscription products, but there are limitations and best practices to consider:

- It is not possible to add all products to the cart with a single button; each subscription has to be chosen and added separately.
- The subscription duration can only be chosen on the results page. It is not possible to recommend a specific subscription duration.
- The customer needs to proceed to the cart first and cannot proceed to checkout directly with subscription products. You can change this in the [checkout settings](https://docs.revenuehunt.com/how-to-guides/change-checkout-settings/).
- We only integrate with the **new Shopify Checkout**; the old Recharge Checkout is not supported. For instructions on how to migrate from the old ReCharge Checkout to the new Shopify Checkout, check [this article](https://support.rechargepayments.com/hc/en-us/articles/4403505928599).

## Other Subscriptions

For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Shop Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

### Step 1: Link One-Time Payment Products to Quiz Choices
1. Identify your subscription products that you wish to promote through the quiz.
2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
3. **Link one-time payment products to chocies**: In the [Link Products](https://docs.revenuehunt.com/reference/quiz-builder/#link-products) section, link each of these one-time payment products to the relevant quiz choices. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

### Step 2: Adjust Checkout Settings
1. **Open Results Page settings**: Navigate to the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings) within your Shop Quiz Results Page.
2. **Change Checkout Settings**: Change the [Checkout Settings](https://docs.revenuehunt.com/how-to-guides/change-checkout-settings/) from “Add to cart” to “Link to product.” This adjustment ensures that instead of adding the product directly to their shopping cart, customers will be directed to the product page on your website.

As a result, the buyers will go directly to the product page and can subscribe there.

---

By following these steps and best practices, you can effectively integrate and recommend subscription products via Shop Quiz.
