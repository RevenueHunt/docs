---
icon: material/sort-variant-off
---

# How to Hide Product Variants 

Within Product Recommendation Quiz it is possible to hide the product variants dropdown on the results page.

![how to hide product variants image1](/images/how_to_hide_product_variants_image1.png)


## Option 1) Recommend a specific product variant instead

You can recommend a specific product variant instead of the main product by changing your Results Page settings. 

![how to hide product variants image2](/images/how_to_hide_product_variants_image2.png)

1. Open [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings) > [Advanced](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
2. Deactivate the `Group product variants` option. 
3. Remember to publish the changes with the top-right `Publish` button to update the preview/live quiz.


## Option 2) Hide the dropdown with custom CSS code


It is also possible to recommend only the main product and simply hide the dropdown with custom CSS code. To do that:

![how to hide product variants image3](/images/how_to_hide_product_variants_image3.png)

1. Open the [Quiz Design](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-design) tab.
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

 