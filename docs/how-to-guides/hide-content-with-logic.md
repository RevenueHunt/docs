---
icon: material/eye-off
---

# How to Show or Hide Content Based on Quiz Answers

In this article, you’ll discover how to use `IF-THEN` conditional logic to display customized text to quiz takers. This includes adding custom text within your quiz using [Jump Logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/), displaying custom text on the Results page with [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/), and achieving similar effects with [Skip Logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/).

Using a skincare routine quiz as an example, we'll show how custom text is displayed based on the customer’s skin type.

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Jump Logic: How to Show Custom Text in the Quiz

=== "Shopify"

    ![how to hide content with logic jump logic](/images/how to hide content with logic jump logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how to hide content with logic jump logic statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"


    !!! warning

        Version 2 of the Shop Quiz: Product Recommender app is not yet available. It is currently in the beta testing phase. Learn more [here](https://docs.revenuehunt.com/customer-success/shopify-v2-beta/).

    ![how to hide content with logic jump logic](/images/how to hide content with logic shopifyv2 jump logic flow.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. 
    
        To add jump logic, you should to the [conditional logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab and select the Skin type question. 
    
        Then, Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.  Like this:

        ![how to hide content with logic jump logic statement](/images/how to hide content with logic shopifyv2 jump logic rule.png)

        Click `+Add another rule (OR)` to add similar Jump Logic rules to direct the user to the Dry, Normal and Combination-Type skin respectively.

        This will ensure that each answer from the Skin Type question will lead tio the right statement.

    4. **Add Default destination Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. 
    
        This is done by going to the [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) tab and scrolling toward the `Default destination` section. Point each statement to the next question.

        ![how to hide content with logic shopifyv2 jump logic default destination](/images/how to hide content with logic shopifyv2 jump logic default destination.png)

    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    ![how to hide content with logic jump logic](/images/how to hide content with logic jump logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how to hide content with logic jump logic statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    ![how to hide content with logic jump logic](/images/how to hide content with logic jump logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how to hide content with logic jump logic statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    ![how to hide content with logic jump logic](/images/how to hide content with logic jump logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how to hide content with logic jump logic statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    ![how to hide content with logic jump logic](/images/how to hide content with logic jump logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: If we don’t add jump logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add jump logic, you should go back to the skin type question and select [conditional logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type. 

        ![how to hide content with logic jump logic statement](/images/how to hide content with logic jump logic statement.png)

    4. **Add "Always Jump to..." Logic**: Once all the statements are linked with logic to the skin type question, you should point each statement to the next question in the quiz. This is done by going to the [jump logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Block Logic: How to Show Custom Text on the Results Page

=== "Shopify"

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](https://docs.revenuehunt.com/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how to hide content with logic block logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.


=== "Shopify V2"


    !!! warning

        Version 2 of the Shop Quiz: Product Recommender app is not yet available. It is currently in the beta testing phase. Learn more [here](https://docs.revenuehunt.com/customer-success/shopify-v2-beta/).

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) to help customers determine their skin type.

    2. **Add Content Sections to Results Page**: Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) and add a new `sections`. To add a new section click the `+ Add section` sign. 
    
        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 block logic sections](/images/how to hide content with logic shopifyv2 block logic sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

    3. **Add Display Logic**: If we don’t add [Display Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. 
    
        To add Display Logic, select a content block and in the right-hand menu locate `Display logic`. Click on `+ Add consition (OR)`. 
        
        Set up IF-THEN statements to control when each statement block should be visible or hidden based on the customer's choices. Like this:

        ![how to hide content with logic block logic statement](/images/how to hide content with logic shopifyv2 block logic rule.png)


    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](https://docs.revenuehunt.com/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how to hide content with logic block logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.


=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](https://docs.revenuehunt.com/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how to hide content with logic block logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.


=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](https://docs.revenuehunt.com/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how to hide content with logic block logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](https://docs.revenuehunt.com/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how to hide content with logic block logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Skip Logic: How to Show Custom Text in the Quiz

=== "Shopify"

    ![how to hide content with logic skip logic](/images/how to hide content with logic skip logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how to hide content with logic skip logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"


    !!! warning

        Version 2 of the Shop Quiz: Product Recommender app is not yet available. It is currently in the beta testing phase. Learn more [here](https://docs.revenuehunt.com/customer-success/shopify-v2-beta/).

    ![how to hide content with logic skip logic](/images/how to hide content with logic shopifyv2 skip logic flow.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. 
    
        To add [skip logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), you should go the [Conditional Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab and select the quesiton that should be skipped.  
    
        Next, in the right-hand menu locte the `Skip Logic` section.
    
        Click `+ Add another rule (OR)` to add a skip logic rule to the selected statement slide. 

        For example:

        ![how to hide content with logic shopifyv2 skip logic rule](/images/how to hide content with logic shopifyv2 skip logic rule.png)

        If the response for Question 4 **is not** "Dry and tight all over" then this question will be skipped. Meaning that if any other answer than "Dry and thight all over" is selected, then this question will be skipped.
    
        Use similar skip logic rules on the other statements to ensure that only relevant statement questions appear based on the customer's skin type selection.

    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    ![how to hide content with logic skip logic](/images/how to hide content with logic skip logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how to hide content with logic skip logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    ![how to hide content with logic skip logic](/images/how to hide content with logic skip logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how to hide content with logic skip logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.


=== "BigCommerce"

    ![how to hide content with logic skip logic](/images/how to hide content with logic skip logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how to hide content with logic skip logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    ![how to hide content with logic skip logic](/images/how to hide content with logic skip logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


    3. **Add Skip Logic**: If we don’t add skip logic to the quiz, our statement questions will just appear one after the other, regardless of the choice we made. To add [skip logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), you should go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how to hide content with logic skip logic statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.



---
For more detailed instructions on using [Jump Logic](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/), [Block Logic](https://docs.revenuehunt.com/how-to-guides/use-block-logic/), and [Skip Logic](https://docs.revenuehunt.com/how-to-guides/use-skip-logic/), consider checking the respective articles linked throughout this guide.
