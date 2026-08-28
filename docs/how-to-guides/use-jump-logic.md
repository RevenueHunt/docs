---
description: "Complete guide to using jump logic in RevenueHunt to branch quiz paths based on answers."
icon: material/directions-fork
---

# How to Use Jump Logic

[Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) sends a customer somewhere other than the next question, from the answer they just gave. One quiz can hold several routes, and each customer travels only their own.

!!! info "Use jump logic to"

    - Send the customer to a different follow-up question.
    - Branch the quiz into separate paths.
    - Send the customer to a different results page.
    - Send the customer to an external URL.

!!! example "What this looks like in a quiz"

    A skincare quiz opens by asking the skin type: dry, normal, combination or oily. Jump logic sends each answer on to the questions that matter for that skin type, and past the ones that do not.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/N2gudKAy4qU?si=hcgIntH-XecaQxua" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

!!! warning "Do not mix jump logic and skip logic in one quiz"

    Each of them rewrites the order of the questions. Together they produce paths that neither rule intended. See [Jump logic and skip logic](#jump-logic-and-skip-logic).

## The conditional logic tab

=== "Shopify"

    ![quiz builder conditional logic](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic.png)

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

## Add a jump logic rule

Every rule reads the same way: **IF** the response to a question **is** a certain choice, **THEN go to** a destination. A destination is another question, a results page or a URL.

=== "Shopify"

    1. **Open the [Quiz builder](/reference/quiz-builder/) and go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question the rule starts from.**

    3. **Open the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) section.**

    4. **Click `+ Add another rule (OR)`.**

    5. **Pick the choice the rule reads, then pick the destination under `THEN go to`.**

        !!! example "One rule"

            ![quiz builder conditional logic jump logic rule](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_example.png)

            A customer who answers `Oily all over` to Question 4, SKIN TYPE, goes to Question 8, SKIN TYPE: OILY.

    6. **Add a rule for every other answer that needs its own destination.**

        !!! example "Two rules on one question"

            ![quiz builder conditional logic jump logic OR rule](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_exampleOR.png)

            `Oily all over` sends the customer to Question 8, SKIN TYPE: OILY. `Oily in certain spots` sends them to Question 6, SKIN TYPE: COMBINATION.

    7. **Set a `Default destination` for the customers no rule catches.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_defaultdestination](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_defaultdestination.png)

    8. **Click the top-right `Save` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Jump logic panel"

        | Button | What it does |
        |---|---|
        | `+ Add another rule (OR)` | Adds another rule to the question, with its own condition and destination |
        | `+ Add concurrent logic (AND)` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Default destination` | The destination for a customer that no rule catches |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

        !!! example "An AND rule"

            ![quiz builder conditional logic jump logic AND rule](/images/manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_exampleAND.png)

            The customer reaches Question 8, SKIN TYPE: OILY, only by answering `Oily all over` to Question 4 and `Teens and 20's` to Question 3.

=== "Shopify (Legacy)"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question the rule starts from.**

    3. **Open the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) section.**

    4. **Click `Add Jump Logic`.**

    5. **Pick the choice the rule reads, then pick the destination under `THEN go to`.**

        !!! example "One rule"

            ![quiz builder conditional logic jump logic rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule.png){width="500"}

            A customer who answers `Myself` to Question 1, Who are you shopping for?, goes to Question 2, What is your skin type?.

    6. **Click the `+` button to add a rule for every other answer that needs its own destination.**

        !!! example "Two rules on one question"

            ![quiz builder conditional logic jump logic OR rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_or.png)

            `Myself` sends the customer to Question 2, What is your skin type?. `A gift` sends them to Question 4, What is their skin type?.

    7. **Set an `Always jump to:` destination for the customers no rule catches.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Jump Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question, with its own condition and destination |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Always jump to:` | The destination for a customer that no rule catches |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

        !!! example "An AND rule"

            ![quiz builder conditional logic jump logic AND rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_and.png){width="500"}

            The customer reaches Question 3, What is your age?, only by answering `Myself` to Question 1 and `Dry` to Question 2.

=== "WooCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question the rule starts from.**

    3. **Open the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) section.**

    4. **Click `Add Jump Logic`.**

    5. **Pick the choice the rule reads, then pick the destination under `THEN go to`.**

        !!! example "One rule"

            ![quiz builder conditional logic jump logic rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule.png){width="500"}

            A customer who answers `Myself` to Question 1, Who are you shopping for?, goes to Question 2, What is your skin type?.

    6. **Click the `+` button to add a rule for every other answer that needs its own destination.**

        !!! example "Two rules on one question"

            ![quiz builder conditional logic jump logic OR rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_or.png)

            `Myself` sends the customer to Question 2, What is your skin type?. `A gift` sends them to Question 4, What is their skin type?.

    7. **Set an `Always jump to:` destination for the customers no rule catches.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Jump Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question, with its own condition and destination |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Always jump to:` | The destination for a customer that no rule catches |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

        !!! example "An AND rule"

            ![quiz builder conditional logic jump logic AND rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_and.png){width="500"}

            The customer reaches Question 3, What is your age?, only by answering `Myself` to Question 1 and `Dry` to Question 2.

