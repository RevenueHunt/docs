---
description: "Learn how to selectively sync product collections with RevenueHunt for optimized quiz performance."
icon: material/folder-sync-outline
---

# How to Selectively Sync Product Collections

=== "Shopify"

    !!! note "Not needed on this platform"

        The `💎Built for Shopify` version reads your products live from Shopify through the Storefront API, so there is no imported catalog to trim. See [How to Import Your Catalog](/how-to-guides/sync-catalog/).

=== "Shopify (Legacy)"

    A catalog above roughly 5,000 items does not have to go into the quiz whole. The `collections-first` feature syncs only the collections you pick.

    That keeps the quiz fast, and keeps a large catalog from running into technical trouble.

    !!! info "Ask support to switch it on"

        This feature is enabled per account. [Contact support](/how-to-guides/contact-customer-support/) to have it turned on for yours.

=== "WooCommerce"

    A catalog above roughly 5,000 items does not have to go into the quiz whole. The `categories-first` feature syncs only the categories you pick.

    That keeps the quiz fast, and keeps a large catalog from running into technical trouble.

    !!! info "Ask support to switch it on"

        This feature is enabled per account. [Contact support](/how-to-guides/contact-customer-support/) to have it turned on for yours.

=== "Magento"

    !!! note "Not available on this platform"

        This version syncs the whole catalog. You cannot pick which categories go into the quiz.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version syncs the whole catalog. You cannot pick which categories go into the quiz.

=== "Standalone"

    The Standalone version has no store catalog to trim. You build the catalog inside the app, or upload a Google Product Feed.

    See [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/).

## Selecting collections/categories for synchronization

=== "Shopify"

    !!! note "Not needed on this platform"

        The `💎Built for Shopify` version reads your products live from Shopify through the Storefront API, so there is no imported catalog to trim. See [How to Import Your Catalog](/how-to-guides/sync-catalog/).

=== "Shopify (Legacy)"

    1. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the `Dashboard`.**

    2. **Click `Choose Active Collections/Categories` under `Sync Products from your store`.**

    3. **Toggle on each collection you want in the quiz.** The number in brackets is how many products that collection holds.

        ![how to sync selected collections](/images/how_to_sync_selected_collections.gif)

        !!! warning "Your plan sets a product limit"

            Once the products you have selected reach the limit of your plan, no further collections can be activated.

    4. **Click `run manual sync`.**

        !!! info "What happens from then on"

            The app refreshes the products in the synced collections once a day, so the quiz keeps current prices and availability.

=== "WooCommerce"

    1. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the `Dashboard`.**

    2. **Click `Choose Active Collections/Categories` under `Sync Products from your store`.**

    3. **Toggle on each category you want in the quiz.** The number in brackets is how many products that category holds.

        ![how to sync selected collections](/images/how_to_sync_selected_collections.gif)

        !!! warning "Your plan sets a product limit"

            Once the products you have selected reach the limit of your plan, no further categories can be activated.

    4. **Click `run manual sync`.**

        !!! info "What happens from then on"

            The app refreshes the products in the synced categories once a day, so the quiz keeps current prices and availability.

=== "Magento"

    !!! note "Not available on this platform"

        This version syncs the whole catalog. You cannot pick which categories go into the quiz.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version syncs the whole catalog. You cannot pick which categories go into the quiz.

=== "Standalone"

    !!! note "Not available on this platform"

        This version has no store to sync from. Add your products in the app instead, as [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/) describes.

---

This article explains how to sync only the collections or categories your quiz needs.