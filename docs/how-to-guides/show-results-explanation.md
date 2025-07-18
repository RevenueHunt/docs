---
icon: material/lightbulb-question
---


# How to Show Results Explanation

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    While our [product recommendation algorithm](/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won’t automatically display custom text depending on the recommended product.

    The legacy version of the RevenueHunt app **doesn't** have a linear score feature (as in every time a customer picks a choice, the "score" will receive one point and at the end, based on that score, different results pages will be displayed). For this reason, it can be very hard to build a **"personality-type"** quiz with our solution.

    If you want to show different text results depending on the recommended products, this functionality has to be built on the [Results Page](/reference/quiz-builder/results-page/). There are a few ways to achieve it:

    1. **Information Recalls/Content Dynamic Source**: Use [Information Recalls/Content Dynamic Source](/how-to-guides/use-information-recalls/) to display a customer's answers within a content block or a text block on the Results Page. This method helps customers understand the rationale behind each product recommendation without any coding or complex logic.

    2. **Display Logic**: [Display Logic](/reference/quiz-builder/conditional-logic/#display-logic) allows you to show or hide text on the Results Page based on the customer's quiz responses. This method is suitable for shorter, simpler quizzes. For detailed guidance on setting up Display Logic, see [here](/how-to-guides/use-display-logic/). 

        !!! tip
        
            For longer, more complex quizzes, we advise using the custom JavaScript approach for optimal flexibility.



        ??? question "How to Build a Personality-Type Quiz?"


            Imagine you want to determine a customer’s skin type. You might ask them specific questions about their skin to narrow down their unique characteristics. Here’s an example:

            ---

            **Step 1: Add Questions to the Quiz**

            **Question 1: Oiliness**  
            *"How does your skin usually feel by the middle of the day?"*  
            - **Very oily, shiny all over.** *(Oily skin)*  
            - **Oily in the T-zone (forehead, nose, chin), but dry elsewhere.** *(Combination skin)*  
            - **Balanced, not too oily or dry.** *(Normal skin)*  
            - **Dry and tight all over.** *(Dry skin)*  

            **Question 2: Sensitivity**  
            *"How does your skin react to new products or environmental changes?"*  
            - **Easily irritated, red, or itchy.** *(Sensitive skin)*  
            - **Rarely reacts, even to strong products.** *(Normal or Oily skin)*  
            - **Reacts sometimes, but not consistently.** *(Combination skin)*  

            **Question 3: Hydration**  
            *"Does your skin often feel dehydrated, regardless of oiliness?"*  
            - **Yes, it feels tight and flaky.** *(Dry or Dehydrated skin)*  
            - **Sometimes, especially in colder months.** *(Combination or Normal skin)*  
            - **Rarely or never.** *(Oily skin)*  

            ---

            **Step 2: Link Products to Choices**

            Associate each answer option with the most appropriate products. For example:  
            - Answers that indicate **Dry Skin** link to products formulated for dry skin.  
            - Answers suggesting **Oily Skin** link to products designed for oily skin.  

            This setup ensures that the quiz [product recommendation algorithm](/how-to-guides/recommend-products/) will automatically provide the most relevant product suggestions.

            *Note: This part is easy. The most difficult part is displaying the right text that corresponds to the product recommendation.*

            ---

            **Step 3: Displaying Skin Type Text Results with Display Logic**

            If you want to display a text summary, like "You have Dry/Oily/Combination/Normal skin," use **Display Logic** to conditionally show content blocks based on customer answers.  

            **Example Setup:**

            1️⃣ **Add Content Blocks to Results Page**  

            Create content blocks on your results page for each skin type. For example:  

            - *You have Dry Skin*  
            - *You have Oily Skin*  
            - *You have Combination Skin*  
            - *You have Normal Skin*  

            ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            2️⃣ **Configure Display Logic Rules**  

            Set [Display Logic](/how-to-guides/use-display-logic/) rules for when each block should appear, based on the answers.  

            **For Dry Skin:**  
            - If the answer to **Question 1: Oiliness** is *Dry and tight all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Yes, it feels tight and flaky*.  

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            **For Combination Skin:**  
            Combination skin may result from varied answer paths. You’ll need rules for multiple scenarios:  

            
            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Reacts sometimes, but not consistently*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Very oily, shiny all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, but not consistently*.         

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)
            ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)
            ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)




            3️⃣ **Repeat this process for all other possible combinations of answers.**
            
            You will have to add similar rules to all the content blocks on the Results Page to show the right text in the end. This means you will have to predict every possible combination of answers a customer can make and add it as Display logic to ensure that the correct text block is shown. 

            ---

            **Simplifying the Process**

            If configuring logic for all combinations feels overwhelming, you can try alternatives highlighted in this article, for example:  
            1. Base your logic on a single question (e.g., Question 1).  
            2. Use JavaScript to dynamically determine the skin type and display the result text.  

            ---

            This step-by-step guide will help you build a personality-type quiz tailored to your customers, making it easier to recommend the perfect products and deliver valuable insights.          



    3. **Custom JavaScript**: For a more refined approach, consider hiring a developer to create a custom JavaScript function. This function can show specific text tailored to the ID of the recommended product. Your developer could also add custom values to quiz choices and create a scoring system for the quiz to then display the right text on the results page. 

        !!! tip

            Instructions on adding custom JavaScript to your Product Recommendation Quiz can be found [here](/how-to-guides/add-javascript/).

    4. **Product Descriptions**: Another option is to enrich your product descriptions with information explaining why each product is recommended. These descriptions are pulled directly from your store's product list. You can manage the visibility of these descriptions in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings -> Show description`. Additionally, you have the option to truncate these descriptions for better readability.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/2b244cde228e450c9908aed5459b99f2?sid=ab8b600e-5464-4c0a-b982-5a1e5627c994" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    While our [product recommendation algorithm](/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation text of **why** a certain product was recommended. It also won’t *automatically* display custom text depending on the recommended product. 
    
    However, there are a few easy ways to show such a custom result text/explanation with the new Built for Shopify version of the RevenueHunt app.

    - The new Built for Shopify version of the RevenueHunt app allows you to set up different section on the results page with different text + product recommendations combinations. 
    
    - You can then use the [Display Logic](/reference/quiz-builder/conditional-logic/#display-logic) feature to tell each section when to be shown or hidden based on a customer answers, variable or a score.  
    
    - For this reason, it can be very easy to build a **"personality-type"** or **Dosha** quiz with our Built for Shopify solution.

    !!! info
    
        To learn how to **use Display Logic** to show different sections on the results page, check [this guide](/how-to-guides/use-display-logic/).

        You can also check [this guide](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) on settings up a quiz with the winning variable or [this guide](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page) on how to set up a quiz with a custom scoring system. Both options are good for building a **personality-type** quiz.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    While our [product recommendation algorithm](/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won’t automatically display custom text depending on the recommended product.

    RevenueHunt app **doesn't** have a linear score feature yet (as in every time a customer picks a choice, the "score" will receive one point and at the end, based on that score, different results pages will be displayed). For this reason, it can be very hard to build a **"personality-type"** quiz with our solution.

    If you want to show different text results depending on the recommended products, this functionality has to be built on the [Results Page](/reference/quiz-builder/results-page/). There are a few ways to achieve it:

    1. **Information Recalls/Content Dynamic Source**: Use [Information Recalls/Content Dynamic Source](/how-to-guides/use-information-recalls/) to display a customer's answers within a content block or a text block on the Results Page. This method helps customers understand the rationale behind each product recommendation without any coding or complex logic.

    2. **Display Logic**: [Display Logic](/reference/quiz-builder/conditional-logic/#display-logic) allows you to show or hide text on the Results Page based on the customer's quiz responses. This method is suitable for shorter, simpler quizzes. For detailed guidance on setting up Display Logic, see [here](/how-to-guides/use-display-logic/). 

        !!! tip
        
            For longer, more complex quizzes, we advise using the custom JavaScript approach for optimal flexibility.



        ??? question "How to Build a Personality-Type Quiz?"


            Imagine you want to determine a customer’s skin type. You might ask them specific questions about their skin to narrow down their unique characteristics. Here’s an example:

            ---

            **Step 1: Add Questions to the Quiz**

            **Question 1: Oiliness**  
            *"How does your skin usually feel by the middle of the day?"*  
            - **Very oily, shiny all over.** *(Oily skin)*  
            - **Oily in the T-zone (forehead, nose, chin), but dry elsewhere.** *(Combination skin)*  
            - **Balanced, not too oily or dry.** *(Normal skin)*  
            - **Dry and tight all over.** *(Dry skin)*  

            **Question 2: Sensitivity**  
            *"How does your skin react to new products or environmental changes?"*  
            - **Easily irritated, red, or itchy.** *(Sensitive skin)*  
            - **Rarely reacts, even to strong products.** *(Normal or Oily skin)*  
            - **Reacts sometimes, but not consistently.** *(Combination skin)*  

            **Question 3: Hydration**  
            *"Does your skin often feel dehydrated, regardless of oiliness?"*  
            - **Yes, it feels tight and flaky.** *(Dry or Dehydrated skin)*  
            - **Sometimes, especially in colder months.** *(Combination or Normal skin)*  
            - **Rarely or never.** *(Oily skin)*  

            ---

            **Step 2: Link Products to Choices**

            Associate each answer option with the most appropriate products. For example:  
            - Answers that indicate **Dry Skin** link to products formulated for dry skin.  
            - Answers suggesting **Oily Skin** link to products designed for oily skin.  

            This setup ensures that the quiz [product recommendation algorithm](/how-to-guides/recommend-products/) will automatically provide the most relevant product suggestions.

            *Note: This part is easy. The most difficult part is displaying the right text that corresponds to the product recommendation.*

            ---

            **Step 3: Displaying Skin Type Text Results with Display Logic**

            If you want to display a text summary, like "You have Dry/Oily/Combination/Normal skin," use **Display Logic** to conditionally show content blocks based on customer answers.  

            **Example Setup:**

            1️⃣ **Add Content Blocks to Results Page**  

            Create content blocks on your results page for each skin type. For example:  

            - *You have Dry Skin*  
            - *You have Oily Skin*  
            - *You have Combination Skin*  
            - *You have Normal Skin*  

            ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            2️⃣ **Configure Display Logic Rules**  

            Set [Display Logic](/how-to-guides/use-display-logic/) rules for when each block should appear, based on the answers.  

            **For Dry Skin:**  
            - If the answer to **Question 1: Oiliness** is *Dry and tight all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Yes, it feels tight and flaky*.  

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            **For Combination Skin:**  
            Combination skin may result from varied answer paths. You’ll need rules for multiple scenarios:  

            
            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Reacts sometimes, but not consistently*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Very oily, shiny all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, but not consistently*.         

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)
            ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)
            ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)




            3️⃣ **Repeat this process for all other possible combinations of answers.**
            
            You will have to add similar rules to all the content blocks on the Results Page to show the right text in the end. This means you will have to predict every possible combination of answers a customer can make and add it as Display logic to ensure that the correct text block is shown. 

            ---

            **Simplifying the Process**

            If configuring logic for all combinations feels overwhelming, you can try alternatives highlighted in this article, for example:  
            1. Base your logic on a single question (e.g., Question 1).  
            2. Use JavaScript to dynamically determine the skin type and display the result text.  

            ---

            This step-by-step guide will help you build a personality-type quiz tailored to your customers, making it easier to recommend the perfect products and deliver valuable insights.          



    3. **Custom JavaScript**: For a more refined approach, consider hiring a developer to create a custom JavaScript function. This function can show specific text tailored to the ID of the recommended product. Your developer could also add custom values to quiz choices and create a scoring system for the quiz to then display the right text on the results page. 

        !!! tip

            Instructions on adding custom JavaScript to your Product Recommendation Quiz can be found [here](/how-to-guides/add-javascript/).

    4. **Product Descriptions**: Another option is to enrich your product descriptions with information explaining why each product is recommended. These descriptions are pulled directly from your store's product list. You can manage the visibility of these descriptions in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings -> Show description`. Additionally, you have the option to truncate these descriptions for better readability.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    While our [product recommendation algorithm](/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won’t automatically display custom text depending on the recommended product.

    RevenueHunt app **doesn't** have a linear score feature yet (as in every time a customer picks a choice, the "score" will receive one point and at the end, based on that score, different results pages will be displayed). For this reason, it can be very hard to build a **"personality-type"** quiz with our solution.

    If you want to show different text results depending on the recommended products, this functionality has to be built on the [Results Page](/reference/quiz-builder/results-page/). There are a few ways to achieve it:

    1. **Information Recalls/Content Dynamic Source**: Use [Information Recalls/Content Dynamic Source](/how-to-guides/use-information-recalls/) to display a customer's answers within a content block or a text block on the Results Page. This method helps customers understand the rationale behind each product recommendation without any coding or complex logic.

    2. **Display Logic**: [Display Logic](/reference/quiz-builder/conditional-logic/#display-logic) allows you to show or hide text on the Results Page based on the customer's quiz responses. This method is suitable for shorter, simpler quizzes. For detailed guidance on setting up Display Logic, see [here](/how-to-guides/use-display-logic/). 

        !!! tip
        
            For longer, more complex quizzes, we advise using the custom JavaScript approach for optimal flexibility.



        ??? question "How to Build a Personality-Type Quiz?"


            Imagine you want to determine a customer’s skin type. You might ask them specific questions about their skin to narrow down their unique characteristics. Here’s an example:

            ---

            **Step 1: Add Questions to the Quiz**

            **Question 1: Oiliness**  
            *"How does your skin usually feel by the middle of the day?"*  
            - **Very oily, shiny all over.** *(Oily skin)*  
            - **Oily in the T-zone (forehead, nose, chin), but dry elsewhere.** *(Combination skin)*  
            - **Balanced, not too oily or dry.** *(Normal skin)*  
            - **Dry and tight all over.** *(Dry skin)*  

            **Question 2: Sensitivity**  
            *"How does your skin react to new products or environmental changes?"*  
            - **Easily irritated, red, or itchy.** *(Sensitive skin)*  
            - **Rarely reacts, even to strong products.** *(Normal or Oily skin)*  
            - **Reacts sometimes, but not consistently.** *(Combination skin)*  

            **Question 3: Hydration**  
            *"Does your skin often feel dehydrated, regardless of oiliness?"*  
            - **Yes, it feels tight and flaky.** *(Dry or Dehydrated skin)*  
            - **Sometimes, especially in colder months.** *(Combination or Normal skin)*  
            - **Rarely or never.** *(Oily skin)*  

            ---

            **Step 2: Link Products to Choices**

            Associate each answer option with the most appropriate products. For example:  
            - Answers that indicate **Dry Skin** link to products formulated for dry skin.  
            - Answers suggesting **Oily Skin** link to products designed for oily skin.  

            This setup ensures that the quiz [product recommendation algorithm](/how-to-guides/recommend-products/) will automatically provide the most relevant product suggestions.

            *Note: This part is easy. The most difficult part is displaying the right text that corresponds to the product recommendation.*

            ---

            **Step 3: Displaying Skin Type Text Results with Display Logic**

            If you want to display a text summary, like "You have Dry/Oily/Combination/Normal skin," use **Display Logic** to conditionally show content blocks based on customer answers.  

            **Example Setup:**

            1️⃣ **Add Content Blocks to Results Page**  

            Create content blocks on your results page for each skin type. For example:  

            - *You have Dry Skin*  
            - *You have Oily Skin*  
            - *You have Combination Skin*  
            - *You have Normal Skin*  

            ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            2️⃣ **Configure Display Logic Rules**  

            Set [Display Logic](/how-to-guides/use-display-logic/) rules for when each block should appear, based on the answers.  

            **For Dry Skin:**  
            - If the answer to **Question 1: Oiliness** is *Dry and tight all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Yes, it feels tight and flaky*.  

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            **For Combination Skin:**  
            Combination skin may result from varied answer paths. You’ll need rules for multiple scenarios:  

            
            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Reacts sometimes, but not consistently*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Very oily, shiny all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, but not consistently*.         

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)
            ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)
            ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)




            3️⃣ **Repeat this process for all other possible combinations of answers.**
            
            You will have to add similar rules to all the content blocks on the Results Page to show the right text in the end. This means you will have to predict every possible combination of answers a customer can make and add it as Display logic to ensure that the correct text block is shown. 

            ---

            **Simplifying the Process**

            If configuring logic for all combinations feels overwhelming, you can try alternatives highlighted in this article, for example:  
            1. Base your logic on a single question (e.g., Question 1).  
            2. Use JavaScript to dynamically determine the skin type and display the result text.  

            ---

            This step-by-step guide will help you build a personality-type quiz tailored to your customers, making it easier to recommend the perfect products and deliver valuable insights.          



    3. **Custom JavaScript**: For a more refined approach, consider hiring a developer to create a custom JavaScript function. This function can show specific text tailored to the ID of the recommended product. Your developer could also add custom values to quiz choices and create a scoring system for the quiz to then display the right text on the results page. 

        !!! tip

            Instructions on adding custom JavaScript to your Product Recommendation Quiz can be found [here](/how-to-guides/add-javascript/).

    4. **Product Descriptions**: Another option is to enrich your product descriptions with information explaining why each product is recommended. These descriptions are pulled directly from your store's product list. You can manage the visibility of these descriptions in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings -> Show description`. Additionally, you have the option to truncate these descriptions for better readability.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    While our [product recommendation algorithm](/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won’t automatically display custom text depending on the recommended product.

    RevenueHunt app **doesn't** have a linear score feature yet (as in every time a customer picks a choice, the "score" will receive one point and at the end, based on that score, different results pages will be displayed). For this reason, it can be very hard to build a **"personality-type"** quiz with our solution.

    If you want to show different text results depending on the recommended products, this functionality has to be built on the [Results Page](/reference/quiz-builder/results-page/). There are a few ways to achieve it:

    1. **Information Recalls/Content Dynamic Source**: Use [Information Recalls/Content Dynamic Source](/how-to-guides/use-information-recalls/) to display a customer's answers within a content block or a text block on the Results Page. This method helps customers understand the rationale behind each product recommendation without any coding or complex logic.

    2. **Display Logic**: [Display Logic](/reference/quiz-builder/conditional-logic/#display-logic) allows you to show or hide text on the Results Page based on the customer's quiz responses. This method is suitable for shorter, simpler quizzes. For detailed guidance on setting up Display Logic, see [here](/how-to-guides/use-display-logic/). 

        !!! tip
        
            For longer, more complex quizzes, we advise using the custom JavaScript approach for optimal flexibility.



        ??? question "How to Build a Personality-Type Quiz?"


            Imagine you want to determine a customer’s skin type. You might ask them specific questions about their skin to narrow down their unique characteristics. Here’s an example:

            ---

            **Step 1: Add Questions to the Quiz**

            **Question 1: Oiliness**  
            *"How does your skin usually feel by the middle of the day?"*  
            - **Very oily, shiny all over.** *(Oily skin)*  
            - **Oily in the T-zone (forehead, nose, chin), but dry elsewhere.** *(Combination skin)*  
            - **Balanced, not too oily or dry.** *(Normal skin)*  
            - **Dry and tight all over.** *(Dry skin)*  

            **Question 2: Sensitivity**  
            *"How does your skin react to new products or environmental changes?"*  
            - **Easily irritated, red, or itchy.** *(Sensitive skin)*  
            - **Rarely reacts, even to strong products.** *(Normal or Oily skin)*  
            - **Reacts sometimes, but not consistently.** *(Combination skin)*  

            **Question 3: Hydration**  
            *"Does your skin often feel dehydrated, regardless of oiliness?"*  
            - **Yes, it feels tight and flaky.** *(Dry or Dehydrated skin)*  
            - **Sometimes, especially in colder months.** *(Combination or Normal skin)*  
            - **Rarely or never.** *(Oily skin)*  

            ---

            **Step 2: Link Products to Choices**

            Associate each answer option with the most appropriate products. For example:  
            - Answers that indicate **Dry Skin** link to products formulated for dry skin.  
            - Answers suggesting **Oily Skin** link to products designed for oily skin.  

            This setup ensures that the quiz [product recommendation algorithm](/how-to-guides/recommend-products/) will automatically provide the most relevant product suggestions.

            *Note: This part is easy. The most difficult part is displaying the right text that corresponds to the product recommendation.*

            ---

            **Step 3: Displaying Skin Type Text Results with Display Logic**

            If you want to display a text summary, like "You have Dry/Oily/Combination/Normal skin," use **Display Logic** to conditionally show content blocks based on customer answers.  

            **Example Setup:**

            1️⃣ **Add Content Blocks to Results Page**  

            Create content blocks on your results page for each skin type. For example:  

            - *You have Dry Skin*  
            - *You have Oily Skin*  
            - *You have Combination Skin*  
            - *You have Normal Skin*  

            ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            2️⃣ **Configure Display Logic Rules**  

            Set [Display Logic](/how-to-guides/use-display-logic/) rules for when each block should appear, based on the answers.  

            **For Dry Skin:**  
            - If the answer to **Question 1: Oiliness** is *Dry and tight all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Yes, it feels tight and flaky*.  

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            **For Combination Skin:**  
            Combination skin may result from varied answer paths. You’ll need rules for multiple scenarios:  

            
            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Reacts sometimes, but not consistently*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Very oily, shiny all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, but not consistently*.         

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)
            ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)
            ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)




            3️⃣ **Repeat this process for all other possible combinations of answers.**
            
            You will have to add similar rules to all the content blocks on the Results Page to show the right text in the end. This means you will have to predict every possible combination of answers a customer can make and add it as Display logic to ensure that the correct text block is shown. 

            ---

            **Simplifying the Process**

            If configuring logic for all combinations feels overwhelming, you can try alternatives highlighted in this article, for example:  
            1. Base your logic on a single question (e.g., Question 1).  
            2. Use JavaScript to dynamically determine the skin type and display the result text.  

            ---

            This step-by-step guide will help you build a personality-type quiz tailored to your customers, making it easier to recommend the perfect products and deliver valuable insights.          



    3. **Custom JavaScript**: For a more refined approach, consider hiring a developer to create a custom JavaScript function. This function can show specific text tailored to the ID of the recommended product. Your developer could also add custom values to quiz choices and create a scoring system for the quiz to then display the right text on the results page. 

        !!! tip

            Instructions on adding custom JavaScript to your Product Recommendation Quiz can be found [here](/how-to-guides/add-javascript/).

    4. **Product Descriptions**: Another option is to enrich your product descriptions with information explaining why each product is recommended. These descriptions are pulled directly from your store's product list. You can manage the visibility of these descriptions in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings -> Show description`. Additionally, you have the option to truncate these descriptions for better readability.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    While our [product recommendation algorithm](/how-to-guides/recommend-products/) works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won’t automatically display custom text depending on the recommended product.

    RevenueHunt app **doesn't** have a linear score feature yet (as in every time a customer picks a choice, the "score" will receive one point and at the end, based on that score, different results pages will be displayed). For this reason, it can be very hard to build a **"personality-type"** quiz with our solution.

    If you want to show different text results depending on the recommended products, this functionality has to be built on the [Results Page](/reference/quiz-builder/results-page/). There are a few ways to achieve it:

    1. **Information Recalls/Content Dynamic Source**: Use [Information Recalls/Content Dynamic Source](/how-to-guides/use-information-recalls/) to display a customer's answers within a content block or a text block on the Results Page. This method helps customers understand the rationale behind each product recommendation without any coding or complex logic.

    2. **Display Logic**: [Display Logic](/reference/quiz-builder/conditional-logic/#display-logic) allows you to show or hide text on the Results Page based on the customer's quiz responses. This method is suitable for shorter, simpler quizzes. For detailed guidance on setting up Display Logic, see [here](/how-to-guides/use-display-logic/). 

        !!! tip
        
            For longer, more complex quizzes, we advise using the custom JavaScript approach for optimal flexibility.



        ??? question "How to Build a Personality-Type Quiz?"


            Imagine you want to determine a customer’s skin type. You might ask them specific questions about their skin to narrow down their unique characteristics. Here’s an example:

            ---

            **Step 1: Add Questions to the Quiz**

            **Question 1: Oiliness**  
            *"How does your skin usually feel by the middle of the day?"*  
            - **Very oily, shiny all over.** *(Oily skin)*  
            - **Oily in the T-zone (forehead, nose, chin), but dry elsewhere.** *(Combination skin)*  
            - **Balanced, not too oily or dry.** *(Normal skin)*  
            - **Dry and tight all over.** *(Dry skin)*  

            **Question 2: Sensitivity**  
            *"How does your skin react to new products or environmental changes?"*  
            - **Easily irritated, red, or itchy.** *(Sensitive skin)*  
            - **Rarely reacts, even to strong products.** *(Normal or Oily skin)*  
            - **Reacts sometimes, but not consistently.** *(Combination skin)*  

            **Question 3: Hydration**  
            *"Does your skin often feel dehydrated, regardless of oiliness?"*  
            - **Yes, it feels tight and flaky.** *(Dry or Dehydrated skin)*  
            - **Sometimes, especially in colder months.** *(Combination or Normal skin)*  
            - **Rarely or never.** *(Oily skin)*  

            ---

            **Step 2: Link Products to Choices**

            Associate each answer option with the most appropriate products. For example:  
            - Answers that indicate **Dry Skin** link to products formulated for dry skin.  
            - Answers suggesting **Oily Skin** link to products designed for oily skin.  

            This setup ensures that the quiz [product recommendation algorithm](/how-to-guides/recommend-products/) will automatically provide the most relevant product suggestions.

            *Note: This part is easy. The most difficult part is displaying the right text that corresponds to the product recommendation.*

            ---

            **Step 3: Displaying Skin Type Text Results with Display Logic**

            If you want to display a text summary, like "You have Dry/Oily/Combination/Normal skin," use **Display Logic** to conditionally show content blocks based on customer answers.  

            **Example Setup:**

            1️⃣ **Add Content Blocks to Results Page**  

            Create content blocks on your results page for each skin type. For example:  

            - *You have Dry Skin*  
            - *You have Oily Skin*  
            - *You have Combination Skin*  
            - *You have Normal Skin*  

            ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            2️⃣ **Configure Display Logic Rules**  

            Set [Display Logic](/how-to-guides/use-display-logic/) rules for when each block should appear, based on the answers.  

            **For Dry Skin:**  
            - If the answer to **Question 1: Oiliness** is *Dry and tight all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Yes, it feels tight and flaky*.  

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            **For Combination Skin:**  
            Combination skin may result from varied answer paths. You’ll need rules for multiple scenarios:  

            
            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Reacts sometimes, but not consistently*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Very oily, shiny all over*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, especially in colder months*.  

            **OR**

            - If the answer to **Question 1: Oiliness** is *Oily in the T-zone (forehead, nose, chin), but dry elsewhere*.  
            - AND the answer to **Question 2: Sensitivity** is *Easily irritated, red, or itchy*.  
            - AND the answer to **Question 3: Hydration** is *Sometimes, but not consistently*.         

            Then this block will be **Visible**; otherwise, it remains hidden.  

            ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)
            ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)
            ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)




            3️⃣ **Repeat this process for all other possible combinations of answers.**
            
            You will have to add similar rules to all the content blocks on the Results Page to show the right text in the end. This means you will have to predict every possible combination of answers a customer can make and add it as Display logic to ensure that the correct text block is shown. 

            ---

            **Simplifying the Process**

            If configuring logic for all combinations feels overwhelming, you can try alternatives highlighted in this article, for example:  
            1. Base your logic on a single question (e.g., Question 1).  
            2. Use JavaScript to dynamically determine the skin type and display the result text.  

            ---

            This step-by-step guide will help you build a personality-type quiz tailored to your customers, making it easier to recommend the perfect products and deliver valuable insights.          



    3. **Custom JavaScript**: For a more refined approach, consider hiring a developer to create a custom JavaScript function. This function can show specific text tailored to the ID of the recommended product. Your developer could also add custom values to quiz choices and create a scoring system for the quiz to then display the right text on the results page. 

        !!! tip

            Instructions on adding custom JavaScript to your Product Recommendation Quiz can be found [here](/how-to-guides/add-javascript/).

    4. **Product Descriptions**: Another option is to enrich your product descriptions with information explaining why each product is recommended. These descriptions are pulled directly from your store's product list. You can manage the visibility of these descriptions in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings -> Show description`. Additionally, you have the option to truncate these descriptions for better readability.


---
This article explains how to show why a certain product was recommended to the customer.