---
description: "Learn how to create a RevenueHunt product matrix to recommend products based on multiple criteria."
icon: material/grid
---

# How to Recommend Products That Match Multiple Criteria

A product matrix recommends a product from two or more criteria at once, such as the customer's age and their skin type.

You build one by grouping the products by criterion, then upvoting the matching group from each choice. The quiz counts the upvotes, and the products that sit in both groups come out on top.

!!! info "How the recommendations are picked"

    Each choice upvotes the products linked to it, and the results page lists the products with the most upvotes first. See [Upvoting system](/how-to-guides/set-up-funnel-quiz/#upvoting-system) for the whole algorithm, including ties and exclusions.

## Simple product matrix

Say you run a skincare shop, and you want to recommend products from two criteria: the customer's age and their skin type. The matrix looks like this.

| Age / Skin type | Dry or Normal | Oily |
|---|---|---|
| Teens and 20's | Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion |
| 30's and above | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary "Buffet" + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/e9bNK96Vt8k?si=q_Dq-G2JVwskpaQx" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

The walkthrough shows the `💎Built for Shopify` version of the app.

### The four groups this matrix needs

One group per value in the matrix: two for the age ranges, and two for the skin types. Every product appears in exactly two of them, one from each criterion.

**Teens and 20's**

| Dry or Normal | Oily |
|---|---|
| Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion |

**30's and above**

| Dry or Normal | Oily |
|---|---|
| All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary "Buffet" + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

**Dry or Normal skin**

| Teens and 20's | 30's and above |
|---|---|
| Redness-Relief Refreshing Cleansing Lotion;<br>Ultra Facial Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Moisturizing Cream-Gel | All Natural Face Cleanser;<br>Fresh Rose Deep Hydration Toner;<br>Khadi Global Natural Hyaluronic Acid Serum;<br>Organix Facial Moisturizer |

**Oily skin**

| Teens and 20's | 30's and above |
|---|---|
| Neutrogena Oil-Free Acne Face Wash;<br>Balancing Force Oil Control Toner;<br>Resist Ultra-Light Super Antioxidant Concentrate Serum;<br>Oil-Free Moisture Lotion | FIRST AID BEAUTY FACE CLEANSER;<br>Balancing Force Oil Control Toner;<br>The Ordinary "Buffet" + Copper Peptides 1%;<br>Oil-Free Moisture-Combination Skin |

### Build the quiz

=== "Shopify"

    1. **Create four collections in your Shopify store.** Two for the age ranges, and two for the skin types.

    2. **Add the products of each group to its collection.** A product that belongs to two groups goes in both.

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new collections.

    4. **Open the app and click `+ Add new quiz`.**

    5. **Name the quiz.** The [Quiz builder](/reference/quiz-builder/) opens.

    6. **Add a multiple-choice question about the customer's age.** Give it the choices Teens and 20's, and 30's and above.

        ![how to recommend products matrix question1](/images/how_to_shopifyv2_recommend_product_matrix_question1.png)

    7. **Add a second question about the customer's skin type.** Give it the choices Dry or Normal, and Oily.

        ![how to recommend products matrix question2](/images/how_to_shopifyv2_recommend_product_matrix_question2.png)

    8. **Open a choice in [Questions](/reference/quiz-builder/questions/), then open its [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

    9. **Click `Upvote`, select `Collections`, and pick the collection that matches the choice.** Repeat for all four choices.

        ![how to recommend products matrix link collections](/images/how_to_shopifyv2_recommend_product_matrix_upvotecollections.png)

    10. **Go to the [Results page](/reference/quiz-builder/results-page/) tab and add a `Products Block`.** Click `+ Add block` and select it from the list.

    11. **Limit the block to 4 products in the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).** This matrix recommends four products, one per step of the routine.

    12. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    13. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.** Answer `30's and above`, then `Oily`.

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    14. **Check that the four products of that cell are the ones recommended.**

        ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

=== "Shopify (Legacy)"

    1. **Create four collections in your Shopify store.** Two for the age ranges, and two for the skin types.

    2. **Add the products of each group to its collection.** A product that belongs to two groups goes in both.

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new collections.

    4. **Open the app and click `add new quiz`.**

    5. **Name the quiz.** The [Quiz Builder](/reference/quiz-builder/) opens.

    6. **Add a multiple-choice question about the customer's age.** Give it the choices Teens and 20's, and 30's and above.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

    7. **Add a second question about the customer's skin type.** Give it the choices Dry or Normal, and Oily.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

    8. **Go to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.**

    9. **Link the collection that matches each choice.** Repeat for all four choices.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

    10. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add a `Products Block`.** Click `+` and select it from the list.

    11. **Limit the block to 4 products in the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).** This matrix recommends four products, one per step of the routine.

    12. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    13. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.** Answer `30's and above`, then `Oily`.

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    14. **Check that the four products of that cell are the ones recommended.**

        ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

