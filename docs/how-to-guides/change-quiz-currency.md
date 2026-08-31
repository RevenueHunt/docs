---
description: "Step-by-step guide to change your RevenueHunt quiz currency and set up multi-currency support with Shopify Markets."
icon: material/currency-usd
---

# How to Change Quiz Currency

This article explains how to set the currency a quiz shows its prices in, and what to do when one store sells in several currencies.

## Change the quiz currency

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=ZRyxw2Tqaul1tzlj&amp;start=239" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This version follows Shopify Markets. A quiz assigned to a market shows the prices in that market's default currency.

    !!! warning "Set your markets up first"

        If you have no Shopify Markets yet, follow Shopify's own guide to [managing markets](https://help.shopify.com/en/manual/international/managing).

    1. **Open the [App settings](/reference/app-settings/).**

    2. **Open the [Shopify Markets](/reference/app-settings/#shopify-markets) tab.**

        ![Shopify Markets tab in App settings](/images/manual_shopifyV2_appsettings_markets.png)

    3. **Find the market and pick its default quiz from the dropdown.**

        ![Choosing the default quiz for a market](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

        The quiz then shows its prices in that market's currency.

    4. **Set how the price reads, in the `Currency` field.** Type `{{amount}} EUR` or `${{amount}}`, whichever suits the market.

        ![Currency format field in the Shopify Markets tab](/images/manual_shopifyV2_appsettings_markets_showall.png)

    !!! tip "A full walkthrough"

        [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/) covers markets, languages and currency together.

=== "Shopify (Legacy)"

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.**

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}

    3. **Scroll to the `Currency` field and open the dropdown.**

    4. **Select your currency.**

    5. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! tip "A currency missing from the list"

        [Contact support](/how-to-guides/contact-customer-support/) and ask for it to be added.

=== "WooCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.**

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}

    3. **Scroll to the `Currency` field and open the dropdown.**

    4. **Select your currency.**

    5. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! tip "A currency missing from the list"

        [Contact support](/how-to-guides/contact-customer-support/) and ask for it to be added.

=== "Magento"

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.**

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}

    3. **Scroll to the `Currency` field and open the dropdown.**

    4. **Select your currency.**

    5. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! tip "A currency missing from the list"

        [Contact support](/how-to-guides/contact-customer-support/) and ask for it to be added.

=== "BigCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.**

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}

    3. **Scroll to the `Currency` field and open the dropdown.**

    4. **Select your currency.**

    5. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! tip "A currency missing from the list"

        [Contact support](/how-to-guides/contact-customer-support/) and ask for it to be added.

=== "Standalone"

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [`Quiz Settings > General`](/reference/quiz-builder/quiz-settings/#general) tab.**

        ![Quiz Settings General tab](/images/manual_quizbuilder_quizsettings_general.png){width="300"}

    3. **Scroll to the `Currency` field and open the dropdown.**

    4. **Select your currency.**

    5. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! tip "A currency missing from the list"

        [Contact support](/how-to-guides/contact-customer-support/) and ask for it to be added.

## Show more than one currency

=== "Shopify"

    Shopify Markets is the multi-currency mechanism. Assign a quiz to each market, and every customer sees the prices of the market they are shopping in. See [Change the quiz currency](#change-the-quiz-currency) for the assignment steps.

    !!! warning "A compare-at price that does not show"

        A compare-at price that is missing, or reads as `null` on the results page, usually comes from the market settings rather than from the quiz. Shopify hides compare-at prices for customers in some regions, the European Economic Area in particular, because of local pricing rules.

        Go to `Shopify Admin > Settings > Markets > Preferences` and turn compare-at prices on for that market.

        ![Compare-at price preference in Shopify Markets](/images/how_to_shopifyv2_change_quiz_language_markets_compareatissue.png)

        To check the fix, preview the quiz on your live store while simulating a customer in that country.

=== "Shopify (Legacy)"

    This version does not support multi-currency stores. It reads your store's **base currency** and uses the prices set there. With a base currency of USD, only the US dollar prices are synced.

    There is a way around it. Hide the price on the Results Page, and send the customer to the product page instead, where your store shows the right price for them.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Results Page](/reference/quiz-builder/results-page/).**

    2. **Open the [Results Page Settings](/reference/quiz-builder/results-page/).**

    3. **In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), find `Checkout Settings` and select `Link to product`.** See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/#link-to-the-product-page).

    4. **Scroll to `Individual Product Settings` and turn `Show price` off.**

    5. **Click the top-right `Publish` button.**

    The results page then shows no price, and the customer reads the price on your product page.

=== "WooCommerce"

    This version does not support multi-currency stores. It reads your store's **base currency** and uses the prices set there. With a base currency of USD, only the US dollar prices are synced.

    There is a way around it. Hide the price on the Results Page, and send the customer to the product page instead, where your store shows the right price for them.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Results Page](/reference/quiz-builder/results-page/).**

    2. **Open the [Results Page Settings](/reference/quiz-builder/results-page/).**

    3. **In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), find `Checkout Settings` and select `Link to product`.** See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/#link-to-the-product-page).

    4. **Scroll to `Individual Product Settings` and turn `Show price` off.**

    5. **Click the top-right `Publish` button.**

    The results page then shows no price, and the customer reads the price on your product page.

=== "Magento"

    This version does not support multi-currency stores. It reads your store's **base currency** and uses the prices set there. With a base currency of USD, only the US dollar prices are synced.

    There is a way around it. Hide the price on the Results Page, and send the customer to the product page instead, where your store shows the right price for them.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Results Page](/reference/quiz-builder/results-page/).**

    2. **Open the [Results Page Settings](/reference/quiz-builder/results-page/).**

    3. **In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), find `Checkout Settings` and select `Link to product`.** See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/#link-to-the-product-page).

    4. **Scroll to `Individual Product Settings` and turn `Show price` off.**

    5. **Click the top-right `Publish` button.**

    The results page then shows no price, and the customer reads the price on your product page.

=== "BigCommerce"

    This version does not support multi-currency stores. It reads your store's **base currency** and uses the prices set there. With a base currency of USD, only the US dollar prices are synced.

    There is a way around it. Hide the price on the Results Page, and send the customer to the product page instead, where your store shows the right price for them.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Results Page](/reference/quiz-builder/results-page/).**

    2. **Open the [Results Page Settings](/reference/quiz-builder/results-page/).**

    3. **In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), find `Checkout Settings` and select `Link to product`.** See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/#link-to-the-product-page).

    4. **Scroll to `Individual Product Settings` and turn `Show price` off.**

    5. **Click the top-right `Publish` button.**

    The results page then shows no price, and the customer reads the price on your product page.

=== "Standalone"

    This version shows one currency, the one you picked in `Quiz Settings > General`. Prices come from the [Catalogue](https://admin.revenuehunt.com/catalogue) exactly as you entered them, so the app has nothing to convert them with.

    There is a way around it. Hide the price on the Results Page, and send the customer to the product page instead, where your store shows the right price for them.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Results Page](/reference/quiz-builder/results-page/).**

    2. **Open the [Results Page Settings](/reference/quiz-builder/results-page/).**

    3. **In [Basic Settings](/reference/quiz-builder/results-page/#basic-settings), find `Checkout Settings` and select `Link to product`.** See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/#link-to-the-product-page).

    4. **Scroll to `Individual Product Settings` and turn `Show price` off.**

    5. **Click the top-right `Publish` button.**

    The results page then shows no price, and the customer reads the price on your product page.

---

This article explains how to set the currency a quiz shows, and what to do when one store sells in several currencies.