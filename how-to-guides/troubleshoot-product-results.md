---
icon: material/printer-pos-wrench
---

# How to Troubleshoot Product Recommendations in Your Quiz

Navigating through the product recommendations can be challenging, especially when dealing with numerous products and collections/categories linked to quiz choices. 

This guide will walk you through the process of troubleshooting product recommendations. It can help you understand why a certain product was recommended or missing from the Results Page.

!!! warning "Understanding the basics"

    When a particular product appears (or fails to appear) on the Results Page, it's crucial to understand the mechanism behind its selection. This involves tracing back to the quiz responses and analyzing the [voting system](/how-to-guides/set-up-funnel-quiz/#voting-system) or [display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) that influences product visibility.

## Step-by-Step Process to Check Recommendations

!!! tip

    Before you begin, open the [Responses section](/reference/quiz-builder/metrics/#responses) from the [App manual](/reference/) in the new browser window. It will come in handy.


=== "Shopify" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/5RFclBk7-LA?si=YwBMN6n0c87QrZRZ" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Explore Responses**: To open the responses sections, go back to the [dashboard](/reference/quiz-builder/). Pick a quiz and click the `...` to open the quiz menu. From the list pick and click on [`Responses`](/reference/quiz-builder/metrics/#responses).
    
        ![manual_shopifyV2_quizbuilder_openresponses](/images/manual_shopifyV2_quizbuilder_openresponses.png)
    
        In the Responses section you will find a list of the latest quiz responses sorted by date. Click on a date to open a specific response.

        ![manual_shopifyV2_quizbuilder_responses](/images/manual_shopifyV2_quizbuilder_responses.png)

        !!! warning "Test responses removal"

            Admin responses and quiz previews are removed from the list after 24 hours to don't add to your plan's limits.

    2. Click `Analyze response` to open the [Quiz Copilot](/how-to-guides/use-quiz-copilot/) chat window. You can ask it anything about the response, it will provide a detailed analysis of the response, help you identify the root cause of the issue and suggest improvements.

    3. Check the `Why was a product recommended or not in this response?` section. This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.

        ![manual_shopifyV2_quizbuilder_responses_sample1](/images/manual_shopifyV2_quizbuilder_responses_sample1.png)
    4. On the results page, identify a product of interest—either one that appeared unexpectedly on the Results Page or one you anticipated but was missing.
    5. **Conduct a Product Search**: Use the `SELECT PRODUCT TO CHECK` section to search the name of the product in question. Select the product from the search results to further investigate its recommendation status.

        **Understanding Product Status Colors**

        - **Green**: Indicates products that received votes through the quiz choices.
        - **Red**: Denotes products that were explicitly excluded from recommendations.
        - **White**: Represents products that did not receive any votes, hence their absence from the recommendations.

    6. **Analyze Product Details**: Upon selecting a product, a detailed panel will reveal critical information.

        ![how to troubleshoot quiz results search products](/images/manual_shopifyV2_quizbuilder_responses_sample1_checkproduct.png)

        Information such as:

        - The collections/categories the product belongs to.
        - The number of votes it received and the reasons for its recommendation or absence.
        - The questions/choices that influenced its votes, including the collections/categories where it was either upvoted or excluded.
        - The specific Results Page and Slots or Product blocks that facilitated its recommendation.

    7. **Troubleshooting and Adjustments**: With this information, you can pinpoint inconsistencies or errors in product categorization, inclusion, or exclusion. 

    !!! tip

        A common issue is a product being **misclassified** into an incorrect collection/category or **accidentally excluded** in quiz settings. Paying close attention to these details can significantly improve the accuracy of your product recommendations.


=== "Shopify (Legacy)" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    1. **Access Quiz Metrics**: First, navigate to the quiz [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.
    2. **Explore Responses**: Within Metrics, locate and open the [Responses](/reference/quiz-builder/metrics/#responses) tab. On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.
    3. Check the `Why was a product recommended or not in this response?` section. This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.
    4. **Preview the Results Page**: Use the provided link at the bottom of the response details to access the Results Page corresponding to the chosen response. 
        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)
    5. On the results page, identify a product of interest—either one that appeared unexpectedly on the Results Page or one you anticipated but was missing.
    6. **Conduct a Product Search**: Use the `SELECT PRODUCT TO CHECK` section at the top of the response to search the name of the product in question. Select the product from the search results to further investigate its recommendation status.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        **Understanding Product Status Colors**

        - **Green**: Indicates products that received votes through the quiz choices.
        - **Red**: Denotes products that were explicitly excluded from recommendations.
        - **White**: Represents products that did not receive any votes, hence their absence from the recommendations.

    7. **Analyze Product Details**: Upon selecting a product, a detailed panel will reveal critical information.

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        Information such as:

        - The collections/categories the product belongs to.
        - The number of votes it received and the reasons for its recommendation or absence.
        - The questions/choices that influenced its votes, including the collections/categories where it was either upvoted or excluded.
        - The specific Results Page and Slots or Product blocks that facilitated its recommendation.

    8. **Troubleshooting and Adjustments**: With this information, you can pinpoint inconsistencies or errors in product categorization, inclusion, or exclusion. 

    !!! tip

        A common issue is a product being **misclassified** into an incorrect collection/category or **accidentally excluded** in quiz settings. Paying close attention to these details can significantly improve the accuracy of your product recommendations.

    Additionally, you may:

    - **Recalculate Recommendations**: If adjustments to the quiz or product collections/categories have been made, use this option to see how these changes affect recommendations.
    - **Resend Notifications**: Useful for updating CRM services or sending revised recommendations via email.

=== "WooCommerce" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Quiz Metrics**: First, navigate to the quiz [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.
    2. **Explore Responses**: Within Metrics, locate and open the [Responses](/reference/quiz-builder/metrics/#responses) tab. On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.
    3. Check the `Why was a product recommended or not in this response?` section. This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.
    4. **Preview the Results Page**: Use the provided link at the bottom of the response details to access the Results Page corresponding to the chosen response. 
        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)
    5. On the results page, identify a product of interest—either one that appeared unexpectedly on the Results Page or one you anticipated but was missing.
    6. **Conduct a Product Search**: Use the `SELECT PRODUCT TO CHECK` section at the top of the response to search the name of the product in question. Select the product from the search results to further investigate its recommendation status.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        **Understanding Product Status Colors**

        - **Green**: Indicates products that received votes through the quiz choices.
        - **Red**: Denotes products that were explicitly excluded from recommendations.
        - **White**: Represents products that did not receive any votes, hence their absence from the recommendations.

    7. **Analyze Product Details**: Upon selecting a product, a detailed panel will reveal critical information.

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        Information such as:

        - The collections/categories the product belongs to.
        - The number of votes it received and the reasons for its recommendation or absence.
        - The questions/choices that influenced its votes, including the collections/categories where it was either upvoted or excluded.
        - The specific Results Page and Slots or Product blocks that facilitated its recommendation.

    8. **Troubleshooting and Adjustments**: With this information, you can pinpoint inconsistencies or errors in product categorization, inclusion, or exclusion. 

    !!! tip

        A common issue is a product being **misclassified** into an incorrect collection/category or **accidentally excluded** in quiz settings. Paying close attention to these details can significantly improve the accuracy of your product recommendations.

    Additionally, you may:

    - **Recalculate Recommendations**: If adjustments to the quiz or product collections/categories have been made, use this option to see how these changes affect recommendations.
    - **Resend Notifications**: Useful for updating CRM services or sending revised recommendations via email.

=== "Magento" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Quiz Metrics**: First, navigate to the quiz [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.
    2. **Explore Responses**: Within Metrics, locate and open the [Responses](/reference/quiz-builder/metrics/#responses) tab. On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.
    3. Check the `Why was a product recommended or not in this response?` section. This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.
    4. **Preview the Results Page**: Use the provided link at the bottom of the response details to access the Results Page corresponding to the chosen response. 
        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)
    5. On the results page, identify a product of interest—either one that appeared unexpectedly on the Results Page or one you anticipated but was missing.
    6. **Conduct a Product Search**: Use the `SELECT PRODUCT TO CHECK` section at the top of the response to search the name of the product in question. Select the product from the search results to further investigate its recommendation status.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        **Understanding Product Status Colors**

        - **Green**: Indicates products that received votes through the quiz choices.
        - **Red**: Denotes products that were explicitly excluded from recommendations.
        - **White**: Represents products that did not receive any votes, hence their absence from the recommendations.

    7. **Analyze Product Details**: Upon selecting a product, a detailed panel will reveal critical information.

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        Information such as:

        - The collections/categories the product belongs to.
        - The number of votes it received and the reasons for its recommendation or absence.
        - The questions/choices that influenced its votes, including the collections/categories where it was either upvoted or excluded.
        - The specific Results Page and Slots or Product blocks that facilitated its recommendation.

    8. **Troubleshooting and Adjustments**: With this information, you can pinpoint inconsistencies or errors in product categorization, inclusion, or exclusion. 

    !!! tip

        A common issue is a product being **misclassified** into an incorrect collection/category or **accidentally excluded** in quiz settings. Paying close attention to these details can significantly improve the accuracy of your product recommendations.

    Additionally, you may:

    - **Recalculate Recommendations**: If adjustments to the quiz or product collections/categories have been made, use this option to see how these changes affect recommendations.
    - **Resend Notifications**: Useful for updating CRM services or sending revised recommendations via email.

=== "BigCommerce" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Quiz Metrics**: First, navigate to the quiz [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.
    2. **Explore Responses**: Within Metrics, locate and open the [Responses](/reference/quiz-builder/metrics/#responses) tab. On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.
    3. Check the `Why was a product recommended or not in this response?` section. This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.
    4. **Preview the Results Page**: Use the provided link at the bottom of the response details to access the Results Page corresponding to the chosen response. 
        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)
    5. On the results page, identify a product of interest—either one that appeared unexpectedly on the Results Page or one you anticipated but was missing.
    6. **Conduct a Product Search**: Use the `SELECT PRODUCT TO CHECK` section at the top of the response to search the name of the product in question. Select the product from the search results to further investigate its recommendation status.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        **Understanding Product Status Colors**

        - **Green**: Indicates products that received votes through the quiz choices.
        - **Red**: Denotes products that were explicitly excluded from recommendations.
        - **White**: Represents products that did not receive any votes, hence their absence from the recommendations.

    7. **Analyze Product Details**: Upon selecting a product, a detailed panel will reveal critical information.

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        Information such as:

        - The collections/categories the product belongs to.
        - The number of votes it received and the reasons for its recommendation or absence.
        - The questions/choices that influenced its votes, including the collections/categories where it was either upvoted or excluded.
        - The specific Results Page and Slots or Product blocks that facilitated its recommendation.

    8. **Troubleshooting and Adjustments**: With this information, you can pinpoint inconsistencies or errors in product categorization, inclusion, or exclusion. 

    !!! tip

        A common issue is a product being **misclassified** into an incorrect collection/category or **accidentally excluded** in quiz settings. Paying close attention to these details can significantly improve the accuracy of your product recommendations.

    Additionally, you may:

    - **Recalculate Recommendations**: If adjustments to the quiz or product collections/categories have been made, use this option to see how these changes affect recommendations.
    - **Resend Notifications**: Useful for updating CRM services or sending revised recommendations via email.

=== "Standalone" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Access Quiz Metrics**: First, navigate to the quiz [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.
    2. **Explore Responses**: Within Metrics, locate and open the [Responses](/reference/quiz-builder/metrics/#responses) tab. On the left-hand side menu, you'll find the most recent 100 responses the quiz received organized by date/timestamp. Click on a date to open a specific response.
    3. Check the `Why was a product recommended or not in this response?` section. This section of the app allows you to troubleshoot individual responses and understand why certain products were recommended to the customer or missing from the recommendations.
    4. **Preview the Results Page**: Use the provided link at the bottom of the response details to access the Results Page corresponding to the chosen response. 
        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)
    5. On the results page, identify a product of interest—either one that appeared unexpectedly on the Results Page or one you anticipated but was missing.
    6. **Conduct a Product Search**: Use the `SELECT PRODUCT TO CHECK` section at the top of the response to search the name of the product in question. Select the product from the search results to further investigate its recommendation status.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        **Understanding Product Status Colors**

        - **Green**: Indicates products that received votes through the quiz choices.
        - **Red**: Denotes products that were explicitly excluded from recommendations.
        - **White**: Represents products that did not receive any votes, hence their absence from the recommendations.

    7. **Analyze Product Details**: Upon selecting a product, a detailed panel will reveal critical information.

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        Information such as:

        - The collections/categories the product belongs to.
        - The number of votes it received and the reasons for its recommendation or absence.
        - The questions/choices that influenced its votes, including the collections/categories where it was either upvoted or excluded.
        - The specific Results Page and Slots or Product blocks that facilitated its recommendation.

    8. **Troubleshooting and Adjustments**: With this information, you can pinpoint inconsistencies or errors in product categorization, inclusion, or exclusion. 

    !!! tip

        A common issue is a product being **misclassified** into an incorrect collection/category or **accidentally excluded** in quiz settings. Paying close attention to these details can significantly improve the accuracy of your product recommendations.

    Additionally, you may:

    - **Recalculate Recommendations**: If adjustments to the quiz or product collections/categories have been made, use this option to see how these changes affect recommendations.
    - **Resend Notifications**: Useful for updating CRM services or sending revised recommendations via email.

---

By following this guide, you will be better equipped to understand and refine the product recommendation process within your quiz, ensuring a more relevant and personalized customer experience.
