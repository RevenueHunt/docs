# How to use Display Logic

[Display logic](/reference/quiz-builder/conditional-logic/#display-logic) is a feature of the [Results Page](/reference/quiz-builder/results-page/) that allows you to make elements visible or hidden on the results page based on conditional logic rules.

!!! info "Use Display Logic to:"

    - Show or hide content on the results page based on customer's responses to questions.
    - Show or hide content on the results page based on the score of a variable (custom scoring quiz, personality-type quiz).
    - Show or hide content on the results page based on the variable with the highest score (personality-type quiz).

In this article, we provide a clear, step-by-step guide on how to use Display Logic, its workings, and examples to illustrate its functionality.

=== "Shopify"

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=3YY9lVuHYozbUYVq" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce"


    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "Magento"


    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "BigCommerce"


    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

=== "Standalone"


    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## Results Page

In the [Results Page](/reference/quiz-builder/results-page/) section, you can add content to the results page shown at the end of the quiz. You can adjust the results page settings and see the preview of how the results page looks like.

=== "Shopify"

    ??? question "What content be added to the Results Page?"

        You can add different types of building blocks to your results page:

        - **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
        - **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.
        - **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
        - **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
        - **Products Block** - Adds a block specifically designed for displaying a list of recommended products.
        - **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

=== "Shopify V2"

    ??? question "What content be added to the Results Page?"

        You can add different types of building blocks to your results page:

        - **Section** - Adds a new section to your page, ideal for grouping content together.

        In each section, you can add the following blocks:

        - **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
        - **Text Block** - Adds a new text block to your page, ideal for adding and formatting text, lists, and links.
        - **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
        - **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
        - **Video Block** - Adds a video block into your page. You can upload your own video from the Shopify ContentLibrary.
        - **Button Block** - Adds a button block into your page. You can add a link to the button.
        - **Products Block** - Adds a block specifically designed for displaying a list of recommended products, product variants or product collections.

=== "WooCommerce"

    ??? question "What content be added to the Results Page?"

        You can add different types of building blocks to your results page:

        - **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
        - **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.
        - **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
        - **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
        - **Products Block** - Adds a block specifically designed for displaying a list of recommended products.
        - **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

=== "Magento"

    ??? question "What content be added to the Results Page?"

        You can add different types of building blocks to your results page:

        - **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
        - **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.
        - **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
        - **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
        - **Products Block** - Adds a block specifically designed for displaying a list of recommended products.
        - **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

=== "BigCommerce"

    ??? question "What content be added to the Results Page?"

        You can add different types of building blocks to your results page:

        - **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
        - **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.
        - **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
        - **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
        - **Products Block** - Adds a block specifically designed for displaying a list of recommended products.
        - **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

=== "Standalone"

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

    With Display Logic you can make sections visible or hidden based on customer's responses.

    1. **Find a section**: Start by identifying or adding the section you wish to add Display Logic to. 
    2. **Open Display Logic settings**: Click on the section and on the right-hand side identify the `Display logic`.

        ![quiz builder results page block menu](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

    3. Next, select `+ Add logic condition (OR)` to set up the first Display Logic rule.

        ---

        **Display logic operators**

        `+ Add condition (OR)` - Adds a new OR display logic rule.

        `+ Add condtion (AND)` - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

        `bin` - Delete the current Logic rule.
        
        `+ Add condition (OR)` - Adds another Display Logic rule. Adds a new OR logical rule.

        `Default` - Select whether this section should be `Shown` or `Hidden` by default.

        ---

        There are three types of Display Logic rules you can choose from:

        ---

        **Type 1: IF The response to the question...**

        Then the Display Logic rules follow the following format:

        - **IF response to** pick the question from a dropdown list
        - **is**/ **is not** pick a choice from the dropdown list
        - **THEN section is Visible** 
        - **Default visibility** pick either **Visible** or **Hidden**. If Visible is selected, then section will be shown by default unless the Display Logic rule is triggered. If Hidden is selected, the section will be hidden by default unless the Display Logic rule is triggered.

        !!! example "Example 1"

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

            In the example, if a user chooses a choice "Oily all over" in Question 4 "SKIN TYPE" then this section will be visible. If they give a different answer in Question 4 this content block will be hidden.

        ---

        **Type 2: IF The score of the variable...**

        Then the Display Logic rules follow the following format:

        - **IF The score of the variable** 
        - **score** pick the variable from a dropdown list
        - **is equal to**/ **is not equal to** / **is greater than**/ **is less than** / **is greater than or equal to** / **is less than or equal to** pick a choice from the dropdown list
        - **Number** / **Another variable** pick a choice from the dropdown list
        - **0** / **1** / **2** / **other numerical value** type a value in the input field
        - **THEN section is Visible** 
        - **Default visibility** pick either **Visible** or **Hidden**. If Visible is selected, then section will be shown by default unless the Display Logic rule is triggered. If Hidden is selected, the section will be hidden by default unless the Display Logic rule is triggered.


        !!! info

            Note: Scores are assigned to each choice in the [Questions](/reference/quiz-builder/questions) tab > [Choice settings](/reference/quiz-builder/choice-settings) section.


        !!! example "Example 2"

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_scorerange](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_scorerange.png)

            In the example, if the score of the variable `dry` is greater than or equal to number `5` AND IF the score of the varaible `dry` is less than or equal to number `7` then this section will be visible. Otherwise, the section will be hidden.

        ---

        **Type 3: IF the variable with the highest score...**

        Then the Display Logic rules follow the following format:

        - **IF the variable with the highest score** 
        - **score** pick the variable from a dropdown list
        - **THEN section is Visible**
        - **Default visibility** pick either **Visible** or **Hidden**. If Visible is selected, then section will be shown by default unless the Display Logic rule is triggered. If Hidden is selected, the section will be hidden by default unless the Display Logic rule is triggered.

        !!! info

            Note: Scores are assigned to each choice in the [Questions](/reference/quiz-builder/questions) tab > [Choice settings](/reference/quiz-builder/choice-settings) section.


        !!! example "Example 3"

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_winningvaraible](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_winningvaraible.png)

            In the example, if the variable with the highest score is `dry` then this section will be visible. Otherwise, the section will be hidden.

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



