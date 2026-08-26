---
icon: material/directions
description: "Learn how to redirect a customer to another page after they finish a RevenueHunt quiz."
---

# How to Redirect Quiz to Another Page

This article explains three ways to send a customer to another page after they finish a quiz.

## Using jump logic for conditional redirection

[Jump Logic](/how-to-guides/use-jump-logic/) sends a customer to a specific URL, based on the answers they gave. To set it up:

=== "Shopify"

      <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/qk1WJJstTjU?si=L7r3OHN9V9Zq6yWF" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the Conditional logic tab**: In the [Quiz builder](/reference/quiz-builder/), open [Conditional logic](/reference/quiz-builder/conditional-logic/). Select the last question, or whichever question should trigger the redirect. In the menu that opens, go to the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab.
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_defaultdestination.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection works correctly.

    Even if you redirect the customer with Jump logic to another page the quiz responses will be saved in the Quiz builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.


=== "Shopify (Legacy)"

    1. **Open the Conditional Logic tab**: In the [Quiz Builder](/reference/quiz-builder/), open [Conditional Logic](/reference/quiz-builder/conditional-logic/). Select the last question, or whichever question should trigger the redirect. In the menu that opens, go to the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab.
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection works correctly.

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "WooCommerce"

    1. **Open the Conditional Logic tab**: In the [Quiz Builder](/reference/quiz-builder/), open [Conditional Logic](/reference/quiz-builder/conditional-logic/). Select the last question, or whichever question should trigger the redirect. In the menu that opens, go to the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab.
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection works correctly.

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "Magento"

    1. **Open the Conditional Logic tab**: In the [Quiz Builder](/reference/quiz-builder/), open [Conditional Logic](/reference/quiz-builder/conditional-logic/). Select the last question, or whichever question should trigger the redirect. In the menu that opens, go to the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab.
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection works correctly.

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "BigCommerce"

    1. **Open the Conditional Logic tab**: In the [Quiz Builder](/reference/quiz-builder/), open [Conditional Logic](/reference/quiz-builder/conditional-logic/). Select the last question, or whichever question should trigger the redirect. In the menu that opens, go to the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab.
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection works correctly.

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

=== "Standalone"

    1. **Open the Conditional Logic tab**: In the [Quiz Builder](/reference/quiz-builder/), open [Conditional Logic](/reference/quiz-builder/conditional-logic/). Select the last question, or whichever question should trigger the redirect. In the menu that opens, go to the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) tab.
    2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)
    3. **Publish & Test Your Setup**: Click the top-right `Publish/Save` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection works correctly.

    Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](/reference/quiz-builder/metrics/#responses) section.

!!! info

      Redirecting with Jump Logic does not transfer quiz data to this new redirection page. If you want to send quiz data to another URL use the [callback function](#redirecting-to-a-custom-results-page-via-callback-function).

## Redirecting to a custom results page via callback function

You can use the [callback function](/how-to-guides/use-callback-function/) to redirect the customers to another (custom-built) Results Page. This allows for greater flexibility in handling quiz data and customizing the quiz results look.

=== "Shopify"

    !!! warning

        The callback function is not supported in the `💎Built for Shopify` version of the RevenueHunt app.

    The results page can do this work instead. It can show sections conditionally, based on quiz answers or custom scores, take custom JavaScript, and hold fixed products. It also has layout and alignment options, so you can build a custom results page without redirecting the customer.


=== "Shopify (Legacy)"

    !!! warning

        To do this, you need basic knowledge of JavaScript and JSON.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Store the results locally, in the browser local storage or cookies. Then redirect the customer to your custom Results Page.
    3. **Access the Results Page First**: The callback fires when the results page is reached. The page has to load, even for a fraction of a second, for the data to transfer. The callback then saves the quiz response as JSON in local storage or cookies, before any redirect.
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "WooCommerce"

    !!! warning

        To do this, you need basic knowledge of JavaScript and JSON.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Store the results locally, in the browser local storage or cookies. Then redirect the customer to your custom Results Page.
    3. **Access the Results Page First**: The callback fires when the results page is reached. The page has to load, even for a fraction of a second, for the data to transfer. The callback then saves the quiz response as JSON in local storage or cookies, before any redirect.
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "Magento"

    !!! warning

        To do this, you need basic knowledge of JavaScript and JSON.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Store the results locally, in the browser local storage or cookies. Then redirect the customer to your custom Results Page.
    3. **Access the Results Page First**: The callback fires when the results page is reached. The page has to load, even for a fraction of a second, for the data to transfer. The callback then saves the quiz response as JSON in local storage or cookies, before any redirect.
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "BigCommerce"

    !!! warning

        To do this, you need basic knowledge of JavaScript and JSON.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Store the results locally, in the browser local storage or cookies. Then redirect the customer to your custom Results Page.
    3. **Access the Results Page First**: The callback fires when the results page is reached. The page has to load, even for a fraction of a second, for the data to transfer. The callback then saves the quiz response as JSON in local storage or cookies, before any redirect.
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

=== "Standalone"

    !!! warning

        To do this, you need basic knowledge of JavaScript and JSON.

    1. **Set Up the Callback Function**: Implement the [callback function](/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
    2. **Store and Redirect**: Store the results locally, in the browser local storage or cookies. Then redirect the customer to your custom Results Page.
    3. **Access the Results Page First**: The callback fires when the results page is reached. The page has to load, even for a fraction of a second, for the data to transfer. The callback then saves the quiz response as JSON in local storage or cookies, before any redirect.
    4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

    For a more detailed guide on setting up the callback function, refer to [this resource](/how-to-guides/use-callback-function/).

## Add a redirection button to the results page

=== "Shopify"

      Offering a direct link to another page from your [Results page](/reference/quiz-builder/results-page/) can be achieved simply with an **Button**.

      1. **Add a Button**: In the [Results page](/reference/quiz-builder/results-page/) editor, click the `+ Add block` button to insert a `Button` block.
      2. **Insert the Button URL**: In the Button URL field, enter the address you want to send the customer to:

           ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_button](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_button.png)


=== "Shopify (Legacy)"

      Offering a direct link to another page from your [Results Page](/reference/quiz-builder/results-page/) can be achieved simply with an **HTML button**.

      1. **Add an HTML Block**: In the [Results Page](/reference/quiz-builder/results-page/) editor, click the `+` button to insert an `HTML block`.
      2. **Insert the Button Code**: Use the following HTML snippet to add a button:

            ```html
            <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
            ```
      Edit the link URL and text to your liking.

      3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, targeting the button with `.lq-results a.button`.

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