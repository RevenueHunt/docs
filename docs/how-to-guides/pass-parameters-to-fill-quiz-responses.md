---
icon: material/slash-forward-box
description: "Learn how to enable pre-fill on retake for RevenueHunt quiz responses to streamline customer experience."
---

# How to Pass Parameters to Pre-fill Quiz Responses

=== "Shopify"

    In the new Built for Shopify version of the RevenueHunt app, pre-filling quiz responses via JavaScript variables or URL parameters is not available. However, there is a built-in [**pre-fill on retake** setting](/reference/quiz-builder/quiz-settings/#general).

    When this is on, a customer who retakes the quiz gets all their previous answers back: choices, text fields, dates. They only need to change what is different.

    To enable it, go to **Quiz settings → Behavior → Pre-fill answers on retake** and toggle it on.

    !!! note

        This setting is off by default for existing quizzes and on by default for newly created quizzes.

=== "Shopify (Legacy)"

    With the RevenueHunt app you can pre-fill the responses to certain questions in your quiz.

    - This is useful when customers are logged in to your store. You do not want to ask again for information you already have, such as their name and email.
    - It also helps when you drive traffic to your quiz from a mailing list. You do not want to ask for contact details again.

    This feature can be implemented in two ways:

    - Declare JavaScript variables in your store source code. This needs a developer.
    - Pass URL parameters on a link to your store.

=== "WooCommerce"

    With the RevenueHunt app you can pre-fill the responses to certain questions in your quiz.

    - This is useful when customers are logged in to your store. You do not want to ask again for information you already have, such as their name and email.
    - It also helps when you drive traffic to your quiz from a mailing list. You do not want to ask for contact details again.

    This feature can be implemented in two ways:

    - Declare JavaScript variables in your store source code. This needs a developer.
    - Pass URL parameters on a link to your store.

=== "Magento"

    With the RevenueHunt app you can pre-fill the responses to certain questions in your quiz.

    - This is useful when customers are logged in to your store. You do not want to ask again for information you already have, such as their name and email.
    - It also helps when you drive traffic to your quiz from a mailing list. You do not want to ask for contact details again.

    This feature can be implemented in two ways:

    - Declare JavaScript variables in your store source code. This needs a developer.
    - Pass URL parameters on a link to your store.

=== "BigCommerce"

    With the RevenueHunt app you can pre-fill the responses to certain questions in your quiz.

    - This is useful when customers are logged in to your store. You do not want to ask again for information you already have, such as their name and email.
    - It also helps when you drive traffic to your quiz from a mailing list. You do not want to ask for contact details again.

    This feature can be implemented in two ways:

    - Declare JavaScript variables in your store source code. This needs a developer.
    - Pass URL parameters on a link to your store.

=== "Standalone"

    With the RevenueHunt app you can pre-fill the responses to certain questions in your quiz.

    - This is useful when customers are logged in to your store. You do not want to ask again for information you already have, such as their name and email.
    - It also helps when you drive traffic to your quiz from a mailing list. You do not want to ask for contact details again.

    This feature can be implemented in two ways:

    - Declare JavaScript variables in your store source code. This needs a developer.
    - Pass URL parameters on a link to your store.

## Option 1: declare window.prq_vars

=== "Shopify"

    Pre-filling quiz responses via `window.prq_vars` is not available in the new Built for Shopify version of the RevenueHunt app. Use the built-in **Pre-fill answers on retake** setting in [**Quiz settings → Behavior**](/reference/quiz-builder/quiz-settings/#general) instead.

=== "Shopify (Legacy)"

    You can declare `window.prq_vars` inside a JavaScript `<script>` tag in your store’s source code:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    // question ID - choices IDs separated by ;
    </script>
    ```

    ### Example

    **Use case**: You have embedded the quiz on all product pages, and want to know which product page the quiz was taken from.

    **Solution**: Pass a parameter such as the product ID to the quiz, and store it in a question as a pre-filled answer.

    1. Create a `Short Text` question to hold the product ID. See [Question Types](/reference/quiz-builder/questions/#question-types).
    2. Copy the question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Add this script to your product page:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    The question is skipped when a parameter is passed. If you also use the quiz outside your product page, pass an empty parameter for that `questionID`, or the question appears in the quiz.

    The `productID` parameter then tells you where the quiz was taken.

=== "WooCommerce"

    You can declare `window.prq_vars` inside a JavaScript `<script>` tag in your store’s source code:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    // question ID - choices IDs separated by ;
    </script>
    ```

    ### Example

    **Use case**: You have embedded the quiz on all product pages, and want to know which product page the quiz was taken from.

    **Solution**: Pass a parameter such as the product ID to the quiz, and store it in a question as a pre-filled answer.

    1. Create a `Short Text` question to hold the product ID. See [Question Types](/reference/quiz-builder/questions/#question-types).
    2. Copy the question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Add this script to your product page:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    The question is skipped when a parameter is passed. If you also use the quiz outside your product page, pass an empty parameter for that `questionID`, or the question appears in the quiz.

    The `productID` parameter then tells you where the quiz was taken.

=== "Magento"

    You can declare `window.prq_vars` inside a JavaScript `<script>` tag in your store’s source code:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    // question ID - choices IDs separated by ;
    </script>
    ```

    ### Example

    **Use case**: You have embedded the quiz on all product pages, and want to know which product page the quiz was taken from.

    **Solution**: Pass a parameter such as the product ID to the quiz, and store it in a question as a pre-filled answer.

    1. Create a `Short Text` question to hold the product ID. See [Question Types](/reference/quiz-builder/questions/#question-types).
    2. Copy the question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Add this script to your product page:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    The question is skipped when a parameter is passed. If you also use the quiz outside your product page, pass an empty parameter for that `questionID`, or the question appears in the quiz.

    The `productID` parameter then tells you where the quiz was taken.

=== "BigCommerce"

    You can declare `window.prq_vars` inside a JavaScript `<script>` tag in your store’s source code:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    // question ID - choices IDs separated by ;
    </script>
    ```

    ### Example

    **Use case**: You have embedded the quiz on all product pages, and want to know which product page the quiz was taken from.

    **Solution**: Pass a parameter such as the product ID to the quiz, and store it in a question as a pre-filled answer.

    1. Create a `Short Text` question to hold the product ID. See [Question Types](/reference/quiz-builder/questions/#question-types).
    2. Copy the question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Add this script to your product page:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    The question is skipped when a parameter is passed. If you also use the quiz outside your product page, pass an empty parameter for that `questionID`, or the question appears in the quiz.

    The `productID` parameter then tells you where the quiz was taken.

=== "Standalone"

    You can declare `window.prq_vars` inside a JavaScript `<script>` tag in your store’s source code:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    // question ID - choices IDs separated by ;
    </script>
    ```

    ### Example

    **Use case**: You have embedded the quiz on all product pages, and want to know which product page the quiz was taken from.

    **Solution**: Pass a parameter such as the product ID to the quiz, and store it in a question as a pre-filled answer.

    1. Create a `Short Text` question to hold the product ID. See [Question Types](/reference/quiz-builder/questions/#question-types).
    2. Copy the question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Add this script to your product page:

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    The question is skipped when a parameter is passed. If you also use the quiz outside your product page, pass an empty parameter for that `questionID`, or the question appears in the quiz.

    The `productID` parameter then tells you where the quiz was taken.

## Option 2: pass URL parameters

=== "Shopify"

    Pre-filling quiz responses via URL parameters is not available in the new Built for Shopify version of the RevenueHunt app. Use the built-in **Pre-fill answers on retake** setting in [**Quiz settings → Behavior**](/reference/quiz-builder/quiz-settings/#general) instead.

=== "Shopify (Legacy)"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    To pre-fill quiz responses, pass these URL parameters when you link to your store, for example from a newsletter:

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    If a value in `window.prq_vars` differs from the one passed in the URL, the URL parameter wins.

    ### Example

    This link to the demo store passes **no parameters**. You have to fill in every question, including the name and email. Click the link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)

    This link passes URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    Take the quiz now, and the name and email questions are pre-filled and skipped.

=== "WooCommerce"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    To pre-fill quiz responses, pass these URL parameters when you link to your store, for example from a newsletter:

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    If a value in `window.prq_vars` differs from the one passed in the URL, the URL parameter wins.

    ### Example

    This link to the demo store passes **no parameters**. You have to fill in every question, including the name and email. Click the link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)

    This link passes URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    Take the quiz now, and the name and email questions are pre-filled and skipped.

=== "Magento"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    To pre-fill quiz responses, pass these URL parameters when you link to your store, for example from a newsletter:

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    If a value in `window.prq_vars` differs from the one passed in the URL, the URL parameter wins.

    ### Example

    This link to the demo store passes **no parameters**. You have to fill in every question, including the name and email. Click the link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)

    This link passes URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    Take the quiz now, and the name and email questions are pre-filled and skipped.

=== "BigCommerce"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    To pre-fill quiz responses, pass these URL parameters when you link to your store, for example from a newsletter:

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    If a value in `window.prq_vars` differs from the one passed in the URL, the URL parameter wins.

    ### Example

    This link to the demo store passes **no parameters**. You have to fill in every question, including the name and email. Click the link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)

    This link passes URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    Take the quiz now, and the name and email questions are pre-filled and skipped.

=== "Standalone"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    To pre-fill quiz responses, pass these URL parameters when you link to your store, for example from a newsletter:

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    If a value in `window.prq_vars` differs from the one passed in the URL, the URL parameter wins.

    ### Example

    This link to the demo store passes **no parameters**. You have to fill in every question, including the name and email. Click the link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)

    This link passes URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    Take the quiz now, and the name and email questions are pre-filled and skipped.

---
This article explains how to pass parameters to pre-fill quiz responses in the RevenueHunt quiz app.