---
icon: material/lightbulb-question
---


# How to Show Results Explanation

While our [product recommendation algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won’t automatically display custom text depending on the recommended product.

For this reason, it can be very hard to build a **"personality-type"** quiz with our solution.

If you want to show different text results depending on the recommended products, this functionality has to be built on the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). There are a few ways to achieve it:

1. **Information Recalls**: Use [Information Recalls](https://docs.revenuehunt.com/how-to-guides/use-information-recalls/) to display a customer's answers within a content block on the Results Page. This method helps customers understand the rationale behind each product recommendation without any coding or complex logic.

2. **Block Logic**: [Block Logic](https://docs.revenuehunt.com/reference/quiz-builder/#block-logic) allows you to show or hide text on the Results Page based on the customer's quiz responses. This method is suitable for shorter, simpler quizzes. For detailed guidance on setting up Block Logic, see [here](https://docs.revenuehunt.com/how-to-guides/use-block-logic/). *Note: For longer, more complex quizzes, we advise using the custom JavaScript approach for optimal flexibility.*

3. **Custom JavaScript**: For a more refined approach, consider hiring a developer to create a custom JavaScript function. This function can show specific text tailored to the ID of the recommended product. Instructions on adding custom JavaScript to your Shop Quiz can be found [here](https://docs.revenuehunt.com/how-to-guides/add-javascript/).

4. **Product Descriptions**: Another option is to enrich your product descriptions with information explaining why each product is recommended. These descriptions are pulled directly from your store's product list. You can manage the visibility of these descriptions in the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings) under `Individual Product Settings -> Show description`. Additionally, you have the option to truncate these descriptions for better readability.