---
description: "Learn how to create a RevenueHunt product matrix to recommend products based on multiple criteria."
icon: material/grid
---

# How to Recommend Products That Match Multiple Criteria

This article outlines a method for recommending skincare products based on multiple criteria using a product matrix to categorize recommendations.

It covers creating product collections, linking products to choices, and the voting system that ranks the recommendations.

## Simple product matrix

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/e9bNK96Vt8k?si=q_Dq-G2JVwskpaQx" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Say you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

    This means that your product matrix looks something like this:

    | Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
    |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
    | 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

=== "Shopify (Legacy)"

    Say you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

    This means that your product matrix looks something like this:

    | Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
    |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
    | 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

=== "WooCommerce"

    Say you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

    This means that your product matrix looks something like this:

    | Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
    |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
    | 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

=== "Magento"

    Say you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

    This means that your product matrix looks something like this:

    | Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
    |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
    | 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

=== "BigCommerce"

    Say you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

    This means that your product matrix looks something like this:

    | Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
    |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
    | 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

=== "Standalone"

    Say you run a skincare shop and want to recommend a product based on two criteria – the client’s age and skin type.

    This means that your product matrix looks something like this:

    | Age/Skin type   | Dry or Normal                                                                                                                                                 | Oily                                                                                                                                                                  |
    |-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Teens and 20’s  | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel                   | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion     |
    | 30’s and above  | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer                     | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary “Buffet” + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin           |

### Step 1: understand the algorithm

