---
icon: material/code-json
description: "Learn about using callback functions for custom integrations with RevenueHunt quiz."
---

# How to Use Callback Function for Custom Integrations

=== "Shopify"

    This version has no callback functions. The results page does the same work inside the app.

    - Show or hide sections with [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic), based on answers, variables or a score.
    - Pin the products for an outcome with [Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/).
    - Run your own code on the results page with [Custom JavaScript](/how-to-guides/add-javascript/), where the `window.quiz` object holds the response.

    Between them you can build a fully custom results page, without sending the customer to a page of your own.

=== "Shopify (Legacy)"

    A callback function is JavaScript that runs when the quiz fires an event, such as a customer finishing the quiz. You define the function on your site, the quiz calls it, and everything the customer did arrives as JSON.

    That gives a developer the material to build a results page of their own, save the answers, or send the customer somewhere specific.

    The response JSON holds:

    - Every question that was asked
    - The answers the customer gave
    - The customer tags that were assigned
    - The products that were recommended
    - The layout and logic of the results page blocks

    !!! note "Follow-up email links fire the callback too"

        The callback runs whenever the results page is reached, including when a customer opens their results from a [follow-up email](/how-to-guides/send-result-emails/).

=== "WooCommerce"

    A callback function is JavaScript that runs when the quiz fires an event, such as a customer finishing the quiz. You define the function on your site, the quiz calls it, and everything the customer did arrives as JSON.

    That gives a developer the material to build a results page of their own, save the answers, or send the customer somewhere specific.

    The response JSON holds:

    - Every question that was asked
    - The answers the customer gave
    - The customer tags that were assigned
    - The products that were recommended
    - The layout and logic of the results page blocks

    !!! note "Follow-up email links fire the callback too"

        The callback runs whenever the results page is reached, including when a customer opens their results from a [follow-up email](/how-to-guides/send-result-emails/).

=== "Magento"

    A callback function is JavaScript that runs when the quiz fires an event, such as a customer finishing the quiz. You define the function on your site, the quiz calls it, and everything the customer did arrives as JSON.

    That gives a developer the material to build a results page of their own, save the answers, or send the customer somewhere specific.

    The response JSON holds:

    - Every question that was asked
    - The answers the customer gave
    - The customer tags that were assigned
    - The products that were recommended
    - The layout and logic of the results page blocks

    !!! note "Follow-up email links fire the callback too"

        The callback runs whenever the results page is reached, including when a customer opens their results from a [follow-up email](/how-to-guides/send-result-emails/).

=== "BigCommerce"

    A callback function is JavaScript that runs when the quiz fires an event, such as a customer finishing the quiz. You define the function on your site, the quiz calls it, and everything the customer did arrives as JSON.

    That gives a developer the material to build a results page of their own, save the answers, or send the customer somewhere specific.

    The response JSON holds:

    - Every question that was asked
    - The answers the customer gave
    - The customer tags that were assigned
    - The products that were recommended
    - The layout and logic of the results page blocks

    !!! note "Follow-up email links fire the callback too"

        The callback runs whenever the results page is reached, including when a customer opens their results from a [follow-up email](/how-to-guides/send-result-emails/).

=== "Standalone"

    A callback function is JavaScript that runs when the quiz fires an event, such as a customer finishing the quiz. You define the function on your site, the quiz calls it, and everything the customer did arrives as JSON.

    That gives a developer the material to build a results page of their own, save the answers, or send the customer somewhere specific.

    The response JSON holds:

    - Every question that was asked
    - The answers the customer gave
    - The customer tags that were assigned
    - The products that were recommended
    - The layout and logic of the results page blocks

    !!! note "Follow-up email links fire the callback too"

        The callback runs whenever the results page is reached, including when a customer opens their results from a [follow-up email](/how-to-guides/send-result-emails/).

## Set up the callback

=== "Shopify"

    Use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. The `window.quiz` object holds the quiz, the answers and the recommended products.

=== "Shopify (Legacy)"

    1. **Add the callback to your theme, just before the closing `</head>` tag.**

        ```html
        <script>
          function prqQuizCallback(quizResponse){
            console.log(quizResponse);
          }
        </script>
        ```

        This logs the whole response JSON to the console. It is a starting point: replace the body with whatever your integration needs.

    2. **Store the response before anything else happens.** Wrap any redirect inside the callback, so the data is saved first.

        ```javascript
        function prqQuizCallback(quizResponse) {
          // Code to map or save the data...

          // Then, redirect the user to the desired page:
          window.location.href = 'yourTargetURLHere';
        }
        ```

        Cookies, local storage or query parameters all work. Pick whichever suits the data.

    3. **Let the customer reach the results page.** The callback only fires there. Even a fraction of a second is enough. A redirect that skips the results page skips the callback too.

    4. **Add the other callbacks you need.** Each one is a global function the quiz calls when its event happens.

        ```javascript
        function prqAddOneToCartCallback(event) {
          // runs when a customer adds one product to the cart
        }
        ```

