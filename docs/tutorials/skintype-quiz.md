---
icon: material/numeric-3
---

# Building a Skin Type Quiz with RevenueHunt App

=== "Shopify"

    Scoring system is not available in the legacy version of the RevenueHunt app for Shopify. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.
    
    Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check [this article](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) to learn how to  recommend products based on the number of user choices in the legacy version of the RevenueHunt app for Shopify.
    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Shopify V2"

    In this tutorial, you’ll learn how to build a quiz that determines the user's skin type and recommends the right products with RevenueHunt App.

    !!! info "You’ll learn:"

        - how to build a personality-type quiz
        - how to assign scores and variables to choices
        - how to show different sections to the results page depending on customer answers
        - how to use display logic to show different sections to the results page depending on customer answers
        - how to show fixed products on the results page
        - how to troubleshoot quiz results
        - how to publish the quiz as a linked button on your Shopify website

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/hRnkKBIzWFc?si=A6p-yYVTu4ZXPqc_" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    This documentation outlines the steps to create a skin type quiz that recommends products based on user responses. It covers quiz setup, variable assignment, results configuration, and integration into a Shopify store.


    ## Plan the Quiz

    Before you begin building your quiz, it’s important to plan what you want to show at the end.

    For each skin type — dry, oily, combination, normal, or sensitive — write a short description and decide which products you want to recommend.

    These will be set up on the results page later, so it’s good to have everything ready in advance.

    ??? example "Sample Skin Types & Recommendations Matrix:"

        | Skin Type          | Heading                | Description                                                                                                                                                                                                                                   | Recommended Products |
        |--------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
        | 🌵 Dry Skin         | You have Dry Skin       | Your skin tends to feel tight, rough, or flaky — especially after washing. It may need extra TLC in the form of rich moisturizers and gentle, hydrating cleansers. Look for ingredients like hyaluronic acid, glycerin, and ceramides to help restore moisture and improve texture.<br><br>**Tip:** Avoid over-exfoliating and opt for creamy, non-stripping products. | 1. Relaxing Night Cream<br>2. Ultra Facial Deep Moisture Balm<br>3. Vitamin C Serum |
        | 🌼 Normal Skin      | You have Normal Skin    | Lucky you! Your skin feels balanced, neither too oily nor too dry. You may have occasional concerns, but overall, your skin is low-maintenance. Focus on maintaining that balance with a simple, consistent skincare routine.<br><br>**Tip:** Keep it steady with gentle cleansers, light hydration, and sunscreen. | 1. Morning Cleanser<br>2. Fresh Rose Deep Hydration Toner<br>3. Organix Facial Moisturizer |
        | 💧 Oily Skin        | You have Oily Skin      | Your skin produces more oil than average, especially in the T-zone. Shine and breakouts might be common, but the upside is slower visible aging! Stick with lightweight, non-comedogenic products that help balance oil without stripping your skin.<br><br>**Tip:** Use gel-based moisturizers, salicylic acid, and clay masks to manage oil and minimize pores. | 1. Balancing Force Oil Control Toner<br>2. Oil-Free Moisture-Combination Skin<br>3. Neutrogena Oil-Free Acne Face Wash |
        | 🌗 Combination Skin | You have Combination Skin | Your skin is a mix — oily in some spots (like the T-zone) and dry or normal in others. You’ll benefit from targeting different areas with different products or using lightweight, balanced formulas.<br><br>**Tip:** Try multi-masking or spot-treating for a tailored approach to your skin’s varying needs. | 1. Oil-Free Moisture-Combination Skin<br>2. Super Antioxidant Serum<br>3. United State Balancing Tonic |
        | 🌸 Sensitive Skin   | You have Sensitive Skin | Your skin reacts easily — whether it’s to weather changes, new products, or stress. Redness, itching, or stinging might be common for you. A minimalist routine with soothing ingredients is your best friend.<br><br>**Tip:** Choose fragrance-free, hypoallergenic products with calming ingredients like aloe vera, chamomile, or calendula. | 1. Redness-Relief Refreshing Cleansing Lotion<br>2. Aloe Soothing Toner<br>3. Soothing Serum |


    ## Build the Quiz

    Next, let’s build the quiz. 
    
    1. Head over to the [Quiz Builder](/reference/quiz-builder/) > [Questions](/reference/quiz-builder/questions/).
    2. Add [multiple-choice questions](/reference/quiz-builder/questions/#multiple-choice) with 5 choices each. These should help determine the customer’s skin condition. Each question and choice should give clues about the user's skin type.

        !!! tip
            Check out our previous tutorial to learn how to use the Quiz Builder and add questions: [How to Make Your First Quiz](/tutorials/making-first-quiz/).


        !!! example "Sample Questions:"

            Question 1: How does your skin feel when you wake up in the morning?

            - Choice 1: Tight 
            - Choice 2: Normal 
            - Choice 3: Oily 
            - Choice 4: Combination 
            - Choice 5: Sensitive 

            Question 2: How does your skin usually look by midday?

            - Choice 1: Still tight 
            - Choice 2: Same as in the morning 
            - Choice 3: Shiny 
            - Choice 4: T-zone shiny 
            - Choice 5: Red and irritated 



    ## Assign Variables to Choices

    Now it’s time to assign variables and scores to each choice.

    1. Click on a choice to open the [Choice Settings](/reference/quiz-builder/questions/#choice-settings).
    2. Scroll to `Scores & Calculations` and add a new variable.
    3. To create a new variable, click on the `Search or create variable` search bar and start typing the name of the variable you want to create (e.g. `dry_skin`, `normal_skin`, `oily_skin`, etc.). Once you've typed the full name, a dropdown will appear that will allow you to `Create a new variable "xxx"`. Click on it to add a new variable.
    4. Assign a score of 1 to the matching variable.
    5. Repeat the process for each choice in that question and move on to the next question in your quiz.

        !!! note

            In the end, the variable with the highest total score will be used to determine the result.

        !!! example "Sample Scores & Variables:"
        
            Question 1: How does your skin feel when you wake up in the morning?

            - Choice 1: Tight (variable `dry_skin` +1)
            - Choice 2: Normal (variable `normal_skin` +1)
            - Choice 3: Oily (variable `oily_skin` +1)
            - Choice 4: Combination (variable `combination_skin` +1)
            - Choice 5: Sensitive (variable `sensitive_skin` +1)      

            Question 2: How does your skin usually look by midday?

            - Choice 1: Still tight (variable `dry_skin` +1)
            - Choice 2: Same as in the morning (variable `normal_skin` +1)
            - Choice 3: Shiny (variable `oily_skin` +1)
            - Choice 4: T-zone shiny (variable `combination_skin` +1)
            - Choice 5: Red and irritated (variable `sensitive_skin` +1)


    ## Add Sections to Results Page

    Now let’s edit the Results Page.
    
    1. Head over to the [Results Page](/reference/quiz-builder/results-page/).
    2. Click `+ Add section` to add a new section to your results page.
    3. Add five different sections — one for each skin type.
    4. In each section, add:
        - A [heading](/reference/quiz-builder/results-page/#heading),
        - A short [text description](/reference/quiz-builder/results-page/#text) of what that means,
        - A [Product Block](/reference/quiz-builder/results-page/.#products-products-variants-collections)
    5. In the [Product Block settings](/reference/quiz-builder/results-page/#products-products-variants-collections), choose the Recommendations System to be `Fixed Recommendations`.
    6. In the [Product Slot](/reference/quiz-builder/results-page/#product-slot) settings, select the `Max. recommended items` and click on `Select products` to manually select the products that match that skin type.
    7. Repeat the process for each skin type section.



    ## Add Display Logic

    Now let’s tell the app *when* to show each section.

    1. Click a specific section to open the `Results Section` settings.
    2. Go to [Display Logic](/reference/quiz-builder/results-page/#display-logic) and click `+ Add condition (OR)`.
    3. Show the section if the corresponding variable has the highest score (e.g., dry skin). Ensure default visibility is set to hidden for all sections until conditions are met.  
    
        Set the conditions like this:

        - IF `the variable with the highest score` `IS` `dry_skin` THEN this section is VISIBLE.
        - Default visibility should be `HIDDEN`.

    4. Repeat this for each skin type section using their corresponding variable.

        !!! example "Sample Display Logic:"

            - IF `the variable with the highest score` `IS` `dry_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `normal_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `oily_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `combination_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `sensitive_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.

    5. Save the changes with the `Save` button.

    ## Preview

    Once everything’s set up, click `Preview` to test your quiz.

    Choose different answers to simulate different skin types, and make sure the correct section and products are shown on the results page.


    ## Troubleshoot Results

    If you see the wrong result, double-check your variables and scoring in the [Questions](/reference/quiz-builder/questions/) tab.

    If you need help debugging, go to the [Responses](/reference/quiz-builder/metrics/#responses) tab and open [Analysis](/reference/quiz-builder/metrics/#response-analysis).

    This section:

    - shows you which variables were scored during a quiz session and in which answer,
    - shows logic behind sections visibility,
    - gives you an overview of the quiz results,
    - gives you access to [Quiz Copilot](/reference/quiz-builder/metrics/#quiz-copilot), an AI assistant that can help you analyze the response.

    You can adjust scores or questions based on the analysis.
    


    ## Publish the Quiz as Link Button

    In Shopify, you can make the quiz appear as a popup by simply linking a button or menu item to `#quiz`.

    1. Set the quiz as default by going to the [Dashboard](/reference/dashboard/) and clicking on the `Set as default` button.
    2. Head over to the [Publish](/reference/quiz-builder/share-publish/) tab and check the `Add the quiz as a link triggered pop-up` option for step-bystep instructions on how to do this.
    3. In Shopify, go to `Online Store > Themes`, and click `Customize` on your current theme.
    4. Go to `App Embeds` in the left sidebar. Find the `Link Popup Quiz` by Rand make sure it’s toggled on.  This will load the quiz script and allow it to open in a popup when the link is clicked.
    5. Now, to add a quiz button. Inside the theme editor, choose a section that contains a button, like `Rich text`.
    6. Edit the section heading and the text on the button.
    7. In the `Button Link` field, type `#quiz`. Just that — not a full URL.

        !!! warning
            Don't link the full URL to the quiz like `https://your-store.com/#quiz`. Otherwise, the quiz will not open. Instead, use the `#quiz` hash only.
    8. Once done, click `Save`.

    And that’s it! Your quiz is now live and accessible via a popup link on your site.

    You’ve just created a skin type quiz with personalized product recommendations using RevenueHunt.

    !!! tip
        You can find a ready-made template for this quiz in the [Create New Quiz](/reference/dashboard/#new-quiz) section of the app, so feel free to use it as a starting point and customize it as needed.


=== "WooCommerce"

    Scoring system is not available in the RevenueHunt app for WooCommerce. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 


    !!! tip 
        Check [this article](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) to learn how to  recommend products based on the number of user choices in the legacy version of the RevenueHunt app for Shopify.
    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Magento"

    Scoring system is not available in the RevenueHunt app for Magento. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 


    !!! tip 
        Check [this article](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) to learn how to  recommend products based on the number of user choices in the legacy version of the RevenueHunt app for Shopify.
    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).



=== "BigCommerce"

    Scoring system is not available in the RevenueHunt app for BigCommerce. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 


    !!! tip 
        Check [this article](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) to learn how to  recommend products based on the number of user choices in the legacy version of the RevenueHunt app for Shopify.
    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 


    !!! tip 
        Check [this article](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) to learn how to  recommend products based on the number of user choices in the legacy version of the RevenueHunt app for Shopify.
    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

---
This article explains how to build a quiz that determines the user's skin type and recommends the right products with RevenueHunt App.







