---
icon: material/code-json
---

# How to Use Callback Function for Custom Integrations

=== "Shopify (Legacy)"

      Custom integrations are essential for developers looking to enhance the functionality of their websites, especially when it comes to tailoring user experiences. One powerful tool for achieving such customization is through the use of JavaScript **callback functions**. 

      This guide will walk you through the process of using a callback function for custom integrations with Product Recommendation Quiz. Whether you're aiming to build your own results page, add unique code, display custom product recommendations, or direct users to specific pages on your store, callback functions offer a versatile solution.


=== "Shopify"

    !!! warning

        The callback function is not supported in Shopify V2.

    The callback function is not supported in Shopify V2. However, the new quiz version's results page includes powerful features such as conditionally displaying sections based on quiz answers or custom scores, adding custom JavaScript, and showcasing fixed products. It also offers advanced layout and alignment options, allowing you to create a unique and fully customized results page—without needing to redirect users to an external page.

=== "WooCommerce"

    Custom integrations are essential for developers looking to enhance the functionality of their websites, especially when it comes to tailoring user experiences. One powerful tool for achieving such customization is through the use of JavaScript **callback functions**. 

    This guide will walk you through the process of using a callback function for custom integrations with Product Recommendation Quiz. Whether you're aiming to build your own results page, add unique code, display custom product recommendations, or direct users to specific pages on your store, callback functions offer a versatile solution.


=== "Magento"

    Custom integrations are essential for developers looking to enhance the functionality of their websites, especially when it comes to tailoring user experiences. One powerful tool for achieving such customization is through the use of JavaScript **callback functions**. 

    This guide will walk you through the process of using a callback function for custom integrations with Product Recommendation Quiz. Whether you're aiming to build your own results page, add unique code, display custom product recommendations, or direct users to specific pages on your store, callback functions offer a versatile solution.


=== "BigCommerce"

    Custom integrations are essential for developers looking to enhance the functionality of their websites, especially when it comes to tailoring user experiences. One powerful tool for achieving such customization is through the use of JavaScript **callback functions**. 

    This guide will walk you through the process of using a callback function for custom integrations with Product Recommendation Quiz. Whether you're aiming to build your own results page, add unique code, display custom product recommendations, or direct users to specific pages on your store, callback functions offer a versatile solution.


=== "Standalone"

    Custom integrations are essential for developers looking to enhance the functionality of their websites, especially when it comes to tailoring user experiences. One powerful tool for achieving such customization is through the use of JavaScript **callback functions**. 

    This guide will walk you through the process of using a callback function for custom integrations with Product Recommendation Quiz. Whether you're aiming to build your own results page, add unique code, display custom product recommendations, or direct users to specific pages on your store, callback functions offer a versatile solution.


## What Are Callback Functions?

A **callback function** is a piece of JavaScript code that executes in response to an event - in this case, the completion of a quiz. You add this callback function to your website and a listener that will be triggered when the quiz is completed. Then you will have access to all the data from quiz responses.

By tapping into the quiz responses, developers can access a wealth of information including individual answers, customer tags, and recommended products. This data is delivered in a **JSON format** via a JavaScript Callback Function, enabling you to add it directly to your website.

The JSON with the quiz response includes:

- The complete set of questions that were asked
- The responses your customer gave
- The customer tags that were assigned to that customer
- The products that were recommended
- The layout and logic of the results page blocks 

!!! note

    Note that this callback function will also be triggered if your customers reach the results page via [follow-up emails](/how-to-guides/send-result-emails/) you send your customers with a link to their results.


## Implementing the Callback Function

=== "Shopify (Legacy)"

    1. **Initial Setup**: To begin, insert the following code into your store's theme, ideally just before the closing `</head>` tag:
      ```html
      <script>
        function prqQuizCallback(quizResponse){
          console.log(quizResponse);
        }
      </script>
      ```
        This simple example utilizes a `console.log()` function to output the JSON containing all the quiz response data. However, this is merely a starting point. Developers are encouraged to tailor the above callback function to meet their specific needs.
    2. **Store the Data**: Confirm that the callback response is being correctly stored on your website. An effective method involves wrapping the redirection logic within the callback function itself. This ensures the data is mapped or saved before any redirection takes place. For example:
        ```javascript
        function prqQuizCallback(quizResponse) {
        // Code to map or save the data...

        // Then, redirect the user to the desired page:
        window.location.href = 'yourTargetURLHere';
        }
        ```
        Choose an appropriate storage solution for the callback response, such as cookies, local storage, or even as query parameters in the URL, depending on your specific needs and the nature of the data.

    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage, before any redirection occurs. It's critical to ensure the results page is accessed even for a fraction of a second to allow this process to unfold correctly.
    4. **Customize the Function**: Beyond merely logging the data, you might want to trigger specific actions based on the quiz outcomes. *For instance, introducing a `prqAddOneToCartCallback(event);` function could be used when a customer adds a product to their cart directly from the quiz results.*
        - There are several other callback functions you can utilize for more granular control and interaction with the quiz results. 
          ```html
          prqSlideCallback(event);
          // triggered when customer responds to a question (slide)

          prqAddOneToCartCallback(event);
          // triggered when customer adds one product to cart 

          prqAddedOneToCartCallback(event);
          // triggered when the product has already been added to the cart 
        
          prqRemoveOneFromCartCallback(event);
          // triggered when customer removes one product from cart 

          prqRemovedOneFromCartCallback(event);
          // triggered when the product has already been removed from the cart (only Shopify) 

          prqAddAllToCartCallback(event); 
          // triggered when customer adds all products to cart 

          prqAddedAllToCartCallback(event);
          // triggered when all the products have already been added to the cart 

          prqAppLoadedCallback();
          // triggered when the Product Recommendation Quiz app has been loaded 
          ```

