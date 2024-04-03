---
icon: material/cards
---

# How to Recommend Products

Our solution takes into account your customer's choices to offer highly personalized product recommendations. 

This guide explains how to recommend products with the Shop Quiz app, explains the underlying algorithm and proposes solutions for complex quizzes.

## Recommending Products

Shop Quiz can show on the results page product variants, main products and [Recharge subscription products](https://docs.revenuehunt.com/how-to-guides/recommend-subscription-products/). 

Shop Quiz cannot recommend collections of products, though it's possible to [only recommend products from a specific collection](https://docs.revenuehunt.com/how-to-guides/recommend-skincare-routine-slots/).

## Voting System

Our product recommendation algorithm works like a voting system:

- Products are linked to each choice
- When a customer picks a choice, all linked products receive one vote
- After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
- If no products have been linked or all the products have been excluded, the results page will appear empty
- If there's a draw in the number of votes, the app will randomize the order of products.

## Understanding Inclusion and Exclusion

### Inclusion
Products or collections added in the `include` field are upvoted in the final recommendations.

How the votes work for each included linked item:

- **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
- **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.
- **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
- **Variant collections**: Created automatically by the app, every product within a linked variant collection receives a vote when their linked choice is selected.
- **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives a vote when their linked choice is selected.
- **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting in [Quiz Settings](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-settings) is required for this option.

`❗Warning: If a product variant is linked to choice "A" (via the Link Products tab) and a collection of products that contain this product variant is also linked to choice "A" (via the Link Collections tab), then this product variant will receive 2 votes from the same choice.`

### Exclusion
Use the `exclude` field to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients. 

`❗Warning: Once a product is excluded in a choice it will never show as a recommendation, even if it's upvoted in another choice earlier/later in the quiz.`


## Recommending the Right Products

### Step 1: Link Products to Choices

1. **Access the Quiz Builder**: Navigate to the [Link Products](https://docs.revenuehunt.com/reference/quiz-builder/#link-products) or [Link Collections](https://docs.revenuehunt.com/reference/quiz-builder/#link-collections) tab within your quiz setup. 
2. **Assign Links to Choices**: For each choice, you can link product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.

### Step 2: Edit the Results Page

3. **Open Results Page**: In the Results Page tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. Check [How to Edit the Results Page](https://docs.revenuehunt.com/how-to-guides/edit-results-page/) for more information.
4. **Choose how to display the product results**: Products can be displayed as a list via the `Product Block` or divided into slots via the `Product Slot Block`. For beginners, it's recommended to use a `Product Block` to show the recommendations.
    - **Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) you can choose how many products you want to show at the end of the quiz.

    - **Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. Check [How to Recommend a Skincare Routine with Slots](https://docs.revenuehunt.com/how-to-guides/recommend-skincare-routine-slots/) for step-by-step instructions on how to set up Slot Blocks. 

### Step 3: Test the Results
 
1. **Publish the changes**: Click [`Publish`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) on the top-right menu. Don't worry, clicking `Publish` will not automatically add the quiz to your website. It will simply save the changes and allow you to preview the quiz.
2. **Preview the quiz**: Click [`Preview`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Use Investigation Tools to troubleshoot results**: Use the quiz's [built-in search bar](https://docs.revenuehunt.com/reference/quiz-builder/#responses) in the `Metrics > Responses` section to understand why specific products were recommended or missing from the recommendations. Check [How to Troubleshoot Quiz Results](https://docs.revenuehunt.com/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

### Step 4: Refine the Results

If you want to make the results ultra-precise, you can also:

1. **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
2. **Use Exclusions**: You can use [Exclusions]() to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

## Guide: How to Build Your Quiz Setup

Check the quiz below to learn how to build the quiz outcome you want:

<script src="https://admin.revenuehunt.com/embed.js" async></script><div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/GrHXAz" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>


## How to recommend products that match multiple criteria (matrix)

[This article](https://docs.revenuehunt.com/how-to-guides/recommend-product-matrix/) outlines a method for recommending skincare products based on multiple criteria using a product matrix to categorize recommendations. 



| Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
| 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |



It describes a step-by-step process involving creating product collections, building and linking quizzes to these collections, and utilizing a voting system algorithm to prioritize product suggestions, catering to complex customer profiles and ensuring personalized recommendations.

[:fontawesome-solid-arrow-right: learn more](https://docs.revenuehunt.com/how-to-guides/recommend-product-matrix/)

## How to Ensure a Specific Product Always Appears on Your Results Page

[This guide](https://docs.revenuehunt.com/how-to-guides/always-recommend-the-same-product/) provides a clear, step-by-step process to making sure that specific products are always visible on the Results Page of your quiz, regardless of the customer's choices.

[:fontawesome-solid-arrow-right: learn more](https://docs.revenuehunt.com/how-to-guides/always-recommend-the-same-product/)


 