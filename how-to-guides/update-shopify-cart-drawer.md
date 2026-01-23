---
icon: material/cart-arrow-down
---


# How to Update Your Shopify Cart Drawer Products After the Quiz

If your quiz is adding products to the cart but your cart drawer isn’t updating or opening automatically, the issue is likely with how your Shopify theme handles cart updates — not with the quiz itself.

!!! warning "Cart Drawer Update"

    You don’t need a dedicated Quiz JS API to update your cart drawer. The RevenueHunt app already triggers Shopify’s native cart events (like `cart/add.js`, `cart/update.js`, and `cart/change.js`) whenever a shopper adds or updates products through the quiz.

    You can listen to these events in your theme or custom script to detect when items are added to the cart and then trigger your cart drawer update logic. This approach works across themes and doesn’t require any changes in the app itself.

This guide explains:

- How RevenueHunt quiz app adds products to the Shopify cart

- Why the cart drawer may not update

- What your theme editor or developer can do to fix it

## Step 1: Understand How Quiz Adds Products to the Cart

Our app uses Shopify’s official AJAX Cart API to add products. These are the same endpoints used by most Shopify themes and apps.

We use:

- `cart/add.js` – adds products to the cart

- `cart/change.js` – changes product quantities

- `cart/update.js` – updates the cart with new contents

- `cart.js` – retrieves the latest state of the cart

These actions notify Shopify that the cart has changed. It’s then up to the theme to update the UI, such as opening or refreshing the cart drawer.

## Step 2: Confirm If Your Theme Supports Cart Drawer Updates

Most modern themes (like Dawn) include a cart drawer or slide-out cart. However, if your cart drawer does not update after a quiz submission:

- Your theme is likely not listening for changes triggered by AJAX cart actions.

- This can happen even in Shopify’s default themes if the cart drawer script wasn’t customized / extended properly or if the cart drawer script isn’t configured to react to external AJAX calls.

## Step 3: Talk to Your Theme Developer

Since our app only triggers Shopify’s standard cart actions, you’ll need to make sure your theme is set up to respond to those actions.

You don’t need a custom Quiz API or event hook to make this work.
The app already triggers Shopify’s native cart events (`cart/add.js`, `cart/update.js`, and `cart/change.js`) whenever shoppers add or update products through the quiz.

To make your cart drawer respond automatically:

- Simply listen for these AJAX calls in your theme or a small custom script.

- When detected, trigger your cart drawer’s “open” or “refresh” logic.

This lightweight approach works across all themes and doesn’t require any modifications to the RevenueHunt app itself.

Share the following resources with your developer or Shopify Expert:

- Shopify AJAX Cart Documentation: [https://shopify.dev/docs/api/ajax/reference/cart](https://shopify.dev/docs/api/ajax/reference/cart)

- Helpful guide on listening to AJAX cart events in Shopify themes: [https://www.perplexity.ai/search/how-to-get-shopify-theme-to-li-whWrlpOyT_6ygEG0ZRt68w#0](https://www.perplexity.ai/search/how-to-get-shopify-theme-to-li-whWrlpOyT_6ygEG0ZRt68w#0)


!!! example "Example from a Merchant"

    A Shopify merchant using the Megastore theme noticed that products were correctly added to the cart after the quiz, but the drawer remained closed and sometimes showed an “Empty Cart” message.

    After reviewing the theme code, they found that it only opened the cart drawer when items were added via the theme’s own product forms:

    ```js
            onSubmitHandler(evt) {
        fetch('/cart/add.js', { /* ... */ })
            .then(response => response.json())
            .then(response => {
            this.cart.renderContents(response); // ← Opens the drawer
            });
        }

    ```

    When external apps (like the quiz) used the Cart API directly, this path was never triggered.

    Solution implemented:

    Their developer added a global Cart API interceptor that:

    - Detects any `/cart/add.js` or `/cart/update.js` requests,
    - Fetches the updated cart contents,
    - Automatically opens or refreshes the drawer,
    - Removes residual "empty cart" messages.

    They also re-attached the overlay and close button handlers after updating the DOM so the drawer worked normally.

    Once this script was added, the cart drawer updated perfectly — without any app-side changes.

## Step 4: Test Your Setup

Once your theme is updated to listen to the AJAX cart actions, test the following:

1. Complete your quiz and click “Add to Cart”.

2. Confirm that:

    - Products are added successfully.

    - The cart drawer opens automatically, or

    - The cart UI updates with the new products.


!!! info "Note"

    The RevenueHunt app already triggers Shopify’s native cart actions.  

    We do **not** modify your cart drawer or theme layout.

    We **cannot** support theme customization or debug third-party JavaScript.

    We’re happy to confirm that our app is triggering the correct cart actions — [just let us know](https://docs.revenuehunt.com/how-to-guides/contact-customer-support/).

    For theme modifications, please consult your theme developer or Shopify Expert.


---

This article explains how to update your Shopify cart drawer products after the quiz.









