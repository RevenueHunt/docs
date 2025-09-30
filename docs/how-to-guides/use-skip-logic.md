# How to Use Skip Logic

[Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) is a tool used in quizzes or surveys to make answering questions smoother for people taking them. It works by changing the order of questions based on the answers given to previous questions. This means if someone answers a question a certain way, they might skip some questions or see different ones next. 

!!! info "Use Skip Logic to:"

    - Skip questions based on the user's answers.
    - Show different follow-up questions based on the user's answers to multiple-choice questions that allow multiple selections. For example, if you want to show different follow-up questions based on the (skin, health) concerns the user selects.


In this article, we will show you how to set up and use Skip Logic in your quiz, including specific use-cases and step-by-step instructions.

=== "Shopify (Legacy)"   

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=iMGaCLXqTpr8yS0B" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce"

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "Magento"

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "BigCommerce"

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "Standalone"

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

??? question "What's Skip Logic?"

    Skip Logic uses IF-AND statements to determine if a question should be skipped based on the user's answers.


!!! warning

    It is advised not to mix [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) and [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) in one quiz. Mixing logic rules can lead to unexpected results.


## Conditional Logic

=== "Shopify (Legacy)"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    In the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab you can branch your quiz. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

    By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

    ??? question "How to navigate the Conditional Logic tab?"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        **+** - Zoom in on the logic tree preview.

        **-** - Zoom out on the logic tree preview.

        **[]** - Center the logic tree preview and fit into view.

        Drag the logic tree with your mouse left button to navigate to specific branches.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The top menu allows you to switch between questions.

        **arrow up** - Takes you to the question higher.

        **arrow down** - Take you to the question lower.

=== "Shopify"

    ![quiz builder conditional logic](/images/how_to_use_skip_logic_cond_logic_intro.png)

    In the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab you can branch your quiz. The right menu allows you to add conditional logic rules to questions in the quiz. The left preview shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

    By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

    ??? question "How to navigate the Conditional Logic tab?"

        ![quiz builder conditional logic preview options](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_zoom.png)

        **+** - Zoom in on the logic tree preview.

        **-** - Zoom out on the logic tree preview.

        **[]** - Center the logic tree preview and fit into view.

        🔒 - Toggle interactivity. Lock or unlock the interactivaity of hte preview.

        Drag the logic tree with your mouse left button to navigate to specific branches.

=== "WooCommerce"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    In the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab you can branch your quiz. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

    By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

    ??? question "How to navigate the Conditional Logic tab?"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        **+** - Zoom in on the logic tree preview.

        **-** - Zoom out on the logic tree preview.

        **[]** - Center the logic tree preview and fit into view.

        Drag the logic tree with your mouse left button to navigate to specific branches.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The top menu allows you to switch between questions.

        **arrow up** - Takes you to the question higher.

        **arrow down** - Take you to the question lower.

=== "Magento"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    In the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab you can branch your quiz. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

    By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

    ??? question "How to navigate the Conditional Logic tab?"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        **+** - Zoom in on the logic tree preview.

        **-** - Zoom out on the logic tree preview.

        **[]** - Center the logic tree preview and fit into view.

        Drag the logic tree with your mouse left button to navigate to specific branches.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The top menu allows you to switch between questions.

        **arrow up** - Takes you to the question higher.

        **arrow down** - Take you to the question lower.

=== "BigCommerce"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    In the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab you can branch your quiz. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

    By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

    ??? question "How to navigate the Conditional Logic tab?"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        **+** - Zoom in on the logic tree preview.

        **-** - Zoom out on the logic tree preview.

        **[]** - Center the logic tree preview and fit into view.

        Drag the logic tree with your mouse left button to navigate to specific branches.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The top menu allows you to switch between questions.

        **arrow up** - Takes you to the question higher.

        **arrow down** - Take you to the question lower.

=== "Standalone"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    In the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab you can branch your quiz. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

    By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

    ??? question "How to navigate the Conditional Logic tab?"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        **+** - Zoom in on the logic tree preview.

        **-** - Zoom out on the logic tree preview.

        **[]** - Center the logic tree preview and fit into view.

        Drag the logic tree with your mouse left button to navigate to specific branches.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The top menu allows you to switch between questions.

        **arrow up** - Takes you to the question higher.

        **arrow down** - Take you to the question lower.

## Add Skip Logic to Questions

Skip Logic determines whether a question is presented or skipped based on responses to previous questions. By default, if no Skip Logic is added to a question, it will be shown.

