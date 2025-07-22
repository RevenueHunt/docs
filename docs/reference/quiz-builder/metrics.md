# Metrics

=== "Shopify"

    In the Metrics section of the Quiz Builder, you can find individual quiz responses and analytics.

=== "Shopify V2"

    In the Metrics section of the Quiz Builder, you can find individual quiz responses and analytics.

=== "WooCommerce"

    In the Metrics section of the Quiz Builder, you can find individual quiz responses and analytics.

=== "Magento"

    In the Metrics section of the Quiz Builder, you can find individual quiz responses and analytics.

=== "BigCommerce"

    In the Metrics section of the Quiz Builder, you can find individual quiz responses and analytics.

=== "Standalone"

    In the Metrics section of the Quiz Builder, you can find individual quiz responses and analytics.

## Responses

=== "Shopify"

    ![quiz builder metrics responses](/images/manual_quizbuilder_metrics_responses.png)

    On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.

    `Export all as CSV` - Click to generate a CSV file with all the quiz responses from the last 90 days. Once ready, a downloadable link will show up on your dashboard once the CSV file is finished generating.

    ![quiz builder metrics responses details1](/images/manual_quizbuilder_metrics_responses_details1.png)

    `Why was a product recommended or not in this response?` - This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

    `SELECT PRODUCT TO CHECK` - Click to select a product from the catalog and analyze it against the response.

    `Responses to Questions` - This section displays all the quiz questions, the answers the customer provided and the products/collections that were upvoted or excluded in each question.

    ![quiz builder metrics responses details2 products](/images/manual_quizbuilder_metrics_responses_details2_products.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Products` - Products were recommended in a Product block.

    `↑1 🎁6` - Minimum number of votes that allow the product to be shown in this product block: 1; Maximum number of products that are allowed to be shown in this product block: 6.

    `Kopi Luwak Coffee` / `Product name` - Displays the name of the product recommended in this product block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details2 slots](/images/manual_quizbuilder_metrics_responses_details2_slots.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Slots` - Products were recommended in a Slots block.

    `Step 1: Cleanser` / `Slot Title` - Displays the title of the Slot block.

    `↑1 🎁1` - Minimum number of votes that allow the product to be shown in this slots block: 1; Maximum number of products that are allowed to be shown in this slots block: 1.

    `✅5` - Displays which products this slot will allow to be displayed.

    `Cleansers (5)` / `Collection (x)` - Displays the collections which are linked to this slot.

    `All Natural Face Cleanser` - Displays the name of the product recommended in this slot block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details3](/images/manual_quizbuilder_metrics_responses_details3.png)

    `Customer Tags` - Displays the customer tags that were recorded in this response.

    `Preview Results` - Displays a preview link which opens this response on the results page.

    `recalculate recommendations` - Recalculate the responses according to the current quiz setup.

    `resend notifications` - Triggers the response again, which results in all the data being re-sent. This will cause the emails or data redirections to integrations to be triggered again.

