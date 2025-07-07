# How to Set Up Funnel Quiz

A Funnel Quiz helps your customers find the best product by assigning "votes" to products as they answer questions. The quiz counts these votes and recommends the most relevant products at the end.

!!! info "Use this method for:"

    - Helping customers narrow down a large product catalog
    - Most quizzes, especially product finders
    - Your first product recommendation quiz
    - Quizzes without complex branching


## ✍🏻 Voting System

Our product recommendation algorithm works like a voting system:

- Product variants are linked to each choice.
- When a customer picks a choice, all linked products receive one vote.
- After the customer takes the quiz, the results page will show the most voted product variants sorted by the number of votes.
- If no products have been linked or all the products have been excluded, the results page will appear empty.
- If there's a draw in the number of votes, the app will randomize the order of products.

**Understand Inclusion and Exclusion**

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

    !!! tip
    
        You can also recommend pure text results by setting up different sections on the results page and controlling visibility of each section with Display Logic. This option is not dependent on the voting system but rather on custom scoring system or conditional logic.



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

## Funnel Quiz

The voting system recommends products by counting how many times each one is "voted for" through customer quiz choices. Each quiz choice can be linked to specific product variants, and every time a customer selects a choice, the associated products receive one vote. 

At the end of the quiz, the results page displays the product variants with the most votes, sorted from highest to lowest. If no products have been linked or all products are excluded by logic, the results page will be empty. In the case of a tie, the app will randomize the product order. You can also configure the system to show only a limited number of top-voted products or set a minimum number of votes for a product to appear.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width=500} 

