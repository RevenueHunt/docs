# How to Set Up Scoring Quiz


## Winning Variable Quiz 

<div style="position: relative; padding-bottom: 74.27785419532324%; height: 0;"><iframe src="https://www.loom.com/embed/7b44356b9eba4fb3a24b6e595fd48088?sid=f5da200d-6189-457b-8a99-24395da4df8a" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Assign variables and scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the most voted varaible.

![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_varaiblequiz.png)

Follow these steps to set up a winning variable quiz:       

=== "Shopify"

    Scoring system is not available in the legacy version of the Shopify app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Shopify V2"

    Let's imagine you are creating a quiz for a skin care brand. You want to know which skin type the customer has.

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their skin condition. For example: itchiness, tightness, dryness, etc. if you are creating a quiz for a skin care brand.

    2. **Assign Variables and Scores to Choices**: Go to each question in your quiz. For each choice, open the [choice settings](/reference/quiz-builderchoice-settings/) and assign varibales to each choice. 

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

    4. **Add a Product Block to Each Section**: Add a [Product Block](/reference/quiz-builder/product-block/) to each section on your Results Page. In the Product Block settings set the `Recommendation System` to `Fixed Recommendations` and select the products you want to recommend for that skin type.  

    5. **Add Display Logic**: Add a [Display Logic](/reference/quiz-builder/display-logic/) to each section on your Results Page to tell it when to be shown or hidden based on the winning variable.

        !!! example

            - If the variable with the highest score is `dry skin`, then Section 1 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `normal skin`, then Section 2 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `oily skin`, then Section 3 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `combination skin`, then Section 4 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `sensitive skin`, then Section 5 is **visible**. Otherwise Default visibility is **hidden**.

    6. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    Scoring system is not available in WooCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).         

=== "Magento"

    Scoring system is not available in Magento. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    Scoring system is not available in BigCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).     

=== "Standalone"

    Scoring system is not available in Standalone. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).  


## One Results Page

Assign numerical scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the accumulated scores.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png)

Follow these steps to set up a scoring quiz with one results page:


=== "Shopify"

    Scoring system is not available in the legacy version of the Shopify app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Shopify V2"

    !!! tip

        We have Scoring Quiz template avialble among the Quiz Templates. To use it go to the [Dashboard]/(reference/dashboard/) and click on `Create Quiz` button. Then, select `Scoring Quiz` template.

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. For example: age, skin type, enviornemnet etc. if you are creating a quiz for a skin care brand.

    2. **Assign Scores to Choices**: Go to each question in your quiz. For each choice, open the choice settings and assign appropriate point values to each choice via the [Choice Settings](/reference/quiz-builderchoice-settings/) section. 

        ![assigning scores to choices](/images/how_to_shopifyv2_scoringquiz_addscore.png)

        !!! example

            For example, with skin type questions:

            - Dry skin choices: 1 point
            - Normal skin choices: 2 points
            - Oily skin choices: 3 points
            - Combination skin choices: 4 points
            - Sensitive skin choices: 5 points

    2. **Add Content Sections to Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) and add a new `sections`. To add a new section click the `+ Add section` sign. 
    
        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_block_logic_sections.png)

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

=== "WooCommerce"

    Scoring system is not available in WooCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Magento"

    Scoring system is not available in Magento. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    Scoring system is not available in BigCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    Scoring system is not available in Standalone. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

## Multiple Results Pages

Assign numerical scores to each choice in your quiz. Then, use Jump Logic to direct customers to different results pages based on their accumulated scores. 

![how_to_shopify_v2_recommendations_scoring_logic](/images/how_to_shopify_v2_recommendations_scoring_logic.png)

Follow these steps to set up a scoring quiz with multiple results pages:


=== "Shopify"

    Scoring system is not available in the legacy version of the Shopify app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. For example: age, skin type, enviornemnet etc. if you are creating a quiz for a skin care brand.

    2. **Assign Scores to Choices**: Go to each question in your quiz. For each choice, open the choice settings and assign appropriate point values to each choice via the [Choice Settings](/reference/quiz-builderchoice-settings/) section. 

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

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_block_logic_sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        Make sure to add product blocks to each results page and set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png) 

    4. **Set Up Jump Logic Based on Scores**: Go tp the [Conditional Logic](/reference/quiz-builder/conditional-logic/) section of Quiz Builder. Find the last question in your quiz and open the [Jump Logic settings](/reference/quiz-builder/conditional-logic/#jump-logic):
        
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

=== "WooCommerce"

    Scoring system is not available in WooCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Magento"

    Scoring system is not available in Magento. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    Scoring system is not available in BigCommerce. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    Scoring system is not available in Standalone. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).



---

This article explains how to set up a scoring quiz with one results page and multiple results pages in the RevenueHunt app.