!!! info

    All the Skip Logic rules follow the same format:

    - **IF response to** pick the question from a dropdown list
    - **is**/ **is not** pick a choice from the dropdown list
    - **THEN this question is skipped**

=== "Shopify (Legacy)"

    1. You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](/reference/quiz-builder/conditional-logic/) of a question.
    2. Open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) tab. 
    3. **Add Skip Logic**: From here, click `Add Skip Logic`. You can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed. These statements follow a simple format: IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 

        !!! example

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then Question 2 "What is your skin type?" will be skipped (it will not be shown).

    4. All slides that contain Skip Logic will be marked with `"skip logic"` text.
    5. Multiple Skip Logic rules can be added to any question if needed.

        - **+** - Adds another Skip Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Skip Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    5. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

=== "Shopify"

    1. You can introduce Skip Logic into your quiz by opening the [Quiz Builder > Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.
    2. Select a question that you want to be skipped and in the right-hand side menu open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) dropdown.

        ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic.png)
    3. **Add Skip Logic**: From here, click `+ Add another rule (OR)`. You can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed. These statements follow a simple format: IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 

        !!! example

            ![quiz builder conditional logic skip logic rule](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            In the example, if a user chooses a choice "Too shiny" in Question 9 "SKIN CONCERNS" then Question 10 "ALERGIES" will be skipped (it will not be shown).

    4. Multiple Skip Logic rules can be added to any question if needed.

        - **+ Add another rule (OR)** - Adds another Skip Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Skip Logic rule.
        - **+ Add concurrent logic (AND)** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    5. **Preview and Adjust:** Publish the changes with the top-right `Save` button to update the preview/live quiz and test the setup.

=== "WooCommerce"

    1. You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](/reference/quiz-builder/conditional-logic/) of a question.
    2. Open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) tab. 
    3. **Add Skip Logic**: From here, click `Add Skip Logic`. You can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed. These statements follow a simple format: IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 

        !!! example

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then Question 2 "What is your skin type?" will be skipped (it will not be shown).

    4. All slides that contain Skip Logic will be marked with `"skip logic"` text.
    5. Multiple Skip Logic rules can be added to any question if needed.

        - **+** - Adds another Skip Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Skip Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    5. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

=== "Magento"

    1. You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](/reference/quiz-builder/conditional-logic/) of a question.
    2. Open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) tab. 
    3. **Add Skip Logic**: From here, click `Add Skip Logic`. You can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed. These statements follow a simple format: IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 

        !!! example

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then Question 2 "What is your skin type?" will be skipped (it will not be shown).

    4. All slides that contain Skip Logic will be marked with `"skip logic"` text.
    5. Multiple Skip Logic rules can be added to any question if needed.

        - **+** - Adds another Skip Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Skip Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    5. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

=== "BigCommerce"

    1. You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](/reference/quiz-builder/conditional-logic/) of a question.
    2. Open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) tab. 
    3. **Add Skip Logic**: From here, click `Add Skip Logic`. You can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed. These statements follow a simple format: IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 

        !!! example

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then Question 2 "What is your skin type?" will be skipped (it will not be shown).

    4. All slides that contain Skip Logic will be marked with `"skip logic"` text.
    5. Multiple Skip Logic rules can be added to any question if needed.

        - **+** - Adds another Skip Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Skip Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    5. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

=== "Standalone"

    1. You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](/reference/quiz-builder/conditional-logic/) of a question.
    2. Open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) tab. 
    3. **Add Skip Logic**: From here, click `Add Skip Logic`. You can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed. These statements follow a simple format: IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 

        !!! example

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then Question 2 "What is your skin type?" will be skipped (it will not be shown).

    4. All slides that contain Skip Logic will be marked with `"skip logic"` text.
    5. Multiple Skip Logic rules can be added to any question if needed.

        - **+** - Adds another Skip Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Skip Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    5. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

## Examples and Applications

### Skip Questions Based on User's Answers

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Skip Logic, which then continues the quiz based on the participant's specific path.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    **Implementation**

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

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=WauBIBFSMPIlFNtm&amp;start=9" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Skip Logic, which then continues the quiz based on the participant's specific path.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

    **Implementation**

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


    **Scenario**

    You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Skip Logic, which then continues the quiz based on the participant's specific path.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    **Implementation**

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


    **Scenario**

    You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Skip Logic, which then continues the quiz based on the participant's specific path.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    **Implementation**

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


    **Scenario**

    You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Skip Logic, which then continues the quiz based on the participant's specific path.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    **Implementation**

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


    **Scenario**

    You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Skip Logic, which then continues the quiz based on the participant's specific path.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    **Implementation**

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




