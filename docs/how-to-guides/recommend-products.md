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

## Voting System

Our product recommendation algorithm works like a voting system:

- Product variants are linked to each choice.
- When a customer picks a choice, all linked products receive one vote.
- After the customer takes the quiz, the results page will show the most voted product variants sorted by the number of votes.
- If no products have been linked or all the products have been excluded, the results page will appear empty.
- If there's a draw in the number of votes, the app will randomize the order of products.

## Understand Inclusion and Exclusion

### Inclusion
Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

=== "Shopify"

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the votes work for each included linked item:

    - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
    - **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
    - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives a vote when their linked choice is selected.
    - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives a vote when their linked choice is selected.
    - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.

=== "Shopify V2"

    ![how to recommend products upvote](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    How the votes work for each upvoted item:

    - **Main Products / All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected.
    - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
    - **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
    - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives a vote when their linked choice is selected.
    - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives a vote when their linked choice is selected.

=== "WooCommerce"

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the votes work for each included linked item:

    - **Simple Products** - Individual products receive a vote when their linked choice is selected.
    - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
    - **Product Bundles**: A bundle is treated as an individual product. Every bundle recieves one vote when their linked choice is selected.
    - **Affiliate Products** - Individual products receive a vote when their linked choice is selected. On the results page the customer is redirected to the affiliate link (not the store link).
    - **Categories**: Every product within a linked category receives a vote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
    - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.

=== "Magento"

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the votes work for each included linked item:

    - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
    - **Categories**: Every product within a linked category receives a vote when their linked choice is selected.

=== "BigCommerce"

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the votes work for each included linked item:

    - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
    - **Categories**: Every product within a linked category receives a vote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.

    !!! tip

        You can also use custom fields as tags within the app by following [these instructions](//how-to-guides/use-custom-fields-as-tags/)

=== "Standalone"

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the votes work for each included linked item:

    - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
    - **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.

!!! warning

    If a product variant is linked to choice "A" (via the Link Products / Upvote tab) and a collection of products that contain this product variant is also linked to choice "A" (via the Link Collections / Upvote tab), then this product variant will receive **2 votes from the same choice**.`

### Exclusion

Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients. 

=== "Shopify"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

=== "Shopify V2"

    ![how to recommend products exclusion](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

=== "WooCommerce"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

=== "Magento"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

=== "BigCommerce"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

=== "Standalone"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

!!! warning

    Once a product is excluded in a choice it will **never show** as a recommendation, even if it's upvoted in another choice earlier/later in the quiz.

!!! example

    If you want the recommended products to be filtered out by question, you can do that using the `exclude` feature. For example, if you want to show only recommendations within a certain price range, you can use the exclude collections feature as in the example below.
    ![how to recommend products exclusion example](/images/how_to_recommend_products_exclusion_example.png)
    This way if a customer chooses that he doesn't want to spend more than 100$, all the products over that price will be excluded from the recommendations.

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

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    **→ OPTION 1: Based on Customer Responses**

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. 

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products/Variants/Collections can be displayed on the Results Page as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.

        **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last.

        ![how to recommend products shopify v2 recommend products based on responses](/images/how_to_recommend_products_shopify_v2_recommend_products_based_on_responses.png)
        
        In [Product Block > Slot settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.

        ![how to recommend products shopify v2 recommend products based on responses max products](/images/how_to_recommend_products_shopify_v2_recommend_products_based_on_responses_max_products.png)

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        Product Block also allows you to display the products in clear steps, for example as a **skincare routine**. Each Product Block that has an added **Segement Filter** can recommend the most-voted product from a collection that's linked to it. *Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.* 

        ![how to recommend products shopify v2 recommend products based on responses segements](/images/how_to_recommend_products_shopify_v2_recommend_products_based_on_responses_segements.png)

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

    **→ OPTION 2: Fixed Recommendations**

    If you don't want to display dynamic recommendations based on customer responses, you can set up fixed recommendations on your Results Page. 

    1. **Open the Results Page**: Navigate to the [Results Page tab]().
    2. **Add a Product Block**: Add a [Product Block]() to your Results Page.
    3. **Set Fixed Recommendations**: In the [Product Block Settings] set the Recommendations System to `Fixed Recommendations`.

        ![how to recommend products shopify v2 recommend fixed products](/images/how_to_recommend_products_shopify_v2_recommend_fixed_products.png)
    4. **Select Recommended Products**: In Slot Settings > Fixed recommended items select the products, variants of collections that should be always recommended to the customer on the results page. 

        ![how to recommend products shopify v2 recommend fixed products slot settings](/images/how_to_recommend_products_shopify_v2_recommend_fixed_products_slot_settings.png)
    5. **Save the changes**: Remember to save the changes to update the preview/live quiz.

    By setting up fixed recommendations, you ensure that the customer will always be shown the same products, no matter what choices they pick throughout the quiz.

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

Check the quiz to learn how to build the quiz outcome you want or consult the *How-to* guides listed below.

<script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/X2Hy6G" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>

### Recommend a Skincare Routine with Slots

With RevenueHunt Product Recommendation Quiz, it is possible to group products into slots and recommend a product for each step in a beauty routine.

![how to recommend slots example](/images/how_to_recommend_slots_example.png)

[This guide](/how-to-guides/recommend-skincare-routine-slots/) is designed to help merchants effectively use [Product Slot Blocks](/reference/quiz-builder/results-page/#block-types) on the results page to organize product recommendations.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-skincare-routine-slots/)

### [How to Only Recommend Products with X Votes or More](/how-to-guides/only-recommend-products-with-minimum-votes/)

It is possible to limit the number of recommended products on the results page by only showing products that received X votes or more (a certain minimum number of votes). This allows you to filter the quiz recommendations and only show the real winners.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/only-recommend-products-with-minimum-votes/)

### Recommend products that match multiple criteria (matrix)

[This article](/how-to-guides/recommend-product-matrix/) outlines a method for recommending skincare products based on multiple criteria using a product matrix to categorize recommendations. 

| Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Teens and 20's  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
| 30's and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary "Buffet" + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

It describes a step-by-step process involving creating product collections, building and linking quizzes to these collections, and utilizing a voting system algorithm to prioritize product suggestions, catering to complex customer profiles and ensuring personalized recommendations.

[:fontawesome-solid-arrow-right: learn more](/how-to-guides/recommend-product-matrix/)

### Recommend Subscription Products

Recommending subscription products via the RevenueHunt Product Recommendation Quiz can significantly enhance your e-commerce strategy by providing a steady revenue stream and fostering long-term customer relationships. With the integration of [ReCharge Subscriptions](https://apps.shopify.com/subscription-payments?surface_intra_position=1&surface_type=partners&surface_version=redesign) or WooCommerce Subscriptions into your product recommendation strategy, you can create a seamless shopping experience for your customers. 

![how to recommend subscription products sample product](/images/how_to_recommend_subscription_products_sample_product.png)

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