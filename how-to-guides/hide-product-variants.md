---
icon: material/sort-variant-off
---

# How to Hide Product Variants 

Within Product Recommendation Quiz it is possible to hide the product variants dropdown on the results page.

![how to hide product variants image1](/images/how_to_hide_product_variants_image1.png)


## Option 1) Recommend a specific product variant instead

=== "Shopify"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings. 

    ![how to hide product variants image2](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![how to hide product variants image2](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option. 
    3. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    You can recommend a specific product variant instead of the main product by changing your Product Block settings on the Results Page.

    1. Open [Results Page](/reference/quiz-builder/results-page/).
    2. Find a [Product Block](/reference/quiz-builder/results-page/#products-products-variants-collections) and open its settings.
    3. Under `Recommendations Type` select `Product Varaints`. 

        ![how to hide product variants image2](/images/how_to_shopifyv2_hide_product_variants_recommend_variants.png)
    4. Save the changes.

    From that point on, the quiz will recommend a specific product variant instead of the main product.

=== "WooCommerce"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings. 

    ![how to hide product variants image2](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![how to hide product variants image2](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option. 
    3. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings. 

    ![how to hide product variants image2](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![how to hide product variants image2](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option. 
    3. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    You can recommend a specific product variant instead of the main product by changing your Results Page settings. 

    ![how to hide product variants image2](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![how to hide product variants image2](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option. 
    3. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"


    You can recommend a specific product variant instead of the main product by changing your Results Page settings. 

    ![how to hide product variants image2](/images/how_to_hide_product_variants_image2.png)

    1. Open [Results Page settings](/reference/quiz-builder/results-page/) > [Advanced](/reference/quiz-builder/results-page/#advanced-settings).

        ![how to hide product variants image2](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    2. Deactivate the `Group product variants` option. 
    3. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

## Option 2) Hide the dropdown with custom CSS code

=== "Shopify"


    It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

    ![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```html
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

    ![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Go to the `Advanced` section and find the CSS console.
    3. Paste the following code into the CSS console:

        ```html
        .select-variants-container {
        display: none;
        }
        ```

    4. Remember to save the changes with the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

    ![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```html
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

    ![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```html
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

    ![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```html
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

    ![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

    1. Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
    2. Scroll to the `Custom CSS` section and click `add`.
    3. Paste the following code into the CSS console:

        ```html
        .no-variants-dropdown {
        display: none;
        }

        .lq-variants-dropdown {
        display: none;
        }
        ```

    4. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.

---
By using this method you can hide the product variants from quiz recommendations.

 