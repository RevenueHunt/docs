---
description: "Step-by-step guide to using display logic in RevenueHunt to show/hide results page content."
icon: material/eye-check-outline
---

# How to Use Display Logic

[Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) shows or hides part of the [results page](/reference/quiz-builder/results-page/), from what the customer answered.

You build one results page that holds the content for every outcome. Display logic then decides which parts of it each customer sees.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=3YY9lVuHYozbUYVq" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A rule sits on a section, so it controls every block in that section at once.

    !!! info "A rule can read"

        - The answer a customer gave to a question.
        - The score of a variable, in a scoring quiz or a personality-type quiz.
        - The variable with the highest score, in a personality-type quiz.

    This article explains how to write a rule, how to score the choices a rule reads, and works through three examples.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A rule sits on a single block, and it reads the answer the customer gave to a question. Each block carries its own rules.

    This article explains how to write a rule, and works through an example.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A rule sits on a single block, and it reads the answer the customer gave to a question. Each block carries its own rules.

    This article explains how to write a rule, and works through an example.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A rule sits on a single block, and it reads the answer the customer gave to a question. Each block carries its own rules.

    This article explains how to write a rule, and works through an example.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A rule sits on a single block, and it reads the answer the customer gave to a question. Each block carries its own rules.

    This article explains how to write a rule, and works through an example.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=-3_Sv297f8B4-KPi" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A rule sits on a single block, and it reads the answer the customer gave to a question. Each block carries its own rules.

    This article explains how to write a rule, and works through an example.

## Write a display logic rule