=== "WooCommerce"

    1. **Create four categories in your WooCommerce store.** Two for the age ranges, and two for the skin types.

    2. **Add the products of each group to its category.** A product that belongs to two groups goes in both.

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new categories.

    4. **Open the app and click `add new quiz`.**

    5. **Name the quiz.** The [Quiz Builder](/reference/quiz-builder/) opens.

    6. **Add a multiple-choice question about the customer's age.** Give it the choices Teens and 20's, and 30's and above.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

    7. **Add a second question about the customer's skin type.** Give it the choices Dry or Normal, and Oily.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

    8. **Go to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.**

    9. **Link the category that matches each choice.** Repeat for all four choices.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

    10. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add a `Products Block`.** Click `+` and select it from the list.

    11. **Limit the block to 4 products in the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).** This matrix recommends four products, one per step of the routine.

    12. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    13. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.** Answer `30's and above`, then `Oily`.

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    14. **Check that the four products of that cell are the ones recommended.**

        ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

=== "Magento"

    1. **Create four categories in your Magento store.** Two for the age ranges, and two for the skin types.

    2. **Add the products of each group to its category.** A product that belongs to two groups goes in both.

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new categories.

    4. **Open the app and click `add new quiz`.**

    5. **Name the quiz.** The [Quiz Builder](/reference/quiz-builder/) opens.

    6. **Add a multiple-choice question about the customer's age.** Give it the choices Teens and 20's, and 30's and above.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

    7. **Add a second question about the customer's skin type.** Give it the choices Dry or Normal, and Oily.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

    8. **Go to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.**

    9. **Link the category that matches each choice.** Repeat for all four choices.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

    10. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add a `Products Block`.** Click `+` and select it from the list.

    11. **Limit the block to 4 products in the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).** This matrix recommends four products, one per step of the routine.

    12. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    13. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.** Answer `30's and above`, then `Oily`.

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    14. **Check that the four products of that cell are the ones recommended.**

        ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

=== "BigCommerce"

    1. **Create four categories in your BigCommerce store.** Two for the age ranges, and two for the skin types.

    2. **Add the products of each group to its category.** A product that belongs to two groups goes in both.

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new categories.

    4. **Open the app and click `add new quiz`.**

    5. **Name the quiz.** The [Quiz Builder](/reference/quiz-builder/) opens.

    6. **Add a multiple-choice question about the customer's age.** Give it the choices Teens and 20's, and 30's and above.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

    7. **Add a second question about the customer's skin type.** Give it the choices Dry or Normal, and Oily.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

    8. **Go to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.**

    9. **Link the category that matches each choice.** Repeat for all four choices.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

    10. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add a `Products Block`.** Click `+` and select it from the list.

    11. **Limit the block to 4 products in the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).** This matrix recommends four products, one per step of the routine.

    12. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    13. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.** Answer `30's and above`, then `Oily`.

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    14. **Check that the four products of that cell are the ones recommended.**

        ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

=== "Standalone"

    1. **Create four collections in your Standalone account.** Two for the age ranges, and two for the skin types.

    2. **Add the products of each group to its collection.** A product that belongs to two groups goes in both.

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new collections.

    4. **Open the app and click `add new quiz`.**

    5. **Name the quiz.** The [Quiz Builder](/reference/quiz-builder/) opens.

    6. **Add a multiple-choice question about the customer's age.** Give it the choices Teens and 20's, and 30's and above.

        ![how to recommend products matrix question1](/images/how_to_recommend_products_question1.png)

    7. **Add a second question about the customer's skin type.** Give it the choices Dry or Normal, and Oily.

        ![how to recommend products matrix question2](/images/how_to_recommend_products_question2.png)

    8. **Go to the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder.**

    9. **Link the collection that matches each choice.** Repeat for all four choices.

        ![how to recommend products matrix link collections](/images/how_to_recommend_products_linkcollections.png)

    10. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add a `Products Block`.** Click `+` and select it from the list.

    11. **Limit the block to 4 products in the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).** This matrix recommends four products, one per step of the routine.

    12. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    13. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.** Answer `30's and above`, then `Oily`.

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    14. **Check that the four products of that cell are the ones recommended.**

        ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

