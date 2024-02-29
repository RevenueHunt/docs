# How to Recommend Products

Our solution stands out by leveraging your customer's choices to offer highly personalized product recommendations. This guide explains the underlying algorithm and how to effectively link products to quiz choices.

## The Algorithm: A Voting System

- **Product Links**: Each quiz choice is linked to specific products or collections.
- **Voting**: Selection of a choice results in a "vote" for all linked products.
- **Results**: Post-quiz, products are displayed on the results page, ranked by their vote count.

## Recommending the Right Products

### Step 1: Link Products to Choices

1. **Access the Quiz Builder**: Navigate to the "Link Products" or "Link Collections" tab within your quiz setup.
   
2. **Assign Links**: For each response, you can link:
   - **Product Variants**: Individual variants receive a vote when their linked choice is selected.
   - **Collections**: Every product within a linked collection receives a vote.
   - **All Variants**: Link all variants of a product to a choice. Note: A special setting in Quiz Settings is required for this option.

### Step 2: Understanding Inclusion and Exclusion

- **Inclusion**: Products or collections added in the "include" field are upvoted in the final recommendations.
- **Exclusion**: Use the "exclude" field to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

## Managing Product Recommendations

- **Variants vs. Products**: It's crucial to note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.

- **Exclusion Strategy**: Products added to the "exclude" section will not appear in the recommendation results, allowing for refined control over the outcomes.

## Results and Analysis

- **Results Page**: Displays products sorted by vote count. Products with the same number of votes are randomized in their presentation.
- **Product Logic**: Proper tagging and categorization in your store's collections are vital for accurate recommendations.
- **Investigation Tools**: Use the quiz's built-in search bar in the Responses section to understand why specific products were recommended or not.

## Advanced Settings: Minimum Votes for Recommendation

- **Limiting Recommendations**: You can set a minimum number of votes required for a product to appear in the recommendations.
- **Settings Navigation**: Go to Results Page settings > Advanced and enable the “Minimum number of votes” option.

By meticulously linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can harness our algorithm to offer precise product recommendations. This not only enhances the customer experience but also increases the likelihood of conversion.
