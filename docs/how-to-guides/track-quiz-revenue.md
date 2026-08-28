---
icon: material/cash-multiple
description: "Track RevenueHunt quiz analytics and revenue metrics to measure ecommerce store performance and ROI."
---

# How to Track Quiz Revenue

See how many orders your quiz produced, and what they were worth. The app attributes an order to the quiz when the customer reaches checkout from the results page.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/feGUgS0rzUQ?si=liZIQ0at-9EJ3tkr" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The app connects to Shopify orders the moment it is installed. There is nothing to connect by hand.

    1. **Open the [Analytics](/reference/quiz-builder/metrics/#analytics) tab in the app.**

    2. **Select a quiz.**

    3. **Set the time period with the today icon.** For example, the last 30 days.

        ![how to track revenue report metrics](/images/manual_shopifyV2_quizbuilder_metrics_analytics.png)

        The panel shows the total quiz responses, the number of orders that came from the quiz, and what those orders were worth.

        !!! tip "Adding more figures"

            `Average order value`, `Number of carts` and others are available. See [how to customize the analytics dashboard](/reference/quiz-builder/metrics/#customize).

    4. **Read the orders and their total value in [Quiz Analytics](/reference/quiz-builder/metrics/#analytics).**

        ![manual_shopifyV2_quizbuilder_metrics_analytics_totordersvalue](/images/manual_shopifyV2_quizbuilder_metrics_analytics_totordersvalue.png)

    Every order that came from a quiz response is also marked in the Shopify Orders tab.

    ![how to show quiz answers on orders example1](/images/how_to_show_quiz_answers_on_orders_example1.png)

    !!! tip "The same revenue in Google Analytics"

        Quiz revenue can sit alongside your other metrics in GA4. See [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

        ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

=== "Shopify (Legacy)"

    The **Shopify Revenue Report** tracks the orders your quiz tagged, so you can see what it contributed to sales.

    1. **Enable Order Notes in your theme settings.** The report cannot work without them. Follow [Shopify's instructions](https://help.shopify.com/en/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/get-more-information-with-order-notes), or ask your theme developer.

    2. **Open the [Connect](/reference/quiz-builder/connect-integrations/) tab in the app.**

    3. **Scroll to `Shopify Revenue Report` and click `Connect`.**

    4. **Give consent to access orders.** That connects the app to your Shopify account, and it starts collecting the order data your quiz tagged.

    5. **Click the top-right `Publish` button.** This saves the changes and updates the preview and the live quiz.

    The revenue then appears in [`Metrics > Analytics`](/reference/quiz-builder/metrics/#analytics):

    ![how to track revenue report metrics](/images/how_to_track_revenue_report_metrics.png)

    - **Number of Orders**: how many people ordered after finishing the quiz.
    - **Total Orders Value**: what all of those orders were worth together.
    - **`Avg. Order Value`**: the average value of an order placed after the quiz.

    !!! warning "Attribution needs an unbroken flow"

        Shopify Revenue Tracking and Orders Tagging need an unbroken flow. The customer has to add products to the cart from the results page, then complete the checkout. An order placed later is no longer attributed to the quiz.

        Set the Checkout settings on your Results Page to `proceed to cart`, not `proceed to checkout` or `link to product`. See [How to Change Checkout Settings on Your Results Page](/how-to-guides/change-checkout-settings/).

    !!! tip "The same revenue in Google Analytics"

        For a more detailed breakdown, see [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

    To see which orders in the Shopify Orders tab came from the quiz, see [How to Show Quiz Answers in Shopify Orders](/how-to-guides/show-quiz-answers-in-orders/).

=== "WooCommerce"

    Track quiz revenue alongside your other metrics in GA4. See [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

=== "Magento"

    Track quiz revenue alongside your other metrics in GA4. See [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

=== "BigCommerce"

    Track quiz revenue alongside your other metrics in GA4. See [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

=== "Standalone"

    Track quiz revenue alongside your other metrics in GA4. See [How to Track Quiz Performance with Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

!!! tip "Which metrics are worth watching"

    See [Product Quiz Metrics: What to Track to Convert Better](/customer-success/track-quiz-metrics-for-better-conversions/).

---

This article explains how to track the revenue your quiz produced in the RevenueHunt app.
