---
icon: material/cards
description: "Learn how RevenueHunt product recommendation algorithm works and how to configure personalized recommendations."
---

# How to Recommend Products

The RevenueHunt app takes into account your customer's choices to offer highly personalized product recommendations.

This guide explains how to recommend products with the RevenueHunt app, the underlying algorithm and proposes solutions for complex quizzes.

## Recommendations

=== "Shopify"

    The RevenueHunt app can show on the results page **product variants**, **main products** and **collections**.

    If you add a Block to your results page, you can choose to display **product variants**, **main products** or **collections** under [Block settings > Recommendations Type](/reference/quiz-builder/results-page/#product-product-variants-collections).

    - If you chose **Products** under Recommendations Type, the Slot shows the main product, with an optional dropdown for choosing a variant. The order in which the product variants are displayed is based on the number of upvotes they received. If all variants of the same product received the same number of upvotes, the variants will be displayed in random order.

    - If you chose **Product Variants** under Recommendations Type, the Slot shows the recommended variants. Each carries the product name followed by the variant name, such as "Toner - 100ml".

        !!! note

            This option cannot show the variants in a dropdown. It sends the customer straight to one variant of a product. To show the variants in a dropdown, use the **Products** option instead.

    - If you chose **Collections** under Recommendations Type, the Slot shows the recommended collection from your Shopify store.

        !!! note

            If a recommended collection has no image, add one in Shopify > Products > Collections. The collection then shows that image on the results page.

=== "Shopify (Legacy)"

    The RevenueHunt app can show on the results page **product variants**, **main products** and **[Recharge subscription products](/how-to-guides/recommend-subscription-products/)**.

    The RevenueHunt app **cannot recommend collections** of products, though you can [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

=== "WooCommerce"

    The RevenueHunt app can show on the results page **simple products**, **variable products**, **grouped products**, **external/affiliate products** and **[WooCommerce subscription products](/how-to-guides/recommend-subscription-products/)**.

    The RevenueHunt app **cannot recommend categories** of products, though you can [only recommend products from a specific category/tag/attribute](/how-to-guides/recommend-skincare-routine-slots/).

    !!! warning

        The RevenueHunt app syncs only one type of variant of a variable product. If a product has both size and color variants, only one of the two is synced.

=== "Magento"

    The RevenueHunt app can show on the results page **product variants** and **main products**.

    The RevenueHunt app **cannot recommend categories** of products, though you can [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

=== "BigCommerce"

    The RevenueHunt app can show on the results page **product variants** and **main products**.

    The RevenueHunt app **cannot recommend categories** of products, though you can [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

=== "Standalone"

    The RevenueHunt app can show on the results page **product variants** and **main products**.

    The RevenueHunt app **cannot recommend collections** of products, though you can [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

## Recommending the right products

=== "Shopify"

    In the `💎Built for Shopify` version of the RevenueHunt app, there are several ways to recommend products:

    **✍🏻 Option 1: Recommend Most Upvoted Products**

    *Best for most quizzes.*

    ![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width="300"}

    - Link products or collections to each quiz choice.
    - On the results page, add a product block that displays the most upvoted items.
    - You can show multiple product slots to recommend a routine or bundle.

    !!! note

        Follow [How to Set Up Funnel Quiz](/how-to-guides/set-up-funnel-quiz/) to learn how to set up this option.

    **🎯 Option 2: Use Scoring or Variables**

    *Best for personality-style quizzes.*

    ![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_variablequiz.png){width="300"}

    - Assign a score or custom variable to each choice in the quiz.
    - Set up result sections with fixed recommendations for each type of outcome.
    - Use display logic to show the right section based on the score or variable with the highest value.
    - **Example:** Show Section A if the top variable is "blue", Section B if it is "red".

    !!! note

        Follow [How to Set Up Scoring Quiz](/how-to-guides/set-up-scoring-quiz/) to learn how to set up this option.

    **🧩 Option 3: Use Complex Display logic**

    *Best for advanced logic or detailed recommendation matrices.*

    ![how_to_shopify_v2_recommendations_displaylogic](/images/how_to_shopify_v2_recommendations_displaylogic.png){width="300"}

    - Create logic-based paths that lead users to different results pages.
    - Or use one results page with multiple sections and display logic for each.
    - Show/hide each section depending on the customer’s answers.

    !!! note

        Follow [How to Set Up Fixed Recommendations Quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up this option.

=== "Shopify (Legacy)"

    Follow these steps to set up product recommendations in your quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: A `Product Block` shows products as a list. A `Product Slot Block` shows them in steps. For a first quiz, use a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-upvoted product from a collection linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you created in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section. It shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](/how-to-guides/set-up-funnel-quiz/#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    Link product variants and collections to quiz choices, and understand the inclusion and exclusion logic. The algorithm then offers precise recommendations.

=== "WooCommerce"

    Follow these steps to set up product recommendations in your quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: A `Product Block` shows products as a list. A `Product Slot Block` shows them in steps. For a first quiz, use a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-upvoted product from a collection linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you created in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section. It shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](/how-to-guides/set-up-funnel-quiz/#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    Link product variants and collections to quiz choices, and understand the inclusion and exclusion logic. The algorithm then offers precise recommendations.

=== "Magento"

    Follow these steps to set up product recommendations in your quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: A `Product Block` shows products as a list. A `Product Slot Block` shows them in steps. For a first quiz, use a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-upvoted product from a collection linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you created in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section. It shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](/how-to-guides/set-up-funnel-quiz/#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    Link product variants and collections to quiz choices, and understand the inclusion and exclusion logic. The algorithm then offers precise recommendations.

=== "BigCommerce"

    Follow these steps to set up product recommendations in your quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: A `Product Block` shows products as a list. A `Product Slot Block` shows them in steps. For a first quiz, use a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-upvoted product from a collection linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you created in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section. It shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](/how-to-guides/set-up-funnel-quiz/#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    Link product variants and collections to quiz choices, and understand the inclusion and exclusion logic. The algorithm then offers precise recommendations.

=== "Standalone"

    Follow these steps to set up product recommendations in your quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: A `Product Block` shows products as a list. A `Product Slot Block` shows them in steps. For a first quiz, use a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-upvoted product from a collection linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you created in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section. It shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](/how-to-guides/set-up-funnel-quiz/#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    Link product variants and collections to quiz choices, and understand the inclusion and exclusion logic. The algorithm then offers precise recommendations.

## How to build your quiz setup

=== "Shopify"

    ![how_to_recommend_products_decision_tree_V2](/images/how_to_recommend_products_decision_tree_V2.png)

    | Recommendation System | Best For | Key Features | Complexity |
    |------------------------|----------|--------------|------------|
    | [🧩 Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations) | Showing the same product(s) to everyone regardless of answers | - Simple setup<br>- Products always shown<br>- No logic or conditions | Very Low |
    | [✍🏻 Upvoting System (Funnel Quiz)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz) | Most quizzes, especially product finders or large catalogs | - Automatically adapts to answers<br>- Simple linking of products to choices<br>- Randomized tie-breaking | Low to Medium |
    | [✍🏻 Upvoting System (Funnel Quiz with Slots)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-with-slots) | Product recommendation routines, different product categories (e.g. cleanser + moisturizer) | - Slot-based grouping<br>- Step-by-step product recommendations<br>- Still uses dynamic upvoting | Medium |
    | [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) | Personality quizzes, Dosha tests, where outcome depends on which variable (A, B, C...) got the most choices | - Tracks most frequent variable<br>- Outputs results by majority<br>- Often used for typology quizzes | Medium |
    | [🎯 Custom Scoring System (Score + Variable)](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page) | Quizzes that need to calculate values or mix scoring with conditions | - Weighted scoring<br>- Adds hidden variables<br>- Logic can combine score + other rules | Medium to High |
    | [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-one-results-page) | Quizzes with a lot of logic conditions, precise rules, or exceptions | - Shows products based on answers<br>- Supports multiple results pages<br>- Allows display rules and custom text | High |

=== "Shopify (Legacy)"

    Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "WooCommerce"

    Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "Magento"

    Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "BigCommerce"

    Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "Standalone"

    Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

## Specific setup guides

### Recommend products from a number or a date

An open-ended Number or Date question cannot drive recommendations. Set up finite choices instead, so the answers can decide what is recommended.

[How to Recommend Products Based on Numerical Inputs](/how-to-guides/recommend-products-based-on-numerical-inputs/)

### Recommend products that match multiple criteria

Use a product matrix when two answers together decide the recommendation, such as age and skin type.

[How to Recommend Products That Match Multiple Criteria](/how-to-guides/recommend-product-matrix/)

### Only recommend products with X upvotes or more

Limit the recommendations to products that received X upvotes or more, so only the strongest matches appear.

[How to Only Recommend Products with X Upvotes or More](/how-to-guides/only-recommend-products-with-minimum-votes/)

### Recommend products by how many choices the customer picked

Recommend a different group of products depending on how many choices the customer selected. This needs custom JavaScript.

[How to Recommend Products Based on Number of User Choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/)

### Always recommend a specific product

Keep a product on the Results Page whatever the customer answers.

[Always the same recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations)

### Recommend subscription products

=== "Shopify"

    Add the `Subscription` component to the [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) on your results page, then pick your subscription app. Shopify Subscriptions and Recharge Subscriptions (Plus plan only) are supported.

    [How to Recommend Subscription Products](/how-to-guides/recommend-subscription-products/)


=== "Shopify (Legacy)"

    If you use a legacy version of the RevenueHunt app for Shopify with Recharge Subscriptions, see [How to Recommend Subscription Products](/how-to-guides/recommend-subscription-products/).

    ![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png){width="150"}

    For other subscription apps check [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) to learn of a possible workaround.


=== "WooCommerce"

    If you use WooCommerce Subscriptions, see [How to Recommend Subscription Products](/how-to-guides/recommend-subscription-products/#woocommerce-subscriptions) to learn how to recommend subscription products directly from the quiz.

    ![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png){width="150"}

    For other subscription apps check [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) to learn of a possible workaround.


=== "BigCommerce"

    The RevenueHunt app for BigCommerce does not yet support recommending subscription products.

    Check [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) to learn of a possible workaround.


=== "Magento"

    The RevenueHunt app for Magento does not yet support recommending subscription products.

    Check [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) to learn of a possible workaround.


=== "Standalone"

    The RevenueHunt app for Headless ecommerce (Standalone) does not yet support recommending subscription products.

    Check [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) to learn of a possible workaround.


### Show results explanation

The recommendation algorithm picks the products. It does not explain **why** a product was recommended, and it does not show custom text for a recommended product.

=== "Shopify"

    To show text that explains why a product was recommended, follow one of two guides. For a personality-type quiz, see [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). For a quiz with many logic conditions, precise rules or exceptions, see [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-one-results-page).

=== "Shopify (Legacy)"

    That makes a "personality-type" quiz hard to build in the legacy app.

    For a legacy version of the RevenueHunt app, on any platform, see the workarounds in [How to Show Results Explanation](/how-to-guides/show-results-explanation/).


=== "WooCommerce"

    That makes a "personality-type" quiz hard to build in the legacy app.

    For a legacy version of the RevenueHunt app, on any platform, see the workarounds in [How to Show Results Explanation](/how-to-guides/show-results-explanation/).


=== "Magento"

    That makes a "personality-type" quiz hard to build in the legacy app.

    For a legacy version of the RevenueHunt app, on any platform, see the workarounds in [How to Show Results Explanation](/how-to-guides/show-results-explanation/).


=== "BigCommerce"

    That makes a "personality-type" quiz hard to build in the legacy app.

    For a legacy version of the RevenueHunt app, on any platform, see the workarounds in [How to Show Results Explanation](/how-to-guides/show-results-explanation/).


=== "Standalone"

    That makes a "personality-type" quiz hard to build in the legacy app.

    For a legacy version of the RevenueHunt app, on any platform, see the workarounds in [How to Show Results Explanation](/how-to-guides/show-results-explanation/).


---
This article explains which products the RevenueHunt app can recommend, and how to set up a quiz to recommend them.