=== "WooCommerce"

    1. **Add the callback to your theme, just before the closing `</head>` tag.**

        ```html
        <script>
          function prqQuizCallback(quizResponse){
            console.log(quizResponse);
          }
        </script>
        ```

        This logs the whole response JSON to the console. It is a starting point: replace the body with whatever your integration needs.

    2. **Store the response before anything else happens.** Wrap any redirect inside the callback, so the data is saved first.

        ```javascript
        function prqQuizCallback(quizResponse) {
          // Code to map or save the data...

          // Then, redirect the user to the desired page:
          window.location.href = 'yourTargetURLHere';
        }
        ```

        Cookies, local storage or query parameters all work. Pick whichever suits the data.

    3. **Let the customer reach the results page.** The callback only fires there. Even a fraction of a second is enough. A redirect that skips the results page skips the callback too.

    4. **Add the other callbacks you need.** Each one is a global function the quiz calls when its event happens.

        ```javascript
        function prqAddOneToCartCallback(event) {
          // runs when a customer adds one product to the cart
        }
        ```

=== "Magento"

    1. **Add the callback to your theme, just before the closing `</head>` tag.**

        ```html
        <script>
          function prqQuizCallback(quizResponse){
            console.log(quizResponse);
          }
        </script>
        ```

        This logs the whole response JSON to the console. It is a starting point: replace the body with whatever your integration needs.

    2. **Store the response before anything else happens.** Wrap any redirect inside the callback, so the data is saved first.

        ```javascript
        function prqQuizCallback(quizResponse) {
          // Code to map or save the data...

          // Then, redirect the user to the desired page:
          window.location.href = 'yourTargetURLHere';
        }
        ```

        Cookies, local storage or query parameters all work. Pick whichever suits the data.

    3. **Let the customer reach the results page.** The callback only fires there. Even a fraction of a second is enough. A redirect that skips the results page skips the callback too.

    4. **Add the other callbacks you need.** Each one is a global function the quiz calls when its event happens.

        ```javascript
        function prqAddOneToCartCallback(event) {
          // runs when a customer adds one product to the cart
        }
        ```

=== "BigCommerce"

    1. **Add the callback to your theme, just before the closing `</head>` tag.**

        ```html
        <script>
          function prqQuizCallback(quizResponse){
            console.log(quizResponse);
          }
        </script>
        ```

        This logs the whole response JSON to the console. It is a starting point: replace the body with whatever your integration needs.

    2. **Store the response before anything else happens.** Wrap any redirect inside the callback, so the data is saved first.

        ```javascript
        function prqQuizCallback(quizResponse) {
          // Code to map or save the data...

          // Then, redirect the user to the desired page:
          window.location.href = 'yourTargetURLHere';
        }
        ```

        Cookies, local storage or query parameters all work. Pick whichever suits the data.

    3. **Let the customer reach the results page.** The callback only fires there. Even a fraction of a second is enough. A redirect that skips the results page skips the callback too.

    4. **Add the other callbacks you need.** Each one is a global function the quiz calls when its event happens.

        ```javascript
        function prqAddOneToCartCallback(event) {
          // runs when a customer adds one product to the cart
        }
        ```

=== "Standalone"

    1. **Add the callback to your theme, just before the closing `</head>` tag.**

        ```html
        <script>
          function prqQuizCallback(quizResponse){
            console.log(quizResponse);
          }
        </script>
        ```

        This logs the whole response JSON to the console. It is a starting point: replace the body with whatever your integration needs.

    2. **Store the response before anything else happens.** Wrap any redirect inside the callback, so the data is saved first.

        ```javascript
        function prqQuizCallback(quizResponse) {
          // Code to map or save the data...

          // Then, redirect the user to the desired page:
          window.location.href = 'yourTargetURLHere';
        }
        ```

        Cookies, local storage or query parameters all work. Pick whichever suits the data.

    3. **Let the customer reach the results page.** The callback only fires there. Even a fraction of a second is enough. A redirect that skips the results page skips the callback too.

    4. **Add the other callbacks you need.** Each one is a global function the quiz calls when its event happens.

        ```javascript
        function prqAddOneToCartCallback(event) {
          // runs when a customer adds one product to the cart
        }
        ```

## Callback reference

