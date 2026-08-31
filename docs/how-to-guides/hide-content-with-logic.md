---
description: "Learn how to use conditional logic to show or hide content in your RevenueHunt quiz based on customer answers and responses."
icon: material/eye-off
---

# How to Show or Hide Content Based on Quiz Answers

This article explains how to use `IF-THEN` conditional logic to show or hide a question or a section, based on what the customer answered. That covers hiding a question or a statement in the quiz using [Jump Logic](/how-to-guides/use-jump-logic/) or [Skip Logic](/how-to-guides/use-skip-logic/) and showing or hiding blocks/sections on the Results page with [Display Logic](/how-to-guides/use-display-logic/).

The examples use a skincare routine quiz, and show custom text and results chosen by the customer’s skin type.

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/s71v8NfNRWk?si=c-8mefpQoHOvppvX" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

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


## Jump logic: how to show custom text in the quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/N2gudKAy4qU?si=hcgIntH-XecaQxua" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)

    1. **Create Quiz**: Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump logic**: Without jump logic, the statement questions appear one after the other, whatever the customer picked.

        To add jump logic, you should to the [conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the Skin type question.

        Then, Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.  Like this:

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_rule.png)

        Click `+Add another rule (OR)` to add similar Jump logic rules to direct the user to the Dry, Normal and Combination-Type skin respectively.

        Each answer to the Skin Type question then leads to the right statement.

    4. **Add Default destination Logic**: With every statement linked to the skin type question, point each one at the next question.

        This is done by going to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Default destination` section. Point each statement to the next question.

        ![how to hide content with logic shopifyv2 jump logic default destination](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_default_destination.png)

    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "Shopify (Legacy)"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: Without jump logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Point each statement at the next question. Go to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: Without jump logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Point each statement at the next question. Go to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: Without jump logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Point each statement at the next question. Go to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: Without jump logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Point each statement at the next question. Go to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Jump Logic**: Without jump logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select [conditional logic](/reference/quiz-builder/conditional-logic/). Set up `IF-THEN` statements with `OR` logic to direct the customer to the correct text based on their skin type.

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    4. **Add "Always Jump to..." Logic**: Point each statement at the next question. Go to the [jump logic](/how-to-guides/use-jump-logic/) tab and scrolling toward the `Always jump to...` section. Point each statement to the next question.

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Display logic: how to show custom text on the results page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=h7Ortp7mpm1wzTHu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Add Content Sections to Results page**: Go to the [Results page](/reference/quiz-builder/results-page/) and add a new `sections`. To add a new section click the `+ Add section` sign.

        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.




    3. **Add Display logic**: Without [Display logic](/how-to-guides/use-display-logic/), the blocks appear one after the other on the Results page, whatever the customer picked.

        ---

        **Display logic operators**

        `+ Add condition (OR)` - Adds a new OR display logic rule.

        `+ Add condtion (AND)` - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

        `bin` - Delete the current Logic rule.

        `+ Add condition (OR)` - Adds another Display logic rule. Adds a new OR logical rule.

        `Default` - Select whether this section should be `Shown` or `Hidden` by default.

        ---

        There are three types of Display logic rules you can choose from:

        ---

        **Type 1: IF The response to the question...**

        Then the Display logic rules follow the following format:

        - **IF response to** pick the question from a dropdown list
        - **is**/ **is not** pick a choice from the dropdown list
        - **THEN section is Visible**
        - **Default visibility** pick either **Visible** or **Hidden**. If Visible is selected, then section will be shown by default unless the Display logic rule is triggered. If Hidden is selected, the section will be hidden by default unless the Display logic rule is triggered.

        !!! example "Example 1"

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

            In the example, if a user chooses a choice "Oily all over" in Question 4 "SKIN TYPE" then this section will be visible. If they give a different answer in Question 4 this content block will be hidden.

        ---

        **Type 2: IF The score of the variable...**

        Then the Display logic rules follow the following format:

        - **IF The score of the variable**
        - **score** pick the variable from a dropdown list
        - The comparison, picked from the dropdown list:
            - **is equal to**
            - **is not equal to**
            - **is greater than**
            - **is less than**
            - **is greater than or equal to**
            - **is less than or equal to**
        - **Number** / **Another variable** pick a choice from the dropdown list
        - **0** / **1** / **2** / **other numerical value** type a value in the input field
        - **THEN section is Visible**
        - **Default visibility** pick either **Visible** or **Hidden**. If Visible is selected, then section will be shown by default unless the Display logic rule is triggered. If Hidden is selected, the section will be hidden by default unless the Display logic rule is triggered.


        !!! info

            Note: Scores are assigned to each choice in the [Questions](/reference/quiz-builder/questions) tab > [Choice settings](/reference/quiz-builder/questions/#choice-settings) section.


        !!! example "Example 2"

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_scorerange](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_scorerange.png)

            In the example, if the score of the variable `dry` is greater than or equal to number `5` AND IF the score of the variable `dry` is less than or equal to number `7` then this section will be visible. Otherwise, the section will be hidden.

        ---

        **Type 3: IF the variable with the highest score...**

        Then the Display logic rules follow the following format:

        - **IF the variable with the highest score**
        - **score** pick the variable from a dropdown list
        - **THEN section is Visible**
        - **Default visibility** pick either **Visible** or **Hidden**. If Visible is selected, then section will be shown by default unless the Display logic rule is triggered. If Hidden is selected, the section will be hidden by default unless the Display logic rule is triggered.

        !!! info

            Note: Scores are assigned to each choice in the [Questions](/reference/quiz-builder/questions) tab > [Choice settings](/reference/quiz-builder/questions/#choice-settings) section.


        !!! example "Example 3"

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_winningvariable](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_winningvariable.png)

            In the example, if the variable with the highest score is `dry` then this section will be visible. Otherwise, the section will be hidden.

    5. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz. Test the quiz by clicking the `Preview` button and selecting different answers and checking if the correct content blocks are displayed.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: Without [Display Logic](/how-to-guides/use-display-logic/), the blocks appear one after the other on the Results Page, whatever the customer picked. To add it, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: Without [Display Logic](/how-to-guides/use-display-logic/), the blocks appear one after the other on the Results Page, whatever the customer picked. To add it, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: Without [Display Logic](/how-to-guides/use-display-logic/), the blocks appear one after the other on the Results Page, whatever the customer picked. To add it, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: Without [Display Logic](/how-to-guides/use-display-logic/), the blocks appear one after the other on the Results Page, whatever the customer picked. To add it, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Display Logic**: Without [Display Logic](/how-to-guides/use-display-logic/), the blocks appear one after the other on the Results Page, whatever the customer picked. To add it, select a content block and click on `display logic`. Next, click `add display logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

