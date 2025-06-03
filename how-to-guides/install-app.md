---
icon: material/download
---

## How To Install the App

=== "Shopify"

    1. Navigate to our [Shopify App Store listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) and click on “Add app”.
    2. Grant permissions to connect our app to your Shopify.
    3. In your Shopify dashboard, go to “Apps” and click on the **RevenueHunt** to open it.
    4. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    5. Drive traffic to your quiz and start getting sales and leads!

=== "Shopify V2"

    1. Navigate to our [Shopify App Store listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) and click on “Add app”.
    2. Grant permissions to connect our app to your Shopify.
    3. In your Shopify dashboard, go to “Apps” and click on the **RevenueHunt** to open it.
    4. From the right-hand side Shopify App menu, select `Switch to Built for Shopify`. 
    5. Confirm app access and permissions. 
    6. Follow the instructions in the [App Manual](/reference/app-settings/#switch-to-v1) to switch back to the original version of the app.

=== "WooCommerce"

    1. Install and activate [WooCommerce](https://woocommerce.com/) if you haven’t already done so.
    2. Install and activate our **Product Recommendation Quiz** plugin for WordPress. Get the latest version [here](https://revenuehunt.com/product-recommendation-quiz-woocommerce/).

        ??? question "What’s the difference between the WooCommerce extension and a WordPress Plugin?"

            The [WordPress Plugin](https://wordpress.org/plugins/product-recommendation-quiz-for-ecommerce/) is free to install and puts you directly on our **Free plan**. The Free plan allows up to 100 quiz responses per month without any charges but has a “Powered by RevenueHunt” branding. If your usage exceeds the Free plan, you’ll be asked to upgrade to a Basic plan which is billed monthly.

            The [WooCommerce extension](https://woocommerce.com/products/product-recommendation-quiz-for-woocommerce/) requires a yearly subscription (29$/year) to install the app and puts you on a **Starter Plan**. The Starter Plan allows up to 250 quiz responses per month and has the “Powered by RevenueHunt” branding removed. If your usage exceeds the Starter plan, you’ll be asked to upgrade to a Basic plan which is billed monthly.

    3. In your WordPress dashboard, navigate to the `Product Quiz` tab.
    4. Grant permission to connect our app to your WooCommerce.
    5. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    6. Drive traffic to your quiz and start getting sales and leads!

    If you have any issues with your WooCommerce installation please check [this article](https://revenuehunt.com/faqs/troubleshooting-product-recommendation-quiz-app-issues-for-wordpress-woocommerce/).

=== "Magento"

    1. Download and install the **Product Recommendation Quiz** module. Get the latest version [here](https://revenuehunt.com/product-recommendation-quiz-for-magento/).

        ??? question "How to install the module?"

            Type 1: Zip file

            - Unzip the zip file in app/code/Revenuehunt
            - Enable the module by running php bin/magento module:enable Revenuehunt_ProductQuiz
            - Apply database updates by running php bin/magento setup:upgrade*
            - Flush the cache by running php bin/magento cache:flush

            Type 2: Composer

            - Make the module available in a composer repository for example:
                - private repository repo.magento.com
                - public repository packagist.org
                - public github repository as vcs
            - Add the composer repository to the configuration by running composer config repositories.repo.magento.com composer https://repo.magento.com/
            - Install the module composer by running composer require Revenuehunt/module-productquiz
            - enable the module by running php bin/magento module:enable Revenuehunt_ProductQuiz
            - apply database updates by running php bin/magento setup:upgrade*
            - Flush the cache by running php bin/magento cache:flush

    2. In your Magento dashboard, navigate to `STORES > Stores > Settings > Configuration > SERVICES > Magento Web API > Web API Security > Allow Anonymous Guest Access : Yes` [See Devdocs Reference](https://devdocs.magento.com/guides/v2.3/rest/anonymous-api-security.html)

        ??? "Configuration details"

            Api URL Test (product_quiz/general/prq_api_url_test)

            prq_admin_url_test (product_quiz/general/prq_admin_url_test)

            Is Test mode (product_quiz/general/prq_is_test)

            API URL (product_quiz/general/prq_api_url)

            Admin URL (product_quiz/general/prq_admin_url)

            RH Domain (product_quiz/hidden/rh_domain)

            rh_api_key (product_quiz/hidden/rh_api_key)

            rh_token (product_quiz/hidden/rh_token)

            rh_shop_hashid (product_quiz/hidden/rh_shop_hashid)

    2. In your Magento dashboard, navigate to the Marketing tab and open `Product Recommendation Quiz`.
    3. Grant permission to connect our app to your Magento store.
    4. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    5. Drive traffic to your quiz and start getting sales and leads!
    
    If you have any issues, follow the instructions provided in GitHub [here](https://github.com/RevenueHunt/product-recommendation-quiz-for-magento).

    !!! warning "Technical Specifications"

        - You website must have a valid HTTPS/SSL certificate installed.
        - Does not work on local/development environments. `revenuehunt/module-productquiz`
        - API Endpoint
            - POST - Revenuehunt\ProductQuiz\Api\PrqSetTokenManagementInterface > Revenuehunt\ProductQuiz\Model\PrqSetTokenManagement
        - Controller `adminhtml > prqfw/index/index`
        - The MiniCart integration is disabled by default. If your theme uses MiniCart, you can uncomment the code in the modeule file: `view/frontend/layout/default.xml`
            ```html
            <block class="Magento\Framework\View\Element\Template" name="revenuehunt-script" template="Revenuehunt_ProductQuiz::head/js.phtml" />
            ```

=== "BigCommerce"

    1. Navigate to our [BigCommerce Marketplace listing](https://admin.revenuehunt.com/bc/affiliate_code), find **Product Recommendation Quiz** and click on `get this app`.
    2. Grant permission to connect our app to your BigCommerce store. 
    3. In your BigCommerce dashboard, go to `Apps` and click on our app.
    4. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    5. Drive traffic to your quiz and start getting sales and leads!

=== "Standalone"

    Is your store build on Wix, Squarespace Commerce, Odoo, or others? We got you covered!

    RevenueHunt grants you the option to install a “standalone” version of our Product Recommendation Quiz app in a custom-built eCommerce. This comes at a cost, though:

    - products have to be added manually to the app or via Google Product Feed
    - the add to cart and proceed to checkout functionalities won’t work. After the user takes the quiz, they’ll see a results page where they can click on the products to view them.

    To install the app:

    1. Sign up for the standalone version of the **RevenueHunt Product Recommendation Quiz** [here](https://admin.revenuehunt.com/register). All you need is an email and a password.
    2. Once registered, you can log in to your account [here](https://admin.revenuehunt.com/login).
    2. Add products and collections. Check how to do that [here](/reference/dashboard/#success-checklist). You can access your in-app Product [Catalogue](https://admin.revenuehunt.com/catalogue) at all times.
    3. Follow the [Success Checklist](/reference/dashboard/#success-checklist) to create and publish your quiz.
    4. Drive traffic to your quiz and start getting sales and leads!
    

    !!! note

        If you want to change the username or password, please [contact support](/how-to-guides/contact-customer-support/).
