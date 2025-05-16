# How to Set Up Funnel Quiz

## Funnel Quiz 


<div style="position: relative; padding-bottom: 74.27785419532324%; height: 0;"><iframe src="https://www.loom.com/embed/f249d672fe414dc390715b210a94a75a?sid=0a795570-01c5-4777-b6b1-62b0a0da3387" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

The voting system counts product "votes" based on customer quiz choices and recommends products with the highest votes.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png) 

Product recommendation algorithm works like a voting system:

- Product variants are linked to each choice.
- When a customer picks a choice, all linked products receive one vote.
- After the customer takes the quiz, the results page will show the most voted product variants sorted by the number of votes.
- If no products have been linked or all the products have been excluded, the results page will appear empty.
- If there's a draw in the number of votes, the app will randomize the order of products.
- You can limit recommendations to a specific number of products or a minimum vote threshold
- Supports arranging recommendations into Slots to recommend complete product routines


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



## Funnel Quiz that Skips Slides

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/706166edd208443f8982525d62455f46?sid=555e7d4e-fbb9-4650-bb79-1b9e3887f85b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Show different follow-up questions based on customer choices in a multiple-choice, multiple selection question. For example, ask about skin concerns and then only show follow-up questions related to the selected concerns. The algorithm counts votes only from questions and answers shown to each customer. 

![how_to_shopify_v2_recommendations_skiplogic.png](/images/how_to_shopify_v2_recommendations_skiplogic.png)

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



