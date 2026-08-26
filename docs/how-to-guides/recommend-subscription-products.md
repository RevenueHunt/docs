---
icon: material/calendar-sync
description: "Step-by-step guide to integrate and recommend subscription products with RevenueHunt app."
---

# How to Recommend Subscription Products

This article explains how to recommend subscription products, so a customer can subscribe straight from the results page.

On Shopify the app works with Shopify Subscriptions and [ReCharge Subscriptions](https://apps.shopify.com/subscription-payments?surface_intra_position=1&surface_type=partners&surface_version=redesign). On WooCommerce it works with [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/).

![A recommended subscription product on the results page](/images/how_to_recommend_subscription_products_sample_product.png)

!!! note "Platform Availability"

    BigCommerce and Magento cannot show subscription products on the results page. The same applies to any Shopify or WooCommerce subscription app that is not on the list above. See [Other subscriptions](#other-subscriptions) for a workaround.

## Shopify and Recharge subscriptions

=== "Shopify"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/X_beZcbcwG4?si=CSBT9I08vEh0Cs4U" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Before you start"

        - Ensure you are using the [Recharge Plus version](https://getrecharge.com/pricing/) to access the Storefront API. On any other plan, contact [Recharge support](https://support.getrecharge.com/hc/en-us#).
        - Confirm that Recharge is configured on your Shopify website according to the [Recharge documentation](https://storefront.rechargepayments.com/client/docs/getting_started/script_setup/).


    1. **Add the Recharge Storefront SDK to your Shopify theme**:

        - Navigate to your online store themes and select `Edit Code`.
        - Open the `layout/theme.liquid` file.
        - Add this script in the `<head>` section, before the RevenueHunt quiz renderer script:

            ```html
            <script src="https://static.rechargecdn.com/assets/storefront/recharge-client-2.0.0.min.js"></script>
            ```

        - Save the changes.

        !!! warning "Legacy Recharge script"

            `https://static.rechargecdn.com/static/js/recharge.js` is not the Storefront SDK required by the quiz. If your theme loads that legacy script, replace it with the `recharge-client-2.0.0.min.js` script above.

    1. To add subscription to your recommended products go to the [Results page](/reference/quiz-builder/results-page/).
    2. Find the [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) and open its settings.
    3. Under `Product components layout`, find the `Subscription` option and add it to the layout.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2.png)

    4. Under `Subscription`, select the subscription app you want to use.


        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_subscription](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_subscription.png)


        !!! info "Supported subscription apps"

            The `Subscription` component supports these apps on Shopify:

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_subscription_apps](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_subscription_apps.png)

            - Shopify Subscriptions,
            - Recharge Subscriptions (Plus plan only).

            To ask about a subscription app that is not on the list, [contact support](/how-to-guides/contact-customer-support/).
    4. Save the changes with the top-right `Save` button.
    5. To test the integration, [publish](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) the quiz on a new page and take it through to the results page. The subscription options appear there. You can add the subscription product to the cart, or go to the cart page.
    6. Verify that the subscription item is added correctly to the cart.

    !!! warning "Quiz Preview"

        The subscription options will not be available in the quiz preview. To test the integration, you need to [publish](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page)  the quiz on a new page in your website.


=== "Shopify (Legacy)"

    !!! warning "Before you start"

        - Ensure you are using the [Recharge Plus version](https://getrecharge.com/pricing/) to access the Storefront API. On any other plan, contact [Recharge support](https://support.getrecharge.com/hc/en-us#).
        - Confirm that Recharge is configured on your Shopify website according to the [Recharge documentation](https://storefront.rechargepayments.com/client/docs/getting_started/script_setup/).


    To connect your ReCharge subscriptions to the RevenueHunt app:

    1. **Open the RevenueHunt App:** Start by accessing your account on the app.

    2. **Navigate and Connect:** In your quiz dashboard, select the [Connect](/reference/quiz-builder/connect-integrations/) tab. Scroll down to the **ReCharge** section and click on the `connect` button.

    3. **Sync the store**: Go to your dashboard > [success checklist](/reference/dashboard/#success-checklist) and run a [catalog sync](/how-to-guides/sync-catalog/). The sync can take 30 to 60 minutes.

    4. **Link Products to Quiz Choices:** In the [Link Products](/reference/quiz-builder/link-products/) tab, associate your ReCharge subscription products with the corresponding choices.

    5. **Publish Your Changes:** Click `Publish` to update the preview and the live quiz.

    Integrating ReCharge with Shopify enhances your ability to recommend subscription products, but there are limitations and best practices to consider:

    - You cannot add all products to the cart with one button. Each subscription has to be chosen and added separately.
    - The subscription duration is chosen on the results page. You cannot recommend a specific duration.
    - The customer needs to proceed to the cart first and cannot proceed to checkout directly with subscription products. You can change this in the [checkout settings](/how-to-guides/change-checkout-settings/).
    - The app works with the **new Shopify Checkout** only. The old Recharge Checkout is not supported. For instructions on how to migrate from the old ReCharge Checkout to the new Shopify Checkout, check [ReCharge migration guide](https://support.rechargepayments.com/hc/en-us/articles/4403505928599).

=== "WooCommerce"

    Not applicable.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

## WooCommerce subscriptions

=== "Shopify"

    Not applicable.



=== "Shopify (Legacy)"

    Not applicable.

=== "WooCommerce"

    Products created with [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) are automatically synced with the app when you install it. You can find them under [Link Products](/reference/quiz-builder/link-products/) tab in the [Quiz Builder](/reference/quiz-builder/).

    !!! tip

        If your WooCommerce subscription products are not on the list, run a [catalog sync](/how-to-guides/sync-catalog/) of the app.

=== "Magento"

    Not applicable.

=== "BigCommerce"

    Not applicable.

=== "Standalone"

    Not applicable.

## Other subscriptions

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/AWrsUZ-u2nk?si=INZh4rcHzVQ4268P" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    For other subscription apps, a workaround still guides your customers towards subscription options. To set up the workaround:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to choices**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each one-time payment product to the relevant quiz choices. You can also set up [Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations) on your Results page. A choice that used to lead to a subscription product then matches its one-time equivalent.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results page settings**: Navigate to the [Results page](/reference/quiz-builder/results-page/) and add or select a [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections)
    2. **Change Product Components Layout**: In [Product block settings](/reference/quiz-builder/results-page/#product-product-variants-collections), find the [`Product Components Layout`](/reference/quiz-builder/results-page/#slot-item-composition) section and remove the `Add to cart button option. Once removed, insert a `Link to Product` component instead.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_linktoproduct](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_linktoproduct.png)


    As a result, the buyers will not be able to add the product to the cart directly from the quiz results page. Instead, they will be redirected to the product page where they can subscribe.


=== "Shopify (Legacy)"

    For other subscription apps, a workaround still guides your customers towards subscription options. To set up the workaround:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to choices**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each one-time payment product to the relevant quiz choices. A choice that used to lead to a subscription product then matches its one-time equivalent.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: In [Checkout Settings](/how-to-guides/change-checkout-settings/), change “Add to cart” to “Link to product”. The customer is then sent to the product page rather than to the cart.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "WooCommerce"

    For other subscription apps, a workaround still guides your customers towards subscription options. To set up the workaround:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to choices**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each one-time payment product to the relevant quiz choices. A choice that used to lead to a subscription product then matches its one-time equivalent.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: In [Checkout Settings](/how-to-guides/change-checkout-settings/), change “Add to cart” to “Link to product”. The customer is then sent to the product page rather than to the cart.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "Magento"

    For other subscription apps, a workaround still guides your customers towards subscription options. To set up the workaround:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to choices**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each one-time payment product to the relevant quiz choices. A choice that used to lead to a subscription product then matches its one-time equivalent.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: In [Checkout Settings](/how-to-guides/change-checkout-settings/), change “Add to cart” to “Link to product”. The customer is then sent to the product page rather than to the cart.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "BigCommerce"

    For other subscription apps, a workaround still guides your customers towards subscription options. To set up the workaround:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to choices**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each one-time payment product to the relevant quiz choices. A choice that used to lead to a subscription product then matches its one-time equivalent.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: In [Checkout Settings](/how-to-guides/change-checkout-settings/), change “Add to cart” to “Link to product”. The customer is then sent to the product page rather than to the cart.

    As a result, the buyers will go directly to the product page and can subscribe there.

=== "Standalone"

    For other subscription apps, a workaround still guides your customers towards subscription options. To set up the workaround:

    **Step 1: Link One-Time Payment Products to Quiz Choices**

    1. Identify your subscription products that you wish to promote through the quiz.
    2. **Create one-time payment options**: Create equivalent one-time payment products for each of your subscription items. These will serve as placeholders in the quiz.
    3. **Link one-time payment products to choices**: In the [Link Products](/reference/quiz-builder/link-products/) section, link each one-time payment product to the relevant quiz choices. A choice that used to lead to a subscription product then matches its one-time equivalent.

    **Step 2: Adjust Checkout Settings**

    1. **Open Results Page settings**: Navigate to the [Results Page settings](/reference/quiz-builder/results-page/) within your Product Recommendation Quiz Results Page.
    2. **Change Checkout Settings**: In [Checkout Settings](/how-to-guides/change-checkout-settings/), change “Add to cart” to “Link to product”. The customer is then sent to the product page rather than to the cart.

    As a result, the buyers will go directly to the product page and can subscribe there.



---

By following these steps and best practices, you can recommend subscription products with the RevenueHunt app.
