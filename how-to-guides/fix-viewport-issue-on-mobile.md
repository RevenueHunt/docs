---
description: "Fix RevenueHunt quiz viewport issues on mobile devices to ensure the quiz remains fixed and provides a smooth user experience."
icon: material/cellphone-link
---

# How to Fix the Mobile Viewport Issue

On a phone, the quiz can zoom in when the customer taps a text input. The page then drifts left and right, and the quiz no longer sits still.

## Why it happens

The meta viewport tag in your store theme sets no maximum scale. Without one, the browser is free to zoom in on a focused input, and the page moves with it.

Adding `maximum-scale=1.0` and `user-scalable=0` to that tag stops the zoom, and the page stays put.

!!! warning "This is a change to your theme"

    The tag lives in your store theme, not in the quiz. Ask your developer to make the change if you are not comfortable editing theme files.

## Find the meta viewport tag

=== "Shopify"

    1. **In your Shopify admin, go to `Online Store > Themes`.**

    2. **Click `...` next to your current theme and select `Edit code`.**

    3. **Open `theme.liquid`, in the `Layout` section.**

    4. **Find the `<head>` section.** The meta viewport tag sits inside it.

=== "Shopify (Legacy)"

    1. **In your Shopify admin, go to `Online Store > Themes`.**

    2. **Click `Actions` next to your current theme and select `Edit code`.**

    3. **Open `theme.liquid`, in the `Layout` section.**

    4. **Find the `<head>` section.** The meta viewport tag sits inside it.

=== "WooCommerce"

    1. **In your WordPress admin, go to `Appearance > Theme Editor`.**

    2. **Open the `header.php` file of your active theme, in the `Theme Files` list.**

    3. **Find the `<head>` section.** The meta viewport tag sits inside it.

=== "Magento"

    Magento builds the `<head>` from a layout file rather than from a template you can edit in the admin, so this one is a developer task.

    1. **Open or create `Magento_Theme/layout/default_head_blocks.xml` in your theme.**

    2. **Add the meta viewport tag to the `<head>` section of that file.**

    3. **Deploy the static content and flush the cache.**

    !!! tip "The file layout, with an example"

        See the Adobe Commerce documentation on [managing layouts](https://developer.adobe.com/commerce/frontend-core/guide/layouts/xml-manage).

=== "BigCommerce"

    A Stencil theme defines the `<head>` in its base layout, so this one is a developer task.

    1. **Open `templates/layout/base.html` in your Stencil theme.**

    2. **Find the `<head>` section.** The meta viewport tag sits inside it.

    3. **Push the theme to your store once you have made the change.**

    !!! tip "How a Stencil theme is put together"

        See the BigCommerce documentation on [page composition and styling](https://developer.bigcommerce.com/docs/storefront/stencil/themes/style/composition-and-styling).

=== "Standalone"

    The quiz runs on a page of your own, so the meta viewport tag is in your own HTML.

    1. **Open the page that holds the quiz.**

    2. **Find the `<head>` section.** The meta viewport tag sits inside it.

    !!! note "A hosted quiz link is not affected"

        This only applies to a quiz you embed on your own page. A quiz opened through a RevenueHunt hosted link runs on a page whose viewport is already set.

!!! warning "Edit the theme your store is actually using"

    A store can hold several themes. Make the change in the published one, or nothing will change for your customers.

## Add the two values

1. **Find the tag.** It usually looks like this.

    ```html
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
    ```

2. **Add `maximum-scale=1.0` and `user-scalable=0` to the end of the `content` attribute.**

    ```html
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0">
    ```

    ![Meta viewport tag in a store theme](/images/fix_viewport_issue_mobile.png)

3. **Save the file.**

!!! note "No viewport tag in the file"

    Add the whole tag from step 2 to the `<head>` section yourself.

## Test the fix

Open the quiz on a phone and tap a text input. The page should stay still.

If it still zooms, the theme you edited may not be the published one, or a second viewport tag may be overriding the first. Ask your developer to check.

---

This article explains why a quiz zooms in on a phone, and how to stop it in your store theme.