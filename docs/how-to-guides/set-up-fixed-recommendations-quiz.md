# How to Set Up Fixed Recommendations Quiz

Recommended for quizzes with complex branching. Set up fixed sections with pre-determined products to be shown on the results page. Then add logic to control visibility of each section or results page.

!!! info "Benefits"

    - Good for complex branching quizzes with multiple very precise outcomes and product recommendations.

## One Results Page 

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/a83d8d15f00a4bfb9adf5f76aeadee83?sid=823442a4-3bb0-412a-8fe6-30ee138c17b2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

**Option 1:** Set up multiple sections on the results page with fixed product and text combinations, then control visibility of each section with Block Logic display rules.

![docs/images/how_to_shopify_v2_recommendations_blocklogic.png](/images/how_to_shopify_v2_recommendations_blocklogic.png)



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

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Add Content Sections to Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) and add a new `sections`. To add a new section click the `+ Add section` sign. 
    
        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 block logic sections](/images/how_to_hide_content_with_logic_shopifyv2_block_logic_sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        To each block add a `Product Block` with the products you want to recommend for that skin type. Make sure to set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).  

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png)         
            

    3. **Add Display Logic**: If we don't add [Display Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. 
    
        To add Display Logic, select a content block and in the right-hand menu locate `Display logic`. Click on `+ Add consition (OR)`. 
              
        Set up IF-THEN statements to control when each statement block should be visible or hidden based on the customer's choices. Like this:

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_shopifyv2_block_logic_rule.png)

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

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

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

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

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

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

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

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Multiple Results Pages 

**Option 2:** Set up multiple results pages with unique fixed product recommendations and texts and control visbility by adding branching with Jump Logic that leads to diferent resutls pages.	

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png)

=== "Shopify"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+ Add Results Page` button to create additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Products Block` with the specific products you want to recommend for that skin type.

        To each block add a `Product Block` with the products you want to recommend for that skin type. Make sure to set the `Recommendation System` to `Fixed Recommendations` in the [Product Block Settings](/reference/quiz-builder/results-page/#products-products-variants-collections).  

        ![how_to_shopifyv2_scoringquiz_fixedrecommendations](/images/how_to_shopifyv2_scoringquiz_fixedrecommendations.png)     


    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up [Jump Logic](/how-to-guides/hide-content-with-logic/#jump-logic-how-to-show-custom-text-in-the-quiz) to direct customers to the appropriate results page based on their skin type choice.

        Open the Jump Logic options and add new rules to this question. Click `+ Add another rule (OR)` to add a new OR Jump Logic rule for the selected question.

        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_example](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_example.png)

            In the example, if a user chooses a choice "Oily all over" in Question 4 "SKIN TYPE" then they will be redirected to Question 8 "SKIN TYPE: OILY".

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

