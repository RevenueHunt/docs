---
icon: material/code-json
---

# How to Use Callback Function for Custom Integrations

Custom integrations are essential for developers looking to enhance the functionality of their websites, especially when it comes to tailoring user experiences. One powerful tool for achieving such customization is through the use of JavaScript **callback functions**. 

This guide will walk you through the process of using a callback function for custom integrations with Shop Quiz: Product Recommendation Quiz. Whether you're aiming to build your own results page, add unique code, display custom product recommendations, or direct users to specific pages on your store, callback functions offer a versatile solution.

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

    Note that this callback function will also be triggered if your customers reach the results page via [follow-up emails](https://docs.revenuehunt.com/how-to-guides/send-result-emails/) you send your customers with a link to their results.


## Implementing the Callback Function

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

![how use callback function example](/images/how use callback function example.png)

---
By following the steps outlined in this guide, you can effectively tap into quiz responses, offering personalized content and interactions based on user inputs.