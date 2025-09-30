---
icon: material/slash-forward-box
---

# How to Pass Parameters to Pre-fill Quiz Responses

=== "Shopify (Legacy)"

    With RevenueHunt app you have the possibility to pre-fill the responses to certain questions in your quiz. 

    - This comes in very handy when users are logged in to your store and don’t want to ask them for the information you already have about them (eg. their name and email).
    - Another use case is when you’re driving traffic to your quiz from a mailing list and, again, you don’t want to ask them for their contact details.

    This feature can be implemented in two ways:

    - either declaring JavaScript variables in your store’s source code (note: developer needed)
    - passing URL parameters on a link to your store.

=== "Shopify"

    It is **not possible yet** to pre-fill quiz responses in the new Built for Shopify version of the RevenueHunt app.


=== "WooCommerce"

    With RevenueHunt app you have the possibility to pre-fill the responses to certain questions in your quiz. 

    - This comes in very handy when users are logged in to your store and don’t want to ask them for the information you already have about them (eg. their name and email).
    - Another use case is when you’re driving traffic to your quiz from a mailing list and, again, you don’t want to ask them for their contact details.

    This feature can be implemented in two ways:

    - either declaring JavaScript variables in your store’s source code (note: developer needed)
    - passing URL parameters on a link to your store.


=== "Magento"

    With RevenueHunt app you have the possibility to pre-fill the responses to certain questions in your quiz. 

    - This comes in very handy when users are logged in to your store and don’t want to ask them for the information you already have about them (eg. their name and email).
    - Another use case is when you’re driving traffic to your quiz from a mailing list and, again, you don’t want to ask them for their contact details.

    This feature can be implemented in two ways:

    - either declaring JavaScript variables in your store’s source code (note: developer needed)
    - passing URL parameters on a link to your store.


=== "BigCommerce"

    With RevenueHunt app you have the possibility to pre-fill the responses to certain questions in your quiz. 

    - This comes in very handy when users are logged in to your store and don’t want to ask them for the information you already have about them (eg. their name and email).
    - Another use case is when you’re driving traffic to your quiz from a mailing list and, again, you don’t want to ask them for their contact details.

    This feature can be implemented in two ways:

    - either declaring JavaScript variables in your store’s source code (note: developer needed)
    - passing URL parameters on a link to your store.

=== "Standalone"

    With RevenueHunt app you have the possibility to pre-fill the responses to certain questions in your quiz. 

    - This comes in very handy when users are logged in to your store and don’t want to ask them for the information you already have about them (eg. their name and email).
    - Another use case is when you’re driving traffic to your quiz from a mailing list and, again, you don’t want to ask them for their contact details.

    This feature can be implemented in two ways:

    - either declaring JavaScript variables in your store’s source code (note: developer needed)
    - passing URL parameters on a link to your store.