!!! tip "Putting the products in a fixed order"

    A products block lists the recommendations by upvote count. To pin them to a fixed order instead, such as cleanser, then toner, then serum, use `Product Slots`. See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).

??? question "Why were those four products recommended?"

    Every product linked to a choice receives one upvote when the customer picks that choice. The products with the most upvotes are recommended first.

    Answering `30's and above` gives one upvote to these eight products:

    ![how to recommend products matrix table1](/images/how_to_recommend_products_table1.png)

    Answering `Oily` gives one upvote to these eight:

    ![how to recommend products matrix table2](/images/how_to_recommend_products_table2.png)

    Four products sit in both groups, so they end on two upvotes each:

    ![how to recommend products matrix table3](/images/how_to_recommend_products_table3.png)

    Those four have the most upvotes, so those four are recommended.

    ![how to recommend products matrix results1](/images/how_to_recommend_products_results1.png)

If the recommendations are not the ones you expect, see [How to Troubleshoot Product Recommendations in Your Quiz](/how-to-guides/troubleshoot-product-results/).

## Complex product matrix

Some matrices read more like a list. This one decides the outcome from three criteria: skin type, age and skin concern.

![how to recommend products complex matrix](/images/how_to_recommend_products_complexmatrix.png)

You can still build a group per outcome, but the number of groups grows fast. The alternative is to pick one criterion and branch the quiz on it with [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic). Each branch asks the same questions, and links its own products to them. The outcomes differ, while the quiz feels the same to the customer.

Here is a conditional logic tree for that matrix, branching on skin type.

![how to recommend products complex matrix logic tree](/images/how_to_recommend_products_complexmatrix_logictree.png)

=== "Shopify"

    Put the Jump logic on the skin type question, and on the last question of every branch. Each branch then leads straight to the results page.

=== "Shopify (Legacy)"

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    *Questions 4, 6, 8 and 10* then point the customer to the Results Page, so each branch ends there.

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

=== "WooCommerce"

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    *Questions 4, 6, 8 and 10* then point the customer to the Results Page, so each branch ends there.

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

=== "Magento"

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    *Questions 4, 6, 8 and 10* then point the customer to the Results Page, so each branch ends there.

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

=== "BigCommerce"

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    *Questions 4, 6, 8 and 10* then point the customer to the Results Page, so each branch ends there.

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

=== "Standalone"

    The Jump Logic for branching is applied to *Question 2*, the skin type question.

    ![how to recommend products complex matrix jump logic 1](/images/how_to_recommend_products_complexmatrix_jumplogic1.png)

    ![how to recommend products complex matrix jump logic 2](/images/how_to_recommend_products_complexmatrix_jumplogic2.png)

    *Questions 4, 6, 8 and 10* then point the customer to the Results Page, so each branch ends there.

    ![how to recommend products complex matrix jump logic 3](/images/how_to_recommend_products_complexmatrix_jumplogic3.png)

!!! warning "A lot of logic slows the Quiz Builder down"

    The quiz stays fast for the customer. The builder is what slows down.

    For a quiz with a lot of conditional logic, consider splitting it into several smaller quizzes instead. There is no limit on how many quizzes you publish on your website. In the example, that means one quiz per skin type, or one per age range.

!!! tip "Fixed recommendations instead"

    To pick the products for each outcome yourself, rather than letting upvotes decide, see [How to Set Up a Fixed Recommendations Quiz](/how-to-guides/set-up-fixed-recommendations-quiz/).

---

This article explains how to recommend products that match several criteria at once, using a product matrix. For the recommendation systems the app offers, see [How to Set Up Recommendations](/how-to-guides/set-up-recommendations/).