=== "Shopify"

    !!! warning

        Not supported in this version of the RevenueHunt app. 

    Not supported in this version of the RevenueHunt app.  However, the new quiz version's results page includes powerful features such as conditionally displaying sections based on quiz answers or custom scores, adding custom JavaScript, and showcasing fixed products. It also offers advanced layout and alignment options, allowing you to create a unique and fully customized results page—without needing to redirect users to an external page.


=== "WooCommerce"


    1. **Initial Setup**: To begin, insert the following code into your store's theme, ideally just before the closing `</head>` tag:
      ```html
      <script>
        function prqQuizCallback(quizResponse){
          console.log(quizResponse);
        }
      </script>
      ```
        This simple example utilizes a `console.log()` function to output the JSON containing all the quiz response data. However, this is merely a starting point. Developers are encouraged to tailor the above callback function to meet their specific needs.
    2. **Store the Data**: Confirm that the callback response is being correctly stored on your website. An effective method involves wrapping the redirection logic within the callback function itself. This ensures the data is mapped or saved before any redirection takes place. For example:
        ```javascript
        function prqQuizCallback(quizResponse) {
        // Code to map or save the data...

        // Then, redirect the user to the desired page:
        window.location.href = 'yourTargetURLHere';
        }
        ```
        Choose an appropriate storage solution for the callback response, such as cookies, local storage, or even as query parameters in the URL, depending on your specific needs and the nature of the data.

    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage, before any redirection occurs. It's critical to ensure the results page is accessed even for a fraction of a second to allow this process to unfold correctly.
    4. **Customize the Function**: Beyond merely logging the data, you might want to trigger specific actions based on the quiz outcomes. *For instance, introducing a `prqAddOneToCartCallback(event);` function could be used when a customer adds a product to their cart directly from the quiz results.*
        - There are several other callback functions you can utilize for more granular control and interaction with the quiz results. 
          ```html
          prqSlideCallback(event);
          // triggered when customer responds to a question (slide)

          prqAddOneToCartCallback(event);
          // triggered when customer adds one product to cart 

          prqAddedOneToCartCallback(event);
          // triggered when the product has already been added to the cart 
        
          prqRemoveOneFromCartCallback(event);
          // triggered when customer removes one product from cart 

          prqRemovedOneFromCartCallback(event);
          // triggered when the product has already been removed from the cart (only Shopify) 

          prqAddAllToCartCallback(event); 
          // triggered when customer adds all products to cart 

          prqAddedAllToCartCallback(event);
          // triggered when all the products have already been added to the cart 

          prqAppLoadedCallback();
          // triggered when the Product Recommendation Quiz app has been loaded 
          ```

