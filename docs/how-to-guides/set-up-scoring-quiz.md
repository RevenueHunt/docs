# Set Up Scoring Quiz

## One Results Page

Assign numerical scores to each choice in your quiz. Then, use Display Logic to control the visibility of content blocks on the Results Page based on the accumulated scores.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png)

How to set this up? Check out the [Set Up Scoring System Quiz](/how-to-guides/set-up-scoring-quiz/) guide.

1. Go to each question in your quiz
2. For each choice, open the choice settings
3. Assign appropriate point values to each choice

**Implementing score-based display logic:**

1. On the Results Page, select a content block
2. In the right-hand menu, locate Display Logic
3. Click on + Add condition (OR)
4. Use "The variable with the highest score..." or "The score of the variable..." option
5. Set up range conditions to control content visibility

!!! example 

    For skin type recommendations:
    - Assign points to choices (Dry: 1, Normal: 2, Oily: 3, Combination: 4, Sensitive: 5)

    Set display logic for content blocks based on total scores:
    - Dry skin content: Score between 5-7 points
    - Normal skin content: Score between 8-12 points
    - Oily skin content: Score between 13-17 points
    - Combination skin content: Score between 18-22 points
    - Sensitive skin content: Score between 23-25 points


## Multiple Results Pages

Assign numerical scores to each choice in your quiz. Then, use Jump Logic or Skip Logic to direct customers to different results pages based on their accumulated scores. 

![how_to_shopify_v2_recommendations_scoring_logic](/images/how_to_shopify_v2_recommendations_scoring_logic.png)