=== "Shopify"

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants**, **main products** and **[Recharge subscription products](/how-to-guides/recommend-subscription-products/)**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend collections** of products, though it's possible to [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

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

    <div style="position: relative; padding-bottom: 74.27785419532324%; height: 0;"><iframe src="https://www.loom.com/embed/f249d672fe414dc390715b210a94a75a?sid=0a795570-01c5-4777-b6b1-62b0a0da3387" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants**, **main products** and **collections**.

    Follow these steps to set up product recommendations in your Product Recommendation Quiz:

    1. **Link Products to Choices**: Navigate to the [Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, upvote relevant products. 
    
        Products or collections added in the `upvotes` field of the [Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.
      
        ![how to recommend products inclusion](/images/how_to_shopifyv2_setuprecommendations_linkcollections.png)

        !!! tip

            Think carefully about which products are upvoted in each choice. You can create special **hidden collections** for each choice in Shopify and add only relevant products to them. Then you can link collections to choices rather than individual products for easier management.

        ??? question "How the votes work for each included linked item?"

            You can upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.

            - **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
            - **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.
            - **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
            - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives a vote when their linked choice is selected.
            - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives a vote when their linked choice is selected.
            - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.
                
        ??? warning "How does product **exclusion** work in the voting system?"
            
            Use the `exclude` field of the [Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients. 
                
            ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)
                
            !!! warning
                
                Once a product is excluded in a choice it will **never show** as a recommendation, even if it's upvoted in another choice earlier/later in the quiz.
                
            !!! example
                
                If you want the recommended products to be filtered out by question, you can do that using the `exclude` feature. For example, if you want to show only recommendations within a certain price range, you can use the exclude collections feature as in the example below.
                ![how to recommend products exclusion example](/images/how_to_recommend_products_exclusion_example.png)
                This way if a customer chooses that he doesn't want to spend more than 100$, all the products over that price will be excluded from the recommendations.

    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. 
    
        - You can add a heading, content block, image block, HTML block or a Product Block. 

        ![how_to_shopifyv2_setuprecommendations_editresults](/images/how_to_shopifyv2_setuprecommendations_editresults.png)

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: Products or variants or collections can be displayed on the Results Page as a list via the `Products Block`. 
    
        - Click `+ Add Block` and select [`Products Block`](/reference/quiz-builder/results-page/#products-products-variants-collections) to add it to your results page.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes.png)

        - In Product Block settings you can chose the `Recommendation system` to be `Based on customer's responses`. the **Product Block** then displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last.

        ![how to recommend products shopify v2 recommend products based on responses](/images/how_to_recommend_products_shopify_v2_recommend_products_based_on_responses.png){width="35%"}

        - Every Product Block comes with a default `Slot` that allows you to display the recommended products. In [Slot settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.

        ![how to recommend products shopify v2 recommend products based on responses max products](/images/how_to_recommend_products_shopify_v2_recommend_products_based_on_responses_max_products.png){width="300"}

        - Then the results page will show the products like this, sorted by the number of votes:

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        !!! note

            Product Block also allows you to display the products in clear steps, for example as a **skincare routine**. Each Product Block that has an added **Segement Filter** can recommend the most-voted product from a collection that's linked to it. Check [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks.


    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz. 
        - Then, click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. 
        
            !!! note
            
                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section to understand why specific products were recommended or missing from the recommendations. 

        ![how to recommend products shopify v2 troubleshoot results](/images/manual_shopifyV2_quizbuilder_responses_sample1_checkproduct.png)

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.
            
    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

=== "WooCommerce"

    RevenueHunt Product Recommendation Quiz can show on the results page **simple products**, **variable products**, **grouped products**, **external/affiliate products** and **[WooCommerce subscription products](/how-to-guides/recommend-subscription-products/)**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend categories** of products, though it's possible to [only recommend products from a specific category/tag/attribute](/how-to-guides/recommend-skincare-routine-slots/).

    !!! warning
    
        Product Recommendation Quiz for WooCommerce can sync only one type of variants of variable products. For example, if a variable product has two types of variants, the first one being size, the second being color, the app will be able to only sync the size variant of your products.

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

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants** and **main products**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend categories** of products, though it's possible to [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

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

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants** and **main products**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend categories** of products, though it's possible to [only recommend products from a specific category](/how-to-guides/recommend-skincare-routine-slots/).

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

    RevenueHunt Product Recommendation Quiz can show on the results page **product variants** and **main products**. 

    RevenueHunt Product Recommendation Quiz **cannot recommend collections** of products, though it's possible to [only recommend products from a specific collection](/how-to-guides/recommend-skincare-routine-slots/).

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

## Funnel Quiz with Slots

The voting system counts product "votes" based on customer quiz choices and then recommends highest voted products based on a filter added to each slot. For example, you can recommend a full skincare routine with a quiz that takes into account the customer answers and shows the most voted cleanser, toner, serum and moisturizer arranged into specific slots. 

![how_to_shopify_v2_recommendations_funnel_with_slots](/images/how_to_shopify_v2_recommendations_funnel_with_slots.png){width=500}


=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    You can also:
    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/)
    - Use Exclusions to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier)

    **Step 2: Organize Products into Collections**

    To group products into slots, create new collections in your Shopify store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each category
    3. Add relevant products to each collection (e.g., all cleansers in the Cleansers collection)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your collections

    ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

    **Step 3: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 4: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or collections to each choice
    3. Ensure every choice has at least one product or collection linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 5: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product collections to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 6: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "Shopify V2"

    Follow these steps to set up a funnel quiz with product slots in Shopify V2:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    You can also:
    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/)
    - Use Exclusions to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier)

    **Step 2: Organize Products into Collections**

    To group products into slots, create new collections in your Shopify store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each category
    3. Add relevant products to each collection (e.g., all cleansers in the Cleansers collection)

    **Step 3: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 4: Link Products to Choices**

    1. Go to [Questions](/reference/quiz-builder/questions/)
    2. Select a multiple-choice question
    3. Select a choice and open the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    4. Link relevant product variants or collections to each choice
    5. Ensure every choice has at least one product or collection linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_shopify_v2_link_products.png)

    **Step 5: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Block`
    4. In the [`Product Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Add segments with corresponding product collections to each slot
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_shopify_v2_set_up_filters.png){width=50%}

    **Step 6: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in WooCommerce:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    You can also:
    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/)
    - Use Exclusions to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier)

    **Step 2: Organize Products into Categories**

    To group products into slots, create new categories in your WooCommerce store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a category in your WooCommerce store](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) for each type
    3. Add relevant products to each category (e.g., all cleansers in the Cleansers category)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your categories

    **Step 3: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 4: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or categories to each choice
    3. Ensure every choice has at least one product or category linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 5: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product categories to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 6: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in Magento:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    You can also:
    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/)
    - Use Exclusions to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier)

    **Step 2: Organize Products into Categories**

    To group products into slots, create new categories in your Magento store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a category in your Magento store](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) for each type
    3. Add relevant products to each category (e.g., all cleansers in the Cleansers category)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your categories

    **Step 3: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 4: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or categories to each choice
    3. Ensure every choice has at least one product or category linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 5: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product categories to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 6: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in BigCommerce:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    You can also:
    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/)
    - Use Exclusions to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier)

    **Step 2: Organize Products into Categories**

    To group products into slots, create new categories in your BigCommerce store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a category in your BigCommerce store](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) for each type
    3. Add relevant products to each category (e.g., all cleansers in the Cleansers category)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your categories

    **Step 3: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 4: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or categories to each choice
    3. Ensure every choice has at least one product or category linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 5: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product categories to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 6: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in Standalone mode:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    You can also:
    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/)
    - Use Exclusions to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier)

    **Step 2: Organize Products into Collections**

    To group products into slots, create new collections in your Standalone account:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. Create collections in your Standalone account via the [Catalogue](/reference/dashboard/#success-checklist) tab or a Google Product Feed
    3. Add relevant products to each collection (e.g., all cleansers in the Cleansers collection)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your collections

    **Step 3: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 4: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or collections to each choice
    3. Ensure every choice has at least one product or collection linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 5: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product collections to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 6: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

## Funnel Quiz that Skips Slides

Show different follow-up questions based on customer choices in a multiple-choice, multiple selection question. For example, ask about skin concerns and then only show follow-up questions related to the selected concerns. The algorithm counts votes only from questions and answers shown to each customer. 

![how_to_shopify_v2_recommendations_skiplogic.png](/images/how_to_shopify_v2_recommendations_skiplogic.png){width=500}

![how_to_hide_content_with_logic_shopifyv2_skip_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

=== "Shopify"

    RevenueHunt Product Recommendation Quiz can use skip logic to show different follow-up questions based on customer choices. The quiz can skip irrelevant questions based on user selections, improving engagement and relevance.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - For example: If 'Skin Concerns' is not 'Acne', skip the Acne questions
        - Repeat for each follow-up question and corresponding concern

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products/variants
        - The quiz will count votes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.


=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/706166edd208443f8982525d62455f46?sid=555e7d4e-fbb9-4650-bb79-1b9e3887f85b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    RevenueHunt Product Recommendation Quiz can use skip logic to show different follow-up questions based on customer choices. The quiz can skip irrelevant questions based on user selections, improving engagement and relevance.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_mulriplechoice.png)

        - Open the Revenue Hunt quiz app and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' in the [`multiple-choice settings`](/reference/quiz-builder/questions/#multiple-choice-settings) to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_followup.png)

        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_skiplogic.png)

        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - For example: If 'Skin Concerns' is not 'Acne', skip the Acne questions
        - Repeat for each follow-up question and corresponding concern

    4. **Link Products to Choices**: Navigate to the [Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_linkproduct.png)

        - For each choice, upvote relevant products
        - Products or collections added in the `upvotes` field are upvoted in the final recommendations
        - The quiz will count votes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
        - Use the preview feature to test different combinations of selections
        - Select multiple concerns (e.g., 'Acne' and 'Blackheads') to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "WooCommerce"

    RevenueHunt Product Recommendation Quiz can use skip logic to show different follow-up questions based on customer choices. The quiz can skip irrelevant questions based on user selections, improving engagement and relevance.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - For example: If 'Skin Concerns' is not 'Acne', skip the Acne questions
        - Repeat for each follow-up question and corresponding concern

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products (simple products, variable products, or grouped products)
        - The quiz will count votes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "Magento"

    RevenueHunt Product Recommendation Quiz can use skip logic to show different follow-up questions based on customer choices. The quiz can skip irrelevant questions based on user selections, improving engagement and relevance.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - For example: If 'Skin Concerns' is not 'Acne', skip the Acne questions
        - Repeat for each follow-up question and corresponding concern

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products or variants
        - The quiz will count votes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "BigCommerce"

    RevenueHunt Product Recommendation Quiz can use skip logic to show different follow-up questions based on customer choices. The quiz can skip irrelevant questions based on user selections, improving engagement and relevance.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - For example: If 'Skin Concerns' is not 'Acne', skip the Acne questions
        - Repeat for each follow-up question and corresponding concern

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products or variants
        - The quiz will count votes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "Standalone"

    RevenueHunt Product Recommendation Quiz can use skip logic to show different follow-up questions based on customer choices. The quiz can skip irrelevant questions based on user selections, improving engagement and relevance.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - For example: If 'Skin Concerns' is not 'Acne', skip the Acne questions
        - Repeat for each follow-up question and corresponding concern

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products or variants
        - The quiz will count votes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.



