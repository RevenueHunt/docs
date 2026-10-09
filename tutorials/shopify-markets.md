---
icon: material/numeric-8
description: "Assign RevenueHunt quizzes to Shopify Markets, customize by language and currency for global storefronts."
---


# Assign Quizzes to Shopify Markets and Languages

=== "Shopify"

    In this tutorial you will learn how to show a different quiz for each Shopify market. It also covers showing a quiz in a different language or currency, based on your market settings.

    !!! info "What you will learn"

        - how to create Shopify Markets,
        - how to duplicate quizzes,
        - how to create quizzes in different languages,
        - how to translate quizzes to different languages with the help of Quiz Copilot,
        - how to display different quizzes for different Shopify markets,
        - how to show quizzes in different languages based on market and language,
        - how to change currency formats in quizzes for different markets,
        - how to test the quiz for different markets in Shopify.

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=lpLnZ1WuwaJDvZzp" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



=== "Shopify (Legacy)"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Intro

=== "Shopify"

    This tutorial covers setting up quizzes in the RevenueHunt app for different Shopify markets, with their language and currency settings. It shows how to create, duplicate and assign quizzes, so that a customer sees the content that matches their market and language.


=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Set up Shopify Markets

=== "Shopify"

    Before assigning quizzes, make sure your Shopify Markets are set up:

    1. **In your Shopify Admin, go to `Markets`.**
    2. **Click `Create Market` and enter the market name, its regions and its currency.**
    3. **Repeat for every region you sell to,** such as the European Union and the United States.
    4. **Save your changes.** The markets sync with the RevenueHunt app on their own.



=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.


## Create multiple quizzes

