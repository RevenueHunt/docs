---
icon: material/lightbulb-question
description: "Learn how to display custom explanations for why products were recommended in RevenueHunt."
---

# How to Show Results Explanation

The [recommendation algorithm](/how-to-guides/recommend-products/) picks the products. It does not explain **why** it picked them, and it does not change the results page text to match them.

Writing that explanation is your job, and how you do it depends on the version of the app.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=fSucoCguqxHBr3j8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This version builds the explanation out of results page sections.

    - Add one section per outcome, each with its own text and its own product recommendations.
    - Give every section a [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) rule that decides when it appears, from an answer, a variable or a score.

    That makes a **personality-type** or **Dosha** quiz straightforward to build here.

    !!! info "Where to read the setup"

        - [How to use display logic](/how-to-guides/use-display-logic/) covers showing and hiding sections.
        - [Winning variable quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) decides the outcome from the variable chosen most often.
        - [Scoring quiz with one results page](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page) decides it from a total score.

        The last two are the usual routes to a personality-type quiz.

    There are other ways to explain a recommendation, and some need much less setup.

    - **Content Dynamic Source.** [A Content Dynamic Source](/how-to-guides/use-information-recalls/) pulls any answer the customer gave into a `Text Block` or a `Heading Block`. One block then adapts to everyone who takes the quiz. A single line such as *"Your dry, sensitive skin needs..."* can stand in for a section per outcome. That removes most of the display logic you would otherwise write.

    - **Product descriptions.** Add a `Description` component to the product slot, under `Product components layout`. The text comes straight from your Shopify catalog, so the reason lives with the product rather than in the quiz.

    - **Metafields.** A `Metafield` component shows a custom product field. A short "why this suits you" note kept on the product in Shopify reaches the results page without any quiz logic at all.

    - **Custom JavaScript.** A developer can write the text from the recommended product ID, or from a score. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note "No linear scoring in this version"

        The legacy version of the RevenueHunt app has no linear score. A choice cannot add one point to a running total that then picks a results page.

        That makes a **personality-type** quiz hard to build here. The results page has to carry the explanation instead, and there are four ways to put it there.

    - **Information Recall.** [Information Recall, or Content Dynamic Source](/how-to-guides/use-information-recalls/), pulls a customer's own answer into a content block on the Results Page. It explains the recommendation in the customer's own words, with no logic and no code.

    - **Display Logic.** [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) shows or hides text on the Results Page from the answers. It suits a short, simple quiz. See [how to use display logic](/how-to-guides/use-display-logic/).

        ??? question "A worked personality-type quiz"

            Say the quiz works out a customer's skin type.

            1. **Ask about oiliness.** "How does your skin usually feel by the middle of the day?"

                - Very oily, shiny all over *(oily skin)*
                - Oily in the T-zone, but dry elsewhere *(combination skin)*
                - Balanced, not too oily or dry *(normal skin)*
                - Dry and tight all over *(dry skin)*

            2. **Ask about sensitivity.** "How does your skin react to new products or environmental changes?"

                - Easily irritated, red or itchy *(sensitive skin)*
                - Rarely reacts, even to strong products *(normal or oily skin)*
                - Reacts sometimes, but not consistently *(combination skin)*

            3. **Ask about hydration.** "Does your skin often feel dehydrated, whatever its oiliness?"

                - Yes, it feels tight and flaky *(dry or dehydrated skin)*
                - Sometimes, especially in colder months *(combination or normal skin)*
                - Rarely or never *(oily skin)*

            4. **Link products to every choice.** Answers that point at dry skin link to the products for dry skin, and so on. The [recommendation algorithm](/how-to-guides/recommend-products/) then handles the products on its own.

            5. **Add one content block per skin type to the Results Page.** One saying *You have Dry Skin*, one *You have Oily Skin*, and so on.

                ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            6. **Give each block a [Display Logic](/how-to-guides/use-display-logic/) rule that makes it visible for its own answers.**

                !!! example "The rule for dry skin"

                    Question 1 is *Dry and tight all over*, **AND** Question 2 is *Easily irritated, red, or itchy*, **AND** Question 3 is *Yes, it feels tight and flaky*.

                    The block is then **Visible**. Otherwise it stays hidden.

                ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            7. **Add a rule for every route to an outcome.** Some outcomes are reached several ways, so they need several rules joined with **OR**.

                !!! example "Combination skin, reached three ways"

                    Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Reacts sometimes*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Very oily, shiny all over*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, but not consistently*.

                ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)

                ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)

                ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)

            8. **Repeat until every content block has its rules.**

                !!! warning "Every combination needs a rule"

                    This method asks you to predict every route a customer can take. A combination with no rule shows no text.

            !!! tip "If the combinations get out of hand"

                - Base the logic on one question rather than all three.
                - Use custom JavaScript to work the skin type out, and write the text from there.

        !!! tip "For a longer quiz, write the logic in code"

            Once a quiz has many questions, the custom JavaScript route below is easier to maintain than a rule per combination.

    - **Custom JavaScript.** A developer can write a function that shows text chosen by the ID of the recommended product. They can also add custom values to choices and build a scoring system, then write the matching text to the results page. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

    - **Product descriptions.** Put the reason in the product description itself. The app pulls descriptions from your store, and you control them in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings` > `Show description`, where they can also be truncated.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note "No linear scoring in this version"

        This version of the RevenueHunt app has no linear score yet. A choice cannot add one point to a running total that then picks a results page.

        That makes a **personality-type** quiz hard to build here. The results page has to carry the explanation instead, and there are four ways to put it there.

    - **Information Recall.** [Information Recall, or Content Dynamic Source](/how-to-guides/use-information-recalls/), pulls a customer's own answer into a content block on the Results Page. It explains the recommendation in the customer's own words, with no logic and no code.

    - **Display Logic.** [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) shows or hides text on the Results Page from the answers. It suits a short, simple quiz. See [how to use display logic](/how-to-guides/use-display-logic/).

        ??? question "A worked personality-type quiz"

            Say the quiz works out a customer's skin type.

            1. **Ask about oiliness.** "How does your skin usually feel by the middle of the day?"

                - Very oily, shiny all over *(oily skin)*
                - Oily in the T-zone, but dry elsewhere *(combination skin)*
                - Balanced, not too oily or dry *(normal skin)*
                - Dry and tight all over *(dry skin)*

            2. **Ask about sensitivity.** "How does your skin react to new products or environmental changes?"

                - Easily irritated, red or itchy *(sensitive skin)*
                - Rarely reacts, even to strong products *(normal or oily skin)*
                - Reacts sometimes, but not consistently *(combination skin)*

            3. **Ask about hydration.** "Does your skin often feel dehydrated, whatever its oiliness?"

                - Yes, it feels tight and flaky *(dry or dehydrated skin)*
                - Sometimes, especially in colder months *(combination or normal skin)*
                - Rarely or never *(oily skin)*

            4. **Link products to every choice.** Answers that point at dry skin link to the products for dry skin, and so on. The [recommendation algorithm](/how-to-guides/recommend-products/) then handles the products on its own.

            5. **Add one content block per skin type to the Results Page.** One saying *You have Dry Skin*, one *You have Oily Skin*, and so on.

                ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            6. **Give each block a [Display Logic](/how-to-guides/use-display-logic/) rule that makes it visible for its own answers.**

                !!! example "The rule for dry skin"

                    Question 1 is *Dry and tight all over*, **AND** Question 2 is *Easily irritated, red, or itchy*, **AND** Question 3 is *Yes, it feels tight and flaky*.

                    The block is then **Visible**. Otherwise it stays hidden.

                ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            7. **Add a rule for every route to an outcome.** Some outcomes are reached several ways, so they need several rules joined with **OR**.

                !!! example "Combination skin, reached three ways"

                    Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Reacts sometimes*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Very oily, shiny all over*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, but not consistently*.

                ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)

                ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)

                ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)

            8. **Repeat until every content block has its rules.**

                !!! warning "Every combination needs a rule"

                    This method asks you to predict every route a customer can take. A combination with no rule shows no text.

            !!! tip "If the combinations get out of hand"

                - Base the logic on one question rather than all three.
                - Use custom JavaScript to work the skin type out, and write the text from there.

        !!! tip "For a longer quiz, write the logic in code"

            Once a quiz has many questions, the custom JavaScript route below is easier to maintain than a rule per combination.

    - **Custom JavaScript.** A developer can write a function that shows text chosen by the ID of the recommended product. They can also add custom values to choices and build a scoring system, then write the matching text to the results page. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

    - **Product descriptions.** Put the reason in the product description itself. The app pulls descriptions from your store, and you control them in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings` > `Show description`, where they can also be truncated.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note "No linear scoring in this version"

        This version of the RevenueHunt app has no linear score yet. A choice cannot add one point to a running total that then picks a results page.

        That makes a **personality-type** quiz hard to build here. The results page has to carry the explanation instead, and there are four ways to put it there.

    - **Information Recall.** [Information Recall, or Content Dynamic Source](/how-to-guides/use-information-recalls/), pulls a customer's own answer into a content block on the Results Page. It explains the recommendation in the customer's own words, with no logic and no code.

    - **Display Logic.** [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) shows or hides text on the Results Page from the answers. It suits a short, simple quiz. See [how to use display logic](/how-to-guides/use-display-logic/).

        ??? question "A worked personality-type quiz"

            Say the quiz works out a customer's skin type.

            1. **Ask about oiliness.** "How does your skin usually feel by the middle of the day?"

                - Very oily, shiny all over *(oily skin)*
                - Oily in the T-zone, but dry elsewhere *(combination skin)*
                - Balanced, not too oily or dry *(normal skin)*
                - Dry and tight all over *(dry skin)*

            2. **Ask about sensitivity.** "How does your skin react to new products or environmental changes?"

                - Easily irritated, red or itchy *(sensitive skin)*
                - Rarely reacts, even to strong products *(normal or oily skin)*
                - Reacts sometimes, but not consistently *(combination skin)*

            3. **Ask about hydration.** "Does your skin often feel dehydrated, whatever its oiliness?"

                - Yes, it feels tight and flaky *(dry or dehydrated skin)*
                - Sometimes, especially in colder months *(combination or normal skin)*
                - Rarely or never *(oily skin)*

            4. **Link products to every choice.** Answers that point at dry skin link to the products for dry skin, and so on. The [recommendation algorithm](/how-to-guides/recommend-products/) then handles the products on its own.

            5. **Add one content block per skin type to the Results Page.** One saying *You have Dry Skin*, one *You have Oily Skin*, and so on.

                ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            6. **Give each block a [Display Logic](/how-to-guides/use-display-logic/) rule that makes it visible for its own answers.**

                !!! example "The rule for dry skin"

                    Question 1 is *Dry and tight all over*, **AND** Question 2 is *Easily irritated, red, or itchy*, **AND** Question 3 is *Yes, it feels tight and flaky*.

                    The block is then **Visible**. Otherwise it stays hidden.

                ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            7. **Add a rule for every route to an outcome.** Some outcomes are reached several ways, so they need several rules joined with **OR**.

                !!! example "Combination skin, reached three ways"

                    Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Reacts sometimes*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Very oily, shiny all over*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, but not consistently*.

                ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)

                ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)

                ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)

            8. **Repeat until every content block has its rules.**

                !!! warning "Every combination needs a rule"

                    This method asks you to predict every route a customer can take. A combination with no rule shows no text.

            !!! tip "If the combinations get out of hand"

                - Base the logic on one question rather than all three.
                - Use custom JavaScript to work the skin type out, and write the text from there.

        !!! tip "For a longer quiz, write the logic in code"

            Once a quiz has many questions, the custom JavaScript route below is easier to maintain than a rule per combination.

    - **Custom JavaScript.** A developer can write a function that shows text chosen by the ID of the recommended product. They can also add custom values to choices and build a scoring system, then write the matching text to the results page. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

    - **Product descriptions.** Put the reason in the product description itself. The app pulls descriptions from your store, and you control them in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings` > `Show description`, where they can also be truncated.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note "No linear scoring in this version"

        This version of the RevenueHunt app has no linear score yet. A choice cannot add one point to a running total that then picks a results page.

        That makes a **personality-type** quiz hard to build here. The results page has to carry the explanation instead, and there are four ways to put it there.

    - **Information Recall.** [Information Recall, or Content Dynamic Source](/how-to-guides/use-information-recalls/), pulls a customer's own answer into a content block on the Results Page. It explains the recommendation in the customer's own words, with no logic and no code.

    - **Display Logic.** [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) shows or hides text on the Results Page from the answers. It suits a short, simple quiz. See [how to use display logic](/how-to-guides/use-display-logic/).

        ??? question "A worked personality-type quiz"

            Say the quiz works out a customer's skin type.

            1. **Ask about oiliness.** "How does your skin usually feel by the middle of the day?"

                - Very oily, shiny all over *(oily skin)*
                - Oily in the T-zone, but dry elsewhere *(combination skin)*
                - Balanced, not too oily or dry *(normal skin)*
                - Dry and tight all over *(dry skin)*

            2. **Ask about sensitivity.** "How does your skin react to new products or environmental changes?"

                - Easily irritated, red or itchy *(sensitive skin)*
                - Rarely reacts, even to strong products *(normal or oily skin)*
                - Reacts sometimes, but not consistently *(combination skin)*

            3. **Ask about hydration.** "Does your skin often feel dehydrated, whatever its oiliness?"

                - Yes, it feels tight and flaky *(dry or dehydrated skin)*
                - Sometimes, especially in colder months *(combination or normal skin)*
                - Rarely or never *(oily skin)*

            4. **Link products to every choice.** Answers that point at dry skin link to the products for dry skin, and so on. The [recommendation algorithm](/how-to-guides/recommend-products/) then handles the products on its own.

            5. **Add one content block per skin type to the Results Page.** One saying *You have Dry Skin*, one *You have Oily Skin*, and so on.

                ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            6. **Give each block a [Display Logic](/how-to-guides/use-display-logic/) rule that makes it visible for its own answers.**

                !!! example "The rule for dry skin"

                    Question 1 is *Dry and tight all over*, **AND** Question 2 is *Easily irritated, red, or itchy*, **AND** Question 3 is *Yes, it feels tight and flaky*.

                    The block is then **Visible**. Otherwise it stays hidden.

                ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            7. **Add a rule for every route to an outcome.** Some outcomes are reached several ways, so they need several rules joined with **OR**.

                !!! example "Combination skin, reached three ways"

                    Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Reacts sometimes*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Very oily, shiny all over*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, but not consistently*.

                ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)

                ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)

                ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)

            8. **Repeat until every content block has its rules.**

                !!! warning "Every combination needs a rule"

                    This method asks you to predict every route a customer can take. A combination with no rule shows no text.

            !!! tip "If the combinations get out of hand"

                - Base the logic on one question rather than all three.
                - Use custom JavaScript to work the skin type out, and write the text from there.

        !!! tip "For a longer quiz, write the logic in code"

            Once a quiz has many questions, the custom JavaScript route below is easier to maintain than a rule per combination.

    - **Custom JavaScript.** A developer can write a function that shows text chosen by the ID of the recommended product. They can also add custom values to choices and build a scoring system, then write the matching text to the results page. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

    - **Product descriptions.** Put the reason in the product description itself. The app pulls descriptions from your store, and you control them in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings` > `Show description`, where they can also be truncated.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/c4cb6bce39a447cc860f8408adade0f4?sid=967d38f5-9c4b-47b0-b73d-41a2aae156d6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note "No linear scoring in this version"

        This version of the RevenueHunt app has no linear score yet. A choice cannot add one point to a running total that then picks a results page.

        That makes a **personality-type** quiz hard to build here. The results page has to carry the explanation instead, and there are four ways to put it there.

    - **Information Recall.** [Information Recall, or Content Dynamic Source](/how-to-guides/use-information-recalls/), pulls a customer's own answer into a content block on the Results Page. It explains the recommendation in the customer's own words, with no logic and no code.

    - **Display Logic.** [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) shows or hides text on the Results Page from the answers. It suits a short, simple quiz. See [how to use display logic](/how-to-guides/use-display-logic/).

        ??? question "A worked personality-type quiz"

            Say the quiz works out a customer's skin type.

            1. **Ask about oiliness.** "How does your skin usually feel by the middle of the day?"

                - Very oily, shiny all over *(oily skin)*
                - Oily in the T-zone, but dry elsewhere *(combination skin)*
                - Balanced, not too oily or dry *(normal skin)*
                - Dry and tight all over *(dry skin)*

            2. **Ask about sensitivity.** "How does your skin react to new products or environmental changes?"

                - Easily irritated, red or itchy *(sensitive skin)*
                - Rarely reacts, even to strong products *(normal or oily skin)*
                - Reacts sometimes, but not consistently *(combination skin)*

            3. **Ask about hydration.** "Does your skin often feel dehydrated, whatever its oiliness?"

                - Yes, it feels tight and flaky *(dry or dehydrated skin)*
                - Sometimes, especially in colder months *(combination or normal skin)*
                - Rarely or never *(oily skin)*

            4. **Link products to every choice.** Answers that point at dry skin link to the products for dry skin, and so on. The [recommendation algorithm](/how-to-guides/recommend-products/) then handles the products on its own.

            5. **Add one content block per skin type to the Results Page.** One saying *You have Dry Skin*, one *You have Oily Skin*, and so on.

                ![how to show results explenation personalityquiz1](/images/how_to_show_results_explenation_personalityquiz1.png)

            6. **Give each block a [Display Logic](/how-to-guides/use-display-logic/) rule that makes it visible for its own answers.**

                !!! example "The rule for dry skin"

                    Question 1 is *Dry and tight all over*, **AND** Question 2 is *Easily irritated, red, or itchy*, **AND** Question 3 is *Yes, it feels tight and flaky*.

                    The block is then **Visible**. Otherwise it stays hidden.

                ![how to show results explenation personalityquiz2](/images/how_to_show_results_explenation_personalityquiz2.png)

            7. **Add a rule for every route to an outcome.** Some outcomes are reached several ways, so they need several rules joined with **OR**.

                !!! example "Combination skin, reached three ways"

                    Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Reacts sometimes*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Very oily, shiny all over*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, especially in colder months*.

                    **OR** Question 1 is *Oily in the T-zone*, **AND** Question 2 is *Easily irritated*, **AND** Question 3 is *Sometimes, but not consistently*.

                ![how to show results explenation personalityquiz3](/images/how_to_show_results_explenation_personalityquiz3.png)

                ![how to show results explenation personalityquiz4](/images/how_to_show_results_explenation_personalityquiz4.png)

                ![how to show results explenation personalityquiz5](/images/how_to_show_results_explenation_personalityquiz5.png)

            8. **Repeat until every content block has its rules.**

                !!! warning "Every combination needs a rule"

                    This method asks you to predict every route a customer can take. A combination with no rule shows no text.

            !!! tip "If the combinations get out of hand"

                - Base the logic on one question rather than all three.
                - Use custom JavaScript to work the skin type out, and write the text from there.

        !!! tip "For a longer quiz, write the logic in code"

            Once a quiz has many questions, the custom JavaScript route below is easier to maintain than a rule per combination.

    - **Custom JavaScript.** A developer can write a function that shows text chosen by the ID of the recommended product. They can also add custom values to choices and build a scoring system, then write the matching text to the results page. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

    - **Product descriptions.** Put the reason in the product description itself. The app pulls descriptions from your store, and you control them in the [Results Page settings](/reference/quiz-builder/results-page/) under `Individual Product Settings` > `Show description`, where they can also be truncated.

---

This article explains how to show why a certain product was recommended to the customer.