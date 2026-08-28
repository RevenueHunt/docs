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

    1. In your Shopify Admin, go to `Markets`.
    2. Create separate markets for different regions, such as **European Union** and **United States**.
    3. To create a new market in Shopify, click on `Create Market` and enter the market name, regions and currency.
    4. Save your changes. The markets sync with the RevenueHunt app on their own.



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

        - 'Skincare Quiz (USA)' < default quiz >,
        - 'Skincare Quiz (Europe)',
        - 'Skincare Quiz (Spanish)',
        - 'Skincare Quiz (French)'.

    1. Open the RevenueHunt app.
    2. Click `Create new quiz` to make the first quiz. Start with creating a main/default quiz for your primary market (e.g., 'Skincare Quiz (USA)').

        !!! tip "Use Quiz Copilot"
            Use [Quiz Copilot](/how-to-guides/use-quiz-copilot/) to help build the first draft, add questions, and set up recommendations.

    3. Once the main quiz is ready, duplicate it from the `Dashboard > ... > Duplicate` to create copies for other markets.
    4. Make market-specific changes as needed to the copy quiz and rename it for easier identification (e.g., 'Skincare Quiz (Europe)').

    To create quizzes in other languages:

    5. Duplicate the quiz and manually translate questions and choices to another language.

        !!! tip "Use Quiz Copilot"
            You can ask [Quiz Copilot](/how-to-guides/use-quiz-copilot/) to create a translated copy.


        !!! warning
            RevenueHunt app does not offer an in-app automatic translation option but you can ask [Quiz Copilot](/how-to-guides/use-quiz-copilot/) to create a translated copy.

    6. In [`Quiz settings`](/reference/quiz-builder/quiz-settings/) go to [`Quiz content`](/reference/quiz-builder/quiz-settings/#messages-quiz-content) click `Reset messages` and change the language of system buttons and helpers as needed. You can also change the translations manually for each field.
    7. Remember to save the changes with the `Save` button.

    !!! info "Product titles and descriptions are translated automatically"

        You translate the quiz **questions, choices and interface text** yourself. The **product titles, descriptions and prices** on the results page come from Shopify in the customer's language and currency, through Shopify's Storefront API. Set up your product translations in the [Translate & Adapt](https://apps.shopify.com/translate-and-adapt) app, or a compatible one, and they appear in the quiz results.



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

    Once the quizzes for different markets and languages are created, you can assign them to be shown only to a specific market or language.

    1. To assign quizzes to specific markets, go to [`App settings`](/reference/app-settings/).
    2. Open the [`Shopify Markets`](/reference/app-settings/#shopify-markets) tab. It lists all your markets.
    3. Click on a dropdown next to each market name to set a default quiz for each market.

        !!! example

            - assign 'Skincare Quiz Europe' to the European market,
            - assign 'Skincare Quiz USA' to the United States market.

            ![sample market assignment](https://loom.com/i/952e7d4c5972482496d85350ca8cb927?workflows_screenshot=true)

    4. Save the changes with the `Save` button.


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

    1. To assign a quiz to a specific language within a market, go to [`App settings`](/reference/app-settings/).
    2. Open the [`Shopify Markets`](/reference/app-settings/#shopify-markets) tab. It lists all your markets.
    3. Click the `>` arrow on a market. It expands with a dropdown for the languages available in your Shopify store.

        !!! info
            The list of languages available in the RevenueHunt app is synced directly from your `Shopify Settings > Languages` and is managed in Shopify via the **Translate & Adapt** app.

    4. Click on a dropdown next to each language name to set a default quiz for each language.

        !!! example

            - assign 'Skincare Quiz Spanish' to the Spanish language in the European market,
            - assign 'Skincare Quiz French' to the French language in the European market,
            - assign 'Skincare Quiz Spanish' to the Spanish language in the United States market,
            - assign 'Skincare Quiz French' to the French language in the United States market.

            ![sample language assignment](https://loom.com/i/87363ed0a819460ea678d3918abfdc7b?workflows_screenshot=true)

    5. Save the changes with the `Save` button.


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
        If `USD` is your default currency format for US market, prices on the results page of the quiz will be displayed as `25 USD`.


    To change the format for a specific market:

    1. Open the [`Shopify Markets`](/reference/app-settings/#shopify-markets) tab. It lists all your markets.
    2. Click the `>` arrow on a market. It then expands to show a language dropdown and a `Currency` field.
    3. In the `Currency` field, enter your preferred format.

        !!! example

            - `${{amount}}` > This will display prices as $25.00 instead of 25 USD.
            - `€{{amount}}` > This will display prices as €25.00 instead of 25 EUR.

            ![sample currency format](https://loom.com/i/251334029cab4f409b2c6fc94a9d186a?workflows_screenshot=true)

    4. Save the changes with the `Save` button.


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

    Before testing, you need to ensure that your default quiz is published on the website. Otherwise, the RevenueHunt app will not be able to display any quizzes.

    To publish the default quiz:

    1. Go to the [`Publish`](/reference/quiz-builder/publish/) tab in the RevenueHunt app.
    2. Pick a publishing option and follow the instructions to add the quiz to your website.
    3. Once the default quiz is published, the app detects the market and language of the customer. It then shows the right quiz.


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

    Once the default quiz is published and markets set up, you can preview your store and test the setup on different markets and languages.

    1. In Shopify, go to `Online store` and click the `👁️` eye icon to preview the store. Your store will open in a new window.
    2. Click on a link that opens the quiz or navigate to the page where the quiz is published.
    3. Switch markets and languages to check that the right quiz loads. The US quiz should load for the United States, and the EU quiz for Belgium.
    4. Confirm that the correct quiz loads for each market and language.
    5. Check that prices are displayed in the correct format.

        !!! example "Example Test Scenarios"

            Market change: Switch to the United States → US quiz appears.

            Market change: Switch to Belgium → EU quiz appears.

            Language change: Change to French → French quiz appears.

            Language change: Change to Spanish → Spanish quiz appears.

            ![sample test](https://loom.com/i/6893314457ef4219a293e28708f91ba1?workflows_screenshot=true)

    You have set up quizzes for different markets and languages in the RevenueHunt app.


    !!! tip

        You can also preview a specific quiz results page within the `Preview` option in the app.

        1. Open the [Quiz builder](/reference/quiz-builder/).
        2. Click the `Preview` button in the top-right corner of the quiz builder and get all the way to the results page.
        3. From there you can preview the results page as a different market or language.

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