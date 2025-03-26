# How to Show Quiz Answers in the Shopify Orders

It’s possible to know exactly which orders in your Shopify Orders tab come from the quiz.

1. Make sure your quiz is connected to [Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/) and that you've [enabled Order Notes](https://help.shopify.com/en/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/get-more-information-with-order-notes) in your Shopify Theme.
2. To activate Shopify Orders Tagging option navigate to the `Connect` tab in the quiz and scroll down to find `Shopify Orders Tagging (Beta)` tab.
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


## Testing the Connection

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