=== "Shopify"

    Use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. The `window.quiz` object holds the quiz, the answers and the recommended products.

=== "Shopify (Legacy)"

    Each callback is a global function you define on the page where the quiz is embedded, or sitewide in your theme. The quiz calls it when the matching event happens and passes it an `event` object. Define only the callbacks you need.

    | Callback | Fires when | Argument |
    |----------|------------|----------|
    | `prqQuizCallback(response)` | The customer reaches the **results page**, including through a [follow-up email](/how-to-guides/send-result-emails/) link | The full response object |
    | `prqSlideCallback(event)` | The customer **answers a question** and moves to the next slide | `event.quiz` and `event.slide`, the answered question with its `attributes.values` and `attributes.choices` |
    | `prqAddOneToCartCallback(event)` | The customer adds one product to the cart | the product or event |
    | `prqAddedOneToCartCallback(event)` | A product has finished being added to the cart | the product or event |
    | `prqRemoveOneFromCartCallback(event)` | The customer removes one product from the cart | the product or event |
    | `prqRemovedOneFromCartCallback(event)` | A product has finished being removed from the cart, Shopify only | the product or event |
    | `prqAddAllToCartCallback(event)` | The customer adds all recommended products to the cart | the products or event |
    | `prqAddedAllToCartCallback(event)` | All products have finished being added to the cart | the products or event |
    | `prqAppLoadedCallback()` | The quiz app has finished **loading** on the page | none |

    !!! note "There is no quiz-start callback"

        `prqAppLoadedCallback` fires when the embed finishes loading, **not** when the customer starts the quiz. The earliest callback tied to what the customer does is `prqSlideCallback`, which fires when they answer the first question.

    The argument passed to `prqQuizCallback` has this top-level shape:

    - `quiz` is the quiz definition. It includes `quiz.attributes.name` and `quiz.attributes.slides.data[]`, every question with its `attributes.choices` and its selected `attributes.values`.
    - `quizid` is the ID of the quiz.
    - `response` is the customer's submission:
        - `response.attributes.recommended_products` holds the products recommended on the results page.
        - `response.attributes.selected_result.data` holds the result the customer landed on.

    The object carries much more, including theme, logic and layout blocks. The quickest way to see all of it is to `console.log(response)` inside `prqQuizCallback` and take the quiz once.

=== "WooCommerce"

    Each callback is a global function you define on the page where the quiz is embedded, or sitewide in your theme. The quiz calls it when the matching event happens and passes it an `event` object. Define only the callbacks you need.

    | Callback | Fires when | Argument |
    |----------|------------|----------|
    | `prqQuizCallback(response)` | The customer reaches the **results page**, including through a [follow-up email](/how-to-guides/send-result-emails/) link | The full response object |
    | `prqSlideCallback(event)` | The customer **answers a question** and moves to the next slide | `event.quiz` and `event.slide`, the answered question with its `attributes.values` and `attributes.choices` |
    | `prqAddOneToCartCallback(event)` | The customer adds one product to the cart | the product or event |
    | `prqAddedOneToCartCallback(event)` | A product has finished being added to the cart | the product or event |
    | `prqRemoveOneFromCartCallback(event)` | The customer removes one product from the cart | the product or event |
    | `prqRemovedOneFromCartCallback(event)` | A product has finished being removed from the cart, Shopify only | the product or event |
    | `prqAddAllToCartCallback(event)` | The customer adds all recommended products to the cart | the products or event |
    | `prqAddedAllToCartCallback(event)` | All products have finished being added to the cart | the products or event |
    | `prqAppLoadedCallback()` | The quiz app has finished **loading** on the page | none |

    !!! note "There is no quiz-start callback"

        `prqAppLoadedCallback` fires when the embed finishes loading, **not** when the customer starts the quiz. The earliest callback tied to what the customer does is `prqSlideCallback`, which fires when they answer the first question.

    The argument passed to `prqQuizCallback` has this top-level shape:

    - `quiz` is the quiz definition. It includes `quiz.attributes.name` and `quiz.attributes.slides.data[]`, every question with its `attributes.choices` and its selected `attributes.values`.
    - `quizid` is the ID of the quiz.
    - `response` is the customer's submission:
        - `response.attributes.recommended_products` holds the products recommended on the results page.
        - `response.attributes.selected_result.data` holds the result the customer landed on.

    The object carries much more, including theme, logic and layout blocks. The quickest way to see all of it is to `console.log(response)` inside `prqQuizCallback` and take the quiz once.

