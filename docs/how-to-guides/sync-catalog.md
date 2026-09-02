---
icon: material/sync
description: "Learn how to import and sync your product catalog with RevenueHunt quiz builder."
---

# How to Import Your Catalog

=== "Shopify"

    Tags, collections, vendors and metafields reach the quiz builder through a catalog import. Run the import when one of them is missing from a dropdown.

    This article explains what the import covers and how to trigger it.

=== "Shopify (Legacy)"

    Products and collections reach the [Link Products](/reference/quiz-builder/link-products/) and [Link Collections/Categories](/reference/quiz-builder/link-collections/) tabs through a catalog sync. Run the sync when something is missing from those lists.

    This article explains what the sync covers, how to trigger it, and what to do when it does not finish.

=== "WooCommerce"

    Products and collections reach the [Link Products](/reference/quiz-builder/link-products/) and [Link Collections/Categories](/reference/quiz-builder/link-collections/) tabs through a catalog sync. Run the sync when something is missing from those lists.

    This article explains what the sync covers, how to trigger it, and what to do when it does not finish.

=== "Magento"

    Products and collections reach the [Link Products](/reference/quiz-builder/link-products/) and [Link Collections/Categories](/reference/quiz-builder/link-collections/) tabs through a catalog sync. Run the sync when something is missing from those lists.

    This article explains what the sync covers, how to trigger it, and what to do when it does not finish.

=== "BigCommerce"

    Products and collections reach the [Link Products](/reference/quiz-builder/link-products/) and [Link Collections/Categories](/reference/quiz-builder/link-collections/) tabs through a catalog sync. Run the sync when something is missing from those lists.

    This article explains what the sync covers, how to trigger it, and what to do when it does not finish.

=== "Standalone"

    Products and collections reach the [Link Products](/reference/quiz-builder/link-products/) and [Link Collections/Categories](/reference/quiz-builder/link-collections/) tabs through a catalog sync. Run the sync when something is missing from those lists.

    This article explains what the sync covers, how to trigger it, and what to do when it does not finish.

