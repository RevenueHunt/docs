# How to Recommend Products

Our solution takes into account your customer's choices to offer highly personalized product recommendations. This guide explains the underlying algorithm and how to effectively link products to quiz choices.

## Voting System

Our product recommendation algorithm works like a voting system:

- Products are linked to each choice
- When a customer picks a choice, all linked products receive one vote
- After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
- If no products have been linked or all the products have been excluded, the results page will appear empty
- If there's a draw in the number of votes, the app will randomize the order of products.

## Understanding Inclusion and Exclusion

**Inclusion**: Products or collections added in the "include" field are upvoted in the final recommendations.

How the votes work for each included linked item:

- **Product variants**: Individual variants receive a vote when their linked choice is selected. Note that only product variants are directly linked to choices. However, on the results page, variants can be grouped under their parent products for a streamlined shopping experience.
- **Collections**: Every product within a linked collection receives a vote when their linked choice is selected.
- **Tags**: Every product within a linked tag receives a vote when their linked choice is selected.
- **Variant collections**: Created automatically by the app, every product within a linked variant collection receives a vote when their linked choice is selected.
- **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives a vote when their linked choice is selected.
- **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting in [Quiz Settings](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-settings) is required for this option.

`❗Warning: If a product variant is linked to choice "A" (via the Link Products tab) and a collection of products that contain this product variant is also linked to choice "A" (via the Link Collections tab), then this product variant will receive 2 votes from the same choice.`

**Exclusion**: Use the "exclude" field to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients. 

`❗Warning: Once a product is excluded in a choice it will never show as a recommendation, even if it's upvoted in another choice earlier/later in the quiz.`


## Recommending the Right Products

### Step 1: Link Products to Choices

1. **Access the Quiz Builder**: Navigate to the [Link Products]() or [Link Collections]() tab within your quiz setup. 
2. **Assign Links to Choices**: For each choice, you can link product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.

### Step 2: Edit the Results Page

3. **Open Results Page**: In the Results Page tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block. Check [How to Edit the Results Page]() for more information.
4. **Choose how to display the product results**: Products can be displayed as a list via the Product Block or divided into slots via the Product Slot Block. For beginners, it's recommended to use a Product Block to show the recommendations.

**Product Block** displays the products sorted by the number of votes - the most voted products are shown first, and the least voted last. In [Product Block settings]() you can choose how many products you want to show at the end of the quiz.

**Product Slot Blocks** allow you to display the products in clear steps, for example as a skincare routine. Each Product Slot will recommend the most-voted product from a collection that's linked to it. Check [How to Recommend a Skincare Routine with Slots]() for step-by-step instructions on how to set up Slot Blocks. 

### Step 3: Test the Results
 
