---
icon: material/slot-machine-outline
---

# How to Recommend a Skincare Routine with Slots

With RevenueHunt Product Recommendation Quiz, it is possible to group products into slots and recommend a product for each step in a beauty routine.

This guide is designed to help merchants effectively use [Product Slot Blocks](/reference/quiz-builder/results-page/#block-types) on the results page to organize product recommendations. 

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 74.27785419532324%; height: 0;"><iframe src="https://www.loom.com/embed/f249d672fe414dc390715b210a94a75a?sid=0a795570-01c5-4777-b6b1-62b0a0da3387" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Magento"


    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

A personalized skincare routine recommendation quiz was chosen as an example to best demonstrate how to work with this feature. See an example of such a Skincare Quiz [here](https://skincarequiz.myshopify.com/#quiz-rkHm6Y).

![how to recommend slots example](/images/how_to_recommend_slots_example.png)

## Step 1: Understand Recommendation Mechanism

Make sure that you're familiar with [how the recommendations work](/how-to-guides/recommend-products/) in RevenueHunt app.

??? question "How do I get the right recommendations?"

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products.

    If you want to make the results ultra-precise, you can also:

    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
    - Use [Exclusions](/how-to-guides/recommend-products/#understanding-inclusion-and-exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

It's advised to familiarize yourself with this [voting system](/how-to-guides/recommend-products/#voting-system) before working with Product Slots.

## Step 2: Organize Products into Collections/Categories

=== "Shopify"

    To group products into slots, you’ll need to create new collections in your Shopify store. These collections will be used to group your products on the results page.

    1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
    2. **Create Collections**: For each category, [create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) with the right products. Each collection should only contain products relevant to its category. For example, 
        - a *Cleansers* collection should have all the cleansing products, a *Toners* collection should have all the toning products, 
        - a *Serums* collection should have all the serums, etc. 
        - You can have more than one collection that includes some of the same products.

        ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

    3. **Catalog Sync**: Perform a [catlog sync](/how-to-guides/sync-catalog/) after creating collections to update RevenueHunt Product Recommendation Quiz with the latest product collections.

=== "Shopify V2"

    To group products into slots, you’ll need to create new collections in your Shopify store. These collections will be used to group your products on the results page.

    1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
    2. **Create Collections**: For each category, [create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) with the right products. Each collection should only contain products relevant to its category. For example, 
        - a *Cleansers* collection should have all the cleansing products, a *Toners* collection should have all the toning products, 
        - a *Serums* collection should have all the serums, etc. 
        - You can have more than one collection that includes some of the same products.

        ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

=== "WooCommerce"

    To group products into slots, you’ll need to create new categories in your WooCommerce store. These categories will be used to group your products on the results page.

    1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
    2. **Create Categories**: For each category, [create a category in your WooCommerce store](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) with the right products. Each category should only contain products relevant to its category. For example, 
        - a *Cleansers* category should have all the cleansing products, 
        - a *Toners* category should have all the toning products, 
        - a *Serums* category should have all the serums, etc. 
        - You can have more than one category that includes some of the same products.

    3. **Catalog Sync**: Perform a [catlog sync](/how-to-guides/sync-catalog/) after creating collections to update RevenueHunt Product Recommendation Quiz with the latest product collections.

=== "Magento"

    To group products into slots, you’ll need to create new categories in your Magento store. These categories will be used to group your products on the results page.

    1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
    2. **Create Categories**: For each category, [create a category in your Magento store](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) with the right products. Each category should only contain products relevant to its category. For example, 
        - a *Cleansers* category should have all the cleansing products, 
        - a *Toners* category should have all the toning products, 
        - a *Serums* category should have all the serums, etc. 
        - You can have more than one category that includes some of the same products.

    3. **Catalog Sync**: Perform a [catlog sync](/how-to-guides/sync-catalog/) after creating collections to update RevenueHunt Product Recommendation Quiz with the latest product collections.

=== "BigCommerce"

    To group products into slots, you’ll need to create new categories in your BigCommerce store. These categories will be used to group your products on the results page.

    1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
    2. **Create Categories**: For each category, [create a category in your BigCommerce store](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) with the right products. Each category should only contain products relevant to its category. For example, 
        - a *Cleansers* category should have all the cleansing products, 
        - a *Toners* category should have all the toning products, 
        - a *Serums* category should have all the serums, etc. 
        - You can have more than one category that includes some of the same products.

    3. **Catalog Sync**: Perform a [catlog sync](/how-to-guides/sync-catalog/) after creating collections to update RevenueHunt Product Recommendation Quiz with the latest product collections.

=== "Standalone"

    To group products into slots, you’ll need to create new collections in your Standalone account's [Catalogue](/reference/dashboard/#success-checklist). These collections will be used to group your products on the results page.

    1. **Identify Product Categories**: Determine your skincare product categories (e.g., Cleansers, Toners, Serums, Moisturizers).
    2. **Create Collections**: For each category, create a collection in your Standalone account via the [Catalogue](/reference/dashboard/#success-checklist) tab or a Google Product Feed with the right products. Each collection should only contain products relevant to its category. For example, 
        - a *Cleansers* collection should have all the cleansing products, a *Toners* collection should have all the toning products, 
        - a *Serums* collection should have all the serums, etc. 
        - You can have more than one collection that includes some of the same products.

    3. **Catalog Sync**: Perform a [catlog sync](/how-to-guides/sync-catalog/) after creating collections to update RevenueHunt Product Recommendation Quiz with the latest product collections.

## Step 3: Build the Quiz

1. **Add new quiz**: Go to the app’s [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).
2. **Choose a template**: Choose a pre-defined template or start from scratch. *Tip: There’s are Basic and Advanced Skincare Quiz templates already available.*
3. **Name your quiz**: The name can be edited later.
4.  **Add slides**: After that, you'll be redirected to the [Quiz Builder](/reference/quiz-builder/). Add questions to your quiz that will help the customer determine their skincare routine. To add a question, click the `+ Add question` button. Select a [question type](/reference/quiz-builder/questions/#question-types) from the dropdown/menu.

## Step 4: Link Products to Choices

Once your quiz is set up, you should add products and collections to the choices in the quiz. This step is necessary to show recommendations.

=== "Shopify"

    1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.
    2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

=== "Shopify V2"

    1. **Go to Link Products/Collections tab**: To add link products or product variants to choices, go to [Questions](/reference/quiz-builder/questions/), select a multiple-choice question, then a choice and open the [Choice Settings](/reference/quiz-builder/questions/#choice-settings).

        ![manual_shopifyV2_quizbuilder_quizbuilder_upvotecollections](/images/manual_shopifyV2_quizbuilder_quizbuilder_upvotecollections.png)
    2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

        ![how to recommend slots link products](/images/how_to_recommend_slots_shopify_v2_link_products.png)

=== "WooCommerce"

    1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.
    2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

=== "Magento"

    1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.
    2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

=== "BigCommerce"

    1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.
    2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

=== "Standalone"

    1. **Go to Link Products/Collections tab**: In the Quiz Builder, go to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.
    2. **Link Products**: Link all relevant product variants or collections to each choice. Ensure every choice in your quiz is linked to at least one product or collection to prevent empty results. If a product does not recieve at least one vote, it will never show up on the results page.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

## Step 5: Add Product Slots to the Results Page

=== "Shopify"

    1. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. Add design elements like headings, logos, and content blocks.
    2. **Add a Product Slots Block**: Use the `+` button to add a `Product Slots Block` to the Results Page.
    3. **Add Slots**: Open the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
    4. **Edit the Slot**: You can add a title or a description to each slot.
    5. **Include Collections/Categories into Slots**: Link the corresponding product collection/category to each slot in the `Include` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection/category that's included.
    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)
    6. **Choose Product number**: In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

=== "Shopify V2"

    1. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. Add design elements like headings, logos, and content blocks.
    2. **Add a Product Block**: Use the `+` button to add a `Product Block` to the Results Page.
    3. **Add Slots**: Open the [`Product Block settings`](/reference/quiz-builder/questions/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
    4. **Edit the Slot**: You can add a title or a description to each slot.
    5. **Add Segments**: Add a segment with the corresponding product collection to each slot in the `Add segment` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection that's added in the segment field.

        ![how to recommend slots slot block](/images/how_to_shopifyV2_recommend_routine_with_slots.png)
    6. **Choose Product number**: In the [`Product Block settings`](/reference/quiz-builder/questions/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

=== "WooCommerce"

    1. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. Add design elements like headings, logos, and content blocks.
    2. **Add a Product Slots Block**: Use the `+` button to add a `Product Slots Block` to the Results Page.
    3. **Add Slots**: Open the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
    4. **Edit the Slot**: You can add a title or a description to each slot.
    5. **Include Collections/Categories into Slots**: Link the corresponding product collection/category to each slot in the `Include` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection/category that's included.
    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)
    6. **Choose Product number**: In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

=== "Magento"

    1. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. Add design elements like headings, logos, and content blocks.
    2. **Add a Product Slots Block**: Use the `+` button to add a `Product Slots Block` to the Results Page.
    3. **Add Slots**: Open the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
    4. **Edit the Slot**: You can add a title or a description to each slot.
    5. **Include Collections/Categories into Slots**: Link the corresponding product collection/category to each slot in the `Include` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection/category that's included.
    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)
    6. **Choose Product number**: In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

=== "BigCommerce"

    1. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. Add design elements like headings, logos, and content blocks.
    2. **Add a Product Slots Block**: Use the `+` button to add a `Product Slots Block` to the Results Page.
    3. **Add Slots**: Open the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
    4. **Edit the Slot**: You can add a title or a description to each slot.
    5. **Include Collections/Categories into Slots**: Link the corresponding product collection/category to each slot in the `Include` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection/category that's included.
    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)
    6. **Choose Product number**: In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

=== "Standalone"

    1. **Edit the Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) tab and edit the content. Add design elements like headings, logos, and content blocks.
    2. **Add a Product Slots Block**: Use the `+` button to add a `Product Slots Block` to the Results Page.
    3. **Add Slots**: Open the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) and add a slot for each step in the skincare routine. For example, if your routine consists of 4 products, you should add 4 slots to your Slots Block.
    4. **Edit the Slot**: You can add a title or a description to each slot.
    5. **Include Collections/Categories into Slots**: Link the corresponding product collection/category to each slot in the `Include` section. It's vital for displaying recommendations. Slot can only show most-voted products from a collection/category that's included.
    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)
    6. **Choose Product number**: In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings) you can choose how many products should be recommended per each step. *Tip: Our most succseful quizzes recommend a single product per slot.*

## Step 6: Test and Troubleshoot

Now that the slots are built and product/collections are linked to each choice, you can test the quiz. To test the quiz, you'll have to save the changes and preview it.

1. **Publish the changes**: Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
2. **Preview the quiz**: Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Troubleshoot results**: Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in the `Metrics > Responses` section to understand why specific products were recommended or missing from the recommendations. 

    !!! tip
        Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

---
This article explains how to set up a quiz that recommends products organized into different categories on the results page, for example, a skincare routine based on the customer's answers.