=== "Magento"

    Each callback is a global function you define on the page where the quiz is embedded, or sitewide in your theme. The quiz calls it when the matching event happens and passes it an `event` object. Define only the callbacks you need.

    | Callback | Fires when | Argument |
    |----------|------------|----------|
    | `prqQuizCallback(response)` | The customer reaches the **results page**, including through a [follow-up email](/how-to-guides/send-result-emails/) link | The full response object |
    | `prqSlideCallback(event)` | The customer **answers a question** and moves to the next slide | `event.quiz` and `event.slide`, the answered question with its `attributes.values` and `attributes.choices` |
    | `prqAddOneToCartCallback(event)` | The customer adds one product to the cart | the product or event |
    | `prqAddedOneToCartCallback(event)` | A product has finished being added to the cart | the product or event |
    | `prqRemoveOneFromCartCallback(event)` | The customer removes one product from the cart | the product or event |
    | `prqRemovedOneFromCartCallback(event)` | A product has finished being removed from the cart, Shopify only | the product or event |
    | `prqAddAllToCartCallback(event)` | The customer adds all recommended products to the cart | the products or event |
    | `prqAddedAllToCartCallback(event)` | All products have finished being added to the cart | the products or event |
    | `prqAppLoadedCallback()` | The quiz app has finished **loading** on the page | none |

    !!! note "There is no quiz-start callback"

        `prqAppLoadedCallback` fires when the embed finishes loading, **not** when the customer starts the quiz. The earliest callback tied to what the customer does is `prqSlideCallback`, which fires when they answer the first question.

    The argument passed to `prqQuizCallback` has this top-level shape:

    - `quiz` is the quiz definition. It includes `quiz.attributes.name` and `quiz.attributes.slides.data[]`, every question with its `attributes.choices` and its selected `attributes.values`.
    - `quizid` is the ID of the quiz.
    - `response` is the customer's submission:
        - `response.attributes.recommended_products` holds the products recommended on the results page.
        - `response.attributes.selected_result.data` holds the result the customer landed on.

    The object carries much more, including theme, logic and layout blocks. The quickest way to see all of it is to `console.log(response)` inside `prqQuizCallback` and take the quiz once.

=== "BigCommerce"

    Each callback is a global function you define on the page where the quiz is embedded, or sitewide in your theme. The quiz calls it when the matching event happens and passes it an `event` object. Define only the callbacks you need.

    | Callback | Fires when | Argument |
    |----------|------------|----------|
    | `prqQuizCallback(response)` | The customer reaches the **results page**, including through a [follow-up email](/how-to-guides/send-result-emails/) link | The full response object |
    | `prqSlideCallback(event)` | The customer **answers a question** and moves to the next slide | `event.quiz` and `event.slide`, the answered question with its `attributes.values` and `attributes.choices` |
    | `prqAddOneToCartCallback(event)` | The customer adds one product to the cart | the product or event |
    | `prqAddedOneToCartCallback(event)` | A product has finished being added to the cart | the product or event |
    | `prqRemoveOneFromCartCallback(event)` | The customer removes one product from the cart | the product or event |
    | `prqRemovedOneFromCartCallback(event)` | A product has finished being removed from the cart, Shopify only | the product or event |
    | `prqAddAllToCartCallback(event)` | The customer adds all recommended products to the cart | the products or event |
    | `prqAddedAllToCartCallback(event)` | All products have finished being added to the cart | the products or event |
    | `prqAppLoadedCallback()` | The quiz app has finished **loading** on the page | none |

    !!! note "There is no quiz-start callback"

        `prqAppLoadedCallback` fires when the embed finishes loading, **not** when the customer starts the quiz. The earliest callback tied to what the customer does is `prqSlideCallback`, which fires when they answer the first question.

    The argument passed to `prqQuizCallback` has this top-level shape:

    - `quiz` is the quiz definition. It includes `quiz.attributes.name` and `quiz.attributes.slides.data[]`, every question with its `attributes.choices` and its selected `attributes.values`.
    - `quizid` is the ID of the quiz.
    - `response` is the customer's submission:
        - `response.attributes.recommended_products` holds the products recommended on the results page.
        - `response.attributes.selected_result.data` holds the result the customer landed on.

    The object carries much more, including theme, logic and layout blocks. The quickest way to see all of it is to `console.log(response)` inside `prqQuizCallback` and take the quiz once.

