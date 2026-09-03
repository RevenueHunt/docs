---
icon: material/earth
description: "Learn how to show different RevenueHunt quizzes based on Shopify markets and languages."
---

# How to Show a Quiz Based on Shopify Markets

=== "Shopify"

    Show a different quiz to customers in different markets and languages. You build one quiz per language, then tell the app which quiz belongs to which Shopify market.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=qKfPEBhJ2RvMlgBz" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "A worked walkthrough"

        [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/) covers the same ground as a tutorial, step by step.

    1. **Enable and configure [Shopify Markets](https://help.shopify.com/en/manual/international/managing) in your Shopify store.** A quiz can only follow a market that exists there already.

        !!! example "Markets you might set up"

            - Europe, with the `EUR` currency
            - The United States, with the `USD` currency
            - A Spanish market, with the `ES` language
            - A French market, with the `FR` language

    2. **Create your quiz in the [Quiz builder](/reference/quiz-builder/).**

    3. **Duplicate it from the dashboard, once for each extra language.**

        ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)

    4. **Translate the questions and choices in each copy by hand.** The quiz has no automatic translation.

    5. **Translate the buttons and app messages in [Quiz settings > Quiz Content](/reference/quiz-builder/quiz-settings/#messages-quiz-content).**

        ![manual_shopifyV2_quizbuilder_quizsettings_quizcontent](/images/manual_shopifyV2_quizbuilder_quizsettings_quizcontent.png)

    6. **Go to [App settings > Shopify Markets](/reference/app-settings/#shopify-markets).** It lists every market and language from your Shopify store.

        ![manual_shopifyV2_appsettings_markets](/images/manual_shopifyV2_appsettings_markets.png)

    7. **Pick the default quiz for each market.**

        ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

    8. **Click the `>` arrow on a market to set a different quiz per language.** The market expands to show its languages.

        ![manual_shopifyV2_appsettings_markets_showall](/images/manual_shopifyV2_appsettings_markets_showall.png)

    9. **Set the price format, if the market default is not the one you want.** Type the format you need, such as `${{amount}}` or `{{amount}}€`, in place of `{{amount}}USD` or `{{amount}}EUR`.

    10. **Save the changes.**

    11. **Publish the quiz.** See the [Publish](/reference/quiz-builder/share-publish/) tab in the app, or [how to publish a quiz on your website](/how-to-guides/publish-quiz/).

    12. **In Shopify, go to `Online store` and click the `👁️` eye icon.** Your store opens in a new window.

    13. **Open the page the quiz is published on.**

    14. **Switch market and language, and check that the right quiz loads each time.**

        !!! example "What to try"

            - Switch to the United States, and the US quiz appears
            - Switch to Belgium, and the EU quiz appears
            - Change the language to French, and the French quiz appears
            - Change the language to Spanish, and the Spanish quiz appears

            ![sample test](https://loom.com/i/6893314457ef4219a293e28708f91ba1?workflows_screenshot=true)

    15. **Check that prices appear in the format you set.**

    !!! info "Product translations come across on their own"

        With Shopify Markets configured, the results page shows translated product titles and descriptions, and localized prices, for the customer's own market and language. This runs through Shopify's Storefront API.

        Translations you made with the [Translate & Adapt](https://apps.shopify.com/translate-and-adapt) app appear automatically. Nothing extra is needed in the RevenueHunt app.

    !!! tip "Preview the results page as a market"

        1. Open the [Quiz builder](/reference/quiz-builder/).
        2. Click `Preview` in the top-right corner and go through to the results page.
        3. Pick the market and language to preview it as.

        ![how to test quiz results page](/images/tutorial_shopifyv2_preview_quiz_as_market.png)

=== "Shopify (Legacy)"

    !!! note "Not available on this platform"

        This version cannot assign a quiz to a market or a language.

        To run a quiz in another language, build a separate quiz for it and [publish that quiz](/how-to-guides/publish-quiz/) on the pages for that language.

=== "WooCommerce"

    !!! note "Not available on this platform"

        This version cannot assign a quiz to a market or a language.

        To run a quiz in another language, build a separate quiz for it and [publish that quiz](/how-to-guides/publish-quiz/) on the pages for that language.

=== "Magento"

    !!! note "Not available on this platform"

        This version cannot assign a quiz to a market or a language.

        To run a quiz in another language, build a separate quiz for it and [publish that quiz](/how-to-guides/publish-quiz/) on the pages for that language.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version cannot assign a quiz to a market or a language.

        To run a quiz in another language, build a separate quiz for it and [publish that quiz](/how-to-guides/publish-quiz/) on the pages for that language.

=== "Standalone"

    !!! note "Not available on this platform"

        This version cannot assign a quiz to a market or a language.

        To run a quiz in another language, build a separate quiz for it and [publish that quiz](/how-to-guides/publish-quiz/) on the pages for that language.

---

This article explains how to show a RevenueHunt quiz based on Shopify Markets.
