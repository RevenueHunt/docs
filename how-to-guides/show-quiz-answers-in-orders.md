---
description: "Learn how to display RevenueHunt quiz answers in Shopify orders and customer notes."
icon: material/receipt-text-outline
---

# How to Show Quiz Answers in Shopify Orders

You can see exactly which orders in your Shopify Orders tab came from the quiz, and what the customer answered to get there.

## Pass the answers to Shopify

=== "Shopify"

    In the Built for Shopify version, quiz data reaches Shopify orders through **custom JavaScript**. You control which values are saved to the cart and carried through to the order.

    !!! info "You choose exactly what to save"

        This version does **not** write every quiz answer into Shopify order notes on its own.

        You pass the values you want instead. That suits saving a result name, a score, a response ID, a campaign tag, or a handful of answers.

    1. **Add your custom code to the relevant [question](/reference/quiz-builder/questions/#question-settings) or [results page](/reference/quiz-builder/results-page/#custom-js-code).** See [how to add JavaScript](/how-to-guides/add-javascript/).

    2. **Write the values you want to keep with `actions.updateCartAttributes({...})`.**

        ```javascript
        if (quiz.metadata.isStoreRenderer && !quiz.metadata.inBuilder) {
          await actions.updateCartAttributes({
            __quiz_response_id: quiz.metadata.responseId,
            __result_ref: quiz.currentResult?.ref || '',
            skincare_segment: quiz.variables.highest || ''
          });
        }
        ```

        That example saves the response ID, the result reference and a custom segment tag from the results page.

        !!! tip "Hidden and visible cart attributes"

            Prefix a name with `__` to keep the value internal to the cart, rather than showing it as a normal storefront cart attribute.

            Leave the prefix off when the value should stay visible on Shopify cart and order screens.

    3. **Click `Save`.** This updates the live quiz.

    4. **Take the quiz on your storefront and add the products to the cart.**

    5. **Place a test order, then check that the values arrived on it.**

    !!! warning "The code has to run before the customer leaves for the cart"

        Cart attributes are written only when the customer reaches the page your custom JavaScript runs on. Put the code on a question or results page that comes before the cart.

    !!! warning "Attribution needs an unbroken flow"

        Shopify Revenue Tracking and cart-based order tagging need an unbroken flow. The customer has to add products to the cart from the results page, then complete the checkout. An order placed later may no longer be attributed to the quiz.

        Set the Checkout settings on your results page to `proceed to cart`, not `proceed to checkout` or `link to product`. See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

=== "Shopify (Legacy)"

    1. **Connect the quiz to [Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/).**

    2. **Enable [Order Notes](https://help.shopify.com/en/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/get-more-information-with-order-notes) in your Shopify theme.**

    3. **Go to the `Connect` tab in the quiz and scroll to `Shopify Orders Tagging`.**

    4. **Click `connect`.** The quiz can then add tags and answers to your orders.

    5. **Click `Publish` in the top-right corner.**

    Every order in the Shopify Orders list then carries a small `Notes` section holding the quiz tags.

    ![how to show quiz answers on orders example1](/images/how_to_show_quiz_answers_on_orders_example1.png)

    Click `Edit` to change what that section says.

    ![how to show quiz answers on orders example3](/images/how_to_show_quiz_answers_on_orders_example3.png)

    !!! warning "Some themes block the tags"

        A few Shopify themes disable passing tags to orders. Those themes usually offer a setting to turn it back on.

    !!! warning "Attribution needs an unbroken flow"

        Shopify Revenue Tracking and Orders Tagging need an unbroken flow. The customer has to add products to the cart from the results page, then complete the checkout. An order placed later is no longer attributed to the quiz.

        Set the Checkout settings on your Results Page to `proceed to cart`, not `proceed to checkout` or `link to product`. See [how to change checkout settings on your results page](/how-to-guides/change-checkout-settings/).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

=== "Magento"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

=== "BigCommerce"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

=== "Standalone"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

## Testing the connection

=== "Shopify"

    Work through these when the cart or order tagging does not behave.

    1. **Open the question or results page holding your custom JavaScript, and confirm the code is saved.**

    2. **Check that the code uses `actions.updateCartAttributes({...})`.** It has to run before the customer leaves for the cart or the checkout.

    3. **Open the live storefront quiz in another browser, or in an incognito window.** Do not test on the preview or on admin.revenuehunt.com.

    4. **Add a temporary `console.log('tagging cart')` line and watch the browser console.** It tells you whether the script runs at all.

    5. **Take the quiz and add the products to the cart.**

    6. **Place a valid [Shopify test order](https://help.shopify.com/en/manual/checkout-settings/test-orders).**

    7. **Open that order in Shopify and check which cart attributes came through the checkout.**

    If the values are still missing, [contact the support team](/how-to-guides/contact-customer-support/) with:

    - your quiz URL
    - the custom JavaScript you used
    - the values you expected to save
    - a screenshot of the order or the cart

=== "Shopify (Legacy)"

    Work through these when the orders tagging does not behave.

    1. **Go to the `Connect` tab and disconnect the quiz from `Shopify Customers` and `Shopify Orders Tagging`.**

    2. **Click the top-right `Publish` button.**

    3. **Connect the quiz to both of them again.**

    4. **Click `Publish` again.** That resets the connection.

    5. **Open the live quiz on your site in another browser, or in an incognito window.** Do not test on the preview or on admin.revenuehunt.com.

    6. **Take the quiz through to the results, giving the email address you will use at the checkout.** An address such as `yourname+test1@example.com` keeps the test out of your real inbox.

    7. **Add the products to the cart, then open the cart.**

    8. **Place a valid [Shopify test order](https://help.shopify.com/en/manual/checkout-settings/test-orders).**

    9. **Check the lead reached `Shopify Customers`, marked `RevenueHunt` in its details.**

    10. **Open `Shopify Orders` and check that the order notes appear on the test order.**

    If the notes are still missing, [contact the support team](/how-to-guides/contact-customer-support/).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

=== "Magento"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

=== "BigCommerce"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

=== "Standalone"

    !!! note "Not available on this platform"

        Quiz answers reach orders in the Shopify versions of the app only.

---

This article explains how to show quiz answers in Shopify Orders.
