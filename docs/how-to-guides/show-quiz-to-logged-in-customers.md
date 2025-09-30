---
icon: material/login
---

# How to Show Quiz Only to Logged-in Customers

=== "Shopify"

    The new Built for Shopify version of the RevenueHunt app does not have a way to show the quiz to logged-in customers yet. It is **not possible yet** to directly show the quiz to logged-in customers using the new Built for Shopify version of the RevenueHunt app.

    If you're interested in this feature, please let us know by [contacting support](/how-to-guides/contact-customer-support/).


=== "Shopify (Legacy)"

    It’s possible to use the customer metafields to render quiz results onto different elements of your Shopify Theme liquids. This article explains how to show the quiz only to logged-in customers in Shopify.

    !!! warning

        This guide is meant for developers and Shopify Partners. If you're not familiar with Shopify liquid, it is advised to ask for help from a professional to implement this. You can find/hire a developer [here](https://experts.shopify.com/).

    !!! note

        This method works only for Shopify accounts using our [RevenueHunt](https://revenuehunt.com/product-recommendation-quiz-shopify/) app. Unfortunately, we don't have a solution yet on how to do this in WooCommerce, Magento or BigCommerce.

    **Step 1: Create a New Page Template**

    1. In your `Online Store > Themes` section, head to `Actions > Edit Code`.
    2. Create a new Page template. 
        - Template type: `liquid`. 
        - Template name: `quiz`.

    ![how to show quiz to logged in customers template](/images/how_to_show_quiz_to_logged_in_customers_template.png)

    **Step 2: Add New Page Code**

    Replace your new `page.quiz.liquid` code for the following code and adapt the texts to your store:

    ```html
    <div class="page-width">
    <div class="grid">
    <div class="grid__item medium-up--five-sixths medium-up--push-one-twelfth">
    <div class="section-header text-center">
    <h1>{{ page.title }}</h1>
    </div><div class="grid myaccount">
    {% if customer %}
    <div class="grid__item rh-inline" style="margin: 60px 0 120px;">
    <script src="https://admin.revenuehunt.com/embed.js" async></script>
    {% if customer.metafields.prq.response_permalink %}
    <h2>Your Profile</h2>
    <iframe src="{{ customer.metafields.prq.response_permalink }}" style="width:100%; border: none; margin-bottom: 30px; position: absolute; left: 0;" />
    {% else %}
    <h2>Take our Quiz to determine your skincare routine</h2>
    <iframe src="https://admin.revenuehunt.com/public/quiz/dbqHqN" style="width:100%; border: none; margin-bottom: 30px; position: absolute; left: 0;" />
    {% endif %}
    </div>
    {% else %}
    <div class="w-100"><h3>You're not logged in.</h3></div>
    <div class="w-100"><p>Please <a href="https://skincarequiz.myshopify.com/account/login">log in</a> or <a href="https://skincarequiz.myshopify.com/account/register">sign up</a> to take the quiz.</p></div>
    {% endif %}
    </div>
    </div>
    </div>
    </div>
    ```

    Remember to replace the URL sections in the code with the correct URLs to the quiz and your website, respectively.

    **Step 3: Apply the theme to the page**

    1. Go to `Online Store > Pages` and click on the `Add Page` button. 
    2. Add the title, then select the `quiz` Theme template.
        ![how to show quiz to logged in customers new page](/images/how_to_show_quiz_to_logged_in_customers_new_page.png)

    3. Click on `Save`.

    The result should look something like this: [https://skincarequiz.myshopify.com/pages/logged-in-quiz](https://skincarequiz.myshopify.com/pages/logged-in-quiz). 

    - If you’re not logged in, you’re prompted to log in or sign up. 
    - If you’re logged in, you’re either shown the results page (if you already took the quiz) or the quiz’s start page.

=== "WooCommerce"

    It is **not possible yet** to directly show the quiz to logged-in customers using the RevenueHunt app for WooCommerce.

    !!! tip 

        Your developer can try embeding the quiz on a customer profile by using the [embed code](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) onto the customer profile theme or template. Please note that this is not a feature of the app and we cannot provide support for this.

=== "Magento"

    It is **not possible yet** to directly show the quiz to logged-in customers using the RevenueHunt app for Magento.

    !!! tip 

        Your developer can try embeding the quiz on a customer profile by using the [embed code](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) onto the customer profile theme or template. Please note that this is not a feature of the app and we cannot provide support for this.

=== "BigCommerce"

    It is **not possible yet** to directly show the quiz to logged-in customers using the RevenueHunt app for BigCommerce.

    !!! tip 

        Your developer can try embeding the quiz on a customer profile by using the [embed code](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) onto the customer profile theme or template. Please note that this is not a feature of the app and we cannot provide support for this.

=== "Standalone"

    It is **not possible yet** to directly show the quiz to logged-in customers using the Standalone RevenueHunt app for Headless ecommerce.

    !!! tip 

        Your developer can try embeding the quiz on a customer profile by using the [embed code](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) onto the customer profile theme or template. Please note that this is not a feature of the app and we cannot provide support for this.

---
By following this article, developers can learn how to show a quiz to logged-in customers only.