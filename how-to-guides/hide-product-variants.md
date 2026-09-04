---
description: "Learn how to hide product variants dropdown in your RevenueHunt quiz or recommend specific variants on results page."
icon: material/sort-variant-off
---

# How to Hide Product Variants

When a recommended product has variants, the results page shows a dropdown so the customer can pick one.

![Variants dropdown on the results page](/images/how_to_hide_product_variants_image1.png)

There are three ways to take it away, and they leave the customer with different things.

| Method | What the customer gets |
|---|---|
| [Remove the dropdown component](#remove-the-dropdown-from-the-product-card) | The main product, with no variant to pick |
| [Hide the dropdown with CSS](#hide-the-dropdown-with-custom-css) | The main product, with no variant to pick |
| [Recommend a variant instead](#recommend-a-specific-variant-instead) | One variant, picked by the quiz |

## Remove the dropdown from the product card

=== "Shopify"

    The product card is built from components you arrange yourself, and the dropdown is one of them. Removing it leaves the rest of the card alone.

    1. **Open your [results page](/reference/quiz-builder/results-page/) and click the `Products` block.**

    2. **Scroll the block settings to [`Slot item composition`](/reference/quiz-builder/results-page/#product-product-variants-collections).** It lists every component the product card shows.

        ![Slot item composition in the Products block settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

    3. **Hover over `Variants dropdown` and click its bin icon.**

    4. **Click the top-right `Save` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! note "The dropdown hides itself in two cases"

        It never appears when no product in that block has variants, or when the slots are stacked. See [Block types](/reference/quiz-builder/results-page/#product-product-variants-collections).

=== "Shopify (Legacy)"

    !!! note "Not part of this version"

        The product card has no component list here, so the dropdown cannot be removed from it.

        [Hide it with custom CSS](#hide-the-dropdown-with-custom-css) instead, or [recommend a specific variant](#recommend-a-specific-variant-instead) so there is nothing left to pick.

=== "WooCommerce"

    !!! note "Not part of this version"

        The product card has no component list here, so the dropdown cannot be removed from it.

        [Hide it with custom CSS](#hide-the-dropdown-with-custom-css) instead, or [recommend a specific variant](#recommend-a-specific-variant-instead) so there is nothing left to pick.

=== "Magento"

    !!! note "Not part of this version"

        The product card has no component list here, so the dropdown cannot be removed from it.

        [Hide it with custom CSS](#hide-the-dropdown-with-custom-css) instead, or [recommend a specific variant](#recommend-a-specific-variant-instead) so there is nothing left to pick.

=== "BigCommerce"

    !!! note "Not part of this version"

        The product card has no component list here, so the dropdown cannot be removed from it.

        [Hide it with custom CSS](#hide-the-dropdown-with-custom-css) instead, or [recommend a specific variant](#recommend-a-specific-variant-instead) so there is nothing left to pick.

=== "Standalone"

    !!! note "Not part of this version"

        The product card has no component list here, so the dropdown cannot be removed from it.

        [Hide it with custom CSS](#hide-the-dropdown-with-custom-css) instead, or [recommend a specific variant](#recommend-a-specific-variant-instead) so there is nothing left to pick.

## Hide the dropdown with custom CSS

=== "Shopify"

    A CSS rule hides the dropdown without touching the block. Removing the component is the tidier route, so try that first.

    1. **Open the [Quiz design](/reference/quiz-builder/quiz-design/) tab.**

    2. **Go to the [Advanced](/reference/quiz-builder/quiz-design/#edit-theme) section and find the CSS console.**

    3. **Paste this rule into the console.**

        ```css
        .select-variants-container {
            display: none;
        }
        ```

    4. **Click the top-right `Save` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! tip "The rest of the results page classes"

        See the [App CSS Structure reference](/reference/css-structure/).

=== "Shopify (Legacy)"

    A CSS rule hides the dropdown while the quiz carries on recommending the main product.

    1. **Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.**

    2. **Scroll to the `Custom CSS` section and click `add`.**

    3. **Paste both rules into the CSS console.**

        ```css
        .no-variants-dropdown {
            display: none;
        }

        .lq-variants-dropdown {
            display: none;
        }
        ```

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! tip "The rest of the results page classes"

        See the [App CSS Structure reference](/reference/css-structure/).

=== "WooCommerce"

    A CSS rule hides the dropdown while the quiz carries on recommending the main product.

    1. **Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.**

    2. **Scroll to the `Custom CSS` section and click `add`.**

    3. **Paste both rules into the CSS console.**

        ```css
        .no-variants-dropdown {
            display: none;
        }

        .lq-variants-dropdown {
            display: none;
        }
        ```

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! tip "The rest of the results page classes"

        See the [App CSS Structure reference](/reference/css-structure/).

=== "Magento"

    A CSS rule hides the dropdown while the quiz carries on recommending the main product.

    1. **Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.**

    2. **Scroll to the `Custom CSS` section and click `add`.**

    3. **Paste both rules into the CSS console.**

        ```css
        .no-variants-dropdown {
            display: none;
        }

        .lq-variants-dropdown {
            display: none;
        }
        ```

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! tip "The rest of the results page classes"

        See the [App CSS Structure reference](/reference/css-structure/).

=== "BigCommerce"

    A CSS rule hides the dropdown while the quiz carries on recommending the main product.

    1. **Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.**

    2. **Scroll to the `Custom CSS` section and click `add`.**

    3. **Paste both rules into the CSS console.**

        ```css
        .no-variants-dropdown {
            display: none;
        }

        .lq-variants-dropdown {
            display: none;
        }
        ```

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! tip "The rest of the results page classes"

        See the [App CSS Structure reference](/reference/css-structure/).

=== "Standalone"

    A CSS rule hides the dropdown while the quiz carries on recommending the main product.

    1. **Open the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.**

    2. **Scroll to the `Custom CSS` section and click `add`.**

    3. **Paste both rules into the CSS console.**

        ```css
        .no-variants-dropdown {
            display: none;
        }

        .lq-variants-dropdown {
            display: none;
        }
        ```

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check the dropdown is gone from the recommendations.**

        ![Results page with the variants dropdown hidden](/images/how_to_hide_product_variants_image3.png)

    !!! tip "The rest of the results page classes"

        See the [App CSS Structure reference](/reference/css-structure/).

## Recommend a specific variant instead

=== "Shopify"

    A `Product variants` block recommends variants in their own right. Each recommendation is then one variant, so the customer has nothing left to pick.

    1. **Open your [results page](/reference/quiz-builder/results-page/) and click `Add block`.**

        ![Block types on the results page](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes.png)

    2. **Under `Slots`, choose [`Product variants`](/reference/quiz-builder/results-page/#product-product-variants-collections).**

        ![Product variants block settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes_productvariants.png)

    3. **Open the block settings and set the `Recommendation system`.** Choose recommendations drawn from the answers, or a fixed set of variants.

    4. **Click the top-right `Save` button.**

    5. **Take the quiz and check that each recommendation is a single variant.**

        ![Results page recommending a single variant](/images/how_to_hide_product_variants_image2.png)

=== "Shopify (Legacy)"

    `Group product variants` collects the variants of a product into one dropdown. With it off, the quiz recommends each variant as an item of its own.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Group product variants` off.**

        ![Group product variants in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that each recommendation is a single variant.**

        ![Results page recommending a single variant](/images/how_to_hide_product_variants_image2.png)

    !!! note "How the variants are ordered"

        Variants appear in the order of the upvotes they collected. Variants on equal upvotes appear in a random order.

=== "WooCommerce"

    `Group product variants` collects the variants of a product into one dropdown. With it off, the quiz recommends each variant as an item of its own.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Group product variants` off.**

        ![Group product variants in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that each recommendation is a single variant.**

        ![Results page recommending a single variant](/images/how_to_hide_product_variants_image2.png)

    !!! note "How the variants are ordered"

        Variants appear in the order of the upvotes they collected. Variants on equal upvotes appear in a random order.

=== "Magento"

    `Group product variants` collects the variants of a product into one dropdown. With it off, the quiz recommends each variant as an item of its own.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Group product variants` off.**

        ![Group product variants in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that each recommendation is a single variant.**

        ![Results page recommending a single variant](/images/how_to_hide_product_variants_image2.png)

    !!! note "How the variants are ordered"

        Variants appear in the order of the upvotes they collected. Variants on equal upvotes appear in a random order.

=== "BigCommerce"

    `Group product variants` collects the variants of a product into one dropdown. With it off, the quiz recommends each variant as an item of its own.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Group product variants` off.**

        ![Group product variants in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that each recommendation is a single variant.**

        ![Results page recommending a single variant](/images/how_to_hide_product_variants_image2.png)

    !!! note "How the variants are ordered"

        Variants appear in the order of the upvotes they collected. Variants on equal upvotes appear in a random order.

=== "Standalone"

    `Group product variants` collects the variants of a product into one dropdown. With it off, the quiz recommends each variant as an item of its own.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Group product variants` off.**

        ![Group product variants in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that each recommendation is a single variant.**

        ![Results page recommending a single variant](/images/how_to_hide_product_variants_image2.png)

    !!! note "How the variants are ordered"

        Variants appear in the order of the upvotes they collected. Variants on equal upvotes appear in a random order.

---

This article explains the three ways to take the variants dropdown off your results page, and what each one leaves the customer with.