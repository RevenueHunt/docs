---
description: "Learn how to display RevenueHunt quiz answers in Shopify orders and customer notes."
---

# How to Show Quiz Answers in the Shopify Orders

It's possible to know exactly which orders in your Shopify Orders tab come from the quiz.

=== "Shopify"

    In the `💎Built for Shopify` version of the app, quiz data can be passed to Shopify orders using **custom JavaScript**. This gives you full control over which values are saved to the cart and carried through to the order.

    1. Add your custom code to the relevant [question](/reference/quiz-builder/questions/#question-settings) or [results page](/reference/quiz-builder/results-page/#custom-js-code) using the [How to Add JavaScript](/how-to-guides/add-javascript/) guide.
    2. Use `actions.updateCartAttributes({...})` to write the values you want to store on the cart.
    3. Click `Save` to update the live quiz.
    4. Test the flow on your storefront by taking the quiz, adding products to the cart, and placing a test order.

    !!! info "Choose exactly what to save"

        The `💎Built for Shopify` version does **not** automatically write every quiz answer into Shopify order notes.

        Instead, you choose which values to pass through checkout. This is useful when you only want to save a result name, score, response ID, campaign tag, or a few selected answers.

    **Example:** save the response ID, result reference, and a custom segment tag on the results page.

    ```javascript
    if (quiz.metadata.isStoreRenderer && !quiz.metadata.inBuilder) {
      await actions.updateCartAttributes({
        __quiz_response_id: quiz.metadata.responseId,
        __result_ref: quiz.currentResult?.ref || '',
        skincare_segment: quiz.variables.highest || ''
      });
    }
    ```

    !!! tip "Hidden and visible cart attributes"

        Use the `__` prefix when you want to save an internal value on the cart without showing it as a normal storefront cart attribute.

        Leave the prefix off when you want the value to stay visible in Shopify cart or order surfaces.

    !!! warning

        Cart attributes are written only when the shopper reaches the page where your custom JavaScript runs. If you need the data before checkout, add the code to the question or result page that appears before the shopper goes to the cart.

    !!! warning

        Shopify Revenue Tracking and cart-based order tagging only work if the customer adds products to the cart directly from the quiz results page **AND** then proceeds through checkout without breaking the flow. If they purchase later, the order may no longer be attributed to the quiz.

        Make sure your Results Page Checkout settings are correctly set to `proceed to cart` (not `proceed to checkout` or `link to product`). To change your checkout settings, check [this guide](/how-to-guides/change-checkout-settings/).

=== "Shopify (Legacy)"

    1. Make sure your quiz is connected to [Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/) and that you've [enabled Order Notes](https://help.shopify.com/en/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/get-more-information-with-order-notes) in your Shopify Theme.
    2. To activate Shopify Orders Tagging option navigate to the `Connect` tab in the quiz and scroll down to find `Shopify Orders Tagging` tab.
    3. To allow the quiz to add tags and question answers to your orders, simply click `connect`.
    4. Make sure to `Publish` the quiz in the top right corner.

    From that moment all the orders under the Shopify Orders list will display a small `Notes` section with the tags related to the quiz.

    ![how to show quiz answers on orders example1](/images/how_to_show_quiz_answers_on_orders_example1.png)

    You can freely edit the content of that section by clicking `Edit` and adding your changes.

    ![how to show quiz answers on orders example3](/images/how_to_show_quiz_answers_on_orders_example3.png)

    !!! warning

        Some Shopify themes disable the passing of tags to the orders. These themes should have the option to activate this feature in the theme settings manually.


    !!! warning

        Shopify Revenue Tracking and Orders Tagging only works if the customer adds the products to the cart directly from the quiz results page **AND** if they immediately proceed to the cart after the quiz, and then right away complete the purchase. If they purchase at a later date, this revenue will not be attributed to the quiz anymore.
             
        Make sure your Results Page Checkout settings are correctly set to `proceed to cart` (not `proceed to checkout` or `link to product`). To change your checkout settings, check [this guide](/how-to-guides/change-checkout-settings/).

=== "WooCommerce"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

=== "Magento"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

=== "BigCommerce"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

=== "Standalone"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

## Testing the Connection

=== "Shopify"

    If the cart or order tagging is not working as expected, try the following:

    1. Open the question or results page where you added the custom JavaScript and confirm the code is saved.
    2. Make sure the code uses `actions.updateCartAttributes({...})` and runs before the customer leaves for the cart or checkout.
    3. Open the **live storefront quiz** in a different browser or incognito window (don't test on preview/admin.revenuehunt).
    4. Add a temporary `console.log('tagging cart')` line to your code and check the browser console to confirm the script runs.
    5. Take the quiz, add products to cart, and place a valid [Shopify test order](https://help.shopify.com/en/manual/checkout-settings/test-orders).
    6. Check the created order in Shopify and review which cart/order attributes were passed through checkout.

    If you're still having issues, please reach out to our [support team](/how-to-guides/contact-customer-support/) and include:

    - your quiz URL
    - the custom JavaScript you used
    - which values you expected to save
    - a screenshot of the order or cart result

=== "Shopify (Legacy)"

    If you believe the orders tagging is not working as it should, try to following steps:

    1. Go to the `Connect` tab and disconnect the quiz from **Shopify Customers** and **Shopify Orders Tagging**. Then, publish the changes with the top-right `Publish` button. 
    2. Connect the quiz again to these tools and (again) publish the changes with the top-right `Publish` button. That should reset the connection.
    3. Use a different browser or incognito browsing mode to open the live quiz on your site (don't test on preview/admin.revenuehunt).
    4. Take the quiz all the way to the results, provide the same email in the quiz that will be used for checkout/placing an order. Good idea is using *yourrealemail+test1@youremail.com* for example. 
    5. Add all the products to cart and proceed to cart, then checkout.
    6. Place a valid test order (as explained [here](https://help.shopify.com/en/manual/checkout-settings/test-orders)).
    7. Check if the lead was added to **Shopify Customers** section and if it was marked with `RevenueHunt` in the details.
    8. Go to **Shopify Orders** and check if the order notes appear along the test order placed. 

    If you're still having issues, please reach out to our [support team](/how-to-guides/contact-customer-support/).

=== "WooCommerce"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

=== "Magento"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

=== "BigCommerce"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

=== "Standalone"

    This feature is currently only available for the `💎Built for Shopify` version of the RevenueHunt app and the Legacy version of the app for Shopify.

---

This article explains how to show quiz answers in the Shopify Orders.
