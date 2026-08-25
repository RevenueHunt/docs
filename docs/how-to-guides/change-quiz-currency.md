---
description: "Step-by-step guide to change your RevenueHunt quiz currency and set up multi-currency support with Shopify Markets."
icon: material/currency-usd
---

# How to Change Quiz Currency

This article explains how to change the currency of your quiz, and how to handle a multi-currency setup based on Shopify Markets.

## Change the quiz currency

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=ZRyxw2Tqaul1tzlj&amp;start=239" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The `💎Built for Shopify` version of the RevenueHunt app supports Shopify Markets. The quiz shows the default currency of the market it is assigned to.

    !!! tip "Tutorial"

        For a step-by-step walkthrough, see [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).

    !!! warning

        If you do not have Shopify Markets set up yet, follow the Shopify instructions for [Shopify Markets](https://help.shopify.com/en/manual/international/managing).

    To assign a quiz to a specific Shopify Market and show prices in the currency of that market, follow the instructions below.

    1. Open the [App settings](/reference/app-settings/).
    2. Open the [Shopify Markets](/reference/app-settings/#shopify-markets) tab.
        ![Shopify Markets tab in App settings](/images/manual_shopifyV2_appsettings_markets.png)
    3. Find a market and use the `dropdown list` to pick its default quiz.
        ![Choosing the default quiz for a market](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)
    4. Once assigned, the quiz will show the product prices in the currency set up for that market.
    5. To change the currency format, use the `Currency` field. Type `{{amount}} EUR` or `${{amount}}` to set how the price reads on the results page.
        ![Currency format field in the Shopify Markets tab](/images/manual_shopifyV2_appsettings_markets_showall.png)



=== "Shopify (Legacy)"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! tip

        If a currency is missing from the list, [contact support](/how-to-guides/contact-customer-support/).

=== "WooCommerce"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! tip

        If a currency is missing from the list, [contact support](/how-to-guides/contact-customer-support/).

=== "Magento"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! tip

        If a currency is missing from the list, [contact support](/how-to-guides/contact-customer-support/).

=== "BigCommerce"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! tip

        If a currency is missing from the list, [contact support](/how-to-guides/contact-customer-support/).

=== "Standalone"

    To change the quiz currency:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}
    3. Scroll down to the `Currency` field and click on the dropdown.
    4. Select your currency from the list.
    5. Update the preview/live quiz by clicking the `Publish` button in the top-right corner.

    !!! tip

        If a currency is missing from the list, [contact support](/how-to-guides/contact-customer-support/).

## Multi-currency quizzes

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=ZRyxw2Tqaul1tzlj&amp;start=239" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The `💎Built for Shopify` version of the RevenueHunt app supports Shopify Markets. The quiz shows the default currency of the market it is assigned to.

    !!! tip "Tutorial"

        For a step-by-step walkthrough, see [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).

    !!! warning

        If you do not have Shopify Markets set up yet, follow the Shopify instructions for [Shopify Markets](https://help.shopify.com/en/manual/international/managing).

    To assign a quiz to a specific Shopify Market and show prices in the currency of that market, follow the instructions below.

    To change the currency format:

    1. Go to the [App settings](/reference/app-settings/)
    2. Open the [Shopify Markets](/reference/app-settings/#shopify-markets) tab.
    3. Find the market you want to change, then click its `Currency` field. Type `{{amount}} EUR` or `${{amount}}` to set how the price reads on the results page.
        ![Currency format field in the Shopify Markets tab](/images/manual_shopifyV2_appsettings_markets_showall.png)
    4. Once assigned, the quiz will show the product prices in the currency set up for that market.

    !!! warning "Why the Compare-at Price May Not Show on the Results page"

        A **compare-at price** that is missing, or shows as `null` on the results page, usually comes from **Shopify Markets settings**. Shopify can hide compare-at prices for customers in some regions, in particular the **European Economic Area (EEA)**, because of local pricing or legal rules.

        To fix it:

        Go to **Shopify Admin → Settings → Markets → Preferences** and enable compare-at prices for that market, such as Germany or the EEA.

        ![Compare-at price preference in Shopify Markets](/images/how_to_shopifyv2_change_quiz_language_markets_compareatissue.png)

        To test it, preview the quiz on your live store while simulating a customer in the affected country.


=== "Shopify (Legacy)"

    The RevenueHunt app does not support multi-currency stores. It pulls your store’s **base currency** and uses the original prices set in your store. With a base currency of USD, only the US dollar prices are synced.

    There is a workaround for a multi-currency shop. Hide the price on the results page and set the checkout option to view the product. The customer then goes to the product page, where the right price applies.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`.
    6. Find `Show price` and click the toggle to turn it off.

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "WooCommerce"

    The RevenueHunt app does not support multi-currency stores. It pulls your store’s **base currency** and uses the original prices set in your store. With a base currency of USD, only the US dollar prices are synced.

    There is a workaround for a multi-currency shop. Hide the price on the results page and set the checkout option to view the product. The customer then goes to the product page, where the right price applies.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`.
    6. Find `Show price` and click the toggle to turn it off.

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "Magento"

    The RevenueHunt app does not support multi-currency stores. It pulls your store’s **base currency** and uses the original prices set in your store. With a base currency of USD, only the US dollar prices are synced.

    There is a workaround for a multi-currency shop. Hide the price on the results page and set the checkout option to view the product. The customer then goes to the product page, where the right price applies.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`.
    6. Find `Show price` and click the toggle to turn it off.

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "BigCommerce"

    The RevenueHunt app does not support multi-currency stores. It pulls your store’s **base currency** and uses the original prices set in your store. With a base currency of USD, only the US dollar prices are synced.

    There is a workaround for a multi-currency shop. Hide the price on the results page and set the checkout option to view the product. The customer then goes to the product page, where the right price applies.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`.
    6. Find `Show price` and click the toggle to turn it off.

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

=== "Standalone"

    The RevenueHunt app does not support multi-currency stores. It pulls your store’s **base currency** and uses the original prices set in your store. With a base currency of USD, only the US dollar prices are synced.

    There is a workaround for a multi-currency shop. Hide the price on the results page and set the checkout option to view the product. The customer then goes to the product page, where the right price applies.

    Follow these steps to apply this workaround:

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Navigate to the [Results Page](/reference/quiz-builder/results-page/).
    3. Open the [Results Page Settings](/reference/quiz-builder/results-page/).
    4. In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), check the `Checkout Settings` section. Select `Link to product`.
    5. Scroll down to `Individual Product Settings`.
    6. Find `Show price` and click the toggle to turn it off.

    Now, the product price will not be shown and the customer will be redirected to the product page from the results page.

---
This article explains how to change quiz currency and how to handle multi-currency setup based on Shopify Markets.