=== "Standalone"

    Each callback is a global function you define on the page where the quiz is embedded, or sitewide in your theme. The quiz calls it when the matching event happens and passes it an `event` object. Define only the callbacks you need.

    | Callback | Fires when | Argument |
    |----------|------------|----------|
    | `prqQuizCallback(response)` | The customer reaches the **results page**, including through a [follow-up email](/how-to-guides/send-result-emails/) link | The full response object |
    | `prqSlideCallback(event)` | The customer **answers a question** and moves to the next slide | `event.quiz` and `event.slide`, the answered question with its `attributes.values` and `attributes.choices` |
    | `prqAddOneToCartCallback(event)` | The customer adds one product to the cart | the product or event |
    | `prqAddedOneToCartCallback(event)` | A product has finished being added to the cart | the product or event |
    | `prqRemoveOneFromCartCallback(event)` | The customer removes one product from the cart | the product or event |
    | `prqRemovedOneFromCartCallback(event)` | A product has finished being removed from the cart, Shopify only | the product or event |
    | `prqAddAllToCartCallback(event)` | The customer adds all recommended products to the cart | the products or event |
    | `prqAddedAllToCartCallback(event)` | All products have finished being added to the cart | the products or event |
    | `prqAppLoadedCallback()` | The quiz app has finished **loading** on the page | none |

    !!! note "There is no quiz-start callback"

        `prqAppLoadedCallback` fires when the embed finishes loading, **not** when the customer starts the quiz. The earliest callback tied to what the customer does is `prqSlideCallback`, which fires when they answer the first question.

    The argument passed to `prqQuizCallback` has this top-level shape:

    - `quiz` is the quiz definition. It includes `quiz.attributes.name` and `quiz.attributes.slides.data[]`, every question with its `attributes.choices` and its selected `attributes.values`.
    - `quizid` is the ID of the quiz.
    - `response` is the customer's submission:
        - `response.attributes.recommended_products` holds the products recommended on the results page.
        - `response.attributes.selected_result.data` holds the result the customer landed on.

    The object carries much more, including theme, logic and layout blocks. The quickest way to see all of it is to `console.log(response)` inside `prqQuizCallback` and take the quiz once.

## Read the JSON object

=== "Shopify"

    Use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. The `window.quiz` object holds the quiz, the answers and the recommended products.

