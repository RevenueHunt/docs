---
description: "Learn how to hide product variants dropdown in your RevenueHunt quiz or recommend specific variants on results page."
icon: material/sort-variant-off
---

# How to Hide Product Variants

You can hide the product variants dropdown on the results page.

![Product variants dropdown on the results page](/images/how_to_hide_product_variants_image1.png)


## Recommend a specific product variant instead

=== "Shopify"

    You can recommend a specific product variant instead of the main product by changing your Product block on the Results page.

    1. Open [Results page](/reference/quiz-builder/results-page/).
    2. Click `+ Add block`.

        ![Block types on the Results page](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes.png)

    3. Find a [Product Variants Block](/reference/quiz-builder/results-page/#product-product-variants-collections) and open its settings.

        ![Product Variants Block settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes_productvariants.png)
    4. Save the changes with the top-right `Save` button.

    The quiz then recommends that variant rather than the main product.

    !!! info "If you use the Product block"

        You can hide the `Variants dropdown` by deleting the `Variants dropdown` option from the [Slot item composition](/reference/quiz-builder/results-page/#product-product-variants-collections) in the [Recommended Product settings](/reference/quiz-builder/results-page/#product-product-variants-collections).

        ![Slot item composition in the Recommended Product settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

=== "Shopify (Legacy)"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings.

    ![Results Page with a single variant recommended](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![Group product variants in Advanced settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option.
    3. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "WooCommerce"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings.

    ![Results Page with a single variant recommended](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![Group product variants in Advanced settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option.
    3. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "Magento"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings.

    ![Results Page with a single variant recommended](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![Group product variants in Advanced settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option.
    3. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "BigCommerce"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings.

    ![Results Page with a single variant recommended](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![Group product variants in Advanced settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option.
    3. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "Standalone"


    You can recommend a specific product variant instead of the main product by changing your Results Page settings.

    ![Results Page with a single variant recommended](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![Group product variants in Advanced settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option.
    3. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.


## Hide the dropdown with custom CSS code

=== "Shopify"

    You can also recommend the main product and hide the dropdown with custom CSS:

    ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz design](/reference/quiz-builder/quiz-design/) tab.
    2. Go to the [Advanced](/reference/quiz-builder/quiz-design/#edit-theme) section and find the CSS console.
    3. Add the following CSS code to the CSS console:

        ```css
        .select-variants-container {
        display: none;
        }
        ```
    4. Save the changes with the top-right `Save` button to update the preview and the live quiz.

=== "Shopify (Legacy)"


    You can also recommend the main product and hide the dropdown with custom CSS:

    ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```css
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "WooCommerce"

    You can also recommend the main product and hide the dropdown with custom CSS:

    ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```css
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "Magento"

    You can also recommend the main product and hide the dropdown with custom CSS:

    ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```css
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "BigCommerce"

    You can also recommend the main product and hide the dropdown with custom CSS:

    ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```css
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

=== "Standalone"

    You can also recommend the main product and hide the dropdown with custom CSS:

    ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```css
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Publish the changes with the top-right `Publish` button to update the preview and the live quiz.

---
By using this method you can hide the product variants from quiz recommendations.

 