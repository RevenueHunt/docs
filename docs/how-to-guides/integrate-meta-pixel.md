---
icon: material/facebook
---

# How to Integrate Meta Pixel with Quiz

The Meta Pixel is an essential analytics tool for tracking user interaction with your quiz and gauging the success of your Facebook ads.

This article explains how to integrate the Meta Pixel with your quiz application and how to use the Meta Events Manager to track user interactions with your quiz.

??? question "What is Meta Pixel?"

    This small piece of code placed on your website helps you monitor conversions from ads, improve the performance of future advertising, and create targeted audiences based on past interactions with your website.

## Setting Up Your Meta Pixel

!!! note

    Facebook Pixel / Meta Pixel tracking works best if you embed your quiz on a new page in your online store. Follow the instuctions in [this article](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page) to set this up.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/3257be8755f044969f803d9e5d29ace6?sid=8a6b4ed5-3bfe-4935-b820-9573ed93ce98" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    If you have not implemented a Pixel on your website yet, set one up following [Meta guide](https://www.facebook.com/business/help/952192354843755?id=1205376682832142). Once created, add it to your website.


    1. **Connect Meta Pixel to your Shopify Store**: Navigate to your Shopify `Store settings > Customer events`. Ensure that the Meta (Facebook) Pixel is integrated. If not, use the [Facebook and Instagram Meta app](https://apps.shopify.com/facebook-and-instagram-meta-app) for integration.
    2. **Set Up Data Sources**: Open the Facebook and Instagram app in Shopify. Go to `settings` and set `shared data` to `maximum` to track advanced and custom events. Choose or create a **data set** for tracking. 

        ![how to integrate fb pixel shopify v2](/images/how_to_shopifyv2_integrate_meta_pixel_facebookappsettings.png)

        !!! tip

            To create a new data set, go to [https://business.facebook.com/](https://business.facebook.com/) > `Ads Manager` > `Events Manager` > `Data sources` > `Create data source`.

    3. **Publish the Quiz**: Ensure the quiz is published on your online store. It is recommended to have a dedicated page for the quiz to track events accurately.

        !!! tip

            Check this article to learn how to publish the quiz on a dedicated landing page: [Publish Quiz Inline](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page)

    4. **Connect Quiz to Meta Pixel**: To integrate the Meta Pixel with your quiz:

        - Go to the [Integrations](/reference/quiz-builder/connect-integrations/) tab within your quiz settings.
        - Find the Meta Pixel section and hit `Activate`.
            ![how to integrate fb pixel shopify v2](/images/how_to_integrate_fb_pixel_shopify_v2.png)
        - Click `Save` to confirm the changes.
        - Once activated the quiz will connect to the Meta Pixel already present on your website.

    4. **Test the Integration**: In Shopify admin, go to Facebook and Instagram app > `settings`, and open the data set to access Meta Events Manager. Use the `Test events` feature to confirm that events are being tracked correctly by interacting with the quiz. Provide your website URL to test the integration. Then navigate to your website and interact with the quiz. After completing the quiz, check the Events Manager for tracked events such as: 
        - Retake quiz
        - View content page
        - Lead submissions (name and email)
        
        If events are visible, the pixel integration is functioning correctly.

        ![how to integrate fb pixel shopify v2](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        For a complete list of tracked events within the Revenue Hunt app, check the [Tracked Events](/how-to-guides/integrate-meta-pixel/#tracked-events) section.

    6. **Review Custom Events**: If you want to use the custom events in your ads and audiences, you need to review them. Check the [Review Custom Events](/how-to-guides/integrate-meta-pixel/#review-custom-events) section.



=== "Shopify (Legacy)"

    If you have not implemented a Pixel on your website yet, set one up following [Meta guide](https://www.facebook.com/business/help/952192354843755?id=1205376682832142). Once created, add it to your website.


    1. **Connect Meta Pixel to your Shopify Store**: Navigate to your Shopify `Store settings > Customer events`. Ensure that the Meta (Facebook) Pixel is integrated. If not, use the [Facebook and Instagram Meta app](https://apps.shopify.com/facebook) for integration.
    2. **Set Up Data Sources**: Open the Facebook and Instagram app in Shopify. Go to `settings` and set `shared data` to `maximum` to track advanced and custom events. Choose or create a **data set** for tracking. 

        ![how to integrate fb pixel shopify v2](/images/how_to_shopifyv2_integrate_meta_pixel_facebookappsettings.png)

        !!! tip

            To create a new data set with a unique Pixel ID, go to [https://business.facebook.com/](https://business.facebook.com/) > `Ads Manager` > `Events Manager` > `Data sources` > `Create data source`.

    3. **Publish the Quiz**: Ensure the quiz is published on your online store. It is recommended to have a dedicated page for the quiz to track events accurately.

        !!! tip

            Check this article to learn how to publish the quiz on a dedicated landing page: [Publish Quiz Inline](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page)

    4. **Connect Quiz to Meta Pixel**: To integrate the Meta Pixel with your quiz:

        1. Go to the [Connect](/reference/quiz-builder/connect-integrations/) tab within your quiz settings.
        2. Find the Meta Pixel section and hit `connect`.
        3. Enter your unique `Meta Pixel ID`. Make sure that this pixel ID is the same as the one you used to set up the data set in the Facebook and Instagram app.

    5. **Test the Integration**: In Shopify admin, go to Facebook and Instagram app > `settings`, and open the data set to access Meta Events Manager. Use the `Test events` feature to confirm that events are being tracked correctly by interacting with the quiz. Provide your website URL to test the integration. Then navigate to your website and interact with the quiz. After completing the quiz, check the Events Manager for tracked events such as: 
        - Retake quiz
        - View content page
        - Lead submissions (name and email)
        
        If events are visible, the pixel integration is functioning correctly.
        
        ![how to integrate fb pixel shopify v2](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)  

        For a complete list of tracked events within the Revenue Hunt app, check the [Tracked Events](/how-to-guides/integrate-meta-pixel/#tracked-events) section.

    6. **Review Custom Events**: If you want to use the custom events in your ads and audiences, you need to review them. Check the [Review Custom Events](/how-to-guides/integrate-meta-pixel/#review-custom-events) section.

=== "WooCommerce"

    If you don't have a Pixel yet, set one up following [Meta guide](https://www.facebook.com/business/help/952192354843755?id=1205376682832142). Once created, integrate it with your quiz:

    1. Go to the [Connect](/reference/quiz-builder/connect-integrations/) tab within your quiz settings.
    2. Find the Meta Pixel section and hit `connect`.
    3. Enter your unique `Meta Pixel ID`. If you haven’t created one already, follow [these instructions](https://www.facebook.com/business/help/952192354843755?id=1205376682832142) to create a new Pixel in Meta.
    4. **Test events**: Go to the [Events Manager](https://business.facebook.com/events/manager/), `Test events` and provide your website URL to test the integration. Then navigate to your website and interact with the quiz. After completing the quiz, check the Events Manager for tracked events such as: 
        - Retake quiz
        - View content page
        - Lead submissions (name and email)
        
        If events are visible, the pixel integration is functioning correctly.

        ![how to integrate fb pixel shopify v2](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        For a complete list of tracked events within the Revenue Hunt app, check the [Tracked Events](/how-to-guides/integrate-meta-pixel/#tracked-events) section.

    5. **Review Custom Events**: If you want to use the custom events in your ads and audiences, you need to review them. Check the [Review Custom Events](/how-to-guides/integrate-meta-pixel/#review-custom-events) section.

=== "Magento"

    If you don't have a Pixel yet, set one up following [Meta guide](https://www.facebook.com/business/help/952192354843755?id=1205376682832142). Once created, integrate it with your quiz:

    1. Go to the [Connect](/reference/quiz-builder/connect-integrations/) tab within your quiz settings.
    2. Find the Meta Pixel section and hit `connect`.
    3. Enter your unique `Meta Pixel ID`. If you haven’t created one already, follow [these instructions](https://www.facebook.com/business/help/952192354843755?id=1205376682832142) to create a new Pixel in Meta.
    4. **Test events**: Go to the [Events Manager](https://business.facebook.com/events/manager/), `Test events` and provide your website URL to test the integration. Then navigate to your website and interact with the quiz. After completing the quiz, check the Events Manager for tracked events such as: 
        - Retake quiz
        - View content page
        - Lead submissions (name and email)
        
        If events are visible, the pixel integration is functioning correctly.

        ![how to integrate fb pixel shopify v2](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        For a complete list of tracked events within the Revenue Hunt app, check the [Tracked Events](/how-to-guides/integrate-meta-pixel/#tracked-events) section.

    5. **Review Custom Events**: If you want to use the custom events in your ads and audiences, you need to review them. Check the [Review Custom Events](/how-to-guides/integrate-meta-pixel/#review-custom-events) section.

=== "BigCommerce"

    If you don't have a Pixel yet, set one up following [Meta guide](https://www.facebook.com/business/help/952192354843755?id=1205376682832142). Once created, integrate it with your quiz:

    1. Go to the [Connect](/reference/quiz-builder/connect-integrations/) tab within your quiz settings.
    2. Find the Meta Pixel section and hit `connect`.
    3. Enter your unique `Meta Pixel ID`. If you haven’t created one already, follow [these instructions](https://www.facebook.com/business/help/952192354843755?id=1205376682832142) to create a new Pixel in Meta.    
    4. **Test events**: Go to the [Events Manager](https://business.facebook.com/events/manager/), `Test events` and provide your website URL to test the integration. Then navigate to your website and interact with the quiz. After completing the quiz, check the Events Manager for tracked events such as: 
        - Retake quiz
        - View content page
        - Lead submissions (name and email)
        
        If events are visible, the pixel integration is functioning correctly.

        ![how to integrate fb pixel shopify v2](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        For a complete list of tracked events within the Revenue Hunt app, check the [Tracked Events](/how-to-guides/integrate-meta-pixel/#tracked-events) section.

    5. **Review Custom Events**: If you want to use the custom events in your ads and audiences, you need to review them. Check the [Review Custom Events](/how-to-guides/integrate-meta-pixel/#review-custom-events) section.    

=== "Standalone"

    If you don't have a Pixel yet, set one up following [Meta guide](https://www.facebook.com/business/help/952192354843755?id=1205376682832142). Once created, integrate it with your quiz:

    1. Go to the [Connect](/reference/quiz-builder/connect-integrations/) tab within your quiz settings.
    2. Find the Meta Pixel section and hit `connect`.
    3. Enter your unique `Meta Pixel ID`. If you haven’t created one already, follow [these instructions](https://www.facebook.com/business/help/952192354843755?id=1205376682832142) to create a new Pixel in Meta.
    4. **Test events**: Go to the [Events Manager](https://business.facebook.com/events/manager/), `Test events` and provide your website URL to test the integration. Then navigate to your website and interact with the quiz. After completing the quiz, check the Events Manager for tracked events such as: 
        - Retake quiz
        - View content page
        - Lead submissions (name and email)
        
        If events are visible, the pixel integration is functioning correctly.

        ![how to integrate fb pixel shopify v2](https://loom.com/i/da1d0cdd420341698d56384c34496a99?workflows_screenshot=true)

        For a complete list of tracked events within the Revenue Hunt app, check the [Tracked Events](/how-to-guides/integrate-meta-pixel/#tracked-events) section.

    5. **Review Custom Events**: If you want to use the custom events in your ads and audiences, you need to review them. Check the [Review Custom Events](/how-to-guides/integrate-meta-pixel/#review-custom-events) section.

## Tracking Engagement with Meta Events Manager

With the Pixel activated, the Meta **Events Manager dashboard** becomes a window into how users interact with your quiz. This data is vital for crafting [Custom Audiences](https://www.facebook.com/business/learn/lessons/custom-audience-tips-with-facebook-pixel) and [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328) to refine your marketing strategies.

![how to integrate fb pixel events](/images/how_to_fb_pixel_events.png)

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

| **Trigger** | **fbq_action** | **fbq_event** | **fbq_params** |
|---------------------------|--------------|-------------|-----------------------------------------------|
| User starts a quiz | `track` | `ViewContent` | `{ content_name: quiz_name, content_category: 'quiz' }` |
| User views a question | `track` | `ViewContent` | `{ content_name: question_title, content_category: 'question' }` |
| User clicks on a choice | `track` | `ViewContent` | `{ content_name: choice_text, content_category: 'choice' }` |
| User submits email | `trackCustom` | `EmailLead` | `{ content_name: quiz_name, content_category: 'lead' }` |
| User submits phone | `trackCustom` | `PhoneLead` | `{ content_name: quiz_name, content_category: 'lead' }` |
| User gets to results page | `track` | `ViewContent` | `{ content_name: results_page_title, content_category: 'results' }` |
| User gets to results page | `track` | `Lead` | `{}` |
| A certain product is recommended in the results page | `track` | `ViewContent` | `{ content_name: product_name, content_type: 'recommendation', content_ids: [sku_or_variant_id], value: product_price, currency: quiz_currency }` |
| Customer adds a product to cart | `track` | `AddToCart` | `{ content_name: product_name, content_type: 'recommendation', content_ids: [sku_or_variant_id], value: product_price, currency: quiz_currency }` |
| Customer proceeds to checkout | `track` | `InitiateCheckout` | `{ num_items: num_products_in_cart, currency: quiz_currency, value: value_of_products_in_cart }` |
| Customer retakes the quiz | `trackCustom` | `RetakeQuiz` | `{ content_name: quiz_name, content_category: 'quiz' }` |



## Review Custom Events


<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/88646c6099e340189f1d5a08ffee8ed7?sid=16508af3-bb5b-4154-85d1-367fdc099de0" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

This section outlines the process for managing custom events in Metapixel after connecting it to your quiz application. It details the steps to review, acknowledge, and confirm the use of custom events for advertising features.

1. After connecting Metapixel to your quiz, new custom events will start appearing in your app.

    Standard events include: 

    - `View Content`
    - `Page View`
    - `Lead`

    Custom events include: 

    - `Retake Quiz Action`
    - `Email Lead Action`
    
    These custom events by default can't be used with ads features but you can enable them to be used with ads features by reviewing them.

2. In your Metapixel data sources, you will see a notification `Custom events can't be used with ads features.` regarding custom events.

    ![how to integrate fb pixel review custom events](/images/how_to_shopifyv2_integrate_meta_pixel_reviewcustomevents.png)

3. To remove this notification, you must review the custom events. Click on `Review` to proceed with the acknowledgment process.

    ![how to integrate fb pixel review custom events 2](/images/how_to_shopifyv2_integrate_meta_pixel_reviewcustomevents2.png)

    - By acknowledging, you agree to review the custom events to ensure compliance with terms and conditions. Click 'Acknowledge' and select the actions for the custom events.

        ![how to integrate fb pixel review custom events 3](https://loom.com/i/6f49a0bcff394c7f85b35addc0cb4294?workflows_screenshot=true)

    - You can choose to enable both custom events: Retake Quiz and Email Lead.
    - After selecting the desired custom events, click 'Next' to confirm their collection.
    - Confirming allows the custom events to be used with ad features, including custom and lookalike audiences.
    - Click 'Confirm' to finalize your acceptance and review of the custom events.

        ![how to integrate fb pixel review custom events 3](https://loom.com/i/89174c089c514d7abc80f0e506581bbc?workflows_screenshot=true)

4. Refresh your Metapixel dashboard to ensure the notification is gone.
5. Your data should now flow correctly, allowing you to use the custom events in your ads and audiences.

## Adding a Custom Pixel

=== "Shopify"

    For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

    To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

    1. **Deactivate Meta Pixel**: If you have previously connected a pixel through the [Connect](/reference/quiz-builder/connect-integrations/) tab, you'll have to deactivate it and publish the changes.
    2. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located (load it sitewide and put it into the theme.liquid):
        ```html
        <script>
        function prqQuizCallback(quizResponse){
            window.fbq(action, event, params);
        }
        </script>

        ```
    3. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
    4. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.


=== "Shopify (Legacy)"

    For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

    To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

    1. **Deactivate Meta Pixel**: If you have previously connected a pixel through the [Connect](/reference/quiz-builder/connect-integrations/) tab, you'll have to deactivate it and publish the changes.
    2. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) on custom integrations to learn how our callback function operates and how it can be utilized for tracking custom events.
    3. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located (load it sitewide and put it into the theme.liquid):
        ```html
        <script>
        function prqQuizCallback(quizResponse){
            window.fbq(action, event, params);
        }
        </script>

        ```
    4. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
    5. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.

=== "WooCommerce"

    For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

    To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

    1. **Deactivate Meta Pixel**: If you have previously connected a pixel through the [Connect](/reference/quiz-builder/connect-integrations/) tab, you'll have to deactivate it and publish the changes.
    2. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) on custom integrations to learn how our callback function operates and how it can be utilized for tracking custom events.
    3. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located (load it sitewide and put it into the theme.liquid):
        ```html
        <script>
        function prqQuizCallback(quizResponse){
            window.fbq(action, event, params);
        }
        </script>

        ```
    4. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
    5. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.

=== "Magento"

    For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

    To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

    1. **Deactivate Meta Pixel**: If you have previously connected a pixel through the [Connect](/reference/quiz-builder/connect-integrations/) tab, you'll have to deactivate it and publish the changes.
    2. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) on custom integrations to learn how our callback function operates and how it can be utilized for tracking custom events.
    3. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located (load it sitewide and put it into the theme.liquid):
        ```html
        <script>
        function prqQuizCallback(quizResponse){
            window.fbq(action, event, params);
        }
        </script>

        ```
    4. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
    5. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.

=== "BigCommerce"

    For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

    To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

    1. **Deactivate Meta Pixel**: If you have previously connected a pixel through the [Connect](/reference/quiz-builder/connect-integrations/) tab, you'll have to deactivate it and publish the changes.
    2. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) on custom integrations to learn how our callback function operates and how it can be utilized for tracking custom events.
    3. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located (load it sitewide and put it into the theme.liquid):
        ```html
        <script>
        function prqQuizCallback(quizResponse){
            window.fbq(action, event, params);
        }
        </script>

        ```
    4. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
    5. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.

=== "Standalone"

    For an alternative approach to tracking user interactions, consider implementing custom JavaScript to measure specific events on your site. By incorporating our [callback function](/how-to-guides/use-callback-function/), you have the capability to manually trigger or log events based on user actions.

    To deploy this method, you can insert a script within the theme of your store's page, especially where a quiz is featured. Follow these steps:

    1. **Deactivate Meta Pixel**: If you have previously connected a pixel through the [Connect](/reference/quiz-builder/connect-integrations/) tab, you'll have to deactivate it and publish the changes.
    2. **Understand the Callback Function**: Visit the [FAQ page](/how-to-guides/use-callback-function/) on custom integrations to learn how our callback function operates and how it can be utilized for tracking custom events.
    3. **Embed the Custom Script**: Insert the following script into the theme of your store’s page where the quiz or the event you want to track is located (load it sitewide and put it into the theme.liquid):
        ```html
        <script>
        function prqQuizCallback(quizResponse){
            window.fbq(action, event, params);
        }
        </script>

        ```
    4. **Customize Your Event Tracking**: In the script, replace the values with the appropriate event name, action, and params that you wish to track. This customization allows you to monitor specific user actions on your website.
    5. **Monitor and Adjust**: After the script is active and events are being tracked, regularly monitor the data to ensure everything is working as intended. Be prepared to make adjustments to the script or event definitions as needed.

---
This article explains how to integrate the Meta Pixel with your quiz application and how to use the Meta Events Manager to track user interactions with your quiz.

