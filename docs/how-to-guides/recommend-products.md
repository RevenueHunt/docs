---
icon: material/cards
---

# How to Recommend Products

Our solution takes into account your customer's choices to offer highly personalized product recommendations. 

This guide explains how to recommend products with the RevenueHunt app, the underlying algorithm and proposes solutions for complex quizzes.

## Recommendations

=== "Shopify" 

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants**, **main products** and **[Recharge subscription products](/how-to-guides/recommend-subscription-products/)**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend collections** of products, though it's possible to [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

=== "Shopify V2" 

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants**, **main products** and **collections**.

    If you add a Block to your results page, you can choose to display **product variants**, **main products** or **collections** under [Block Settings > Recommendations Type](/reference/quiz-builder/results-page/#products-products-variants-collections). 

    - If you chose a **Products** under Recommendations Type, the Slot will show the main product with a optional dropdown to choose the specific variant. The order in which the product variants are displayed is based on the number of votes they received. If all varaints of the same product received the same number of votes, the variants will be displayed in random order.

    - If you chose a **Product Varaints** under Recommendations Type, the Slot will show recommended variants of a product with the full name of a product followed by the varaint name, for example "Toner - 100ml". 
    
        !!! note
        
            It is not possible to display the variants in a dropdown with this option, because it's meant to lead the user to the specific variant of a product. If you want to display the variants in a dropdown, you can use a **Products** option instead.

    - If you chose a **Collections** under Recommendations Type, the Slot will show the recommended a specific collection from your Shopify store. 

        !!! note

            If your recommended collections doesn't show any image, it's likely becuase you have not yet added an image to the collection in your Shopify > Products > Collections section. Once you add an image, the collection will show the image on the results page.


=== "WooCommerce" 

    RevenueHunt Product Recommendation Quiz can show on the results page **simple products**, **variable products**, **grouped products**, **external/affiliate products** and **[WooCommerce subscription products](/how-to-guides/recommend-subscription-products/)**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend categories** of products, though it's possible to [only recommend products from a specific category/tag/attribute](/how-to-guides/recommend-skincare-routine-slots/).

    !!! warning
    
        Product Recommendation Quiz for WooCommerce can sync only one type of variants of variable products. For example, if a variable product has two types of variants, the first one being size, the second being color, the app will be able to only sync the size variant of your products.

=== "Magento" 

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants** and **main products**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend categories** of products, though it's possible to [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

=== "BigCommerce" 

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants** and **main products**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend categories** of products, though it's possible to [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

=== "Standalone" 

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants** and **main products**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend collections** of products, though it's possible to [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).


## Recommending the Right Products

=== "Shopify"

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. 

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products can be displayed on the Results Page as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.
        - **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.* 
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz. 
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. 
        
            !!! note
            
                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section to understand why specific products were recommended or missing from the recommendations. 

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.
            
    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

=== "Shopify V2" 

    In Shopify V2, there are several ways to recommend products:

    **✅ Option 1: Recommend Most Voted Products**

    *Best for most quizzes.*

    ![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width="300"}

    - Link products or collections to each quiz choice.
    - On the results page, add a product block that displays the most voted items.
    - You can show multiple product slots to recommend a routine or bundle.

    Follow [this guide](/how-to-guides/set-up-funnel-quiz/) to learn how to set up this option.

    **🧠 Option 2: Use Scoring or Variables**

    *Best for personality-style quizzes.*

    ![how_to_shopify_v2_recommendations_displaylogic](/images/how_to_shopify_v2_recommendations_displaylogic.png){width="300"}

    - Assign a score or custom variable to each choice in the quiz.
    - Set up result sections with fixed recommendations for each type of outcome.
    - Use display logic to show the right section based on the score or variable with the highest value.
    - **Example:** Show Section A if the top variable is "blue", Section B if it’s "red".

    Follow [this guide](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz) to learn how to set up this option.

    **🧩 Option 3: Use Complex Display Logic**

    *Best for advanced logic or detailed recommendation matrices.*

    ![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_varaiblequiz.png){width="300"}

    - Create logic-based paths that lead users to different result pages.
    - Or use one results page with multiple sections and display logic for each.
    - Show/hide each section depending on the customer’s answers.

    Follow [this guide](/how-to-guides/set-up-fixed-recommendations-quiz/#one-results-page) to learn how to set up this option.

=== "WooCommerce"

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. 

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products can be displayed on the Results Page as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.
        - **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.* 
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz. 
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. 
        
            !!! note
            
                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section to understand why specific products were recommended or missing from the recommendations. 

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.
            
    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

=== "Magento"

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. 

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products can be displayed on the Results Page as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.
        - **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.* 
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz. 
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. 
        
            !!! note
            
                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section to understand why specific products were recommended or missing from the recommendations. 

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.
            
    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

=== "BigCommerce"

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. 

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products can be displayed on the Results Page as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.
        - **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.* 
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz. 
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. 
        
            !!! note
            
                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section to understand why specific products were recommended or missing from the recommendations. 

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.
            
    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

=== "Standalone"

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. 

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products can be displayed on the Results Page as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.
        - **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.* 
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz. 
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. 
        
            !!! note
            
                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section to understand why specific products were recommended or missing from the recommendations. 

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.
            
    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

## How to Build Your Quiz Setup

=== "Shopify"

    Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

    <script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

=== "Shopify V2"

    ![how_to_recommend_products_decision_tree_V2](/images/how_to_recommend_products_decision_tree_V2.png)

    | Recommendation System | Best For | Key Features | Complexity |
    |------------------------|----------|--------------|------------|
    | [🧩 Fixed Recommendations](/how-to-guides/set-up-fixed-recommendations-quiz/) | Showing the same product(s) to everyone regardless of answers | - Simple setup<br>- Products always shown<br>- No logic or conditions | Very Low |
    | [✍🏻 Voting System (Funnel Quiz)](/how-to-guides/set-up-funnel-quiz/) | Most quizzes, especially product finders or large catalogs | - Automatically adapts to answers<br>- Simple linking of products to choices<br>- Randomized tie-breaking | Low to Medium |
    | [✍🏻 Voting System (Funnel Quiz with Slots)](/how-to-guides/recommend-skincare-routine-slots/) | Product recommendation routines, different product categories (e.g. cleanser + moisturizer) | - Slot-based grouping<br>- Step-by-step product recommendations<br>- Still uses dynamic voting | Medium |
    | [🎯 Custom Scoring System (Most Voted Variable)](/how-to-guides/set-up-scoring-quiz/) | Personality quizzes, Dosha tests, where outcome depends on which variable (A, B, C...) got the most choices | - Tracks most frequent variable<br>- Outputs results by majority<br>- Often used for typology quizzes | Medium |
    | [🎯 Custom Scoring System (Score + Variable)](/how-to-guides/set-up-scoring-quiz/) | Quizzes that need to calculate values or mix scoring with conditions | - Weighted scoring<br>- Adds hidden variables<br>- Logic can combine score + other rules | Medium to High |
    | [🧩 Fixed Recommendations with Display Logic](https://docs.revenuehunt.com/how-to-guides/set-up-fixed-recommendations-quiz/) | Quizzes with a lot of logic conditions, precise rules, or exceptions | - Shows products based on answers<br>- Supports multiple result pages<br>- Allows display rules and custom text | High |



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


## Specific Use Cases

### [Recommend Most Voted Products](/how-to-guides/set-up-funnel-quiz/)

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width="300"}

[This guide](/how-to-guides/set-up-funnel-quiz/) is designed to help merchants effectively use [Product Slot Blocks](/reference/quiz-builder/results-page/#block-types) on the results page to organize product recommendations.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/set-up-funnel-quiz/)    

### [Recommend a Skincare Routine with Most Voted Products](/how-to-guides/recommend-skincare-routine-slots/)

With RevenueHunt Product Recommendation Quiz, it is possible to group products into slots and recommend a product for each step in a beauty routine.

![how to recommend slots example](/images/how_to_recommend_slots_example.png){width="300"}

[This guide](/how-to-guides/recommend-skincare-routine-slots/) is designed to help merchants effectively use [Product Slot Blocks](/reference/quiz-builder/results-page/#block-types) on the results page to organize product recommendations.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-skincare-routine-slots/)

### [Recommend Fixed Products Based on a Custom Variable - Personality Type Quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz)

Recommended for personality-type, dosha and quizzes that want to show different text results based on choices. Assign varaibles and scores to choices and use the total scores to determine which products to recommend.

![how_to_shopify_v2_recommendations_winningvariable](/images/how_to_shopifyv2_scoringquiz_varaiblequiz.png){width="300"}

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz)

### [Recommend Fixed Products Based on a Custom Score](/how-to-guides/set-up-scoring-quiz/#one-results-page)

Recommended for personality-type quizzes and quizzes that want to show different text results based on choices. Assign point values to choices and use the total scores to determine which products to recommend.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png){width="300"}

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/set-up-scoring-quiz/#one-results-page)

### [Recommend Products Based on Numerical Inputs](/how-to-guides/recommend-products-based-on-numerical-inputs/)

With RevenueHunt Product Recommendation Quiz, it is not possible to recommend products based on open-ended numerical questions like Number or Date. Instead, it's recommended to set up finite choices to be able to use the user responses to set up precise recommendations.

[This guide](/how-to-guides/recommend-products-based-on-numerical-inputs/) is designed to help merchants effectively use dropdown and multiple-choice questions to set up precise numerical recommendations.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-products-based-on-numerical-inputs/)

### Recommend products that match multiple criteria (matrix)

[This article](/how-to-guides/recommend-product-matrix/) outlines a method for recommending skincare products based on multiple criteria using a product matrix to categorize recommendations. 

| Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Teens and 20's  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
| 30's and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary "Buffet" + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

It describes a step-by-step process involving creating product collections, building and linking quizzes to these collections, and utilizing a voting system algorithm to prioritize product suggestions, catering to complex customer profiles and ensuring personalized recommendations.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-product-matrix/)

