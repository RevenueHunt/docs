---
description: "Fix RevenueHunt quiz viewport issues on mobile devices to ensure the quiz remains fixed and provides a smooth user experience."
icon: material/cellphone-link
---

# Fixing Viewport Issue on Mobile

On a mobile device, the quiz can zoom in slightly when the customer taps a text input. The page then shifts from left to right, and the quiz no longer sits still.

## Problem description

The cause is the meta viewport tag in your store theme. Without a maximum scale, the browser zooms in on a focused input, and the page moves with it.

## Solution

Your developer edits the meta viewport tag in the store theme to add `maximum-scale=1.0` and `user-scalable=0`. Those two values stop the page from moving.

### Step-by-step guide

1. Locate the meta viewport tag in the HTML of your store. It might look like this:

   ```html
   <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
   ```

2. Modify the tag to include `maximum-scale=1.0` and `user-scalable=0`:

   ```html
   <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0">
   ```

3. If the meta viewport tag is missing, add the modified tag to the `<head>` section of your HTML.

![Meta viewport tag in a store theme](/images/fix_viewport_issue_mobile.png)

## Testing

Test the quiz on a mobile device. Tap a text input and check that the page stays still.

## Additional notes

- Apply the change to the theme your store is actually using.
- If the problem continues, ask your web developer for help.

## Platform-specific instructions

=== "Shopify"

    1. In Shopify admin, go to **Online Store** > **Themes**.
    2. Click **...** next to your current theme and select **Edit code**.
    3. In the **Layout** section, open the `theme.liquid` file.
    4. Find the `<head>` section and edit the meta viewport tag there.

=== "Shopify (Legacy)"

    1. Log in to your Shopify admin panel.
    2. Go to **Online Store** > **Themes**.
    3. Click on **Actions** next to your current theme and select **Edit code**.
    4. In the **Layout** section, find and open the `theme.liquid` file.
    5. Locate the `<head>` section in this file to modify the meta viewport tag.

=== "WooCommerce"

    1. Log in to your WordPress admin panel.
    2. Go to **Appearance** > **Theme Editor**.
    3. In the **Theme Files** section, find and open the `header.php` file of your active theme.
    4. Locate the `<head>` section in this file to modify the meta viewport tag.

=== "Magento"

    Magento builds the `<head>` from a layout file rather than from a template you can edit in the admin, so this is a developer task.

    1. In your theme, open or create `Magento_Theme/layout/default_head_blocks.xml`.
    2. Add the meta viewport tag to the `<head>` section of that file.
    3. Deploy the static content and flush the cache.

    !!! tip

        For the file layout and an example, see the Adobe Commerce documentation on [managing layouts](https://developer.adobe.com/commerce/frontend-core/guide/layouts/xml-manage).

=== "BigCommerce"

    A Stencil theme defines the `<head>` in its base layout, so this is a developer task.

    1. In your Stencil theme, open `templates/layout/base.html`.
    2. Find the `<head>` section and edit the meta viewport tag there.
    3. Push the theme to your store.

    !!! tip

        For how a Stencil theme is put together, see the BigCommerce documentation on [page composition and styling](https://developer.bigcommerce.com/docs/storefront/stencil/themes/style/composition-and-styling).

=== "Standalone"

    The Standalone quiz runs on your own page, so the meta viewport tag is in your own HTML.

    1. Open the page that holds the quiz.
    2. Find the `<head>` section and edit the meta viewport tag there.

    !!! note "Platform Availability"

        A quiz opened through a RevenueHunt hosted link is not affected. This applies only to a quiz you embed on your own page.
