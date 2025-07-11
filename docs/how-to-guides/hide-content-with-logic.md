---
icon: material/eye-off
---

# How to Show or Hide Content Based on Quiz Answers

In this article, you’ll discover how to use `IF-THEN` conditional logic to display customized text to quiz takers. This includes adding custom text within your quiz using [Jump Logic](/how-to-guides/use-jump-logic/), displaying custom text on the Results page with [Display Logic](/how-to-guides/use-display-logic/), and achieving similar effects with [Skip Logic](/how-to-guides/use-skip-logic/).

Using a skincare routine quiz as an example, we'll show how custom text is displayed based on the customer’s skin type.

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Shopify V2"


=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


## Jump Logic: How to Show Custom Text in the Quiz

=== "Shopify"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/33942abdef344d19a6e95b478c3f1e8a?sid=16f14cfc-9a54-4eb3-8a90-9ac6e8729195" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. 
    
        To add jump logic, you should to the [conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the Skin type question. 
    
        Then, Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.  Like this:

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_rule.png)

        Click `+Add another rule (OR)` to add similar Jump Logic rules to direct the user to the Dry, Normal and Combination-Type skin respectively.

        This will ensure that each answer from the Skin Type question will lead tio the right statement.

    4. **Add Default destination Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. 
    
        This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Default destination` section. Point each statement to the next question.

        ![how to hide content with logic shopifyv2 jump logic default destination](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_default_destination.png)

    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Display Logic: How to Show Custom Text on the Results Page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

    

    3. **Add Display Logic**: If we don't add [Display Logic](/how-to-guides/use-display-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. 

        !!! info "*➡️ Method 1: Using Answer-Based Display Logic"
    
            To add Display Logic, select a content block and in the right-hand menu locate `Display logic`. Click on `+ Add consition (OR)`. 
            
            Set up IF-THEN statements to control when each statement block should be visible or hidden based on the customer's choices. Like this:

            ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_rule.png)

        

        !!! info "➡️ Method 2: Using Score-Based Display Logic"

            **Assign Scores to Choices**: Shopify V2 offers an alternative method using a scoring system to personalize results.
        
            - Go to each question in your quiz
            - For each choice, open the choice settings
            - Assign appropriate point values to each choice

            !!! example

                For example, with skin type questions:
                - Dry skin choices: 1 point
                - Normal skin choices: 2 points
                - Oily skin choices: 3 points
                - Combination skin choices: 4 points
                - Sensitive skin choices: 5 points

            ![assigning scores to choices](/images/how_to_hide_content_with_logic_shopifyv2_scoring.png)

            **Add Score-Based Display Logic**: On the Results Page, select a content block and in the right-hand menu locate `Display logic`.
        
            - Click on `+ Add condition (OR)`
            - Instead of using question-specific conditions, use the `The varaible with the highest score...` or `The score of the varaible...` option
            - Set up range conditions to control when each content block should be visible/hidden.

            !!! example

                For example:
                - Dry skin content: Total score is between 5-7 points
                - Normal skin content: Total score is between 8-12 points
                - Oily skin content: Total score is between 13-17 points
                - Combination skin content: Total score is between 18-22 points
                - Sensitive skin content: Total score is between 23-25 points

            ![score-based display logic](/images/how_to_hide_content_with_logic_shopifyv2_score_logic.png)

    5. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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

## Skip Logic: How to Show Custom Text in the Quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/974fa05168164ed691522e5ced0f36d1?sid=0609fcf4-60c9-4098-86cb-6503c343f73c" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. 
    
        To add [skip logic](/how-to-guides/use-skip-logic/), you should go the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the quesiton that should be skipped.  
    
        Next, in the right-hand menu locte the `Skip Logic` section.
    
        Click `+ Add another rule (OR)` to add a skip logic rule to the selected statement slide. 

        For example:

        ![how to hide content with logic shopifyv2 skip logic rule](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_rule.png)

        If the response for Question 4 **is not** "Dry and tight all over" then this question will be skipped. Meaning that if any other answer than "Dry and thight all over" is selected, then this question will be skipped.
    
        Use similar skip logic rules on the other statements to ensure that only relevant statement questions appear based on the customer's skin type selection.

    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

---
For more detailed instructions on using [Jump Logic](/how-to-guides/use-jump-logic/), [Display Logic](/how-to-guides/use-display-logic/), and [Skip Logic](/how-to-guides/use-skip-logic/), consider checking the respective articles linked throughout this guide.
