---
description: "Step-by-step guide to create a RevenueHunt quiz with fixed product recommendations."
icon: material/pin-outline
---

# How to Set Up a Fixed Recommendations Quiz

A fixed recommendation shows the products you choose, rather than the products the quiz scores. Build a section for each outcome and fill it with the products you want. Logic then decides which section or results page each customer sees.

This suits a quiz with complex branching.

!!! info "Use this method for:"

    - Quizzes that show the same product(s) to everyone regardless of answers
    - Quizzes with multiple very precise outcomes and product recommendations
    - Quizzes with complex branching
    - Quizzes that require a lot of logic conditions and custom text

!!! tip "Recognizing a product matrix"

    If your product matrix looks like this one, this method is the one you want.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png){width=300}

There are three ways to build one. They differ in how many results pages you need, and in which kind of logic decides what the customer sees.

| Method | Use it when |
|---|---|
| [Always the same recommendations](#always-the-same-recommendations) | Every customer sees the same products, whatever they answered |
| [Fixed recommendations with display logic and one results page](#fixed-recommendations-with-display-logic-and-one-results-page) | One results page holds a section per outcome, and display logic shows the matching one |
| [Fixed recommendations with display logic and multiple results pages](#fixed-recommendations-with-display-logic-and-multiple-results-pages) | Each outcome gets its own results page, and jump logic sends the customer to it |

## Always the same recommendations

A fixed section shows the same products on the results page, whatever the customer answered.

![how_to_shopify_v2_recommendations_fixedrecommendations](/images/how_to_shopify_v2_recommendations_fixedrecommendations.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/uiJwV1MxZKg?si=Ucpz_kB6PXt5VgJ4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add a [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) to the Results page.**

    2. **Set its `Recommendation system` to `Fixed Recommendations`.**

    3. **Open `Slot 1`, go to `Fixed recommended items` and select the products to show.**

    4. **Set `Max. recommended items` to the number of products you chose.**

    5. **Click `Save`.**

    6. **Preview the quiz and check that the products appear.**

=== "Shopify (Legacy)"

    !!! note "This version has no fixed recommendations"

        This version of the app cannot pin products to the Results Page. Two workarounds get the same result. Use whichever fits your quiz.

    **Option 1: show the same products to everyone**

    Every customer sees the same products, whatever they answered.

    1. **Go to the [Link Products section](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Choose any question in your quiz.**

    3. **Link the products you want to pin to every choice in that question.**

        !!! info "Why this works"

            Every choice upvotes the same products, so those products collect upvotes whatever the customer picks. They then sit at the top of the Results Page, as the most upvoted products.

    **Option 2: give the fixed products their own block**

    This keeps the scored recommendations, and adds a separate block for the pinned products.

    1. **Create a collection in your Shopify store holding the products you always want shown.**

    2. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the app and click `Sync Catalog`.**

    3. **Go to [Link Products](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    4. **Select any question, and link the new collection to every choice.** Those products then collect upvotes whatever the customer picks.

    5. **Add two blocks to your [Results Page](/reference/quiz-builder/results-page/):**

        - **Product Block** - shows the dynamic recommendations, which change with the answers.
        - **Slot Block** - shows the most upvoted products from the collection linked to that slot.

    6. **Set the title and description of the Slot Block, and choose how many products it shows.**

    7. **Link your new collection in the `Included Collections` field of the Slot Block.**

    8. **Save the quiz.**

    9. **Take the quiz several times, with different answers each time.**

    10. **Check that the dynamic recommendations change, and that the fixed products stay in their slot.**

=== "WooCommerce"

    !!! note "This version has no fixed recommendations"

        This version of the app cannot pin products to the Results Page. Two workarounds get the same result. Use whichever fits your quiz.

    **Option 1: show the same products to everyone**

    Every customer sees the same products, whatever they answered.

    1. **Go to the [Link Products section](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Choose any question in your quiz.**

    3. **Link the products you want to pin to every choice in that question.**

        !!! info "Why this works"

            Every choice upvotes the same products, so those products collect upvotes whatever the customer picks. They then sit at the top of the Results Page, as the most upvoted products.

    **Option 2: give the fixed products their own block**

    This keeps the scored recommendations, and adds a separate block for the pinned products.

    1. **Create a category in your WooCommerce store holding the products you always want shown.**

    2. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the app and click `Sync Catalog`.**

    3. **Go to [Link Products](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    4. **Select any question, and link the new category to every choice.** Those products then collect upvotes whatever the customer picks.

    5. **Add two blocks to your [Results Page](/reference/quiz-builder/results-page/):**

        - **Product Block** - shows the dynamic recommendations, which change with the answers.
        - **Slot Block** - shows the most upvoted products from the category linked to that slot.

    6. **Set the title and description of the Slot Block, and choose how many products it shows.**

    7. **Link your new category in the `Included Collections` field of the Slot Block.**

    8. **Save the quiz.**

    9. **Take the quiz several times, with different answers each time.**

    10. **Check that the dynamic recommendations change, and that the fixed products stay in their slot.**

=== "Magento"

    !!! note "This version has no fixed recommendations"

        This version of the app cannot pin products to the Results Page. Two workarounds get the same result. Use whichever fits your quiz.

    **Option 1: show the same products to everyone**

    Every customer sees the same products, whatever they answered.

    1. **Go to the [Link Products section](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Choose any question in your quiz.**

    3. **Link the products you want to pin to every choice in that question.**

        !!! info "Why this works"

            Every choice upvotes the same products, so those products collect upvotes whatever the customer picks. They then sit at the top of the Results Page, as the most upvoted products.

    **Option 2: give the fixed products their own block**

    This keeps the scored recommendations, and adds a separate block for the pinned products.

    1. **Create a category in your Magento store holding the products you always want shown.**

    2. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the app and click `Sync Catalog`.**

    3. **Go to [Link Products](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    4. **Select any question, and link the new category to every choice.** Those products then collect upvotes whatever the customer picks.

    5. **Add two blocks to your [Results Page](/reference/quiz-builder/results-page/):**

        - **Product Block** - shows the dynamic recommendations, which change with the answers.
        - **Slot Block** - shows the most upvoted products from the category linked to that slot.

    6. **Set the title and description of the Slot Block, and choose how many products it shows.**

    7. **Link your new category in the `Included Collections` field of the Slot Block.**

    8. **Save the quiz.**

    9. **Take the quiz several times, with different answers each time.**

    10. **Check that the dynamic recommendations change, and that the fixed products stay in their slot.**

=== "BigCommerce"

    !!! note "This version has no fixed recommendations"

        This version of the app cannot pin products to the Results Page. Two workarounds get the same result. Use whichever fits your quiz.

    **Option 1: show the same products to everyone**

    Every customer sees the same products, whatever they answered.

    1. **Go to the [Link Products section](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Choose any question in your quiz.**

    3. **Link the products you want to pin to every choice in that question.**

        !!! info "Why this works"

            Every choice upvotes the same products, so those products collect upvotes whatever the customer picks. They then sit at the top of the Results Page, as the most upvoted products.

    **Option 2: give the fixed products their own block**

    This keeps the scored recommendations, and adds a separate block for the pinned products.

    1. **Create a category in your BigCommerce store holding the products you always want shown.**

    2. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the app and click `Sync Catalog`.**

    3. **Go to [Link Products](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    4. **Select any question, and link the new category to every choice.** Those products then collect upvotes whatever the customer picks.

    5. **Add two blocks to your [Results Page](/reference/quiz-builder/results-page/):**

        - **Product Block** - shows the dynamic recommendations, which change with the answers.
        - **Slot Block** - shows the most upvoted products from the category linked to that slot.

    6. **Set the title and description of the Slot Block, and choose how many products it shows.**

    7. **Link your new category in the `Included Collections` field of the Slot Block.**

    8. **Save the quiz.**

    9. **Take the quiz several times, with different answers each time.**

    10. **Check that the dynamic recommendations change, and that the fixed products stay in their slot.**

=== "Standalone"

    !!! note "This version has no fixed recommendations"

        This version of the app cannot pin products to the Results Page. Two workarounds get the same result. Use whichever fits your quiz.

    **Option 1: show the same products to everyone**

    Every customer sees the same products, whatever they answered.

    1. **Go to the [Link Products section](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Choose any question in your quiz.**

    3. **Link the products you want to pin to every choice in that question.**

        !!! info "Why this works"

            Every choice upvotes the same products, so those products collect upvotes whatever the customer picks. They then sit at the top of the Results Page, as the most upvoted products.

    **Option 2: give the fixed products their own block**

    This keeps the scored recommendations, and adds a separate block for the pinned products.

    1. **Create a collection in your Standalone account holding the products you always want shown.**

    2. **Go to the [Success Checklist](/reference/dashboard/#success-checklist) in the app and click `Sync Catalog`.**

    3. **Go to [Link Products](/reference/quiz-builder/link-products/) in the [Quiz Builder](/reference/quiz-builder/).**

    4. **Select any question, and link the new collection to every choice.** Those products then collect upvotes whatever the customer picks.

    5. **Add two blocks to your [Results Page](/reference/quiz-builder/results-page/):**

        - **Product Block** - shows the dynamic recommendations, which change with the answers.
        - **Slot Block** - shows the most upvoted products from the collection linked to that slot.

    6. **Set the title and description of the Slot Block, and choose how many products it shows.**

    7. **Link your new collection in the `Included Collections` field of the Slot Block.**

    8. **Save the quiz.**

    9. **Take the quiz several times, with different answers each time.**

    10. **Check that the dynamic recommendations change, and that the fixed products stay in their slot.**

## Fixed recommendations with display logic and one results page

One results page holds the text and the products for every outcome. Display Logic then shows the ones that match the answers, and hides the rest.

![how_to_shopify_v2_recommendations_displaylogic](/images/how_to_shopify_v2_recommendations_displaylogic.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/NvDLDlknJv4?si=x9HaGPZxsjDwTrY-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers recognize their own skin type.

    2. **Go to the [Results page](/reference/quiz-builder/results-page/) tab and click `+ Add section`.** Add one section per skin type.

    3. **Add content blocks to each section, describing that skin type and its challenges.**

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_shopifyv2_fixedrecommendationquiz_sectionsresultspage.png)

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add a `Product Block` to each section, holding the products for that skin type.**

    5. **Set the `Recommendation system` to `Fixed Recommendations` in the [Product block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).**

        ![how to recommend products fixed recommendations resultspage](/images/how_to_shopifyv2_fixedrecommendationquiz_fixedrecommendationsresultspage.png)

    6. **In the `Slot` settings, set the maximum number of products and choose which ones to show.**

        ![how to recommend products fixed recommendations resultspage2](/images/how_to_shopifyv2_fixedrecommendationquiz_fixedrecommendationsresultspage2.png)

    7. **Select a content block and find `Display logic` in the right-hand menu.**

    8. **Click `+ Add condition (OR)` and write an IF-THEN rule that shows the block for one skin type.**

        ![how to hide content with logic display logic statement](/images/how_to_shopifyv2_fixedrecommendationquiz_displaylogic.png)

        !!! info "Without display logic, every block shows"

            Without [Display logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results page, whatever the customer answered.

    9. **Repeat for every block that belongs to one skin type only.**

    10. **Click the top-right `Save` button to update the preview and the live quiz.**

=== "Shopify (Legacy)"

    !!! note "This version cannot pin products"

        This version cannot pin products to a block. Use Display Logic for the text, and one of the workarounds in [Always the same recommendations](#always-the-same-recommendations) for the products.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the Results Page and click the `+` sign.**

    3. **Select `Content Block` from the list.**

    4. **Write the text for one skin type in the block.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        !!! tip "Formatting the text"

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    5. **Repeat for every skin type.**

    6. **Select a content block, click `display logic`, then `add display logic`.**

    7. **Write an IF-THEN rule that shows the block for one skin type.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

        !!! info "Without Display Logic, every block shows"

            Without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

    8. **Repeat for every content block.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "WooCommerce"

    !!! note "This version cannot pin products"

        This version cannot pin products to a block. Use Display Logic for the text, and one of the workarounds in [Always the same recommendations](#always-the-same-recommendations) for the products.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the Results Page and click the `+` sign.**

    3. **Select `Content Block` from the list.**

    4. **Write the text for one skin type in the block.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        !!! tip "Formatting the text"

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    5. **Repeat for every skin type.**

    6. **Select a content block, click `display logic`, then `add display logic`.**

    7. **Write an IF-THEN rule that shows the block for one skin type.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

        !!! info "Without Display Logic, every block shows"

            Without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

    8. **Repeat for every content block.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "Magento"

    !!! note "This version cannot pin products"

        This version cannot pin products to a block. Use Display Logic for the text, and one of the workarounds in [Always the same recommendations](#always-the-same-recommendations) for the products.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the Results Page and click the `+` sign.**

    3. **Select `Content Block` from the list.**

    4. **Write the text for one skin type in the block.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        !!! tip "Formatting the text"

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    5. **Repeat for every skin type.**

    6. **Select a content block, click `display logic`, then `add display logic`.**

    7. **Write an IF-THEN rule that shows the block for one skin type.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

        !!! info "Without Display Logic, every block shows"

            Without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

    8. **Repeat for every content block.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "BigCommerce"

    !!! note "This version cannot pin products"

        This version cannot pin products to a block. Use Display Logic for the text, and one of the workarounds in [Always the same recommendations](#always-the-same-recommendations) for the products.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the Results Page and click the `+` sign.**

    3. **Select `Content Block` from the list.**

    4. **Write the text for one skin type in the block.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        !!! tip "Formatting the text"

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    5. **Repeat for every skin type.**

    6. **Select a content block, click `display logic`, then `add display logic`.**

    7. **Write an IF-THEN rule that shows the block for one skin type.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

        !!! info "Without Display Logic, every block shows"

            Without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

    8. **Repeat for every content block.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "Standalone"

    !!! note "This version cannot pin products"

        This version cannot pin products to a block. Use Display Logic for the text, and one of the workarounds in [Always the same recommendations](#always-the-same-recommendations) for the products.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the Results Page and click the `+` sign.**

    3. **Select `Content Block` from the list.**

    4. **Write the text for one skin type in the block.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

        !!! tip "Formatting the text"

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    5. **Repeat for every skin type.**

    6. **Select a content block, click `display logic`, then `add display logic`.**

    7. **Write an IF-THEN rule that shows the block for one skin type.**

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

        !!! info "Without Display Logic, every block shows"

            Without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

    8. **Repeat for every content block.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

## Fixed recommendations with display logic and multiple results pages

Give each results page its own fixed products and its own text. Jump Logic then sends each customer to the right page.

!!! info "How this differs from the previous method"

    The previous method uses one results page holding several blocks, and Display Logic shows or hides them. This method uses several results pages, and Jump Logic decides which one the customer reaches. The work is the same either way. Only the place you put the logic changes.

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/uLqul_uj0UQ?si=E77WIlpSvtjC4w7R" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` about the skin type.** Give it the choices Dry, Normal, Oily and Combination-type skin.

        !!! tip "Helping the customer choose"

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers recognize their own skin type.

    2. **Go to the [Results page](/reference/quiz-builder/results-page/) tab and click `+ Add Results Page`.** Create one results page per skin type.

    3. **Add content blocks to each results page, describing that skin type.**

        ![how to set up multiple results pages](/images/how_to_shopifyv2_fixedrecommendationquiz_resultpages.png)

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add a `Products Block` to each results page, holding the products for that skin type.**

    5. **Set the `Recommendation system` to `Fixed Recommendations` in the [Product block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).**

        ![how to recommend products fixed recommendations resultspage](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_fixedrecommendationsresultspage.png)

    6. **In the `Slot` settings, set the maximum number of products and select the ones to show.**

        ![how to recommend products fixed recommendations resultspage2](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_fixedrecommendationsresultspage2.png)

    7. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and pick the last question in the quiz.**

        ![how to set up jump logic for results pages](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_jumplogic.png)

    8. **Add a [Jump logic](/how-to-guides/hide-content-with-logic/#branch-the-quiz-with-jump-logic) rule that sends one skin type to its own results page.** Click `+ Add another rule (OR)` for each further rule.

        !!! example "A rule that routes one choice"

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_example](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_jumplogic_example.png)

            A customer who picks "Not too oily..." in Question 4, "SKIN TYPE", goes to Results page 2.

    9. **Repeat until every choice in the skin type question has a rule.**

    10. **Click the top-right `Save` button to update the preview and the live quiz.**

=== "Shopify (Legacy)"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add the `Multiple-choice questions` that ask about the customer's needs.**

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and click the `+` sign.** Add one results page per outcome, such as one per skin type.

        !!! tip "Working with several results pages"

            See [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    3. **Add a Product Block to each results page.**

    4. **Write the text for that outcome on each results page.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Use Jump Logic to branch the quiz.** Draw the branches first, then build them.

        Stage 1, the logic tree:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2, the same branches in the Quiz Builder:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    6. **Link the recommended products to the choices in the last question of each branch.**

    7. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and add one Jump Logic rule per branch.** Each rule sends the customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

    8. **Repeat until every choice in the last question has a rule.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "WooCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add the `Multiple-choice questions` that ask about the customer's needs.**

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and click the `+` sign.** Add one results page per outcome, such as one per skin type.

        !!! tip "Working with several results pages"

            See [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    3. **Add a Product Block to each results page.**

    4. **Write the text for that outcome on each results page.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Use Jump Logic to branch the quiz.** Draw the branches first, then build them.

        Stage 1, the logic tree:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2, the same branches in the Quiz Builder:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    6. **Link the recommended products to the choices in the last question of each branch.**

    7. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and add one Jump Logic rule per branch.** Each rule sends the customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

    8. **Repeat until every choice in the last question has a rule.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "Magento"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add the `Multiple-choice questions` that ask about the customer's needs.**

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and click the `+` sign.** Add one results page per outcome, such as one per skin type.

        !!! tip "Working with several results pages"

            See [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    3. **Add a Product Block to each results page.**

    4. **Write the text for that outcome on each results page.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Use Jump Logic to branch the quiz.** Draw the branches first, then build them.

        Stage 1, the logic tree:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2, the same branches in the Quiz Builder:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    6. **Link the recommended products to the choices in the last question of each branch.**

    7. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and add one Jump Logic rule per branch.** Each rule sends the customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

    8. **Repeat until every choice in the last question has a rule.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "BigCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add the `Multiple-choice questions` that ask about the customer's needs.**

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and click the `+` sign.** Add one results page per outcome, such as one per skin type.

        !!! tip "Working with several results pages"

            See [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    3. **Add a Product Block to each results page.**

    4. **Write the text for that outcome on each results page.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Use Jump Logic to branch the quiz.** Draw the branches first, then build them.

        Stage 1, the logic tree:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2, the same branches in the Quiz Builder:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    6. **Link the recommended products to the choices in the last question of each branch.**

    7. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and add one Jump Logic rule per branch.** Each rule sends the customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

    8. **Repeat until every choice in the last question has a rule.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

=== "Standalone"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and add the `Multiple-choice questions` that ask about the customer's needs.**

        !!! tip "Helping the customer choose"

            Use the description box in `Question Settings -> Show Description` to help customers recognize their own skin type.

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and click the `+` sign.** Add one results page per outcome, such as one per skin type.

        !!! tip "Working with several results pages"

            See [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/).

    3. **Add a Product Block to each results page.**

    4. **Write the text for that outcome on each results page.**

        !!! example "Text for each skin type"

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    5. **Use Jump Logic to branch the quiz.** Draw the branches first, then build them.

        Stage 1, the logic tree:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2, the same branches in the Quiz Builder:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    6. **Link the recommended products to the choices in the last question of each branch.**

    7. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and add one Jump Logic rule per branch.** Each rule sends the customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

    8. **Repeat until every choice in the last question has a rule.**

    9. **Click the top-right `Publish` button to update the preview and the live quiz.**

---

---
This article explains how to show the same products to every customer, and how to vary them with display logic instead of scoring.
