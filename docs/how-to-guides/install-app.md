---
description: "Step-by-step guide to install the RevenueHunt app on your Shopify store and get started with product recommendation quizzes."
icon: material/download
---

# How to Install the App

The app installs from a different place on each platform. Pick yours below.

=== "Shopify"

    The Built for Shopify version is the current app, and it installs from the Shopify App Store.

    1. **Open the [Shopify App Store listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) and click `Add app`.**

    2. **Grant the permissions that connect the app to your store.**

    3. **In your Shopify admin, go to `Apps` and open `RevenueHunt Product Quiz Maker`.**

    4. **Confirm the app access and permissions.**

    5. **Check that the app opens on its [Dashboard](/reference/dashboard/).** That is where your quizzes are listed.

    Work through the [Success Checklist](/reference/dashboard/#success-checklist) next, to build and publish your first quiz.

    !!! tip "Going back to the legacy version"

        Select `Switch to legacy app` in the Shopify side menu. Your progress is saved in both versions, so nothing is lost either way.

        See [Switch to legacy](/reference/dashboard/#switch-to-legacy).

=== "Shopify (Legacy)"

    The legacy app installs from the same Shopify App Store listing as the current one. You choose between the two interfaces inside the app.

    1. **Open the [Shopify App Store listing](https://apps.shopify.com/product-recommendation-quiz-revenuehunt) and click `Add app`.**

    2. **Grant the permissions that connect the app to your store.**

    3. **In your Shopify admin, go to `Apps` and open `RevenueHunt Product Quiz Maker`.**

    4. **Check that the app opens on its [Dashboard](/reference/dashboard/).** That is where your quizzes are listed.

    Work through the [Success Checklist](/reference/dashboard/#success-checklist) next, to build and publish your first quiz.

    !!! tip "Moving to the Built for Shopify version"

        1. **Open the app in your Shopify admin.**

        2. **Select `Switch to Built for Shopify` in the Shopify side menu.**

            ![Switching from the legacy app to Built for Shopify](/images/switch-to-bfs.png)

        3. **Confirm the app access and permissions.**

        Your progress is saved in both versions, and you can switch back whenever you want.

        To bring a quiz you have already built across, use `Migrate from Legacy App` in the [New quiz](/reference/dashboard/#new-quiz) menu. See [How to Migrate a Legacy Quiz](/how-to-guides/migrate-shopify-legacy-quiz/).

=== "WooCommerce"

    The quiz runs as a WordPress plugin that connects your store to RevenueHunt.

    1. **Install and activate [WooCommerce](https://woocommerce.com/), if it is not already running.**

    2. **Install and activate the Product Recommendation Quiz plugin.** It is on the [WordPress Plugin Directory](https://wordpress.org/plugins/product-recommendation-quiz-for-ecommerce/) and on the [WooCommerce Marketplace](https://woocommerce.com/products/product-recommendation-quiz-for-woocommerce/). Both are free.

    3. **In your WordPress admin, open the `Product Quiz` tab.**

    4. **Grant the permission that connects the app to your WooCommerce store.**

    5. **Check that the app opens on its [Dashboard](/reference/dashboard/).** That is where your quizzes are listed.

    Work through the [Success Checklist](/reference/dashboard/#success-checklist) next, to build and publish your first quiz.

    !!! info "What the free plugin covers"

        Either plugin puts you on the Free plan, which covers up to 100 quiz responses a month. Above that the app asks you to upgrade to a Basic plan, billed monthly.

        See [Plans and pricing](/reference/plans-pricing/) for the rest of the plans.

    !!! tip "The plugin is not connecting"

        See [WordPress and WooCommerce troubleshooting](/how-to-guides/troubleshooting-product-recommendation-quiz-app-issues-for-wordpress-woocommerce/).

=== "Magento"

    The quiz runs as a Magento module. Installing it needs command line access to your server, so this one is a developer task.

    1. **Download the Product Recommendation Quiz module** from the [Product Recommendation Quiz for Magento page](https://revenuehunt.com/product-recommendation-quiz-for-magento/).

    2. **Install the module from the zip file, or with Composer.**

        ??? question "The commands for each route"

            **From a zip file**

            - Unzip the file into `app/code/Revenuehunt`.
            - Enable the module: `php bin/magento module:enable Revenuehunt_ProductQuiz`
            - Apply the database updates: `php bin/magento setup:upgrade`
            - Flush the cache: `php bin/magento cache:flush`

            **With Composer**

            - Make the module available in a Composer repository, such as the private `repo.magento.com`, the public `packagist.org`, or a public GitHub repository added as `vcs`.
            - Add that repository to your configuration: `composer config repositories.repo.magento.com composer https://repo.magento.com/`
            - Install the module: `composer require Revenuehunt/module-productquiz`
            - Enable the module: `php bin/magento module:enable Revenuehunt_ProductQuiz`
            - Apply the database updates: `php bin/magento setup:upgrade`
            - Flush the cache: `php bin/magento cache:flush`

    3. **In your Magento admin, go to `Stores > Settings > Configuration > Services > Magento Web API > Web API Security` and set `Allow Anonymous Guest Access` to `Yes`.** See the Magento documentation on [anonymous API security](https://devdocs.magento.com/guides/v2.3/rest/anonymous-api-security.html).

        ??? info "Where the module keeps its configuration"

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

    4. **In your Magento admin, go to `Marketing` and open `Product Recommendation Quiz`.**

    5. **Grant the permission that connects the app to your Magento store.**

    6. **Check that the app opens on its [Dashboard](/reference/dashboard/).** That is where your quizzes are listed.

    Work through the [Success Checklist](/reference/dashboard/#success-checklist) next, to build and publish your first quiz.

    !!! warning "What the module needs"

        - Your website must have a valid HTTPS or SSL certificate.
        - The module does not run on a local or development environment.
        - The MiniCart integration is off by default. If your theme uses MiniCart, uncomment this line in `view/frontend/layout/default.xml`.

                    ```html
            <block class="Magento\Framework\View\Element\Template" name="revenuehunt-script" template="Revenuehunt_ProductQuiz::head/js.phtml" />
                    ```

    ??? info "For the developer installing it"

        - Composer package: `revenuehunt/module-productquiz`
        - API endpoint: POST `Revenuehunt\ProductQuiz\Api\PrqSetTokenManagementInterface` to `Revenuehunt\ProductQuiz\Model\PrqSetTokenManagement`
        - Controller: `adminhtml > prqfw/index/index`
        - Source and issues: [Magento module repository on GitHub](https://github.com/RevenueHunt/product-recommendation-quiz-for-magento)

=== "BigCommerce"

    The quiz installs as a BigCommerce app.

    1. **Open the [BigCommerce listing for Product Recommendation Quiz](https://admin.revenuehunt.com/bc/affiliate_code) and click `get this app`.**

    2. **Grant the permission that connects the app to your BigCommerce store.**

    3. **In your BigCommerce admin, go to `Apps` and open Product Recommendation Quiz.**

    4. **Check that the app opens on its [Dashboard](/reference/dashboard/).** That is where your quizzes are listed.

    Work through the [Success Checklist](/reference/dashboard/#success-checklist) next, to build and publish your first quiz.

=== "Standalone"

    The standalone version runs on its own, with no store behind it. It suits a shop built on Wix, Squarespace Commerce, Odoo, or anything else the app has no plugin for.

    !!! warning "Two things work differently here"

        - Products are not pulled from a store. Add them by hand or through a Google Product Feed.
        - There is no add to cart and no checkout. The customer reads the results page and clicks a product to open it.

    1. **Sign up on the [RevenueHunt registration page](https://admin.revenuehunt.com/register).** An email address and a password are all it takes.

    2. **[Log in to your account](https://admin.revenuehunt.com/login).**

    3. **Add your products and collections in the in-app [Catalogue](https://admin.revenuehunt.com/catalogue).**

    4. **Check that the app opens on its [Dashboard](/reference/dashboard/).** That is where your quizzes are listed.

    Work through the [Success Checklist](/reference/dashboard/#success-checklist) next, to build and publish your first quiz.

    !!! tip "Filling the catalogue"

        See [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/).

    !!! note "Changing your username or password"

        [Contact customer support](/how-to-guides/contact-customer-support/) to change either one.

---

This article explains how to install the RevenueHunt app on each platform, and how to check that the install worked.