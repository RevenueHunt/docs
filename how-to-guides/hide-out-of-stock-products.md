---
description: "Learn how to hide out-of-stock and draft products from your RevenueHunt quiz recommendations automatically."
icon: material/basket-off-outline
---

# How to Hide Out-Of-Stock or Draft Products from Recommendations

A quiz can recommend a product the customer cannot buy. Out-of-stock products and draft products are two separate cases, and this article covers both.

## Hide out-of-stock products

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/XX_TkB2waI4?si=8wvx1m28KyRQRdR3" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The app settings hold an inventory filter. Once it is on, a product below the stock level you set is left out of every quiz.

    1. **Go to [`App settings`](/reference/app-settings/) and select [`Catalog`](/reference/app-settings/#catalog) in the left menu.**

    2. **In the `Low inventory filter` section, check `Filter products by inventory level`.**

        ![Low inventory filter and Draft products in the Catalog tab](/images/manual_shopifyV2_appsettings_catalogue.png)

    3. **Set the `Minimum stock level`.** Any product below it is then left out of the recommendations. The level can be negative.

    4. **Save the change.**

    5. **Take the quiz and check that an out-of-stock product no longer appears.**

    !!! note "Products with several variants"

        A product is hidden only when every one of its variants is below the minimum stock level. One variant above it keeps the product in the recommendations.

    !!! tip "Showing sold-out products instead of hiding them"

        Leave `Filter products by inventory level` unchecked, which is how the app starts.

        An out-of-stock variant then still appears in the recommendations. Its `Add to cart` button reads `Sold out` and is disabled, so the customer cannot add it to the cart.

        Change that wording in [Quiz settings > Content](/reference/quiz-builder/quiz-settings/#messages-quiz-content) under `Buttons`.

=== "Shopify (Legacy)"

    One toggle in the results page settings decides whether the quiz can recommend a product that is out of stock.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Show unavailable products` off.**

        ![Show unavailable products in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that an out-of-stock product no longer appears.**

=== "WooCommerce"

    One toggle in the results page settings decides whether the quiz can recommend a product that is out of stock.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Show unavailable products` off.**

        ![Show unavailable products in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that an out-of-stock product no longer appears.**

=== "Magento"

    One toggle in the results page settings decides whether the quiz can recommend a product that is out of stock.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Show unavailable products` off.**

        ![Show unavailable products in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that an out-of-stock product no longer appears.**

=== "BigCommerce"

    One toggle in the results page settings decides whether the quiz can recommend a product that is out of stock.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Show unavailable products` off.**

        ![Show unavailable products in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that an out-of-stock product no longer appears.**

=== "Standalone"

    One toggle in the results page settings decides whether the quiz can recommend a product that is out of stock.

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab.**

    3. **Under `Recommendations Settings`, turn `Show unavailable products` off.**

        ![Show unavailable products in the Advanced tab](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}

    4. **Click the top-right `Publish` button.**

    5. **Take the quiz and check that an out-of-stock product no longer appears.**

## Hide draft products

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/XX_TkB2waI4?si=NeS6OBRV63_RLPeu&amp;start=64" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This version recommends draft products by default. The same catalog settings hold the checkbox that turns them off.

    1. **Go to [`App settings`](/reference/app-settings/) and select [`Catalog`](/reference/app-settings/#catalog) in the left menu.**

    2. **In the `Draft products` section, uncheck `Include draft products in recommendations`.**

        ![Low inventory filter and Draft products in the Catalog tab](/images/manual_shopifyV2_appsettings_catalogue.png)

    3. **Save the change.**

    4. **Take the quiz and check that a draft product no longer appears.**

    !!! tip "Leave the box checked while you build"

        With it checked, draft products appear in the `Quiz preview` and under [Responses > Analysis](/reference/quiz-builder/metrics/#response-analysis), so you can test the quiz before you publish them. They never reach the live quiz until they are published.

=== "Shopify (Legacy)"

    !!! note "There is nothing to set here"

        A draft product is never recommended in this version. The catalog import brings in active products only, and leaves draft and archived ones out, as [how to import your catalog](/how-to-guides/sync-catalog/) explains.

        `Show unavailable products` does not change this. That toggle covers out-of-stock products only, and turning it on brings back out-of-stock products, never draft or archived ones.

=== "WooCommerce"

    !!! note "There is nothing to set here"

        A draft product is never recommended in this version. The catalog import brings in active products only, and leaves draft and archived ones out, as [how to import your catalog](/how-to-guides/sync-catalog/) explains.

        `Show unavailable products` does not change this. That toggle covers out-of-stock products only, and turning it on brings back out-of-stock products, never draft or archived ones.

=== "Magento"

    !!! note "There is nothing to set here"

        A draft product is never recommended in this version. The catalog import brings in active products only, and leaves draft and archived ones out, as [how to import your catalog](/how-to-guides/sync-catalog/) explains.

        `Show unavailable products` does not change this. That toggle covers out-of-stock products only, and turning it on brings back out-of-stock products, never draft or archived ones.

=== "BigCommerce"

    !!! note "There is nothing to set here"

        A draft product is never recommended in this version. The catalog import brings in active products only, and leaves draft and archived ones out, as [how to import your catalog](/how-to-guides/sync-catalog/) explains.

        `Show unavailable products` does not change this. That toggle covers out-of-stock products only, and turning it on brings back out-of-stock products, never draft or archived ones.

=== "Standalone"

    !!! note "There is nothing to set here"

        A draft product is never recommended in this version. The catalog import brings in active products only, and leaves draft and archived ones out, as [how to import your catalog](/how-to-guides/sync-catalog/) explains.

        `Show unavailable products` does not change this. That toggle covers out-of-stock products only, and turning it on brings back out-of-stock products, never draft or archived ones.

---

This article explains how to keep out-of-stock and draft products out of your quiz recommendations.