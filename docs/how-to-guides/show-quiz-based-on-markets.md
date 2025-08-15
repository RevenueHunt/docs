---
icon: material/earth
---

# How to Show a Quiz Based on Shopify Markets

=== "Shopify"


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.


=== "Shopify V2"

    This article explains how to show a quiz based on Shopify Markets.

    With RevenueHunt Quizzes app, you can show a different quiz to users from different markets and languages.

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.youtube.com/embed/c0exzYPtydo?si=qKfPEBhJ2RvMlgBz" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "Tutorial"

        Check our step by step tutorial on how to set up Shopify Markets and assign quizzes to different markets and languages with the RevenueHunt app: [Assign Quizzes to Shopify Markets and Languages](/tutorials/shopify-markets/).


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


    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.



=== "Shopify V2"

    To start, make sure you have [Shopify Markets](https://help.shopify.com/en/manual/international/managing) enabled and cofigured in your Shopify store. In order to show a quiz in a differnt currency or language, you first need to have a market configured in your Shopify store for these currencies or languages.

    !!! example "Example"
        If you have a market configured for Europe with the `EUR` currency, you can show a quiz in that market. 
        
        If you have a market configured for the US with the `USD` currency, you can show a quiz in that market.

        If you have a market in Spanish with the `ES` language, you can show a quiz in Spanish for that market.

        If you market in France with the `FR` language, you can show a quiz in French for that market.


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

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.


=== "Shopify V2"

    Go to the [Quiz Builder](/reference/quiz-builder/) and create a new quiz. 
    
    To create a quiz in a different languege, duplicate the quiz from the dashbaord and edit the quiz. 
    
    ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)
    
    The quiz doesn't have an automatic translstaion option, so you will have to transalte all the questions and answers manually. The text of buttons and admin messages can be translated in the [Quiz Settings > Quiz Content](/reference/quiz-builder/quiz-settings/#messages-quiz-content) section.  
    
    ![manual_shopifyV2_quizbuilder_quizsettings_quizcontent](/images/manual_shopifyV2_quizbuilder_quizsettings_quizcontent.png)
    
    You can create as many quizzes as you want, each in a different language.


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

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "Shopify V2"

    Once all your quizzes in different languages are created, head over to [App Settings > Shopify Markets](/reference/app-settings/#shopify-markets). This section contains all the markets and langueges you've set up in your Shopify store.

    ![manual_shopifyV2_appsettings_markets](/images/manual_shopifyV2_appsettings_markets.png)

    Select which quiz should be the default quiz shown for each market.

    ![manual_shopifyV2_appsettings_markets_pickquiz](/images/manual_shopifyV2_appsettings_markets_pickquiz.png)

    Click on `Show ALL locales` to set up a different default quiz for each languge and market specifically.

    ![manual_shopifyV2_appsettings_markets_showall](/images/manual_shopifyV2_appsettings_markets_showall.png)

    In there, you can also change format of how the price currency on recommended product is displayed. If you don't change the default, the price will be displayed as set up in your Shopify Market. If you want to change the format type the currency in the format you want, for example `${{amount}}` or `{{amount}}€` can be used to replace the default `{{amount}}USD` or `{{amount}}EUR`.


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

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "Shopify V2"

    Save the changes. From now on, the default quiz for your store will open. If you've configured [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that specific market will be shown instead.


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

    !!! note "Platform Availability"
        This feature is only available in the Built for Shopify version of the RevenueHunt app. It is **not** available for the legacy version of the RevenueHunt app for Shopify.

=== "Shopify V2"

    To test that the right quiz is shown for the right market, ensure that the quiz is published on your website by following the instructions in the [Publish](/reference/quiz-builder/share-publish/) tab of the app or [this how to article](https://docs.revenuehunt.com/how-to-guides/publish-quiz/).

    Then navigate to your website and change the languge or region to see if the right quiz is shown for that market.

    !!! warning

        The `Preview` option in the quiz builder always displays the default quiz in the default main market. It is not yet possible to preview the quiz in a different market within the app. To test the quiz in a different market, you need to publish the quiz on your website and then change the languge or region to see if the right quiz is shown for that market.


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


