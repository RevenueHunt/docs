---
description: "Learn how to use conditional logic to show or hide content in your RevenueHunt quiz based on customer answers and responses."
icon: material/eye-off
---

# How to Show or Hide Content Based on Quiz Answers

A quiz can hold the content for every outcome and show each customer only the part that fits them. An `IF-THEN` rule decides which part.

There are three ways to do it, and this article works the same skincare quiz through all three.

| Rule | What it does | Where |
|---|---|---|
| [Jump logic](#branch-the-quiz-with-jump-logic) | Sends the customer straight to the matching statement | In the quiz |
| [Skip logic](#skip-a-statement-with-skip-logic) | Hides the statements that do not match | In the quiz |
| [Display logic](#show-a-section-with-display-logic) | Hides the results page sections that do not match | On the results page |

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/s71v8NfNRWk?si=c-8mefpQoHOvppvX" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/mYejhkIPYTI" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## Branch the quiz with jump logic

Your quiz holds one statement per skin type, one after another. Without a rule, the customer reads all four.

Jump logic sends the customer from the skin type question straight to the statement that matches their answer. Each statement then points at the next question, so the quiz carries on from there.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/N2gudKAy4qU?si=hcgIntH-XecaQxua" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    4. **Find `Jump Logic` in the menu on the right, and click `+ Add another rule (OR)`.**

    5. **Set the rule to `IF the response to` the skin type question `is` the dry skin choice, `THEN go to` the dry skin statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_rule.png)

    6. **Click `+ Add another rule (OR)` again for each of the other three answers.**

    7. **Select each statement in turn, and set its `Default destination` to the next question.**

        ![how to hide content with logic shopifyv2 jump logic default destination](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_default_destination.png)

        Without this the branches never rejoin, and a customer who read the dry skin statement carries straight on into the normal skin statement.

    8. **Click the top-right `Save` button, then answer the quiz once per skin type.** Each answer should lead to its own statement, and then on to the next question.

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice, `THEN go to` the dry skin statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    6. **Click the `+` button to add a rule for each of the other three answers.**

    7. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries straight on into the normal skin statement.

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Each answer should lead to its own statement, and then on to the next question.

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice, `THEN go to` the dry skin statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    6. **Click the `+` button to add a rule for each of the other three answers.**

    7. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries straight on into the normal skin statement.

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Each answer should lead to its own statement, and then on to the next question.

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice, `THEN go to` the dry skin statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    6. **Click the `+` button to add a rule for each of the other three answers.**

    7. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries straight on into the normal skin statement.

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Each answer should lead to its own statement, and then on to the next question.

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice, `THEN go to` the dry skin statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    6. **Click the `+` button to add a rule for each of the other three answers.**

    7. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries straight on into the normal skin statement.

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Each answer should lead to its own statement, and then on to the next question.

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=gdRcqMWV35IOV0QA" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic jump logic](/images/how_to_hide_content_with_logic_jump_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Add one `Statement` slide per skin type.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    3. **Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select the skin type question.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice, `THEN go to` the dry skin statement.**

        ![how to hide content with logic jump logic statement](/images/how_to_hide_content_with_logic_jump_logic_statement.png)

    6. **Click the `+` button to add a rule for each of the other three answers.**

    7. **Select each statement in turn, and set its `Always jump to...` destination to the next question.**

        Without this the branches never rejoin, and a customer who read the dry skin statement carries straight on into the normal skin statement.

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Each answer should lead to its own statement, and then on to the next question.

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

## Skip a statement with skip logic

Your quiz holds the same four statements, and the customer travels through all of them in order.

Skip logic puts a rule on each statement that hides it unless the answer matches. The customer walks past the three that do not apply, and reads only theirs.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/ImHVs7AT8YY?si=iMGaCLXqTpr8yS0B" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

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

    !!! tip "More on skip logic"

        See [How to Use Skip Logic](/how-to-guides/use-skip-logic/).

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

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

    !!! tip "More on skip logic"

        See [How to Use Skip Logic](/how-to-guides/use-skip-logic/).

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

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

    !!! tip "More on skip logic"

        See [How to Use Skip Logic](/how-to-guides/use-skip-logic/).

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

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

    !!! tip "More on skip logic"

        See [How to Use Skip Logic](/how-to-guides/use-skip-logic/).

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

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

    !!! tip "More on skip logic"

        See [How to Use Skip Logic](/how-to-guides/use-skip-logic/).

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=pRhc-juq4lgIsIw2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ![how to hide content with logic skip logic](/images/how_to_hide_content_with_logic_skip_logic.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

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

    !!! tip "More on skip logic"

        See [How to Use Skip Logic](/how-to-guides/use-skip-logic/).

## Show a section with display logic

Your results page holds one section per skin type, and all four show by default.

Display logic puts a rule on each section that hides it unless the answer matches. The customer reads only the section for their skin type.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oORLg_BU0fI?si=h7Ortp7mpm1wzTHu" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Go to the [Results page](/reference/quiz-builder/results-page/) and click `+ Add section` once per skin type.**

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_hide_content_with_logic_shopifyv2_display_logic_sections.png)

    3. **Write the text for one skin type in each section.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    4. **Select the dry skin section, find `Display logic`, and click `+ Add logic condition (OR)`.**

    5. **Set the rule to `IF the response to` the skin type question `is` the dry skin choice.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_displaylogic.png)

    6. **Set `Default visibility` to `Hidden`.** The section then appears only for that answer.

    7. **Repeat for the other three sections, each reading its own choice.**

    8. **Click the top-right `Save` button, then answer the quiz once per skin type.** Only the matching section should appear each time.

    !!! tip "Rules on a score or a variable"

        A display logic rule can also read the score of a variable, or the variable with the highest score. See [Write a display logic rule](/how-to-guides/use-display-logic/#write-a-display-logic-rule) for all three kinds, and for what the buttons in the panel do.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) and click `+` once per skin type, adding a `Content Block` each time.**

    3. **Write the text for one skin type in each block.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    4. **Select the dry skin block, click `display logic`, then click `add display logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    6. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    7. **Repeat for the other three blocks, each reading its own choice.**

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

    !!! tip "More on display logic"

        See [How to Use Display Logic](/how-to-guides/use-display-logic/).

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) and click `+` once per skin type, adding a `Content Block` each time.**

    3. **Write the text for one skin type in each block.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    4. **Select the dry skin block, click `display logic`, then click `add display logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    6. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    7. **Repeat for the other three blocks, each reading its own choice.**

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

    !!! tip "More on display logic"

        See [How to Use Display Logic](/how-to-guides/use-display-logic/).

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) and click `+` once per skin type, adding a `Content Block` each time.**

    3. **Write the text for one skin type in each block.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    4. **Select the dry skin block, click `display logic`, then click `add display logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    6. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    7. **Repeat for the other three blocks, each reading its own choice.**

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

    !!! tip "More on display logic"

        See [How to Use Display Logic](/how-to-guides/use-display-logic/).

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) and click `+` once per skin type, adding a `Content Block` each time.**

    3. **Write the text for one skin type in each block.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    4. **Select the dry skin block, click `display logic`, then click `add display logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    6. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    7. **Repeat for the other three blocks, each reading its own choice.**

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

    !!! tip "More on display logic"

        See [How to Use Display Logic](/how-to-guides/use-display-logic/).

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=tBJo7gXHs4dvRTn1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking for the skin type.** Offer dry, normal, oily and combination.

        !!! tip "Help the customer answer"

            Describe each skin type in an [image or text block](/reference/quiz-builder/questions/#block-settings), so the customer can tell which one fits.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) and click `+` once per skin type, adding a `Content Block` each time.**

    3. **Write the text for one skin type in each block.**

        !!! example "Four statements, one per skin type"

            - *You have Dry Skin*: The itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you. It has no major issues, and it still deserves care that sustains that natural harmony.
            - *You have Oily Skin*: Your skin is shiny with excess oil rather than a natural glow. It wants a routine that balances and clarifies, with light hydration.
            - *You have Combination-Type Skin*: Your T-zone runs oily, while the rest of your face is normal or dry.

    4. **Select the dry skin block, click `display logic`, then click `add display logic`.**

    5. **Set the rule to `IF response to` the skin type question `is` the dry skin choice.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    6. **Set `IN ALL OTHER CASES this block is` to `Hidden`.**

    7. **Repeat for the other three blocks, each reading its own choice.**

    8. **Click the top-right `Publish` button, then answer the quiz once per skin type.** Only the matching block should appear each time.

    !!! tip "More on display logic"

        See [How to Use Display Logic](/how-to-guides/use-display-logic/).

---

This article works one skincare quiz through jump logic, skip logic and display logic, so you can see what each rule changes.