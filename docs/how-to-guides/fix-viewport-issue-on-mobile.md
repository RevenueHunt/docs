# Fixing Viewport Issue on Mobile

## Introduction

This guide addresses a common issue where the form on mobile devices is not fixed and moves from side to side, causing a poor user experience. This problem can be resolved by adjusting the meta viewport tag in the store's HTML.

## Problem Description

Users have reported that on mobile devices, the form page is not fixed and moves from left to right, causing a poor user experience. This issue needs to be addressed to ensure the form remains fixed on mobile devices.

## Solution

To fix this issue, the developer needs to modify the meta viewport tag in the store's HTML. The tag should include `maximum-scale=1.0` and `user-scalable=0` to prevent the page from moving.

### Step-by-Step Guide

1. Locate the meta viewport tag in the HTML of your store. It might look like this:

   ```html
   <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
   ```

2. Modify the tag to include `maximum-scale=1.0` and `user-scalable=0`:

   ```html
   <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0">
   ```

3. If the meta viewport tag is missing, add the modified tag to the `<head>` section of your HTML.

## Testing

After making these changes, test the form on a mobile device to ensure it remains fixed and does not move from side to side.

## Additional Notes

- Ensure that the changes are applied to the correct HTML file in your store.
- If you encounter any issues, consider reaching out to your web developer for assistance.

## Platform-Specific Instructions

=== "Shopify"

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