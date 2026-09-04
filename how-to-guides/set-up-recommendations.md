---
icon: material/tune
description: "Comprehensive guide to different RevenueHunt recommendation systems for product quizzes."
---

# How to Set Up Recommendations

Every quiz needs a recommendation system. It decides which products a customer sees at the end. The app has three of them, and eleven ways to use them. This page explains what each one does, so you can choose before you build the quiz.

![how_to_recommend_products_decision_tree_V2](/images/how_to_recommend_products_decision_tree_V2.png)

| Recommendation System | Best For | Key Features | Complexity |
|------------------------|----------|--------------|------------|
| [🧩 Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations) | Showing the same product(s) to everyone regardless of answers | - Simple setup<br>- Products always shown<br>- No logic or conditions | Very Low |
| [✍🏻 Upvoting System (Funnel Quiz)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz) | Most quizzes, especially product finders or large catalogs | - Automatically adapts to answers<br>- Simple linking of products to choices<br>- Randomized or collection-based tie-breaking | Low to Medium |
| [✍🏻 Upvoting System (Funnel Quiz with Slots)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-with-slots) | Product recommendation routines, different product categories (e.g. cleanser + moisturizer) | - Slot-based grouping<br>- Step-by-step product recommendations<br>- Still uses dynamic upvoting | Medium |
| [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) | Personality quizzes, Dosha tests, where outcome depends on which variable (A, B, C...) got the most choices | - Tracks most frequent variable<br>- Outputs results by majority<br>- Often used for typology quizzes | Medium |
| [🎯 Custom Scoring System (Score + Variable)](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page) | Quizzes that need to calculate values or mix scoring with conditions | - Weighted scoring<br>- Adds hidden variables<br>- Logic can combine score + other rules | Medium to High |
| [🧩 Fixed Recommendations with Display Logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-one-results-page) | Quizzes with a lot of logic conditions, precise rules, or exceptions | - Shows products based on answers<br>- Supports multiple results pages<br>- Allows display rules and custom text | High |

!!! tip "Not sure which one you need?"

    [Take the quiz and find out!](https://skincarequiz.myshopify.com/#quiz-LKPc6j)

## Upvoting system

Recommended for most quizzes. Each choice upvotes the products linked to it, and the quiz recommends the products with the most upvotes.

!!! info "Use this method for:"

    - Helping customers narrow down a large product catalog
    - Most quizzes, especially product finders
    - Your first product recommendation quiz
    - Quizzes without complex branching

### Funnel quiz

Every customer answers the same questions, and the products with the most upvotes are recommended first.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width=500}

How the algorithm works:

- You link product variants to each choice.
- A customer picks a choice, and every linked product receives one upvote.
- The results page lists the most upvoted variants first.
- You can cap how many products appear, or require a minimum upvote count.

