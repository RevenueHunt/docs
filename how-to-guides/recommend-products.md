---
icon: material/cards
description: "Learn how RevenueHunt product recommendation algorithm works and how to configure personalized recommendations."
---

# How to Recommend Products

The RevenueHunt app reads the choices a customer makes and recommends products to match them.

This page explains what a quiz can recommend, which recommendation system to pick, and where to find the guide for each one.

## What a quiz can recommend

=== "Shopify"

    The results page can show **product variants**, **main products** and **collections**.

    Pick which one in [Block settings > Recommendations Type](/reference/quiz-builder/results-page/#product-product-variants-collections).

    | Recommendations Type | What the slot shows |
    |---|---|
    | **Products** | The main product, with an optional dropdown for choosing a variant. Variants are ordered by upvote count, and variants on equal upvotes appear in random order. |
    | **Product Variants** | The recommended variants. Each one carries the product name followed by the variant name, such as "Toner - 100ml". |
    | **Collections** | The recommended collection from your Shopify store. |

    !!! info "Product Variants sends the customer straight to one variant"

        This type cannot offer the variants in a dropdown. Use **Products** when the customer should choose the variant themselves.

    !!! tip "Give your collections an image"

        A recommended collection with no image shows none on the results page. Add one in Shopify under `Products` > `Collections`.

=== "Shopify (Legacy)"

    The Results Page can show **product variants**, **main products** and **[Recharge subscription products](/how-to-guides/recommend-subscription-products/)**.

    This version **cannot recommend collections** of products. You can, however, [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

=== "WooCommerce"

    The Results Page can show **simple products**, **variable products**, **grouped products**, **external/affiliate products** and **[WooCommerce subscription products](/how-to-guides/recommend-subscription-products/)**.

    This version **cannot recommend categories** of products. You can, however, [only recommend products from a specific category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    !!! warning "One variant type per product"

        The app syncs only one type of variant per variable product. If a product varies by both size and color, only one of the two is synced.

=== "Magento"

    The Results Page can show **product variants** and **main products**.

    This version **cannot recommend categories** of products. You can, however, [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

=== "BigCommerce"

    The Results Page can show **product variants** and **main products**.

    This version **cannot recommend categories** of products. You can, however, [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

=== "Standalone"

    The Results Page can show **product variants** and **main products**.

    This version **cannot recommend collections** of products. You can, however, [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

## Choose a recommendation system

=== "Shopify"

    ![how_to_recommend_products_decision_tree_V2](/images/how_to_recommend_products_decision_tree_V2.png)

    There are three families to choose from.

    **Recommend the most upvoted products.** Best for most quizzes. Link products or collections to each choice, then add a products block that shows the most upvoted items. Slots can split them into a routine or a bundle.

    ![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width="300"}

    [How to set up a funnel quiz](/how-to-guides/set-up-funnel-quiz/)

    **Score the answers, or count variables.** Best for personality-style quizzes. Give each choice a score or a variable, then build a results section per outcome. Display logic shows the section that matches the highest total.

    ![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_variablequiz.png){width="300"}

    [How to set up a scoring quiz](/how-to-guides/set-up-scoring-quiz/)

    **Choose the products for each outcome yourself.** Best for a detailed recommendation matrix. Build a section or a results page per outcome, then use display logic or jump logic to decide which one the customer reaches.

    ![how_to_shopify_v2_recommendations_displaylogic](/images/how_to_shopify_v2_recommendations_displaylogic.png){width="300"}

    [How to set up a fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/)

    All six variants, with the effort each one takes:

    | Recommendation System | Best For | Key Features | Complexity |
    |------------------------|----------|--------------|------------|
    | [🧩 Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations) | Showing the same product(s) to everyone regardless of answers | - Simple setup<br>- Products always shown<br>- No logic or conditions | Very Low |
    | [✍🏻 Upvoting System (Funnel Quiz)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz) | Most quizzes, especially product finders or large catalogs | - Automatically adapts to answers<br>- Simple linking of products to choices<br>- Randomized tie-breaking | Low to Medium |
    | [✍🏻 Upvoting System (Funnel Quiz with Slots)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-with-slots) | Product recommendation routines, different product categories (e.g. cleanser + moisturizer) | - Slot-based grouping<br>- Step-by-step product recommendations<br>- Still uses dynamic upvoting | Medium |
    | [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) | Personality quizzes, Dosha tests, where outcome depends on which variable (A, B, C...) got the most choices | - Tracks most frequent variable<br>- Outputs results by majority<br>- Often used for typology quizzes | Medium |
    | [🎯 Custom Scoring System (Score + Variable)](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page) | Quizzes that need to calculate values or mix scoring with conditions | - Weighted scoring<br>- Adds hidden variables<br>- Logic can combine score + other rules | Medium to High |
    | [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-one-results-page) | Quizzes with a lot of logic conditions, precise rules, or exceptions | - Shows products based on answers<br>- Supports multiple results pages<br>- Allows display rules and custom text | High |

=== "Shopify (Legacy)"

    This version recommends products with the upvoting system. You link products to choices, and the Results Page shows the products with the most upvotes first.

    [How to set up a funnel quiz](/how-to-guides/set-up-funnel-quiz/#funnel-quiz)

    Take the quiz to work out which setup you need, or use the guides in [Specific setup guides](#specific-setup-guides).

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "WooCommerce"

    This version recommends products with the upvoting system. You link products to choices, and the Results Page shows the products with the most upvotes first.

    [How to set up a funnel quiz](/how-to-guides/set-up-funnel-quiz/#funnel-quiz)

    Take the quiz to work out which setup you need, or use the guides in [Specific setup guides](#specific-setup-guides).

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "Magento"

    This version recommends products with the upvoting system. You link products to choices, and the Results Page shows the products with the most upvotes first.

    [How to set up a funnel quiz](/how-to-guides/set-up-funnel-quiz/#funnel-quiz)

    Take the quiz to work out which setup you need, or use the guides in [Specific setup guides](#specific-setup-guides).

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "BigCommerce"

    This version recommends products with the upvoting system. You link products to choices, and the Results Page shows the products with the most upvotes first.

    [How to set up a funnel quiz](/how-to-guides/set-up-funnel-quiz/#funnel-quiz)

    Take the quiz to work out which setup you need, or use the guides in [Specific setup guides](#specific-setup-guides).

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "Standalone"

    This version recommends products with the upvoting system. You link products to choices, and the Results Page shows the products with the most upvotes first.

    [How to set up a funnel quiz](/how-to-guides/set-up-funnel-quiz/#funnel-quiz)

    Take the quiz to work out which setup you need, or use the guides in [Specific setup guides](#specific-setup-guides).

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

## Specific setup guides

### Recommend products from a number or a date

An open-ended Number or Date question cannot drive recommendations. Set up finite choices instead, so the answers can decide what is recommended.

[How to recommend products based on numerical inputs](/how-to-guides/recommend-products-based-on-numerical-inputs/)

### Recommend products that match multiple criteria

Use a product matrix when two answers together decide the recommendation, such as age and skin type.

[How to recommend products that match multiple criteria](/how-to-guides/recommend-product-matrix/)

### Only recommend products with X upvotes or more

Limit the recommendations to products that received X upvotes or more, so only the strongest matches appear.

[How to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/)

### Recommend products by how many choices the customer picked

Recommend a different group of products depending on how many choices the customer selected. This needs custom JavaScript.

[How to recommend products based on the number of choices](/how-to-guides/recommend-products-based-on-number-of-user-choices/)

### Always recommend a specific product

Keep a product on the Results Page whatever the customer answers.

[Always the same recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations)

### Recommend subscription products

=== "Shopify"

    Add the `Subscription` component to the [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) on your results page, then pick your subscription app. Shopify Subscriptions and Recharge Subscriptions (Plus plan only) are supported.

    [How to recommend subscription products](/how-to-guides/recommend-subscription-products/)

=== "Shopify (Legacy)"

    If you use a legacy version of the RevenueHunt app for Shopify with Recharge Subscriptions, see [how to recommend subscription products](/how-to-guides/recommend-subscription-products/).

    ![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png){width="150"}

    For other subscription apps, see [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) for a possible workaround.

=== "WooCommerce"

    If you use WooCommerce Subscriptions, see [how to recommend subscription products](/how-to-guides/recommend-subscription-products/).

    ![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png){width="150"}

    For other subscription apps, see [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) for a possible workaround.

=== "Magento"

    !!! note "Not available on this platform"

        This version of the app cannot recommend subscription products.

    See [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) for a possible workaround.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version of the app cannot recommend subscription products.

    See [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) for a possible workaround.

=== "Standalone"

    !!! note "Not available on this platform"

        This version of the app cannot recommend subscription products.

    See [Other subscriptions](/how-to-guides/recommend-subscription-products/#other-subscriptions) for a possible workaround.

### Show results explanation

The recommendation algorithm picks the products. It does not explain **why** a product was recommended, and it does not show custom text for a recommended product.

=== "Shopify"

    Two guides cover the text that explains a recommendation. For a personality-type quiz, see [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). For a quiz with many logic conditions, precise rules or exceptions, see [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-one-results-page).

=== "Shopify (Legacy)"

    This version cannot explain a recommendation on its own, which makes a personality-type quiz hard to build. See the workarounds in [how to show results explanation](/how-to-guides/show-results-explanation/).

=== "WooCommerce"

    This version cannot explain a recommendation on its own, which makes a personality-type quiz hard to build. See the workarounds in [how to show results explanation](/how-to-guides/show-results-explanation/).

=== "Magento"

    This version cannot explain a recommendation on its own, which makes a personality-type quiz hard to build. See the workarounds in [how to show results explanation](/how-to-guides/show-results-explanation/).

=== "BigCommerce"

    This version cannot explain a recommendation on its own, which makes a personality-type quiz hard to build. See the workarounds in [how to show results explanation](/how-to-guides/show-results-explanation/).

=== "Standalone"

    This version cannot explain a recommendation on its own, which makes a personality-type quiz hard to build. See the workarounds in [how to show results explanation](/how-to-guides/show-results-explanation/).

---

This article explains which products the RevenueHunt app can recommend, and how to set up a quiz to recommend them.
