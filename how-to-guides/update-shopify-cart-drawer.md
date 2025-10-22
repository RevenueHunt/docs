---
icon: material/cart-arrow-down
---


# How to Update Your Shopify Cart Drawer Products After the Quiz

If your quiz is adding products to the cart but your cart drawer isn’t updating or opening automatically, the issue is likely with how your Shopify theme handles cart updates — not with the quiz itself.

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

- This can happen even in Shopify’s default themes if the cart drawer script wasn’t customized or extended properly.

## Step 3: Talk to Your Theme Developer

Since our app only triggers Shopify’s standard cart actions, you’ll need to make sure your theme is set up to respond to those actions.

Share the following resources with your developer or Shopify Expert:

- Shopify AJAX Cart Documentation: [https://shopify.dev/docs/api/ajax/reference/cart](https://shopify.dev/docs/api/ajax/reference/cart)

- Helpful guide on listening to AJAX cart events in Shopify themes: [https://www.perplexity.ai/search/how-to-get-shopify-theme-to-li-whWrlpOyT_6ygEG0ZRt68w#0](https://www.perplexity.ai/search/how-to-get-shopify-theme-to-li-whWrlpOyT_6ygEG0ZRt68w#0)


## Step 4: Test Your Setup

Once your theme is updated to listen to the AJAX cart actions, test the following:

1. Complete your quiz and click “Add to Cart”.

2. Confirm that:

    - Products are added successfully.

    - The cart drawer opens automatically, or

    - The cart UI updates with the new products.


!!! info "Note"

    We do **not** modify your cart drawer or theme layout.

    We **cannot** support theme customization or debug third-party JavaScript.

    We’re happy to confirm that our app is triggering the correct cart actions — [just let us know](https://docs.revenuehunt.com/how-to-guides/contact-customer-support/).

    For theme modifications, please consult your theme developer or Shopify Expert.


---

This article explains how to update your Shopify cart drawer products after the quiz.