### Show Different Follow-Up Questions After Multiple-Selection Question

=== "Shopify (Legacy)"


    **Scenario**

    You want to create a beauty quiz where customers can select multiple areas of concern (nails, skin, hair, etc.) and then only see follow-up questions relevant to their selections.

    **Implementation**

    1. **Create a Multiple Selection Question**: Start with a question that allows customers to select multiple options, such as "Which areas would you like to focus on?" with choices like "Nails", "Skin", "Hair", and "Makeup".

        !!! tip

            You can allow multiple selections in the [block settings > multiple choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Set Up Follow-up Questions**: Create a series of follow-up questions for each area, arranged in groups:

        - Questions 2-3: Nail-related questions
        - Questions 4-5: Skin-related questions
        - Questions 6-7: Hair-related questions
        - Questions 8-9: Makeup-related questions

    3. **Apply Skip Logic to Each Follow-up Question**:

        - For each nail-related question (2-3), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Nails' THEN this question is skipped"
        - For each skin-related question (4-5), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Skin' THEN this question is skipped"
        - For each hair-related question (6-7), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Hair' THEN this question is skipped"
        - For each makeup-related question (8-9), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Makeup' THEN this question is skipped"

        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            In the example, if a user chooses a choice "Too shiny" in Question 9 "SKIN CONCERNS" then Question 10 "ALERGIES" will be skipped (it will not be shown).


    4. **Result**: When a customer selects multiple areas (e.g., "Nails" and "Skin"), they will only see the follow-up questions for those specific areas, skipping all others. This creates a personalized experience while maintaining a linear quiz structure.

    !!! tip

        This approach works best with a linear quiz structure (no branching). The key is to use the "IS NOT" condition in your Skip Logic rules, which ensures that questions are only shown when the customer has selected the relevant option in the main question.


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=8mMuIlNk_TnNkKnD&amp;start=62" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You want to create a beauty quiz where customers can select multiple areas of concern (acne, flaky skin, wrinkles, etc.) and then only see follow-up questions relevant to their selections. The goal is to display only the follow-up questions that are relevant to the user's selections. For example, if a user selects 'acne' as a skin concern, only questions related to acne should be displayed.

    **Implementation**

    1. **Setting Up Follow-Up Questions**: Use the [Quiz Builder](/reference/quiz-builder/) to add a multiple-choice question that allows multiple selections (this can be done via the [Multiple Choice Block Settings](/reference/quiz-builder/questions/#multiple-choice)) and create several follow-up questions that match the choices in the initial question.

        !!! example

            For example, if my Skin Concerns question has the following choices:

            - Acne
            - Flaky Skin
            - Wrinkles

            I can create the following follow-up questions:

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/how_to_shopifyV2_skiplogic_example_logic_multipleselection_questions.png)

        !!! warning

            Follow-up questions should be ordered in the same order as the choices presented in the initial question. So if the first choice is 'acne', the first follow-up question should be the one related to acne, and so on.

    2. **Configuring Skip Logic Rules**: Head over to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that should be skipped. For each follow-up question, establish a skip logic rule: 

        Skip Logic Rules will follow the following format:

        !!! example

            **IF** the response to the question... `Q9: Skin Concerns` **is not** `acne`, then this question will be skipped.

            ![how_to_shopifyV2_skiplogic_example_logic_rule_multipleselection](/images/how_to_shopifyV2_skiplogic_example_logic_rule_multipleselection.png)

        Similar rules must be applied for the other skin concern follow-up questions.

    3. **Testing Skip Logic Functionality**: After setting up the skip logic, make sure to save the changes with the top-right `Save` button. Then, ` Preview` the quiz and test the functionality by selecting different options in the quiz. 
    
        *For instance, selecting 'acne' and 'wrinkles' should display only the relevant follow-up questions while skipping others. If 'tight flaky skin' is selected, only questions related to flaky skin should appear, confirming that the skip logic is functioning correctly.*


=== "WooCommerce"



    **Scenario**

    You want to create a beauty quiz where customers can select multiple areas of concern (nails, skin, hair, etc.) and then only see follow-up questions relevant to their selections.

    **Implementation**

    1. **Create a Multiple Selection Question**: Start with a question that allows customers to select multiple options, such as "Which areas would you like to focus on?" with choices like "Nails", "Skin", "Hair", and "Makeup".

        !!! tip

            You can allow multiple selections in the [block settings > multiple choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Set Up Follow-up Questions**: Create a series of follow-up questions for each area, arranged in groups:

        - Questions 2-3: Nail-related questions
        - Questions 4-5: Skin-related questions
        - Questions 6-7: Hair-related questions
        - Questions 8-9: Makeup-related questions

    3. **Apply Skip Logic to Each Follow-up Question**:

        - For each nail-related question (2-3), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Nails' THEN this question is skipped"
        - For each skin-related question (4-5), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Skin' THEN this question is skipped"
        - For each hair-related question (6-7), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Hair' THEN this question is skipped"
        - For each makeup-related question (8-9), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Makeup' THEN this question is skipped"

        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            In the example, if a user chooses a choice "Too shiny" in Question 9 "SKIN CONCERNS" then Question 10 "ALERGIES" will be skipped (it will not be shown).


    4. **Result**: When a customer selects multiple areas (e.g., "Nails" and "Skin"), they will only see the follow-up questions for those specific areas, skipping all others. This creates a personalized experience while maintaining a linear quiz structure.

    !!! tip

        This approach works best with a linear quiz structure (no branching). The key is to use the "IS NOT" condition in your Skip Logic rules, which ensures that questions are only shown when the customer has selected the relevant option in the main question.



=== "Magento"



    **Scenario**

    You want to create a beauty quiz where customers can select multiple areas of concern (nails, skin, hair, etc.) and then only see follow-up questions relevant to their selections.

    **Implementation**

    1. **Create a Multiple Selection Question**: Start with a question that allows customers to select multiple options, such as "Which areas would you like to focus on?" with choices like "Nails", "Skin", "Hair", and "Makeup".

        !!! tip

            You can allow multiple selections in the [block settings > multiple choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Set Up Follow-up Questions**: Create a series of follow-up questions for each area, arranged in groups:

        - Questions 2-3: Nail-related questions
        - Questions 4-5: Skin-related questions
        - Questions 6-7: Hair-related questions
        - Questions 8-9: Makeup-related questions

    3. **Apply Skip Logic to Each Follow-up Question**:

        - For each nail-related question (2-3), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Nails' THEN this question is skipped"
        - For each skin-related question (4-5), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Skin' THEN this question is skipped"
        - For each hair-related question (6-7), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Hair' THEN this question is skipped"
        - For each makeup-related question (8-9), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Makeup' THEN this question is skipped"

        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            In the example, if a user chooses a choice "Too shiny" in Question 9 "SKIN CONCERNS" then Question 10 "ALERGIES" will be skipped (it will not be shown).


    4. **Result**: When a customer selects multiple areas (e.g., "Nails" and "Skin"), they will only see the follow-up questions for those specific areas, skipping all others. This creates a personalized experience while maintaining a linear quiz structure.

    !!! tip

        This approach works best with a linear quiz structure (no branching). The key is to use the "IS NOT" condition in your Skip Logic rules, which ensures that questions are only shown when the customer has selected the relevant option in the main question.



=== "BigCommerce"



    **Scenario**

    You want to create a beauty quiz where customers can select multiple areas of concern (nails, skin, hair, etc.) and then only see follow-up questions relevant to their selections.

    **Implementation**

    1. **Create a Multiple Selection Question**: Start with a question that allows customers to select multiple options, such as "Which areas would you like to focus on?" with choices like "Nails", "Skin", "Hair", and "Makeup".

        !!! tip

            You can allow multiple selections in the [block settings > multiple choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Set Up Follow-up Questions**: Create a series of follow-up questions for each area, arranged in groups:

        - Questions 2-3: Nail-related questions
        - Questions 4-5: Skin-related questions
        - Questions 6-7: Hair-related questions
        - Questions 8-9: Makeup-related questions

    3. **Apply Skip Logic to Each Follow-up Question**:

        - For each nail-related question (2-3), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Nails' THEN this question is skipped"
        - For each skin-related question (4-5), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Skin' THEN this question is skipped"
        - For each hair-related question (6-7), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Hair' THEN this question is skipped"
        - For each makeup-related question (8-9), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Makeup' THEN this question is skipped"

        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            In the example, if a user chooses a choice "Too shiny" in Question 9 "SKIN CONCERNS" then Question 10 "ALERGIES" will be skipped (it will not be shown).


    4. **Result**: When a customer selects multiple areas (e.g., "Nails" and "Skin"), they will only see the follow-up questions for those specific areas, skipping all others. This creates a personalized experience while maintaining a linear quiz structure.

    !!! tip

        This approach works best with a linear quiz structure (no branching). The key is to use the "IS NOT" condition in your Skip Logic rules, which ensures that questions are only shown when the customer has selected the relevant option in the main question.



=== "Standalone"



    **Scenario**

    You want to create a beauty quiz where customers can select multiple areas of concern (nails, skin, hair, etc.) and then only see follow-up questions relevant to their selections.

    **Implementation**

    1. **Create a Multiple Selection Question**: Start with a question that allows customers to select multiple options, such as "Which areas would you like to focus on?" with choices like "Nails", "Skin", "Hair", and "Makeup".

        !!! tip

            You can allow multiple selections in the [block settings > multiple choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Set Up Follow-up Questions**: Create a series of follow-up questions for each area, arranged in groups:

        - Questions 2-3: Nail-related questions
        - Questions 4-5: Skin-related questions
        - Questions 6-7: Hair-related questions
        - Questions 8-9: Makeup-related questions

    3. **Apply Skip Logic to Each Follow-up Question**:

        - For each nail-related question (2-3), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Nails' THEN this question is skipped"
        - For each skin-related question (4-5), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Skin' THEN this question is skipped"
        - For each hair-related question (6-7), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Hair' THEN this question is skipped"
        - For each makeup-related question (8-9), add a Skip Logic rule: "IF response to Question 1 IS NOT 'Makeup' THEN this question is skipped"

        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            In the example, if a user chooses a choice "Too shiny" in Question 9 "SKIN CONCERNS" then Question 10 "ALERGIES" will be skipped (it will not be shown).


    4. **Result**: When a customer selects multiple areas (e.g., "Nails" and "Skin"), they will only see the follow-up questions for those specific areas, skipping all others. This creates a personalized experience while maintaining a linear quiz structure.

    !!! tip

        This approach works best with a linear quiz structure (no branching). The key is to use the "IS NOT" condition in your Skip Logic rules, which ensures that questions are only shown when the customer has selected the relevant option in the main question.




!!! info

    Also check our guide to setting up a [Funnel Quiz that Skips Slides](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-that-skips-slides).



### Filtering Email Collection Based on Interest

=== "Shopify (Legacy)"

    **Scenario**

    You want to collect emails from interested customers without deterring others.

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    **Implementation**

    - Start with a `Yes/No question` asking if the customer is willing to leave their email.
    - Follow up with an `email` input question.
    - Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.

=== "Shopify"


    **Scenario**

    You want to collect emails from interested customers without deterring others.

    ![how to use skip logic example2](/images/how_to_shopifyV2_skiplogic_example_logic_email_question_skipped.png)

    **Implementation**

    - Start with a [`Yes/No question`](/reference/quiz-builder/questions/#yesno) asking if the customer is willing to leave their email.
    - Follow up with an [`email` input question](/reference/quiz-builder/questions/#email).
    - Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.


=== "WooCommerce"


    **Scenario**

    You want to collect emails from interested customers without deterring others.

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    **Implementation**

    - Start with a `Yes/No question` asking if the customer is willing to leave their email.
    - Follow up with an `email` input question.
    - Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.


=== "Magento"


    **Scenario**

    You want to collect emails from interested customers without deterring others.

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    **Implementation**

    - Start with a `Yes/No question` asking if the customer is willing to leave their email.
    - Follow up with an `email` input question.
    - Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.


=== "BigCommerce"


    **Scenario**

    You want to collect emails from interested customers without deterring others.

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    **Implementation**

    - Start with a `Yes/No question` asking if the customer is willing to leave their email.
    - Follow up with an `email` input question.
    - Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.


=== "Standalone"


    **Scenario**

    You want to collect emails from interested customers without deterring others.

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    **Implementation**

    - Start with a `Yes/No question` asking if the customer is willing to leave their email.
    - Follow up with an `email` input question.
    - Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.




### Skip Logic vs. Jump Logic

The new app interface gives the option to use Jump Logic and Skip Logic. You shouldn’t combine both types of logic in the same quiz.

- **Jump Logic** creates diverging paths within a quiz based on respondent answers, allowing for a branched experience.
- **Skip Logic**, in contrast, customizes the path by omitting certain questions based on previous answers, keeping the overall sequence intact but personalized.



## Additional Resources

Understanding conditional logic, the foundation of Skip Logic, can be challenging. Resources such as [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) offer tutorials on AND/OR logic, which can enhance your ability to create effective and complex quiz flows.

---
This guide explains how to use Skip Logic in your quiz to hide follow-up questions based on the user's answers and includes specific use-cases and step-by-step instructions.

