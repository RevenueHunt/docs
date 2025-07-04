# How to Set Up Fixed Recommendations Quiz

Recommended for quizzes with complex branching. Set up fixed sections with pre-determined products to be shown on the results page. Then add logic to control visibility of each section or results page.

Use this method for: 

- Quizzes with multiple very precise outcomes and product recommendations
- Quizzes with complex branching
- Quizzes that require a lot of logic conditions 

!!! info "Benefits"

    - Good for complex branching quizzes with multiple very precise outcomes and product recommendations.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png){width=300px;}

## One Results Page 

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/316e4dcc9db14812a76ace51e85b6fe5?sid=cdb69306-37dd-4331-8e76-aeb763351f12" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

**Option 1:** Set up multiple sections on the results page with fixed product and text combinations, then control visibility of each section with Display Logic display rules.

![docs/images/how_to_shopify_v2_recommendations_displaylogic.png](/images/how_to_shopify_v2_recommendations_displaylogic.png)



=== "Shopify"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: If we don’t add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Display Logic, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Add Content Sections to Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) and add a new `sections`. To add a new section click the `+ Add section` sign. 
    
        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_shopifyv2_fixedrecommendationquiz_sectionsresultspage.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Product Blocks**: To each block add a `Product Block` with the products you want to recommend for that skin type. Make sure to set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).  

        ![how to recommend products fixed recommendations resultspage](/images/how_to_shopifyv2_fixedrecommendationquiz_fixedrecommendationsresultspage.png)

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png)         

        Then, select the max. number of products to show in the `Slot` settings and select which products to show.

        ![how to recommend products fixed recommendations resultspage2](/images/how_to_shopifyv2_fixedrecommendationquiz_fixedrecommendationsresultspage2.png)
            

    3. **Add Display Logic**: If we don't add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. 
    
        To add Display Logic, select a content block and in the right-hand menu locate `Display logic`. Click on `+ Add condition (OR)`. 
              
        Set up IF-THEN statements to control when each statement block should be visible or hidden based on the customer's choices. Like this:

        ![how to hide content with logic display logic statement](/images/how_to_shopifyv2_fixedrecommendationquiz_displaylogic.png)

    5. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: If we don’t add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Display Logic, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: If we don’t add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Display Logic, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: If we don’t add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Display Logic, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: If we don’t add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Display Logic, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Multiple Results Pages 

**Option 2:** Set up multiple results pages with unique fixed product recommendations and texts and control visbility by adding branching with Jump Logic that leads to diferent results pages.	

!!! note

    The difference between this method and the previous one is that in this method you set up multiple results pages and control visbility by adding branching with Jump Logic that leads to diferent results pages while the previous method is a single results page with multiple content + product blocks controlled by Display Logic. 
    
    Overall, both methods are the same, the difference is only in where you add the conditonal logic (Display Logic vs Jump Logic).

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png)

=== "Shopify"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Result Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.    

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges and a Product Block. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: Use Jump Logic to branch your quiz and **link the recommended produsts to the choices in the last question on each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their choices.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+ Add Results Page` button to create additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:+

        ![how to set up multiple results pages](/images/how_to_shopifyv2_fixedrecommendationquiz_resultpages.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Products Block` with the specific products you want to recommend for that skin type.

        To each block add a `Product Block` with the products you want to recommend for that skin type. Make sure to set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).  +

        ![how to recommend products fixed recommendations resultspage](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_fixedrecommendationsresultspage.png)

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png)     

        Then go to Slot settings and select the max. number of products to show and select which products to show.

        ![how to recommend products fixed recommendations resultspage2](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_fixedrecommendationsresultspage2.png)


    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and pick the last question in the quiz. Set up [Jump Logic](/how-to-guides/hide-content-with-logic/#jump-logic-how-to-show-custom-text-in-the-quiz) to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_jumplogic.png)

        Open the Jump Logic options and add new rules to this question. Click `+ Add another rule (OR)` to add a new OR Jump Logic rule for the selected question.


        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_example](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_jumplogic_example.png)

            In the example, if a user chooses a choice "Not too oily..." in Question 4 "SKIN TYPE" then they will be redirected to Results Page 2.

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Result Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.    

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges and a Product Block. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: Use Jump Logic to branch your quiz and **link the recommended produsts to the choices in the last question on each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their choices.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Result Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.    

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges and a Product Block. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: Use Jump Logic to branch your quiz and **link the recommended produsts to the choices in the last question on each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their choices.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Result Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.    

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges and a Product Block. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: Use Jump Logic to branch your quiz and **link the recommended produsts to the choices in the last question on each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their choices.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Result Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.    

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges and a Product Block. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: Use Jump Logic to branch your quiz and **link the recommended produsts to the choices in the last question on each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their choices.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

