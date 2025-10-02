---
icon: material/star-box
---

# How to Show Product Reviews

This article explains how to show product reviews on the results page on your quiz.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/fe6c665726c74209a6c844fe29c03c8c?sid=b5c8e484-ceca-441f-a262-eb538f87e71f" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    This documentation outlines the steps to display product reviews on the results page of a quiz created with the Revenue Hunt app. It covers adding the reviews section, selecting a review app, and troubleshooting syncing issues.

    1. Open [Results Page](/reference/quiz-builder/results-page/).
    2. **Adding the Reviews Section**: Locate your [Product Block](/reference/quiz-builder/results-page/#products-products-variants-collections) that recommends products. 
    3. Under `Recommended Products`, find [`Product Component Layout`](/reference/quiz-builder/results-page/#product-components-layout). Click `+ Add Block` and select the `Reviews` section.

        ![Add Reviews Block](https://docs.revenuehunt.com/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_addblock.png){width="500"}

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

    5. You can move the reviews section to a different position within the product component layout, such as right below the product title. 
    6. Once satisfied with the layout, save your changes with the top-right `Save` button.
    7. **Previewing the Quiz**: To check if the reviews are displayed correctly, click on `Preview` to preview the quiz.
    8. **Troubleshooting Review Syncing**: If product reviews do not sync automatically, go to the app settings in the review app. Navigate to [`App Settings` > `Catalog`](/reference/app-settings/#catalogue) and perform a quick [catalog import](/how-to-guides/sync-catalog/). After the import, return to the Revenue Hunt app, check the results page, and preview the quiz again.

    !!! info

        If issues persist with reviews not being pulled, contact the support team for assistance.

    ## Review Apps

    ### Loox Reviews

    Loox metafields for reviews are set to private by default, but it can be changed in order to display the reviews in the quiz result page.

    You can make the Loox metafields (like `num_reviews` and `avg_rating` ) available in the Storefront
    API directly through the Shopify Admin interface using your browser. This involves **editing the metafield definitions in Shopify Admin to enable storefront access**, which sets the permission to `PUBLIC_READ`.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/1be62fe8d4a942db9393051bfc3bdd02?sid=24de0b08-81d8-4eb3-81fb-a159efb1bc93" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    Step-by-Step Guide:

    1. Log in to your Shopify Admin dashboard.
    2. Navigate to `Settings` (bottom left) > `Metafields and metaobjects`.
    3. Select the resource type for the metafields, such as `Products` (Loox typically uses product-level
    metafields).
    4. Locate the specific Loox metafield (e.g., search for `loox.avg_rating` or `loox.num_reviews` in the
    list). Loox reviews metafields can be located under `unstructured metafields`.
    5. Click on the metafield name to edit it.
    6. In the Access section, check the box for `Storefronts` (this enables public read access for custom
    storefronts and the Storefront API).

        ![Loox Storefront API](/images/how_to_show_reviews_loox_storefrontapi.png){width="500"}
    7. Optionally, adjust other settings like name, description, or validation if needed.
    8. Click `Save`.

    Once saved, the metafields should appear in the app.

    !!! warning

        If the metafields don't appear editable (rare, but possible for locked app setups), contact Loox support for assistance. 
        
        Changes take effect immediately, but you may need to clear any caches in your
        storefront app.


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
