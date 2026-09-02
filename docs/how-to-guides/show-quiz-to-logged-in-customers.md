---
icon: material/login
description: "Information about showing RevenueHunt quiz only to logged-in customers in Shopify."
---

# How to Show a Quiz Only to Logged-in Customers

Put the quiz on a page that only signed-in customers can use. A customer who already took it sees their own results instead, and everyone else is asked to log in.

=== "Shopify"

    !!! note "Not available on this platform"

        The Built for Shopify version has no way to show the quiz to logged-in customers only.

        To register your interest in the feature, [contact support](/how-to-guides/contact-customer-support/).

=== "Shopify (Legacy)"

    Customer metafields can render quiz results into any part of your Shopify theme. This section uses them to build a page that behaves differently for a logged-in customer.

    !!! warning "This one is for a developer"

        The steps below need Shopify Liquid. If you do not write Liquid, ask a professional to do it. You can find or hire one through [Shopify Experts](https://experts.shopify.com/).

    1. **Go to `Online Store` > `Themes`, then `Actions` > `Edit Code`.**

    2. **Create a new page template.** Set the template type to `liquid` and the name to `quiz`.

        ![how to show quiz to logged in customers template](/images/how_to_show_quiz_to_logged_in_customers_template.png)

    3. **Replace the contents of `page.quiz.liquid` with this code.**

        ```html
        <div class="page-width">
          <div class="grid">
            <div class="grid__item medium-up--five-sixths medium-up--push-one-twelfth">
              <div class="section-header text-center">
                <h1>{{ page.title }}</h1>
              </div>
              <div class="grid myaccount">
                {% if customer %}
                  <div class="grid__item rh-inline" style="margin: 60px 0 120px;">
                    <script src="https://admin.revenuehunt.com/embed.js" async></script>
                    {% if customer.metafields.prq.response_permalink %}
                      <h2>Your Profile</h2>
                      <iframe src="{{ customer.metafields.prq.response_permalink }}" style="width:100%; border: none; margin-bottom: 30px; position: absolute; left: 0;"></iframe>
                    {% else %}
                      <h2>Take our Quiz to determine your skincare routine</h2>
                      <iframe src="https://admin.revenuehunt.com/public/quiz/dbqHqN" style="width:100%; border: none; margin-bottom: 30px; position: absolute; left: 0;"></iframe>
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

    4. **Replace the quiz URL and the two account URLs with your own.** Adapt the headings and the copy to your store as well.

    5. **Go to `Online Store` > `Pages` and click `Add Page`.**

    6. **Give the page a title, then select the `quiz` theme template.**

        ![how to show quiz to logged in customers new page](/images/how_to_show_quiz_to_logged_in_customers_new_page.png)

    7. **Click `Save`.**

    The page then behaves like [this demo page](https://skincarequiz.myshopify.com/pages/logged-in-quiz):

    - A customer who is not logged in is asked to log in or sign up.
    - A customer who is logged in sees their results page, or the start of the quiz if they have not taken it yet.

=== "WooCommerce"

    !!! note "Not available on this platform"

        The app cannot show the quiz to logged-in customers only in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

=== "Magento"

    !!! note "Not available on this platform"

        The app cannot show the quiz to logged-in customers only in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

=== "BigCommerce"

    !!! note "Not available on this platform"

        The app cannot show the quiz to logged-in customers only in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

=== "Standalone"

    !!! note "Not available on this platform"

        The app cannot show the quiz to logged-in customers only in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

---

This guide explains how to show a quiz only to logged-in customers in Shopify.