=== "Shopify"

    1. **Open the [Results page](/reference/quiz-builder/results-page/) and select the section you want to control.** Add the section first if it does not exist yet.

    2. **Find `Display logic` in the section settings on the right.**

        ![quiz builder results page block menu](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

    3. **Click `+ Add logic condition (OR)`.**

    4. **Pick what the condition reads.** The dropdown offers the response to a question, the score of a variable, or the variable with the highest score.

    5. **Complete the condition and leave the rule set to `THEN section is Visible`.**

    6. **Set `Default visibility` to `Hidden`.** The section then appears only when the rule is true.

    7. **Click the top-right `Save` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Display logic panel"

        | Button | What it does |
        |---|---|
        | `+ Add condition (OR)` | Adds another rule. The section shows when any one rule is true |
        | `+ Add condition (AND)` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Default` | Sets the section to `Shown` or `Hidden` before any rule is true |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

    !!! example "A rule on an answer"

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

        `IF the response to` **Question 4, SKIN TYPE**, `is` **Oily all over**, `THEN section is Visible`. `Default visibility` is `Hidden`.

        The section appears for customers who chose `Oily all over`, and stays hidden for everyone else.

    !!! example "A rule on the score of a variable"

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_scorerange](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_scorerange.png)

        `IF the score of the variable` **dry** `is greater than or equal to` **5**, `AND IF the score of the variable` **dry** `is less than or equal to` **7**, `THEN section is Visible`.

        The section appears for a `dry` score of 5, 6 or 7, and stays hidden otherwise.

    !!! example "A rule on the winning variable"

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_winningvariable](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic_winningvariable.png)

        `IF the variable with the highest score` `is` **dry**, `THEN section is Visible`.

        The section appears for customers whose highest score is `dry`, and stays hidden otherwise.

    !!! note "Where the scores come from"

        A score belongs to a choice. You set it in the [Questions](/reference/quiz-builder/questions/) tab, under [Choice settings](/reference/quiz-builder/questions/#choice-settings). See [Add scores and variables to choices](#add-scores-and-variables-to-choices).

=== "Shopify (Legacy)"

    1. **Open the Results Page and select the block you want to control.** Add the block first if it does not exist yet.

    2. **Click the `conditional logic / tree icon` button in the block menu.**

        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

    3. **Click `add Display Logic`.**

        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    4. **Pick the question the rule reads, under `IF response to`.**

    5. **Pick `is` or `is not`, then pick the choice.**

    6. **Set `THEN block is` to `Visible`.**

    7. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Display Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule. The block shows when any one rule is true |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

    !!! example "A rule on an answer"

        ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

        `IF response to` **Question 1, Who are you shopping for?**, `is` **A gift**, `THEN block is Visible`. `IN ALL OTHER CASES this block is` `Hidden`.

        The block appears for customers who chose `A gift`, and stays hidden for everyone else.

=== "WooCommerce"

    1. **Open the Results Page and select the block you want to control.** Add the block first if it does not exist yet.

    2. **Click the `conditional logic / tree icon` button in the block menu.**

        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

    3. **Click `add Display Logic`.**

        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    4. **Pick the question the rule reads, under `IF response to`.**

    5. **Pick `is` or `is not`, then pick the choice.**

    6. **Set `THEN block is` to `Visible`.**

    7. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Display Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule. The block shows when any one rule is true |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

    !!! example "A rule on an answer"

        ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

        `IF response to` **Question 1, Who are you shopping for?**, `is` **A gift**, `THEN block is Visible`. `IN ALL OTHER CASES this block is` `Hidden`.

        The block appears for customers who chose `A gift`, and stays hidden for everyone else.

=== "Magento"

    1. **Open the Results Page and select the block you want to control.** Add the block first if it does not exist yet.

    2. **Click the `conditional logic / tree icon` button in the block menu.**

        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

    3. **Click `add Display Logic`.**

        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    4. **Pick the question the rule reads, under `IF response to`.**

    5. **Pick `is` or `is not`, then pick the choice.**

    6. **Set `THEN block is` to `Visible`.**

    7. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Display Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule. The block shows when any one rule is true |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

    !!! example "A rule on an answer"

        ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

        `IF response to` **Question 1, Who are you shopping for?**, `is` **A gift**, `THEN block is Visible`. `IN ALL OTHER CASES this block is` `Hidden`.

        The block appears for customers who chose `A gift`, and stays hidden for everyone else.

=== "BigCommerce"

    1. **Open the Results Page and select the block you want to control.** Add the block first if it does not exist yet.

    2. **Click the `conditional logic / tree icon` button in the block menu.**

        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

    3. **Click `add Display Logic`.**

        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    4. **Pick the question the rule reads, under `IF response to`.**

    5. **Pick `is` or `is not`, then pick the choice.**

    6. **Set `THEN block is` to `Visible`.**

    7. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Display Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule. The block shows when any one rule is true |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

    !!! example "A rule on an answer"

        ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

        `IF response to` **Question 1, Who are you shopping for?**, `is` **A gift**, `THEN block is Visible`. `IN ALL OTHER CASES this block is` `Hidden`.

        The block appears for customers who chose `A gift`, and stays hidden for everyone else.

=== "Standalone"

    1. **Open the Results Page and select the block you want to control.** Add the block first if it does not exist yet.

    2. **Click the `conditional logic / tree icon` button in the block menu.**

        ![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

    3. **Click `add Display Logic`.**

        ![quiz builder results page display logic](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic.png)

    4. **Pick the question the rule reads, under `IF response to`.**

    5. **Pick `is` or `is not`, then pick the choice.**

    6. **Set `THEN block is` to `Visible`.**

    7. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Display Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule. The block shows when any one rule is true |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

    !!! example "A rule on an answer"

        ![quiz builder results page display logic example](/images/manual_quizbuilder_resultspage_blockmenu_displaylogic_example.png)

        `IF response to` **Question 1, Who are you shopping for?**, `is` **A gift**, `THEN block is Visible`. `IN ALL OTHER CASES this block is` `Hidden`.

        The block appears for customers who chose `A gift`, and stays hidden for everyone else.

## Add scores and variables to choices

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=EoRzoYJ04e48VsJu&amp;start=96" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A variable turns the choices a customer makes into a number. Display logic reads that number, which is how a scoring quiz and a personality-type quiz work.

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add the `Multiple-choice questions` your quiz needs.** For a skin type quiz, ask about age, skin condition and concerns.

    2. **Click a choice to open its [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

    3. **Find the `Scores and calculations` section.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations.png)

    4. **Set the value of the built-in `score` variable with the up and down arrows.** Negative values are allowed.

        !!! example "Scoring one question"

            ![how to add scores or variables to choices](https://loom.com/i/8180f5a1dd8c48a894ac3a6300bd7fe4?workflows_screenshot=true)

            The first choice scores 1, the second scores 2, and the third scores 3.

    5. **To add a variable of your own, type its name in the `Search or create variable` bar.** For example `dry skin` or `variable1`.

    6. **Click `Create a new variable "xxx"` in the dropdown below the bar.**

        ![how to add scores or variables to choices](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_scoresandcalculations_newvariable.png)

    7. **Give the new variable a score on this choice.**

    8. **Repeat for every choice in the question, then move on to the next question.**

    !!! tip "Quizzes built on scores"

        - [How to Set Up a Personality Type Quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz)
        - [How to Set Up a Scoring Quiz](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page)

=== "Shopify (Legacy)"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "WooCommerce"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "Magento"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "BigCommerce"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "Standalone"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

## Examples

### Show content from an answer

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=w8QWpvi3Ga5dbtxl&amp;start=11" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type in question 4, and the results page holds one section per type: dry, normal, oily and combination. Without display logic, all four appear at once.

    1. **Add one section per skin type to the [Results page](/reference/quiz-builder/results-page/).** Give each one its own heading, text and product block.

    2. **Select the dry skin section and find `Display logic`.**

    3. **Click `+ Add logic condition (OR)`.**

    4. **Set the rule to `IF the response to` the skin type question `is` the dry skin choice.**

    5. **Leave `THEN section is Visible` and set `Default visibility` to `Hidden`.**

        ![display logic example](/images/how_to_shopifyv2_use_display_logic_based_on_answers_example1.png)

    6. **Repeat for the other three sections, each on its own choice.**

        | Section | Shown when the answer is |
        |---|---|
        | Normal skin | not too oily and not too dry |
        | Oily skin | oily all over |
        | Combination skin | oily in certain spots |

    7. **Click `Save`, then preview the quiz and answer it once per skin type.** Only the matching section should appear each time.

    !!! tip "Rules that read more than one answer"

        A section can react to several answers. Show it when the skin type is `dry and tight` OR the age group is `teens`. Or show it only when the skin type is `dry and tight` AND the concerns include `acne`.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and the Results Page holds one content block per type: dry, normal, oily and combination. Without Display Logic, all four appear at once.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Go to the Results Page, click the `+` sign and select `Content Block`.**

    3. **Write the text for one skin type in that block.**

        !!! example "Four blocks, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

        !!! tip "Make the heading stand out"

            Put a `#` in front of a line to turn it into a heading. See [How to Use Markdown](/how-to-guides/use-markdown/) for the rest of the formatting.

    4. **Repeat for every skin type, one content block each.**

    5. **Select the first content block, click `display logic`, then click `add display logic`.**

    6. **Set the rule to `IF response to` the skin type question `is` that block's own skin type.**

    7. **Set `THEN block is` to `Visible`, and `IN ALL OTHER CASES this block is` to `Hidden`.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    8. **Repeat for every block.**

    9. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and the Results Page holds one content block per type: dry, normal, oily and combination. Without Display Logic, all four appear at once.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Go to the Results Page, click the `+` sign and select `Content Block`.**

    3. **Write the text for one skin type in that block.**

        !!! example "Four blocks, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

        !!! tip "Make the heading stand out"

            Put a `#` in front of a line to turn it into a heading. See [How to Use Markdown](/how-to-guides/use-markdown/) for the rest of the formatting.

    4. **Repeat for every skin type, one content block each.**

    5. **Select the first content block, click `display logic`, then click `add display logic`.**

    6. **Set the rule to `IF response to` the skin type question `is` that block's own skin type.**

    7. **Set `THEN block is` to `Visible`, and `IN ALL OTHER CASES this block is` to `Hidden`.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    8. **Repeat for every block.**

    9. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and the Results Page holds one content block per type: dry, normal, oily and combination. Without Display Logic, all four appear at once.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Go to the Results Page, click the `+` sign and select `Content Block`.**

    3. **Write the text for one skin type in that block.**

        !!! example "Four blocks, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

        !!! tip "Make the heading stand out"

            Put a `#` in front of a line to turn it into a heading. See [How to Use Markdown](/how-to-guides/use-markdown/) for the rest of the formatting.

    4. **Repeat for every skin type, one content block each.**

    5. **Select the first content block, click `display logic`, then click `add display logic`.**

    6. **Set the rule to `IF response to` the skin type question `is` that block's own skin type.**

    7. **Set `THEN block is` to `Visible`, and `IN ALL OTHER CASES this block is` to `Hidden`.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    8. **Repeat for every block.**

    9. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and the Results Page holds one content block per type: dry, normal, oily and combination. Without Display Logic, all four appear at once.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Go to the Results Page, click the `+` sign and select `Content Block`.**

    3. **Write the text for one skin type in that block.**

        !!! example "Four blocks, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

        !!! tip "Make the heading stand out"

            Put a `#` in front of a line to turn it into a heading. See [How to Use Markdown](/how-to-guides/use-markdown/) for the rest of the formatting.

    4. **Repeat for every skin type, one content block each.**

    5. **Select the first content block, click `display logic`, then click `add display logic`.**

    6. **Set the rule to `IF response to` the skin type question `is` that block's own skin type.**

    7. **Set `THEN block is` to `Visible`, and `IN ALL OTHER CASES this block is` to `Hidden`.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    8. **Repeat for every block.**

    9. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and the Results Page holds one content block per type: dry, normal, oily and combination. Without Display Logic, all four appear at once.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Go to the Results Page, click the `+` sign and select `Content Block`.**

    3. **Write the text for one skin type in that block.**

        !!! example "Four blocks, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

        !!! tip "Make the heading stand out"

            Put a `#` in front of a line to turn it into a heading. See [How to Use Markdown](/how-to-guides/use-markdown/) for the rest of the formatting.

    4. **Repeat for every skin type, one content block each.**

    5. **Select the first content block, click `display logic`, then click `add display logic`.**

    6. **Set the rule to `IF response to` the skin type question `is` that block's own skin type.**

    7. **Set `THEN block is` to `Visible`, and `IN ALL OTHER CASES this block is` to `Hidden`.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    8. **Repeat for every block.**

    9. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

### Show content from the winning variable

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=G0PM__FcEyQJDtBp&amp;start=189" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A personality-type or dosha quiz sorts the customer into one type. Five questions carry five choices each, and every choice adds a point to one skin type variable.

    - Dry skin: `dry +1`
    - Normal skin: `normal +1`
    - Oily skin: `oily +1`
    - Combination skin: `combination +1`
    - Sensitive skin: `sensitive +1`

    ![how to shopifyv2 use display logic based on variable example1 scores](/images/how_to_shopifyv2_use_display_logic_based_on_variable_example1_scores.png)

    The variable with the most points at the end is the customer's skin type.

    1. **Give every choice its variable and score in [Choice settings](/reference/quiz-builder/questions/#choice-settings).** See [Add scores and variables to choices](#add-scores-and-variables-to-choices).

    2. **Add one section per skin type to the [Results page](/reference/quiz-builder/results-page/).** Each holds a heading, text and a [product block](/reference/quiz-builder/results-page/#product-product-variants-collections).

    3. **Decide how each product block picks its products.**

        !!! info "Two recommendation systems"

            - **Fixed Recommendations** show the products you select for that section, whatever the customer answered. This suits a personality-type quiz.
            - **Dynamic Recommendations** rank the products by the upvotes you set in the choice settings.

            Set this in `Recommendation system`, in the [Product Block Settings](/reference/quiz-builder/results-page/#product-product-variants-collections).

    4. **Open `Display Logic` on the dry skin section and click `+ Add condition (OR)`.**

    5. **Set the rule to `IF the variable with the highest score` `is` `dry`.**

    6. **Leave `THEN this section is VISIBLE` and set `Default visibility` to `Hidden`.**

        ![how to shopifyv2 use display logic based on variable example1 display logic](/images/how_to_shopifyv2_use_display_logic_based_on_variable_example1.png)

    7. **Repeat for the other four sections, one variable each.**

        | Section | Shown when the highest score is |
        |---|---|
        | Normal skin | `normal` |
        | Oily skin | `oily` |
        | Combination skin | `combination` |
        | Sensitive skin | `sensitive` |

    8. **Click `Save`, then preview the quiz and answer it as one clear type.** Answer mostly dry, and only the dry skin section should appear.

=== "Shopify (Legacy)"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "WooCommerce"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "Magento"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "BigCommerce"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "Standalone"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

### Show content from a score

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=JG9rNnYpv1aqcdvO&amp;start=269" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A scoring quiz adds the choices up into one number, and each band of the total gets its own section. Five questions carry five choices each, worth 1 to 5 points.

    - First choice: 1 point
    - Second choice: 2 points
    - Third choice: 3 points
    - Fourth choice: 4 points
    - Fifth choice: 5 points

    ![how_to_shopifyv2_use_display_logic_based_on_score_example1](/images/how_to_shopifyv2_use_display_logic_based_on_score_example1.png)

    The total runs from 5 to 25, and the band it lands in is the customer's skin type.

    1. **Give every choice its points in [Choice settings](/reference/quiz-builder/questions/#choice-settings).** See [Add scores and variables to choices](#add-scores-and-variables-to-choices).

    2. **Add one section per band to the [Results page](/reference/quiz-builder/results-page/).** Each holds a heading, text and a [product block](/reference/quiz-builder/results-page/#product-product-variants-collections).

    3. **Decide how each product block picks its products.**

        !!! info "Two recommendation systems"

            - **Fixed Recommendations** show the products you select for that section, whatever the customer answered. This suits a personality-type quiz.
            - **Dynamic Recommendations** rank the products by the upvotes you set in the choice settings.

            Set this in `Recommendation system`, in the [Product Block Settings](/reference/quiz-builder/results-page/#product-product-variants-collections).

    4. **Open `Display Logic` on the dry skin section and click `+ Add condition (OR)`.**

    5. **Set the first test to `IF the score of a variable` `score` `is greater than or equal to` `5`.**

    6. **Click `+ Add condition (AND)`, then set the second test to `is less than or equal to` `7`.**

    7. **Leave `THEN this section is VISIBLE` and set `Default visibility` to `Hidden`.**

        ![how_to_shopifyv2_use_display_logic_based_on_score_example1_logic](/images/how_to_shopifyv2_use_display_logic_based_on_score_example1_logic.png)

    8. **Repeat for the other four bands.**

        | Section | Shown when |
        |---|---|
        | Dry skin | `score >= 5 && score <= 7` |
        | Normal skin | `score >= 8 && score <= 12` |
        | Oily skin | `score >= 13 && score <= 17` |
        | Combination skin | `score >= 18 && score <= 22` |
        | Sensitive skin | `score >= 23 && score <= 25` |

    9. **Click `Save`, then preview the quiz and answer it to land in each band.** Only the matching section should appear each time.

    !!! warning "Leave no gap between the bands"

        Every possible total needs a band, or a customer lands on a results page with nothing on it. Run the lowest band down to the lowest score the quiz can produce, and the highest band up to the highest.

=== "Shopify (Legacy)"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "WooCommerce"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "Magento"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "BigCommerce"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

=== "Standalone"

    !!! note "Scores are not part of this version"

        A quiz here cannot hold a score or a variable, so a rule can only read an answer.

        To sort customers into types or score bands, add [custom JavaScript](/how-to-guides/add-javascript/) to the Results Page. The quiz response carries every answer the customer gave, so a developer can count them and show the right content.

## Additional resources

Read up on boolean logic before writing complex AND/OR rules. [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) evaluates a rule you type in, and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) explains how AND and OR combine.

See [How to Use Conditional Logic](/how-to-guides/use-conditional-logic/) for the logic that runs inside the quiz itself, rather than on the results page.

---

This article explains how to write display logic rules, and works through the answer, variable and score examples.