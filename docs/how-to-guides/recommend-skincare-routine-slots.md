# How to Recommend a Skincare Routine with Slots

This guide is designed to help merchants effectively use Product Slot Blocks on the results page to organize product recommendations. A personalized skincare routine recommendation quiz was chosen as an example to best demonstrate how to work with this feature. With Shop Quiz, it is possible to group products into slots and recommend a product for each step in a beauty routine.

See an example of such a Skincare Quiz [here](https://skincarequiz.myshopify.com/#quiz-rkHm6Y).

## Step 1: Understand the Recommendation Mechanism

Understand that the product recommendation operates like a [voting system](https://docs.revenuehunt.com/how-to-guides/how-to-recommend-products/#voting-system). Choices in the quiz are linked to products, gaining votes based on customer selections. The most-voted products are recommended first on the results page, the least-voted products are shown last. It's advised to familiarize yourself with this [voting system](https://docs.revenuehunt.com/how-to-guides/how-to-recommend-products/#voting-system) before working with Product Slots.

## Step 2: Organize Products into Collections

To group products into slots, you’ll need to create new collections in your Shopify store.

1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
2. **Create Collections**: For each category, [create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) with the right products. Each collection should only contain products relevant to its category. For example, a *Cleansers* collection should have all the cleansing products, a *Toners* collection should have all the toning products, a *Serums* collection should have all the serums, etc. You can have more than one collection that includes some of the same products.
3. **Catalog Sync**: Perform a [catlog sync](https://docs.revenuehunt.com/how-to-guides/how-to-sync-catalog/) after creating collections to update your quiz tool with the latest product categorizations.

## Step 3: Build the Quiz

1. **Add new quiz**: Go to the app’s [dashboard](https://docs.revenuehunt.com/reference/dashboard/) and click [`add new quiz`](https://docs.revenuehunt.com/reference/dashboard/#new-quiz).
2. **Choose a template**: Choose a pre-defined template or start from scratch. *Tip: There’s a Basic Skincare Quiz template that’s ready to use.*
3. **Name your quiz**: The name can be edited later.
4. **Redirect to Quiz Builder**: After that, you'll be redirected to the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
5. **Add slides**: To add a question, click the `+` button or hover over an existing question and click the `add new question` button. Select a [question type](https://docs.revenuehunt.com/reference/quiz-builder/#question-types) from the dropdown.

## Step 4: Link Products to Choices

Once your quiz is set up, you should add products and collections to the choices in the quiz. This step is necessary to show recommendations.

1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](https://docs.revenuehunt.com/reference/quiz-builder/#link-products) or [Link Collections](https://docs.revenuehunt.com/reference/quiz-builder/#link-collections) tab.
2. **Link Products**: Link product variants or collections to each choice. This determines the product recommendations based on customer responses. In the end, the Results Page will display the products sorted by the number of votes.
3. **Verification**: Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If no collections are included, the slot will be empty!

## Step 5: Edit the Results Page

1. **Edit the Results Page**: Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and edit the content. 
2. **Page Design**: Add design elements like headings, logos, and content blocks.
3. **Add a Product Slots Block**: Use `+` to add a `Product `Slots Block` to the Results Page.
4. **Configure Slots**: Open the `Slot Block settings` and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
5. **Include Collections into Slots**: Link the corresponding product category collection to each slot in the `Include` section. It's vital for displaying recommendations.
6. **Choose Product number**: In the `Slot Block settings` you can choose how many products should be recommended per each step and add a title to each slot. *Tip: Our most succseful quizzes recommend a single product per slot.*

## Step 6: Test and Troubleshoot

Now that the slots are built and product/collections are linked to each choice, you can test the quiz. To test the quiz, you'll have to save the changes and preview it.

1. **Publish the changes**: Click [`Publish`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) on the top-right menu. Don't worry, clicking `Publish` will not automatically add the quiz to your website. It will simply save the changes and allow you to preview the quiz.
2. **Preview the quiz**: Click [`Preview`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Troubleshoot results**: Use the quiz's [built-in search bar]() in the `Metrics > Responses` section to understand why specific products were recommended or missing from the recommendations. Check [How to Check Why a Product was Recommended or Not]() for detailed instructions on how to use this tool.

By adhering to these steps, you can offer a valuable tool to your customers, enhancing their shopping experience through personalized skincare routine recommendations.
