---
icon: material/account-file-text-outline
description: "Information about showing RevenueHunt quiz on Shopify customer profile pages."
---

# How to Show a Quiz on a Customer Profile

Showing a customer their own quiz results inside their account page keeps the recommendation available long after they took the quiz.

=== "Shopify"

    !!! note "Not available on this platform"

        The `💎Built for Shopify` version has no app embed for the customer profile yet, so the quiz cannot be shown there.

        To register your interest in the feature, [contact support](/how-to-guides/contact-customer-support/).

=== "Shopify (Legacy)"

    This section explains how to render a customer's quiz results inside their Shopify account page.

    !!! warning "This one is for a developer"

        The steps below need Shopify Liquid. If you do not write Liquid, ask a professional to do it. You can find or hire one through [Shopify Experts](https://experts.shopify.com/).

    1. **Connect the quiz to [Shopify's Customer List](/how-to-guides/send-leads-to-shopify-customers/).** The results can only reach a profile once the lead is attached to it.

        !!! tip "Check the connection first"

            [How to Send Quiz Leads to Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/) covers the setup and how to confirm it worked.

    2. **Go to your `Shopify Theme` > `Actions` > `Edit code` and open `customers/account.liquid`.**

    3. **Find the metafield the app writes to the profile.** Every completed quiz sends the customer a `metafield` holding the response and its recommendations.

        ```html
        customer.metafields.prq.response_permalink
        ```

        ![how to show quiz on customer profile](/images/how_to_show_quiz_on_customer_profile.png)

    4. **Add the `embed.js` script to the template.** It is on line 67 of the screenshot.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    5. **[Generate an embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) from the [Share](/reference/quiz-builder/share-publish/) section of the quiz.**

    6. **Insert the iframe, pointing it at the metafield.** It is on line 68 of the screenshot.

        ```html
        <iframe src="{{ customer.metafields.prq.response_permalink }}" style="width:100%; border: none; margin-bottom: 30px; position: absolute; left: 0;"></iframe>
        ```

    The customer's profile then carries their results page:

    ![how to show quiz on customer profile rendered](/images/how_to_show_quiz_on_customer_profile_rendered.png)

=== "WooCommerce"

    !!! note "Not available on this platform"

        The app cannot show the quiz on a customer profile in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

=== "Magento"

    !!! note "Not available on this platform"

        The app cannot show the quiz on a customer profile in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

=== "BigCommerce"

    !!! note "Not available on this platform"

        The app cannot show the quiz on a customer profile in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

=== "Standalone"

    !!! note "Not available on this platform"

        The app cannot show the quiz on a customer profile in this version.

    !!! tip "A developer can try it anyway"

        Your developer can place the [embed code](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) into the customer profile theme or template. This is not a feature of the app, so the support team cannot help with it.

---

This guide explains how to show a quiz on a customer profile in Shopify.