=== "Shopify (Legacy)"

    !!! tip "See it running first"

        The [RevenueHunt demo store](https://skincarequiz.myshopify.com/) handles quiz responses live, which is the fastest way to understand the shape of the data.

        ![how use callback function example](/images/how_use_callback_function_example.png)

    The most useful data points sit in these places.

    ![how to callback image1](/images/how_to_callback_image1.png)

    The `Quiz` section holds:

    - **Attributes**: most of the quiz information.
    - **ID**: the ID of the quiz.
    - **Type**: Quiz.

=== "WooCommerce"

    !!! tip "See it running first"

        The [RevenueHunt demo store](https://skincarequiz.myshopify.com/) handles quiz responses live, which is the fastest way to understand the shape of the data.

        ![how use callback function example](/images/how_use_callback_function_example.png)

    The most useful data points sit in these places.

    ![how to callback image1](/images/how_to_callback_image1.png)

    The `Quiz` section holds:

    - **Attributes**: most of the quiz information.
    - **ID**: the ID of the quiz.
    - **Type**: Quiz.

=== "Magento"

    !!! tip "See it running first"

        The [RevenueHunt demo store](https://skincarequiz.myshopify.com/) handles quiz responses live, which is the fastest way to understand the shape of the data.

        ![how use callback function example](/images/how_use_callback_function_example.png)

    The most useful data points sit in these places.

    ![how to callback image1](/images/how_to_callback_image1.png)

    The `Quiz` section holds:

    - **Attributes**: most of the quiz information.
    - **ID**: the ID of the quiz.
    - **Type**: Quiz.

=== "BigCommerce"

    !!! tip "See it running first"

        The [RevenueHunt demo store](https://skincarequiz.myshopify.com/) handles quiz responses live, which is the fastest way to understand the shape of the data.

        ![how use callback function example](/images/how_use_callback_function_example.png)

    The most useful data points sit in these places.

    ![how to callback image1](/images/how_to_callback_image1.png)

    The `Quiz` section holds:

    - **Attributes**: most of the quiz information.
    - **ID**: the ID of the quiz.
    - **Type**: Quiz.

=== "Standalone"

    !!! tip "See it running first"

        The [RevenueHunt demo store](https://skincarequiz.myshopify.com/) handles quiz responses live, which is the fastest way to understand the shape of the data.

        ![how use callback function example](/images/how_use_callback_function_example.png)

    The most useful data points sit in these places.

    ![how to callback image1](/images/how_to_callback_image1.png)

    The `Quiz` section holds:

    - **Attributes**: most of the quiz information.
    - **ID**: the ID of the quiz.
    - **Type**: Quiz.

### The attributes object

=== "Shopify"

    Use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. The `window.quiz` object holds the quiz, the answers and the recommended products.

=== "Shopify (Legacy)"

    ![how to callback image2](/images/how_to_callback_image2.png)

    !!! note "Some entries carry more than others"

        Logic, messages and preferences hold far more data than the rest.

    - **Logic**: the conditional logic rules you used on the quiz slides.
    - **Messages**: the text inside buttons, such as proceed to cart or see product.
    - **Name**: the name of the quiz.
    - **Preferences**: the settings of the quiz.
    - **Results**: the blocks on the results page.

        ![how to callback image3](/images/how_to_callback_image3.png)

        The data array holds one entry per block you added.

        ![how to callback image4](/images/how_to_callback_image4.png)

    - **Slides**: the questions themselves.

        ![how to callback image5](/images/how_to_callback_image5.png)

        `data` holds every slide, and each slide object carries everything about it.

        ![how to callback image6](/images/how_to_callback_image6.png)

        That is the ID of the slide, plus an `attributes` object holding the rest.

        ![how to callback image7](/images/how_to_callback_image7.png)

        Inside `slides > attributes`:

        - **Choices**: every choice a customer can pick.
        - **Description**: the text from [question settings](/reference/quiz-builder/questions/#question-settings), under `question settings → Show description`.
        - **Preferences**: how the customer selects the choices.
        - **Slide type**: the type of slide.
        - **Title**: the title you wrote for the slide.
        - **Validations**: further settings, such as whether the question is optional, and how many choices can be selected.
        - **Values**: which answers were selected, expressed as IDs.

    - **Theme**: the look and feel of the quiz.

        - **Background Image**: the image, if you added one, and its opacity.
        - **Colors**: the colors used through the quiz.
        - **Custom CSS**: your custom CSS, including custom fonts.
        - **Font**: the main font, or the fallback if the embedded font fails.
        - **Name**: the name of the theme.

        ![how to callback image9](/images/how_to_callback_image9.png)

    ??? question "How do I know which choice an ID represents?"

        No separate lookup is needed, because the labels are already in the callback object. Each slide carries its possible choices in `slide.attributes.choices.data[]`, each with an `id` and an `attributes.label`, and the selected answer IDs in `slide.attributes.values`. Match one against the other to read the label:

        ```javascript
        var choices = (slide.attributes.choices && slide.attributes.choices.data) || [];
        var labels = (slide.attributes.values || []).map(function (id) {
          var c = choices.filter(function (x) { return x.id === id; })[0];
          return c ? c.attributes.label : id; // raw value for text/number questions
        });
        ```

        To read an ID straight off the page instead, inspect the choice element and take the value after `#choice-`.

        ![how to callback image8](/images/how_to_callback_image8.png)

        The ID of that one is `36HzG42`.

    The callback carries more than this. You or your developer can copy the object into a JSON viewer to explore the rest.

=== "WooCommerce"

    ![how to callback image2](/images/how_to_callback_image2.png)

    !!! note "Some entries carry more than others"

        Logic, messages and preferences hold far more data than the rest.

    - **Logic**: the conditional logic rules you used on the quiz slides.
    - **Messages**: the text inside buttons, such as proceed to cart or see product.
    - **Name**: the name of the quiz.
    - **Preferences**: the settings of the quiz.
    - **Results**: the blocks on the results page.

        ![how to callback image3](/images/how_to_callback_image3.png)

        The data array holds one entry per block you added.

        ![how to callback image4](/images/how_to_callback_image4.png)

    - **Slides**: the questions themselves.

        ![how to callback image5](/images/how_to_callback_image5.png)

        `data` holds every slide, and each slide object carries everything about it.

        ![how to callback image6](/images/how_to_callback_image6.png)

        That is the ID of the slide, plus an `attributes` object holding the rest.

        ![how to callback image7](/images/how_to_callback_image7.png)

        Inside `slides > attributes`:

        - **Choices**: every choice a customer can pick.
        - **Description**: the text from [question settings](/reference/quiz-builder/questions/#question-settings), under `question settings → Show description`.
        - **Preferences**: how the customer selects the choices.
        - **Slide type**: the type of slide.
        - **Title**: the title you wrote for the slide.
        - **Validations**: further settings, such as whether the question is optional, and how many choices can be selected.
        - **Values**: which answers were selected, expressed as IDs.

    - **Theme**: the look and feel of the quiz.

        - **Background Image**: the image, if you added one, and its opacity.
        - **Colors**: the colors used through the quiz.
        - **Custom CSS**: your custom CSS, including custom fonts.
        - **Font**: the main font, or the fallback if the embedded font fails.
        - **Name**: the name of the theme.

        ![how to callback image9](/images/how_to_callback_image9.png)

    ??? question "How do I know which choice an ID represents?"

        No separate lookup is needed, because the labels are already in the callback object. Each slide carries its possible choices in `slide.attributes.choices.data[]`, each with an `id` and an `attributes.label`, and the selected answer IDs in `slide.attributes.values`. Match one against the other to read the label:

        ```javascript
        var choices = (slide.attributes.choices && slide.attributes.choices.data) || [];
        var labels = (slide.attributes.values || []).map(function (id) {
          var c = choices.filter(function (x) { return x.id === id; })[0];
          return c ? c.attributes.label : id; // raw value for text/number questions
        });
        ```

        To read an ID straight off the page instead, inspect the choice element and take the value after `#choice-`.

        ![how to callback image8](/images/how_to_callback_image8.png)

        The ID of that one is `36HzG42`.

    The callback carries more than this. You or your developer can copy the object into a JSON viewer to explore the rest.

=== "Magento"

    ![how to callback image2](/images/how_to_callback_image2.png)

    !!! note "Some entries carry more than others"

        Logic, messages and preferences hold far more data than the rest.

    - **Logic**: the conditional logic rules you used on the quiz slides.
    - **Messages**: the text inside buttons, such as proceed to cart or see product.
    - **Name**: the name of the quiz.
    - **Preferences**: the settings of the quiz.
    - **Results**: the blocks on the results page.

        ![how to callback image3](/images/how_to_callback_image3.png)

        The data array holds one entry per block you added.

        ![how to callback image4](/images/how_to_callback_image4.png)

    - **Slides**: the questions themselves.

        ![how to callback image5](/images/how_to_callback_image5.png)

        `data` holds every slide, and each slide object carries everything about it.

        ![how to callback image6](/images/how_to_callback_image6.png)

        That is the ID of the slide, plus an `attributes` object holding the rest.

        ![how to callback image7](/images/how_to_callback_image7.png)

        Inside `slides > attributes`:

        - **Choices**: every choice a customer can pick.
        - **Description**: the text from [question settings](/reference/quiz-builder/questions/#question-settings), under `question settings → Show description`.
        - **Preferences**: how the customer selects the choices.
        - **Slide type**: the type of slide.
        - **Title**: the title you wrote for the slide.
        - **Validations**: further settings, such as whether the question is optional, and how many choices can be selected.
        - **Values**: which answers were selected, expressed as IDs.

    - **Theme**: the look and feel of the quiz.

        - **Background Image**: the image, if you added one, and its opacity.
        - **Colors**: the colors used through the quiz.
        - **Custom CSS**: your custom CSS, including custom fonts.
        - **Font**: the main font, or the fallback if the embedded font fails.
        - **Name**: the name of the theme.

        ![how to callback image9](/images/how_to_callback_image9.png)

    ??? question "How do I know which choice an ID represents?"

        No separate lookup is needed, because the labels are already in the callback object. Each slide carries its possible choices in `slide.attributes.choices.data[]`, each with an `id` and an `attributes.label`, and the selected answer IDs in `slide.attributes.values`. Match one against the other to read the label:

        ```javascript
        var choices = (slide.attributes.choices && slide.attributes.choices.data) || [];
        var labels = (slide.attributes.values || []).map(function (id) {
          var c = choices.filter(function (x) { return x.id === id; })[0];
          return c ? c.attributes.label : id; // raw value for text/number questions
        });
        ```

        To read an ID straight off the page instead, inspect the choice element and take the value after `#choice-`.

        ![how to callback image8](/images/how_to_callback_image8.png)

        The ID of that one is `36HzG42`.

    The callback carries more than this. You or your developer can copy the object into a JSON viewer to explore the rest.

=== "BigCommerce"

    ![how to callback image2](/images/how_to_callback_image2.png)

    !!! note "Some entries carry more than others"

        Logic, messages and preferences hold far more data than the rest.

    - **Logic**: the conditional logic rules you used on the quiz slides.
    - **Messages**: the text inside buttons, such as proceed to cart or see product.
    - **Name**: the name of the quiz.
    - **Preferences**: the settings of the quiz.
    - **Results**: the blocks on the results page.

        ![how to callback image3](/images/how_to_callback_image3.png)

        The data array holds one entry per block you added.

        ![how to callback image4](/images/how_to_callback_image4.png)

    - **Slides**: the questions themselves.

        ![how to callback image5](/images/how_to_callback_image5.png)

        `data` holds every slide, and each slide object carries everything about it.

        ![how to callback image6](/images/how_to_callback_image6.png)

        That is the ID of the slide, plus an `attributes` object holding the rest.

        ![how to callback image7](/images/how_to_callback_image7.png)

        Inside `slides > attributes`:

        - **Choices**: every choice a customer can pick.
        - **Description**: the text from [question settings](/reference/quiz-builder/questions/#question-settings), under `question settings → Show description`.
        - **Preferences**: how the customer selects the choices.
        - **Slide type**: the type of slide.
        - **Title**: the title you wrote for the slide.
        - **Validations**: further settings, such as whether the question is optional, and how many choices can be selected.
        - **Values**: which answers were selected, expressed as IDs.

    - **Theme**: the look and feel of the quiz.

        - **Background Image**: the image, if you added one, and its opacity.
        - **Colors**: the colors used through the quiz.
        - **Custom CSS**: your custom CSS, including custom fonts.
        - **Font**: the main font, or the fallback if the embedded font fails.
        - **Name**: the name of the theme.

        ![how to callback image9](/images/how_to_callback_image9.png)

    ??? question "How do I know which choice an ID represents?"

        No separate lookup is needed, because the labels are already in the callback object. Each slide carries its possible choices in `slide.attributes.choices.data[]`, each with an `id` and an `attributes.label`, and the selected answer IDs in `slide.attributes.values`. Match one against the other to read the label:

        ```javascript
        var choices = (slide.attributes.choices && slide.attributes.choices.data) || [];
        var labels = (slide.attributes.values || []).map(function (id) {
          var c = choices.filter(function (x) { return x.id === id; })[0];
          return c ? c.attributes.label : id; // raw value for text/number questions
        });
        ```

        To read an ID straight off the page instead, inspect the choice element and take the value after `#choice-`.

        ![how to callback image8](/images/how_to_callback_image8.png)

        The ID of that one is `36HzG42`.

    The callback carries more than this. You or your developer can copy the object into a JSON viewer to explore the rest.

=== "Standalone"

    ![how to callback image2](/images/how_to_callback_image2.png)

    !!! note "Some entries carry more than others"

        Logic, messages and preferences hold far more data than the rest.

    - **Logic**: the conditional logic rules you used on the quiz slides.
    - **Messages**: the text inside buttons, such as proceed to cart or see product.
    - **Name**: the name of the quiz.
    - **Preferences**: the settings of the quiz.
    - **Results**: the blocks on the results page.

        ![how to callback image3](/images/how_to_callback_image3.png)

        The data array holds one entry per block you added.

        ![how to callback image4](/images/how_to_callback_image4.png)

    - **Slides**: the questions themselves.

        ![how to callback image5](/images/how_to_callback_image5.png)

        `data` holds every slide, and each slide object carries everything about it.

        ![how to callback image6](/images/how_to_callback_image6.png)

        That is the ID of the slide, plus an `attributes` object holding the rest.

        ![how to callback image7](/images/how_to_callback_image7.png)

        Inside `slides > attributes`:

        - **Choices**: every choice a customer can pick.
        - **Description**: the text from [question settings](/reference/quiz-builder/questions/#question-settings), under `question settings → Show description`.
        - **Preferences**: how the customer selects the choices.
        - **Slide type**: the type of slide.
        - **Title**: the title you wrote for the slide.
        - **Validations**: further settings, such as whether the question is optional, and how many choices can be selected.
        - **Values**: which answers were selected, expressed as IDs.

    - **Theme**: the look and feel of the quiz.

        - **Background Image**: the image, if you added one, and its opacity.
        - **Colors**: the colors used through the quiz.
        - **Custom CSS**: your custom CSS, including custom fonts.
        - **Font**: the main font, or the fallback if the embedded font fails.
        - **Name**: the name of the theme.

        ![how to callback image9](/images/how_to_callback_image9.png)

    ??? question "How do I know which choice an ID represents?"

        No separate lookup is needed, because the labels are already in the callback object. Each slide carries its possible choices in `slide.attributes.choices.data[]`, each with an `id` and an `attributes.label`, and the selected answer IDs in `slide.attributes.values`. Match one against the other to read the label:

        ```javascript
        var choices = (slide.attributes.choices && slide.attributes.choices.data) || [];
        var labels = (slide.attributes.values || []).map(function (id) {
          var c = choices.filter(function (x) { return x.id === id; })[0];
          return c ? c.attributes.label : id; // raw value for text/number questions
        });
        ```

        To read an ID straight off the page instead, inspect the choice element and take the value after `#choice-`.

        ![how to callback image8](/images/how_to_callback_image8.png)

        The ID of that one is `36HzG42`.

    The callback carries more than this. You or your developer can copy the object into a JSON viewer to explore the rest.

---

This article explains how to use the quiz callback functions, and what arrives in the response JSON.