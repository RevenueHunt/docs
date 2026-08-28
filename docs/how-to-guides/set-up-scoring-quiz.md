---
description: "Learn how to create a RevenueHunt scoring quiz with personality types and calculated results."
icon: material/scoreboard-outline
---

# How to Set Up a Scoring Quiz

Give each choice a score, a variable, or both. The quiz adds them up as the customer answers. Logic then decides which text and which products appear at the end.

!!! info "Use this method for:"

    - Personality type quizzes, Dosha quizzes
    - Quizzes that show different results based on how many choices the customer picked (for example if the customer chooses most As, Bs, Cs, etc.)
    - Quizzes that show different text results based on choices
    - Quizzes that need to calculate scores that show different products

!!! note "Scoring is a Built for Shopify feature"

    Only the `💎Built for Shopify` version of the RevenueHunt app has the scoring system. In every other version a developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

There are three ways to use a score once you have one.

| Method | Use it when |
|---|---|
| [Winning variable quiz](#winning-variable-quiz) | The outcome is a type, such as a skin type or a personality. The variable chosen most often wins |
| [Scoring quiz with one results page](#scoring-quiz-with-one-results-page) | One results page holds a section per outcome, and display logic shows the one that matches the total |
| [Scoring quiz with multiple results pages](#scoring-quiz-with-multiple-results-pages) | Each score range gets its own results page, and jump logic sends the customer there |

## How to add scores or variables to choices

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/hoAcDUqp9u4?si=BW3HNCCZasjFUVal" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A score is a number a choice adds to a running total. A variable is a named bucket, such as `dry skin`, that keeps a total of its own. A choice can carry either, or both.

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add your `Multiple-choice questions`.** For a quiz that works out a skin type, ask about age, skin condition, and so on.

    2. **Open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) of a choice.**

    3. **Find the `Scores and calculations` section.**

    4. **Set the score for that choice with the up and down arrows.** Negative values are allowed.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations.png)

        !!! example "Scoring three choices"

            ![how to add scores or variables to choices](https://loom.com/i/8180f5a1dd8c48a894ac3a6300bd7fe4?workflows_screenshot=true)

            - For choice one, set the score to 1.
            - For choice two, set the score to 2.
            - For choice three, set the score to 3.

    5. **To add a variable, click the `Search or create variable` bar and type its name.** For example `dry skin` or `variable1`.

    6. **Click `Create a new variable` in the dropdown.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations_newvariable](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations_newvariable.png)

    7. **Assign a score to the new variable.**

    8. **Repeat for every choice in the question, then move on to the next question.**

    !!! tip "What to do with the scores and variables"

        - [How to Use Display logic](/how-to-guides/use-display-logic/)
        - [How to Set Up a Personality Type Quiz](#winning-variable-quiz)
        - [How to Set Up a Scoring Quiz](#scoring-quiz-with-one-results-page)

=== "Shopify (Legacy)"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "WooCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Magento"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

## Winning variable quiz

Give each choice a variable instead of a plain score. The variable with the highest total decides the outcome, and Display Logic shows the section that matches it.

![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_variablequiz.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Frn5srnYSkY?si=vbLbqtfXjzSC7yna" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The example below is a quiz for a skin care brand that works out the customer's skin type.

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add your `Multiple-choice questions` about the customer's skin condition.** For example: itchiness, tightness or dryness.

    2. **Assign a variable to every choice in the [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

        !!! tip "Adding the scores"

            See [How to Add Scores or Variables to Choices](#how-to-add-scores-or-variables-to-choices).

        !!! example "Two questions, five variables"

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

    3. **Add a [Results page](/reference/quiz-builder/results-page/) to your quiz.**

    4. **Add one section per outcome to the results page.**

        !!! example "One section per skin type"

            - Section 1: Dry Skin
            - Section 2: Normal Skin
            - Section 3: Oily Skin
            - Section 4: Combination Skin
            - Section 5: Sensitive Skin

    5. **Add a heading, text and a [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) to each section.**

    6. **Set the `Recommendation system` to `Fixed Recommendations` in the product block settings, then pick the products for that skin type.**

    7. **Add [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) to each section, so that it appears only for its own winning variable.**

        !!! example "One rule per section"

            - If the variable with the highest score is `dry skin`, then Section 1 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `normal skin`, then Section 2 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `oily skin`, then Section 3 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `combination skin`, then Section 4 is **visible**. Otherwise Default visibility is **hidden**.
            - If the variable with the highest score is `sensitive skin`, then Section 5 is **visible**. Otherwise Default visibility is **hidden**.

    8. **Click the top-right `Save` button to update the preview and the live quiz.**

=== "Shopify (Legacy)"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    To recommend products by how many choices the customer picked, see [How to Recommend Products Based on Number of User Choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/).

=== "WooCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    To recommend products by how many choices the customer picked, see [How to Recommend Products Based on Number of User Choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/).

=== "Magento"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    To recommend products by how many choices the customer picked, see [How to Recommend Products Based on Number of User Choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/).

=== "BigCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    To recommend products by how many choices the customer picked, see [How to Recommend Products Based on Number of User Choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/).

=== "Standalone"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

    To recommend products by how many choices the customer picked, see [How to Recommend Products Based on Number of User Choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/).

## Scoring quiz with one results page

Give each choice a number of points. One results page holds a section per outcome, and Display Logic shows the section that matches the total the customer reached.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/byAgOMjzi9A?si=vGZrYCxmNUK_Ool7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! tip "Start from the template"

        The app has a Scoring Quiz template. Go to the [Dashboard](/reference/dashboard/), click `Create Quiz`, then select the `Scoring Quiz` template.

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add your `Multiple-choice questions`.** For a skin care quiz, ask about age, skin type or environment.

    2. **Assign a point value to every choice in the [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

        ![assigning scores to choices](/images/how_to_shopifyv2_scoringquiz_addscore.png)

        !!! tip "Adding the scores"

            See [How to Add Scores or Variables to Choices](#how-to-add-scores-or-variables-to-choices).

        !!! example "Points for each skin type"

            - Dry skin choices: 1 point
            - Normal skin choices: 2 points
            - Oily skin choices: 3 points
            - Combination skin choices: 4 points
            - Sensitive skin choices: 5 points

    3. **Go to the [Results page](/reference/quiz-builder/results-page/) and click `+ Add section`.** Add one section per outcome.

    4. **Add content blocks to each section, describing that skin type and its challenges.**

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Add a `Product Block` to each section, holding the products for that skin type.**

    6. **Set the `Recommendation system` to `Fixed Recommendations` in the [Product block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).**

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    7. **Select a content block and find `Display logic` in the right-hand menu.**

    8. **Click `+ Add condition (OR)`.**

    9. **Choose `The variable with the highest score...` or `The score of the variable...`.** These conditions read the total, rather than one specific answer.

    10. **Set the score range that makes the block visible.**

        ![score-based display logic](/images/how_to_shopifyv2_scoringquiz_displaylogic.png)

        !!! example "A range for each skin type"

            - Dry skin content: total score is between 5 and 7 points
            - Normal skin content: total score is between 8 and 12 points
            - Oily skin content: total score is between 13 and 17 points
            - Combination skin content: total score is between 18 and 22 points
            - Sensitive skin content: total score is between 23 and 25 points

    11. **Repeat for every content block.**

    12. **Click the top-right `Save` button to update the preview and the live quiz.**

=== "Shopify (Legacy)"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "WooCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Magento"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

## Scoring quiz with multiple results pages

Give each choice a number of points, then build one results page per outcome. Jump Logic sends each customer to the page that matches their total.

![how_to_shopify_v2_recommendations_scoring_logic](/images/how_to_shopify_v2_recommendations_scoring_logic.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/aRp9cmo8XLI?si=dlqABFGJMtT4mmnc" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add your `Multiple-choice questions`.** For a skin care quiz, ask about age, skin type or environment.

    2. **Assign a point value to every choice in the [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

        ![assigning scores to choices](/images/how_to_shopifyv2_scoringquiz_addscore.png)

        !!! tip "Adding the scores"

            See [How to Add Scores or Variables to Choices](#how-to-add-scores-or-variables-to-choices).

        !!! example "Points for each skin type"

            - Dry skin choices: 1 point
            - Normal skin choices: 2 points
            - Oily skin choices: 3 points
            - Combination skin choices: 4 points
            - Sensitive skin choices: 5 points

    3. **Go to the [Results page](/reference/quiz-builder/results-page/) section and click `+ Add Results Page`.** Create one results page per outcome.

        ![how_to_shopifyv2_scoringquiz_multiresultspages](/images/how_to_shopifyv2_scoringquiz_multiresultspages.png)

        !!! example "One results page per skin type"

            - Results page 1: Dry Skin Routine
            - Results page 2: Normal Skin Routine
            - Results page 3: Oily Skin Routine
            - Results page 4: Combination Skin Routine
            - Results page 5: Sensitive Skin Routine

    4. **Add the text for that outcome to each results page.**

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Add a product block to each results page, holding the products for that skin type.**

    6. **Set the `Recommendation system` to `Fixed Recommendations` in the [Product block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).**

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    7. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) section and open the [Jump logic settings](/reference/quiz-builder/conditional-logic/#jump-logic) of the last question.**

    8. **Click `+ Add condition (OR)`.**

    9. **Select `The variable with the highest score...` or `The score of the variable...`.**

    10. **Set the score range that sends the customer to one results page.**

        ![how_to_shopifyv2_scoringquiz_multiresultspages_logic](/images/how_to_shopifyv2_scoringquiz_multiresultspages_logic.png)

        !!! example "A range for each results page"

            - A total between 5 and 7 points jumps to Dry Skin Routine
            - A total between 8 and 12 points jumps to Normal Skin Routine
            - A total between 13 and 17 points jumps to Oily Skin Routine
            - A total between 18 and 22 points jumps to Combination Skin Routine
            - A total between 23 and 25 points jumps to Sensitive Skin Routine

    11. **Repeat for every results page.**

    12. **Click the top-right `Save` button to update the preview and the live quiz.**

=== "Shopify (Legacy)"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "WooCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Magento"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "BigCommerce"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

=== "Standalone"

    The scoring system is not available in this version of the app. A developer can build one with custom JavaScript on the Results Page. See [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

---