!!! info "Empty results, and ties"

    A results page comes back empty when nothing was linked to the choices the customer made, or when exclusions removed every product that was upvoted.

    When two products have the same number of upvotes, the order depends on your `Catalog mode` setting. Ties are randomized by default. Set `Preserve collection order` in [Settings > Catalog](/reference/app-settings/#catalog) to keep the order of your Shopify collections.

[✍🏻 Upvoting System (Funnel Quiz)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz)

### Funnel quiz with slots

The quiz counts the upvotes, then fills every slot with the highest upvoted product that matches that slot. Use it to recommend a full routine: the most upvoted cleanser, then toner, then serum, then moisturizer.

![how_to_shopify_v2_recommendations_funnel_with_slots](/images/how_to_shopify_v2_recommendations_funnel_with_slots.png){width=500}

[✍🏻 Upvoting System (Funnel Quiz with Slots)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-with-slots)

### Funnel quiz with branching

Branch the quiz so that different answers lead to different follow-up questions. The quiz counts upvotes only from the questions the customer saw.

![how_to_shopify_v2_recommendations_jumplogic](/images/how_to_shopify_v2_recommendations_jumplogic.png){width=500}

[✍🏻 Upvoting System (Funnel Quiz with Branching)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-with-branching) and [Jump Logic](/how-to-guides/hide-content-with-logic/#branch-the-quiz-with-jump-logic)

### Funnel quiz that skips slides

Ask about several concerns in one multiple-choice question, then show only the follow-up questions that match the concerns the customer selected. The quiz counts upvotes only from the questions it showed.

![how_to_shopify_v2_recommendations_skiplogic.png](/images/how_to_shopify_v2_recommendations_skiplogic.png){width=500}

![how_to_hide_content_with_logic_shopifyv2_skip_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

[✍🏻 Upvoting System (Funnel Quiz that Skips Slides)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-that-skips-slides) and [Skip Logic](/how-to-guides/hide-content-with-logic/#skip-a-statement-with-skip-logic)

### Funnel quiz that shows custom text based on choices

Show and hide text blocks on the results page, so the wording matches the answers. Every route through the quiz needs its own display logic rule.

![how_to_shopify_v2_recommendations_funnel_displaylogic](/images/how_to_shopify_v2_recommendations_funnel_displaylogic.png){width=500}

!!! warning "Not the best fit for a personality quiz"

    The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display Logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

[✍🏻 Upvoting System (Funnel Quiz that Shows Custom Text Based on Choices)](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-that-shows-custom-text-based-on-choices) and [Display Logic](/how-to-guides/hide-content-with-logic/#show-a-section-with-display-logic)

## Fixed recommendations

Recommended for quizzes with complex branching and several precise outcomes. You pick the products for each outcome yourself, then add logic that decides which section or results page the customer reaches.

!!! info "Use this method for:"

    - Quizzes that show the same product(s) to everyone regardless of answers
    - Quizzes with multiple very precise outcomes and product recommendations
    - Quizzes with complex branching
    - Quizzes that require a lot of logic conditions and custom text

### Always the same recommendations

Pin the products you choose to the results page. Every customer sees them, whatever they answered.

![how_to_shopify_v2_recommendations_fixedrecommendations](/images/how_to_shopify_v2_recommendations_fixedrecommendations.png){width=500}

[🧩 Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#always-the-same-recommendations)

### Fixed recommendations with display logic and one results page

One results page holds the text and the products for every outcome. Display Logic then shows the ones that match the answers, and hides the rest.

![how_to_shopify_v2_recommendations_displaylogic](/images/how_to_shopify_v2_recommendations_displaylogic.png){width=500}

[🧩 Fixed Recommendations with Display Logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-one-results-page)

### Fixed recommendations with display logic and multiple results pages

Each outcome gets its own results page, with its own products and its own text. Jump Logic sends each customer to the page that matches their answers.

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png){width=500}

[🧩 Fixed Recommendations with Display Logic](/how-to-guides/set-up-fixed-recommendations-quiz/#fixed-recommendations-with-display-logic-and-multiple-results-pages)

## Custom scoring system

Recommended for personality-type quizzes. Give each choice a score or a variable, then let the totals decide what the customer sees.

!!! info "Use this method for:"

    - Personality type quizzes, Dosha quizzes
    - Quizzes that show different results based on the number of choices (for example if the customer chooses most As, Bs, Cs, etc.)
    - Quizzes that show different text results based on choices
    - Quizzes that need to calculate scores that show different products

### Winning variable quiz

Assign a variable to each choice. The variable chosen most often decides the outcome, and Display Logic shows the content and product blocks that match it.

![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_variablequiz.png){width=500}

[🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz)

### Scoring quiz with one results page

Assign a numerical score to each choice. Display Logic then shows or hides the content blocks on one results page, based on the total the customer reached.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png){width=500}

[🎯 Custom Scoring System (Score + Variable)](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-one-results-page)

### Scoring quiz with multiple results pages

Assign a numerical score to each choice. Jump Logic or Skip Logic then sends each customer to the results page that matches their total.

![how_to_shopify_v2_recommendations_scoring_logic](/images/how_to_shopify_v2_recommendations_scoring_logic.png){width=500}

[🎯 Custom Scoring System (Score + Variable)](/how-to-guides/set-up-scoring-quiz/#scoring-quiz-with-multiple-results-pages)

---

This how-to article explains different ways to set up product recommendations in the RevenueHunt app.
