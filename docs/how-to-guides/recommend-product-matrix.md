# How to recommend products that match multiple criteria (matrix)

This article outlines a method for recommending skincare products based on multiple criteria using a product matrix to categorize recommendations. 

It describes a step-by-step process involving creating product collections, linking products, and using a voting system algorithm to prioritize product suggestions, catering to complex customer profiles and ensuring personalized recommendations.

## Simple product matrix

Let’s say that you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

This means that your product matrix looks something like this:

| Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
| 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |


### Step 1: Understand the algorithm

First of all, you should understand that the recommendations algorithm works like a [voting system](#voting-system). 


??? question "How do I get the right recommendations?"

    Our product recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there's a draw in the number of votes, the app will randomize the order of products.

    If you want to make the results ultra-precise, you can also:

    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/reference/quiz-builder/results-page/#advanced-settings).
    - Use [Exclusions](/how-to-guides/recommend-products/#understanding-inclusion-and-exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).



### Step 2: Create collections/categories

To recommend the right product, in your eCommerce platform you should create four collections/categories and include in them the following products:

- Collection 1: Teens and 20's

| Age/Skin type  | Dry or Normal                                                                                       | Oily                                                                                                          |
|----------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Teens and 20’s | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion |

- Collection 2: 30’s and above

| Age/Skin type  | Dry or Normal                                                                                           | Oily                                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 30’s and above | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

- Collection 3: Dry or Normal Skin

| Skin Type     | Products                                                                                                                                                                                                                                                                                  |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dry or Normal | **Teens and 20’s:**<br>Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel<br>**30’s and above:**<br>All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer |

- Collection 4: Oily Skin

| Skin Type | Products                                                                                                                                                                                                                                                                 |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Oily      | **Teens and 20’s:**<br>Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion<br>**30’s and above:**<br>FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

After creating products or collections you may need to sync the app with your store. Here‘s [How to Sync Your Catalog with the App](/how-to-guides/sync-catalog/).

### Step 3: Build the quiz

You can start building your quiz. 

1. **Add new quiz**: Go to the RevenueHunt app and click on `add new quiz`. 
2. **Name the quiz**: Name the quiz and you’ll be directed to the [Quiz Builder](/reference/quiz-builder/).
3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer. 

    - The first question is about the client’s age.

    ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

    - The second question is about client’s skin type.

    ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

### Step 4: Link collections/categories

You should link the collections created in [Step 2](#step-2-create-collections) to the choices in the quiz. 

1. **Open Link Collections/Categories tab**: To do that, navigate to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.
2. **Link Collections/Categories to choices**: Link the collections/categories to chocies as shown below.

    ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

### Step 5: Create a Products block on the Results Page

For the products to show on the Results Page, you need to add a `Products Block`. 

1. **Go to the Results Page tab**: You can do that by navigating to the [Results Page](/reference/quiz-builder/results-page/).
2. **Add a Product Block**:  Clicking the `+` to add a block type. Slect a `Product Block` from the dropdown list.
3. **Limit the numebr of recommended products**: In this example, we should limit the amount of recommended products to 4 (based on the matrix). To limit the number of recommended products shown open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

### Step 6: Preview the quiz and check results

Now that the quiz is built and product are linked to each choice, you can test the quiz. To test the quiz, you'll have to save the changes and preview it.

1. **Publish the changes**: Click [`Publish`](/reference/quiz-builder/questions/) on the top-right menu. Don't worry, clicking `Publish` will not automatically add the quiz to your website. It will simply save the changes and allow you to preview the quiz.
2. **Preview the quiz**: Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you've created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Check results** : Go through the quiz and check if the correct products are recommended. Let’s check this answering route:

    - What’s your age?
        - 30’s and above

    - How does your skin feel on an average day?
        - Oily
 
If the quiz is set up correctly, the following products should be recommended in accordance with the product matrix:

![how to recommend products matrix resutls1](/images/how_to_recommend_products_results1.png)

If you’re not getting the expected results, please check [this article](/how-to-guides/troubleshoot-product-results/) to learn how to troubleshoot the quiz results.

??? question "Why were these products recommended?"

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

If you’d like to organize the products in a specific order, you can create `Product Slots` on the Results Page. Check [this article](/how-to-guides/recommend-skincare-routine-slots/) to learn how to do that.

## Complex product matrix

If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations.  Let’s look at the matrix below. 

![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

For this complex matrix, creating separate collections for each outcome is possible, but there’s also an alternative. What you can do instead is to pick one of the factors and create branching in the quiz with [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic). This will allow you to show the customer the same questions but link different products to each branch, therefore resulting in different outcomes.

Here’s an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branchign factor:

![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

The Jump Logic for bnranching is applied to *Question 2*, the skin type question.

![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

This setup allows you to link different products to the same questions leading to differnt results, while maintaining the same customer experince.

!!! warning

    A lot of conditional logic can significantly slow down the loading times of the quiz builder app (it doesn’t affect the quiz as viewed by the customer though). 
    
    If you plan on building a quiz with a lot of conditional logic, **consider splitting the quiz into multiple smaller quizzes** instead. There’s no limit to how many quizzes can be published on your webiste. 
    
    In the example above, you can create 4 different quizzes for skin types (Dry, Oily, Combination, or Normal skin), or you can create a quiz for different age groups.
