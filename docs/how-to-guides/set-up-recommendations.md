---
icon: material/cards
---

# How to Set Up Recommendations

Product recommendations are the heart of any successful quiz experience. They help guide customers to the perfect products for their needs, increasing conversion rates and customer satisfaction. In this guide, we'll explore different recommendation systems that can be implemented in your RevenueHunt quiz, each designed for different use cases and business needs.

| Recommendation System | Best For | Key Features | Complexity |
|----------------------|----------|--------------|------------|
| ✍🏻 Voting System | Most quizzes, especially product finders | - Dynamic product recommendations<br>- Adapts to product catalog changes<br>- Works as a funnel | Low to Medium |
| 🧩 Fixed Recommendations | Complex branching quizzes | - Pre-determined product sections<br>- Precise control over outcomes<br>- Multiple results pages | Medium |
| 🎯 Custom Scoring System | Personality-type quizzes | - Weighted scoring system<br>- Nuanced recommendations<br>- Variable outcomes | Medium to High |


## ✍🏻 Voting System


Recommended for most quizzes. The voting system counts product "votes" based on customer quiz choices and recommends products with the highest votes.

!!! note "Benefits of the Voting System Algorithm"  

    - Most versatile solution that adapts to changes in your product catalog
    - Always recommends top products based on customer choices
    - Works as a funnel to effectively narrow down product selection

### Funnel Quiz

The voting system counts product "votes" based on customer quiz choices and recommends products with the highest votes.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png) 

Product recommendation algorithm works like a voting system:

- Product variants are linked to each choice.
- When a customer picks a choice, all linked products receive one vote.
- After the customer takes the quiz, the results page will show the most voted product variants sorted by the number of votes.
- If no products have been linked or all the products have been excluded, the results page will appear empty.
- If there's a draw in the number of votes, the app will randomize the order of products.
- You can limit recommendations to a specific number of products or a minimum vote threshold
- Supports arranging recommendations into Slots to recommend complete product routines

!!! tip "How to set this up?"

    Check out the [Set Up Funnel Quiz](/how-to-guides/set-up-funnel-quiz/) guide.



### Funnel Quiz with Branching

Branch your quiz to show different follow-up questions based on customer choices. The algorithm counts votes only from questions and answers shown to each customer.

  ![how_to_shopify_v2_recommendations_jumplogic](/images/how_to_shopify_v2_recommendations_jumplogic.png)

!!! tip "How to set this up?"

    Check out the [Jump Logic Quiz](/how-to-guides/hide-content-with-logic/#jump-logic-how-to-show-custom-text-in-the-quiz) guide.

### Funnel Quiz that Skips Slides

Show different follow-up questions based on customer choices in a multiple-choice, multiple selection question. For example, ask about skin concerns and then only show follow-up questions related to the selected concerns. The algorithm counts votes only from questions and answers shown to each customer. 

![how_to_shopify_v2_recommendations_skiplogic.png](/images/how_to_shopify_v2_recommendations_skiplogic.png)

![how_to_hide_content_with_logic_shopifyv2_skip_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

!!! tip "How to set this up?"

    Check out the [Skip Logic Quiz](/how-to-guides/hide-content-with-logic/#skip-logic-how-to-show-custom-text-in-the-quiz) and [Funnel Quiz that Skips Slides](/how-to-guides/set-up-funnel-quiz/#funnel-quiz-that-skips-slides) guides.

### Funnel Quiz that Shows Custom Text Based on Choices

Show or hide different text blocks on the results page. This approach requires predicting every possible answering route and adding display logic rules for each text block. 

![how_to_shopify_v2_recommendations_funnel_blocklogic](/images/how_to_shopify_v2_recommendations_funnel_blocklogic.png)

!!! tip "How to set this up?"

    Check out the [Display Logic Quiz](/how-to-guides/hide-content-with-logic/#block-logic-how-to-show-custom-text-on-the-results-page) guide.

!!! warning "Not recommended for personality-type quizzes"

    Not recommended for personality-type quizzes due to complexity. For this application, try the [Custom Scoring System](/how-to-guides/custom-scoring-system/) solution.


## 🧩 Fixed Recommendations

Recommended for quizzes with complex branching. Set up fixed sections with pre-determined products to be shown on the results page. Then add logic to control visibility of each section or results page.

!!! info "Benefits"

    - Good for complex branching quizzes with multiple very precise outcomes and product recommendations.

### One Results Page 

**Option 1:** Set up multiple sections on the results page with fixed product and text combinations, then control visibility of each section with Display Logic display rules.

![docs/images/how_to_shopify_v2_recommendations_blocklogic.png](/images/how_to_shopify_v2_recommendations_blocklogic.png)

!!! tip "How to set this up?"

    Check out the [Set Up Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#one-results-page) guide.

### Multiple Results Pages

**Option 2:** Set up multiple results pages with unique fixed product recommendations and texts and control visbility by adding branching with Jump Logic that leads to diferent results pages.	

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png)

!!! tip "How to set this up?"

    Check out the [Set Up Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/#multiple-results-pages) guide.

## 🎯 Custom Scoring System 

Recommended for personality-type quizzes. Assign point values to choices and use the total scores to determine which products to recommend.

!!! info "Benefits"

    - Personality quizzes with variable outcomes
    - When you need to weigh different factors with varying importance
    - Creating nuanced recommendation categories

### Winning Variable Quiz

Assign variables and scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the most voted varaible.

![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_varaiblequiz.png)

!!! tip "How to set this up?"

    Check out the [Set Up Scoring System Quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) guide.



### One Results Page

Assign numerical scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the accumulated scores.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png)


!!! tip "How to set this up?"

    Check out the [Set Up Scoring System Quiz](/how-to-guides/set-up-scoring-quiz/#one-results-page) guide.


### Multiple Results Pages

Assign numerical scores to each choice in your quiz. Then, use Jump Logic or Skip Logic to direct customers to different results pages based on their accumulated scores. 

![how_to_shopify_v2_recommendations_scoring_logic](/images/how_to_shopify_v2_recommendations_scoring_logic.png)

!!! tip "How to set this up?"

    Check out the [Set Up Scoring System Quiz](/how-to-guides/set-up-scoring-quiz/#multiple-results-pages) guide.

---

This how-to article explains different ways to set up product recommendations in the RevenueHunt app.

