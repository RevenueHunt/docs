---
icon: material/currency-usd
---

# How to Change Quiz Currency

=== "Shopify"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "Shopify V2"

    Version 2 of the RevenueHunt App for Shopify fully supports the Shopify Markets feature. Your quiz will display the default currency from the market the quiz was assigned to. 
    
    To assign a market to the quiz follow the instructions below.
    
    1. Open the [App Settings](/reference/app-settings/).
    2. Open the [Shopify Markets](/reference/app-settings/#markets) tab.
        ![manual_shopifyV2_appsettings_markets](/images/manual_shopifyV2_appsettings_markets.png)
    3. Find a market and click the `dropdown list` to select the quiz that should be default for this market. 
        ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)
    4. Once assigned, the quiz will show the product prices in the currency set up for that market.

=== "WooCommerce"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "Magento"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "BigCommerce"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "Standalone"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

## Multi-currency quizzes

=== "Shopify"

    At the moment the RevenueHunt app doesn’t support multi-currency stores. We’re pulling your store’s **base currency**. Our app takes into account the original prices set up in your store. If your base currency is in USD dollars, then the US dollar prices will be the only ones synced with the app.

    If you run a multi-currency shop there's a workaround. What most customers do is show the product on the results page without the price and instead choose the checkout option to view the product. This way the customer is redirected to the product page from the result where the right price is applied.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`. 
    5. Search for `Show price` and click the toggle to deactivate it. 

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "Shopify V2"

    Version 2 of the RevenueHunt App for Shopify fully supports the Shopify Markets feature. Your quiz will display the default currency from the market the quiz was assigned to. 

    To assign a quiz to the market follow the instructions above.

    To change the currency format:

    1. Go to the [App Settings](/reference/app-settings/)
    2. Open the [Shopify Markets](/reference/app-settings/#markets) tab.
    3. Find the market you want to change the currency format for and click on the `Currency` field to set up the format you want.  Type `{{amount}} EUR` or `${{amount}}` to change the currency format as displayed on the results page.
        ![how_to_shopifyv2_change_currency](/images/how_to_shopifyv2_change_currency.png)
    4. Once assigned, the quiz will show the product prices in the currency set up for that market. 

=== "WooCommerce"

    At the moment the RevenueHunt app doesn’t support multi-currency stores. We’re pulling your store’s **base currency**. Our app takes into account the original prices set up in your store. If your base currency is in USD dollars, then the US dollar prices will be the only ones synced with the app.

    If you run a multi-currency shop there's a workaround. What most customers do is show the product on the results page without the price and instead choose the checkout option to view the product. This way the customer is redirected to the product page from the result where the right price is applied.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`. 
    5. Search for `Show price` and click the toggle to deactivate it. 

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "Magento"

    At the moment the RevenueHunt app doesn’t support multi-currency stores. We’re pulling your store’s **base currency**. Our app takes into account the original prices set up in your store. If your base currency is in USD dollars, then the US dollar prices will be the only ones synced with the app.

    If you run a multi-currency shop there's a workaround. What most customers do is show the product on the results page without the price and instead choose the checkout option to view the product. This way the customer is redirected to the product page from the result where the right price is applied.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`. 
    5. Search for `Show price` and click the toggle to deactivate it. 

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "BigCommerce"

    At the moment the RevenueHunt app doesn’t support multi-currency stores. We’re pulling your store’s **base currency**. Our app takes into account the original prices set up in your store. If your base currency is in USD dollars, then the US dollar prices will be the only ones synced with the app.

    If you run a multi-currency shop there's a workaround. What most customers do is show the product on the results page without the price and instead choose the checkout option to view the product. This way the customer is redirected to the product page from the result where the right price is applied.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`. 
    5. Search for `Show price` and click the toggle to deactivate it. 

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "Standalone"

    At the moment the RevenueHunt app doesn’t support multi-currency stores. We’re pulling your store’s **base currency**. Our app takes into account the original prices set up in your store. If your base currency is in USD dollars, then the US dollar prices will be the only ones synced with the app.

    If you run a multi-currency shop there's a workaround. What most customers do is show the product on the results page without the price and instead choose the checkout option to view the product. This way the customer is redirected to the product page from the result where the right price is applied.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`. 
    5. Search for `Show price` and click the toggle to deactivate it. 

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

---
This article explains how to change quiz currency and how to handle multi-currency setup.

