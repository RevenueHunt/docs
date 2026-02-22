---
icon: material/star-box
---

# How to Show Product Reviews

This article explains how to show product reviews on the results page on your quiz.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/0nRTov-gCxY?si=33FdTH4HYZ7UDM04" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    This documentation outlines the steps to display product reviews on the results page of a quiz created with the Revenue Hunt app. It covers adding the reviews section, selecting a review app, and troubleshooting syncing issues.

    1. Open [Results Page](/reference/quiz-builder/results-page/).
    2. **Adding the Reviews Section**: Locate your [Product Block](/reference/quiz-builder/results-page/#products-products-variants-collections) that recommends products. 
    3. Under `Recommended Products`, find [`Product Component Layout`](/reference/quiz-builder/results-page/#product-components-layout). Click `+ Add Block` and select the `Reviews` section.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2.png)

    4. **Configuring the Reviews Section**: After adding the reviews section, a star rating box will appear at the bottom of your product card. Open the `Reviews` tab to select a review app from the dropdown menu.

        ![Add Reviews Block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_reviews.png)

        ![Add Reviews Block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_reviews_apps.png)

        !!! example 
            In this example, `Judge.me` is selected, but other review apps are available. 
            
            We currently support these review apps for Shopify:

            - Judge.me,
            - Yotpo,
            - Stamped,
            - Loox.

    5. **Enable Storefront API Access**: For reviews to display properly, you need to enable Storefront API access for the review metafields in your Shopify settings. Follow the detailed instructions in the [Enabling Storefront API Access](#enabling-storefront-api-access-for-review-apps) section below.
    6. You can move the reviews section to a different position within the product component layout, such as right below the product title. 
    7. Once satisfied with the layout, save your changes with the top-right `Save` button.
    8. **Previewing the Quiz**: To check if the reviews are displayed correctly, click on `Preview` to preview the quiz.
    9. **Troubleshooting Review Syncing**: If product reviews do not sync automatically, go to the app settings in the review app. Navigate to [`App Settings` > `Catalog`](/reference/app-settings/#catalogue) and perform a quick [catalog import](/how-to-guides/sync-catalog/). After the import, return to the Revenue Hunt app, check the results page, and preview the quiz again.

    !!! info

        If issues persist with reviews not being pulled, contact the support team for assistance.

    ## Enabling Storefront API Access for Review Apps

    All review apps store product ratings in Shopify metafields. For our app to display these reviews, the metafields must be **exposed to the Storefront API**. By default, most review apps set their metafields to private.

    !!! info "Which metafields are used?"

        All supported review apps use Shopify's reserved `reviews` namespace:

        - `reviews.rating` - The average star rating (stored as JSON with `value`, `scale_min`, `scale_max`)
        - `reviews.rating_count` - The total number of reviews (stored as an integer)

    ### How to Enable Storefront API Access

    Follow these steps to make review metafields accessible:

    1. Log in to your **Shopify Admin** dashboard.
    2. Navigate to **Settings** (bottom left) > **Custom data**.
    3. Select **Products** from the list.
    4. Look for the `reviews.rating` and `reviews.rating_count` metafield definitions.
        - If they don't appear in the main list, check under **View unstructured metafields** (click "More actions" menu).
    5. Click on each metafield to edit it.
    6. In the **Storefront access** section, enable the checkbox for **"Read"** or **"Storefronts"** (this sets the permission to `PUBLIC_READ`).

        ![Storefront API Access](/images/how_to_show_reviews_loox_storefrontapi.png){width="500"}

    7. Click **Save**.
    8. Repeat for both `reviews.rating` and `reviews.rating_count`.

    Once saved, the reviews should appear in your quiz results page.

    !!! tip "Changes take effect immediately"

        After saving, you may need to clear your browser cache or wait a few seconds for Shopify's edge cache to update.

    ### Review App-Specific Notes

    #### Judge.me

    Judge.me automatically creates the `reviews.rating` and `reviews.rating_count` metafields when reviews are collected. Follow the steps above to enable Storefront API access.

    #### Loox

    Loox writes review data to Shopify's reserved `reviews` namespace. Follow the steps above to enable Storefront API access.

    #### Yotpo

    Yotpo uses the standard `reviews` namespace for ratings. Follow the steps above to enable Storefront API access.

    #### Stamped

    Stamped uses the standard `reviews` namespace. Follow the steps above to enable Storefront API access.

    ### Troubleshooting

    If reviews still don't appear after enabling Storefront API access:

    1. **Verify the product has reviews**: Check the product in your review app to confirm it has collected reviews.
    2. **Check metafield values**: In Shopify Admin, go to **Products** > select a product > scroll to **Metafields** section to verify the review data exists.
    3. **Run a catalog sync**: Go to [App Settings > Catalog](/reference/app-settings/#catalogue) and perform a quick [catalog import](/how-to-guides/sync-catalog/).
    4. **Wait for cache**: Shopify's edge cache can take 5-30 seconds to update after changes.
    5. **Contact support**: If issues persist, contact our support team or your review app's support for assistance.


=== "Shopify (Legacy)"

    This section covers how to enable product reviews for the legacy Shopify interface.

    1. Navigate to [`Results Page settings > Basic settings`](/reference/quiz-builder/results-page/#basic-settings) > `Individual product settings`.
        
        ![Individual Product Settings](https://docs.revenuehunt.com/images/manual_quizbuilder_resultspage_settings_basic_individualproductsettings.png){width="500"}

    2. **Toggle the `Show reviews` option** to display product ratings below the product name on the results page.
    3. **Run a [Catalog Sync](/how-to-guides/sync-catalog/)** after activation to sync all product reviews with the app.

    !!! info "Supported Review Apps"
        We currently support these review apps for Shopify:
        
        - Product Reviews by Shopify
        - Stamped Product Reviews & UGC  
        - Judge.me Product Reviews
        - Rivyo Product Reviews



=== "WooCommerce"

    This section covers how to enable product reviews for WooCommerce stores.

    1. Navigate to [`Results Page settings > Basic settings`](/reference/quiz-builder/results-page/#basic-settings) > `Individual product settings`.
        
        ![Individual Product Settings](https://docs.revenuehunt.com/images/manual_quizbuilder_resultspage_settings_basic_individualproductsettings.png){width="500"}

    2. **Toggle the `Show reviews` option** to display product ratings below the product name on the results page.
    3. **Run a [Catalog Sync](/how-to-guides/sync-catalog/)** after activation to sync all product reviews with the app.

    !!! info "Review Support"
        We currently sync only the official WooCommerce Reviews.

=== "Magento"

    Currently, there is no option to show reviews on the results page in the Revenue Hunt app for Magento.

=== "BigCommerce"

    Currently, there is no option to show reviews on the results page in the Revenue Hunt app for BigCommerce.

=== "Standalone"

    Currently, there is no option to show reviews on the results page in the standalone version of the Revenue Hunt app.


---
This article explains how to show product reviews on the results page on your quiz.