=== "Shopify"

    Create a quiz for each market or language.

    !!! example

        - `Skincare Quiz (USA)`, the default quiz
        - `Skincare Quiz (Europe)`
        - `Skincare Quiz (Spanish)`
        - `Skincare Quiz (French)`

    1. **Open the RevenueHunt app and click `Create new quiz`.** Build the main quiz for your primary market first, such as `Skincare Quiz (USA)`.

        !!! tip "Use Quiz Copilot"
            Use [Quiz Copilot](/how-to-guides/use-quiz-copilot/) to help build the first draft, add questions, and set up recommendations.

    2. **Once the main quiz is ready, open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Duplicate`.**
    3. **Rename the copy after its market and make any market-specific changes,** such as `Skincare Quiz (Europe)`.

    Then, for each extra language:

    1. **Duplicate the quiz again and translate the questions and choices by hand.**

        !!! warning "There is no automatic translation"

            The app cannot translate a quiz for you. You can, however, ask [Quiz Copilot](/how-to-guides/use-quiz-copilot/) to create a translated copy.

    2. **Go to [`Quiz settings > Quiz content`](/reference/quiz-builder/quiz-settings/#messages-quiz-content) and click `Reset messages`.** This pulls in the system buttons and helper text for the new language.
    3. **Change any remaining field by hand, then click `Save`.**

    !!! info "Product titles and descriptions are translated automatically"

        You translate the quiz questions, choices and interface text yourself. The product titles, descriptions and prices on the results page come from Shopify in the customer's language and currency, through Shopify's Storefront API. Set up your product translations in the [Translate & Adapt](https://apps.shopify.com/translate-and-adapt) app, or a compatible one, and they appear in the quiz results.



=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Assign quizzes to markets

=== "Shopify"

    Once the quizzes are built, you can assign each one to a market or to a language.

    1. **Go to [`App settings`](/reference/app-settings/).**
    2. **Open the [`Shopify Markets`](/reference/app-settings/#shopify-markets) tab.** It lists all your markets.
    3. **Click the dropdown next to a market name and pick that market's default quiz.**

        !!! example

            - assign `Skincare Quiz Europe` to the European market,
            - assign `Skincare Quiz USA` to the United States market.

            ![sample market assignment](https://loom.com/i/952e7d4c5972482496d85350ca8cb927?workflows_screenshot=true)

    4. **Save the changes with the `Save` button.**


=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Assign quizzes by language

=== "Shopify"

    You can also assign a quiz to a specific language within a market.

    1. **Go to [`App settings`](/reference/app-settings/).**
    2. **Open the [`Shopify Markets`](/reference/app-settings/#shopify-markets) tab.** It lists all your markets.
    3. **Click the `>` arrow on a market.** It expands to show the languages available in your Shopify store.

        !!! info
            The list of languages available in the RevenueHunt app is synced directly from your `Shopify Settings > Languages` and is managed in Shopify with the `Translate & Adapt` app.

    4. **Click the dropdown next to a language name and pick that language's default quiz.**

        !!! example

            - assign `Skincare Quiz Spanish` to the Spanish language in the European market,
            - assign `Skincare Quiz French` to the French language in the European market,
            - assign `Skincare Quiz Spanish` to the Spanish language in the United States market,
            - assign `Skincare Quiz French` to the French language in the United States market.

            ![sample language assignment](https://loom.com/i/87363ed0a819460ea678d3918abfdc7b?workflows_screenshot=true)

    5. **Save the changes with the `Save` button.**


=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Change currency format for markets

=== "Shopify"

    By default, quiz result prices follow the currency format in your Shopify Markets settings.

    !!! example
        If `USD` is the default currency format for your US market, the results page shows prices as `25 USD`.


    To change the format for a specific market:

    1. **Go to [`App settings`](/reference/app-settings/) and open the [`Shopify Markets`](/reference/app-settings/#shopify-markets) tab.**
    2. **Click the `>` arrow on a market.** It expands to show a language dropdown and a `Currency` field.
    3. **In the `Currency` field, enter the format you want.**

        !!! example

            - `${{amount}}` shows prices as $25.00 rather than 25 USD.
            - `€{{amount}}` shows prices as €25.00 rather than 25 EUR.

            ![sample currency format](https://loom.com/i/251334029cab4f409b2c6fc94a9d186a?workflows_screenshot=true)

    4. **Save the changes with the `Save` button.**


=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Publish the main quiz

=== "Shopify"

    Your default quiz has to be published on the website before you can test any of this. Until it is, the app has no quiz to show.

    To publish the default quiz:

    1. **Go to the [`Publish`](/reference/quiz-builder/share-publish/) tab in the RevenueHunt app.**
    2. **Pick a publishing option and follow the instructions to add the quiz to your website.**

    From then on the app reads the market and language of each customer, and shows the quiz you assigned to them.


=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.

## Test the setup

=== "Shopify"

    With the default quiz published and the markets set up, preview your store and test each market and language.

    1. **In Shopify, go to `Online store` and click the `👁️` eye icon.** Your store opens in a new window.
    2. **Open the page the quiz is published on.**
    3. **Switch market and language, and check that the right quiz loads each time.**
    4. **Check that the prices use the format you set.**

        !!! example "What to try"

            Market change: Switch to the United States → US quiz appears.

            Market change: Switch to Belgium → EU quiz appears.

            Language change: Change to French → French quiz appears.

            Language change: Change to Spanish → Spanish quiz appears.

            ![sample test](https://loom.com/i/6893314457ef4219a293e28708f91ba1?workflows_screenshot=true)

    You have set up quizzes for different markets and languages in the RevenueHunt app.


    !!! tip

        You can also preview a specific quiz results page within the `Preview` option in the app.

        1. **Open the [Quiz builder](/reference/quiz-builder/).**
        2. **Click the top-right `Preview` button and work through the quiz to the results page.**
        3. **From there, preview the results page as a different market or language.**

        ![how to test quiz results page](/images/tutorial_shopifyv2_preview_quiz_as_market.png)


=== "Shopify (Legacy)"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "WooCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for WooCommerce stores.

=== "Magento"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for Magento stores.

=== "BigCommerce"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for BigCommerce stores.

=== "Standalone"

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is not available for standalone installations.




---
This tutorial explains how to show a different quiz for each Shopify market, and how to show a quiz in a different language or currency.