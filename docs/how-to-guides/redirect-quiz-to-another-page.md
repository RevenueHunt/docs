---
icon: material/directions
---

# How to Redirect Quiz to Another Page

In this guide, we'll explore several methods to redirect your customers to another page following the completion of a quiz. Below, you'll find detailed steps for implementing page redirection using various techniques within a quiz environment.

## Using Jump Logic for Conditional Redirection

[Jump Logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) offers a dynamic way to direct customers to specific URLs based on their quiz interactions. Here’s how to implement it:

1. **Navigate to the Jump Logic Section**: In the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/), locate the [Jump Logic](https://docs.revenuehunt.com/reference/quiz-builder/#jump-logic) settings.
2. **Configure URL Redirection**: Specify the URL to which customers should be redirected to. This can be set to occur after a specific question or based on selected answers.
    	![how to redirect quiz ot another page jump logic](/images/how to redirect quiz ot another page jump logic.png)
3. **Publish & Test Your Setup**: Click the top-right `Publish` button to update the preview/live quiz. Then, `Preview` the quiz to ensure the redirection wors correctly. 

Even if you redirect the customer with Jump Logic to another page the quiz responses will be saved in the Quiz Builder's [`Metrics`](https://docs.revenuehunt.com/reference/quiz-builder/#responses) section.

*Note: Redirecting with Jump Logic does not transfer quiz data to this new redirection page. If you want to send quiz data to another URL use the [callback function](#redirecting-to-a-custom-results-page-via-callback-function).*

## Redirecting to a Custom Results Page via Callback Function

You can use our [callback function](https://docs.revenuehunt.com/how-to-guides/use-callback-function/) to redirect the customers to another (custom-built) Results Page. This allows for greater flexibility in handling quiz data and customizing the quiz resutls look.

*Note: To do this, you'll need basic knowledge of JavaScript and handling JSON data.*

1. **Set Up the Callback Function**: Implement the [callback function](https://docs.revenuehunt.com/how-to-guides/use-callback-function/) on your website to capture quiz results in JSON format.
2. **Store and Redirect**: Configure the function to store the results locally (e.g., in the browser's local storage or cookies) before redirecting the user to your custom Results Page.
3. **Access the Results Page First**: The callback function is designed to trigger upon reaching the quiz's results page. Make sure that the results page is loaded even for a fraction of a second for the data to trasfer correctly. This sequence ensures that the callback captures the quiz response, saving it as JSON in your website's local storage/cookies, before any redirection occurs. 
4. **Use the Data**: On your custom page, use the `console.log(quizResponse)` function to retrieve and use the quiz data as needed.

For a more detailed guide on setting up the callback function, refer to [this resource](https://docs.revenuehunt.com/how-to-guides/use-callback-function/).

## Add a Redirection Button to the Results Page

Offering a direct link to another page from your [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) can be achieved simply with an **HTML button**.

1. **Add an HTML Block**: In the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) editor, click the `+` button to insert an `HTML block`.
2. **Insert the Button Code**: Use the following HTML snippet to add a button:

      ```html
      <a class="button" href="https://revenuehunt.com/">Visit RevenueHunt.com</a>
      ```
   Edit the link URL and text to your liking.

3. **Customize Appearance**: Style the button with CSS. You can add custom styles in the [Quiz Design](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-design) tab, targeting the button with `.lq-results a.button`.


*Note: Redirecting with HTML link does not transfer quiz data to this new redirection page. If you want to send quiz data to another URL use the [callback function](#redirecting-to-a-custom-results-page-via-callback-function).*

--- 
By following these steps, you can effectively guide customers to relevant pages mid or post-quiz.