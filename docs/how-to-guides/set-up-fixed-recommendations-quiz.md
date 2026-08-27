---
description: "Step-by-step guide to create a RevenueHunt quiz with fixed product recommendations."
icon: material/pin-outline
---

# How to Set Up Fixed Recommendations Quiz

A fixed recommendation shows the products you choose, rather than the products the quiz scores. Build a section for each outcome and fill it with the products you want. Logic then decides which section or results page each customer sees.

This suits a quiz with complex branching.

!!! info "Use this method for:"

    - Quizzes that show the same product(s) to everyone regardless of answers
    - Quizzes with multiple very precise outcomes and product recommendations
    - Quizzes with complex branching
    - Quizzes that require a lot of logic conditions and custom text

!!! tip

    If your product matrix looks something like the below, this method is for you.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png){width=300px;}


## Always the same recommendations

A fixed section shows the same products on the results page, whatever the customer answered.

![how_to_shopify_v2_recommendations_fixedrecommendations](/images/how_to_shopify_v2_recommendations_fixedrecommendations.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/uiJwV1MxZKg?si=Ucpz_kB6PXt5VgJ4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Add a [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) to the Results page and set its `Recommendation system` to `Fixed Recommendations`.
    2. Under `Slot 1` go to `Fixed recommended items` and select the products you want to show.
    3. Set `Max. recommended items` to the number of products you chose.
    4. Save the changes and preview the quiz.


=== "Shopify (Legacy)"

    !!! note "Legacy Version Workaround"
        The legacy version of the app has no fixed product recommendations. Two workarounds get you the same result.

    **Option 1: Show the Same Products to Everyone**

    This makes the same products appear for every customer, whatever they answered.

    1. Go to the [Link Products section](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
    2. Choose any question in your quiz
    3. Link your desired fixed products to EVERY choice in that question
    4. These products will now receive upvotes regardless of customer choices
    5. They will appear at the top of the Results Page due to having the most upvotes

    **Option 2: Create a Dedicated Fixed Products Section**

    This combines scored recommendations with fixed products, using a separate product block.

    1. **Create a Collection for Fixed Products**: in Shopify, create a collection holding the products you always want shown.

    2. **Sync Your Store**
        - Go to [Success Checklist](/reference/dashboard/#success-checklist) in the app
        - Click `Sync Catalog` to update your catalog

    3. **Link the Collection**
        - Go to [Link Products](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
        - Select any question in your quiz
        - Link your new collection to EVERY choice
        - This ensures these products always get upvotes

    4. **Set Up the Results Page**
        - Add two separate Blocks to your [Results Page](/reference/quiz-builder/results-page/):
            1. Product Block: Shows dynamic recommendations based on quiz answers.
            2. Slot Block: shows the most upvoted products from the collection linked to that Slot. Set the block title and description, and adjust how many products to display. Link your new collection in the Included Collections field.

    5. **Test Your Setup**
        - Save and preview the quiz
        - Take the quiz multiple times with different answers
        - Verify that:
            - Dynamic recommendations change based on answers
            - Fixed products always appear in their dedicated Slot


=== "WooCommerce"

    !!! note "Workaround"
        The WooCommerce version of the app has no fixed product recommendations. Two workarounds get you the same result.

    **Option 1: Show the Same Products to Everyone**

    This makes the same products appear for every customer, whatever they answered.

    1. Go to the [Link Products section](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
    2. Choose any question in your quiz
    3. Link your desired fixed products to EVERY choice in that question
    4. These products will now receive upvotes regardless of customer choices
    5. They will appear at the top of the Results Page due to having the most upvotes

    **Option 2: Create a Dedicated Fixed Products Section**

    This combines scored recommendations with fixed products, using a separate product block.

    1. **Create a Collection for Fixed Products**: in Shopify, create a collection holding the products you always want shown.

    2. **Sync Your Store**
        - Go to [Success Checklist](/reference/dashboard/#success-checklist) in the app
        - Click `Sync Catalog` to update your catalog

    3. **Link the Collection**
        - Go to [Link Products](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
        - Select any question in your quiz
        - Link your new collection to EVERY choice
        - This ensures these products always get upvotes

    4. **Set Up the Results Page**
        - Add two separate Blocks to your [Results Page](/reference/quiz-builder/results-page/):
            1. Product Block: Shows dynamic recommendations based on quiz answers.
            2. Slot Block: shows the most upvoted products from the collection linked to that Slot. Set the block title and description, and adjust how many products to display. Link your new collection in the Included Collections field.

    5. **Test Your Setup**
        - Save and preview the quiz
        - Take the quiz multiple times with different answers
        - Verify that:
            - Dynamic recommendations change based on answers
            - Fixed products always appear in their dedicated Slot

=== "Magento"

    !!! note "Workaround"
        The Magento version of the app has no fixed product recommendations. Two workarounds get you the same result.

    **Option 1: Show the Same Products to Everyone**

    This makes the same products appear for every customer, whatever they answered.

    1. Go to the [Link Products section](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
    2. Choose any question in your quiz
    3. Link your desired fixed products to EVERY choice in that question
    4. These products will now receive upvotes regardless of customer choices
    5. They will appear at the top of the Results Page due to having the most upvotes

    **Option 2: Create a Dedicated Fixed Products Section**

    This combines scored recommendations with fixed products, using a separate product block.

    1. **Create a Collection for Fixed Products**: in Shopify, create a collection holding the products you always want shown.

    2. **Sync Your Store**
        - Go to [Success Checklist](/reference/dashboard/#success-checklist) in the app
        - Click `Sync Catalog` to update your catalog

    3. **Link the Collection**
        - Go to [Link Products](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
        - Select any question in your quiz
        - Link your new collection to EVERY choice
        - This ensures these products always get upvotes

    4. **Set Up the Results Page**
        - Add two separate Blocks to your [Results Page](/reference/quiz-builder/results-page/):
            1. Product Block: Shows dynamic recommendations based on quiz answers.
            2. Slot Block: shows the most upvoted products from the collection linked to that Slot. Set the block title and description, and adjust how many products to display. Link your new collection in the Included Collections field.

    5. **Test Your Setup**
        - Save and preview the quiz
        - Take the quiz multiple times with different answers
        - Verify that:
            - Dynamic recommendations change based on answers
            - Fixed products always appear in their dedicated Slot

=== "BigCommerce"

    !!! note "Workaround"
        The BigCommerce version of the app has no fixed product recommendations. Two workarounds get you the same result.

    **Option 1: Show the Same Products to Everyone**

    This makes the same products appear for every customer, whatever they answered.

    1. Go to the [Link Products section](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
    2. Choose any question in your quiz
    3. Link your desired fixed products to EVERY choice in that question
    4. These products will now receive upvotes regardless of customer choices
    5. They will appear at the top of the Results Page due to having the most upvotes

    **Option 2: Create a Dedicated Fixed Products Section**

    This combines scored recommendations with fixed products, using a separate product block.

    1. **Create a Collection for Fixed Products**: in Shopify, create a collection holding the products you always want shown.

    2. **Sync Your Store**
        - Go to [Success Checklist](/reference/dashboard/#success-checklist) in the app
        - Click `Sync Catalog` to update your catalog

    3. **Link the Collection**
        - Go to [Link Products](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
        - Select any question in your quiz
        - Link your new collection to EVERY choice
        - This ensures these products always get upvotes

    4. **Set Up the Results Page**
        - Add two separate Blocks to your [Results Page](/reference/quiz-builder/results-page/):
            1. Product Block: Shows dynamic recommendations based on quiz answers.
            2. Slot Block: shows the most upvoted products from the collection linked to that Slot. Set the block title and description, and adjust how many products to display. Link your new collection in the Included Collections field.

    5. **Test Your Setup**
        - Save and preview the quiz
        - Take the quiz multiple times with different answers
        - Verify that:
            - Dynamic recommendations change based on answers
            - Fixed products always appear in their dedicated Slot

=== "Standalone"

    !!! note "Workaround"
        The Standalone version of the app has no fixed product recommendations. Two workarounds get you the same result.

    **Option 1: Show the Same Products to Everyone**

    This makes the same products appear for every customer, whatever they answered.

    1. Go to the [Link Products section](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
    2. Choose any question in your quiz
    3. Link your desired fixed products to EVERY choice in that question
    4. These products will now receive upvotes regardless of customer choices
    5. They will appear at the top of the Results Page due to having the most upvotes

    **Option 2: Create a Dedicated Fixed Products Section**

    This combines scored recommendations with fixed products, using a separate product block.

    1. **Create a Collection for Fixed Products**: in Shopify, create a collection holding the products you always want shown.

    2. **Sync Your Store**
        - Go to [Success Checklist](/reference/dashboard/#success-checklist) in the app
        - Click `Sync Catalog` to update your catalog

    3. **Link the Collection**
        - Go to [Link Products](/reference/quiz-builder/link-products/) in [Quiz Builder](/reference/quiz-builder/)
        - Select any question in your quiz
        - Link your new collection to EVERY choice
        - This ensures these products always get upvotes

    4. **Set Up the Results Page**
        - Add two separate Blocks to your [Results Page](/reference/quiz-builder/results-page/):
            1. Product Block: Shows dynamic recommendations based on quiz answers.
            2. Slot Block: shows the most upvoted products from the collection linked to that Slot. Set the block title and description, and adjust how many products to display. Link your new collection in the Included Collections field.

    5. **Test Your Setup**
        - Save and preview the quiz
        - Take the quiz multiple times with different answers
        - Verify that:
            - Dynamic recommendations change based on answers
            - Fixed products always appear in their dedicated Slot

## Fixed recommendations with display logic and one results page

Set up multiple sections on the results page with fixed product and text combinations, then control visibility of each section with Display Logic display rules.

![docs/images/how_to_shopify_v2_recommendations_displaylogic.png](/images/how_to_shopify_v2_recommendations_displaylogic.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/NvDLDlknJv4?si=x9HaGPZxsjDwTrY-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Add content sections to the Results page**: go to the [Results page](/reference/quiz-builder/results-page/) and click `+ Add section`.

        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 display logic sections](/images/how_to_shopifyv2_fixedrecommendationquiz_sectionsresultspage.png)

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Product blocks**: add a `Product Block` to each section, holding the products for that skin type. Set the `Recommendation system` to `Fixed Recommendations` in the [Product block Settings](/reference/quiz-builder/results-page/#product-product-variants-collections).

        ![how to recommend products fixed recommendations resultspage](/images/how_to_shopifyv2_fixedrecommendationquiz_fixedrecommendationsresultspage.png)

        In the `Slot` settings, set the maximum number of products and choose which ones to show.

        ![how to recommend products fixed recommendations resultspage2](/images/how_to_shopifyv2_fixedrecommendationquiz_fixedrecommendationsresultspage2.png)


    4. **Add Display logic**: without [Display logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results page, whatever the customer answered.

        Select a content block, find `Display logic` in the right-hand menu, and click `+ Add condition (OR)`.

        Set up IF-THEN statements that show or hide each block based on the customer's answers:

        ![how to hide content with logic display logic statement](/images/how_to_shopifyv2_fixedrecommendationquiz_displaylogic.png)

    5. **Publish the changes**: click the top-right `Save` button to update the preview and the live quiz.


=== "Shopify (Legacy)"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    3. **Add Display Logic**: without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

        Select a content block, click `display logic`, then `add display logic`. Set up IF-THEN statements that show or hide each block based on the customer's answers.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    3. **Add Display Logic**: without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

        Select a content block, click `display logic`, then `add display logic`. Set up IF-THEN statements that show or hide each block based on the customer's answers.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    3. **Add Display Logic**: without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

        Select a content block, click `display logic`, then `add display logic`. Set up IF-THEN statements that show or hide each block based on the customer's answers.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    3. **Add Display Logic**: without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

        Select a content block, click `display logic`, then `add display logic`. Set up IF-THEN statements that show or hide each block based on the customer's answers.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.


        !!! tip

            Make the heading stand out with [Markdown](/how-to-guides/use-markdown/). A `#` before a line turns it into a heading, and `**` around text makes it bold.

    3. **Add Display Logic**: without [Display Logic](/how-to-guides/use-display-logic/), every block appears one after another on the Results Page, whatever the customer answered.

        Select a content block, click `display logic`, then `add display logic`. Set up IF-THEN statements that show or hide each block based on the customer's answers.

        ![how to hide content with logic display logic statement](/images/how_to_hide_content_with_logic_display_logic_statement.png)

    4. **Publish the changes**: click the top-right `Publish` button to update the preview and the live quiz.

## Fixed recommendations with display logic and multiple results pages

Give each results page its own fixed products and its own text. Jump Logic then sends each customer to the right page.

!!! note

    The previous method uses one results page, holding several content and product blocks that Display Logic shows or hides. This method uses several results pages, and Jump Logic decides which one the customer reaches.

    Overall, both methods are the same, the difference is only in where you add the conditional logic (Display Logic vs Jump Logic).

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/uLqul_uj0UQ?si=E77WIlpSvtjC4w7R" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Create Quiz**: Open the [Quiz builder](/reference/quiz-builder/) and add a `Multiple-choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin.

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Multiple Results pages**: In the [Results page](/reference/quiz-builder/results-page/) tab, click on the `+ Add Results Page` button to create additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

    3. **Add Content to Each Results page**: on each results page, add content blocks describing that skin type. For example:

        ![how to set up multiple results pages](/images/how_to_shopifyv2_fixedrecommendationquiz_resultpages.png)

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product blocks to Each Results page**: add a `Products Block` to each results page, holding the products for that skin type.

        To each block add a `Product Block` with the products you want to recommend for that skin type. Make sure to set the `Recommendation system` to `Fixed Recommendations` in the [Product block Settings](/reference/quiz-builder/results-page/#product-product-variants-collections).  +

        ![how to recommend products fixed recommendations resultspage](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_fixedrecommendationsresultspage.png)

        Then go to Slot settings and select the max. number of products to show and select which products to show.

        ![how to recommend products fixed recommendations resultspage2](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_fixedrecommendationsresultspage2.png)


    5. **Set Up Jump logic**: Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and pick the last question in the quiz. Set up [Jump logic](/how-to-guides/hide-content-with-logic/#jump-logic-how-to-show-custom-text-in-the-quiz) to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_jumplogic.png)

        Open the Jump logic options and add new rules to this question. Click `+ Add another rule (OR)` to add a new OR Jump logic rule for the selected question.


        !!! example

            ![manual_shopifyV2_quizbuilder_quizbuilder_conditionallogic_jumplogic_example](/images/how_to_shopifyv2_fixedrecommendationquiz_mrp_jumplogic_example.png)

            In the example, if a user chooses a choice "Not too oily..." in Question 4 "SKIN TYPE" then they will be redirected to Results page 2.

        !!! tip

            For each choice in your skin type question, create a Jump logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.


=== "Shopify (Legacy)"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple-choice questions` asking the customer about their needs.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.

    3. **Add Content to Each Results Page**: on each results page, add a Product Block and content describing that skin type. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: use Jump Logic to branch the quiz. **Link the recommended products to the choices in the last question of each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab. Set up Jump Logic to send each customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple-choice questions` asking the customer about their needs.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.

    3. **Add Content to Each Results Page**: on each results page, add a Product Block and content describing that skin type. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: use Jump Logic to branch the quiz. **Link the recommended products to the choices in the last question of each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab. Set up Jump Logic to send each customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple-choice questions` asking the customer about their needs.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.

    3. **Add Content to Each Results Page**: on each results page, add a Product Block and content describing that skin type. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: use Jump Logic to branch the quiz. **Link the recommended products to the choices in the last question of each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab. Set up Jump Logic to send each customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple-choice questions` asking the customer about their needs.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.

    3. **Add Content to Each Results Page**: on each results page, add a Product Block and content describing that skin type. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: use Jump Logic to branch the quiz. **Link the recommended products to the choices in the last question of each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab. Set up Jump Logic to send each customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add your `Multiple-choice questions` asking the customer about their needs.

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each result (for example, based on skin type (Dry, Normal, Oily, Combination)).

        !!! tip

            Check this article [Set Multiple Results Pages](/how-to-guides/set-multiple-result-pages/) to learn how to set up multiple results pages.

    3. **Add Content to Each Results Page**: on each results page, add a Product Block and content describing that skin type. For example:

        !!! example

            - *You have Dry Skin*: the itchiness, the tightness, the dryness. Your skin wants a routine that is deeply nourishing and hydrating.
            - *You have Normal Skin*: your skin feels balanced, just like you. It has no major issues, and it still deserves care. Your skin wants a routine that keeps that balance.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Branch your quiz**: use Jump Logic to branch the quiz. **Link the recommended products to the choices in the last question of each branch**.

        Stage 1:

        ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

        Stage 2:

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_branching.png)

    5. **Set Up Jump Logic**: open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab. Set up Jump Logic to send each customer to the results page that matches their answers.

        ![how to recommend products complex matrix logic tree](/images/how_to_shopifyv_fixedrecommendationquiz_mrp_resultsjumps.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

---
This article explains how to set up a quiz with fixed recommendations or recommendations controlled by strict Display Logic rules.