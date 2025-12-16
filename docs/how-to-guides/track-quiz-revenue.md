---
icon: material/cash-multiple
---

# How to Track Quiz Revenue

Understanding the revenue generated from quizzes on your eCommerce store can provide valuable insights into customer engagement and the effectiveness of your marketing strategies. 

This documentation outlines how to track quiz analytics and revenue generated from quizzes in the Revenue Hunt app.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/feGUgS0rzUQ?si=liZIQ0at-9EJ3tkr" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The RevenueHunt app automatically connects to Shopify orders when installed on your store, so no manual connection is required.

    Follow the steps below to track quiz revenue in the new Built for Shopfiy version of RevenueHunt app:

    1. **Open the Analytics tab**: Open the RevenueHunt app and navigate to the [Analytics](/reference/quiz-builder/metrics/#analytics) tab.
    2. **Select a quiz and time period**: Select a specific quiz and set the desired time period (e.g., last 30 days) by clicking on the today icon.

        In the analytics section, you can view by default:

        ![how to track revenue report metrics](/images/manual_shopifyV2_quizbuilder_metrics_analytics.png)

        - Total quiz responses
        - Number of orders resulting from the quiz
        - Total value of these orders

        !!! tip
            To see more data, like the `Average order value`, `Number of carts` or simialr, you can [customize the analytics dashboard](/reference/quiz-builder/metrics/#customize).

    3. **View quiz-attributed orders**: All orders and their values resulting from quiz responses will be automatically tracked and marked in the Shopify Orders tab.
        
        ![how to show quiz answers on orders example1](/images/how_to_show_quiz_answers_on_orders_example1.png)
    
    
    4. In [Quiz Analytics](/reference/quiz-builder/metrics/#analytics), you can see the number of orders and total order value attributed to the quiz.

        ![manual_shopifyV2_quizbuilder_metrics_analytics_totordersvalue](/images/manual_shopifyV2_quizbuilder_metrics_analytics_totordersvalue.png)


    !!! tip "Track Revenue with Google Analytics"

        You can also track quiz revenue alongside other metrics with [Google Analytics](/how-to-guides/integrate-google-analytics/).

        ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

        [:fontawesome-solid-arrow-right: learn more](/how-to-guides/integrate-google-analytics/)


=== "Shopify (Legacy)"

    The [**Shopify Revenue Report**](#activate-shopify-revenue-report) feature within the RevenueHunt app allows you to track orders tagged by your quiz, offering a clear view of its impact on sales. 

    This how-to article guides you through the process of setting up your Shopify Revenue Report and accessing vital orders data from the quiz.

    Alternatively, you can track quiz revenue with [Google Analytics](/how-to-guides/integrate-google-analytics/).

    ## Activate Shopify Revenue Report

    To enable the automated revenue report feature:

    1. **Enable Order Notes**: You need to enable Order Notes in your Theme Settings for this feature to work. Follow [these instructions](https://help.shopify.com/en/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/get-more-information-with-order-notes) to enable them or contact your theme developer.
    2. **Open the Connect tab**: Open the RevenueHunt app and navigate to the [Connect](/reference/quiz-builder/connect-integrations/) tab.
    3. **Conect to Shopify Reprots**: Scroll down to find the **Shopify Revenue Report** section. Click on the `Connect` button within the Shopify Revenue Report section.
    4. **Give consent**: The system will ask for your consent to access orders. Once accepted, it will establish a connection between the RevenueHunt app and your Shopify account, allowing the app to start gathering order data tagged by the quiz.
    5. **Publish the changes**: Click on the top-right `Publish` button to updated the quiz preview/live quiz and save the changes.

    After the connection is successfully established, you can access the revenue data generated from your quizzes. Go to the [`Metrics > Analytics`](/reference/quiz-builder/metrics/#analytics) section within the RevenueHunt app. Here, you will find the following information:

    ![how to track revenue report metrics](/images/how_to_track_revenue_report_metrics.png)

    - **Number of Orders**: Displays the number of people who placed an order after completing the quiz.
    - **Total Orders Value**: Shows the total value of all orders placed following quiz completion.
    - **Avg. Order Value**: Indicates the average value of orders placed post-quiz.

    !!! warning

         Shopify Revenue Tracking and Orders Tagging only works if the customer adds the products to the cart directly from the quiz results page **AND** if they immediately proceed to the cart after the quiz, and then right away complete the purchase. If they purchase at a later date, this revenue will not be attributed to the quiz anymore.
         
         Make sure your Results Page Checkout settings are correctly set to `proceed to cart` (not `proceed to checkout` or `link to product`). To change your checkout settings, check [this guide](/how-to-guides/change-checkout-settings/).

    ## Tracking Revenue with Google Analytics

    For a more detailed analysis you can track quiz revenue alongside other metrics with [Google Analytics](/how-to-guides/integrate-google-analytics/).

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/integrate-google-analytics/)

    ## Show Quiz Answers in the Shopify Orders

    It’s possible to know exactly which orders in your Shopify Orders tab come from the quiz.

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/show-quiz-answers-in-orders/)

=== "WooCommerce"

    You can track quiz revenue alongside other metrics with [Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/integrate-google-analytics/)

=== "Magento"

    You can track quiz revenue alongside other metrics with [Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/integrate-google-analytics/)
    
=== "BigCommerce"

    You can track quiz revenue alongside other metrics with [Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/integrate-google-analytics/)

=== "Standalone"

    You can track quiz revenue alongside other metrics with [Google Analytics](/how-to-guides/integrate-google-analytics/).

    ![how to show revenue in google analytics](/images/how_to_ga_revenue2.png)

    [:fontawesome-solid-arrow-right: learn more](/how-to-guides/integrate-google-analytics/)


!!! tip "Learn which meterics to track"

    Check out [this customer success article](/customer-success/track-quiz-metrics-for-better-conversions/) to learn which metrics to track to convert better.

---

This article explains how to track quiz revenue in the Revenue Hunt app.

By following these steps, you can monitor the revenue attributed to your quizzes, helping you to measure their success and optimize future campaigns.