## Funnel Quiz with Branching

Branch your quiz to show different follow-up questions based on customer choices. The algorithm counts votes only from questions and answers shown to each customer. You can display recommendations either as a simple list or arrange them into slots for a more structured presentation.

![how_to_shopify_v2_recommendations_jumplogic](/images/how_to_shopify_v2_recommendations_jumplogic.png){width=500}

=== "Shopify"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. Don't worry about the order yet - you'll set that up with Jump Logic

    **Step 3: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"
        - Example: If "What's your skin type?" is "Oily", jump to "Oily Skin Concerns"
    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 4: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count votes from questions shown to the user

    **Step 5: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "Shopify V2"

    Follow these steps to set up a branching funnel quiz in Shopify V2:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Create a new quiz in the [Quiz Builder](/reference/quiz-builder/)
    2. Add all questions needed for each branch
    3. Add all possible choices for each question
    4. The order doesn't matter yet - you'll configure that with Jump Logic

    **Step 3: Set Up Branching**

    ![how_to_hide_content_with_logic_shopifyv2_jump_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)

    1. Go to each question's settings
    2. Add Jump Logic rules in the Conditional Logic section:
        - Set conditions for when to jump
        - Choose destination question
        - Add multiple rules if needed
    3. Make sure each branch ends with:
        - Lead collection question, or
        - Results page

    **Step 4: Link Products**

    1. For each choice in every branch:
        - Open Choice Settings
        - Add products to "Upvote" section
        - Add collections if applicable
    2. The quiz only counts votes from shown questions

    **Step 5: Configure Results Page**

    1. Add a Products Block
    2. Set "Recommendation system" to "Based on customer's responses"
    3. Configure number of products to show
    4. Optionally add segments for structured recommendations

    **Step 6: Test and Launch**

    1. Save changes
    2. Preview and test each branch
    3. Use Response Analysis to verify logic
    4. Publish when ready