=== "Shopify V2"

    To open the responses sections, go back to the [dashboard](/reference/dashboard/). 

    Pick a quiz and click the `...` to open the quiz menu. 

    From the list pick and click on `Responses`.

    ![manual_shopifyV2_quizbuilder_openresponses](/images/manual_shopifyV2_quizbuilder_openresponses.png)

    In the Responses section you will find a list of the latest quiz responses sorted by date.

    ![manual_shopifyV2_quizbuilder_responses](/images/manual_shopifyV2_quizbuilder_responses.png)

    `All` / `With recommendations` / `No recommendations` - Switch to filter responses that recieved product recommendations and those that did not.
    
    `Export CSV` - Download the selected responses in a CSV file format.

    `Response date` - The date and time the response has been submitted.

    `Type` - The type of quiz response, eg. `Preview` or `Customer`. Preview responses are created when you click the `Preview` button in the quiz builder. Customer responses are created when a customer completes the quiz on the live site.

    `Name` - Name provided by the quiz taker.

    `Email` - Email provided by the quiz taker.

    `Recommendations` - The number of recommended products.

    `View` - Click to open the response details.

    ![manual_shopifyV2_quizbuilder_responses_viewmenu](/images/manual_shopifyV2_quizbuilder_responses_viewmenu.png)

    `View response` - Click to open the response in a new tab.

    `Debug mode` - Click to open the response in debug mode.

    `Analysis` - Click to open the response analysis page.

    ### Response analysis

    Each response analysis page displays the following sections:

    ![manual_shopifyV2_quizbuilder_responses_sample1](/images/manual_shopifyV2_quizbuilder_responses_sample1.png)

    `Analyze response` - Click to open the [Quiz Copilot](/how-to-guides/use-quiz-copilot/) chat window. The Copilot will ask you the following question: *"I can help you analyze this quiz response. What seems to be the issue? You can select a common question below or type your own."* and once you reply it will provide a detailed analysis of the response, help you identify the root cause of the issue and suggest improvements.

    **Responses to questions** - Displays all the quiz questions, the answers the customer provided and the products/collections that were upvoted or excluded in each question. Click `▼` on a question to expand it and check the details.

    ![manual_shopifyV2_quizbuilder_responses_sample2](/images/manual_shopifyV2_quizbuilder_responses_sample2.png)

    **Why was a product recommended or not in this response?** - This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

    `v Select item to check` - Click to select a product from the catalog and analyze it against the response. Choose an item below to know why it was recommended or not.

    ![manual_shopifyV2_quizbuilder_responses_sample1_checkproduct](/images/manual_shopifyV2_quizbuilder_responses_sample1_checkproduct.png)

    `Contact information` - Displays the contact information provided by the customer in the quiz such as name, email, phone number, etc.

    `Customer Tags` - Displays the customer tags associated with this response. Customer tags help you understand your customer's needs, as well as helping with segmentation and retargeting.

    **Result: Results page 1** - - Displays the name of the results page recommended. This screen displays the configuration of a Result Section and explains what was shown to the customer and why.

    ![manual_shopifyV2_quizbuilder_responses_sample2_productdetails](/images/manual_shopifyV2_quizbuilder_responses_sample2_productdetails.png)

    **Section Overview**

    `Section Title` - Displays the name of the section recommended.

    `Section Ref` - Internal reference used to identify the section.


    **Display logic**

    `Show more details` - click to expand the display logic section.

    `Default visibility` - `Visible` or `Hidden` - The section explains if the section was shown or not.

    `Conditional Logic` - This section explains if the section was shown based on the quiz logic.

    `Conditions` - Explains why the section was shown or hidden based on the quiz logic.


    **Section blocks with slots** - Displays the blocks with slots in detail. Each section can include one or more blocks.

    `Block Ref` - Internal reference used to identify the block.

    `Block Type` - `Products` or `Collections` or `Text` - This block explains the block type.

    `Minimum Upvotes` - The minimum number of upvotes a product must receive to be shown in the block.

    `Recommendation System` - `Fixed recommendations` or `Based on customer responses` - This explains if the recommendations are fixed or dynamic.

    **Slots in Detail** - Displays the slots in detail. Each block contains one or more slots, which define which products are shown and how they are selected:

    `Slot Ref` - Internal reference used to identify the slot.

    `Fixed Items` -  Exlpains that the recommendations are fixed in this slot and shows which products were selected.

    `Recommendations` - Final products shown to the user.


=== "WooCommerce"

    ![manual_woo_quizbuilder_metrics_responses](/images/manual_woo_quizbuilder_metrics_responses.png)

    On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.

    `Export all as CSV` - Click to generate a CSV file with all the quiz responses from the last 90 days. Once ready, a downloadable link will show up on your dashboard once the CSV file is finished generating.

    ![quiz builder metrics responses details1](/images/manual_quizbuilder_metrics_responses_details1.png)

    `Why was a product recommended or not in this response?` - This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

    `SELECT PRODUCT TO CHECK` - Click to select a product from the catalog and analyze it against the response.

    `Responses to Questions` - This section displays all the quiz questions, the answers the customer provided and the products/collections that were upvoted or excluded in each question.

    ![quiz builder metrics responses details2 products](/images/manual_quizbuilder_metrics_responses_details2_products.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Products` - Products were recommended in a Product block.

    `↑1 🎁6` - Minimum number of votes that allow the product to be shown in this product block: 1; Maximum number of products that are allowed to be shown in this product block: 6.

    `Kopi Luwak Coffee` / `Product name` - Displays the name of the product recommended in this product block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details2 slots](/images/manual_quizbuilder_metrics_responses_details2_slots.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Slots` - Products were recommended in a Slots block.

    `Step 1: Cleanser` / `Slot Title` - Displays the title of the Slot block.

    `↑1 🎁1` - Minimum number of votes that allow the product to be shown in this slots block: 1; Maximum number of products that are allowed to be shown in this slots block: 1.

    `✅5` - Displays which products this slot will allow to be displayed.

    `Cleansers (5)` / `Collection (x)` - Displays the collections which are linked to this slot.

    `All Natural Face Cleanser` - Displays the name of the product recommended in this slot block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details3](/images/manual_quizbuilder_metrics_responses_details3.png)

    `Customer Tags` - Displays the customer tags that were recorded in this response.

    `Preview Results` - Displays a preview link which opens this response on the results page.

    `recalculate recommendations` - Recalculate the responses according to the current quiz setup.

    `resend notifications` - Triggers the response again, which results in all the data being re-sent. This will cause the emails or data redirections to integrations to be triggered again.