## Import your catalog

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/4-MTXwFFwtU?si=M-wK6Gi4b0XXWEkU" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! info "What the import does, and does not do"

        Product names, descriptions, prices and images are pulled live from Shopify through the Storefront API every time a results page renders. They are never part of the import, and they are never out of date.

        The import brings in **tags, collections, vendors, variants and metafields**, so that they appear in the quiz builder dropdowns. It runs on its own every 24 hours.

    A manual import is only needed when you have just added tags, collections or metafields in Shopify and they are not in the builder yet.

    1. **Go to [App settings > Catalog](/reference/app-settings/#catalog).**

    2. **Click `Import now` in the `Import tags, collections, vendors & metafields` section.**

        ![manual_shopifyV2_appsettings_catalogue](/images/manual_shopifyV2_appsettings_catalogue.png)

    3. **Wait for the `Imported` timestamp to change.** Click `Refresh` if it still shows the old time once the import has finished.

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Go to your [Dashboard](/reference/dashboard/) and find the [Success Checklist](/reference/dashboard/#success-checklist).**

    2. **Click `run manual sync` under `SYNC PRODUCTS FROM YOUR STORE`.** The sync takes 30 to 60 minutes, depending on the size of your catalog.

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Go to your [Dashboard](/reference/dashboard/) and find the [Success Checklist](/reference/dashboard/#success-checklist).**

    2. **Click `run manual sync` under `SYNC PRODUCTS FROM YOUR STORE`.** The sync takes 30 to 60 minutes, depending on the size of your catalog.

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Go to your [Dashboard](/reference/dashboard/) and find the [Success Checklist](/reference/dashboard/#success-checklist).**

    2. **Click `run manual sync` under `SYNC PRODUCTS FROM YOUR STORE`.** The sync takes 30 to 60 minutes, depending on the size of your catalog.

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Go to your [Dashboard](/reference/dashboard/) and find the [Success Checklist](/reference/dashboard/#success-checklist).**

    2. **Click `run manual sync` under `SYNC PRODUCTS FROM YOUR STORE`.** The sync takes 30 to 60 minutes, depending on the size of your catalog.

=== "Standalone"

    1. **Go to your [Dashboard](/reference/dashboard/) and find the [Success Checklist](/reference/dashboard/#success-checklist).**

    2. **Click `run manual sync` under `SYNC PRODUCTS FROM YOUR STORE`.** The sync takes 30 to 60 minutes, depending on the size of your catalog.

## Import details

=== "Shopify"

    - The import runs **automatically every 24 hours**.
    - Only products marked **active** are included. **Archived products are excluded.**
    - **Draft products are included**, unless you exclude them in your [Catalog Settings](/reference/app-settings/#catalog).
    - A manual import is rarely needed. Run one when new tags, collections or vendors have not reached the quiz builder yet.
    - The `Import now` button lives in [App settings > Catalog](/reference/app-settings/#catalog).

    !!! warning "A metafield in the dropdown is not the whole story"

        Finding a metafield during the import only puts it in the dropdown list. Showing that metafield on a live quiz also needs Storefront API access for its definition in Shopify.

        See [How to enable storefront API access](/how-to-guides/show-product-reviews/#how-to-enable-storefront-api-access) for the steps.

=== "Shopify (Legacy)"

    !!! info "The app syncs on its own"

        The app syncs your catalog every 24 hours, and again whenever your store catalog changes. That covers products, collections, tags, variants and vendors.

    - The **first** sync after you install the app takes the longest. Depending on the size of your catalog, expect **30 minutes to several hours**.
    - Only products marked **active** are synced and appear in the dropdowns. **Draft and archived products are excluded.**
    - You can run a manual sync **once an hour**.
    - Make your store changes before you run a manual sync, so that the sync picks them up.

=== "WooCommerce"

    !!! info "The app syncs on its own"

        The app syncs your catalog every 24 hours, and again whenever your store catalog changes. That covers products, collections, tags, variants and vendors.

    !!! warning "A variable product syncs one attribute only"

        If a variable product varies by two attributes, such as size and color, the app syncs the first one and leaves the second behind.

    - The **first** sync after you install the app takes the longest. Depending on the size of your catalog, expect **30 minutes to several hours**.
    - Only products marked **active** are synced and appear in the dropdowns. **Draft and archived products are excluded.**
    - You can run a manual sync **once an hour**.
    - Make your store changes before you run a manual sync, so that the sync picks them up.

=== "Magento"

    !!! info "The app syncs on its own"

        The app syncs your catalog every 24 hours, and again whenever your store catalog changes. That covers products, collections, tags, variants and vendors.

    - The **first** sync after you install the app takes the longest. Depending on the size of your catalog, expect **30 minutes to several hours**.
    - Only products marked **active** are synced and appear in the dropdowns. **Draft and archived products are excluded.**
    - You can run a manual sync **once an hour**.
    - Make your store changes before you run a manual sync, so that the sync picks them up.

=== "BigCommerce"

    !!! info "The app syncs on its own"

        The app syncs your catalog every 24 hours, and again whenever your store catalog changes. That covers products, collections, tags, variants and vendors.

    - The **first** sync after you install the app takes the longest. Depending on the size of your catalog, expect **30 minutes to several hours**.
    - Only products marked **active** are synced and appear in the dropdowns. **Draft and archived products are excluded.**
    - You can run a manual sync **once an hour**.
    - Make your store changes before you run a manual sync, so that the sync picks them up.

=== "Standalone"

    !!! info "The app syncs on its own"

        The app syncs your catalog every 24 hours, and again whenever your store catalog changes. That covers products, collections, tags, variants and vendors.

    - The **first** sync after you install the app takes the longest. Depending on the size of your catalog, expect **30 minutes to several hours**.
    - Only products marked **active** are synced and appear in the dropdowns. **Draft and archived products are excluded.**
    - You can run a manual sync **once an hour**.
    - Make your store changes before you run a manual sync, so that the sync picks them up.

## Troubleshooting import issues

=== "Shopify"

    - **Tags, collections or vendors missing from the builder?** Run a manual import from [App settings > Catalog](/reference/app-settings/#catalog) with `Import now`. New items appear within a few minutes.
    - **A product missing?** Check that it is set to `Active` in your Shopify store. Archived products are excluded from the import.
    - **Import stuck, or failed?** Check the import status in [App settings > Catalog](/reference/app-settings/#catalog). Click `Import now` to retry a failed import. If it keeps failing, [contact the support team](/how-to-guides/contact-customer-support/).

=== "Shopify (Legacy)"

    - **Nothing showing up, or product counts still at zero?** The first sync may still be running, or it may have stopped early. Check the sync status before anything else.
    - **Still missing after the expected sync time?** [Contact the support team](/how-to-guides/contact-customer-support/). The team can run a full sync of your shop by hand.

=== "WooCommerce"

    - **Nothing showing up, or product counts still at zero?** The first sync may still be running, or it may have stopped early. Check the sync status before anything else.
    - **Still missing after the expected sync time?** [Contact the support team](/how-to-guides/contact-customer-support/). The team can run a full sync of your shop by hand.

=== "Magento"

    - **Nothing showing up, or product counts still at zero?** The first sync may still be running, or it may have stopped early. Check the sync status before anything else.
    - **Still missing after the expected sync time?** [Contact the support team](/how-to-guides/contact-customer-support/). The team can run a full sync of your shop by hand.

=== "BigCommerce"

    - **Nothing showing up, or product counts still at zero?** The first sync may still be running, or it may have stopped early. Check the sync status before anything else.
    - **Still missing after the expected sync time?** [Contact the support team](/how-to-guides/contact-customer-support/). The team can run a full sync of your shop by hand.

=== "Standalone"

    - **Nothing showing up, or product counts still at zero?** The first sync may still be running, or it may have stopped early. Check the sync status before anything else.
    - **Still missing after the expected sync time?** [Contact the support team](/how-to-guides/contact-customer-support/). The team can run a full sync of your shop by hand.

## Selectively import product collections/categories

=== "Shopify"

    !!! note "Not needed on this platform"

        The app imports data only for the products and collections your quizzes use.

=== "Shopify (Legacy)"

    A catalog above roughly 5,000 items does not have to go into the quiz whole. The `collections-first` feature imports only the collections you choose.

    [How to Selectively Sync Product Collections](/how-to-guides/sync-selected-collections/)

=== "WooCommerce"

    A catalog above roughly 5,000 items does not have to go into the quiz whole. The `categories-first` feature imports only the categories you choose.

    [How to Selectively Sync Product Collections](/how-to-guides/sync-selected-collections/)

=== "Magento"

    !!! note "Not available on this platform"

        This version imports the whole catalog.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version imports the whole catalog.

=== "Standalone"

    !!! note "Not available on this platform"

        This version imports the whole catalog.

---

This article explains how to import your catalog data into the RevenueHunt app.