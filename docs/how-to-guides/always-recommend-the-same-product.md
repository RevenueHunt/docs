
# How to Ensure a Specific Product Always Appears on Your Results Page

This guide provides a clear, step-by-step process to making sure that specific products are always visible on the Results Page of your quiz, regardless of the customer's choices.

!!! warning "Understand the voting system first"

    The backbone of personalized product recommendations is an algorithm that functions like a [voting system](#how-to-recommend-products), where products gain 'votes' based on customer selections in a quiz. The more votes a product has by the end of the quiz, the more likely it is to be displayed on the Results Page. Familiarizing yourself with [this recommendation mechanism](#how-to-recommend-products) is essential for effectively implementing the strategies outlined below.

## Strategy 1: Link Your Product to Every Choice

This approach ensures your chosen product always tops the Results Page by securing the most votes.

1. Access the [Link Products](/reference/quiz-builder/link-products/) section of the Quiz Builder. 
2. Link your selected product with **every choice** available in the quiz. This method guarantees that the product collects votes with each customer selection, ensuring its appearance on the Results Page.

This strategy positions the product at the forefront of the Results Page every time.

## Strategy 2: Use a Dedicated Product Slot

For those looking to highlight a new product or collection without dominating the entire recommendation list, creating a dedicated `Products Slot` on the Results Page offers a balanced solution.

1. **Create a Collection/Category for Your Product(s)**: Group the products you wish to feature in a `New Products` collection/category. For instance, include your `Essentials Makeup Kit COMPLETE` in this collection.

2. **Ensure Your Store Is Synced**: After creating your collection/category or adding new products, [sync the app](/how-to-guides/sync-catalog/).

3. **Link the Collection/Category to Quiz Responses**: Select a quiz question and link your new product or collection/category to **every response option**. This step is crucial as it ensures the product or collection/category receives at least one vote, guaranteeing its appearance on the Results Page regardless of quiz outcomes.

4. **Add a Dedicated Slot on the Results Page**: Edit the [Results Page](/reference/quiz-builder/results-page/) to include a new `Product Slot` specifically for showcasing your selected product or collection/category. This specialized section will exclusively feature items from your chosen collection/category, distinguishing them from the general recommendations.

5. **Link colelction/category to slot**: Make sure to `include` the created collection/category in the `Product Slot`.

5. **Preview and Test Your Setup**: With your dedicated slot in place, click the `Publish` button to update the preview/live quiz. Then, preview the quiz and its results to ensure the new product or collection is displayed as intended. This final step confirms that your selected items are correctly highlighted on the Results Page.

---
By following these detailed steps, you can significantly enhance the visibility of specific products on your website, ensuring they are consistently presented to your customers.
