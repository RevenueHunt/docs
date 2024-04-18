---
icon: material/slot-machine-outline
---

# How to Recommend a Skincare Routine with Slots

With Shop Quiz, it is possible to group products into slots and recommend a product for each step in a beauty routine.

This guide is designed to help merchants effectively use [Product Slot Blocks](https://docs.revenuehunt.com/reference/quiz-builder/#block-types) on the results page to organize product recommendations. 

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

A personalized skincare routine recommendation quiz was chosen as an example to best demonstrate how to work with this feature. See an example of such a Skincare Quiz [here](https://skincarequiz.myshopify.com/#quiz-rkHm6Y).

![how to recommend slots example](/images/how to recommend slots example.png)

## Step 1: Understand Recommendation Mechanism

Make sure that you're familiar with [how the recommendations work](https://docs.revenuehunt.com/how-to-guides/recommend-products/) in Shop Quiz.

??? question "How do I get the right recommendations?"

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products.

    If you want to make the results ultra-precise, you can also:

    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](https://docs.revenuehunt.com/how-to-guides/only-recommend-products-with-minimum-votes/).
    - Use [Exclusions](https://docs.revenuehunt.com/how-to-guides/recommend-products/#understanding-inclusion-and-exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).


It's advised to familiarize yourself with this [voting system](https://docs.revenuehunt.com/how-to-guides/how-to-recommend-products/#voting-system) before working with Product Slots.

## Step 2: Organize Products into Collections

To group products into slots, you’ll need to create new collections in your Shopify store. These collections will be used to group your products on the results page.

1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
2. **Create Collections**: For each category, [create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) with the right products. Each collection should only contain products relevant to its category. For example, 
    - a *Cleansers* collection should have all the cleansing products, a *Toners* collection should have all the toning products, 
    - a *Serums* collection should have all the serums, etc. 
    - You can have more than one collection that includes some of the same products.

    ![how to recommend slots cleansers collection](/images/how to recommend slots cleansers collection.png)

3. **Catalog Sync**: Perform a [catlog sync](https://docs.revenuehunt.com/how-to-guides/sync-catalog/) after creating collections to update Shop Quiz with the latest product collections.

## Step 3: Build the Quiz

1. **Add new quiz**: Go to the app’s [dashboard](https://docs.revenuehunt.com/reference/dashboard/) and click [`add new quiz`](https://docs.revenuehunt.com/reference/dashboard/#new-quiz).
2. **Choose a template**: Choose a pre-defined template or start from scratch. *Tip: There’s are Basic and Advanced Skincare Quiz templates already available.*
3. **Name your quiz**: The name can be edited later.
4.  **Add slides**: After that, you'll be redirected to the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/). Add questions to your quiz that will help the customer determine their skincare routine. To add a question, click the `+` button or hover over an existing question and click the `add new question` button. Select a [question type](https://docs.revenuehunt.com/reference/quiz-builder/#question-types) from the dropdown.

## Step 4: Link Products to Choices

Once your quiz is set up, you should add products and collections to the choices in the quiz. This step is necessary to show recommendations.

1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](https://docs.revenuehunt.com/reference/quiz-builder/#link-products) or [Link Collections](https://docs.revenuehunt.com/reference/quiz-builder/#link-collections) tab.
2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

    ![how to recommend slots link products](/images/how to recommend slots link products.png)

## Step 5: Add Product Slots to the Results Page

1. **Edit the Results Page**: Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and edit the content. Add design elements like headings, logos, and content blocks.
2. **Add a Product Slots Block**: Use the `+` button to add a `Product Slots Block` to the Results Page.
3. **Add Slots**: Open the [`Slot Block settings`](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
4. **Edit the Slot**: You can add a title or a description to each slot.
5. **Include Collections into Slots**: Link the corresponding product collection to each slot in the `Include` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection that's included.
![how to recommend slots slot block](/images/how to recommend slots slot block.png)
6. **Choose Product number**: In the [`Slot Block settings`](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

## Step 6: Test and Troubleshoot

Now that the slots are built and product/collections are linked to each choice, you can test the quiz. To test the quiz, you'll have to save the changes and preview it.

1. **Publish the changes**: Click [`Publish`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) on the top-right menu to update the preview/live quiz.
2. **Preview the quiz**: Click [`Preview`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Troubleshoot results**: Use the quiz's [built-in search bar](https://docs.revenuehunt.com/how-to-guides/troubleshoot-product-results/) in the `Metrics > Responses` section to understand why specific products were recommended or missing from the recommendations. 

    !!! tip
        Check [How to Troubleshoot Quiz Results](https://docs.revenuehunt.com/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

---
By adhering to these steps, you can offer a valuable tool to your customers, enhancing their shopping experience through personalized skincare routine recommendations.