## Option 1: Declare window.prq_vars

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

    **Use case**: You’ve embedded the quiz on all product pages and want to know from which product page the quiz was taken.

    **Solution**: You can pass parameters to the quiz (eg. product ID) and “store” them in a question as a pre-filled answer.

    
    1. You will first need to create a `Short Text` question to store the product ID. Check how to add this question [here](/reference/quiz-builder/questions/#question-types).
    2. Copy that question ID from [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Then in your main product page include the following script, so you can add some script like this to your product page:

    ```html
    <script>
    window.prq_vars = {}; 
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    That question will be automatically skipped if parameters have been passed, but note that if you use the quiz outside your product page you will need to also pass some “empty” parameter to that questionID otherwise it will be shown in the quiz.
    
    This way you will pass the productID as a parameter to differentiate where the quiz was taken from.

=== "Shopify"

    It is **not possible yet** to pre-fill quiz responses in the new Built for Shopify version of the RevenueHunt app.

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

    **Use case**: You’ve embedded the quiz on all product pages and want to know from which product page the quiz was taken.

    **Solution**: You can pass parameters to the quiz (eg. product ID) and “store” them in a question as a pre-filled answer.

    
    1. You will first need to create a `Short Text` question to store the product ID. Check how to add this question [here](/reference/quiz-builder/questions/#question-types).
    2. Copy that question ID from [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Then in your main product page include the following script, so you can add some script like this to your product page:

    ```html
    <script>
    window.prq_vars = {}; 
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    That question will be automatically skipped if parameters have been passed, but note that if you use the quiz outside your product page you will need to also pass some “empty” parameter to that questionID otherwise it will be shown in the quiz.
    
    This way you will pass the productID as a parameter to differentiate where the quiz was taken from.

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

    **Use case**: You’ve embedded the quiz on all product pages and want to know from which product page the quiz was taken.

    **Solution**: You can pass parameters to the quiz (eg. product ID) and “store” them in a question as a pre-filled answer.

    
    1. You will first need to create a `Short Text` question to store the product ID. Check how to add this question [here](/reference/quiz-builder/questions/#question-types).
    2. Copy that question ID from [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Then in your main product page include the following script, so you can add some script like this to your product page:

    ```html
    <script>
    window.prq_vars = {}; 
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    That question will be automatically skipped if parameters have been passed, but note that if you use the quiz outside your product page you will need to also pass some “empty” parameter to that questionID otherwise it will be shown in the quiz.
    
    This way you will pass the productID as a parameter to differentiate where the quiz was taken from.

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

    **Use case**: You’ve embedded the quiz on all product pages and want to know from which product page the quiz was taken.

    **Solution**: You can pass parameters to the quiz (eg. product ID) and “store” them in a question as a pre-filled answer.

    
    1. You will first need to create a `Short Text` question to store the product ID. Check how to add this question [here](/reference/quiz-builder/questions/#question-types).
    2. Copy that question ID from [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Then in your main product page include the following script, so you can add some script like this to your product page:

    ```html
    <script>
    window.prq_vars = {}; 
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    That question will be automatically skipped if parameters have been passed, but note that if you use the quiz outside your product page you will need to also pass some “empty” parameter to that questionID otherwise it will be shown in the quiz.
    
    This way you will pass the productID as a parameter to differentiate where the quiz was taken from.

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

    **Use case**: You’ve embedded the quiz on all product pages and want to know from which product page the quiz was taken.

    **Solution**: You can pass parameters to the quiz (eg. product ID) and “store” them in a question as a pre-filled answer.

    
    1. You will first need to create a `Short Text` question to store the product ID. Check how to add this question [here](/reference/quiz-builder/questions/#question-types).
    2. Copy that question ID from [question settings](/reference/quiz-builder/questions/#question-settings).
    3. Then in your main product page include the following script, so you can add some script like this to your product page:

    ```html
    <script>
    window.prq_vars = {}; 
    window.prq_vars.questionID = 'productID';
    </script>
    ```

    That question will be automatically skipped if parameters have been passed, but note that if you use the quiz outside your product page you will need to also pass some “empty” parameter to that questionID otherwise it will be shown in the quiz.
    
    This way you will pass the productID as a parameter to differentiate where the quiz was taken from.

## Option 2: Pass URL parameters

=== "Shopify (Legacy)"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    In order to pre-fill certain quiz responses, you can pass the following URL parameters when linking to your store (eg. linking from a newsletter):

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    In case of differences in the values declared in the `window.prq_vars` and the values passed via URL parameters, the URL parameters will prevail.

    ### Example

    Here’s a link to our demo store **without passing parameters**. You’ll see that you have to fill in all the questions, including the name and email. Click on the following link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)


    On the other hand, in this other link we are passing URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    You’ll notice that if you take the quiz now, the “name” and “email” questions are pre-filled and skipped.

=== "Shopify"

    It is **not possible yet** to pre-fill quiz responses in the new Built for Shopify version of the RevenueHunt app.

=== "WooCommerce"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    In order to pre-fill certain quiz responses, you can pass the following URL parameters when linking to your store (eg. linking from a newsletter):

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    In case of differences in the values declared in the `window.prq_vars` and the values passed via URL parameters, the URL parameters will prevail.

    ### Example

    Here’s a link to our demo store **without passing parameters**. You’ll see that you have to fill in all the questions, including the name and email. Click on the following link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)


    On the other hand, in this other link we are passing URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    You’ll notice that if you take the quiz now, the “name” and “email” questions are pre-filled and skipped.


=== "Magento"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    In order to pre-fill certain quiz responses, you can pass the following URL parameters when linking to your store (eg. linking from a newsletter):

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    In case of differences in the values declared in the `window.prq_vars` and the values passed via URL parameters, the URL parameters will prevail.

    ### Example

    Here’s a link to our demo store **without passing parameters**. You’ll see that you have to fill in all the questions, including the name and email. Click on the following link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)


    On the other hand, in this other link we are passing URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    You’ll notice that if you take the quiz now, the “name” and “email” questions are pre-filled and skipped.

=== "BigCommerce"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    In order to pre-fill certain quiz responses, you can pass the following URL parameters when linking to your store (eg. linking from a newsletter):

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    In case of differences in the values declared in the `window.prq_vars` and the values passed via URL parameters, the URL parameters will prevail.

    ### Example

    Here’s a link to our demo store **without passing parameters**. You’ll see that you have to fill in all the questions, including the name and email. Click on the following link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)


    On the other hand, in this other link we are passing URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    You’ll notice that if you take the quiz now, the “name” and “email” questions are pre-filled and skipped.

=== "Standalone"

    URL parameters (also known as query strings) are a way to structure additional information for a given URL. Parameters are added to the end of a URL after a `?` symbol, and multiple parameters can be included when separated by the `&` symbol.

    In order to pre-fill certain quiz responses, you can pass the following URL parameters when linking to your store (eg. linking from a newsletter):

    ```html
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    // question ID - choices IDs separated by ;
    ```

    In case of differences in the values declared in the `window.prq_vars` and the values passed via URL parameters, the URL parameters will prevail.

    ### Example

    Here’s a link to our demo store **without passing parameters**. You’ll see that you have to fill in all the questions, including the name and email. Click on the following link and take the quiz:

    [https://skincarequiz.myshopify.com/pages/inline-quiz/](https://skincarequiz.myshopify.com/pages/inline-quiz/)


    On the other hand, in this other link we are passing URL parameters:
    [https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com](https://skincarequiz.myshopify.com/pages/inline-quiz/?prq_name=John%20Doe&prq_email=john.doe@gmail.com)

    You’ll notice that if you take the quiz now, the “name” and “email” questions are pre-filled and skipped.

---
This article explains how to pass parameters to pre-fill quiz responses in the RevenueHunt quiz app.