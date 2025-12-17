---
icon: material/numeric-6
---

# Product Quiz Metrics: What to Track to Convert Better

Data from product recommendation quizzes can significantly enhance your conversion rates. Understanding which metrics to track and how to interpret them is key to optimizing your quizzes for better performance. 

Here’s a guide on the most critical quiz metrics and how they can drive better conversion outcomes.

![product quiz metrics: what to track to convert better image1](https://revenuehunt.com/wp-content/uploads/2024/06/Quiz-Metrics.png)

## Where to find the data?

### ➡️ Quiz Metrics

All the information gathered by your RevenueHunt Product Recommendation Quiz can be found in the [Metrics/Analytics](/reference/quiz-builder/metrics/) panel. 

- The [Responses](/reference/quiz-builder/metrics/#responses) section shows all the quiz responses organized by date/timestamp. Click on a date to open a specific response. Each response shows what choices the customer made, which products were upvoted or excluded, which products were recommended, and what customer tags carried out until the results page.

    ![quiz builder metrics responses](/images/manual_shopifyV2_quizbuilder_responses.png)

    ![quiz builder metrics responses details](/images/manual_shopifyV2_quizbuilder_responses_sample1.png)

- The [Analytics](/reference/quiz-builder/metrics/#analytics) section provides graphs on quiz engagement, conversion rate, and revenue. You can analyze the data by date and compare it to past periods or other quizzes.

    ![quiz builder metrics analytics](/images/manual_shopifyV2_quizbuilder_metrics_analytics.png)

- The [Drop Off](/reference/quiz-builder/metrics/#drop-off) section displays a breakdown percentage of users leaving certain questions in your quiz. The data is shown in a table format.

    ![quiz builder metrics drop off](/images/manual_shopifyV2_quizbuilder_metrics_analytics_dropoff.png)


###➡️ Download Raw Data

You can analyze the data there or [download all the responses as a .CSV file](/how-to-guides/download-quiz-responses/) and analyze it in Google Sheets or Microsoft Excel.

![quiz builder metrics responses download](/images/manual_shopifyV2_quizbuilder_responses_exportCSV.png)

###➡️ Advanced Tracking

Additionally, RevenueHunt app offers integrations with [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) where additional information like click rate per choice, traffic source or revenue can be collected and measured.


## What to analyze and how to improve?

### 1️⃣ Customer Engagement
 

**Quiz Starts and Completions**

Tracking the number of quiz starts and responses/completions is fundamental. High start rates indicate good initial engagement, but the completion rate is what truly matters for conversions. If you notice a drop-off between starts and completions, it might be time to refine your quiz flow or simplify the questions.

![quiz builder metrics analytics starts and completions](/images/cs_track_metrics_starts_responses.png)

!!! note

    `Quiz Starts` refers to the number of people who have engaged with the quiz by passing the first slide. 
    
    `Quiz Responses` refers to the number of people who have completed the quiz, aka. reached the quiz results page. 
    
    If the customer closes the quiz before the results page, this will not be counted as a response/completion.

**Completion Rate**

!!! info "Completion Rate Formula"  

    **Completion Rate (%)** = (Number of Quiz Completions ÷ Number of Quiz Starts) × 100


`Completion Rate` is the percentage of people who have engaged with the quiz and completed it. The completion rate is a clear indicator of how engaging and user-friendly your quiz is. A higher completion rate suggests that users find the quiz relevant and easy to navigate, which increases the likelihood of them following through to purchase recommendations. The aim is to keep the completion rate as high as possible, around 90-100%.

![quiz builder metrics analytics completion rate](https://docs.revenuehunt.com/images/manual_quizbuilder_metrics_analytics_comprate.png)

**Drop-off Points / Drop-off Rate**

Identifying where users drop off in your quiz can provide insights into potential friction points. Are users abandoning the quiz at a specific question or step? Use this data to adjust those points, making them more intuitive or engaging.

![quiz builder metrics drop off](/images/manual_shopifyV2_quizbuilder_metrics_analytics_dropoff.png)


!!! note
    The `drop-off rate` is measured based on events, which are triggered whenever someone starts a quiz. Some of these start events can be blocked by adblocking plugins in browsers. If you see a difference between the number of quiz starts and the dropoff rate, that is because the number of quiz starts in the analytics tab is automatically adjusted by the algorithm to filter in also the starts blocked by the ad blocker plugin.

| Issue                          | Solution                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Low Quiz Starts**            | - **Make the quiz more visible.** Publish the quiz in multiple ways on your website, send a link to the quiz in your newsletter, or post a link on social media. <br> - **Promote the quiz.** Check [this article](/customer-success/how-to-get-more-quiz-engagement/) for great advice on how to increase your quiz starts. <br> - **Run ads to increase quiz popularity.** If using GA4, check the best traffic sources for your quiz and invest more in them. |
| **Low Completion Rate / High Drop Off** | - **Make the quiz shorter, max. 5-6 questions.** Customers are likely losing attention. <br> - **Add more visuals to the quiz.** Turn multiple-choice questions into picture questions. Add images and videos to your quiz. Visual quizzes have a much higher completion rate than pure text-based ones. <br> - **Check your mandatory questions.** Perhaps customers don’t want to leave their phone number, name, or email. You can make any question optional in [Question Settings](/reference/quiz-builder/questions/#question-settings). <br> - **Add personal data questions towards the end of the quiz.** Customers are more likely to stay and leave their data while already invested in the quiz. |


### 2️⃣ Revenue
 

**Carts Count and Total Carts Value**

Tracking how many users proceed to cart after completing the quiz can help you gauge the effectiveness of your product recommendations. A high cart count and total cart value indicate that the recommended products resonate well with the users.


![quiz builder metrics analytics carts count and value](/images/cs_track_metrics_number_carts.png)
![quiz builder metrics analytics carts count and value](/images/cs_track_metrics_tot_carts_value.png)

**Average Cart Value**

!!! info "Average Cart Value Formula"  
    
    **Average Cart Value** = Total Carts Value ÷ Carts Count

Understanding the average value of products in the carts can help you assess the monetary impact of your quiz. This metric is crucial for evaluating the overall financial performance and can guide you in setting appropriate pricing strategies.

![quiz builder metrics analytics average carts](https://docs.revenuehunt.com/images/manual_quizbuilder_metrics_analytics_avgcarts.png)

**Number of Orders and Total Orders Value**

For a more direct measure of conversion, track the number of orders placed and their total value, allowing you to directly correlate quiz engagement with sales performance.

!!! warning "Connect your quiz to Shopify Customers and Shopify Revenue Reports"

    Connect your quiz to [Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/) (and [Shopify Revenue Reports](/how-to-guides/track-quiz-revenue/?h=shopify+revenue#activate-shopify-revenue-report)) to track the number of orders and their total value.

![quiz builder metrics analytics number of orders and total orders value](/images/cs_track_metrics_orders.png)

**Average Order Value**

!!! info "Average Order Value Formula"  
    
    **Average Order Value** = Total Orders Value ÷ Number of Orders


Monitoring the average order value post-quiz completion provides insights into the spending behavior of your users. It helps in understanding whether the quiz is effectively driving higher-value purchases. By using RevnueHunt Product Recommendation Quiz in your store you should expect the AOV to increase by 20%.

**Conversion Rate**

!!! info "Conversion Rate Formula"  

    **Conversion Rate (%)** = (Number of Purchases after Quiz Completion ÷ Total Number of Quiz Completions) × 100


To measure the conversion rate of your quiz, track the number of users who complete the quiz and proceed to make a purchase, then calculate the percentage of these users relative to the total number of quiz completions. This metric is essential because it reveals how effectively the quiz drives sales, aiding in optimizing the quiz design and marketing strategies to maximize revenue.  By using a RevenueHunt Product Recommendation Quiz in your store you should expect conversion rates bumped up from 2% to 5%.

| Issue                                      | Solution                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Customers don’t add products to cart**   | - Check if the quiz returns recommendations. <br> - Check your quiz [checkout settings](/how-to-guides/change-checkout-settings/). <br> - **Limit the number of recommended products.** A good product selector should recommend only one product that matches all the customer criteria or one product per routine step (in case of beauty shops). <br> - Make the call-to-action buttons more visible by styling them. <br> - Offer a discount or a coupon code. |
| **Low Conversion Rate**                    | - **Limit the number of recommended products.** A good product selector should recommend only one product that matches all the customer criteria or one product per routine step (in case of beauty shops). <br> - Offer a discount or a coupon code. <br> - Set up a [post-quiz email flow](/tutorials/follow-up-emails-klaviyo/) to recapture the lost revenue.                                             |
| **Customers add to the cart but don’t buy** | - Offer a [discount or a coupon code](/how-to-guides/add-discount/). <br> - Set up a [post-quiz email flow](/tutorials/follow-up-emails-klaviyo/) to recapture the lost revenue.                                                                                                                                                                                                                                                          |
| **Customers purchase only once**           | - Customer preferences change. Make new versions of the quiz and improve upon it by, for example, giving personalized advice along the recommendations. <br> - Segment your customers and follow up with more targeted marketing campaigns post-quiz.                                                                                                              |


!!! tip "Tip: Measure Quiz Revenue"
    Not sure how to measure quiz revenue? Check our step-by-step guide [here](/how-to-guides/track-quiz-revenue/).


### 3️⃣ Recommendations



!!! info "How to get the data?"

    To get data about most clicked choices you can use the two method highlighted below:

    - **Export as CSV**

        Regularly [export quiz response data](/how-to-guides/download-quiz-responses/) for in-depth analysis in *Google Sheets* or *Microsoft Excel*. This allows you to spot trends, understand user behavior over time, and make data-driven decisions to enhance your quiz strategy.

    - **Use Google Analytics**

        With [GA4](/how-to-guides/integrate-google-analytics/) you can measure extra information about the quiz and the customer. You can track customer behavior with events like clicking a choice or a questions, answering an open question or clicking on a product or description. This provides more insight into who the customers are and how they interact with the quiz. 

 

**Recommendation Analysis**

Delve into why specific products or routines were recommended most often. This helps in fine-tuning your recommendation algorithms. Analyzing individual responses allows you to understand customer preferences better and adjust your product catalog accordingly.

**Product and Slot Blocks**

Evaluate the performance of product and slot blocks within the quiz. Ensure that the products being recommended are aligned with user preferences and catch their attention. This granular analysis can lead to better-targeted recommendations, improving user satisfaction and conversion rates.

**Most Clicked Products**

Track which products are most frequently clicked on during the quiz. This data reveals which products are generating the most interest and engagement. Use this insight to highlight popular products more prominently in your quiz and marketing efforts.

**Most Purchased Products**

Identify which recommended products are being purchased most often. This metric helps you understand the effectiveness of your recommendations in driving sales. Emphasize these high-performing products in future quizzes and promotional campaigns.

**Least Purchased Products**

Determine which products are being recommended but not purchased. Investigate potential reasons for low conversions, such as pricing, product appeal, or placement within the quiz. Adjust your strategy to either improve the attractiveness of these products or replace them with alternatives.

 | Issue                                | Solution                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Customers buy the same products all the time** | - Use the [responses troubleshooter](/how-to-guides/troubleshoot-product-results/) to check if some products in your quiz get by default more votes than others. <br> - If that’s the case, you can diversify the product recommendations by adding an extra question to your quiz or by linking other products to more choices.                                                            |
| **Customers get empty recommendations**          | - Check if your Results Page has a Product Block or a Slot Block to show the products. <br> - Check if you’ve linked products or collections to choices in the quiz. <br> - Check if you’re not excluding too many products from choices.                                                                                                |


### 4️⃣ Customer Answers
 

The quiz should help you answer the questions, such as who is my customer and what kind of products are they interested in, and what products they buy. You can understand these things by diving deeper into customer choices and open answers.

**Most Clicked Choices**

Measure which quiz choices are most frequently clicked. This data provides insights into customer interests and preferences. By understanding which options are most popular, you can improve quiz engagement by highlighting popular choices more prominently and ensuring that the flow of the quiz guides users towards these choices. 


!!! info "How to get the data?"

    To get data about most clicked choices you can use the two method highlighted below:

    - **Export as CSV**

        Regularly [export quiz response data](/how-to-guides/download-quiz-responses/) for in-depth analysis in *Google Sheets* or *Microsoft Excel*. This allows you to spot trends, understand user behavior over time, and make data-driven decisions to enhance your quiz strategy.

    - **Use Google Analytics**

        With [GA4](/how-to-guides/integrate-google-analytics/) you can measure extra information about the quiz and the customer. You can track customer behavior with events like clicking a choice or a questions, answering an open question or clicking on a product or description. This provides more insight into who the customers are and how they interact with the quiz. 


**Customer Tags**

Use [customer tags](/how-to-guides/use-customer-tags/) collected from quiz responses to segment your audience effectively. This segmentation can then be used to personalize marketing efforts, ensuring that customers receive relevant offers and recommendations, thereby enhancing the likelihood of conversion.

| Issue                                      | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **I don’t know who my customers are**      | - Analyze customer quiz responses in the [Responses](/reference/quiz-builder/metrics/#responses) panel. <br> - Use [Customer Tags](/how-to-guides/use-customer-tags/) to mark certain quiz choices to help you define the customer group. For example, if you ask your customer an age question, you can tag them based on their age group. You can do the same with other quiz questions, and soon you’ll be able to identify the most popular tags and buyer personas.                                                                                                         |
| **I don’t know what my customers buy**     | - Check your Orders and Revenue tracking tools to see the most frequently purchased items. <br> - Analyze the product recommendations given in the quiz and cross-reference them with actual purchases to see what recommended products are being bought. <br> - Use post-purchase surveys to confirm why customers chose certain products.                                                                                                                                                |
| **I don’t know how to make customers purchase regularly** | - Use [Customer Tags](/how-to-guides/use-customer-tags/) to mark certain quiz choices to help you define the customer group. You can then create a marketing campaign in your CRM platform to target that specific group of customers. Highly segmented campaigns tend to have higher returns. <br> - Offer loyalty programs or subscription services to encourage repeat purchases. <br> - Send personalized follow-up emails with product recommendations based on previous purchases and quiz responses. <br> - Introduce time-limited discounts or special offers to incentivize repeat purchases. |
| **I don’t know which products are underperforming** | - Review the quiz responses to see which products are least selected or recommended. <br> - Analyze sales data to identify products with low conversion rates. <br> - Gather customer feedback to understand why certain products may not be appealing. <br> - Consider revising the product descriptions, images, or prices to improve their attractiveness. <br> - Test different product placements in your quiz to see if visibility affects their performance.                                 |
| **I don’t know how to keep my quiz content fresh** | - Regularly update your quiz questions and product recommendations based on current trends and customer feedback. <br> - Introduce seasonal or thematic quizzes to keep the content relevant and engaging. <br> - Monitor industry trends and competitor quizzes to stay ahead in content innovation. <br> - Solicit feedback from quiz takers on how to improve the quiz and incorporate their suggestions. <br> - Use [A/B testing](/how-to-guides/a-b-testing/) to continuously refine quiz elements and identify what resonates best with your audience. |


---

By focusing on these key metrics, you can transform your product recommendation quizzes into powerful conversion tools. 

Understanding and optimizing each stage of the quiz journey—from engagement to order placement—enables you to provide a personalized shopping experience that drives better conversion rates and increases overall sales.

This article explains how to track quiz metrics and improve your conversion rates.