=== "WooCommerce"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. Don't worry about the order yet - you'll set that up with Jump Logic

    **Step 3: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"
        - Example: If "What's your skin type?" is "Oily", jump to "Oily Skin Concerns"
    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 4: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count votes from questions shown to the user

    **Step 5: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "Magento"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. Don't worry about the order yet - you'll set that up with Jump Logic

    **Step 3: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"
        - Example: If "What's your skin type?" is "Oily", jump to "Oily Skin Concerns"
    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 4: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count votes from questions shown to the user

    **Step 5: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "BigCommerce"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. Don't worry about the order yet - you'll set that up with Jump Logic

    **Step 3: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"
        - Example: If "What's your skin type?" is "Oily", jump to "Oily Skin Concerns"
    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 4: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count votes from questions shown to the user

    **Step 5: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "Standalone"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. Don't worry about the order yet - you'll set that up with Jump Logic

    **Step 3: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"
        - Example: If "What's your skin type?" is "Oily", jump to "Oily Skin Concerns"
    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 4: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count votes from questions shown to the user

    **Step 5: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic


## Funnel Quiz that Shows Custom Text Based on Choices

Show or hide different text blocks on the results page based on customer choices. This approach requires predicting every possible answering route and adding display logic rules for each text block. 

![how_to_shopify_v2_recommendations_funnel_displaylogic](/images/how_to_shopify_v2_recommendations_funnel_displaylogic.png){width=500}