=== "Magento"


    1. **Initial Setup**: To begin, insert the following code into your store's theme, ideally just before the closing `</head>` tag:
      ```html
      <script>
        function prqQuizCallback(quizResponse){
          console.log(quizResponse);
        }
      </script>
      ```
        This simple example utilizes a `console.log()` function to output the JSON containing all the quiz response data. However, this is merely a starting point. Developers are encouraged to tailor the above callback function to meet their specific needs.
    2. **Store the Data**: Confirm that the callback response is being correctly stored on your website. An effective method involves wrapping the redirection logic within the callback function itself. This ensures the data is mapped or saved before any redirection takes place. For example:
        ```javascript
        function prqQuizCallback(quizResponse) {
        // Code to map or save the data...

        // Then, redirect the user to the desired page:
        window.location.href = 'yourTargetURLHere';
        }
        ```
        Choose an appropriate storage solution for the callback response, such as cookies, local storage, or even as query parameters in the URL, depending on your specific needs and the nature of the data.

    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage, before any redirection occurs. It's critical to ensure the results page is accessed even for a fraction of a second to allow this process to unfold correctly.
    4. **Customize the Function**: Beyond merely logging the data, you might want to trigger specific actions based on the quiz outcomes. *For instance, introducing a `prqAddOneToCartCallback(event);` function could be used when a customer adds a product to their cart directly from the quiz results.*
        - There are several other callback functions you can utilize for more granular control and interaction with the quiz results. 
          ```html
          prqSlideCallback(event);
          // triggered when customer responds to a question (slide)

          prqAddOneToCartCallback(event);
          // triggered when customer adds one product to cart 

          prqAddedOneToCartCallback(event);
          // triggered when the product has already been added to the cart 
        
          prqRemoveOneFromCartCallback(event);
          // triggered when customer removes one product from cart 

          prqRemovedOneFromCartCallback(event);
          // triggered when the product has already been removed from the cart (only Shopify) 

          prqAddAllToCartCallback(event); 
          // triggered when customer adds all products to cart 

          prqAddedAllToCartCallback(event);
          // triggered when all the products have already been added to the cart 

          prqAppLoadedCallback();
          // triggered when the Product Recommendation Quiz app has been loaded 
          ```

=== "BigCommerce"


    1. **Initial Setup**: To begin, insert the following code into your store's theme, ideally just before the closing `</head>` tag:
      ```html
      <script>
        function prqQuizCallback(quizResponse){
          console.log(quizResponse);
        }
      </script>
      ```
        This simple example utilizes a `console.log()` function to output the JSON containing all the quiz response data. However, this is merely a starting point. Developers are encouraged to tailor the above callback function to meet their specific needs.
    2. **Store the Data**: Confirm that the callback response is being correctly stored on your website. An effective method involves wrapping the redirection logic within the callback function itself. This ensures the data is mapped or saved before any redirection takes place. For example:
        ```javascript
        function prqQuizCallback(quizResponse) {
        // Code to map or save the data...

        // Then, redirect the user to the desired page:
        window.location.href = 'yourTargetURLHere';
        }
        ```
        Choose an appropriate storage solution for the callback response, such as cookies, local storage, or even as query parameters in the URL, depending on your specific needs and the nature of the data.

    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage, before any redirection occurs. It's critical to ensure the results page is accessed even for a fraction of a second to allow this process to unfold correctly.
    4. **Customize the Function**: Beyond merely logging the data, you might want to trigger specific actions based on the quiz outcomes. *For instance, introducing a `prqAddOneToCartCallback(event);` function could be used when a customer adds a product to their cart directly from the quiz results.*
        - There are several other callback functions you can utilize for more granular control and interaction with the quiz results. 
          ```html
          prqSlideCallback(event);
          // triggered when customer responds to a question (slide)

          prqAddOneToCartCallback(event);
          // triggered when customer adds one product to cart 

          prqAddedOneToCartCallback(event);
          // triggered when the product has already been added to the cart 
        
          prqRemoveOneFromCartCallback(event);
          // triggered when customer removes one product from cart 

          prqRemovedOneFromCartCallback(event);
          // triggered when the product has already been removed from the cart (only Shopify) 

          prqAddAllToCartCallback(event); 
          // triggered when customer adds all products to cart 

          prqAddedAllToCartCallback(event);
          // triggered when all the products have already been added to the cart 

          prqAppLoadedCallback();
          // triggered when the Product Recommendation Quiz app has been loaded 
          ```

=== "Standalone"

    1. **Initial Setup**: To begin, insert the following code into your store's theme, ideally just before the closing `</head>` tag:
      ```html
      <script>
        function prqQuizCallback(quizResponse){
          console.log(quizResponse);
        }
      </script>
      ```
        This simple example utilizes a `console.log()` function to output the JSON containing all the quiz response data. However, this is merely a starting point. Developers are encouraged to tailor the above callback function to meet their specific needs.
    2. **Store the Data**: Confirm that the callback response is being correctly stored on your website. An effective method involves wrapping the redirection logic within the callback function itself. This ensures the data is mapped or saved before any redirection takes place. For example:
        ```javascript
        function prqQuizCallback(quizResponse) {
        // Code to map or save the data...

        // Then, redirect the user to the desired page:
        window.location.href = 'yourTargetURLHere';
        }
        ```
        Choose an appropriate storage solution for the callback response, such as cookies, local storage, or even as query parameters in the URL, depending on your specific needs and the nature of the data.

    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage, before any redirection occurs. It's critical to ensure the results page is accessed even for a fraction of a second to allow this process to unfold correctly.
    4. **Customize the Function**: Beyond merely logging the data, you might want to trigger specific actions based on the quiz outcomes. *For instance, introducing a `prqAddOneToCartCallback(event);` function could be used when a customer adds a product to their cart directly from the quiz results.*
        - There are several other callback functions you can utilize for more granular control and interaction with the quiz results. 
          ```html
          prqSlideCallback(event);
          // triggered when customer responds to a question (slide)

          prqAddOneToCartCallback(event);
          // triggered when customer adds one product to cart 

          prqAddedOneToCartCallback(event);
          // triggered when the product has already been added to the cart 
        
          prqRemoveOneFromCartCallback(event);
          // triggered when customer removes one product from cart 

          prqRemovedOneFromCartCallback(event);
          // triggered when the product has already been removed from the cart (only Shopify) 

          prqAddAllToCartCallback(event); 
          // triggered when customer adds all products to cart 

          prqAddedAllToCartCallback(event);
          // triggered when all the products have already been added to the cart 

          prqAppLoadedCallback();
          // triggered when the Product Recommendation Quiz app has been loaded 
          ```