=== "Magento"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question the rule starts from.**

    3. **Open the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) section.**

    4. **Click `Add Jump Logic`.**

    5. **Pick the choice the rule reads, then pick the destination under `THEN go to`.**

        !!! example "One rule"

            ![quiz builder conditional logic jump logic rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule.png){width="500"}

            A customer who answers `Myself` to Question 1, Who are you shopping for?, goes to Question 2, What is your skin type?.

    6. **Click the `+` button to add a rule for every other answer that needs its own destination.**

        !!! example "Two rules on one question"

            ![quiz builder conditional logic jump logic OR rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_or.png)

            `Myself` sends the customer to Question 2, What is your skin type?. `A gift` sends them to Question 4, What is their skin type?.

    7. **Set an `Always jump to:` destination for the customers no rule catches.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Jump Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question, with its own condition and destination |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Always jump to:` | The destination for a customer that no rule catches |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

        !!! example "An AND rule"

            ![quiz builder conditional logic jump logic AND rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_and.png){width="500"}

            The customer reaches Question 3, What is your age?, only by answering `Myself` to Question 1 and `Dry` to Question 2.

=== "BigCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question the rule starts from.**

    3. **Open the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) section.**

    4. **Click `Add Jump Logic`.**

    5. **Pick the choice the rule reads, then pick the destination under `THEN go to`.**

        !!! example "One rule"

            ![quiz builder conditional logic jump logic rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule.png){width="500"}

            A customer who answers `Myself` to Question 1, Who are you shopping for?, goes to Question 2, What is your skin type?.

    6. **Click the `+` button to add a rule for every other answer that needs its own destination.**

        !!! example "Two rules on one question"

            ![quiz builder conditional logic jump logic OR rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_or.png)

            `Myself` sends the customer to Question 2, What is your skin type?. `A gift` sends them to Question 4, What is their skin type?.

    7. **Set an `Always jump to:` destination for the customers no rule catches.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Jump Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question, with its own condition and destination |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Always jump to:` | The destination for a customer that no rule catches |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

        !!! example "An AND rule"

            ![quiz builder conditional logic jump logic AND rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_and.png){width="500"}

            The customer reaches Question 3, What is your age?, only by answering `Myself` to Question 1 and `Dry` to Question 2.

