---
icon: material/directions
---

# How to Redirect Quiz to Another Page

In this guide, we'll explore several methods to redirect your customers to another page following the completion of a quiz. Below, you'll find detailed steps for implementing page redirection using various techniques within a quiz environment.

## Using Jump Logic for Conditional Redirection

[Jump Logic](/how-to-guides/use-jump-logic/) offers a dynamic way to direct customers to specific URLs based on their quiz interactions. Here's how to implement it:

=== "Shopify (Legacy)"

    1. **Navigate to the Conditional Logic Section**: In the [Quiz Builder](/reference/quiz-builder/), locate the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select the last question in the quiz (or another question if you want to redirect the customer after a specific question). In the menu that opens, go the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab. 
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "Shopify"

      <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/312b3b8099174391abe9f5f17b6918bb?sid=2f2dc229-23be-418c-9c7a-ab66922c30f8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Navigate to the Conditional Logic Section**: In the [Quiz Builder](/reference/quiz-builder/), locate the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select the last question in the quiz (or another question if you want to redirect the customer after a specific question). In the menu that opens, go the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab. 
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_defaultdestination.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "WooCommerce"

    1. **Navigate to the Conditional Logic Section**: In the [Quiz Builder](/reference/quiz-builder/), locate the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select the last question in the quiz (or another question if you want to redirect the customer after a specific question). In the menu that opens, go the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab. 
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "Magento"

    1. **Navigate to the Conditional Logic Section**: In the [Quiz Builder](/reference/quiz-builder/), locate the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select the last question in the quiz (or another question if you want to redirect the customer after a specific question). In the menu that opens, go the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab. 
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "BigCommerce"

    1. **Navigate to the Conditional Logic Section**: In the [Quiz Builder](/reference/quiz-builder/), locate the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select the last question in the quiz (or another question if you want to redirect the customer after a specific question). In the menu that opens, go the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab. 
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "Standalone"

    1. **Navigate to the Conditional Logic Section**: In the [Quiz Builder](/reference/quiz-builder/), locate the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select the last question in the quiz (or another question if you want to redirect the customer after a specific question). In the menu that opens, go the [`Jump Logic`](/reference/quiz-builder/
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

!!! info

      Redirecting with Jump Logic does not transfer quiz data to this new redirection page. If you want to send quiz data to another URL use the [callback function](#redirecting-to-a-custom-results-page-via-callback-function).

## Redirecting to a Custom Results Page via Callback Function

You can use our [callback function](/how-to-guides/use-callback-function/) to redirect the customers to another (custom-built) Results Page. This allows for greater flexibility in handling quiz data and customizing the quiz results look.

=== "Shopify (Legacy)"

    !!! warning

          To do this, you'll need basic knowledge of JavaScript and handling JSON data.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Configure the function to store the results locally (e.g., in the browser's local storage or cookies) before redirecting the user to your custom Results Page.
    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. Make sure that the results page is loaded even for a fraction of a second for the data to trasfer correctly. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage/cookies, before any redirection occurs. 
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "Shopify"

    !!! warning

          The callback function is not supported in Shopify V2.

      The callback function is not supported in Shopify V2. However, the new quiz version's results page includes powerful features such as conditionally displaying sections based on quiz answers or custom scores, adding custom JavaScript, and showcasing fixed products. It also offers advanced layout and alignment options, allowing you to create a unique and fully customized results page—without needing to redirect users to an external page.

=== "WooCommerce"

    !!! warning

          To do this, you'll need basic knowledge of JavaScript and handling JSON data.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Configure the function to store the results locally (e.g., in the browser's local storage or cookies) before redirecting the user to your custom Results Page.
    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. Make sure that the results page is loaded even for a fraction of a second for the data to trasfer correctly. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage/cookies, before any redirection occurs. 
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "Magento"

    !!! warning

          To do this, you'll need basic knowledge of JavaScript and handling JSON data.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Configure the function to store the results locally (e.g., in the browser's local storage or cookies) before redirecting the user to your custom Results Page.
    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. Make sure that the results page is loaded even for a fraction of a second for the data to trasfer correctly. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage/cookies, before any redirection occurs. 
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "BigCommerce"

    !!! warning

          To do this, you'll need basic knowledge of JavaScript and handling JSON data.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Configure the function to store the results locally (e.g., in the browser's local storage or cookies) before redirecting the user to your custom Results Page.
    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. Make sure that the results page is loaded even for a fraction of a second for the data to trasfer correctly. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage/cookies, before any redirection occurs. 
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "Standalone"

    !!! warning

          To do this, you'll need basic knowledge of JavaScript and handling JSON data.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Configure the function to store the results locally (e.g., in the browser's local storage or cookies) before redirecting the user to your custom Results Page.
    3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. Make sure that the results page is loaded even for a fraction of a second for the data to trasfer correctly. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage/cookies, before any redirection occurs. 
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

## Add a Redirection Button to the Results Page

=== "Shopify (Legacy)"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **HTML button**.

      1. **Add an HTML Block**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+` button to insert an `HTML block`.
      2. **Insert the Button Code**: Use the following HTML snippet to add a button:

            ```html
            <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
            ```
      Edit the link URL and text to your liking.

      3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, targeting the button with `.lq-results a.button`.

=== "Shopify"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **Button**.

      1. **Add a Button**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+ Add block` button to insert a `Button` block.
      2. **Insert the Button URL**: Use the Button URL field to add a custom link URL you want the user to be redirected to:
           
           ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_button](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_button.png)

=== "WooCommerce"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **HTML button**.

      1. **Add an HTML Block**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+` button to insert an `HTML block`.
      2. **Insert the Button Code**: Use the following HTML snippet to add a button:

            ```html
            <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
            ```
      Edit the link URL and text to your liking.

      3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, targeting the button with `.lq-results a.button`.

=== "Magento"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **HTML button**.

      1. **Add an HTML Block**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+` button to insert an `HTML block`.
      2. **Insert the Button Code**: Use the following HTML snippet to add a button:

            ```html
            <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
            ```
      Edit the link URL and text to your liking.

      3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, targeting the button with `.lq-results a.button`.

=== "BigCommerce"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **HTML button**.

      1. **Add an HTML Block**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+` button to insert an `HTML block`.
      2. **Insert the Button Code**: Use the following HTML snippet to add a button:

            ```html
            <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
            ```
      Edit the link URL and text to your liking.

      3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, targeting the button with `.lq-results a.button`.

=== "Standalone"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **HTML button**.

      1. **Add an HTML Block**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+` button to insert an `HTML block`.
      2. **Insert the Button Code**: Use the following HTML snippet to add a button:

            ```html
            <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
            ```
      Edit the link URL and text to your liking.

      3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, targeting the button with `.lq-results a.button`.

!!! info

      Redirecting with a Button/ HTML link does not transfer quiz data to this new redirection page. If you want to send quiz data to another URL use the [callback function](#redirecting-to-a-custom-results-page-via-callback-function).

--- 
By following these steps, you can effectively guide customers to relevant pages mid or post-quiz.