=== "Magento"

    ![manual_standalone_quizbuilder_metrics_responses](/images/manual_standalone_quizbuilder_metrics_responses.png)

    On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.

    `Export all as CSV` - Click to generate a CSV file with all the quiz responses from the last 90 days. Once ready, a downloadable link will show up on your dashboard once the CSV file is finished generating.

    ![quiz builder metrics responses details1](/images/manual_quizbuilder_metrics_responses_details1.png)

    `Why was a product recommended or not in this response?` - This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

    `SELECT PRODUCT TO CHECK` - Click to select a product from the catalog and analyze it against the response.

    `Responses to Questions` - This section displays all the quiz questions, the answers the customer provided and the products/collections that were upvoted or excluded in each question.

    ![quiz builder metrics responses details2 products](/images/manual_quizbuilder_metrics_responses_details2_products.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Products` - Products were recommended in a Product block.

    `↑1 🎁6` - Minimum number of votes that allow the product to be shown in this product block: 1; Maximum number of products that are allowed to be shown in this product block: 6.

    `Kopi Luwak Coffee` / `Product name` - Displays the name of the product recommended in this product block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details2 slots](/images/manual_quizbuilder_metrics_responses_details2_slots.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Slots` - Products were recommended in a Slots block.

    `Step 1: Cleanser` / `Slot Title` - Displays the title of the Slot block.

    `↑1 🎁1` - Minimum number of votes that allow the product to be shown in this slots block: 1; Maximum number of products that are allowed to be shown in this slots block: 1.

    `✅5` - Displays which products this slot will allow to be displayed.

    `Cleansers (5)` / `Collection (x)` - Displays the collections which are linked to this slot.

    `All Natural Face Cleanser` - Displays the name of the product recommended in this slot block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details3](/images/manual_quizbuilder_metrics_responses_details3.png)

    `Customer Tags` - Displays the customer tags that were recorded in this response.

    `Preview Results` - Displays a preview link which opens this response on the results page.

    `recalculate recommendations` - Recalculate the responses according to the current quiz setup.

    `resend notifications` - Triggers the response again, which results in all the data being re-sent. This will cause the emails or data redirections to integrations to be triggered again.

=== "BigCommerce"

    ![manual_standalone_quizbuilder_metrics_responses](/images/manual_standalone_quizbuilder_metrics_responses.png)

    On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.

    `Export all as CSV` - Click to generate a CSV file with all the quiz responses from the last 90 days. Once ready, a downloadable link will show up on your dashboard once the CSV file is finished generating.

    ![quiz builder metrics responses details1](/images/manual_quizbuilder_metrics_responses_details1.png)

    `Why was a product recommended or not in this response?` - This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

    `SELECT PRODUCT TO CHECK` - Click to select a product from the catalog and analyze it against the response.

    `Responses to Questions` - This section displays all the quiz questions, the answers the customer provided and the products/collections that were upvoted or excluded in each question.

    ![quiz builder metrics responses details2 products](/images/manual_quizbuilder_metrics_responses_details2_products.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Products` - Products were recommended in a Product block.

    `↑1 🎁6` - Minimum number of votes that allow the product to be shown in this product block: 1; Maximum number of products that are allowed to be shown in this product block: 6.

    `Kopi Luwak Coffee` / `Product name` - Displays the name of the product recommended in this product block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details2 slots](/images/manual_quizbuilder_metrics_responses_details2_slots.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Slots` - Products were recommended in a Slots block.

    `Step 1: Cleanser` / `Slot Title` - Displays the title of the Slot block.

    `↑1 🎁1` - Minimum number of votes that allow the product to be shown in this slots block: 1; Maximum number of products that are allowed to be shown in this slots block: 1.

    `✅5` - Displays which products this slot will allow to be displayed.

    `Cleansers (5)` / `Collection (x)` - Displays the collections which are linked to this slot.

    `All Natural Face Cleanser` - Displays the name of the product recommended in this slot block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details3](/images/manual_quizbuilder_metrics_responses_details3.png)

    `Customer Tags` - Displays the customer tags that were recorded in this response.

    `Preview Results` - Displays a preview link which opens this response on the results page.

    `recalculate recommendations` - Recalculate the responses according to the current quiz setup.

    `resend notifications` - Triggers the response again, which results in all the data being re-sent. This will cause the emails or data redirections to integrations to be triggered again.

