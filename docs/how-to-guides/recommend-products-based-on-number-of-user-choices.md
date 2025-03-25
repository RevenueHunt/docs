
# How to Recommend Products Based on Number of User Choices

??? question "Do I need advanced technical skills to set this up?"

    While the process isn’t entirely plug-and-play, with the assistance of a developer, it’s manageable. If you’re not familiar with JavaScript or CSS, seeking developer help is advisable.

## How do I recommend products based on the number of user choices?

The recommendation process is based on how many choices the user selects out of the given set. Here’s a step-by-step guide:

1. **Create collections/categories**. Create distinct collections for each group of products you wish to recommend, e.g., “1/10 choices selected,” “2/10 choices selected,” etc.
2. **Add hidden choices**. In your final question, include a multiple-choice option that correlates with the aforementioned collections/categories. This ensures that each choice connects to its respective recommended collection/category. Make sure to hide these choices from the user with custom CSS code.
3. **Add custom JavaScript**. Using custom JavaScript, evaluate the choices selected throughout the quiz and write a piece of code that automatically selects one of the hidden choices in the last question. This will determine which product collection/category to recommend based on the number of choices the user made.

## How can I ensure that users don’t see the choices in the last question?

You can hide these technical choices in the last question using custom CSS code. A guide on how to customize the quiz design can be found [here](https://docs.revenuehunt.com/how-to-guides/customize-quiz-design/).

## Where do I input the custom JavaScript code?

[This article](https://docs.revenuehunt.com/how-to-guides/add-javascript/) explains how to add custom JavaScript code to quiz questions. For example:

![recommend-products-based-on-number-of-user-choices image1](/images/recommend-products-based-on-number-of-user-choices_image1.png)

The custom JavaScript code should be integrated into the final question to assess the user’s choices and click the right choices in order to recommend a product collection accordingly.

## How can I identify the selected choices from each slide or question with JavaScript?

To review the values or choice IDs selected for each slide/question, you can use the JavaScript console and search for the values:

![recommend-products-based-on-number-of-user-choices image2](/images/recommend-products-based-on-number-of-user-choices_image2.png)

---
This guide provides information on how to set up a custom solution that will recommend products based on the number of user choices.
