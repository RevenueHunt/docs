---
description: "Troubleshooting guide to diagnose and fix common issues preventing products from being added to cart in your RevenueHunt quiz."
icon: material/cart-off
---

# Why Products Are Not Added to the Cart

If the quiz does not put a product in the cart, one of these three causes is usually behind it.

## Your quiz is not published on a live website

=== "Shopify"

    The quiz has to run on a published theme on your live store. A password page, a store still in trial, or a theme you are only previewing all block the cart.

    !!! tip "Publishing the quiz"

        See [how to publish a quiz on your website](/how-to-guides/publish-quiz/).

=== "Shopify (Legacy)"

    The quiz has to run on a published theme on your live store. A password page, a store still in trial, or a theme you are only previewing all block the cart.

    !!! tip "Publishing the quiz"

        See [how to publish a quiz on your website](/how-to-guides/publish-quiz/).

=== "WooCommerce"

    The quiz has to run on a live site. A coming-soon or maintenance-mode plugin, a password-protected page, or a staging site all block the cart.

    !!! tip "Publishing the quiz"

        See [how to publish a quiz on your website](/how-to-guides/publish-quiz/).

=== "Magento"

    The quiz has to run on a live storefront. Maintenance mode and a developer-only environment both block the cart.

    !!! tip "Publishing the quiz"

        See [how to publish a quiz on your website](/how-to-guides/publish-quiz/).

=== "BigCommerce"

    The quiz has to run on a live storefront. A store still in prelaunch, or a storefront behind a password, blocks the cart.

    !!! tip "Publishing the quiz"

        See [how to publish a quiz on your website](/how-to-guides/publish-quiz/).

=== "Standalone"

    !!! note "This version has no cart"

        The results page sends the customer to the product page instead, so nothing is ever added to a cart.

        See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/) for what the buttons can do here.

## Your store has a cart drawer or mini cart

=== "Shopify"

    On most themes the quiz updates the drawer cart itself. It adds the product, refreshes the drawer, and opens it, with no setup on your side.

    This works on Dawn and the themes built on it, and on Horizon and the themes released with it. Together they cover the most used themes on Shopify.

    A drawer cart belongs to the theme rather than to Shopify, so a few themes still do not update.

    That happens when the theme offers neither cart sections nor standard cart events, the two contracts the app can use. It also happens when a cart app has replaced the theme drawer and renders its own.

    There are two ways around that.

    **Option 1: have your developer listen for the standard cart event**

    The app announces every cart change as `shopify:cart:lines-update` on `document`. A developer can listen for it, request the current cart, and re-render the drawer.

    !!! info "What your theme editor or developer needs to know"

        [How to update your Shopify cart drawer products after the quiz](/how-to-guides/update-shopify-cart-drawer/) names the themes that need no setup. It also covers how the app adds products to the cart, and what to change in a theme that still does not update.

    **Option 2: send the customer to the product page**

    Change the checkout settings so the results page links to the product instead of adding it to the cart. The customer then adds it to the drawer cart themselves.

    !!! tip "Changing what the button does"

        See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

    !!! tip "Report your theme"

        If the drawer cart does not update on your theme, contact support with your theme name and version. See [how to contact customer support](/how-to-guides/contact-customer-support/).

=== "Shopify (Legacy)"

    The app adds products to the regular Shopify cart, not to the drawer cart your theme draws over it. The product is in the cart, but the drawer can keep showing what it held before.

    A drawer cart belongs to the theme rather than to Shopify, and the app cannot integrate with every theme that has one. There are two ways around it.

    **Option 1: have your theme handle the cart update**

    The app calls the Shopify AJAX Cart API, the same endpoints most themes use. A theme that listens for those calls can refresh its drawer from the quiz.

    !!! info "What your theme editor or developer needs to know"

        [How to update your Shopify cart drawer products after the quiz](/how-to-guides/update-shopify-cart-drawer/) covers how the app adds products to the Shopify cart, why the drawer may not update, and what to change in the theme.

    **Option 2: send the customer to the product page**

    Change the checkout settings so the results page links to the product instead of adding it to the cart. The customer then adds it to the drawer cart themselves.

    !!! tip "Changing what the button does"

        See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

