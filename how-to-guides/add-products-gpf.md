---
description: "Learn how to add products manually or import them from Google Merchant Center to your RevenueHunt Standalone app catalog."
icon: material/package-variant-plus
---

# How to Add Products in Standalone RevenueHunt App

The Standalone version has no store behind it, so its catalogue is yours to fill. You can type the products in one at a time, or import them from Google Merchant Center as a Google Product Feed XML file.

## Add products manually

=== "Shopify"

    !!! note "Not available on this platform"

        Your products come from Shopify, and the app imports them for you. There is nothing to add by hand.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "Shopify (Legacy)"

    !!! note "Not available on this platform"

        Your products come from Shopify, and the app imports them for you. There is nothing to add by hand.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Your products come from WooCommerce, and the app imports them for you. There is nothing to add by hand.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "Magento"

    !!! note "Not available on this platform"

        Your products come from Magento, and the app imports them for you. There is nothing to add by hand.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Your products come from BigCommerce, and the app imports them for you. There is nothing to add by hand.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "Standalone"

    These steps add products and collections by hand, through the RevenueHunt catalogue.

    1. **Open your RevenueHunt dashboard and find the Success Checklist icons.** They look like ❓❗✅ 🔄.

    2. **Click the 🔄 icon to open the Sync section.**

        ![Sync section of the Success Checklist](/images/manual_standalone_succcesschecklist.png){width="500"}

    3. **Click `View Catalog`.** The [Catalogue](https://admin.revenuehunt.com/catalogue) opens, where you manage your products.

        ![View Catalog button in the Success Checklist](/images/manual_standalone_succcesschecklist_products.png){width="500"}

    4. **Click `+ add new product`.**

    5. **Type a name for the product and click `Create`.**

    6. **Fill in the product details, to match what you sell.** Your changes save as you make them.

        ![Add new product in the Catalogue](/images/manual_standalone_succcesschecklist_catalogue_add_product.png)

    7. **Click `+ add new collection` to group products together.**

    8. **Type a name for the collection and click `Create`.**

    9. **Pick the products that belong in it from the dropdown.** Your changes save as you make them.

        ![Add new collection in the Catalogue](/images/manual_standalone_succcesschecklist_catalogue_add_collection.png)

## Add products via Google Merchant Center

=== "Shopify"

    !!! note "Not available on this platform"

        The app reads your Shopify catalog directly, so it needs no product feed.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "Shopify (Legacy)"

    !!! note "Not available on this platform"

        The app reads your Shopify catalog directly, so it needs no product feed.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "WooCommerce"

    !!! note "Not available on this platform"

        The app reads your WooCommerce catalog directly, so it needs no product feed.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "Magento"

    !!! note "Not available on this platform"

        The app reads your Magento catalog directly, so it needs no product feed.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        The app reads your BigCommerce catalog directly, so it needs no product feed.

        See [how to import your catalog](/how-to-guides/sync-catalog/).

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.289308176100626%; height: 0;"><iframe src="https://www.loom.com/embed/5817998bfddb47c7a13d1adb28beeb05?sid=584e70a7-c306-407a-a76e-7b370108c0c8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    These steps import your products from Google Merchant Center in one go.

    1. **Open your RevenueHunt dashboard and find the Success Checklist icons.** They look like ❓❗✅ 🔄.

    2. **Click the 🔄 icon to open the Sync section.**

        ![Sync section of the Success Checklist](/images/manual_standalone_succcesschecklist.png){width="500"}

    3. **Click `>activate Google Product Feed`.**

        ![Activate Google Product Feed in the Success Checklist](/images/manual_standalone_succcesschecklist_products.png){width="500"}

    4. **Paste your feed URL into the `Add your Google Product Feed:` field.** The address has to end in `.xml`.

        ![Google Product Feed URL field](/images/manual_standalone_succcesschecklist_productfeed.png)

    5. **Wait while the app reads the feed.** Your products and collections arrive in the quiz account.

    ??? info "Finding your Google Product Feed URL"

        1. **Sign in at [merchants.google.com](https://merchants.google.com/).**

        2. **Click `Products`, then `Manage product sources`.**

        3. **Click the name of your data source.**

        4. **Copy the address in the `File URL` field, under `Data source setup`.**

        That address is what step 4 above asks for.

    ??? tip "Hosting the XML file yourself"

        A feed does not have to come from Google. Any public address ending in `.xml` works.

        - **Shopify.** Go to `Settings` → `Files`, upload `google_product_feed.xml`, and copy the address Shopify gives you. It looks like `https://cdn.shopify.com/s/files/.../google_product_feed.xml`.
        - **Your own hosting.** Upload the file over FTP, through cPanel File Manager, or with your CMS media library.
        - **Cloud storage.** Dropbox, Google Drive with a direct link, or Amazon S3. The link has to be public.

    !!! warning "The file has to be a valid Google Product Feed"

        Not every XML file works. Check yours against the [Google Merchant Center feed specification](https://support.google.com/merchants/answer/12631822?hl=en), and run it through the [Google feed validation service](https://developers.google.com/product-review-feeds/validation/).

        If the feed looks right and still does not import, [contact support](/how-to-guides/contact-customer-support/).

## What to do next

Once your catalogue holds products, the quiz can start recommending them.

- [Start building your quiz](/how-to-guides/create-first-quiz/)
- [Set up product recommendations](/how-to-guides/set-up-recommendations/)
- [Customize your quiz design](/how-to-guides/customize-quiz-design/)

---

This article explains how to fill the Standalone catalogue, by hand or from a Google Product Feed.