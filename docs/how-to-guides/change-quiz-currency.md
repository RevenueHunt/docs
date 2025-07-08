---
icon: material/currency-usd
---

# How to Change Quiz Currency

This guide explains how to change the currency of your quiz and how to handle multi-currency setups based on Shopify Markets.

## Change the quiz currency

=== "Shopify"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.

        ![manual_shopify_quizbuilder_quizsettings_general](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/d460aea970c04b9ea6388b37329eccea?sid=d2137eb0-344a-4930-a905-2d9388743629" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Version 2 of the RevenueHunt App for Shopify fully supports the Shopify Markets feature. Your quiz will display the default currency from the market the quiz was assigned to. 

    !!! warning

        If you don't have Shopify Markets set up yet, you can create them by following the instructions for [Shopify Markets](https://help.shopify.com/en/manual/international/managing).
    
    To assign a quiz to a specific Shopify Market and show prices in the currency of that market, follow the instructions below.
    
    1. Open the [App Settings](/reference/app-settings/).
    2. Open the [Shopify Markets](/reference/app-settings/#markets) tab.
        ![manual_shopifyV2_appsettings_markets](/images/manual_shopifyV2_appsettings_markets.png)
    3. Find a market and click the `dropdown list` to select the quiz that should be default for this market. 
        ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)
    4. Once assigned, the quiz will show the product prices in the currency set up for that market.
    5. If you want to change the currency format, use the `Currency` field to set up the format you want. Type `{{amount}} EUR` or `${{amount}}` to change the currency format as displayed on the results page.
        ![how_to_shopifyv2_change_currency](/images/how_to_shopifyv2_change_currency.png)   


=== "WooCommerce"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    
        ![manual_shopify_quizbuilder_quizsettings_general](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "Magento"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    
        ![manual_shopify_quizbuilder_quizsettings_general](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "BigCommerce"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    
        ![manual_shopify_quizbuilder_quizsettings_general](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! info

        If you're missing a currency from the list, please [contact support](/how-to-guides/contact-customer-support/).

=== "Standalone"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.
    
        ![manual_shopify_quizbuilder_quizsettings_general](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
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

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/d460aea970c04b9ea6388b37329eccea?sid=d2137eb0-344a-4930-a905-2d9388743629" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Version 2 of the RevenueHunt App for Shopify fully supports the Shopify Markets feature. Your quiz will display the default currency from the market the quiz was assigned to. 

    !!! warning

        If you don't have Shopify Markets set up yet, you can create them by following the instructions for [Shopify Markets](https://help.shopify.com/en/manual/international/managing).
    
    To assign a quiz to a specific Shopify Market and show prices in the currency of that market, follow the instructions below.

    To change the currency format:

    1. Go to the [App Settings](/reference/app-settings/)
    2. Open the [Shopify Markets](/reference/app-settings/#markets) tab.
    3. Find the market you want to change the currency format for and click on the `Currency` field to set up the format you want.  Type `{{amount}} EUR` or `${{amount}}` to change the currency format as displayed on the results page.
        ![how_to_shopifyv2_change_currency](/images/how_to_shopifyv2_change_currency.png)
    4. Once assigned, the quiz will show the product prices in the currency set up for that market. 

    !!! warning "Why the Compare-at Price May Not Show on the Results Page"

        If the **compare-at price** is missing or showing as `null` on the quiz results page, this is often due to **Shopify Markets settings**. By default, Shopify can hide compare-at prices for customers in certain regions—especially in the **European Economic Area (EEA)**—due to local pricing or legal restrictions.

        How to Fix It:

        Go to **Shopify Admin → Settings → Markets → Preferences** and ensure that compare-at prices are enabled for the relevant market (e.g., Germany or the EEA). 

        ![how_to_shopifyv2_change_quiz_languge_markets_compareatissue](/images/how_to_shopifyv2_change_quiz_languge_markets_compareatissue.png)
        
        You can test this by previewing the quiz on your live store while simulating a visitor from the affected country.

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
This article explains how to change quiz currency and how to handle multi-currency setup based on Shopify Markets.