=== "WooCommerce"

    Many WooCommerce themes and plugins add a side cart or mini cart. The product does reach the cart, but that panel keeps showing the old contents until the page reloads.

    A mini cart refreshes through WooCommerce cart fragments. A theme or plugin that overrides the `add_to_cart_fragments` hook, or a cache that serves a stale fragment response, stops it updating.

    !!! warning "Check your cache first"

        Page and CDN caches are the most common cause. Clear the cache in your caching plugin, at your host, and at your CDN, then take the quiz again.

    **Option 1: have the fragments refreshed**

    The panel has to request the cart fragments again after the quiz adds a product. Your developer can also test with a default theme such as Storefront, to find which plugin or theme holds the old state.

    **Option 2: send the customer to the product page**

    Change the checkout settings so the results page links to the product instead of adding it to the cart. The customer then adds it to the side cart themselves.

    !!! tip "Changing what the button does"

        See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

=== "Magento"

    The Magento minicart keeps its own copy of the cart in customer data sections. The product does reach the cart, but the minicart keeps showing the old contents until that section reloads.

    !!! warning "Check your cache first"

        Full page cache and Varnish are a common cause. Flush the Magento cache, then take the quiz again.

    **Option 1: have the cart section invalidated**

    The minicart refreshes when the `cart` customer data section is invalidated and reloaded. A theme or extension that changes the minicart can stop that happening.

    **Option 2: send the customer to the product page**

    Change the checkout settings so the results page links to the product instead of adding it to the cart. The customer then adds it to the minicart themselves.

    !!! tip "Changing what the button does"

        See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

=== "BigCommerce"

    Many Stencil themes show a cart preview, a flyout panel that opens from the cart icon. The product does reach the cart, but that panel keeps showing the old contents until the page reloads.

    The cart preview belongs to the theme rather than to BigCommerce, so the app cannot refresh it directly.

    **Option 1: have the cart preview refreshed**

    The theme has to request the cart preview again after the quiz adds a product. Your developer can look in the theme JavaScript for the event it already uses.

    **Option 2: send the customer to the product page**

    Change the checkout settings so the results page links to the product instead of adding it to the cart. The customer then adds it to the cart themselves.

    !!! tip "Changing what the button does"

        See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

=== "Standalone"

    !!! note "This version has no cart"

        Nothing is added to a cart here, so a cart drawer never comes into it. The results page sends the customer to the product page instead.

    To build cart behavior of your own, send the quiz data to your own results page with a [callback function](/how-to-guides/use-callback-function/).

## Your product is a subscription product

=== "Shopify"

    The app syncs and recommends subscription products from Shopify Subscriptions and from Recharge Subscriptions. See [how to recommend subscription products](/how-to-guides/recommend-subscription-products/) for the setup.

    For any other subscription app, a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "Shopify (Legacy)"

    The app syncs and recommends subscription products from Recharge Subscriptions. See [how to recommend subscription products](/how-to-guides/recommend-subscription-products/) for the setup.

    For any other subscription app, a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "WooCommerce"

    Products created with [WooCommerce Subscriptions](https://woocommerce.com/products/woocommerce-subscriptions/) sync with the app once the plugin is installed. If one is missing, run a [catalog sync](/how-to-guides/sync-catalog/).

    For any other subscription plugin, a [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "Magento"

    !!! note "Subscription products do not sync here"

        The app does not read subscription products in Magento.

    A [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "BigCommerce"

    !!! note "Subscription products do not sync here"

        The app does not read subscription products in BigCommerce.

    A [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

=== "Standalone"

    !!! note "Subscription products do not sync here"

        The app does not read subscription products in this version.

    A [workaround](/how-to-guides/recommend-subscription-products/#other-subscriptions) still points the customer at your subscription options.

---

This article covers three reasons a quiz does not add a product to the cart. They are an unpublished quiz, a cart drawer that does not refresh, and subscription products.