## Skip logic: how to show custom text in the quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=iMGaCLXqTpr8yS0B" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

    1. **Create Quiz**: Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip logic**: Without skip logic, the statement questions appear one after the other, whatever the customer picked.

        To add [skip logic](/how-to-guides/use-skip-logic/), go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the question that should be skipped.

        In the right-hand menu, find the `Skip logic` section.

        Click `+ Add another rule (OR)` to add a skip logic rule to the selected statement slide.

        For example:

        ![how to hide content with logic shopifyv2 skip logic rule](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_rule.png)

        If the answer to Question 4 **is not** "Dry and tight all over", this question is skipped. Any other answer skips it.

        Use similar skip logic rules on the other statements to ensure that only relevant statement questions appear based on the customer's skin type selection.

    4. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: Without skip logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: Without skip logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: Without skip logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: Without skip logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Statement Questions**: Add multiple `Statement` slides describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: Itchiness, tightness and dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced. It has no major issues, and it wants a routine that keeps that natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Skip Logic**: Without skip logic, the statement questions appear one after the other, whatever the customer picked. To add it, go back to the skin type question and select `conditional logic`. Next, you should navigate to the `Skip Logic` section and add a skip logic rule to each statement. Use skip logic to ensure that only relevant statement questions appear based on the customer's skin type selection.

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

---
For more detailed instructions on using [Jump Logic](/how-to-guides/use-jump-logic/), [Display Logic](/how-to-guides/use-display-logic/), and [Skip Logic](/how-to-guides/use-skip-logic/), consider checking the respective articles linked throughout this guide.

This article explains how to use Jump Logic, Skip Logic or Display Logic to hide/show content in the quiz based on customer     answers.
