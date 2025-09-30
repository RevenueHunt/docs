# How to Set Up Scoring Quiz

Assign variables and scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the most voted varaibl or a score.

!!! info "Use this method for:"

    - Personality type quizzes, Dosha quizzes
    - Quizzes that show different results based on the number of user choices (for example if the customer chooses most As, Bs, Cs, etc.)
    - Quizzes that show different text results based on choices
    - Quizzes that need to calculate scores that show different products


## How to Add Scores or Variables to Choices

=== "Shopify (Legacy)"

    Scoring system is not available in the legacy version of the RevenueHunt app for Shopify. Your developer can implement a custom scoring system with JavaScript on the Results Page instead.    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Shopify" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/f4daa9fcce0e4764865b49844600b7e0?sid=9529b937-8c1f-42f6-86b1-edcbbc717c8e" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Custom scores or variables can be assigned to choices in the quiz in order to set up a scoring quiz, personality type quiz, dosha quiz, etc.

    To add scores or variables to choices, follow these steps:

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. For example: age, skincondition, etc. if you are building a quzi that determines a skin type.
    2. Open the [Choice Settings](/reference/quiz-builder/questions/#choice-settings).
    3. Find the `Scores and calculations` section.
    4. You can adjust the pre-made 'score' variable for each choice with the up/down arrows. You can assign negative values if needed

        ![how to add scores or variables to choices](https://loom.com/i/8180f5a1dd8c48a894ac3a6300bd7fe4?workflows_screenshot=true)
        !!! example

            - For choice one, set the score to 1.
            - For choice two, set the score to 2.
            - For choice three, set the score to 3.

    5. To create a new variable, click on the `Search or create variable` search bar and start typing the name of the variable you want to create (e.g. `dry skin` or `variable1`). 
    6. Once you've typed the full name, a dropdown will appear that will allow you to `Create a new variable "xxx"`. Click on it to add a new variable.

        ![how to add scores or variables to choices](https://loom.com/i/7b28b691b0e8451dadaaab68807ae51f?workflows_screenshot=true)
    7. Once a new variable is created, you can assign a score to it.
    8. Repeat the process for each choice in that question and move on to the next question in your quiz.

    !!! tip

        To learn how to use these variables to set up a personality type quiz, dosha quiz, scoring quiz, etc. check out the following articles:

        - [How to Use Display Logic](/how-to-guides/use-display-logic/)
        - [How to Set Up a Personality Type Quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz)
        - [How to Set Up a Scoring Quiz](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page)

=== "WooCommerce"

    Scoring system is not available in the WooCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Magento"

    Scoring system is not available in the Magento version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    Scoring system is not available in the BigCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

## Winning Variable Quiz 

Assign variables and scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the most voted varaible.

![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_varaiblequiz.png){width=500}

Follow these steps to set up a winning variable quiz:       

=== "Shopify"

    <div style="position: relative; padding-bottom: 74.27785419532324%; height: 0;"><iframe src="https://www.loom.com/embed/7b44356b9eba4fb3a24b6e595fd48088?sid=f5da200d-6189-457b-8a99-24395da4df8a" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Let's imagine you are creating a quiz for a skin care brand. You want to know which skin type the customer has.

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their skin condition. For example: itchiness, tightness, dryness, etc. if you are creating a quiz for a skin care brand.

    2. **Assign Variables and Scores to Choices**: Go to each question in your quiz. For each choice, open the [choice settings](/reference/quiz-builder/questions/#choice-settings) and [assign varibales to each choice](/how-to-guides/set-up-scoring-quiz/#how-to-add-scores-or-variables-to-choices). 

        !!! tip

            To learn how to add scores or variables to choices, check out this guide: [How to Add Scores or Variables to Choices](/how-to-guides/set-up-scoring-quiz/#how-to-add-scores-or-variables-to-choices).

        !!! example

            Question 1: How does your skin feel when you wake up in the morning?

            - Choice 1: Tight (variable `dry skin` +1)
            - Choice 2: Normal (variable `normal skin` +1)
            - Choice 3: Oily (variable `oily skin` +1)
            - Choice 4: Combination (variable `combination skin` +1)
            - Choice 5: Sensitive (variable `sensitive skin` +1)  

            Question 2: How does your skin usually look by midday?

            - Choice 1: Still tight (variable `dry skin` +1)
            - Choice 2: Same as in the morning (variable `normal skin` +1)
            - Choice 3: Shiny (variable `oily skin` +1)
            - Choice 4: T-zone shiny (variable `combination skin` +1)
            - Choice 5: Red and irritated (variable `sensitive skin` +1)

    3. **Add a Results Page and Sections**: Add a [Results Page](/reference/quiz-builder/results-page/) to your quiz. On the Results Page add several **Sections** with Heading, Text and Product Block that shows products for specific skin type and its challenges.

        !!! example

            Section 1: Dry Skin

            Section 2: Normal Skin

            Section 3: Oily Skin

            Section 4: Combination Skin 

            Section 5: Sensitive Skin

    4. **Add a Product Block to Each Section**: Add a [Product Block](/reference/quiz-builder/results-page/#products-products-variants-collections) to each section on your Results Page. In the Product Block settings set the `Recommendation System` to `Fixed Recommendations` and select the products you want to recommend for that skin type.  

    5. **Add Display Logic**: Add a [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) to each section on your Results Page to tell it when to be shown or hidden based on the winning variable.

        !!! example

            - If the variable with the highest score is `dry skin`, then Section 1 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `normal skin`, then Section 2 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `oily skin`, then Section 3 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `combination skin`, then Section 4 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `sensitive skin`, then Section 5 is **visible**. Otherwise Default visibility is **hidden**.

    6. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "Shopify (Legacy)"

    Scoring system is not available in the legacy version of the RevenueHunt app for Shopify. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


    Alternatively, your developer can also try this setup:

    
    ??? question "Do I need advanced technical skills to set this up?"

        While the process isn’t entirely plug-and-play, with the assistance of a developer, it’s manageable. If you’re not familiar with JavaScript or CSS, seeking developer help is advisable.

    **How do I recommend products based on the number of user choices?**

    The recommendation process is based on how many choices the user selects out of the given set. Here’s a step-by-step guide:

    1. **Create collections/categories**. Create distinct collections for each group of products you wish to recommend, e.g., “1/10 choices selected,” “2/10 choices selected,” etc.
    2. **Add hidden choices**. In your final question, include a multiple-choice option that correlates with the aforementioned collections/categories. This ensures that each choice connects to its respective recommended collection/category. Make sure to hide these choices from the user with custom CSS code.
    3. **Add custom JavaScript**. Using custom JavaScript, evaluate the choices selected throughout the quiz and write a piece of code that automatically selects one of the hidden choices in the last question. This will determine which product collection/category to recommend based on the number of choices the user made.

    **How can I ensure that users don’t see the choices in the last question?**

    You can hide these technical choices in the last question using custom CSS code. A guide on how to customize the quiz design can be found [here](/how-to-guides/customize-quiz-design/).

    **Where do I input the custom JavaScript code?**

    [This article](/how-to-guides/add-javascript/) explains how to add custom JavaScript code to quiz questions. For example:

    ![recommend-products-based-on-number-of-user-choices image1](/images/recommend-products-based-on-number-of-user-choices_image1.png){width=500}

    The custom JavaScript code should be integrated into the final question to assess the user’s choices and click the right choices in order to recommend a product collection accordingly.

    **How can I identify the selected choices from each slide or question with JavaScript?**

    To review the values or choice IDs selected for each slide/question, you can use the JavaScript console and search for the values:

    ![recommend-products-based-on-number-of-user-choices image2](/images/recommend-products-based-on-number-of-user-choices_image2.png)




=== "WooCommerce"

    Scoring system is not available in the WooCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    Alternatively, your developer can also try this setup:

    
    ??? question "Do I need advanced technical skills to set this up?"

        While the process isn’t entirely plug-and-play, with the assistance of a developer, it’s manageable. If you’re not familiar with JavaScript or CSS, seeking developer help is advisable.

    **How do I recommend products based on the number of user choices?**

    The recommendation process is based on how many choices the user selects out of the given set. Here’s a step-by-step guide:

    1. **Create collections/categories**. Create distinct collections for each group of products you wish to recommend, e.g., “1/10 choices selected,” “2/10 choices selected,” etc.
    2. **Add hidden choices**. In your final question, include a multiple-choice option that correlates with the aforementioned collections/categories. This ensures that each choice connects to its respective recommended collection/category. Make sure to hide these choices from the user with custom CSS code.
    3. **Add custom JavaScript**. Using custom JavaScript, evaluate the choices selected throughout the quiz and write a piece of code that automatically selects one of the hidden choices in the last question. This will determine which product collection/category to recommend based on the number of choices the user made.

    **How can I ensure that users don’t see the choices in the last question?**

    You can hide these technical choices in the last question using custom CSS code. A guide on how to customize the quiz design can be found [here](/how-to-guides/customize-quiz-design/).

    **Where do I input the custom JavaScript code?**

    [This article](/how-to-guides/add-javascript/) explains how to add custom JavaScript code to quiz questions. For example:

    ![recommend-products-based-on-number-of-user-choices image1](/images/recommend-products-based-on-number-of-user-choices_image1.png){width=500}

    The custom JavaScript code should be integrated into the final question to assess the user’s choices and click the right choices in order to recommend a product collection accordingly.

    **How can I identify the selected choices from each slide or question with JavaScript?**

    To review the values or choice IDs selected for each slide/question, you can use the JavaScript console and search for the values:

    ![recommend-products-based-on-number-of-user-choices image2](/images/recommend-products-based-on-number-of-user-choices_image2.png)     

=== "Magento"

    Scoring system is not available in the Magento version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    Alternatively, your developer can also try this setup:

    
    ??? question "Do I need advanced technical skills to set this up?"

        While the process isn’t entirely plug-and-play, with the assistance of a developer, it’s manageable. If you’re not familiar with JavaScript or CSS, seeking developer help is advisable.

    **How do I recommend products based on the number of user choices?**

    The recommendation process is based on how many choices the user selects out of the given set. Here’s a step-by-step guide:

    1. **Create collections/categories**. Create distinct collections for each group of products you wish to recommend, e.g., “1/10 choices selected,” “2/10 choices selected,” etc.
    2. **Add hidden choices**. In your final question, include a multiple-choice option that correlates with the aforementioned collections/categories. This ensures that each choice connects to its respective recommended collection/category. Make sure to hide these choices from the user with custom CSS code.
    3. **Add custom JavaScript**. Using custom JavaScript, evaluate the choices selected throughout the quiz and write a piece of code that automatically selects one of the hidden choices in the last question. This will determine which product collection/category to recommend based on the number of choices the user made.

    **How can I ensure that users don’t see the choices in the last question?**

    You can hide these technical choices in the last question using custom CSS code. A guide on how to customize the quiz design can be found [here](/how-to-guides/customize-quiz-design/).

    **Where do I input the custom JavaScript code?**

    [This article](/how-to-guides/add-javascript/) explains how to add custom JavaScript code to quiz questions. For example:

    ![recommend-products-based-on-number-of-user-choices image1](/images/recommend-products-based-on-number-of-user-choices_image1.png){width=500}

    The custom JavaScript code should be integrated into the final question to assess the user’s choices and click the right choices in order to recommend a product collection accordingly.

    **How can I identify the selected choices from each slide or question with JavaScript?**

    To review the values or choice IDs selected for each slide/question, you can use the JavaScript console and search for the values:

    ![recommend-products-based-on-number-of-user-choices image2](/images/recommend-products-based-on-number-of-user-choices_image2.png)

=== "BigCommerce"

    Scoring system is not available in the BigCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    Alternatively, your developer can also try this setup:

    
    ??? question "Do I need advanced technical skills to set this up?"

        While the process isn’t entirely plug-and-play, with the assistance of a developer, it’s manageable. If you’re not familiar with JavaScript or CSS, seeking developer help is advisable.

    **How do I recommend products based on the number of user choices?**

    The recommendation process is based on how many choices the user selects out of the given set. Here’s a step-by-step guide:

    1. **Create collections/categories**. Create distinct collections for each group of products you wish to recommend, e.g., “1/10 choices selected,” “2/10 choices selected,” etc.
    2. **Add hidden choices**. In your final question, include a multiple-choice option that correlates with the aforementioned collections/categories. This ensures that each choice connects to its respective recommended collection/category. Make sure to hide these choices from the user with custom CSS code.
    3. **Add custom JavaScript**. Using custom JavaScript, evaluate the choices selected throughout the quiz and write a piece of code that automatically selects one of the hidden choices in the last question. This will determine which product collection/category to recommend based on the number of choices the user made.

    **How can I ensure that users don’t see the choices in the last question?**

    You can hide these technical choices in the last question using custom CSS code. A guide on how to customize the quiz design can be found [here](/how-to-guides/customize-quiz-design/).

    **Where do I input the custom JavaScript code?**

    [This article](/how-to-guides/add-javascript/) explains how to add custom JavaScript code to quiz questions. For example:

    ![recommend-products-based-on-number-of-user-choices image1](/images/recommend-products-based-on-number-of-user-choices_image1.png){width=500}

    The custom JavaScript code should be integrated into the final question to assess the user’s choices and click the right choices in order to recommend a product collection accordingly.

    **How can I identify the selected choices from each slide or question with JavaScript?**

    To review the values or choice IDs selected for each slide/question, you can use the JavaScript console and search for the values:

    ![recommend-products-based-on-number-of-user-choices image2](/images/recommend-products-based-on-number-of-user-choices_image2.png)    

=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    Alternatively, your developer can also try this setup:

    
    ??? question "Do I need advanced technical skills to set this up?"

        While the process isn’t entirely plug-and-play, with the assistance of a developer, it’s manageable. If you’re not familiar with JavaScript or CSS, seeking developer help is advisable.

    **How do I recommend products based on the number of user choices?**

    The recommendation process is based on how many choices the user selects out of the given set. Here’s a step-by-step guide:

    1. **Create collections/categories**. Create distinct collections for each group of products you wish to recommend, e.g., “1/10 choices selected,” “2/10 choices selected,” etc.
    2. **Add hidden choices**. In your final question, include a multiple-choice option that correlates with the aforementioned collections/categories. This ensures that each choice connects to its respective recommended collection/category. Make sure to hide these choices from the user with custom CSS code.
    3. **Add custom JavaScript**. Using custom JavaScript, evaluate the choices selected throughout the quiz and write a piece of code that automatically selects one of the hidden choices in the last question. This will determine which product collection/category to recommend based on the number of choices the user made.

    **How can I ensure that users don’t see the choices in the last question?**

    You can hide these technical choices in the last question using custom CSS code. A guide on how to customize the quiz design can be found [here](/how-to-guides/customize-quiz-design/).

    **Where do I input the custom JavaScript code?**

    [This article](/how-to-guides/add-javascript/) explains how to add custom JavaScript code to quiz questions. For example:

    ![recommend-products-based-on-number-of-user-choices image1](/images/recommend-products-based-on-number-of-user-choices_image1.png){width=500}

    The custom JavaScript code should be integrated into the final question to assess the user’s choices and click the right choices in order to recommend a product collection accordingly.

    **How can I identify the selected choices from each slide or question with JavaScript?**

    To review the values or choice IDs selected for each slide/question, you can use the JavaScript console and search for the values:

    ![recommend-products-based-on-number-of-user-choices image2](/images/recommend-products-based-on-number-of-user-choices_image2.png)


## Scoring Quiz with One Results Page

Assign numerical scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the accumulated scores.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png){width=500}

Follow these steps to set up a scoring quiz with one results page:


=== "Shopify"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/bdfab85a0d3b4ecf9beb264fb2a19299?sid=6742d6dc-e3e5-4a3b-a7de-bbd1381170c1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip

        We have Scoring Quiz template avialble among the Quiz Templates. To use it go to the [Dashboard]/(reference/dashboard/) and click on `Create Quiz` button. Then, select `Scoring Quiz` template.

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. For example: age, skin type, enviornemnet etc. if you are creating a quiz for a skin care brand.

    2. **Assign Scores to Choices**: Go to each question in your quiz. For each choice, open the choice settings and [assign appropriate point values to each choice](/how-to-guides/set-up-scoring-quiz/#how-to-add-scores-or-variables-to-choices) via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings) section. 

        ![assigning scores to choices](/images/how_to_shopifyv2_scoringquiz_addscore.png)

        !!! tip

            To learn how to add scores or variables to choices, check out this guide: [How to Add Scores or Variables to Choices](/how-to-guides/set-up-scoring-quiz/#how-to-add-scores-or-variables-to-choices).

        !!! example

            For example, with skin type questions:

            - Dry skin choices: 1 point
            - Normal skin choices: 2 points
            - Oily skin choices: 3 points
            - Combination skin choices: 4 points
            - Sensitive skin choices: 5 points

    2. **Add Content Sections to Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) and add a new `sections`. To add a new section click the `+ Add section` sign. 
    
        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        To each block add a `Product Block` with the products you want to recommend for that skin type. Make sure to set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).  

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png)
            
    3. **Add Score-Based Display Logic**: On the Results Page, select a content block and in the right-hand menu locate `Display logic`.
        
        - Click on `+ Add condition (OR)`
        - Instead of using question-specific conditions, use the `The varaible with the highest score...` or `The score of the varaible...` option
        - Set up range conditions to control when each content block should be visible/hidden.

        ![score-based display logic](/images/how_to_shopifyv2_scoringquiz_displaylogic.png)

        !!! example

            For example:

            - Dry skin content: Total score is between 5-7 points
            - Normal skin content: Total score is between 8-12 points
            - Oily skin content: Total score is between 13-17 points
            - Combination skin content: Total score is between 18-22 points
            - Sensitive skin content: Total score is between 23-25 points

    5. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "Shopify (Legacy)"

    Scoring system is not available in the legacy version of the RevenueHunt app for Shopify. Your developer can implement a custom scoring system with JavaScript on the Results Page instead.    
    
    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "WooCommerce"

    Scoring system is not available in the RevenueHunt app for WooCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Magento"

    Scoring system is not available in the RevenueHunt app for Magento. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "BigCommerce"

    Scoring system is not available in the RevenueHunt app for BigCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


## Scoring Quiz with Multiple Results Pages

Assign numerical scores to each choice in your quiz. Then, use Jump Logic to direct customers to different results pages based on their accumulated scores. 

![how_to_shopify_v2_recommendations_scoring_logic](/images/how_to_shopify_v2_recommendations_scoring_logic.png){width=500}

Follow these steps to set up a scoring quiz with multiple results pages:


=== "Shopify"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/a6aa2b811b6f4adc87f986f0441d6328?sid=f4329a4f-b169-46b6-9a66-2c66644577b8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. For example: age, skin type, enviornemnet etc. if you are creating a quiz for a skin care brand.

    2. **Assign Scores to Choices**: Go to each question in your quiz. For each choice, open the choice settings and [assign appropriate point values to each choice](/how-to-guides/set-up-scoring-quiz/#how-to-add-scores-or-variables-to-choices) via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings) section. 

        !!! tip

            To learn how to add scores or variables to choices, check out this guide: [How to Add Scores or Variables to Choices](/how-to-guides/set-up-scoring-quiz/#how-to-add-scores-or-variables-to-choices).

        ![assigning scores to choices](/images/how_to_shopifyv2_scoringquiz_addscore.png)

        !!! example

            For example, with skin type questions:

            - Dry skin choices: 1 point
            - Normal skin choices: 2 points
            - Oily skin choices: 3 points
            - Combination skin choices: 4 points
            - Sensitive skin choices: 5 points

    3. **Create Multiple Results Pages**: Go to the [Results Page](/reference/quiz-builder/results-page/) section and click `+ Add Results Page` to create additional results pages. Create one results page for each possible outcome.

        ![how_to_shopifyv2_scoringquiz_multiresultspages](/images/how_to_shopifyv2_scoringquiz_multiresultspages.png)

        !!! example

            For example:

            - Results Page 1: Dry Skin Routine
            - Results Page 2: Normal Skin Routine
            - Results Page 3: Oily Skin Routine
            - Results Page 4: Combination Skin Routine
            - Results Page 5: Sensitive Skin Routine

    3. **Add Content to Each Results Page**: For each results page, addustom text describing the specific skin type and its challenges, product recommendations for that skin type and any additional content blocks relevant to that skin type.

        To each results page add a section with content describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        Make sure to add product blocks to each results page and set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png) 

    4. **Set Up Jump Logic Based on Scores**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) section of Quiz Builder. Find the last question in your quiz and open the [Jump Logic settings](/reference/quiz-builder/conditional-logic/#jump-logic):
        
        - Click on `+ Add condition (OR)`
        - Select `The variable with the highest score...` or `The score of the variable...` option
        - Set up range conditions to control which results page the user will be directed to

        ![how_to_shopifyv2_scoringquiz_multiresultspages_logic](/images/how_to_shopifyv2_scoringquiz_multiresultspages_logic.png)

        !!! example

            For example:

            - If total score is between 5-7 points → Jump to Dry Skin Routine
            - If total score is between 8-12 points → Jump to Normal Skin Routine
            - If total score is between 13-17 points → Jump to Oily Skin Routine
            - If total score is between 18-22 points → Jump to Combination Skin Routine
            - If total score is between 23-25 points → Jump to Sensitive Skin Routine

    5. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "Shopify (Legacy)"

    Scoring system is not available in the legacy version of the RevenueHunt app for Shopify. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "WooCommerce"

    Scoring system is not available in the WooCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Magento"

    Scoring system is not available in the Magento version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "BigCommerce"

    Scoring system is not available in the BigCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. 

    !!! tip 
        Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).



---

This article explains how to set up a scoring quiz with one results page and multiple results pages in the RevenueHunt app.