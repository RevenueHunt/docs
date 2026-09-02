---
description: "Learn how to fix product images not showing in your RevenueHunt quiz and troubleshoot missing images from your catalog."
icon: material/image-off
---

# How to Fix Product Images Not Showing

A recommended product can arrive on the results page with no picture. Where the picture was meant to come from decides what to check.

=== "Shopify"

    Product and collection images come straight from your Shopify catalog, so a blank one is nearly always blank in Shopify.

    1. **Open the product in your Shopify admin and check it has an image.**

    2. **For a recommended collection, check the collection itself has one.** A collection carries no image until you give it one, under `Products > Collections`.

    3. **Take the quiz and check the image appears on the results page.**

    !!! tip "The image is in Shopify but not in the quiz"

        Images are read live from Shopify on this version, so there is nothing to sync and no cache to clear. If the product has an image and the quiz still shows none, [contact customer support](/how-to-guides/contact-customer-support/).

=== "Shopify (Legacy)"

    Product and collection images come straight from your Shopify catalog, so a blank one is nearly always blank in Shopify.

    1. **Open the product in your Shopify admin and check it has an image.**

    2. **For a recommended collection, check the collection itself has one.** A collection carries no image until you give it one, under `Products > Collections`.

    3. **Take the quiz and check the image appears on the results page.**

    !!! tip "The image is in Shopify but not in the quiz"

        Run a [catalog import](/how-to-guides/sync-catalog/), so your latest catalog reaches the quiz.

=== "WooCommerce"

    Your store holds the images, and the quiz runs in an iframe served from the RevenueHunt server. Every picture is therefore fetched across two domains, and anything that refuses those requests leaves it blank.

    1. **Check the product has an image in `Products` in your WordPress admin.**

    2. **Allow the RevenueHunt server through whatever is blocking it.** Add `admin.revenuehunt.com` and the IP address `3.14.55.225` to the allowlist of your firewall, security plugin or CDN.

    3. **Take the quiz and check the image appears on the results page.**

    !!! info "What is being blocked"

        Showing an image on one site by linking to the site that hosts it is called [hotlinking](https://simple.wikipedia.org/wiki/Hotlinking). Something between your store and the quiz is refusing those requests.

        WordPress allows hotlinking by default, so if your images are blocked, a security plugin, a CDN or your host has turned protection on. See this [guide to image hotlinking in WordPress](https://serverguy.com/disable-image-hotlinking-in-wordpress/).

    !!! tip "Other WordPress and WooCommerce problems"

        See [WordPress and WooCommerce troubleshooting](/how-to-guides/troubleshooting-product-recommendation-quiz-app-issues-for-wordpress-woocommerce/).

=== "Magento"

    Your store holds the images, and the quiz runs in an iframe served from the RevenueHunt server. Every picture is therefore fetched across two domains, and anything that refuses those requests leaves it blank.

    1. **Check the product has an image in your Magento admin.**

    2. **Allow the RevenueHunt server through whatever is blocking it.** Add `admin.revenuehunt.com` and the IP address `3.14.55.225` to the allowlist of your firewall, security plugin or CDN.

    3. **Take the quiz and check the image appears on the results page.**

    !!! info "What is being blocked"

        Showing an image on one site by linking to the site that hosts it is called [hotlinking](https://simple.wikipedia.org/wiki/Hotlinking). Something between your store and the quiz is refusing those requests.

=== "BigCommerce"

    Your store holds the images, and the quiz runs in an iframe served from the RevenueHunt server. Every picture is therefore fetched across two domains, and anything that refuses those requests leaves it blank.

    1. **Check the product has an image in your BigCommerce admin.**

    2. **Allow the RevenueHunt server through whatever is blocking it.** Add `admin.revenuehunt.com` and the IP address `3.14.55.225` to the allowlist of your firewall, security plugin or CDN.

    3. **Take the quiz and check the image appears on the results page.**

    !!! info "What is being blocked"

        Showing an image on one site by linking to the site that hosts it is called [hotlinking](https://simple.wikipedia.org/wiki/Hotlinking). Something between your store and the quiz is refusing those requests.

=== "Standalone"

    A standalone product carries the image URL you gave it, rather than one pulled from a store. A blank picture is nearly always a problem with that URL.

    1. **Open your [Catalogue](https://admin.revenuehunt.com/catalogue) and check the product's `Product Image URL` field is filled in.**

    2. **Paste that URL into a browser tab.** If the image does not load there, it will not load in the quiz either.

    3. **If your products come from a Google Product Feed, check the image URL for that product in the feed.** See [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/).

    4. **If the image sits on your own server, allow the RevenueHunt server to reach it.** Add `admin.revenuehunt.com` and the IP address `3.14.55.225` to the allowlist of your firewall or CDN.

    5. **Take the quiz and check the image appears on the results page.**

    !!! info "What is being blocked"

        Showing an image on one site by linking to the site that hosts it is called [hotlinking](https://simple.wikipedia.org/wiki/Hotlinking). Something between your store and the quiz is refusing those requests.

---

This article explains why a recommended product can appear with no picture, and what to check on each platform.