=== "Standalone"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.**

    2. **Select the question the rule starts from.**

    3. **Open the [`Jump Logic`](/reference/quiz-builder/conditional-logic/#jump-logic) section.**

    4. **Click `Add Jump Logic`.**

    5. **Pick the choice the rule reads, then pick the destination under `THEN go to`.**

        !!! example "One rule"

            ![quiz builder conditional logic jump logic rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule.png){width="500"}

            A customer who answers `Myself` to Question 1, Who are you shopping for?, goes to Question 2, What is your skin type?.

    6. **Click the `+` button to add a rule for every other answer that needs its own destination.**

        !!! example "Two rules on one question"

            ![quiz builder conditional logic jump logic OR rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_or.png)

            `Myself` sends the customer to Question 2, What is your skin type?. `A gift` sends them to Question 4, What is their skin type?.

    7. **Set an `Always jump to:` destination for the customers no rule catches.**

    8. **Click the top-right `Publish` button, then preview the quiz and answer it as a customer would.**

    ??? info "The buttons in the Jump Logic panel"

        | Button | What it does |
        |---|---|
        | `+` | Adds another rule to the question, with its own condition and destination |
        | `+ add concurrent logic` | Adds a second test to the current rule. Both tests must be true |
        | `bin` | Deletes the current rule |
        | `Always jump to:` | The destination for a customer that no rule catches |

        Most quizzes need only OR rules. An AND rule is easy to write and hard to satisfy, because every test in it has to be true at the same time.

        !!! example "An AND rule"

            ![quiz builder conditional logic jump logic AND rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_and.png){width="500"}

            The customer reaches Question 3, What is your age?, only by answering `Myself` to Question 1 and `Dry` to Question 2.

## Examples

### Branch the quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/N2gudKAy4qU?si=Ud8s2dtSN0uJECkC&amp;start=13" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A skincare quiz asks for the skin type, shows one statement of four, and then carries on with the rest of the questions.

    ![how to use jump logic](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_default_destination.png)

    1. **Add the skin type question, and one statement slide per skin type.**

        ![how to use jump logic](https://loom.com/i/11c8cff2e27a451a8c8b40b348de4a42?workflows_screenshot=true)

    2. **Open the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    3. **Add one rule per answer, each pointing at its own statement.**

        ![how to use jump logic](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_rule.png){width="300"}

        | Answer | Destination |
        |---|---|
        | Dry and tight all over | Dry skin statement |
        | Not too oily, not too dry | Normal skin statement |
        | Oily in certain spots | Combination skin statement |
        | Oily all over | Oily skin statement |

    4. **Select each statement in turn, and set its `Default destination` to the next question.**

        ![how to use jump logic](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_rule2.png){width="300"}

        Without this the branches never rejoin, and a customer who read the dry skin statement carries on into the normal skin statement.

    5. **Click the top-right `Save` button, then answer the quiz once per skin type.**

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png){width="500"}

    A skincare quiz asks for the skin type, shows one statement of four, and then carries on with the rest of the questions.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go back to the skin type question and open [Conditional Logic](/reference/quiz-builder/conditional-logic/).**

    4. **Add one `OR` rule per answer, each pointing at its own statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    5. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries on into the normal skin statement.

    6. **Click the top-right `Publish` button, then answer the quiz once per skin type.**

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png){width="500"}

    A skincare quiz asks for the skin type, shows one statement of four, and then carries on with the rest of the questions.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go back to the skin type question and open [Conditional Logic](/reference/quiz-builder/conditional-logic/).**

    4. **Add one `OR` rule per answer, each pointing at its own statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    5. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries on into the normal skin statement.

    6. **Click the top-right `Publish` button, then answer the quiz once per skin type.**

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png){width="500"}

    A skincare quiz asks for the skin type, shows one statement of four, and then carries on with the rest of the questions.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go back to the skin type question and open [Conditional Logic](/reference/quiz-builder/conditional-logic/).**

    4. **Add one `OR` rule per answer, each pointing at its own statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    5. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries on into the normal skin statement.

    6. **Click the top-right `Publish` button, then answer the quiz once per skin type.**

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png){width="500"}

    A skincare quiz asks for the skin type, shows one statement of four, and then carries on with the rest of the questions.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go back to the skin type question and open [Conditional Logic](/reference/quiz-builder/conditional-logic/).**

    4. **Add one `OR` rule per answer, each pointing at its own statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    5. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries on into the normal skin statement.

    6. **Click the top-right `Publish` button, then answer the quiz once per skin type.**

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=K5rbKH2WhSmVBTeP" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png){width="500"}

    A skincare quiz asks for the skin type, shows one statement of four, and then carries on with the rest of the questions.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in `Question Settings -> Show Description`, so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go back to the skin type question and open [Conditional Logic](/reference/quiz-builder/conditional-logic/).**

    4. **Add one `OR` rule per answer, each pointing at its own statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    5. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries on into the normal skin statement.

    6. **Click the top-right `Publish` button, then answer the quiz once per skin type.**

