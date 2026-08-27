---
description: "Learn how to hide out-of-stock and draft products from your RevenueHunt quiz recommendations automatically."
icon: material/basket-off-outline
---

# How to Hide Out-Of-Stock or Draft Products from Recommendations

This article explains how to keep out-of-stock and draft products out of your quiz recommendations.

## Hide Out-of-stock products

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/XX_TkB2waI4?si=8wvx1m28KyRQRdR3" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Exclude out-of-stock items from your recommendations in **App settings** under the **Catalog** tab.

    1. Go to [`App settings`](/reference/app-settings/) and select [`Catalog`](/reference/app-settings/#catalog) from the left menu.
    2. In the `Inventory filter` section, check the box labeled `Filter products by inventory level` and set the `Minimum stock level` (can be negative).

        ![Catalog tab in App settings](/images/manual_shopifyV2_appsettings_catalogue.png)
    3. Any product below that stock level, including an out-of-stock one, is then left out of the recommendations.
    4. Save the changes.

    !!! note "Products with multiple variants"

        A product is hidden only when **all** of its variants are below the minimum stock level. One variant above it keeps the product in the recommendations.

    !!! tip "Displaying sold out products instead of hiding them"

        To show out-of-stock products with a "Sold out" label instead of hiding them, leave the inventory filter unchecked.

        **Default behavior for out-of-stock products:**

        - When a product variant is out of stock, the "Add to cart" button reads "Sold out" and is disabled.
        - A customer cannot add an out-of-stock variant to their cart.
        - Change the sold out text in [Quiz settings > Content](/reference/quiz-builder/quiz-settings/#messages-quiz-content) under **Buttons**.
        - To hide sold out products instead, enable the inventory filter in [App settings > Catalog > Low inventory filter](/reference/app-settings/#catalog).

=== "Shopify (Legacy)"

    You can exclude all out-of-stock items from your recommendations in the [Results Page settings](/reference/quiz-builder/results-page/).

    1. Open the [Results Page](/reference/quiz-builder/results-page/) and click the cog icon to open the [Results Page Settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings) tab.
    3. Under `Recommendation Settings` scroll to the `Show Unavailable products` field.
    4. Toggle it off, so unavailable and out-of-stock products are not recommended.

        ![Show unavailable products in Advanced Settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    5. Click the top-right `Publish` button to update the preview and the live quiz.

=== "WooCommerce"

    You can exclude all out-of-stock items from your recommendations in the [Results Page settings](/reference/quiz-builder/results-page/).

    1. Open the [Results Page](/reference/quiz-builder/results-page/) and click the cog icon to open the [Results Page Settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings) tab.
    3. Under `Recommendation Settings` scroll to the `Show Unavailable products` field.
    4. Toggle it off, so unavailable and out-of-stock products are not recommended.

        ![Show unavailable products in Advanced Settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    5. Click the top-right `Publish` button to update the preview and the live quiz.

=== "Magento"

    You can exclude all out-of-stock items from your recommendations in the [Results Page settings](/reference/quiz-builder/results-page/).

    1. Open the [Results Page](/reference/quiz-builder/results-page/) and click the cog icon to open the [Results Page Settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings) tab.
    3. Under `Recommendation Settings` scroll to the `Show Unavailable products` field.
    4. Toggle it off, so unavailable and out-of-stock products are not recommended.

        ![Show unavailable products in Advanced Settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    5. Click the top-right `Publish` button to update the preview and the live quiz.

=== "BigCommerce"

    You can exclude all out-of-stock items from your recommendations in the [Results Page settings](/reference/quiz-builder/results-page/).

    1. Open the [Results Page](/reference/quiz-builder/results-page/) and click the cog icon to open the [Results Page Settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings) tab.
    3. Under `Recommendation Settings` scroll to the `Show Unavailable products` field.
    4. Toggle it off, so unavailable and out-of-stock products are not recommended.

        ![Show unavailable products in Advanced Settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    5. Click the top-right `Publish` button to update the preview and the live quiz.

=== "Standalone"

    You can exclude all out-of-stock items from your recommendations in the [Results Page settings](/reference/quiz-builder/results-page/).

    1. Open the [Results Page](/reference/quiz-builder/results-page/) and click the cog icon to open the [Results Page Settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings) tab.
    3. Under `Recommendation Settings` scroll to the `Show Unavailable products` field.
    4. Toggle it off, so unavailable and out-of-stock products are not recommended.

        ![Show unavailable products in Advanced Settings](/images/manual_quizbuilder_resultspage_settings_advanced.png){width=50%}
    5. Click the top-right `Publish` button to update the preview and the live quiz.


## Hide draft products

=== "Shopify"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/XX_TkB2waI4?si=NeS6OBRV63_RLPeu&amp;start=64" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Exclude draft items from your recommendations in **App settings** under the **Catalog** tab.

    1. Go to [`App settings`](/reference/app-settings/) and select [`Catalog`](/reference/app-settings/#catalog) from the left menu.
    2. In the `Draft products` section, uncheck the box labeled `Include draft products in recommendations`.

        ![Catalog tab in App settings](/images/manual_shopifyV2_appsettings_catalogue.png)
    3. Draft products are then left out of the recommendations.
    4. Save the changes with the top-right `Save` button.


=== "Shopify (Legacy)"

    !!! note "Platform Availability"

        There is no setting for this, because a draft product is never recommended. Only products marked as **active** are synced, and draft or archived products are left out, as [How to Import Your Catalog](/how-to-guides/sync-catalog/) explains.

        This does not depend on `Show unavailable products`. That setting covers out-of-stock products only. Turning it on brings back out-of-stock products, never draft or archived ones.

=== "WooCommerce"

    !!! note "Platform Availability"

        There is no setting for this, because a draft product is never recommended. Only products marked as **active** are synced, and draft or archived products are left out, as [How to Import Your Catalog](/how-to-guides/sync-catalog/) explains.

        This does not depend on `Show unavailable products`. That setting covers out-of-stock products only. Turning it on brings back out-of-stock products, never draft or archived ones.

=== "Magento"

    !!! note "Platform Availability"

        There is no setting for this, because a draft product is never recommended. Only products marked as **active** are synced, and draft or archived products are left out, as [How to Import Your Catalog](/how-to-guides/sync-catalog/) explains.

        This does not depend on `Show unavailable products`. That setting covers out-of-stock products only. Turning it on brings back out-of-stock products, never draft or archived ones.

=== "BigCommerce"

    !!! note "Platform Availability"

        There is no setting for this, because a draft product is never recommended. Only products marked as **active** are synced, and draft or archived products are left out, as [How to Import Your Catalog](/how-to-guides/sync-catalog/) explains.

        This does not depend on `Show unavailable products`. That setting covers out-of-stock products only. Turning it on brings back out-of-stock products, never draft or archived ones.

=== "Standalone"

    !!! note "Platform Availability"

        There is no setting for this, because a draft product is never recommended. Only products marked as **active** are synced, and draft or archived products are left out, as [How to Import Your Catalog](/how-to-guides/sync-catalog/) explains.

        This does not depend on `Show unavailable products`. That setting covers out-of-stock products only. Turning it on brings back out-of-stock products, never draft or archived ones.



---
By following this guide you can disable showing out-of-stock or draft products on your results page.
