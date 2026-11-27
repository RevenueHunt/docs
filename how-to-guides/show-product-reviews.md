---
icon: material/star-box
description: "Learn how to display product reviews on your RevenueHunt quiz results page."
---

# How to Show Product Reviews

Add a star rating and a review count to the product cards on your quiz results page. The ratings come from the review app you already use.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/0nRTov-gCxY?si=33FdTH4HYZ7UDM04" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Results page](/reference/quiz-builder/results-page/) tab.**

    2. **Find the [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) that recommends the products.**

    3. **Open [`Product Component Layout`](/reference/quiz-builder/results-page/#slot-item-composition), under `Recommended Products`.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2.png)

    4. **Click `+ Add Block` and select the `Reviews` section.** A star rating box appears at the bottom of the product card.

        ![Add Reviews Block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_reviews.png)

    5. **Open the `Reviews` tab and pick your review app from the dropdown.**

        ![Add Reviews Block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_reviews_apps.png)

        !!! info "Supported review apps"

            Judge.me, Yotpo, Stamped and Loox. The screenshot uses Judge.me.

    6. **Drag the reviews section to where you want it in the product component layout.** Right below the product title works well.

    7. **Expose the review metafields to the Storefront API in Shopify.** The stars stay empty until you do. See [Enabling storefront API access for review apps](#enabling-storefront-api-access-for-review-apps).

    8. **Click the top-right `Save` button.**

    9. **Click `Preview` and check that the ratings appear.**

    ## Enabling storefront API access for review apps

    Every review app stores its product ratings in Shopify metafields. The RevenueHunt app can only read a metafield that is **exposed to the Storefront API**, and most review apps keep theirs private.

    !!! info "Which metafields are used?"

        All supported review apps use Shopify's reserved `reviews` namespace:

        - `reviews.rating` - the average star rating, stored as JSON with `value`, `scale_min` and `scale_max`
        - `reviews.rating_count` - the total number of reviews, stored as an integer

    ### How to enable storefront API access

    1. **Log in to your Shopify Admin.**

    2. **Go to `Settings` in the bottom left, then `Custom data`.**

    3. **Select `Products` from the list.**

    4. **Find the `reviews.rating` metafield definition.**

        !!! tip "If the definition is not in the list"

            Open the `More actions` menu and select `View unstructured metafields`.

    5. **Open the definition and turn on `Read` or `Storefronts` in the `Storefront access` section.** This sets the permission to `PUBLIC_READ`.

        ![Storefront API Access](/images/how_to_show_reviews_loox_storefrontapi.png){width="500"}

    6. **Click `Save`.**

    7. **Repeat for `reviews.rating_count`.**

    The ratings then appear on your quiz results page.

    !!! info "Give the cache a moment"

        Shopify's edge cache takes a few seconds to pick up the change. Clear your browser cache if the ratings do not appear straight away.

    ### Notes for each review app

    | Review app | What to know |
    |---|---|
    | Judge.me | Creates the `reviews.rating` and `reviews.rating_count` metafields on its own, once it has collected reviews. |
    | Loox | Writes its review data to the reserved `reviews` namespace. |
    | Yotpo | Uses the standard `reviews` namespace for ratings. |
    | Stamped | Uses the standard `reviews` namespace. |

    All four need Storefront API access before the ratings show. See [how to enable storefront API access](#how-to-enable-storefront-api-access).

    !!! warning "Loox may need a manual sync"

        Loox reviews and review counts sometimes stay missing after you enable Storefront API access. Email Loox support at [support@loox.io](mailto:support@loox.io) and ask them to sync your store to the default `reviews.rating` and `reviews.rating_count` metafields.

    ### Troubleshooting

    Work through these if the ratings still do not appear.

    1. **Check that the product has reviews.** Open it in your review app and confirm it collected some.

    2. **Check the metafield values.** In Shopify Admin, go to `Products`, select a product, then scroll to the `Metafields` section.

    3. **Run a catalog import.** Go to [App settings > Catalog](/reference/app-settings/#catalog) and run a quick [catalog import](/how-to-guides/sync-catalog/).

    4. **Wait for the cache.** Shopify's edge cache can take 5 to 30 seconds to update after a change.

    5. **Contact support.** See [how to contact customer support](/how-to-guides/contact-customer-support/), or ask your review app's support team.

=== "Shopify (Legacy)"

    1. **Go to [`Results Page settings > Basic settings`](/reference/quiz-builder/results-page/#basic-settings), then `Individual product settings`.**

        ![Individual Product Settings](/images/manual_quizbuilder_resultspage_settings_basic_individualproductsettings.png){width="500"}

    2. **Turn on `Show reviews`.** Product ratings then appear below the product name on the Results Page.

    3. **Run a [Catalog Sync](/how-to-guides/sync-catalog/).** This is what brings the reviews into the app.

    !!! info "Supported review apps"

        - Product Reviews by Shopify
        - Stamped Product Reviews and UGC
        - Judge.me Product Reviews
        - Rivyo Product Reviews

=== "WooCommerce"

    1. **Go to [`Results Page settings > Basic settings`](/reference/quiz-builder/results-page/#basic-settings), then `Individual product settings`.**

        ![Individual Product Settings](/images/manual_quizbuilder_resultspage_settings_basic_individualproductsettings.png){width="500"}

    2. **Turn on `Show reviews`.** Product ratings then appear below the product name on the Results Page.

    3. **Run a [Catalog Sync](/how-to-guides/sync-catalog/).** This is what brings the reviews into the app.

    !!! info "Supported review apps"

        Only the official WooCommerce Reviews are synced.

=== "Magento"

    !!! note "Not available on this platform"

        This version of the app cannot show product reviews on the Results Page.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version of the app cannot show product reviews on the Results Page.

=== "Standalone"

    !!! note "Not available on this platform"

        This version of the app cannot show product reviews on the Results Page.

---

This article explains how to show product reviews on the results page of your quiz.