=== "Shopify"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 3: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, varaints or collections.
    3. The quiz will count votes from all questions

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 5: Set Up Display Logic**

    1. For each content block, add display logic rules:
        - Format: If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.
        - You can combine multiple conditions with AND/OR operators
        - Example: If "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show skincare routine for oily, acne-prone skin
    2. Ensure all possible answer combinations are covered!

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "Shopify V2"

    !!! warning "Not recommended for personality-type quizzes"

        Not recommended for personality-type quizzes due to complexity. For this application, try the [🎯 Custom Scoring System (Most Voted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display Logic](/how-to-guides/set-up-fixed-recommendations-quiz/) solutions.

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify V2:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed. Add all possible choices for each question.

    **Step 3: Link Products to Choices**

    1. For each choice open Choice Settings and add products to "Upvote" section.
    2. The quiz will count votes from all questions

    **Step 4: Configure Results Page**

    1. Add a Products Block with "Based on customer's responses" setting for Recommendations System.
    2. Add multiple Sections to your results page for different answer combinations. To each section add text, images or HTML content blocks for different answer combinations.

    **Step 5: Set Up Display Logic**

    1. For each content block:
        - Add display logic rules in block settings. Format: If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.
        - Combine conditions with AND/OR operators.
        - Example: If "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show this block.
    2. Cover all possible answer combinations!

    **Step 6: Test and Launch**

    1. Save changes
    2. Test thoroughly! Try different answer combinations. Verify correct content appears. Check product recommendations.
    3. Use [Response Analysis](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "WooCommerce"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 3: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, varaints or collections.
    3. The quiz will count votes from all questions

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 5: Set Up Display Logic**

    1. For each content block, add display logic rules:
        - Format: If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.
        - You can combine multiple conditions with AND/OR operators
        - Example: If "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show skincare routine for oily, acne-prone skin
    2. Ensure all possible answer combinations are covered!

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "Magento"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 3: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, varaints or collections.
    3. The quiz will count votes from all questions

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 5: Set Up Display Logic**

    1. For each content block, add display logic rules:
        - Format: If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.
        - You can combine multiple conditions with AND/OR operators
        - Example: If "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show skincare routine for oily, acne-prone skin
    2. Ensure all possible answer combinations are covered!

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "BigCommerce"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 3: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, varaints or collections.
    3. The quiz will count votes from all questions

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 5: Set Up Display Logic**

    1. For each content block, add display logic rules:
        - Format: If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.
        - You can combine multiple conditions with AND/OR operators
        - Example: If "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show skincare routine for oily, acne-prone skin
    2. Ensure all possible answer combinations are covered!

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "Standalone"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Understand Recommendation Mechanism**

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products

    **Step 2: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 3: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, varaints or collections.
    3. The quiz will count votes from all questions

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 5: Set Up Display Logic**

    1. For each content block, add display logic rules:
        - Format: If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.
        - You can combine multiple conditions with AND/OR operators
        - Example: If "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show skincare routine for oily, acne-prone skin
    2. Ensure all possible answer combinations are covered!

    **Step 6: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.


---
This article explains how to set up a quiz that recommends products based on customer choices using a built-in voting system.
