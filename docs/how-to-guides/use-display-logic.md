# How to use Display Logic

[Display logic](/reference/quiz-builder/conditional-logic/#display-logic) is a feature of the [Results Page](/reference/quiz-builder/results-page/) that allows you to make elements visible or hidden based on conditional logic rules.

<div class="videoWrapper"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## Results Page

In the [Results Page](/reference/quiz-builder/results-page/) section, you can add content to the results page shown at the end of the quiz. You can adjust the results page settings and see the preview of how the results page looks like.

??? question "What content be added to the Results Page?"

    You can add different types of building blocks to your results page:

    - **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
    - **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.
    - **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
    - **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
    - **Products Block** - Adds a block specifically designed for displaying a list of recommended products.
    - **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

## Add Display Logic to Block / Section

=== "Shopify"

    With Display Logic you can make blocks visible or hidden based on customer's responses.

    1. **Find a block**: Start by identifying or adding the block you wish to add Display Logic to. 
    2. **Open Display Logic settings**: Look for a `conditional logic / tree icon` button and click it. 
        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

        **conditional logic** / **tree icon** - Opens the [Display Logic](#display-logic) menu.

    3. Next, select `add Display Logic`.
        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    3. **Add your rules**: Add you display logic rules for when the block should be visible or hidden. 

        !!! info

            All the Display Logic rules follow the same format

            - **IF response to** pick the question from a dropdown list
            - **is**/ **is not** pick a choice from the dropdown list
            - **THEN block is** pick either **Visible** or **Hidden**
            - **IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

        !!! example

            ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.

    4. You can add multiple rules by clicking the `+` button.
        
        - **+** - Adds another Display Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Display Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    4. **Preview and Adjust**: Publish the changes with the top-right Publish button to update the preview/live quiz and test the setup.

=== "Shopify V2"

    With Display Logic / Display Logic you can make blocks visible or hidden based on customer's responses.

    1. **Find a section**: Start by identifying or adding the section you wish to add Display Logic to. 
    2. **Open DisplayLogic settings**: Click on the section and on the right-hand side identify the `Display logic`.

        ![quiz builder results page block menu](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

    3. Next, select `+ Add logic condition (OR)`.

        


        !!! info "➡️ Method 1: Using Answer-Based Display Logic"
    
            **Add your rules**: Add your display logic rules for when the block should be visible or hidden based on specific answers. 

            !!! info

                All the Display Logic rules follow the same format

                - **IF response to** pick the question from a dropdown list
                - **is**/ **is not** pick a choice from the dropdown list
                - **THEN block is** pick either **Visible** or **Hidden**
                - **IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

            !!! example

                ![quiz builder results page display logic example](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_exampleOR.png)

                In the example, if a user chooses a choice "Oily" in Question 1 "SKIN TYPE" then this section will be hidden. If they give a different answer in Question 1 this content block will be shown.

            You can add multiple rules by clicking the `+` button.
            
            - **+ Add condition (OR)** - Adds another Display Logic rule. Adds a new OR logical rule.
            - **bin** - Delete the current Display Logic rule.
            - **+ Add condtion (AND)** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.



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
            - Instead of using question-specific conditions, use the `The variable with the highest score...` or `The score of the variable...` option
            - Set up range conditions to control when each content block should be visible/hidden

            !!! example

                For example:
                - Dry skin content: Total score is between 5-7 points
                - Normal skin content: Total score is between 8-12 points
                - Oily skin content: Total score is between 13-17 points
                - Combination skin content: Total score is between 18-22 points
                - Sensitive skin content: Total score is between 23-25 points

            ![score-based display logic](/images/how_to_hide_content_with_logic_shopifyv2_score_logic.png)

    4. **Preview and Adjust**: Publish the changes with the top-right `Save` button to update the preview/live quiz and test the setup.

=== "WooCommerce"

    With Display Logic you can make blocks visible or hidden based on customer's responses.

    1. **Find a block**: Start by identifying or adding the block you wish to add Display Logic to. 
    2. **Open Display Logic settings**: Look for a `conditional logic / tree icon` button and click it. 
        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

        **conditional logic** / **tree icon** - Opens the [Display Logic](#display-logic) menu.

    3. Next, select `add Display Logic`.
        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    3. **Add your rules**: Add you display logic rules for when the block should be visible or hidden. 

        !!! info

            All the Display Logic rules follow the same format

            - **IF response to** pick the question from a dropdown list
            - **is**/ **is not** pick a choice from the dropdown list
            - **THEN block is** pick either **Visible** or **Hidden**
            - **IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

        !!! example

            ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.

    4. You can add multiple rules by clicking the `+` button.
        
        - **+** - Adds another Display Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Display Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    4. **Preview and Adjust**: Publish the changes with the top-right Publish button to update the preview/live quiz and test the setup.

=== "Magento"

    With Display Logic you can make blocks visible or hidden based on customer's responses.

    1. **Find a block**: Start by identifying or adding the block you wish to add Display Logic to. 
    2. **Open Display Logic settings**: Look for a `conditional logic / tree icon` button and click it. 
        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

        **conditional logic** / **tree icon** - Opens the [Display Logic](#display-logic) menu.

    3. Next, select `add Display Logic`.
        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    3. **Add your rules**: Add you display logic rules for when the block should be visible or hidden. 

        !!! info

            All the Display Logic rules follow the same format

            - **IF response to** pick the question from a dropdown list
            - **is**/ **is not** pick a choice from the dropdown list
            - **THEN block is** pick either **Visible** or **Hidden**
            - **IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

        !!! example

            ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.

    4. You can add multiple rules by clicking the `+` button.
        
        - **+** - Adds another Display Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Display Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    4. **Preview and Adjust**: Publish the changes with the top-right Publish button to update the preview/live quiz and test the setup.

=== "BigCommerce"

    With Display Logic you can make blocks visible or hidden based on customer's responses.

    1. **Find a block**: Start by identifying or adding the block you wish to add Display Logic to. 
    2. **Open Display Logic settings**: Look for a `conditional logic / tree icon` button and click it. 
        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

        **conditional logic** / **tree icon** - Opens the [Display Logic](#display-logic) menu.

    3. Next, select `add Display Logic`.
        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    3. **Add your rules**: Add you display logic rules for when the block should be visible or hidden. 

        !!! info

            All the Display Logic rules follow the same format

            - **IF response to** pick the question from a dropdown list
            - **is**/ **is not** pick a choice from the dropdown list
            - **THEN block is** pick either **Visible** or **Hidden**
            - **IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

        !!! example

            ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.

    4. You can add multiple rules by clicking the `+` button.
        
        - **+** - Adds another Display Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Display Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    4. **Preview and Adjust**: Publish the changes with the top-right Publish button to update the preview/live quiz and test the setup.

=== "Standalone"

    With Display Logic you can make blocks visible or hidden based on customer's responses.

    1. **Find a block**: Start by identifying or adding the block you wish to add Display Logic to. 
    2. **Open Display Logic settings**: Look for a `conditional logic / tree icon` button and click it. 
        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

        **conditional logic** / **tree icon** - Opens the [Display Logic](#display-logic) menu.

    3. Next, select `add Display Logic`.
        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    3. **Add your rules**: Add you display logic rules for when the block should be visible or hidden. 

        !!! info

            All the Display Logic rules follow the same format

            - **IF response to** pick the question from a dropdown list
            - **is**/ **is not** pick a choice from the dropdown list
            - **THEN block is** pick either **Visible** or **Hidden**
            - **IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

        !!! example

            ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

            In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.

    4. You can add multiple rules by clicking the `+` button.
        
        - **+** - Adds another Display Logic rule. Adds a new OR logical rule.
        - **bin** - Delete the current Display Logic rule.
        - **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

    4. **Preview and Adjust**: Publish the changes with the top-right Publish button to update the preview/live quiz and test the setup.

## Examples and Applications

### Customizing Content Based on Skin Type

You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

![how to use display logic example](/images/how_to_use_display_logic_example.png)

To learn how to build such a quiz check this [step-by-step guide](/how-to-guides/hide-content-with-logic/).

## Additional Resources

Understanding conditional logic can be challenging. Resources such as [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) offer tutorials on AND/OR logic, which can enhance your ability to create effective and complex quiz flows.

---
This guide explains what is Display Logic and how to use it in Product Recommendation Quiz.