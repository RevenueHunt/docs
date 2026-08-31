---
description: "Step-by-step guide to using skip logic in RevenueHunt to skip questions dynamically."
icon: material/skip-next-outline
---

# How to Use Skip Logic

[Skip logic](/reference/quiz-builder/conditional-logic/#skip-logic) drops a question when the customer's earlier answers have made it irrelevant. The quiz keeps one path, and each customer walks a shorter version of it.

!!! info "Use skip logic to"

    - Skip a question that does not apply to this customer.
    - Show only the follow-up questions that match what the customer selected.

!!! example "What this looks like in a quiz"

    A skincare quiz asks about skin concerns and lets the customer pick several. Only the follow-up questions for the concerns they picked are asked, and the rest are skipped.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=iMGaCLXqTpr8yS0B" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=5vIwsEn0Z5X6_Eeb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

!!! warning "Do not mix skip logic and jump logic in one quiz"

    Each of them rewrites the order of the questions. Together they produce paths that neither rule intended. See [Skip logic and jump logic](#skip-logic-and-jump-logic).

## The conditional logic tab

=== "Shopify"

    ![quiz builder conditional logic](/images/how_to_use_skip_logic_cond_logic_intro.png)

    The [Conditional logic](/reference/quiz-builder/conditional-logic/) tab is where you branch a quiz. Rules go in the menu on the right, and the tree on the left redraws itself as you add them.

    Without a rule, the quiz runs through the questions in order. Every rule you write is an exception to that order.

    ??? question "Moving around the logic tree"

        ![quiz builder conditional logic preview options](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_zoom.png)

        | Control | What it does |
        |---|---|
        | `+` | Zooms in |
        | `-` | Zooms out |
        | `[]` | Centers the tree and fits it to the view |
        | `lock` | Locks the preview, so a stray drag cannot move it |

        Drag the tree with the left mouse button to reach a particular branch.

=== "Shopify (Legacy)"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    The [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab is where you branch a quiz. Rules go in the menu on the left, and the tree on the right redraws itself as you add them.

    Without a rule, the quiz runs through the questions in order. Every rule you write is an exception to that order.

    ??? question "Moving around the logic tree"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        | Control | What it does |
        |---|---|
        | `+` | Zooms in |
        | `-` | Zooms out |
        | `[]` | Centers the tree and fits it to the view |

        Drag the tree with the left mouse button to reach a particular branch.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The arrows in the top menu move you to the question above or the question below.

=== "WooCommerce"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    The [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab is where you branch a quiz. Rules go in the menu on the left, and the tree on the right redraws itself as you add them.

    Without a rule, the quiz runs through the questions in order. Every rule you write is an exception to that order.

    ??? question "Moving around the logic tree"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        | Control | What it does |
        |---|---|
        | `+` | Zooms in |
        | `-` | Zooms out |
        | `[]` | Centers the tree and fits it to the view |

        Drag the tree with the left mouse button to reach a particular branch.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The arrows in the top menu move you to the question above or the question below.

=== "Magento"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    The [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab is where you branch a quiz. Rules go in the menu on the left, and the tree on the right redraws itself as you add them.

    Without a rule, the quiz runs through the questions in order. Every rule you write is an exception to that order.

    ??? question "Moving around the logic tree"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        | Control | What it does |
        |---|---|
        | `+` | Zooms in |
        | `-` | Zooms out |
        | `[]` | Centers the tree and fits it to the view |

        Drag the tree with the left mouse button to reach a particular branch.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The arrows in the top menu move you to the question above or the question below.

=== "BigCommerce"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    The [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab is where you branch a quiz. Rules go in the menu on the left, and the tree on the right redraws itself as you add them.

    Without a rule, the quiz runs through the questions in order. Every rule you write is an exception to that order.

    ??? question "Moving around the logic tree"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        | Control | What it does |
        |---|---|
        | `+` | Zooms in |
        | `-` | Zooms out |
        | `[]` | Centers the tree and fits it to the view |

        Drag the tree with the left mouse button to reach a particular branch.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The arrows in the top menu move you to the question above or the question below.

=== "Standalone"

    ![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

    The [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab is where you branch a quiz. Rules go in the menu on the left, and the tree on the right redraws itself as you add them.

    Without a rule, the quiz runs through the questions in order. Every rule you write is an exception to that order.

    ??? question "Moving around the logic tree"

        ![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

        | Control | What it does |
        |---|---|
        | `+` | Zooms in |
        | `-` | Zooms out |
        | `[]` | Centers the tree and fits it to the view |

        Drag the tree with the left mouse button to reach a particular branch.

        ![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

        The arrows in the top menu move you to the question above or the question below.

## Add a skip logic rule

Every rule reads the same way: **IF** the response to an earlier question **is**, or **is not**, a certain choice, **THEN this question is skipped**. A question carrying no rule is always asked.

=== "Shopify"

    1. **Open the [Quiz builder](/reference/quiz-builder/) and go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question you want to skip.** Pick it from the dropdown at the top of the right-hand menu, or click it on the logic tree.

    3. **Open the [`Skip logic`](/reference/quiz-builder/conditional-logic/#skip-logic) dropdown in the menu on the right.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic.png)

    4. **Click `+ Add another rule (OR)`.**

    5. **Pick the earlier question the rule reads, then pick `is` or `is not` and the choice.**

        !!! example "One rule"

            ![quiz builder conditional logic skip logic rule](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example.png)

            A customer who answers `Too shiny` to Question 9, SKIN CONCERNS, is never asked Question 10, `ALERGIES`.

    6. **Click the top-right `Save` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Skip logic panel"

        | Button | What it does |
        |---|---|
        | `+ Add another rule (OR)` | Adds another rule to the question. Any one of them can skip it |
        | `+ Add concurrent logic (AND)` | Adds a second test to the current rule. Both tests must be true |
        | `...` | Opens the rule menu, where you delete the rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

=== "Shopify (Legacy)"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question you want to skip.**

    2. **Open the [`Skip Logic`](/reference/quiz-builder/conditional-logic/#skip-logic) tab.**

    3. **Click `Add Skip Logic`.**

    4. **Pick the earlier question the rule reads, then pick `is` or `is not` and the choice.**

        !!! example "One rule"

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            A customer who answers `A gift` to Question 1, Who are you shopping for?, is never asked Question 2, What is your skin type?.

    5. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    Every slide carrying a rule is marked `skip logic` in the builder, so you can see which questions are conditional.

    ??? info "The buttons in the Skip Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question. Any one of them can skip it |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

=== "WooCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question you want to skip.**

    2. **Open the [`Skip Logic`](/reference/quiz-builder/conditional-logic/#skip-logic) tab.**

    3. **Click `Add Skip Logic`.**

    4. **Pick the earlier question the rule reads, then pick `is` or `is not` and the choice.**

        !!! example "One rule"

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            A customer who answers `A gift` to Question 1, Who are you shopping for?, is never asked Question 2, What is your skin type?.

    5. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    Every slide carrying a rule is marked `skip logic` in the builder, so you can see which questions are conditional.

    ??? info "The buttons in the Skip Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question. Any one of them can skip it |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

=== "Magento"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question you want to skip.**

    2. **Open the [`Skip Logic`](/reference/quiz-builder/conditional-logic/#skip-logic) tab.**

    3. **Click `Add Skip Logic`.**

    4. **Pick the earlier question the rule reads, then pick `is` or `is not` and the choice.**

        !!! example "One rule"

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            A customer who answers `A gift` to Question 1, Who are you shopping for?, is never asked Question 2, What is your skin type?.

    5. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    Every slide carrying a rule is marked `skip logic` in the builder, so you can see which questions are conditional.

    ??? info "The buttons in the Skip Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question. Any one of them can skip it |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

=== "BigCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question you want to skip.**

    2. **Open the [`Skip Logic`](/reference/quiz-builder/conditional-logic/#skip-logic) tab.**

    3. **Click `Add Skip Logic`.**

    4. **Pick the earlier question the rule reads, then pick `is` or `is not` and the choice.**

        !!! example "One rule"

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            A customer who answers `A gift` to Question 1, Who are you shopping for?, is never asked Question 2, What is your skin type?.

    5. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    Every slide carrying a rule is marked `skip logic` in the builder, so you can see which questions are conditional.

    ??? info "The buttons in the Skip Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question. Any one of them can skip it |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

=== "Standalone"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question you want to skip.**

    2. **Open the [`Skip Logic`](/reference/quiz-builder/conditional-logic/#skip-logic) tab.**

    3. **Click `Add Skip Logic`.**

    4. **Pick the earlier question the rule reads, then pick `is` or `is not` and the choice.**

        !!! example "One rule"

            ![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

            A customer who answers `A gift` to Question 1, Who are you shopping for?, is never asked Question 2, What is your skin type?.

    5. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    Every slide carrying a rule is marked `skip logic` in the builder, so you can see which questions are conditional.

    ??? info "The buttons in the Skip Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question. Any one of them can skip it |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

## Examples

### Show only the statement that matches the answer

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=WauBIBFSMPIlFNtm&amp;start=9" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type in question 4, and carries one statement slide per type. Skip logic hides the three that do not apply.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the dry skin statement.**

    4. **Find `Skip logic` in the menu on the right, and click `+ Add another rule (OR)`.**

    5. **Set the rule to `IF the response to` the skin type question `is not` the dry skin choice.**

        ![how to hide content with logic shopifyv2 skip logic rule](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_rule.png)

        The statement is then skipped for every answer except that one.

    6. **Repeat for the other three statements, each reading its own choice.**

    7. **Click the top-right `Save` button, then answer the quiz once per skin type.** Only the matching statement should appear each time.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and carries one statement slide per type. Skip Logic hides the three that do not apply.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the dry skin statement.**

    4. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is not` the dry skin choice.**

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

        The statement is then skipped for every answer except that one.

    6. **Repeat for the other three statements, each reading its own choice.**

    7. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching statement should appear each time.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and carries one statement slide per type. Skip Logic hides the three that do not apply.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the dry skin statement.**

    4. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is not` the dry skin choice.**

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

        The statement is then skipped for every answer except that one.

    6. **Repeat for the other three statements, each reading its own choice.**

    7. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching statement should appear each time.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and carries one statement slide per type. Skip Logic hides the three that do not apply.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the dry skin statement.**

    4. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is not` the dry skin choice.**

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

        The statement is then skipped for every answer except that one.

    6. **Repeat for the other three statements, each reading its own choice.**

    7. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching statement should appear each time.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and carries one statement slide per type. Skip Logic hides the three that do not apply.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the dry skin statement.**

    4. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is not` the dry skin choice.**

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

        The statement is then skipped for every answer except that one.

    6. **Repeat for the other three statements, each reading its own choice.**

    7. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching statement should appear each time.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, and carries one statement slide per type. Skip Logic hides the three that do not apply.

    ![how to use skip logic example](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the dry skin statement.**

    4. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is not` the dry skin choice.**

        ![how to hide content with logic skip logic statement](/images/how_to_hide_content_with_logic_skip_logic_statement.png)

        The statement is then skipped for every answer except that one.

    6. **Repeat for the other three statements, each reading its own choice.**

    7. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching statement should appear each time.

### Ask only the follow-up questions the customer needs

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=8mMuIlNk_TnNkKnD&amp;start=62" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A beauty quiz lets the customer pick several skin concerns at once, then asks a follow-up question about each concern they picked.

    1. **Add a multiple-choice question and allow several selections.** The setting sits in the [Multiple Choice block settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Add one follow-up question per choice, in the same order as the choices.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_skiplogic_example](/images/how_to_shopifyV2_skiplogic_example_logic_multipleselection_questions.png)

        !!! warning "Keep the two lists in the same order"

            A follow-up question has to sit in the same position as its choice. If `Acne` is the first choice, its follow-up has to be the first follow-up question.

    3. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the first follow-up question.**

    4. **Set the rule to `IF the response to` the concerns question `is not` that question's own concern.**

        !!! example "The acne follow-up"

            `IF the response to the question Q9: Skin Concerns is not acne, then this question is skipped.`

            ![how_to_shopifyV2_skiplogic_example_logic_rule_multipleselection](/images/how_to_shopifyV2_skiplogic_example_logic_rule_multipleselection.png)

    5. **Repeat for every other follow-up question.**

    6. **Click the top-right `Save` button, then answer the quiz picking two concerns.** Only the follow-up questions for those two should appear.

    !!! tip "Why the rule reads `is not`"

        A rule phrased as `is not` skips the question for everyone who did not pick that choice, and shows it to everyone who did. The quiz keeps one straight path, however many choices the customer makes.

=== "Shopify (Legacy)"

    A beauty quiz lets the customer pick several areas to focus on at once, then asks the follow-up questions for each area they picked.

    1. **Add a question asking which areas the customer wants to focus on.** For example nails, skin, hair and makeup.

        !!! tip "Allow several selections"

            The setting sits in [block settings, multiple-choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Add the follow-up questions for each area, grouped together and in the order of the choices.**

        | Questions | Area |
        |---|---|
        | 2 and 3 | Nails |
        | 4 and 5 | Skin |
        | 6 and 7 | Hair |
        | 8 and 9 | Makeup |

    3. **Add a skip logic rule to every follow-up question, reading its own area.**

        !!! example "The nail questions"

            `IF response to Question 1 is not Nails, then this question is skipped.`

        Questions 4 and 5 read `Skin`, questions 6 and 7 read `Hair`, and questions 8 and 9 read `Makeup`.

    4. **Click the top-right `Publish` button, then answer the quiz picking two areas.** Only the questions for those two areas should appear.

    !!! tip "Why the rule reads `is not`"

        A rule phrased as `is not` skips the question for everyone who did not pick that choice, and shows it to everyone who did. The quiz keeps one straight path, however many choices the customer makes.

=== "WooCommerce"

    A beauty quiz lets the customer pick several areas to focus on at once, then asks the follow-up questions for each area they picked.

    1. **Add a question asking which areas the customer wants to focus on.** For example nails, skin, hair and makeup.

        !!! tip "Allow several selections"

            The setting sits in [block settings, multiple-choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Add the follow-up questions for each area, grouped together and in the order of the choices.**

        | Questions | Area |
        |---|---|
        | 2 and 3 | Nails |
        | 4 and 5 | Skin |
        | 6 and 7 | Hair |
        | 8 and 9 | Makeup |

    3. **Add a skip logic rule to every follow-up question, reading its own area.**

        !!! example "The nail questions"

            `IF response to Question 1 is not Nails, then this question is skipped.`

        Questions 4 and 5 read `Skin`, questions 6 and 7 read `Hair`, and questions 8 and 9 read `Makeup`.

    4. **Click the top-right `Publish` button, then answer the quiz picking two areas.** Only the questions for those two areas should appear.

    !!! tip "Why the rule reads `is not`"

        A rule phrased as `is not` skips the question for everyone who did not pick that choice, and shows it to everyone who did. The quiz keeps one straight path, however many choices the customer makes.

=== "Magento"

    A beauty quiz lets the customer pick several areas to focus on at once, then asks the follow-up questions for each area they picked.

    1. **Add a question asking which areas the customer wants to focus on.** For example nails, skin, hair and makeup.

        !!! tip "Allow several selections"

            The setting sits in [block settings, multiple-choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Add the follow-up questions for each area, grouped together and in the order of the choices.**

        | Questions | Area |
        |---|---|
        | 2 and 3 | Nails |
        | 4 and 5 | Skin |
        | 6 and 7 | Hair |
        | 8 and 9 | Makeup |

    3. **Add a skip logic rule to every follow-up question, reading its own area.**

        !!! example "The nail questions"

            `IF response to Question 1 is not Nails, then this question is skipped.`

        Questions 4 and 5 read `Skin`, questions 6 and 7 read `Hair`, and questions 8 and 9 read `Makeup`.

    4. **Click the top-right `Publish` button, then answer the quiz picking two areas.** Only the questions for those two areas should appear.

    !!! tip "Why the rule reads `is not`"

        A rule phrased as `is not` skips the question for everyone who did not pick that choice, and shows it to everyone who did. The quiz keeps one straight path, however many choices the customer makes.

=== "BigCommerce"

    A beauty quiz lets the customer pick several areas to focus on at once, then asks the follow-up questions for each area they picked.

    1. **Add a question asking which areas the customer wants to focus on.** For example nails, skin, hair and makeup.

        !!! tip "Allow several selections"

            The setting sits in [block settings, multiple-choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Add the follow-up questions for each area, grouped together and in the order of the choices.**

        | Questions | Area |
        |---|---|
        | 2 and 3 | Nails |
        | 4 and 5 | Skin |
        | 6 and 7 | Hair |
        | 8 and 9 | Makeup |

    3. **Add a skip logic rule to every follow-up question, reading its own area.**

        !!! example "The nail questions"

            `IF response to Question 1 is not Nails, then this question is skipped.`

        Questions 4 and 5 read `Skin`, questions 6 and 7 read `Hair`, and questions 8 and 9 read `Makeup`.

    4. **Click the top-right `Publish` button, then answer the quiz picking two areas.** Only the questions for those two areas should appear.

    !!! tip "Why the rule reads `is not`"

        A rule phrased as `is not` skips the question for everyone who did not pick that choice, and shows it to everyone who did. The quiz keeps one straight path, however many choices the customer makes.

=== "Standalone"

    A beauty quiz lets the customer pick several areas to focus on at once, then asks the follow-up questions for each area they picked.

    1. **Add a question asking which areas the customer wants to focus on.** For example nails, skin, hair and makeup.

        !!! tip "Allow several selections"

            The setting sits in [block settings, multiple-choice settings](/reference/quiz-builder/questions/#multiple-choice).

    2. **Add the follow-up questions for each area, grouped together and in the order of the choices.**

        | Questions | Area |
        |---|---|
        | 2 and 3 | Nails |
        | 4 and 5 | Skin |
        | 6 and 7 | Hair |
        | 8 and 9 | Makeup |

    3. **Add a skip logic rule to every follow-up question, reading its own area.**

        !!! example "The nail questions"

            `IF response to Question 1 is not Nails, then this question is skipped.`

        Questions 4 and 5 read `Skin`, questions 6 and 7 read `Hair`, and questions 8 and 9 read `Makeup`.

    4. **Click the top-right `Publish` button, then answer the quiz picking two areas.** Only the questions for those two areas should appear.

    !!! tip "Why the rule reads `is not`"

        A rule phrased as `is not` skips the question for everyone who did not pick that choice, and shows it to everyone who did. The quiz keeps one straight path, however many choices the customer makes.

!!! info "A quiz built entirely on skipped slides"

    See [Funnel Quiz that Skips Slides](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-that-skips-slides).

### Ask for an email only when the customer offers one

=== "Shopify"

    ![how to use skip logic example2](/images/how_to_shopifyV2_skiplogic_example_logic_email_question_skipped.png)

    1. **Add a [`Yes/No question`](/reference/quiz-builder/questions/#yesno) asking whether the customer will leave an email address.**

    2. **Add an [`Email address` question](/reference/quiz-builder/questions/#email-address) after it.**

    3. **Add a skip logic rule to the email question, reading `IF the response to` the yes or no question `is` `No`.**

    A customer who declines goes straight on to the results page, and is never asked for an address.

=== "Shopify (Legacy)"

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    1. **Add a `Yes/No question` asking whether the customer will leave an email address.**

    2. **Add an `email` input question after it.**

    3. **Add a Skip Logic rule to the email question, reading `IF response to` the yes or no question `is` `No`.**

    A customer who declines goes straight on to the Results Page, and is never asked for an address.

=== "WooCommerce"

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    1. **Add a `Yes/No question` asking whether the customer will leave an email address.**

    2. **Add an `email` input question after it.**

    3. **Add a Skip Logic rule to the email question, reading `IF response to` the yes or no question `is` `No`.**

    A customer who declines goes straight on to the Results Page, and is never asked for an address.

=== "Magento"

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    1. **Add a `Yes/No question` asking whether the customer will leave an email address.**

    2. **Add an `email` input question after it.**

    3. **Add a Skip Logic rule to the email question, reading `IF response to` the yes or no question `is` `No`.**

    A customer who declines goes straight on to the Results Page, and is never asked for an address.

=== "BigCommerce"

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    1. **Add a `Yes/No question` asking whether the customer will leave an email address.**

    2. **Add an `email` input question after it.**

    3. **Add a Skip Logic rule to the email question, reading `IF response to` the yes or no question `is` `No`.**

    A customer who declines goes straight on to the Results Page, and is never asked for an address.

=== "Standalone"

    ![how to use skip logic example2](/images/how_to_use_skip_logic_example2.png)

    1. **Add a `Yes/No question` asking whether the customer will leave an email address.**

    2. **Add an `email` input question after it.**

    3. **Add a Skip Logic rule to the email question, reading `IF response to` the yes or no question `is` `No`.**

    A customer who declines goes straight on to the Results Page, and is never asked for an address.

## Skip logic and jump logic

Both rules change which question comes next, and they go about it differently.

| Rule | What it does |
|---|---|
| Skip logic | Leaves the path alone, and drops the questions that do not apply |
| Jump logic | Sends the customer to a named destination, so the quiz splits into separate paths |

Use skip logic when there is one path, and some questions on it are irrelevant to some customers. Use [jump logic](/how-to-guides/use-jump-logic/) when the paths diverge and stay apart.

Do not use both in one quiz.

## Additional resources

Read up on boolean logic before writing complex AND/OR rules. [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) evaluates a rule you type in, and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) explains how AND and OR combine.

See [How to Use Conditional Logic](/how-to-guides/use-conditional-logic/) for the other kinds of logic a quiz can use.

---

This article explains how to write skip logic rules, and how to hide the questions a customer does not need.