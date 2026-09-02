---
icon: material/cart-arrow-down
description: "Learn how to update your Shopify cart drawer when products are added via RevenueHunt quiz."
---

# How to Update Your Shopify Cart Drawer Products After the Quiz

The quiz adds products to the cart. On most themes it also refreshes your cart drawer and opens it, with no setup on your side.

This article explains what happens after `Add to Cart`, which themes need nothing from you, and what to do when a drawer still shows the old contents.

!!! note "Which version you are on decides what you have to do"

    The 💎 Built for Shopify app refreshes the drawer itself, so most stores need nothing. The legacy app does not, and the drawer still needs theme work. See [Cart drawer support in the legacy app](#cart-drawer-support-in-the-legacy-app).

## How the quiz adds products to the cart

The app uses Shopify's official AJAX Cart API, the same endpoints most Shopify themes and apps use:

- `cart/add.js` adds products to the cart.
- `cart/change.js` changes product quantities.
- `cart/update.js` updates the cart with new contents.
- `cart.js` retrieves the current state of the cart.

Once the cart has changed, the app does two more things:

- It announces the change on Shopify's standard storefront events. A theme that listens for them re-renders its own cart.
- It refreshes the drawer through the theme's own section rendering, then opens the drawer.

The app never edits your theme. It uses the contracts Shopify publishes for themes, and leaves the rendering to the theme.

## The two ways a theme refreshes its cart

Shopify themes refresh their cart in one of two ways. The app supports both, and it uses whichever one your theme provides.

**Cart sections.** The theme exposes its cart as a section that Shopify can render again. The app asks the drawer which sections it needs, fetches them, and hands the fresh markup back. The theme then paints its own drawer. Dawn and the themes built on it work this way.

**Standard cart events.** The theme renders its cart in the browser and listens for the cart events Shopify publishes. The app announces that the cart changed, and the theme re-renders its own cart. Horizon and the themes released with it work this way.

Neither needs setup from you. The app picks the contract your theme provides at the moment it adds the product.

!!! info "Why this matters"

    The app never writes markup into your drawer. It asks your theme to render its own cart, so your drawer keeps your theme's design, wording and currency formatting.

## Themes that need no setup

### Themes built on Horizon

These render the cart in the browser and update from Shopify's standard cart events.

- Horizon
- Savor
- Atelier
- Tinker
- Fabric
- Ritual
- Vessel
- Dwell
- Pitch
- Heritage

### Themes built on Dawn

These expose cart sections, so the app refreshes the drawer and then opens it.

- Dawn
- Rise
- Sense
- Refresh
- Craft
- Studio
- Taste
- Ride
- Colorblock
- Publisher
- Origin
- Spotlight
- Crave

A paid theme built on one of these also works, as long as it keeps the cart drawer its parent theme ships.

To find your theme name, go to **Online Store > Themes** in Shopify Admin.

!!! warning "Theme versions are not updated for you"

    Shopify does not update your theme automatically. A theme that is several versions behind can behave differently from the current release of the same theme. Check for a theme update before you report a problem.

!!! tip "Your theme is not on this list"

    The list is not exhaustive, and many other themes work. Two cases are worth reporting: a theme that is missing, and a listed theme whose drawer does not update. Contact support with your theme name and version. The support team checks the theme and adds coverage where possible. See [How to Contact Customer Support](/how-to-guides/contact-customer-support/).

## When the drawer still does not update

Two causes remain.

- **Your theme supports neither contract.** Some paid themes expose no section rendering and no standard events. The product reaches the cart, but nothing tells the drawer to refresh.
- **A cart app replaced your drawer.** Cart upsell and side cart apps often hide the theme drawer and render their own. The quiz refreshes the drawer your theme ships, which that app has hidden.

You have two ways forward.

**Option 1: Ask your developer to listen for the standard cart event**

The app announces every cart change as `shopify:cart:lines-update` on `document`. A developer can listen for that event, request the current cart, and re-render the drawer from it. That is what Shopify's own recent themes do, and it needs no change inside the app.

Share these with your developer or your Shopify Expert:

- [Shopify AJAX Cart API reference](https://shopify.dev/docs/api/ajax/reference/cart)
- [Shopify cart lines update event reference](https://shopify.dev/docs/api/storefront-events-and-actions/events/cart-lines-update)

**Option 2: Send the customer to the product page**

Change the checkout settings to send the customer to the product page rather than add the product to the cart. The customer then adds the product from your theme's own form, which every drawer already reacts to.

!!! tip "Changing what the button does"

    See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/#link-to-the-product-page).

## Cart drawer support in the legacy app

The legacy app calls the AJAX Cart API and nothing else. It does not announce cart changes and it does not refresh the drawer, so the theme has to do that work.

Your developer has to listen for those AJAX cart calls, then trigger the drawer's own open or refresh logic when one of them fires.

!!! example "How one merchant fixed it on the legacy app"

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

!!! tip "This work goes away on the current version"

    Moving to the Built for Shopify version removes this work on the themes listed under [Themes that need no setup](#themes-that-need-no-setup). See [How to Migrate Your Shopify Legacy Quiz](/how-to-guides/migrate-shopify-legacy-quiz/).

## Test the setup

1. **Take the quiz through to the results page and click `Add to Cart`.**
2. **Check that the products reach the cart.**
3. **Check that the drawer opens on its own, and that it shows the new products.**

!!! info "What the app does, and what it does not"

    The app updates the cart, announces the change, and refreshes and opens the theme's own drawer. It does not modify your cart drawer or your theme layout.

    The support team can confirm that the app is firing the right cart actions. See [How to Contact Customer Support](/how-to-guides/contact-customer-support/).

    Theme customization and third-party JavaScript are outside what support can debug. For those, ask your theme developer or a Shopify Expert.

---

This article explains how the quiz refreshes your cart drawer. It also covers which themes need no setup, and what to do when a drawer does not update.
