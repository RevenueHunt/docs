---
icon: material/sync
---

# How to Import Your Catalogue

=== "Shopify"


    If you're missing tags, collections, vendors, or metafields in the quiz builder within the Built for Shopify version of the RevenueHunt app, you can run a catalogue import from the app settings.

    This article explains what the catalogue import does and how to trigger it.


=== "Shopify (Legacy)"

    If you're missing products or collections from the list in the [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab, you can run a product sync from the app's dashboard.

    This article will guide you through troubleshooting and syncing your product catalog with the RevenueHunt app.

=== "WooCommerce"


    If you're missing products or collections from the list in the [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab, you can run a product sync from the app's dashboard.

    This article will guide you through troubleshooting and syncing your product catalog with the RevenueHunt app.

=== "Magento"

    If you're missing products or collections from the list in the [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab, you can run a product sync from the app's dashboard.

    This article will guide you through troubleshooting and syncing your product catalog with the RevenueHunt app.

=== "BigCommerce"


    If you're missing products or collections from the list in the [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab, you can run a product sync from the app's dashboard.

    This article will guide you through troubleshooting and syncing your product catalog with the RevenueHunt app.

=== "Standalone"


    If you're missing products or collections from the list in the [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab, you can run a product sync from the app's dashboard.

    This article will guide you through troubleshooting and syncing your product catalog with the RevenueHunt app.