=== "Standalone"

    ![manual_standalone_quizbuilder_metrics_responses](/images/manual_standalone_quizbuilder_metrics_responses.png)

    On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.

    `Export all as CSV` - Click to generate a CSV file with all the quiz responses from the last 90 days. Once ready, a downloadable link will show up on your dashboard once the CSV file is finished generating.

    ![quiz builder metrics responses details1](/images/manual_quizbuilder_metrics_responses_details1.png)

    `Why was a product recommended or not in this response?` - This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

    `SELECT PRODUCT TO CHECK` - Click to select a product from the catalog and analyze it against the response.

    `Responses to Questions` - This section displays all the quiz questions, the answers the customer provided and the products/collections that were upvoted or excluded in each question.

    ![quiz builder metrics responses details2 products](/images/manual_quizbuilder_metrics_responses_details2_products.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Products` - Products were recommended in a Product block.

    `↑1 🎁6` - Minimum number of votes that allow the product to be shown in this product block: 1; Maximum number of products that are allowed to be shown in this product block: 6.

    `Kopi Luwak Coffee` / `Product name` - Displays the name of the product recommended in this product block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details2 slots](/images/manual_quizbuilder_metrics_responses_details2_slots.png)

    `Results Page 1` - Displays the name of the results page recommended.

    `Slots` - Products were recommended in a Slots block.

    `Step 1: Cleanser` / `Slot Title` - Displays the title of the Slot block.

    `↑1 🎁1` - Minimum number of votes that allow the product to be shown in this slots block: 1; Maximum number of products that are allowed to be shown in this slots block: 1.

    `✅5` - Displays which products this slot will allow to be displayed.

    `Cleansers (5)` / `Collection (x)` - Displays the collections which are linked to this slot.

    `All Natural Face Cleanser` - Displays the name of the product recommended in this slot block. Hover over the product to see how many upvotes it received in the quiz.

    ![quiz builder metrics responses details3](/images/manual_quizbuilder_metrics_responses_details3.png)

    `Customer Tags` - Displays the customer tags that were recorded in this response.

    `Preview Results` - Displays a preview link which opens this response on the results page.

    `recalculate recommendations` - Recalculate the responses according to the current quiz setup.

    `resend notifications` - Triggers the response again, which results in all the data being re-sent. This will cause the emails or data redirections to integrations to be triggered again.

## Analytics

=== "Shopify"

    ![quiz builder metrics analytics](/images/manual_quizbuilder_metrics_analytics.png)

    The data in the graphs are totals in a selected period of time for a selected quiz. 

    ![quiz builder metrics analytics dates](/images/manual_quizbuilder_metrics_analytics_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    **Compare:** - Choose how you want to compare the data in the graphs. 

    `Part Period` - Presents data against the values from previous 30 days.

    `Quiz` - Choose a quiz name against which you want to compare the metrics against.

    **Quiz Starts** / **Starts** - Number of people who have engaged with the quiz and have passed the first slide (clicked on the “start quiz” button or answered the first question). 

    ![quiz builder metrics analytics starts](/images/manual_quizbuilder_metrics_analytics_starts.png)

    `Quiz Responses` / `Responses` - Number of people who have completed the quiz. Test responses (completed via the Test quiz button) are deleted from your metrics after one hour.

    ![quiz builder metrics analytics responses](/images/manual_quizbuilder_metrics_analytics_responses.png)

    `Completion Rate` / `Comp. Rate` - Percentage of people who have engaged with the quiz and completed it.

    ![quiz builder metrics analytics completion rate](/images/manual_quizbuilder_metrics_analytics_comprate.png)

    `Carts Count` / `Num. Carts` - Number of people who have selected products and clicked on the “proceed to cart” or “proceed to checkout” button.

    ![quiz builder metrics analytics carts count](/images/manual_quizbuilder_metrics_analytics_cartscount.png)

    `Avg. Cart Value` - Average value of the products included in the carts or checkouts.

    ![quiz builder metrics analytics average carts](/images/manual_quizbuilder_metrics_analytics_avgcarts.png)

    `Total Carts Value` - Total value of the products included in all the carts or checkouts. This does not represent the total value of purchases since you should expect some drop-off at checkout.

    ![quiz builder metrics analytics total carts](/images/manual_quizbuilder_metrics_analytics_totalcarts.png)

    `Number of Orders (Beta)` - Number of people who have placed an order after completing this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Total Orders Value (Beta)` - Total value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Avg. Order Value (Beta)` - Average value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

=== "Shopify V2"

    Access the Analytics from the [Dashboard](/reference/dashboard/). You can open the Analytics tab from the Shopify side menu.

    ![manual_shopifyV2_quizbuilder_matrics_analytics_accessfromdashboard_sidemenu](/images/manual_shopifyV2_quizbuilder_matrics_analytics_accessfromdashboard_sidemenu.png)
    
    or pick a quiz and click the  `...` to open the quiz menu. From the list pick and click on `Analytics`.

    ![manual_shopifyV2_quizbuilder_matrics_analytics_accessfromdashboard1](/images/manual_shopifyV2_quizbuilder_matrics_analytics_accessfromdashboard1.png)

    The Analytics tab will open with the data for the selected quiz.

    ![manual_shopifyV2_quizbuilder_metrics_analytics](/images/manual_shopifyV2_quizbuilder_metrics_analytics.png)

    The data in the graphs are totals in a selected period of time for a selected quiz. 

    Click the `Quiz name` to change the quiz.

    `Today` / `Last 90 days` - To change the dates click on the `Today`/ `Last 90 days` button. You can change the period to select it from the moment you started using the quiz or from a given date.

    `No comparison` - Choose how you want to compare the data in the graphs. 

    `Auto-refresh` - The data will refresh ever 60 seconds. Otherwise, the data is updated every 24 hours.

    `Quiz Starts` - Number of people who have engaged with the quiz and have passed the first slide (clicked on the “start quiz” button or answered the first question). 

    `Quiz Responses` - Number of people who have completed the quiz. Test responses (completed via the Test quiz button) are deleted from your metrics after one hour.

    `Numer of carts` - Number of people who have selected products and clicked on the “proceed to cart” or “proceed to checkout” button.

    `Total carts value` - Total value of the products included in all the carts or checkouts. This does not represent the total value of purchases since you should expect some drop-off at checkout.

    `Number of orders` - Number of people who have placed an order after completing this quiz. 

    `Total orders value` - Total value of orders placed after taking this quiz.

    !!! warning "Note"

        To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Customers via the [Integrations](https://docs.revenuehunt.com/how-to-guides/send-leads-to-shopify-customers/) tab.

=== "WooCommerce"

    ![manual_woo_quizbuilder_metrics_analytics](/images/manual_woo_quizbuilder_metrics_analytics.png)

    The data in the graphs are totals in a selected period of time for a selected quiz. 

    ![quiz builder metrics analytics dates](/images/manual_quizbuilder_metrics_analytics_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    **Compare:** - Choose how you want to compare the data in the graphs. 

    `Part Period` - Presents data against the values from previous 30 days.

    `Quiz` - Choose a quiz name against which you want to compare the metrics against.

    `Quiz Starts` / `Starts` - Number of people who have engaged with the quiz and have passed the first slide (clicked on the “start quiz” button or answered the first question). 

    ![quiz builder metrics analytics starts](/images/manual_quizbuilder_metrics_analytics_starts.png)

    `Quiz Responses` / `Responses` - Number of people who have completed the quiz. Test responses (completed via the Test quiz button) are deleted from your metrics after one hour.

    ![quiz builder metrics analytics responses](/images/manual_quizbuilder_metrics_analytics_responses.png)

    `Completion Rate` / `Comp. Rate` - Percentage of people who have engaged with the quiz and completed it.

    ![quiz builder metrics analytics completion rate](/images/manual_quizbuilder_metrics_analytics_comprate.png)

    `Carts Count` / `Num. Carts` - Number of people who have selected products and clicked on the “proceed to cart” or “proceed to checkout” button.

    ![quiz builder metrics analytics carts count](/images/manual_quizbuilder_metrics_analytics_cartscount.png)

    `Avg. Cart Value` - Average value of the products included in the carts or checkouts.

    ![quiz builder metrics analytics average carts](/images/manual_quizbuilder_metrics_analytics_avgcarts.png)

    `Total Carts Value` - Total value of the products included in all the carts or checkouts. This does not represent the total value of purchases since you should expect some drop-off at checkout.

    ![quiz builder metrics analytics total carts](/images/manual_quizbuilder_metrics_analytics_totalcarts.png)

    `Number of Orders (Beta)` - Number of people who have placed an order after completing this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Total Orders Value (Beta)` - Total value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Avg. Order Value (Beta)` - Average value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

=== "Magento"

    ![manual_standalone_quizbuilder_metrics_analytics](/images/manual_standalone_quizbuilder_metrics_analytics.png)

    The data in the graphs are totals in a selected period of time for a selected quiz. 

    ![quiz builder metrics analytics dates](/images/manual_quizbuilder_metrics_analytics_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    **Compare:** - Choose how you want to compare the data in the graphs. 

    `Part Period` - Presents data against the values from previous 30 days.

    `Quiz` - Choose a quiz name against which you want to compare the metrics against.

    `Quiz Starts` / `Starts` - Number of people who have engaged with the quiz and have passed the first slide (clicked on the “start quiz” button or answered the first question). 

    ![quiz builder metrics analytics starts](/images/manual_quizbuilder_metrics_analytics_starts.png)

    `Quiz Responses` / `Responses` - Number of people who have completed the quiz. Test responses (completed via the Test quiz button) are deleted from your metrics after one hour.

    ![quiz builder metrics analytics responses](/images/manual_quizbuilder_metrics_analytics_responses.png)

    `Completion Rate` / `Comp. Rate` - Percentage of people who have engaged with the quiz and completed it.

    ![quiz builder metrics analytics completion rate](/images/manual_quizbuilder_metrics_analytics_comprate.png)

    `Carts Count` / `Num. Carts` - Number of people who have selected products and clicked on the “proceed to cart” or “proceed to checkout” button.

    ![quiz builder metrics analytics carts count](/images/manual_quizbuilder_metrics_analytics_cartscount.png)

    `Avg. Cart Value` - Average value of the products included in the carts or checkouts.

    ![quiz builder metrics analytics average carts](/images/manual_quizbuilder_metrics_analytics_avgcarts.png)

    `Total Carts Value` - Total value of the products included in all the carts or checkouts. This does not represent the total value of purchases since you should expect some drop-off at checkout.

    ![quiz builder metrics analytics total carts](/images/manual_quizbuilder_metrics_analytics_totalcarts.png)

    `Number of Orders (Beta)` - Number of people who have placed an order after completing this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Total Orders Value (Beta)` - Total value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Avg. Order Value (Beta)` - Average value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

=== "BigCommerce"

    ![manual_standalone_quizbuilder_metrics_analytics](/images/manual_standalone_quizbuilder_metrics_analytics.png)

    The data in the graphs are totals in a selected period of time for a selected quiz. 

    ![quiz builder metrics analytics dates](/images/manual_quizbuilder_metrics_analytics_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    **Compare:** - Choose how you want to compare the data in the graphs. 

    `Part Period` - Presents data against the values from previous 30 days.

    `Quiz` - Choose a quiz name against which you want to compare the metrics against.

    `Quiz Starts` / `Starts` - Number of people who have engaged with the quiz and have passed the first slide (clicked on the “start quiz” button or answered the first question). 

    ![quiz builder metrics analytics starts](/images/manual_quizbuilder_metrics_analytics_starts.png)

    `Quiz Responses` / `Responses` - Number of people who have completed the quiz. Test responses (completed via the Test quiz button) are deleted from your metrics after one hour.

    ![quiz builder metrics analytics responses](/images/manual_quizbuilder_metrics_analytics_responses.png)

    `Completion Rate` / `Comp. Rate` - Percentage of people who have engaged with the quiz and completed it.

    ![quiz builder metrics analytics completion rate](/images/manual_quizbuilder_metrics_analytics_comprate.png)

    `Carts Count` / `Num. Carts` - Number of people who have selected products and clicked on the “proceed to cart” or “proceed to checkout” button.

    ![quiz builder metrics analytics carts count](/images/manual_quizbuilder_metrics_analytics_cartscount.png)

    `Avg. Cart Value` - Average value of the products included in the carts or checkouts.

    ![quiz builder metrics analytics average carts](/images/manual_quizbuilder_metrics_analytics_avgcarts.png)

    `Total Carts Value` - Total value of the products included in all the carts or checkouts. This does not represent the total value of purchases since you should expect some drop-off at checkout.

    ![quiz builder metrics analytics total carts](/images/manual_quizbuilder_metrics_analytics_totalcarts.png)

    `Number of Orders (Beta)` - Number of people who have placed an order after completing this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Total Orders Value (Beta)` - Total value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Avg. Order Value (Beta)` - Average value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

=== "Standalone"

    ![manual_standalone_quizbuilder_metrics_analytics](/images/manual_standalone_quizbuilder_metrics_analytics.png)

    The data in the graphs are totals in a selected period of time for a selected quiz. 

    ![quiz builder metrics analytics dates](/images/manual_quizbuilder_metrics_analytics_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    **Compare:** - Choose how you want to compare the data in the graphs. 

    `Part Period` - Presents data against the values from previous 30 days.

    `Quiz` - Choose a quiz name against which you want to compare the metrics against.

    `Quiz Starts` / `Starts` - Number of people who have engaged with the quiz and have passed the first slide (clicked on the “start quiz” button or answered the first question). 

    ![quiz builder metrics analytics starts](/images/manual_quizbuilder_metrics_analytics_starts.png)

    `Quiz Responses` / `Responses` - Number of people who have completed the quiz. Test responses (completed via the Test quiz button) are deleted from your metrics after one hour.

    ![quiz builder metrics analytics responses](/images/manual_quizbuilder_metrics_analytics_responses.png)

    `Completion Rate` / `Comp. Rate` - Percentage of people who have engaged with the quiz and completed it.

    ![quiz builder metrics analytics completion rate](/images/manual_quizbuilder_metrics_analytics_comprate.png)

    `Carts Count` / `Num. Carts` - Number of people who have selected products and clicked on the “proceed to cart” or “proceed to checkout” button.

    ![quiz builder metrics analytics carts count](/images/manual_quizbuilder_metrics_analytics_cartscount.png)

    `Avg. Cart Value` - Average value of the products included in the carts or checkouts.

    ![quiz builder metrics analytics average carts](/images/manual_quizbuilder_metrics_analytics_avgcarts.png)

    `Total Carts Value` - Total value of the products included in all the carts or checkouts. This does not represent the total value of purchases since you should expect some drop-off at checkout.

    ![quiz builder metrics analytics total carts](/images/manual_quizbuilder_metrics_analytics_totalcarts.png)

    `Number of Orders (Beta)` - Number of people who have placed an order after completing this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Total Orders Value (Beta)` - Total value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

    `Avg. Order Value (Beta)` - Average value of orders placed after taking this quiz. To track Order values with the RevenueHunt app for Shopify, connect your quiz to the Shopify Revenue Reports via the Connect tab.

## Drop-off

=== "Shopify"

    ![quiz builder metrics drop off](/images/manual_quizbuilder_metrics_dropoff.png)

    The drop-off rate is measured based on events, which are triggered whenever someone starts a quiz. Some of these start events can be blocked by adblocking plugins in browsers. If you see a difference between the number of quiz starts and the dropoff rate, that is because the number of quiz starts in the analytics tab is automatically adjusted by the algorithm to filter in also the starts blocked by the ad blocker plugin.

    ![quiz builder metrics drop off dates](/images/manual_quizbuilder_metrics_dropoff_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    `table` - Displays the dropoff rate for each question and the results page in a table format.

    ![quiz builder metrics drop off table](/images/manual_quizbuilder_metrics_dropoff_table.png)

    `chart` - Displays the dropoff rate for each question and the results page in a chart format.

    ![quiz builder metrics drop off chart](/images/manual_quizbuilder_metrics_dropoff_chart.png)

=== "Shopify V2"

    Coming Soon

=== "WooCommerce"

    ![manual_woo_quizbuilder_metrics_dropoff](/images/manual_woo_quizbuilder_metrics_dropoff.png)

    The drop-off rate is measured based on events, which are triggered whenever someone starts a quiz. Some of these start events can be blocked by adblocking plugins in browsers. If you see a difference between the number of quiz starts and the dropoff rate, that is because the number of quiz starts in the analytics tab is automatically adjusted by the algorithm to filter in also the starts blocked by the ad blocker plugin.

    ![quiz builder metrics drop off dates](/images/manual_quizbuilder_metrics_dropoff_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    `table` - Displays the dropoff rate for each question and the results page in a table format.

    ![quiz builder metrics drop off table](/images/manual_quizbuilder_metrics_dropoff_table.png)

    `chart` - Displays the dropoff rate for each question and the results page in a chart format.

    ![quiz builder metrics drop off chart](/images/manual_quizbuilder_metrics_dropoff_chart.png)

=== "Magento"

    ![manual_standalone_quizbuilder_metrics_dropoff](/images/manual_standalone_quizbuilder_metrics_dropoff.png)

    The drop-off rate is measured based on events, which are triggered whenever someone starts a quiz. Some of these start events can be blocked by adblocking plugins in browsers. If you see a difference between the number of quiz starts and the dropoff rate, that is because the number of quiz starts in the analytics tab is automatically adjusted by the algorithm to filter in also the starts blocked by the ad blocker plugin.

    ![quiz builder metrics drop off dates](/images/manual_quizbuilder_metrics_dropoff_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    `table` - Displays the dropoff rate for each question and the results page in a table format.

    ![quiz builder metrics drop off table](/images/manual_quizbuilder_metrics_dropoff_table.png)

    `chart` - Displays the dropoff rate for each question and the results page in a chart format.

    ![quiz builder metrics drop off chart](/images/manual_quizbuilder_metrics_dropoff_chart.png)

=== "BigCommerce"

    ![manual_standalone_quizbuilder_metrics_dropoff](/images/manual_standalone_quizbuilder_metrics_dropoff.png)

    The drop-off rate is measured based on events, which are triggered whenever someone starts a quiz. Some of these start events can be blocked by adblocking plugins in browsers. If you see a difference between the number of quiz starts and the dropoff rate, that is because the number of quiz starts in the analytics tab is automatically adjusted by the algorithm to filter in also the starts blocked by the ad blocker plugin.

    ![quiz builder metrics drop off dates](/images/manual_quizbuilder_metrics_dropoff_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    `table` - Displays the dropoff rate for each question and the results page in a table format.

    ![quiz builder metrics drop off table](/images/manual_quizbuilder_metrics_dropoff_table.png)

    `chart` - Displays the dropoff rate for each question and the results page in a chart format.

    ![quiz builder metrics drop off chart](/images/manual_quizbuilder_metrics_dropoff_chart.png)

=== "Standalone"

    ![manual_standalone_quizbuilder_metrics_dropoff](/images/manual_standalone_quizbuilder_metrics_dropoff.png)

    The drop-off rate is measured based on events, which are triggered whenever someone starts a quiz. Some of these start events can be blocked by adblocking plugins in browsers. If you see a difference between the number of quiz starts and the dropoff rate, that is because the number of quiz starts in the analytics tab is automatically adjusted by the algorithm to filter in also the starts blocked by the ad blocker plugin.

    ![quiz builder metrics drop off dates](/images/manual_quizbuilder_metrics_dropoff_dates.png)

    To change the dates click on the 📆 icon. You can change the period to select it from the moment you started using the quiz or from a given date.

    `table` - Displays the dropoff rate for each question and the results page in a table format.

    ![quiz builder metrics drop off table](/images/manual_quizbuilder_metrics_dropoff_table.png)

    `chart` - Displays the dropoff rate for each question and the results page in a chart format.

    ![quiz builder metrics drop off chart](/images/manual_quizbuilder_metrics_dropoff_chart.png)


---

← [Back to Quiz Builder Index](/reference/quiz-builder/)


← Previous: [Share / Publish](/reference/quiz-builder/share-publish/)
