---
icon: material/cards
---

# How to Set Up Recommendations

There are three ways to set up product recommendations within the RevenueHunt app:

## 1. Voting System Algorithm (Recommended for most quizzes)

**How it works:**
The voting system counts product "votes" based on customer quiz choices and recommends products with the highest votes.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png)

**Key features:**
- Link products to quiz choices
- Products accumulate votes as customers select associated choices
- Results page shows products with the most votes
- Can limit recommendations to a specific number of products or a minimum vote threshold
- Supports arranging recommendations into Slots to recommend complete product routines

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





### How to set up a Voting System Quiz

=== "Shopify"

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products. 
        - You can link./upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.

        ??? question "How does product inclusion work in the voting system?"
    
          Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.
    
          ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)
      
          How the votes work for each included linked item:
      
          - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
          - **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.
          - **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
          - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives a vote when their linked choice is selected.
          - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives a vote when their linked choice is selected.
          - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.

        ??? question "How does product exclusion work in the voting system?"
            
            Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients. 
            
                ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)
            
            !!! warning
            
                Once a product is excluded in a choice it will **never show** as a recommendation, even if it's upvoted in another choice earlier/later in the quiz.
            
            !!! example
            
                If you want the recommended products to be filtered out by question, you can do that using the `exclude` feature. For example, if you want to show only recommendations within a certain price range, you can use the exclude collections feature as in the example below.
                ![how to recommend products exclusion example](/images/how_to_recommend_products_exclusion_example.png)
                This way if a customer chooses that he doesn't want to spend more than 100$, all the products over that price will be excluded from the recommendations.



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
    4. **Select Recommended Products**: In Slot Settings > Fixed recommended itents select the products, variants of collections that should be always recommended to the customer on the resutls page. 

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

**Benefits:**
- Most versatile solution that adapts to changes in your product catalog
- Always recommends top products based on customer choices
- Works as a funnel to effectively narrow down product selection

**Best practices:**
- Think carefully about which products are upvoted in each choice
- Create special hidden collections for each choice and add relevant products
- Link collections to choices rather than individual products for easier management

**Variants:**
1. **With Jump Logic:** Branch your quiz to show different follow-up questions based on customer choices. The algorithm counts votes only from questions and answers shown to each customer.

2. **With Skip Logic:** Show different follow-up questions based on customer choices in a multiple-choice, multiple selection question. For example, ask about skin concerns and then only show follow-up questions related to the selected concerns.

3. **With Block Logic:** Show or hide different text blocks on the results page. This approach requires predicting every possible answering route and adding block logic rules for each text block. Not recommended for personality-type quizzes due to complexity.

## 2. Fixed Recommendations (Recommended for quizzes with complex branching)

**How it works:**
Set up fixed sections with pre-determined products to be shown on the results page.

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png)

### How to set up Fixed Recommendations

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
    4. **Select Recommended Products**: In Slot Settings > Fixed recommended itents select the products, variants of collections that should be always recommended to the customer on the resutls page. 

        ![how to recommend products shopify v2 recommend fixed products slot settings](/images/how_to_recommend_products_shopify_v2_recommend_fixed_products_slot_settings.png)
    5. **Save the changes**: Remember to save the changes to update the preview/live quiz.

    By setting up fixed recommendations, you ensure that the customer will always be shown the same products, no matter what choices they pick throughout the quiz.

**Key features:**
- No need to link products to choices
- Set up multiple sections on the results page with fixed product and text combinations
- Control visibility with Block Logic display rules
- Can be combined with Jump Logic for complex branching

**Benefits:**
- All text blocks and logic are in one place with a single results page
- Easier to maintain than complex voting systems
- Good for quizzes that show different text based on customer choices

**Variants:**
1. **Single Results Page:** Set up one results page with multiple sections controlled by Block Logic.

2. **Multiple Results Pages:** Split your quiz into branches using Jump Logic. Each branch leads to a specific results page with unique product recommendations (fixed or voting-based). Instead of one results page with multiple sections, you have multiple results pages with one section each.

**Best for:**
- Complex quizzes with extensive branching
- Quizzes requiring very specific product recommendations
- When you need precise results (though requires more setup and maintenance)

## 3. Custom Scoring System (Recommended for personality-type quizzes)

**How it works:**
Assign point values to choices and use the total scores to determine which products to recommend.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png)

**Key features:**
- Assign numerical scores to each choice in your quiz
- Create score ranges that correspond to different recommendation categories
- Use display logic based on accumulated scores to show appropriate content

**Setup process:**
1. Go to each question in your quiz
2. For each choice, open the choice settings
3. Assign appropriate point values to each choice

**Implementing score-based display logic:**
1. On the Results Page, select a content block
2. In the right-hand menu, locate Display Logic
3. Click on + Add condition (OR)
4. Use "The variable with the highest score..." or "The score of the variable..." option
5. Set up range conditions to control content visibility

**Example:**
For skin type recommendations:
- Assign points to choices (Dry: 1, Normal: 2, Oily: 3, Combination: 4, Sensitive: 5)
- Set display logic for content blocks based on total scores:
  - Dry skin content: Score between 5-7 points
  - Normal skin content: Score between 8-12 points
  - Oily skin content: Score between 13-17 points
  - Combination skin content: Score between 18-22 points
  - Sensitive skin content: Score between 23-25 points

**Best for:**
- Personality quizzes with variable outcomes
- When you need to weigh different factors with varying importance
- Creating nuanced recommendation categories