### Recommend Product Based on a Complex Product Matrix

Recommended for quizzes with complex branching. Set up fixed sections with pre-determined products to be shown on the results page. Then add logic to control visibility of each section or results page.

![docs/images/how_to_shopify_v2_recommendations_displaylogic.png](/images/how_to_shopify_v2_recommendations_displaylogic.png){width="300"}

Set up multiple sections on the results page with fixed product and text combinations, then control visibility of each section with Display Logic display rules.

or

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png){width="300"}

Set up multiple results pages with unique fixed product recommendations and texts and control visbility by adding branching with Jump Logic that leads to diferent results pages.	

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/set-up-fixed-recommendations-quiz/)


### [Only Recommend Products with X Votes or More](/how-to-guides/only-recommend-products-with-minimum-votes/)

It is possible to limit the number of recommended products on the results page by only showing products that received X votes or more (a certain minimum number of votes). This allows you to filter the quiz recommendations and only show the real winners.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/only-recommend-products-with-minimum-votes/)


### Recommend Subscription Products

Recommending subscription products via the RevenueHunt Product Recommendation Quiz can significantly enhance your e-commerce strategy by providing a steady revenue stream and fostering long-term customer relationships. With the integration of [ReCharge Subscriptions](https://apps.shopify.com/subscription-payments?surface_intra_position=1&surface_type=partners&surface_version=redesign) or WooCommerce Subscriptions into your product recommendation strategy, you can create a seamless shopping experience for your customers. 

![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png){width="150"}

[This guide](/how-to-guides/recommend-subscription-products/) explains how to integrate and recommend subscription products with RevenueHunt Product Recommendation Quiz.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-subscription-products/)

### Ensure a Specific Product Always Appears on Your Results Page

[This guide](/how-to-guides/always-recommend-the-same-product/) provides a clear, step-by-step process to making sure that specific products are always visible on the Results Page of your quiz, regardless of the customer's choices.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/always-recommend-the-same-product/)

### Show Results Explanation

While our product recommendation algorithm works to recommend specific products, it will not automatically display an explanation of **why** a certain product was recommended. It also won't automatically display custom text depending on the recommended product.

For this reason, it can be very hard to build a "personality-type" quiz with our solution. [This article](/how-to-guides/show-results-explanation/) proposes some solutions for this problem.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/show-results-explanation/)

### Recommend Products Based on the Number of User Choices

This guide provides information on how to set up a custom solution that will recommend products based on the number of user choices.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-products-based-on-number-of-user-choices/)