## How to Add Scores or Variables to Choices

=== "Shopify"

    Scoring system is not available in the legacy version of the Shopify app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Shopify V2" 

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=EoRzoYJ04e48VsJu&amp;start=96" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Custom scores or variables can be assigned to choices in the quiz in order to set up a scoring quiz, personality type quiz, dosha quiz, etc.

    To add scores or variables to choices, follow these steps:

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple choice questions` asking the customer about their needs. For example: age, skincondition, etc. if you are building a quzi that determines a skin type.
    2. Open the [Choice Settings](/reference/quiz-builder/choice-settings/).
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

    Scoring system is not available in the WooCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Magento"

    Scoring system is not available in the Magento version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    Scoring system is not available in the BigCommerce version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. Your developer can implement a custom scoring system with JavaScript on the Results Page instead. Check this article to learn how to add custom JavaScript to the Results Page: [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).




## Examples and Applications

### Display Logic Based on Customer Answers

=== "Shopify"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You want to show a custom text block based on the customer's answer to a question. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different text and recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

    **Implementation**

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

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=w8QWpvi3Ga5dbtxl&amp;start=11" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You want to show a section based on the customer's answer to a question. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different text and recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

    **Implementation**

    **Step 1: Add sections to the Results Page**

    The quiz has four sections on the Results Page for different skin types: Dry Skin, Normal Skin, Oily Skin, and Combination Skin. Without display logic, all sections would be visible at once.To show only one section based on user responses, display logic must be applied to each section.

    **Step 2: Configuring Display Logic for Dry Skin Section**

    1. *Find the Dry Skin Section*: Locate the section on the Results Page that corresponds to Dry Skin.
    2. *Open Display Logic Settings*: Click the `conditional logic / tree icon` button to open the Display Logic menu.
    3. *Add Display Logic Rule*: Select `+ Add logic condition (OR)` to create a new Display Logic rule.
    4. *Set Up the Rule*:

        - **If** `The response to question` - Choose the `question` that determines the skin type.
        - **is** - Select the choice that corresponds to `Dry Skin`.
        - **THEN section is VISIBLE**
        - Choose `Default visibility` to be `Hidden`.

        ![display logic example](/images/how_to_shopifyv2_use_display_logic_based_on_answers_example1.png)

    **Step 3: Repeat the process for other skin types:** 

    - Normal Skin: Visible if the response is "not too oily and not too dry".
    - Oily Skin: Visible if the response is "oily all over".
    - Combination Skin: Visible if the response is "oily in certain spots".

    **Step 4: Preview and Adjust**

    Publish the changes with the top-right `Save` button to update the preview/live quiz and test the setup. Test by selecting different skin types to ensure only the relevant section is displayed.

    **Advanced Display Logic Conditions**

    You can set multiple conditions for display logic: 

    - Example: A section can be visible if the skin type is "dry and tight" or if the age group is "teens".
    - Another example: A section can be visible if both conditions are met: skin type is "dry and tight" and skin concerns include "acne".

=== "WooCommerce"



    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You want to show a custom text block based on the customer's answer to a question. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different text and recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

    **Implementation**

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

    **Scenario**

    You want to show a custom text block based on the customer's answer to a question. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different text and recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

    **Implementation**

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

    **Scenario**

    You want to show a custom text block based on the customer's answer to a question. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different text and recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

    **Implementation**

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

    **Scenario**

    You want to show a custom text block based on the customer's answer to a question. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different text and recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Display Logic.

    **Implementation**

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



### Diplsay Logic Based on Winning Variable

=== "Shopify"

    **Scenario**

    You're building a personality-type or Dosha quiz. You want to show a different text and product recommendations based on the winning variable. For examples, if the user chooses mostly A's, B's, C's, etc. a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the legacy version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.


=== "Shopify V2"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=G0PM__FcEyQJDtBp&amp;start=189" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You're building a personality-type or Dosha quiz. You want to show a different text and product recommendations based on the winning variable. For examples, if the user chooses mostly A's, B's, C's, etc. a different section with different text and product recommendations is shown.

    **Implementation**

    **Step 1: Add Questions, Choices and Custom Variables**

    The quiz consists of five questions, each with five choices. Each choice is associated with a [custom variable and a score](#how-to-add-scores-or-variables-to-choices) via the [`Choices Settings`](/reference/quiz-builder/questions/#choice-settings) section. 

    !!! tip

        To learn how to add scores or variables to choices, check out this guide: [How to Add Scores or Variables to Choices](/how-to-guides/use-display-logic/#how-to-add-scores-or-variables-to-choices).
    
    Each answer contributes a score of +1 to the corresponding skin type variable: 

    - Dry skin: `dry +1`    
    - Normal skin: `normal +1`
    - Oily skin: `oily +1`
    - Combination skin: `combination +1`
    - Sensitive skin: `sensitive +1`

    ![how to shopifyv2 use display logic based on variable example1 scores](/images/how_to_shopifyv2_use_display_logic_based_on_variable_example1_scores.png)

    This scoring will help determine the user's skin type based on their responses.

    **Step 2: Add Sections to the Results Page**

    The results page contains five sections, each corresponding to a skin type. Each section contains a heading, text and a product block to recommend products for that skin type.

    Each section can display recommended products in a [product block](/reference/quiz-builder/results-page/#products-products-variants-collections) based on user responses or fixed recommendations: 

    - **Dynamic Recommendations:** Requires upvoting products via choice settings to influence the recommendation algorithm.
    - **Fixed Recommendations:** Set specific products to always display for each skin type section by changing the recommendation system to fixed and selecting items for each block. Ensure to configure fixed recommendations for all sections to provide consistent product suggestions.

    Change the `Recommendation System` in the [`Product Block Settings`](/reference/quiz-builder/results-page/#products-products-variants-collections) to whatever best suits your needs. For a personality-type quiz, we recommend using `Fixed Recommendations` and selecting products for each section.

    **Step 3: Add Display Logic to the Sections**

    To display the correct section based on the highest scoring variable, follow these steps: 

    1. Go to Section Settings, find `Display Logic` and click `+ Add condition (OR)`.

    2. Set up the rule like this:

        - **If** `The variable with the highest score` 
        - `is` - `dry` 
        - **THEN this section is VISIBLE**
        - Set the `Default visibility` to `Hidden`.

        ![how to shopifyv2 use display logic based on variable example1 display logic](/images/how_to_shopifyv2_use_display_logic_based_on_variable_example1.png)

    3. For each skin type, set a similar rule for the visibility condition: 

        - If the highest score is `dry`, show the dry skin section.
        - If the highest score is `normal`, show the normal skin section.
        - If the highest score is `oily`, show the oily skin section.
        - If the highest score is `combination`, show the combination section.
        - If the highest score is `sensitive`, show the sensitive skin section.

    **Step 4: Save and Test the Setup**

    Publish the changes with the top-right `Save` button to update the preview/live quiz and click `Preview` to test the setup. Select answers that correspond to a specific skin type (e.g., mostly dry skin). Verify that the correct results section is displayed based on the selected answers.

=== "WooCommerce"

    **Scenario**

    You're building a personality-type or Dosha quiz. You want to show a different text and product recommendations based on the winning variable. For examples, if the user chooses mostly A's, B's, C's, etc. a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the WooCommerce version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.

=== "Magento"

    **Scenario**

    You're building a personality-type or Dosha quiz. You want to show a different text and product recommendations based on the winning variable. For examples, if the user chooses mostly A's, B's, C's, etc. a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the Magento version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.


=== "BigCommerce"

    **Scenario**

    You're building a personality-type or Dosha quiz. You want to show a different text and product recommendations based on the winning variable. For examples, if the user chooses mostly A's, B's, C's, etc. a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the BigCommerce version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.   

=== "Standalone"    

    **Scenario**

    You're building a personality-type or Dosha quiz. You want to show a different text and product recommendations based on the winning variable. For examples, if the user chooses mostly A's, B's, C's, etc. a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the standalone version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.


### Display Logic Based on Custom Score

=== "Shopify"

    **Scenario**

    You're building a custom scoring or presonality-type quiz. You want to show a different text and product recommendations based on the score of a variable. For examples, if the user's score is above 50, a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the legacy version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=JG9rNnYpv1aqcdvO&amp;start=269" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Scenario**

    You're building a custom scoring or presonality-type quiz. You want to show a different text and product recommendations based on the score of a variable. For examples, if the user's score is above 50, a different section with different text and product recommendations is shown.

    **Implementation**

    **Step 1: Add Questions, Choices and Custom Variables**

    The quiz consists of five questions, each with five choices. Each choice is associated with a [custom score](/how-to-guides/use-display-logic/#how-to-add-scores-or-variables-to-choices) via the [`Choices Settings`](/reference/quiz-builder/questions/#choice-settings) section. 

    !!! tip

        To learn how to add scores or variables to choices, check out this guide: [How to Add Scores or Variables to Choices](/how-to-guides/use-display-logic/#how-to-add-scores-or-variables-to-choices).
    
    Each answer contributes a score of +1 to the corresponding skin type variable: 

    - First choice: 1 point
    - Second choice: 2 points
    - Third choice: 3 points
    - Fourth choice: 4 points
    - Fifth choice: 5 points

    The total score helps determine the user's skin type based on their selections.

    ![how_to_shopifyv2_use_display_logic_based_on_score_example1](/images/how_to_shopifyv2_use_display_logic_based_on_score_example1.png)

    **Step 2: Add Sections to the Results Page**

    The results page contains five sections, each corresponding to a skin type. Each section contains a heading, text and a product block to recommend products for that skin type.

    Each section can display recommended products in a [product block](/reference/quiz-builder/results-page/#products-products-variants-collections) based on user responses or fixed recommendations: 

    - **Dynamic Recommendations:** Requires upvoting products via choice settings to influence the recommendation algorithm.
    - **Fixed Recommendations:** Set specific products to always display for each skin type section by changing the recommendation system to fixed and selecting items for each block. Ensure to configure fixed recommendations for all sections to provide consistent product suggestions.

    Change the `Recommendation System` in the [`Product Block Settings`](/reference/quiz-builder/results-page/#products-products-variants-collections) to whatever best suits your needs. For a personality-type quiz, we recommend using `Fixed Recommendations` and selecting products for each section.      

    **Step 3: Add Display Logic to the Sections**

    To display the correct section based on the total score, follow these steps: 

    1. Go to Section Settings, find `Display Logic` and click `+ Add condition (OR)`.

    2. Set up the rule like this:

        - **If** `The score of a variable`  select the varaible `score` 
        - `is greater than or equal to` - `5`
        - **AND**
        - **IF** `The score of a variable`  select the varaible `score` 
        - `is less than or equal to` - `7`
        - **THEN this section is VISIBLE**
        - Set the `Default visibility` to `Hidden`.

        ![how_to_shopifyv2_use_display_logic_based_on_score_example1_logic](/images/how_to_shopifyv2_use_display_logic_based_on_score_example1_logic.png)

    3. For each skin type, set a similar rule for the visibility condition: 

        - Show  dry skin section if score is between 5 and 7 (inclusive). Condition: `score >= 5 && score <= 7`
        - Show normal skin section if score is between 8 and 12 (inclusive). Condition: `score >= 8 && score <= 12`
        - Show oily skin section if score is between 13 and 17 (inclusive). Condition: `score >= 13 && score <= 17`
        - Show combination skin section if score is between 18 and 22 (inclusive). Condition: `score >= 18 && score <= 22`
        - Show sensitive skin section if score is between 23 and 25 (inclusive). Condition: `score >= 23 && score <= 25`


    **Step 4: Save and Test the Setup**

    Publish the changes with the top-right `Save` button to update the preview/live quiz and click `Preview` to test the setup. Select answers that correspond to a specific skin type (e.g., mostly dry skin). Verify that the correct results section is displayed based on the selected answers.





=== "WooCommerce"

    **Scenario**

    You're building a custom scoring or presonality-type quiz. You want to show a different text and product recommendations based on the score of a variable. For examples, if the user's score is above 50, a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the legacy version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.

=== "Magento"

    **Scenario**

    You're building a custom scoring or presonality-type quiz. You want to show a different text and product recommendations based on the score of a variable. For examples, if the user's score is above 50, a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the Magento version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.


=== "BigCommerce"

    **Scenario**

    You're building a custom scoring or presonality-type quiz. You want to show a different text and product recommendations based on the score of a variable. For examples, if the user's score is above 50, a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the BigCommerce version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.

=== "Standalone"

    **Scenario**

    You're building a custom scoring or presonality-type quiz. You want to show a different text and product recommendations based on the score of a variable. For examples, if the user's score is above 50, a different section with different text and product recommendations is shown.

    **Implementation**

    Custom Scores or variables are not natively supported in the standalone version of the RevenueHunt app. In this version of the app displaying content based on a custom score or variable is only possible via custom JavaScript and may require help from a developer.

    Check our [How to Add JavaScript](/how-to-guides/add-javascript/) guide for more information on implementing custom JavaScript into your product recommendation quiz.


## Additional Resources

Understanding conditional logic can be challenging. Resources such as [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) offer tutorials on AND/OR logic, which can enhance your ability to create effective and complex quiz flows.

---
This guide explains what is Display Logic and how to use it in Product Recommendation Quiz to show or hide content based on customer's responses to questions, the score of a variable (custom scoring quiz, personality-type quiz), or the variable with the highest score (personality-type quiz).