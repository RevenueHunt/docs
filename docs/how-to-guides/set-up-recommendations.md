---
icon: material/cards
---

# How to Set Up Recommendations

There are three ways to set up product recommendations within the RevenueHunt app:

## ✍🏻 Voting System


Recommended for most quizzes. The voting system counts product "votes" based on customer quiz choices and recommends products with the highest votes.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png) 

### How It Works

Product recommendation algorithm works like a voting system:

- Product variants are linked to each choice.
- When a customer picks a choice, all linked products receive one vote.
- After the customer takes the quiz, the results page will show the most voted product variants sorted by the number of votes.
- If no products have been linked or all the products have been excluded, the results page will appear empty.
- If there's a draw in the number of votes, the app will randomize the order of products.
- You can limit recommendations to a specific number of products or a minimum vote threshold
- Supports arranging recommendations into Slots to recommend complete product routines

!!! note "Benefits of the Voting System Algorithm"  

    - Most versatile solution that adapts to changes in your product catalog
    - Always recommends top products based on customer choices
    - Works as a funnel to effectively narrow down product selection


### How to Set Up

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


### Branching Quiz Logic

1. **With Jump Logic:** Branch your quiz to show different follow-up questions based on customer choices. The algorithm counts votes only from questions and answers shown to each customer. Check how to use [Jump Logic](/how-to-guides/hide-content-with-logic/#jump-logic-how-to-show-custom-text-in-the-quiz) to learn how to set it up.

  ![how_to_hide_content_with_logic_shopifyv2_jump_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)
2. **With Skip Logic:** Show different follow-up questions based on customer choices in a multiple-choice, multiple selection question. For example, ask about skin concerns and then only show follow-up questions related to the selected concerns. The algorithm counts votes only from questions and answers shown to each customer. Check how to use [Skip Logic](/how-to-guides/hide-content-with-logic/#skip-logic-how-to-show-custom-text-in-the-quiz) to learn how to set it up.

  ![how_to_hide_content_with_logic_shopifyv2_skip_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)
3. **With Block Logic:** Show or hide different text blocks on the results page. This approach requires predicting every possible answering route and adding block logic rules for each text block. Not recommended for personality-type quizzes due to complexity. For this application, try the [Custom Scoring System](/how-to-guides/custom-scoring-system/) solution.

## 🧩 Fixed Recommendations

Recommended for quizzes with complex branching. Set up fixed sections with pre-determined products to be shown on the results page. Then add logic to control visibility of each section or results page.


### How It Works

**Option 1:** Set up multiple sections on the results page with fixed product and text combinations, then control visibility of each section with Block Logic display rules.

![docs/images/how_to_shopify_v2_recommendations_blocklogic.png](/images/how_to_shopify_v2_recommendations_blocklogic.png)

**Option 2:** Set up multiple results pages with unique fixed product recommendations and texts and control visbility by adding branching with Jump Logic that leads to diferent resutls pages.	

![how_to_shopify_v2_recommendations_logic](/images/how_to_shopify_v2_recommendations_logic.png)

!!! info "Benefits"

    - Good for complex branching quizzes with multiple very precise outcomes and product recommendations.

### How to Set Up Fixed Recommendations with One Results Page 

Set up one results page with multiple sections controlled by Block Logic/Display Logic on the results page. 



=== "Shopify"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Add Content Sections to Results Page**: Go to the [Results Page](/reference/quiz-builder/results-page/) and add a new `sections`. To add a new section click the `+ Add section` sign. 
    
        Add multiple content blocks describing the specific skin type and its challenges. For example:

        ![how to hide content with logic shopifyv2 block logic sections](/images/how_to_hide_content_with_logic_shopifyv2_block_logic_sections.png)

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    3. **Add Display Logic**: If we don't add [Display Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. 
    
        To add Display Logic, select a content block and in the right-hand menu locate `Display logic`. Click on `+ Add consition (OR)`. 
              
        Set up IF-THEN statements to control when each statement block should be visible or hidden based on the customer's choices. Like this:

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_shopifyv2_block_logic_rule.png)

    5. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Add Content Blocks to Results Page**: Go to the Results Page and add a new `content block`. To add a content block click the `+` sign and select `Content Block` from the list. Add multiple content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that’s deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn’t experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin’s natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.
            

        !!! tip    
        
            Make the heading stand out with [markdown language](/how-to-guides/use-markdown/). Use the`#` sign before a sentence can make it bold.

    3. **Add Block Logic**: If we don’t add [Block Logic](/how-to-guides/use-block-logic/) to the quiz, our blocks will just appear one after the other on the Results Page, regardless of the choice we made. To add Block Logic, select a content block and click on `block logic`. Next, click `add block logic`. Set up IF-THEN statements to control when each content block should be visible or hidden based on the customer's choices.

        ![how to hide content with logic block logic statement](/images/how_to_hide_content_with_logic_block_logic_statement.png)

    4. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

### How to Set Up Fixed Recommendations with Multiple Results Pages

Set up multiple results pages with unique fixed product recommendations and texts, then control which results page is shown using Jump Logic in the Conditional Logic tab.

=== "Shopify"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Shopify V2"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the [images or text blocks](/reference/quiz-builder/questions/#block-settings) to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+ Add Results Page` button to create additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages shopify v2](/images/how_to_set_up_multiple_results_pages_shopify_v2.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Products Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages shopify v2](/images/how_to_add_product_blocks_to_results_pages_shopify_v2.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages shopify v2](/images/how_to_set_up_jump_logic_for_results_pages_shopify_v2.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Save` button to update the preview/live quiz.

=== "WooCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Magento"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "BigCommerce"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.

=== "Standalone"

    1. **Create Quiz**: Open the [Quiz Builder](/reference/quiz-builder/) and add a `Multiple choice question` asking the customer about their skin type: Dry, Normal, Oily, or Combination-type skin. 

        !!! tip

            Use the description box in `Question Settings -> Show Description` to help customers determine their skin type.

    2. **Create Multiple Results Pages**: In the [Results Page](/reference/quiz-builder/results-page/) tab, click on the `+` sign to add additional results pages. Create a separate results page for each skin type (Dry, Normal, Oily, Combination).

        ![how to set up multiple results pages](/images/how_to_set_up_multiple_results_pages.png)

    3. **Add Content to Each Results Page**: For each results page, add content blocks describing the specific skin type and its challenges. For example:

        !!! example

            - *You have Dry Skin*: The itchiness, tightness and dryness – we know your struggle! Your skin wants a routine that's deeply nourishing and hydrating.
            - *You have Normal Skin*: Your skin feels balanced, just like you! Even though your skin doesn't experience major issues, it deserves amazing care! Your skin wants a routine that sustains your skin's natural harmony.
            - *You have Oily Skin*: Your skin is oh-so shiny, but with excess oil instead of your natural glow! Your skin wants a routine that reduces oil to provide balance and clarity, all while giving your skin the proper amount of light hydration.
            - *You have Combination-Type Skin*: Your skin has multiple things going on at once: you experience your T-zone to be on the oily side, while the rest of your face is either normal or dry.

    4. **Add Product Blocks to Each Results Page**: For each results page, add a `Product Block` with the specific products you want to recommend for that skin type.

        ![how to add product blocks to results pages](/images/how_to_add_product_blocks_to_results_pages.png)

    5. **Set Up Jump Logic**: Go to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and set up Jump Logic to direct customers to the appropriate results page based on their skin type choice.

        ![how to set up jump logic for results pages](/images/how_to_set_up_jump_logic_for_results_pages.png)

        !!! tip

            For each choice in your skin type question, create a Jump Logic rule that directs to the corresponding results page.

    6. **Publish the changes**: Click the top-right `Publish` button to update the preview/live quiz.


## 🎯 Custom Scoring System 

Recommended for personality-type quizzes. Assign point values to choices and use the total scores to determine which products to recommend.

![how_to_shopify_v2_recommendations_scoring](/images/how_to_shopify_v2_recommendations_scoring.png)

### How It Works

- Assign numerical scores to each choice in your quiz
- Create score ranges that correspond to different recommendation categories
- Use display logic based on accumulated scores to show appropriate content

!!! info "Benefits"

    - Personality quizzes with variable outcomes
    - When you need to weigh different factors with varying importance
    - Creating nuanced recommendation categories


### How to Set Up a Custom Scoring System

1. Go to each question in your quiz
2. For each choice, open the choice settings
3. Assign appropriate point values to each choice

**Implementing score-based display logic:**

1. On the Results Page, select a content block
2. In the right-hand menu, locate Display Logic
3. Click on + Add condition (OR)
4. Use "The variable with the highest score..." or "The score of the variable..." option
5. Set up range conditions to control content visibility

!!! example 

    For skin type recommendations:
    - Assign points to choices (Dry: 1, Normal: 2, Oily: 3, Combination: 4, Sensitive: 5)

    Set display logic for content blocks based on total scores:
    - Dry skin content: Score between 5-7 points
    - Normal skin content: Score between 8-12 points
    - Oily skin content: Score between 13-17 points
    - Combination skin content: Score between 18-22 points
    - Sensitive skin content: Score between 23-25 points