### Send customers to different results pages

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/N2gudKAy4qU?si=0v4iXxZKuT0ljH-c&amp;start=82" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create the results pages the quiz needs.** See [How to Set Up Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    2. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the outcome.**

    3. **Open the `Jump Logic` section and click `+ Add another rule (OR)`.**

    4. **Point each answer at its own results page.**

        !!! example "One results page per skin type"

            | Answer to `Q1: What is your skin type?` | Destination |
            |---|---|
            | Dry | Results page 1 |
            | Oily | Results page 2 |
            | Normal | Results page 3 |
            | Combination | Results page 4 |

    5. **Click the top-right `Save` button.**

    ![send users to different results pages jump logic](https://loom.com/i/cf75df4cb4574b2ab7f4b81eff37c83e?workflows_screenshot=true)

=== "Shopify (Legacy)"

    1. **Create the Results Pages the quiz needs.** See [How to Set Up Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    2. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the outcome.**

    3. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    4. **Point each answer at its own Results Page.**

        !!! example "One Results Page per skin type"

            | Answer to `Q1: What is your skin type?` | Destination |
            |---|---|
            | Dry | Results Page 1 |
            | Oily | Results Page 2 |
            | Normal | Results Page 3 |
            | Combination | Results Page 4 |

    5. **Click the top-right `Publish` button.**

    ![send users to different results pages jump logic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)

=== "WooCommerce"

    1. **Create the Results Pages the quiz needs.** See [How to Set Up Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    2. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the outcome.**

    3. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    4. **Point each answer at its own Results Page.**

        !!! example "One Results Page per skin type"

            | Answer to `Q1: What is your skin type?` | Destination |
            |---|---|
            | Dry | Results Page 1 |
            | Oily | Results Page 2 |
            | Normal | Results Page 3 |
            | Combination | Results Page 4 |

    5. **Click the top-right `Publish` button.**

    ![send users to different results pages jump logic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)

=== "Magento"

    1. **Create the Results Pages the quiz needs.** See [How to Set Up Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    2. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the outcome.**

    3. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    4. **Point each answer at its own Results Page.**

        !!! example "One Results Page per skin type"

            | Answer to `Q1: What is your skin type?` | Destination |
            |---|---|
            | Dry | Results Page 1 |
            | Oily | Results Page 2 |
            | Normal | Results Page 3 |
            | Combination | Results Page 4 |

    5. **Click the top-right `Publish` button.**

    ![send users to different results pages jump logic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)

=== "BigCommerce"

    1. **Create the Results Pages the quiz needs.** See [How to Set Up Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    2. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the outcome.**

    3. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    4. **Point each answer at its own Results Page.**

        !!! example "One Results Page per skin type"

            | Answer to `Q1: What is your skin type?` | Destination |
            |---|---|
            | Dry | Results Page 1 |
            | Oily | Results Page 2 |
            | Normal | Results Page 3 |
            | Combination | Results Page 4 |

    5. **Click the top-right `Publish` button.**

    ![send users to different results pages jump logic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)

=== "Standalone"

    1. **Create the Results Pages the quiz needs.** See [How to Set Up Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    2. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the outcome.**

    3. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    4. **Point each answer at its own Results Page.**

        !!! example "One Results Page per skin type"

            | Answer to `Q1: What is your skin type?` | Destination |
            |---|---|
            | Dry | Results Page 1 |
            | Oily | Results Page 2 |
            | Normal | Results Page 3 |
            | Combination | Results Page 4 |

    5. **Click the top-right `Publish` button.**

    ![send users to different results pages jump logic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)

### Send customers to an external URL

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/N2gudKAy4qU?si=M8ps59EfgFulqM9z&amp;start=123" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the destination.**

    2. **Open the `Jump Logic` section and click `+ Add another rule (OR)`.**

    3. **Pick the choice the rule reads, then choose `Link to URL` and paste the address.**

        !!! example "One rule"

            A customer who answers `Dry` to `Q1: What is your skin type?` goes to `https://yourstore.com/dry-skin`.

    4. **To send every customer to one page after this question, set the `Default destination` to `Link to URL` instead.**

    5. **Click the top-right `Save` button.**

    ![how to send users to an external url jump logic](https://loom.com/i/87753ed6e35d45ee8f0abfb0d1c3c92b?workflows_screenshot=true)

    !!! tip "Other ways to redirect a quiz"

        See [Using jump logic for conditional redirection](/how-to-guides/redirect-quiz-to-another-page/#using-jump-logic-for-conditional-redirection).

=== "Shopify (Legacy)"

    1. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the destination.**

    2. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    3. **Pick the choice the rule reads, then paste the address as the destination.**

        !!! example "One rule"

            A customer who answers `Dry` to `Q1: What is your skin type?` goes to `https://yourstore.com/dry-skin`.

    4. **To send every customer to one page after this question, paste the address into `Always jump to` instead.**

    5. **Click the top-right `Publish` button.**

    ![how to send users to an external url jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)

    !!! tip "Other ways to redirect a quiz"

        See [Using jump logic for conditional redirection](/how-to-guides/redirect-quiz-to-another-page/#using-jump-logic-for-conditional-redirection).

=== "WooCommerce"

    1. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the destination.**

    2. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    3. **Pick the choice the rule reads, then paste the address as the destination.**

        !!! example "One rule"

            A customer who answers `Dry` to `Q1: What is your skin type?` goes to `https://yourstore.com/dry-skin`.

    4. **To send every customer to one page after this question, paste the address into `Always jump to` instead.**

    5. **Click the top-right `Publish` button.**

    ![how to send users to an external url jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)

    !!! tip "Other ways to redirect a quiz"

        See [Using jump logic for conditional redirection](/how-to-guides/redirect-quiz-to-another-page/#using-jump-logic-for-conditional-redirection).

=== "Magento"

    1. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the destination.**

    2. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    3. **Pick the choice the rule reads, then paste the address as the destination.**

        !!! example "One rule"

            A customer who answers `Dry` to `Q1: What is your skin type?` goes to `https://yourstore.com/dry-skin`.

    4. **To send every customer to one page after this question, paste the address into `Always jump to` instead.**

    5. **Click the top-right `Publish` button.**

    ![how to send users to an external url jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)

    !!! tip "Other ways to redirect a quiz"

        See [Using jump logic for conditional redirection](/how-to-guides/redirect-quiz-to-another-page/#using-jump-logic-for-conditional-redirection).

=== "BigCommerce"

    1. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the destination.**

    2. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    3. **Pick the choice the rule reads, then paste the address as the destination.**

        !!! example "One rule"

            A customer who answers `Dry` to `Q1: What is your skin type?` goes to `https://yourstore.com/dry-skin`.

    4. **To send every customer to one page after this question, paste the address into `Always jump to` instead.**

    5. **Click the top-right `Publish` button.**

    ![how to send users to an external url jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)

    !!! tip "Other ways to redirect a quiz"

        See [Using jump logic for conditional redirection](/how-to-guides/redirect-quiz-to-another-page/#using-jump-logic-for-conditional-redirection).

=== "Standalone"

    1. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the question that decides the destination.**

    2. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    3. **Pick the choice the rule reads, then paste the address as the destination.**

        !!! example "One rule"

            A customer who answers `Dry` to `Q1: What is your skin type?` goes to `https://yourstore.com/dry-skin`.

    4. **To send every customer to one page after this question, paste the address into `Always jump to` instead.**

    5. **Click the top-right `Publish` button.**

    ![how to send users to an external url jump logic](/images/how_to_redirect_quiz_ot_another_page_jump_logic.png)

    !!! tip "Other ways to redirect a quiz"

        See [Using jump logic for conditional redirection](/how-to-guides/redirect-quiz-to-another-page/#using-jump-logic-for-conditional-redirection).

## Jump logic and skip logic

Both rules change which question comes next, and they go about it differently.

| Rule | What it does |
|---|---|
| Jump logic | Sends the customer to a named destination, so the quiz splits into separate paths |
| Skip logic | Leaves the path alone, and drops the questions that do not apply |

Use jump logic when the paths diverge and stay apart. Use [skip logic](/how-to-guides/use-skip-logic/) when there is one path, and some questions on it are irrelevant to some customers.

Do not use both in one quiz.

## Additional resources

Read up on boolean logic before writing complex AND/OR rules. [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) evaluates a rule you type in, and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) explains how AND and OR combine.

See [How to Use Conditional Logic](/how-to-guides/use-conditional-logic/) for the other kinds of logic a quiz can use.

---

This article explains how to write jump logic rules, and how to branch a quiz with them.