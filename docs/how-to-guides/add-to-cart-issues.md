---
description: "Troubleshooting guide to diagnose and fix common issues preventing products from being added to cart in your RevenueHunt quiz."
icon: material/cart-off
---


# Why Products Are Not Added to the Cart

If your products are not added to the cart, here are the most probable causes.

## Your quiz is not published on a live website

=== "Shopify"

    The quiz has to run on a published theme on your live store. A password page, a store still in trial, or a theme you are only previewing all block the cart.

    !!! tip

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) to learn how to publish your quiz.

=== "Shopify (Legacy)"

    The quiz has to run on a published theme on your live store. A password page, a store still in trial, or a theme you are only previewing all block the cart.

    !!! tip

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) to learn how to publish your quiz.

=== "WooCommerce"

    The quiz has to run on a live site. A “coming soon” or maintenance mode plugin, a password-protected page, or a staging site all block the cart.

    !!! tip

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) to learn how to publish your quiz.

=== "Magento"

    The quiz has to run on a live storefront. Maintenance mode and a developer-only environment both block the cart.

    !!! tip

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) to learn how to publish your quiz.

=== "BigCommerce"

    The quiz has to run on a live storefront. A store still in prelaunch, or a storefront behind a password, blocks the cart.

    !!! tip

        See [How to Publish a Quiz on Your Website](/how-to-guides/publish-quiz/) to learn how to publish your quiz.

=== "Standalone"

    The Standalone version has no cart of its own. It sends the customer to the product page instead, so there is nothing to add to a cart.

    !!! note "Platform Availability"

        Add to cart is not available in the Standalone version. See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/).

## Your store uses a cart drawer

=== "Shopify"

    The RevenueHunt app does not integrate with drawer carts. After the quiz, it adds products to the “regular” cart rather than the drawer cart in your theme.

    A drawer cart comes from a store theme, not from Shopify itself. The app cannot integrate with every theme that has one. There are two ways around it.

    !!! warning "Cart Drawer"

        [How to Update Your Shopify Cart Drawer Products After the Quiz](/how-to-guides/update-shopify-cart-drawer/) explains:

        - How the RevenueHunt app adds products to the Shopify cart

        - Why the cart drawer may not update

        - What your theme editor or developer can do to fix it

    **Option 1: Configure your Shopify theme to handle cart updates**

    The app calls the Shopify AJAX Cart API, the same endpoints most themes use. A theme that listens for those calls can refresh its drawer from the quiz.

    **Option 2: Send the customer to the product page**

    Change the checkout settings to send the customer to the product page rather than add the product to the cart. They can then add it to the drawer cart themselves.

    !!! tip

        See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/) to learn how to change your checkout settings.

=== "Shopify (Legacy)"

    The RevenueHunt app does not integrate with drawer carts. After the quiz, it adds products to the “regular” cart rather than the drawer cart in your theme.

    A drawer cart comes from a store theme, not from Shopify itself. The app cannot integrate with every theme that has one. There are two ways around it.

    !!! warning "Cart Drawer"

        [How to Update Your Shopify Cart Drawer Products After the Quiz](/how-to-guides/update-shopify-cart-drawer/) explains:

        - How the RevenueHunt app adds products to the Shopify cart

        - Why the cart drawer may not update

        - What your theme editor or developer can do to fix it

    **Option 1: Configure your Shopify theme to handle cart updates**

    The app calls the Shopify AJAX Cart API, the same endpoints most themes use. A theme that listens for those calls can refresh its drawer from the quiz.

    **Option 2: Send the customer to the product page**

    Change the checkout settings to send the customer to the product page rather than add the product to the cart. They can then add it to the drawer cart themselves.

    !!! tip

        See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/) to learn how to change your checkout settings.

=== "WooCommerce"

    Many WooCommerce themes and plugins add a side cart or mini cart. The product does reach the cart, but that panel keeps showing the old contents until the page reloads.

    A mini cart refreshes through WooCommerce cart fragments. A theme or plugin that overrides the `add_to_cart_fragments` hook, or a cache that serves a stale fragment response, stops it from updating.

    **Option 1: Ask your theme or plugin developer to refresh the fragments**

    The panel has to request the cart fragments again after the quiz adds a product. Your developer can also test with a default theme such as Storefront to confirm which plugin or theme is holding the old state.

    **Option 2: Send the customer to the product page**

    Change the checkout settings to send the customer to the product page rather than add the product to the cart. They can then add it to the side cart themselves.

    !!! tip

        See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/) to learn how to change your checkout settings.

    !!! warning "Check your cache first"

        Page and CDN caches are the most common cause. Clear the cache in your caching plugin, at your host, and at your CDN, then take the quiz again.

=== "Magento"

    The Magento minicart keeps its own copy of the cart in customer data sections. The product does reach the cart, but the minicart keeps showing the old contents until that section is reloaded.

    **Option 1: Ask your developer to invalidate the cart section**

    The minicart refreshes when the `cart` customer data section is invalidated and reloaded. A theme or extension that changes the minicart can stop that happening.

    **Option 2: Send the customer to the product page**

    Change the checkout settings to send the customer to the product page rather than add the product to the cart. They can then add it to the minicart themselves.

    !!! tip

        See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/) to learn how to change your checkout settings.

    !!! warning "Check your cache first"

        Full page cache and Varnish are a common cause. Flush the Magento cache, then take the quiz again.

=== "BigCommerce"

    Many Stencil themes show a cart preview, a flyout panel that opens from the cart icon. The product does reach the cart, but that panel keeps showing the old contents until the page reloads.

    The cart preview is part of the theme, not of BigCommerce itself, so the app cannot refresh it directly.

    **Option 1: Ask your theme developer to refresh the cart preview**

    The theme has to re-request the cart preview after the quiz adds a product. Your developer can check the cart handling in the theme JavaScript for the event it already uses.

    **Option 2: Send the customer to the product page**

    Change the checkout settings to send the customer to the product page rather than add the product to the cart. They can then add it to the cart themselves.

    !!! tip

        See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/) to learn how to change your checkout settings.

=== "Standalone"

    !!! note "Platform Availability"

        The Standalone version cannot add products to a cart, so a cart drawer never applies. The results page sends the customer to the product page instead.

    To build your own cart behavior, send the quiz data to your own results page with the [Callback function](/how-to-guides/use-callback-function/).

## Your product is a subscription product

=== "Shopify"

    The RevenueHunt app can sync and recommend subscription products created with Recharge Subscriptions for Shopify. See [How to Recommend Subscription Products](/how-to-guides/recommend-subscription-products/) for how to enable it.

    For other subscription apps, a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "Shopify (Legacy)"

    The RevenueHunt app can sync and recommend subscription products created with Recharge Subscriptions for Shopify. See [How to Recommend Subscription Products](/how-to-guides/recommend-subscription-products/) for how to enable it.

    For other subscription apps, a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "WooCommerce"

    Products created with [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) sync with the app on install. If one is missing, run a [catalog sync](/how-to-guides/sync-catalog/).

    For other subscription plugins, a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "Magento"

    !!! note "Platform Availability"

        The app does not sync subscription products in Magento.

    A [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "BigCommerce"

    !!! note "Platform Availability"

        The app does not sync subscription products in BigCommerce.

    A [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "Standalone"

    !!! note "Platform Availability"

        The app does not sync subscription products in the Standalone version.

    A [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.


---
This article covers the common reasons a quiz does not add a product to the cart: an unpublished quiz, a cart drawer, and subscription products.