1. **Publish the changes**: Click [`Publish`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) on the top-right menu. Don't worry, clicking `Publish` will not automatically add the quiz to your website. It will simply save the changes and allow you to preview the quiz.
2. **Preview the quiz**: Click [`Preview`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Use Investigation Tools to troubleshoot results**: Use the quiz's [built-in search bar]() in the `Metrics > Responses` section to understand why specific products were recommended or missing from the recommendations. Check [How to Check Why a Product was Recommended or Not]() for detailed instructions on how to use this tool.

### Step 4: Refine the Results

If you want to make the results ultra-precise, you can also:

1. **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X votes or more in the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
2. **Use Exclusions**: You can use [Exclusions]() to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

By linking product variants and collections to quiz choices, and understanding the inclusion/exclusion logic, you can use our algorithm to offer precise product recommendations.

## How to recommend products that match multiple criteria (matrix)

Let’s say that you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

This means that your product matrix looks something like this:

| Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
| 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |


### Step 1: Understand the algorithm

First of all, you should understand that the recommendations algorithm works like a [voting system](#voting-system). Products are linked to each choice. When a customer picks that choice, all the linked products receive one vote. When the quiz is done, products with the highest amount of votes will show on the Results page first, then products with less votes.

### Step 2: Create collections
To recommend the right product, in your eCommerce platform you should create four collections and include in them the following products:

Collection 1: Teens and 20's

| Age/Skin type  | Dry or Normal                                                                                       | Oily                                                                                                              |
|----------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Teens and 20’s | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion |

Collection 2: 30’s and above

| Age/Skin type  | Dry or Normal                                                                                           | Oily                                                                                                                  |
|----------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 30’s and above | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

Collection 3: Dry or Normal Skin

| Skin Type     | Products                                                                                                                                                                                                                                                                                  |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dry or Normal | **Teens and 20’s:**<br>Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel<br>**30’s and above:**<br>All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer |

Collection 4: Oily Skin

| Skin Type | Products                                                                                                                                                                                                                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Oily      | **Teens and 20’s:**<br>Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion<br>**30’s and above:**<br>FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

After creating products or collections you may need to sync the app with your store. Here‘s [How to Sync Your Catalog with the App](https://docs.revenuehunt.com/how-to-guides/how-to-sync-catalog/).

### Step 3: Build the quiz

Then, you can start building your quiz. 

1. **Add new quiz**: Go to the Shop Quiz app and click on `add new quiz`. 
2. **Name the quiz**: Name the quiz and you’ll be directed to the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer. 

The first question is about the client’s age.

![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

The second question is about client’s skin type.

![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

### Step 4: Link collections

Now you should link the collections created in [Step 2](#step-2-create-collections) to the choices in the quiz. 

1. **Open Link Collections tab**: To do that, navigate to the [Link Collections](https://docs.revenuehunt.com/reference/quiz-builder/#link-collections) tab in the Quiz Builder.
2. **Link Collections to choices**: Link the collections to chocies as shown below.

![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

### Step 5: Create a Products block on the Results Page

For the products to show on the Results Page, you need to add a Products Block. 

1. **Go to the Results Page tab**: You can do that by navigating to the Results Page.
2. **Add a Product Block**:  Clicking the `+` to add a block type. Slect a Product Block from the dropdown list.
3. **Limit the numebr of recommended products**: In this example, we should limit the amount of recommended products to 4 (based on the matrix). To limit the number of recommended products shown open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

### Step 6: Preview the quiz and check results

Now that the quiz is built and product are linked to each choice, you can test the quiz. To test the quiz, you'll have to save the changes and preview it.

1. **Publish the changes**: Click [`Publish`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) on the top-right menu. Don't worry, clicking `Publish` will not automatically add the quiz to your website. It will simply save the changes and allow you to preview the quiz.
2. **Preview the quiz**: Click [`Preview`](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Check results** : Go through the quiz and check if the correct products are recommended. Let’s check this answering route:

What’s your age?
- 30’s and above

How does your skin feel on an average day?
- Oily
 
If the quiz is set up correctly, the following products should be recommended in accordance with the product matrix:

![how to recommend products matrix resutls1](/images/how_to_recommend_products_results1.png)

If you’re not getting the expected results, please check [this article]() to learn how to troubleshoot the quiz results.

**Why were these products recommended?**

To understand the quiz results, we need to recall how the voting system works. Every product linked to a choice receives one vote when clicked on. In the end, the products with the most votes will be recommended first on the Results Page.

- So in our example, if the user selects “30’s and above” in the first question, the following 8 products will receive 1 vote each:

![how to recommend products matrix table1](/images/how_to_recommend_products_table1.png)

- Next, if the user selects “Oily”, the following 8 products will receive 1 vote each:

![how to recommend products matrix table2](/images/how_to_recommend_products_table2.png)

- After the two questions, the following 4 products will already have 2 votes each, because they were part of both collections:

![how to recommend products matrix table2](/images/how_to_recommend_products_table3.png)

These products recieved the most amount of votes (2) so they were recommended.

![how to recommend products matrix resutls1](/images/how_to_recommend_products_results1.png)

When products receive the same amount of votes, the algorithm randomizes the order in which they are shown on the Results page.

If you’d like to organize the products in a specific order, you can create Product Slots on the Results Page. Check [this article]() to learn how to do that.

## How to recommend products that match multiple criteria (complex matrix)

If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations.  Let’s look at the matrix below. 

![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

For this complex matrix, creating separate collections for each outcome is possible, but there’s also an alternative. What you can do instead is to pick one of the factors and create branching in the quiz with [Jump Logic](https://docs.revenuehunt.com/reference/quiz-builder/#jump-logic). This will allow you to show the customer the same questions but link different products to each branch, therefore resulting in different outcomes.

Here’s an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branchign factor:

![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

The Jump Logic for bnranching is applied to *Question 2*, the skin type question.

![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

This setup allows you to link different products to the same questions leading to differnt results, while maintaining the same customer experince.

`❗Warning: A lot of conditional logic can significantly slow down the loading times of the quiz builder app (it doesn’t affect the quiz as viewed by the customer though). If you plan on building a quiz with a lot of conditional logic, consider splitting the quiz into multiple smaller quizzes instead. There’s no limit to how many quizzes can be published on your webiste. In the example above, you can create 4 different quizzes for skin types (Dry, Oily, Combination, or Normal skin), or you can create a quiz for different age groups.`
 