## Seeing Callback Function in Action

For a practical demonstration of the callback function at work, visit the demo store at [https://skincarequiz.myshopify.com/](https://skincarequiz.myshopify.com/). Here, you can witness how the quiz responses are handled in a live environment, providing a clearer understanding of the process.

![how use callback function example](/images/how_use_callback_function_example.png)


## Making sense of the Callback’s JSON Object

You will find some of the most important data points on the object within the following locations:

### General Data

![how to callback image1](/images/how_to_callback_image1.png)

On the Quiz section, you will find the following entries:

- **Attributes**: You can find most of the quiz information within this object. Some interesting data points include:
- **ID**: You can see/copy the ID of the quiz here.
- **Type**: Quiz

### ⤵ Attributes Object

![how to callback image2](/images/how_to_callback_image2.png)

!!! note

    Some of the data points have more properties than others, for example, logic, messages, preferences…

- **Logic**: The conditional logic rules you’ve used on the quiz slides.
- **Messages**: The text contained within buttons (for example, proceed to cart or see product).
- **Name**: Name of the Quiz.
- **Preferences**: The preferences/settings of the Quiz.
- **⤵ Results**: One of the composite objects. Here you will find the result’s page blocks:
  ![how to callback image3](/images/how_to_callback_image3.png)
  
    One entry in the data array for each block you add:
    ![how to callback image4](/images/how_to_callback_image4.png)

- **⤵ Slides**: One of the most interesting sections:
  ![how to callback image5](/images/how_to_callback_image5.png)

    In here, you will find “data”, which contains each of the slides, or questions, you’re using. On each of the slide objects, you can find all the information related to it:
    ![how to callback image6](/images/how_to_callback_image6.png)
    
    ID of the slide and the **⤵ attribute** object with more data. 
    
    Let’s open the **⤵ attributes** to better understand which information is contained in it:
    ![how to callback image7](/images/how_to_callback_image7.png)

    **⤵ Slides >  ⤵ attributes**

    - **Choices**: You can find all the possible choices a respondent can choose here.
    - **Description**: If you [add a description](/reference/quiz-builder/questions/#question-settings) to your slide (`question settings → Show description`), you will see your text here.
    - **Preferences**: All preferences related to how your respondents select your choices.
    - **Slide type**: The type of slide.
    - **Title**: The text you’ve written as the title of the slide.
    - **Validations**: More settings of the question, such as if it's an optional question or not, and how many items/choices they were allowed to select.
    - **Values**: One of the most important data points, **which answers were selected**. You will note they’re expressed in IDs.

!!! question "How to Know Which Choice the ID(s) Represent?"

    You can simply make a test response, see what option you selected, and jot down the IDs of each response that way. An alternative would be to inspect the element of the choice to see the ID:
    ![how to callback image8](/images/how_to_callback_image8.png)

    *The ID of this one is `36HzG42` - just take the number after `#choice-[your ID here]`.*

- **⤵ Theme**

  On the Theme, you will find all attributes of the quiz look & feel:

  - **Background Image**: (if you added one) and its opacity.
  - **Colors**: The colors used throughout the quiz.
  - **Custom CSS**: If you’ve done so; custom fonts will appear here.
  - **Font**: The main font being used (or fallback if there’s an issue with your custom-embedded font).
  - **Name**: Name of the theme used.

![how to callback image9](/images/how_to_callback_image9.png)

More information and data points are available throughout the callback function. You or your developer can also copy the object and paste it into their preferred software for visualizing JSON objects for more clarity and organization.




---
By following the steps outlined in this guide, you can effectively tap into quiz responses, offering personalized content and interactions based on user inputs.