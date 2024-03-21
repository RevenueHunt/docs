# How to Integrate Your Facebook Pixel

The Facebook Pixel is an essential analytics tool for tracking user interaction with your quiz and gauging the success of your Facebook ads.

**What is the Facebook Pixel?**

This small piece of code placed on your website helps you monitor conversions from ads, improve the performance of future advertising, and create targeted audiences based on past interactions with your website.

## Setting Up Your Facebook Pixel

If you don't have a Pixel yet, set one up following Facebook's guide. Once created, integrate it with your quiz:

1. Go to the **Connect** tab within your quiz settings.
2. Find the Facebook Pixel section and hit **"connect."**
3. Enter your unique Facebook Pixel ID. If you haven’t created one already, follow [these instructions](https://www.facebook.com/business/help/952192354843755?id=1205376682832142) to create a new Pixel in Facebook.

## Tracking Engagement with Facebook Events Manager

With the Pixel activated, the Facebook **Events Manager dashboard** becomes a window into how users interact with your quiz. This data is vital for crafting [Custom Audiences](https://www.facebook.com/business/learn/lessons/custom-audience-tips-with-facebook-pixel) and [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) to refine your marketing strategies.

![how to integrate fb pixel events](/images/how to fb pixel events.png)

### Tracked Interactions

The Pixel will fire a `viewContent` event for the following user actions:

- Initiating a quiz
- Viewing a question
- Selecting an answer
- Reaching the results page
- Browsing a product

Each `viewContent` event is distinguished by a specific "category" tag, allowing for detailed tracking.

### Tracked Events

Besides the `viewContent` events, the Pixel will also track when a user:

- Adds a product to their cart
- Heads to the cart or checkout
- Answers an email question
- Answers a phone question

Here’s a list of all the tracked events:

| Trigger                        | fbq_action  | fbq_event        | fbq_params                                                                                                                                                   |
|--------------------------------|-------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User starts a quiz             | track       | ViewContent      | { content_name: quiz_name, content_category: 'quiz' }                                                                                                        |
| User views a question          | track       | ViewContent      | { content_name: question_title, content_category: 'question' }                                                                                                |
| User clicks on a choice        | track       | ViewContent      | { content_name: choice_text, content_category: 'choice' }                                                                                                     |
| User responds to the email     | trackCustom | EmailLead        | { content_name: quiz_name, content_category: 'lead' }                                                                                                        |
| User responds to the phone     | trackCustom | PhoneLead        | { content_name: quiz_name, content_category: 'lead' }                                                                                                        |
| User gets to results page      | track       | ViewContent      | { content_name: quiz_title, content_category: 'results' }                                                                                                    |
| A certain product is recommended in the results page | track | lead | { content_name: product_name, content_type: 'recommendation', content_ids: sku_or_variant_id, value: product_price, currency: quiz_currency }               |
| Customer clicks on product     | track       | ViewContent      | { content_name: product_name, content_type: 'recommendation', content_ids: sku_or_variant_id, value: product_price, currency: quiz_currency }                 |
| Customer adds a product to cart| track       | AddToCart        | { content_name: product_name, content_type: 'recommendation', content_ids: sku_or_variant_id, value: product_price, currency: quiz_currency }                 |
| Customer proceeds to cart/checkout | track   | InitiateCheckout | { num_items: num_products_in_cart, currency: quiz_currency, value: value_of_products_in_cart }                                                              |
| Customer retakes quiz          | track       | ViewContent      | { content_name: quiz_name, content_category: 'quiz' }                                                                                                        |


## Adding a Custom Pixel

For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](https://docs.revenuehunt.com/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

1. **Deactivate Facebook Pixel**: If you have previously connected a pixel through the `Connect`tab, you'll have to adeactivate it and publish the changes.
2. **Understand the Callback Function**: Visit the [FAQ page](https://docs.revenuehunt.com/how-to-guides/use-callback-function/) on custom integrations to learn how our callback function operates and how it can be utilized for tracking custom events.
3. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located:
    ```html
    <script>
    function prqQuizCallback(quizResponse){
        window.fbq(action, event, params);
    }
    </script>

    ```
4. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
5. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.

By implementing the Facebook Pixel, you'll harness powerful data to optimize your ad campaigns, personalize the user experience, and ultimately, increase conversions.