## Import Your Catalogue

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/l-JPWb82zNA?si=AtL09re7OHc6fKXL" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    In the `💎Built for Shopify` version of the RevenueHunt app, product names, descriptions, prices, and images shown in quiz results are **always pulled live from Shopify** via the Storefront API. This data is always up to date — no import needed.

    The catalogue import pulls **tags, collections, vendors, variants, and metafields** from your Shopify store so they appear in the quiz builder's dropdown lists. This happens automatically every 24 hours. You only need a manual import if you've just added new tags or collections in Shopify and don't see them in the builder yet.

    To run a manual import:

    1. **Navigate to App Settings:** Go to [App Settings > Catalogue](/reference/app-settings/#catalogue).
    2. **Click "Import now"** in the *Import tags, collections, vendors & metafields* section.

        ![manual_shopifyV2_appsettings_catalogue](/images/manual_shopifyV2_appsettings_catalogue.png)


=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Navigate to Dashboard:** Log in to your [Dashboard](/reference/dashboard/) and locate the [Success Checklist](/reference/dashboard/#success-checklist).
    2. **Initiate Manual Sync:** Under the `SYNC PRODUCTS FROM YOUR STORE` section, click the `run manual sync` button. The sync takes about 30-60 minutes to complete depending on the size of your catalog.

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Navigate to Dashboard:** Log in to your [Dashboard](/reference/dashboard/) and locate the [Success Checklist](/reference/dashboard/#success-checklist).
    2. **Initiate Manual Sync:** Under the `SYNC PRODUCTS FROM YOUR STORE` section, click the `run manual sync` button. The sync takes about 30-60 minutes to complete depending on the size of your catalog.

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Navigate to Dashboard:** Log in to your [Dashboard](/reference/dashboard/) and locate the [Success Checklist](/reference/dashboard/#success-checklist).
    2. **Initiate Manual Sync:** Under the `SYNC PRODUCTS FROM YOUR STORE` section, click the `run manual sync` button. The sync takes about 30-60 minutes to complete depending on the size of your catalog.

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/i-CHRHuRcAs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Navigate to Dashboard:** Log in to your [Dashboard](/reference/dashboard/) and locate the [Success Checklist](/reference/dashboard/#success-checklist).
    2. **Initiate Manual Sync:** Under the `SYNC PRODUCTS FROM YOUR STORE` section, click the `run manual sync` button. The sync takes about 30-60 minutes to complete depending on the size of your catalog.

=== "Standalone"

    1. **Navigate to Dashboard:** Log in to your [Dashboard](/reference/dashboard/) and locate the [Success Checklist](/reference/dashboard/#success-checklist).
    2. **Initiate Manual Sync:** Under the `SYNC PRODUCTS FROM YOUR STORE` section, click the `run manual sync` button. The sync takes about 30-60 minutes to complete depending on the size of your catalog.

## Import Details

=== "Shopify"

    !!! info "What does the catalogue import do?"
        The import pulls tags, collections, vendors, variants, and metafields from your Shopify store so they appear in the quiz builder's dropdown lists. Product names, descriptions, prices, and images are **not** part of this import — they are always fetched live from Shopify when quiz results are displayed.

    - The catalogue import runs **automatically every 24 hours**.
    - Only products marked as **active** are included in the import. **Archived products are excluded**.
    - **Draft products are included** in the import unless you change your [Catalogue Settings](/reference/app-settings/#catalogue) to exclude them.
    - You typically don't need to run a manual import. It's only necessary when you've added new tags, collections, or vendors in Shopify and they haven't appeared in the quiz builder yet.
    - To run a manual import, use the `Import now` button in [App Settings > Catalogue](/reference/app-settings/#catalogue).


=== "Shopify (Legacy)"

    !!! info "Important"
        Our app automatically syncs your store's catalog every 24 hours and whenever changes are made in your store's catalog. This includes updates to products, collections, tags, variants, and vendors.

    - If you've **just installed the app**, remember that syncing your store's entire product catalog for the first time can take a bit. Depending on your catalog size, expect to wait anywhere from **30 minutes to several hours** for the sync to complete.
    - Only products marked as **active** will be synced with the app and appear in dropdown choices. **Draft or Archived products are excluded** from the sync and will not be visible.
    - You can manually sync your store **every 1 hour**. Additionally, our app automatically performs a sync every 24 hours to keep your catalog current.
    - For optimal results, make any necessary updates or changes to your store before triggering a manual sync. This ensures your latest product information is accurately reflected in the app.

=== "WooCommerce"

    !!! info "Important"
        Our app automatically syncs your store's catalog every 24 hours and whenever changes are made in your store's catalog. This includes updates to products, collections, tags, variants, and vendors.

    - If you've **just installed the app**, remember that syncing your store's entire product catalog for the first time can take a bit. Depending on your catalog size, expect to wait anywhere from **30 minutes to several hours** for the sync to complete.
    - Only products marked as **active** will be synced with the app and appear in dropdown choices. **Draft or Archived products are excluded** from the sync and will not be visible.
    - You can manually sync your store **every 1 hour**. Additionally, our app automatically performs a sync every 24 hours to keep your catalog current.
    - For optimal results, make any necessary updates or changes to your store before triggering a manual sync. This ensures your latest product information is accurately reflected in the app.

=== "Magento"

    !!! info "Important"
        Our app automatically syncs your store's catalog every 24 hours and whenever changes are made in your store's catalog. This includes updates to products, collections, tags, variants, and vendors.

    - If you've **just installed the app**, remember that syncing your store's entire product catalog for the first time can take a bit. Depending on your catalog size, expect to wait anywhere from **30 minutes to several hours** for the sync to complete.
    - Only products marked as **active** will be synced with the app and appear in dropdown choices. **Draft or Archived products are excluded** from the sync and will not be visible.
    - You can manually sync your store **every 1 hour**. Additionally, our app automatically performs a sync every 24 hours to keep your catalog current.
    - For optimal results, make any necessary updates or changes to your store before triggering a manual sync. This ensures your latest product information is accurately reflected in the app.

=== "BigCommerce"

    !!! info "Important"
        Our app automatically syncs your store's catalog every 24 hours and whenever changes are made in your store's catalog. This includes updates to products, collections, tags, variants, and vendors.

    - If you've **just installed the app**, remember that syncing your store's entire product catalog for the first time can take a bit. Depending on your catalog size, expect to wait anywhere from **30 minutes to several hours** for the sync to complete.
    - Only products marked as **active** will be synced with the app and appear in dropdown choices. **Draft or Archived products are excluded** from the sync and will not be visible.
    - You can manually sync your store **every 1 hour**. Additionally, our app automatically performs a sync every 24 hours to keep your catalog current.
    - For optimal results, make any necessary updates or changes to your store before triggering a manual sync. This ensures your latest product information is accurately reflected in the app.

=== "Standalone"

    !!! info "Important"
        Our app automatically syncs your store's catalog every 24 hours and whenever changes are made in your store's catalog. This includes updates to products, collections, tags, variants, and vendors.

    - If you've **just installed the app**, remember that syncing your store's entire product catalog for the first time can take a bit. Depending on your catalog size, expect to wait anywhere from **30 minutes to several hours** for the sync to complete.
    - Only products marked as **active** will be synced with the app and appear in dropdown choices. **Draft or Archived products are excluded** from the sync and will not be visible.
    - You can manually sync your store **every 1 hour**. Additionally, our app automatically performs a sync every 24 hours to keep your catalog current.
    - For optimal results, make any necessary updates or changes to your store before triggering a manual sync. This ensures your latest product information is accurately reflected in the app.

## Troubleshooting Import Issues

=== "Shopify"

    - **Missing tags, collections, or vendors in the builder?** Run a manual import from [App Settings > Catalogue](/reference/app-settings/#catalogue) by clicking `Import now`. New items should appear within a few minutes.
    - **Products not showing up?** Check that they are set to "Active" status in your Shopify store. Archived products are excluded from the import.
    - **Import stuck or failed?** Check the import status in [App Settings > Catalogue](/reference/app-settings/#catalogue). If it shows "Import failed", click `Import now` to retry. If problems persist, please [contact our support team](/how-to-guides/contact-customer-support/) for assistance.


=== "Shopify (Legacy)"

    - **Check Sync Status:** If your products or collections aren't showing up as expected, or if the product counts remain at zero, it's possible the initial sync is still in progress or has encountered an issue.
    - **Contact Support:** Should issues persist beyond the expected sync time, please [contact our support team](/how-to-guides/contact-customer-support/). We can manually initiate a complete sync of your shop to ensure everything is up-to-date.

=== "WooCommerce"

    - **Check Sync Status:** If your products or collections aren't showing up as expected, or if the product counts remain at zero, it's possible the initial sync is still in progress or has encountered an issue.
    - **Contact Support:** Should issues persist beyond the expected sync time, please [contact our support team](/how-to-guides/contact-customer-support/). We can manually initiate a complete sync of your shop to ensure everything is up-to-date.

=== "Magento"

    - **Check Sync Status:** If your products or collections aren't showing up as expected, or if the product counts remain at zero, it's possible the initial sync is still in progress or has encountered an issue.
    - **Contact Support:** Should issues persist beyond the expected sync time, please [contact our support team](/how-to-guides/contact-customer-support/). We can manually initiate a complete sync of your shop to ensure everything is up-to-date.

=== "BigCommerce"

    - **Check Sync Status:** If your products or collections aren't showing up as expected, or if the product counts remain at zero, it's possible the initial sync is still in progress or has encountered an issue.
    - **Contact Support:** Should issues persist beyond the expected sync time, please [contact our support team](/how-to-guides/contact-customer-support/). We can manually initiate a complete sync of your shop to ensure everything is up-to-date.

=== "Standalone"

    - **Check Sync Status:** If your products or collections aren't showing up as expected, or if the product counts remain at zero, it's possible the initial sync is still in progress or has encountered an issue.
    - **Contact Support:** Should issues persist beyond the expected sync time, please [contact our support team](/how-to-guides/contact-customer-support/). We can manually initiate a complete sync of your shop to ensure everything is up-to-date.

## Selectively Import Product Collections/Categories

=== "Shopify"

    This feature is not needed. The app only imports data for the products and collections you use in your quizzes.


=== "Shopify (Legacy)"

    For stores with extensive product catalogs, especially those exceeding 5,000 items, it might not be practical or desirable to include every single product in your quiz recommendations. Fortunately,RevenueHunt app offers a targeted solution: the `collections-first` feature. 

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/sync-selected-collections/)

=== "WooCommerce"

    For stores with extensive product catalogs, especially those exceeding 5,000 items, it might not be practical or desirable to include every single product in your quiz recommendations. Fortunately, RevenueHunt app offers a targeted solution: the `categories-first` feature. 

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/sync-selected-collections/)

=== "Magento"

    This feature is not available.

=== "BigCommerce"

    This feature is not available.

=== "Standalone"

    This feature is not available.

---
This article explains how to import your catalogue data into the RevenueHunt app.

By following these steps, you can ensure your tags, collections, vendors, and metafields are up to date in the quiz builder.