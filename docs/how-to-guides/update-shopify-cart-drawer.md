---
icon: material/cart-arrow-down
description: "Learn how to update your Shopify cart drawer when products are added via RevenueHunt quiz."
---

# How to Update Your Shopify Cart Drawer Products After the Quiz

The quiz adds the products to the cart, but your cart drawer stays closed or shows nothing. The cause is in how your Shopify theme handles cart updates, rather than in the quiz.

The app already fires Shopify's native cart events. Your theme has to listen for them, and no quiz-specific API is needed for that.

## How the quiz adds products to the cart

The app uses Shopify's official AJAX Cart API, the same endpoints most Shopify themes and apps use:

- `cart/add.js` adds products to the cart.
- `cart/change.js` changes product quantities.
- `cart/update.js` updates the cart with new contents.
- `cart.js` retrieves the current state of the cart.

Those calls tell Shopify that the cart changed. Updating what the customer sees, including opening or refreshing the drawer, is the theme's job.

## Why the drawer may not update

Most modern themes, Dawn among them, have a cart drawer or slide-out cart. When yours does not update after a quiz submission, one of these is usually true.

- The theme is not listening for the changes that AJAX cart actions trigger.
- The drawer script was extended without being set up to react to AJAX calls from outside the theme. This happens in Shopify's own themes too.

## What your developer needs to do

The app only triggers Shopify's standard cart actions, so the theme has to respond to them.

1. **Listen for those AJAX calls**, in the theme or in a small custom script.
2. **Trigger the drawer's open or refresh logic** when one of them fires.

This works across themes, and needs no change inside the app.

Share these with your developer or your Shopify Expert:

- [Shopify AJAX Cart API reference](https://shopify.dev/docs/api/ajax/reference/cart)
- [Listening to AJAX cart events in Shopify themes](https://www.perplexity.ai/search/how-to-get-shopify-theme-to-li-whWrlpOyT_6ygEG0ZRt68w#0)

!!! example "How one merchant fixed it"

    On the Megastore theme, products reached the cart after the quiz, but the drawer stayed closed and sometimes showed an "Empty Cart" message.

    Reading the theme code showed that it only opened the drawer for items added through the theme's own product forms:

    ```js
    onSubmitHandler(evt) {
      fetch('/cart/add.js', { /* ... */ })
        .then(response => response.json())
        .then(response => {
          this.cart.renderContents(response); // ← Opens the drawer
        });
    }
    ```

    An app calling the Cart API directly never reached that code.

    Their developer added a global Cart API interceptor that:

    - detects any `/cart/add.js` or `/cart/update.js` request,
    - fetches the updated cart contents,
    - opens or refreshes the drawer,
    - clears any leftover "empty cart" message.

    They also re-attached the overlay and close button handlers after updating the DOM, so the drawer kept working normally. With that script in place, the drawer updated correctly, and nothing changed on the app side.

## Test the setup

Once the theme listens for the AJAX cart actions:

1. **Take the quiz through to the results page and click `Add to Cart`.**
2. **Check that the products reach the cart.**
3. **Check that the drawer opens on its own, or that the cart shows the new products.**

!!! info "What the app does, and what it does not"

    The app triggers Shopify's native cart actions. It does not modify your cart drawer or your theme layout.

    The support team can confirm that the app is firing the right cart actions. See [How to Contact Customer Support](/how-to-guides/contact-customer-support/).

    Theme customization and third-party JavaScript are outside what support can debug. For those, ask your theme developer or a Shopify Expert.

---

This article explains how to update your Shopify cart drawer products after the quiz.
