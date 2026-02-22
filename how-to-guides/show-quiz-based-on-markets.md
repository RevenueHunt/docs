---
icon: material/earth
---

# How to Show a Quiz Based on Shopify Markets

=== "Shopify"

    This article explains how to show a quiz based on Shopify Markets.

    With RevenueHunt Quizzes app, you can show a different quiz to users from different markets and languages.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=qKfPEBhJ2RvMlgBz" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "Tutorial"

        Check our step by step tutorial on how to set up Shopify Markets and assign quizzes to different markets and languages with the RevenueHunt app: [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).



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

## Step 1: Configure Shopify Markets

=== "Shopify"

    To start, make sure you have [Shopify Markets](https://help.shopify.com/en/manual/international/managing) enabled and cofigured in your Shopify store. In order to show a quiz in a differnt currency or language, you first need to have a market configured in your Shopify store for these currencies or languages.

    !!! example "Example"
        If you have a market configured for Europe with the `EUR` currency, you can show a quiz in that market. 
        
        If you have a market configured for the US with the `USD` currency, you can show a quiz in that market.

        If you have a market in Spanish with the `ES` language, you can show a quiz in Spanish for that market.

        If you market in France with the `FR` language, you can show a quiz in French for that market.



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


## Step 2: Create Different Quizzes for Different Markets

=== "Shopify"

    Go to the [Quiz Builder](/reference/quiz-builder/) and create a new quiz. 
    
    To create a quiz in a different languege, duplicate the quiz from the dashbaord and edit the quiz. 
    
    ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)
    
    The quiz doesn't have an automatic translstaion option, so you will have to transalte all the questions and answers manually. The text of buttons and admin messages can be translated in the [Quiz Settings > Quiz Content](/reference/quiz-builder/quiz-settings/#messages-quiz-content) section.  
    
    ![manual_shopifyV2_quizbuilder_quizsettings_quizcontent](/images/manual_shopifyV2_quizbuilder_quizsettings_quizcontent.png)
    
    You can create as many quizzes as you want, each in a different language.



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



## Step 3: Configure In-App Shopify Markets

=== "Shopify"

    Once all your quizzes in different languages are created, head over to [App Settings > Shopify Markets](/reference/app-settings/#shopify-markets). This section contains all the markets and langueges you've set up in your Shopify store.

    ![manual_shopifyV2_appsettings_markets](/images/manual_shopifyV2_appsettings_markets.png)

    Select which quiz should be the default quiz shown for each market.

    ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

    Click on `Show ALL locales` to set up a different default quiz for each languge and market specifically.

    ![manual_shopifyV2_appsettings_markets_showall](/images/manual_shopifyV2_appsettings_markets_showall.png)

    In there, you can also change format of how the price currency on recommended product is displayed. If you don't change the default, the price will be displayed as set up in your Shopify Market. If you want to change the format type the currency in the format you want, for example `${{amount}}` or `{{amount}}€` can be used to replace the default `{{amount}}USD` or `{{amount}}EUR`.



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



## Step 4: Save the Changes

=== "Shopify"

    Save the changes. From now on, the default quiz for your store will open. If you've configured [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that specific market will be shown instead.



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


## Step 5: Test the Quiz

=== "Shopify"

    To test that the right quiz is shown for the right market, ensure that the quiz is published on your website by following the instructions in the [Publish](/reference/quiz-builder/share-publish/) tab of the app or [this how to article](https://docs.revenuehunt.com/how-to-guides/publish-quiz/).
    
    Once the default quiz is published and markets set up, you can preview your store and test the setup on different markets and languages.

    1. In Shopify, go to `Online store` and click the `👁️` eye icon to preview the store. Your store will open in a new window. 
    2. Click on a link that opens the quiz or navigate to the page where the quiz is published. 
    3. Test by switching markets and languages to verify the correct quizzes load (e.g., US quiz for the United States, EU quiz for Belgium).
    4. Confirm that the correct quiz loads for each market and language.
    5. Check that prices are displayed in the correct format.

        !!! example "Example Test Scenarios"

            Market change: Switch to the United States → US quiz appears.

            Market change: Switch to Belgium → EU quiz appears.

            Language change: Change to French → French quiz appears.

            Language change: Change to Spanish → Spanish quiz appears.

            ![sample test](https://loom.com/i/6893314457ef4219a293e28708f91ba1?workflows_screenshot=true)


    !!! tip

        You can also preview a specific quiz results page within the `Preview` option in the app. 
        
        1. Open the [Quiz Builder](/reference/quiz-builder/).
        2. Click the `Preview` button in the top-right corner of the quiz builder and get all the way to the results page.
        3. There, you'll have the option to preview the results page as different markets and languages.

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
This article explains how to show a RevenueHunt Quizzes app quiz based on Shopify Markets.