First of all, you should understand that the recommendations algorithm works like a [voting system](#step-1-understand-the-algorithm).

??? question "How do I get the right recommendations?"

    The recommendation algorithm works like a voting system:

    - Products are linked to each choice
    - When a customer picks a choice, all linked products receive one vote
    - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
    - If no products have been linked or all the products have been excluded, the results page will appear empty
    - If there is a draw in the number of votes, the order depends on your Catalogue mode setting. By default, ties are randomized. Enable 'Preserve collection order' in [Settings > Catalogue](/reference/app-settings/#catalogue) to show products in the same order as your Shopify collections.

    If you want to make the results ultra-precise, you can also:

    - Limit the recommendations to only show products that received X votes or more in the [Results Page settings](/reference/quiz-builder/results-page/#advanced-settings).
    - Use [Exclusions](/how-to-guides/set-up-funnel-quiz/#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

### Step 2: create collections/categories

To recommend the right product, in your ecommerce platform you should create four collections/categories and include in them the following products:

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

!!! tip "Sync your catalog"

    After creating products or collections you may need to sync the app with your store. Here‘s [How to Sync Your Catalog with the App](/how-to-guides/sync-catalog/).

### Step 3: build the quiz

=== "Shopify"

    You can start building your quiz.

    1. **Add new quiz**: Go to the RevenueHunt app and click on `+ Add new quiz`.
    2. **Name the quiz**: Name the quiz. The [Quiz builder](/reference/quiz-builder/) then opens.
    3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer.

        - The first question is about the client’s age.

        ![how to recommend products matrix question1](/images/how_to_shopifyv2_recommend_product_matrix_question1.png)

        - The second question is about client’s skin type.

        ![how to recommend products matrix question2](/images/how_to_shopifyv2_recommend_product_matrix_question2.png)

=== "Shopify (Legacy)"

    You can start building your quiz.

    1. **Add new quiz**: Go to the RevenueHunt app and click on `add new quiz`.
    2. **Name the quiz**: Name the quiz. The [Quiz Builder](/reference/quiz-builder/) then opens.
    3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer.

        - The first question is about the client’s age.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

        - The second question is about client’s skin type.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

=== "WooCommerce"

    You can start building your quiz.

    1. **Add new quiz**: Go to the RevenueHunt app and click on `add new quiz`.
    2. **Name the quiz**: Name the quiz. The [Quiz Builder](/reference/quiz-builder/) then opens.
    3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer.

        - The first question is about the client’s age.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

        - The second question is about client’s skin type.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

=== "Magento"

    You can start building your quiz.

    1. **Add new quiz**: Go to the RevenueHunt app and click on `add new quiz`.
    2. **Name the quiz**: Name the quiz. The [Quiz Builder](/reference/quiz-builder/) then opens.
    3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer.

        - The first question is about the client’s age.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

        - The second question is about client’s skin type.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

=== "BigCommerce"

    You can start building your quiz.

    1. **Add new quiz**: Go to the RevenueHunt app and click on `add new quiz`.
    2. **Name the quiz**: Name the quiz. The [Quiz Builder](/reference/quiz-builder/) then opens.
    3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer.

        - The first question is about the client’s age.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

        - The second question is about client’s skin type.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

=== "Standalone"

    You can start building your quiz.

    1. **Add new quiz**: Go to the RevenueHunt app and click on `add new quiz`.
    2. **Name the quiz**: Name the quiz. The [Quiz Builder](/reference/quiz-builder/) then opens.
    3. **Add questions**: Based on the above table, two questions will be necessary to determine the right product for the customer.

        - The first question is about the client’s age.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

        - The second question is about client’s skin type.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

### Step 4: link collections/categories

=== "Shopify"

    Upvote the collections you made in [Step 2: create collections/categories](#step-2-create-collectionscategories) to the choices in the quiz.

    1. **Open Choice settings**: In the Quiz builder, open the [Questions](/reference/quiz-builder/questions/) tab. Click a choice to open its [Choice settings](/reference/quiz-builder/questions/#choice-settings).
    2. **Upvote Collections**: In Choice settings, find the `Upvote` button and select `Collections` from the dropdown.
    3. For each choice find a collection to be added from your catalog and add it to the choice.

        ![how to recommend products matrix link collections](/images/how_to_shopifyv2_recommend_product_matrix_upvotecollections.png)

=== "Shopify (Legacy)"

    Link the collections you made in [Step 2: create collections/categories](#step-2-create-collectionscategories) to the choices in the quiz.

    1. **Open Link Collections/Categories tab**: To do that, navigate to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.
    2. **Link Collections/Categories to choices**: Link each collection or category to a choice.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

=== "WooCommerce"

    Link the collections you made in [Step 2: create collections/categories](#step-2-create-collectionscategories) to the choices in the quiz.

    1. **Open Link Collections/Categories tab**: To do that, navigate to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.
    2. **Link Collections/Categories to choices**: Link each collection or category to a choice.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

=== "Magento"

    Link the collections you made in [Step 2: create collections/categories](#step-2-create-collectionscategories) to the choices in the quiz.

    1. **Open Link Collections/Categories tab**: To do that, navigate to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.
    2. **Link Collections/Categories to choices**: Link each collection or category to a choice.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

=== "BigCommerce"

    Link the collections you made in [Step 2: create collections/categories](#step-2-create-collectionscategories) to the choices in the quiz.

    1. **Open Link Collections/Categories tab**: To do that, navigate to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.
    2. **Link Collections/Categories to choices**: Link each collection or category to a choice.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

=== "Standalone"

    Link the collections you made in [Step 2: create collections/categories](#step-2-create-collectionscategories) to the choices in the quiz.

    1. **Open Link Collections/Categories tab**: To do that, navigate to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.
    2. **Link Collections/Categories to choices**: Link each collection or category to a choice.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

### Step 5: create a products block on the results page

=== "Shopify"

    For the products to show on the Results page, you need to add a `Products Block`.

    1. **Go to the Results page tab**: You can do that by navigating to the [Results page](/reference/quiz-builder/results-page/).
    2. **Add a Product block**: Click `+ Add block` to add a block. Select `Product Block` from the dropdown list.
    3. **Limit the number of recommended products**: This matrix needs a limit of 4. Open the [`Product Block settings`](/reference/quiz-builder/results-page/#product-product-variants-collections) and select how many products should be recommended in this Product block from the dropdown.

=== "Shopify (Legacy)"

    For the products to show on the Results Page, you need to add a `Products Block`.

    1. **Go to the Results Page tab**: You can do that by navigating to the [Results Page](/reference/quiz-builder/results-page/).
    2. **Add a Product Block**: Click `+` to add a block. Select `Product Block` from the dropdown list.
    3. **Limit the number of recommended products**: This matrix needs a limit of 4. Open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

=== "WooCommerce"

    For the products to show on the Results Page, you need to add a `Products Block`.

    1. **Go to the Results Page tab**: You can do that by navigating to the [Results Page](/reference/quiz-builder/results-page/).
    2. **Add a Product Block**: Click `+` to add a block. Select `Product Block` from the dropdown list.
    3. **Limit the number of recommended products**: This matrix needs a limit of 4. Open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

=== "Magento"

    For the products to show on the Results Page, you need to add a `Products Block`.

    1. **Go to the Results Page tab**: You can do that by navigating to the [Results Page](/reference/quiz-builder/results-page/).
    2. **Add a Product Block**: Click `+` to add a block. Select `Product Block` from the dropdown list.
    3. **Limit the number of recommended products**: This matrix needs a limit of 4. Open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

=== "BigCommerce"

    For the products to show on the Results Page, you need to add a `Products Block`.

    1. **Go to the Results Page tab**: You can do that by navigating to the [Results Page](/reference/quiz-builder/results-page/).
    2. **Add a Product Block**: Click `+` to add a block. Select `Product Block` from the dropdown list.
    3. **Limit the number of recommended products**: This matrix needs a limit of 4. Open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

=== "Standalone"

    For the products to show on the Results Page, you need to add a `Products Block`.

    1. **Go to the Results Page tab**: You can do that by navigating to the [Results Page](/reference/quiz-builder/results-page/).
    2. **Add a Product Block**: Click `+` to add a block. Select `Product Block` from the dropdown list.
    3. **Limit the number of recommended products**: This matrix needs a limit of 4. Open the `Product Block settings` and select how many products should be recommended in this Product Block from the dropdown.

### Step 6: preview the quiz and check results

Now that the quiz is built and the products are linked to each choice, you can test the quiz. Save the changes, then preview it.

1. **Publish the changes**: Click [`Publish/Save`](/reference/quiz-builder/questions/) in the top-right menu. That does not add the quiz to your website. It saves the changes so you can preview the quiz.
2. **Preview the quiz**: Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz you created in a new window. You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.
3. **Check results** : Go through the quiz and check if the correct products are recommended. Check this answering route:

    - What is your age?
        - 30’s and above

    - How does your skin feel on an average day?
        - Oily

If the quiz is set up correctly, the following products should be recommended in accordance with the product matrix:

![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

If you do not get the expected results, see [How to Troubleshoot Product Recommendations in Your Quiz](/how-to-guides/troubleshoot-product-results/) to learn how to troubleshoot the quiz results.

??? question "Why were these products recommended?"

    To understand the quiz results, recall how the voting system works. Every product linked to a choice receives one vote when clicked on. In the end, the products with the most votes will be recommended first on the Results Page.

    - In this example, if the user selects “30’s and above” in the first question, the following 8 products will receive 1 vote each:

        ![how to recommend products matrix table1](/images/how_to_recommend_products_table1.png)

    - Next, if the user selects “Oily”, the following 8 products will receive 1 vote each:

        ![how to recommend products matrix table2](/images/how_to_recommend_products_table2.png)

    - After the two questions, the following 4 products will already have 2 votes each, because they were part of both collections:

        ![how to recommend products matrix table2](/images/how_to_recommend_products_table3.png)

    These products received the most amount of votes (2) so they were recommended.

    ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

    When products receive the same amount of votes, the algorithm randomizes the order in which they are shown on the Results page. By default, ties are randomized. Enable 'Preserve collection order' in [Settings > Catalogue](/reference/app-settings/#catalogue) to show products in the same order as your Shopify collections.

To organize the products in a specific order, create `Product Slots` on the Results Page. See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/) to learn how to do that.

## Complex product matrix

=== "Shopify"

    If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations. Look at the matrix below.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

    The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

    For this complex matrix, creating separate collections for each outcome is possible, but there is also an **alternative**.

    Instead, pick one of the factors and branch the quiz with [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic). That lets you show the customer the same questions, and link different products to each branch, therefore resulting in different outcomes.

    Here is an example of a Conditional logic tree for the Matrix above where Skin Type was chosen as a branching factor:

    ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

    !!! tip

        Check this guide [Set up fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up a quiz with fixed recommendations and display logic for very precise product recommendations.

=== "Shopify (Legacy)"

    If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations. Look at the matrix below.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

    The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

    For this complex matrix, creating separate collections for each outcome is possible, but there is also an alternative. Instead, pick one of the factors and branch the quiz with [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic). That lets you show the customer the same questions, and link different products to each branch, therefore resulting in different outcomes.

    Here is an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branching factor:

    ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

    This setup lets you link different products to the same questions, so the results differ while the customer experience stays the same.

    !!! tip

        Check this guide [Set up fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up a quiz with fixed recommendations and display logic for very precise product recommendations.

    !!! warning

        A lot of conditional logic slows down the quiz builder app. It does not affect the quiz as the customer sees it.

        If you plan on building a quiz with a lot of conditional logic, **consider splitting the quiz into multiple smaller quizzes** instead. There is no limit to how many quizzes can be published on your website.

        In the example above, you can create 4 quizzes, one per skin type. You can also create a quiz for each age group.

=== "WooCommerce"

    If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations. Look at the matrix below.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

    The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

    For this complex matrix, creating separate collections for each outcome is possible, but there is also an alternative. Instead, pick one of the factors and branch the quiz with [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic). That lets you show the customer the same questions, and link different products to each branch, therefore resulting in different outcomes.

    Here is an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branching factor:

    ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

    This setup lets you link different products to the same questions, so the results differ while the customer experience stays the same.

    !!! tip

        Check this guide [Set up fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up a quiz with fixed recommendations and display logic for very precise product recommendations.

    !!! warning

        A lot of conditional logic slows down the quiz builder app. It does not affect the quiz as the customer sees it.

        If you plan on building a quiz with a lot of conditional logic, **consider splitting the quiz into multiple smaller quizzes** instead. There is no limit to how many quizzes can be published on your website.

        In the example above, you can create 4 quizzes, one per skin type. You can also create a quiz for each age group.

=== "Magento"

    If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations. Look at the matrix below.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

    The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

    For this complex matrix, creating separate collections for each outcome is possible, but there is also an alternative. Instead, pick one of the factors and branch the quiz with [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic). That lets you show the customer the same questions, and link different products to each branch, therefore resulting in different outcomes.

    Here is an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branching factor:

    ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

    This setup lets you link different products to the same questions, so the results differ while the customer experience stays the same.

    !!! tip

        Check this guide [Set up fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up a quiz with fixed recommendations and display logic for very precise product recommendations.

    !!! warning

        A lot of conditional logic slows down the quiz builder app. It does not affect the quiz as the customer sees it.

        If you plan on building a quiz with a lot of conditional logic, **consider splitting the quiz into multiple smaller quizzes** instead. There is no limit to how many quizzes can be published on your website.

        In the example above, you can create 4 quizzes, one per skin type. You can also create a quiz for each age group.

=== "BigCommerce"

    If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations. Look at the matrix below.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

    The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

    For this complex matrix, creating separate collections for each outcome is possible, but there is also an alternative. Instead, pick one of the factors and branch the quiz with [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic). That lets you show the customer the same questions, and link different products to each branch, therefore resulting in different outcomes.

    Here is an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branching factor:

    ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

    This setup lets you link different products to the same questions, so the results differ while the customer experience stays the same.

    !!! tip

        Check this guide [Set up fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up a quiz with fixed recommendations and display logic for very precise product recommendations.

    !!! warning

        A lot of conditional logic slows down the quiz builder app. It does not affect the quiz as the customer sees it.

        If you plan on building a quiz with a lot of conditional logic, **consider splitting the quiz into multiple smaller quizzes** instead. There is no limit to how many quizzes can be published on your website.

        In the example above, you can create 4 quizzes, one per skin type. You can also create a quiz for each age group.

=== "Standalone"

    If your product Matrix looks more like a list, there is another way to achieve your precise product recommendations. Look at the matrix below.

    ![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

    The outcome of the quiz depends on 3 factors: skin type, age, and skin concern. In each case, the products recommended differing.

    For this complex matrix, creating separate collections for each outcome is possible, but there is also an alternative. Instead, pick one of the factors and branch the quiz with [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic). That lets you show the customer the same questions, and link different products to each branch, therefore resulting in different outcomes.

    Here is an example of a Conditional Logic tree for the Matrix above where Skin Type was chosen as a branching factor:

    ![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    And *Questions 4, 6, 8, and 10* to point the customer to the Results Page directly after completing the branch:

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

    This setup lets you link different products to the same questions, so the results differ while the customer experience stays the same.

    !!! tip

        Check this guide [Set up fixed recommendations quiz](/how-to-guides/set-up-fixed-recommendations-quiz/) to learn how to set up a quiz with fixed recommendations and display logic for very precise product recommendations.

    !!! warning

        A lot of conditional logic slows down the quiz builder app. It does not affect the quiz as the customer sees it.

        If you plan on building a quiz with a lot of conditional logic, **consider splitting the quiz into multiple smaller quizzes** instead. There is no limit to how many quizzes can be published on your website.

        In the example above, you can create 4 quizzes, one per skin type. You can also create a quiz for each age group.

---
This article explains how to set up a quiz with a product matrix. For a more detailed guide on setting up a quiz with product recommendations, see [How to Set Up Recommendations](/how-to-guides/set-up-recommendations/).