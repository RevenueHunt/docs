---
description: "Step-by-step guide to install the RevenueHunt app on your Shopify store and get started with product recommendation quizzes."
icon: material/download
---

# How to Install the App

=== "Shopify"

    1. Navigate to our [Shopify App Store listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) and click on “Add app”.
    2. Grant permissions to connect the app to your Shopify store.
    3. In your Shopify dashboard, go to “Apps” and click on the **RevenueHunt** to open it.
    4. Confirm app access and permissions.
    5. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    6. Drive traffic to your quiz and start getting sales and leads.

    !!! info "For Shopify legacy app users"

        You can switch to the new Built for Shopify version of the app by following these steps:

        1. Open the **RevenueHunt** app in your Shopify dashboard.
        2. From the right-hand side Shopify App menu, select `Switch to Built for Shopify`.
        3. Confirm app access and permissions.
        4. Follow the onboarding process to create and publish your quiz.
        5. Follow the instructions in the [App Manual](/reference/dashboard/#switch-to-legacy) to switch back to the original version of the app. When switching, all your changes will be saved on both app versions.

        You can migrate existing quizzes from the legacy app using the **Migrate from Legacy App** option in the [New Quiz](/how-to-guides/migrate-shopify-legacy-quiz/) menu.




=== "Shopify (Legacy)"

    1. Navigate to our [Shopify App Store listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) and click on “Add app”.
    2. Grant permissions to connect the app to your Shopify store.
    3. In your Shopify dashboard, go to “Apps” and click on the **RevenueHunt** to open it.
    4. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    5. Drive traffic to your quiz and start getting sales and leads.

    !!! info "For Shopify legacy app users"

        You can switch to the new Built for Shopify version of the app by following these steps:

        1. Open the **RevenueHunt** app in your Shopify dashboard.
        2. From the right-hand side Shopify App menu, select `Switch to Built for Shopify`.
        3. Confirm app access and permissions.
        4. Follow the onboarding process to create and publish your quiz.
        5. Follow the instructions in the [App Manual](/reference/dashboard/#switch-to-legacy) to switch back to the original version of the app. When switching, all your changes will be saved on both app versions.

        You can migrate existing quizzes from the legacy app using the **Migrate from Legacy App** option in the [New Quiz](/how-to-guides/migrate-shopify-legacy-quiz/) menu.


=== "WooCommerce"

    1. Install and activate [WooCommerce](https://woocommerce.com/) if you have not already.
    2. Install and activate our **Product Recommendation Quiz** plugin from the [WordPress Plugin Directory](https://wordpress.org/plugins/product-recommendation-quiz-for-ecommerce/). It is also available on the [WooCommerce Marketplace](https://woocommerce.com/products/product-recommendation-quiz-for-woocommerce/). Both are free and put you on the **Free plan**, which covers up to 100 quiz responses a month. Above that you are asked to upgrade to a Basic plan, billed monthly.

    3. In your WordPress dashboard, navigate to the `Product Quiz` tab.
    4. Grant permission to connect the app to your WooCommerce store.
    5. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    6. Drive traffic to your quiz and start getting sales and leads.

    If you have any issues with your WooCommerce installation please check [WooCommerce troubleshooting FAQ](https://revenuehunt.com/faqs/troubleshooting-product-recommendation-quiz-app-issues-for-wordpress-woocommerce/).

=== "Magento"

    1. Download and install the **Product Recommendation Quiz** module. Get the latest version from the [Product Recommendation Quiz for Magento page](https://revenuehunt.com/product-recommendation-quiz-for-magento/).

        ??? question "How to install the module?"

            Type 1: Zip file

            - Unzip the file into `app/code/Revenuehunt`.
            - Enable the module: `php bin/magento module:enable Revenuehunt_ProductQuiz`
            - Apply the database updates: `php bin/magento setup:upgrade`
            - Flush the cache: `php bin/magento cache:flush`

            Type 2: Composer

            - Make the module available in a composer repository, for example:
                - the private repository `repo.magento.com`
                - the public repository `packagist.org`
                - a public GitHub repository, as `vcs`
            - Add that repository to your configuration: `composer config repositories.repo.magento.com composer https://repo.magento.com/`
            - Install the module: `composer require Revenuehunt/module-productquiz`
            - Enable the module: `php bin/magento module:enable Revenuehunt_ProductQuiz`
            - Apply the database updates: `php bin/magento setup:upgrade`
            - Flush the cache: `php bin/magento cache:flush`

    2. In your Magento dashboard, navigate to `STORES > Stores > Settings > Configuration > SERVICES > Magento Web API > Web API Security > Allow Anonymous Guest Access : Yes` See the Magento documentation on [anonymous API security](https://devdocs.magento.com/guides/v2.3/rest/anonymous-api-security.html).

        ??? info "Configuration details"

            | Setting | Configuration path |
            |---|---|
            | Api URL Test | `product_quiz/general/prq_api_url_test` |
            | Admin URL Test | `product_quiz/general/prq_admin_url_test` |
            | Is Test mode | `product_quiz/general/prq_is_test` |
            | API URL | `product_quiz/general/prq_api_url` |
            | Admin URL | `product_quiz/general/prq_admin_url` |
            | RH Domain | `product_quiz/hidden/rh_domain` |
            | API key | `product_quiz/hidden/rh_api_key` |
            | Token | `product_quiz/hidden/rh_token` |
            | Shop hash id | `product_quiz/hidden/rh_shop_hashid` |

    3. In your Magento dashboard, go to the Marketing tab and open `Product Recommendation Quiz`.
    4. Grant permission to connect the app to your Magento store.
    5. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    6. Drive traffic to your quiz and start getting sales and leads.

    If you have any issues, follow the instructions in the [Magento module repository on GitHub](https://github.com/RevenueHunt/product-recommendation-quiz-for-magento).

    !!! warning "Technical Specifications"

        - Your website must have a valid HTTPS or SSL certificate installed.
        - Does not work on a local or development environment. The package is `revenuehunt/module-productquiz`.
        - API Endpoint
            - POST - `Revenuehunt\ProductQuiz\Api\PrqSetTokenManagementInterface` > `Revenuehunt\ProductQuiz\Model\PrqSetTokenManagement`
        - Controller `adminhtml > prqfw/index/index`
        - The MiniCart integration is disabled by default. If your theme uses MiniCart, uncomment the code in the module file: `view/frontend/layout/default.xml`
            ```html
            <block class="Magento\Framework\View\Element\Template" name="revenuehunt-script" template="Revenuehunt_ProductQuiz::head/js.phtml" />
            ```

=== "BigCommerce"

    1. Navigate to our [BigCommerce Marketplace listing](https://admin.revenuehunt.com/bc/affiliate_code), find **Product Recommendation Quiz** and click on `get this app`.
    2. Grant permission to connect the app to your BigCommerce store.
    3. In your BigCommerce dashboard, go to `Apps` and click on our app.
    4. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    5. Drive traffic to your quiz and start getting sales and leads.

=== "Standalone"

    Is your store built on Wix, Squarespace Commerce, Odoo or something else?

    You can install a “standalone” version of the RevenueHunt app on a custom-built store. Two things do not work:

    - products have to be added manually to the app or via Google Product Feed
    - add to cart and proceed to checkout are not available. After the quiz, the customer sees a results page and clicks a product to view it.

    To install the app:

    1. Sign up for the standalone version of the **RevenueHunt Product Recommendation Quiz** on the [RevenueHunt registration page](https://admin.revenuehunt.com/register). All you need is an email and a password.
    2. Once registered, [log in to your account](https://admin.revenuehunt.com/login).
    3. Add products and collections. Your in-app [Catalogue](https://admin.revenuehunt.com/catalogue) is available at any time.
    4. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    5. Drive traffic to your quiz and start getting sales and leads.

    !!! tip "How do I add products to Standalone RevenueHunt App?"

        To add products and collections to the Standalone version, see [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/).

    !!! note

        To change the username or password, [contact support](/how-to-guides/contact-customer-support/).
