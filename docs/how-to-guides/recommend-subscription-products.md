---
icon: material/calendar-sync
---

# How to Recommend Subscription Products

This guide explains how to integrate and recommend subscription products with RevenueHunt app.

Recommending subscription products via the RevenueHunt Product Recommendation Quiz can simplify your e-commerce strategy by providing a steady revenue stream and fostering long-term customer relationships. 

However, not all subscription apps are supported yet with the RevenueHunt app. Currently, we support [ReCharge Subscriptions](https://apps.shopify.com/subscription-payments?surface_intra_position=1&surface_type=partners&surface_version=redesign) for Shopify V1 (legacy version) and [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) for WooCommerce.

If you're using a subscription app that is not supported, you can still recommend subscription products to your users by sending them to a single-time payment product page from the quiz results using [this workaround](#other-subscriptions). This will allow your users to subscribe to the product from the product page.

![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png)


!!! warning

    RevenueHunt app currently only integrates with [ReCharge Subscriptions](https://apps.shopify.com/subscription-payments?surface_intra_position=1&surface_type=partners&surface_version=redesign) for Shopify V1 (legacy version) and [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) for WooCommerce. Subscription products are not yet supported in the Product Recommendation Quiz for Shopify (new version),BigCommerce or Magento. They will not show up on the Results page. However, there’s a workaround explained in the [Other subscriptions](#other-subscriptions) section of the article.

## ReCharge Subscriptions

=== "Shopify"

    Here’s how to connect your ReCharge subscriptions to your RevenueHunt app:

    1. **Open the RevenueHunt App:** Start by accessing your account on the app.
    
    2. **Navigate and Connect:** In your quiz dashboard, select the [Connect](/reference/quiz-builder/connect-integrations/) tab. Scroll down to the **ReCharge** section and click on the `connect` button.

    3. **Sync the store**: Go to your dashboard > [success checklist](/reference/dashboard/#success-checklist) and run a [catalog sync](/how-to-guides/sync-catalog/). The sync can take up to 30 - 60 minutes.

    4. **Link Products to Quiz Choices:** In the [Link Products](/reference/quiz-builder/link-products/) tab, associate your ReCharge subscription products with the corresponding choices. 

    5. **Publish Your Changes:** After linking the products, don’t forget to hit the `Publish` button to update the preview/live quiz.

    Integrating ReCharge with Shopify enhances your ability to recommend subscription products, but there are limitations and best practices to consider:

    - It is not possible to add all products to the cart with a single button; each subscription has to be chosen and added separately.
    - The subscription duration can only be chosen on the results page. It is not possible to recommend a specific subscription duration.
    - The customer needs to proceed to the cart first and cannot proceed to checkout directly with subscription products. You can change this in the [checkout settings](/how-to-guides/change-checkout-settings/).
    - We only integrate with the **new Shopify Checkout**; the old Recharge Checkout is not supported. For instructions on how to migrate from the old ReCharge Checkout to the new Shopify Checkout, check [this article](https://support.rechargepayments.com/hc/en-us/articles/4403505928599).

=== "Shopify V2"

    Not supported yet.

=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

## WooCommerce Subscriptions

=== "Shopify"

    Not applicable.

=== "Shopify V2"

    Not applicable.


=== "WooCommerce"

    Products created with [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) are automatically synced with the app when you install it. You can find them under [Link Products](/reference/quiz-builder/link-products/) tab in the [Quiz Builder](/reference/quiz-builder/).

    !!! tip

        If you don’t see your WooCommerce subscription products on the list, try to launch a [catalog sync](/how-to-guides/sync-catalog/) of the app.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

## Other Subscriptions

=== "Shopify"

    For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Product Reocommendation Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to chocies**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each of these one-time payment products to the relevant quiz choices. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: Change the [Checkout Settings](/how-to-guides/change-checkout-settings/) from “Add to cart” to “Link to product.” This adjustment ensures that instead of adding the product directly to their shopping cart, customers will be directed to the product page on your website.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/d5f15461e3014d2fa8ad33637410d4ba?sid=ed6fdfff-9d0e-439b-aa83-a61708b36a44" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Product Reocommendation Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to chocies**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each of these one-time payment products to the relevant quiz choices or set up [Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations) on your Results Page. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page](/reference/quiz-builder/results-page/) and add or select a [Product Block](/reference/quiz-builder/results-page/#products-products-variants-collections)
    2. **Change Product Components Layout**: In [Product Block settings](/reference/quiz-builder/results-page/#products-products-variants-collections), find the [`Product Components Layout`](/reference/quiz-builder/results-page/#product-components-layout) section and remove the `Add to cart button option. Once removed, insert a `Link to Product` component instead.

        ![how_to_shopifyV2_recommend_subscriptions_workaround](/images/how_to_shopifyV2_recommend_subscriptions_workaround.png)

    As a result, the buyers will not be able to add the product to the cart directly from the quiz results page. Instead, they will be redirected to the product page where they can subscribe.

=== "WooCommerce"

    For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Product Reocommendation Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to chocies**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each of these one-time payment products to the relevant quiz choices. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: Change the [Checkout Settings](/how-to-guides/change-checkout-settings/) from “Add to cart” to “Link to product.” This adjustment ensures that instead of adding the product directly to their shopping cart, customers will be directed to the product page on your website.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "Magento"

    For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Product Reocommendation Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to chocies**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each of these one-time payment products to the relevant quiz choices. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: Change the [Checkout Settings](/how-to-guides/change-checkout-settings/) from “Add to cart” to “Link to product.” This adjustment ensures that instead of adding the product directly to their shopping cart, customers will be directed to the product page on your website.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "BigCommerce"

    For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Product Reocommendation Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to chocies**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each of these one-time payment products to the relevant quiz choices. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: Change the [Checkout Settings](/how-to-guides/change-checkout-settings/) from “Add to cart” to “Link to product.” This adjustment ensures that instead of adding the product directly to their shopping cart, customers will be directed to the product page on your website.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "Standalone"

    For other subscription apps, there's a workaround that allows you to still guide your customers towards subscription options via the Product Reocommendation Quiz. Here's a step-by-step guide on how to implement this workaround effectively:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to chocies**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each of these one-time payment products to the relevant quiz choices. This ensures that when a customer selects an option that would traditionally lead to a subscription product, they are instead matched with the corresponding one-time payment product.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: Change the [Checkout Settings](/how-to-guides/change-checkout-settings/) from “Add to cart” to “Link to product.” This adjustment ensures that instead of adding the product directly to their shopping cart, customers will be directed to the product page on your website.

    As a result, the buyers will go directly to the product page and can subscribe there.



---

By following these steps and best practices, you canintegrate and recommend subscription products via RevenueHunt Product Recommendation Quiz.
