---
description: "Step-by-step guide to recommend RevenueHunt products based on the number of choices the customer selects."
icon: material/checkbox-multiple-marked-outline
---

# How to Recommend Products Based on the Number of Choices

Recommend a different group of products depending on how many choices the customer selects.

The quiz cannot do this on its own. This method adds a hidden choice for each possible outcome, then uses custom JavaScript to pick the right one.

!!! note "Before you start"

    This is not plug-and-play. If you are not familiar with JavaScript and CSS, ask a developer for help.

## Set up the recommendations

=== "Shopify"

    1. **Create one collection for each outcome.** Each collection holds the products for one outcome. Name them `1/10 choices selected`, `2/10 choices selected`, and so on.
    2. **Add one hidden choice per collection.** They all go in the final question of the quiz.
    3. **Link each choice to its collection.** See [Link Collections](/reference/quiz-builder/link-collections/).
    4. **Hide those choices with custom CSS.** The choices are there for the script, not for the customer. See [how to customize the quiz design](/how-to-guides/customize-quiz-design/).
    5. **Add custom JavaScript to the final question.** The script counts the choices the customer selected across the quiz. It then clicks the hidden choice that matches that number. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

        ![Custom JavaScript field in the question settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_questionsettings_customJS.png)
    6. **Click `Save`** to update the preview and the live quiz.

=== "Shopify (Legacy)"

    1. **Create one collection for each outcome.** Each collection holds the products for one outcome. Name them `1/10 choices selected`, `2/10 choices selected`, and so on.
    2. **Add one hidden choice per collection.** They all go in the final question of the quiz.
    3. **Link each choice to its collection.** See [Link Collections](/reference/quiz-builder/link-collections/).
    4. **Hide those choices with custom CSS.** The choices are there for the script, not for the customer. See [how to customize the quiz design](/how-to-guides/customize-quiz-design/).
    5. **Add custom JavaScript to the final question.** The script counts the choices the customer selected across the quiz. It then clicks the hidden choice that matches that number. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

        ![Custom JavaScript field in the question settings](/images/recommend-products-based-on-number-of-user-choices_image1.png)
    6. **Click `Publish`** to update the preview and the live quiz.

=== "WooCommerce"

    1. **Create one category for each outcome.** Each category holds the products for one outcome. Name them `1/10 choices selected`, `2/10 choices selected`, and so on.
    2. **Add one hidden choice per category.** They all go in the final question of the quiz.
    3. **Link each choice to its category.** See [Link Categories](/reference/quiz-builder/link-collections/).
    4. **Hide those choices with custom CSS.** The choices are there for the script, not for the customer. See [how to customize the quiz design](/how-to-guides/customize-quiz-design/).
    5. **Add custom JavaScript to the final question.** The script counts the choices the customer selected across the quiz. It then clicks the hidden choice that matches that number. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

        ![Custom JavaScript field in the question settings](/images/recommend-products-based-on-number-of-user-choices_image1.png)
    6. **Click `Publish`** to update the preview and the live quiz.

=== "Magento"

    1. **Create one category for each outcome.** Each category holds the products for one outcome. Name them `1/10 choices selected`, `2/10 choices selected`, and so on.
    2. **Add one hidden choice per category.** They all go in the final question of the quiz.
    3. **Link each choice to its category.** See [Link Categories](/reference/quiz-builder/link-collections/).
    4. **Hide those choices with custom CSS.** The choices are there for the script, not for the customer. See [how to customize the quiz design](/how-to-guides/customize-quiz-design/).
    5. **Add custom JavaScript to the final question.** The script counts the choices the customer selected across the quiz. It then clicks the hidden choice that matches that number. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

        ![Custom JavaScript field in the question settings](/images/recommend-products-based-on-number-of-user-choices_image1.png)
    6. **Click `Publish`** to update the preview and the live quiz.

=== "BigCommerce"

    1. **Create one category for each outcome.** Each category holds the products for one outcome. Name them `1/10 choices selected`, `2/10 choices selected`, and so on.
    2. **Add one hidden choice per category.** They all go in the final question of the quiz.
    3. **Link each choice to its category.** See [Link Categories](/reference/quiz-builder/link-collections/).
    4. **Hide those choices with custom CSS.** The choices are there for the script, not for the customer. See [how to customize the quiz design](/how-to-guides/customize-quiz-design/).
    5. **Add custom JavaScript to the final question.** The script counts the choices the customer selected across the quiz. It then clicks the hidden choice that matches that number. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

        ![Custom JavaScript field in the question settings](/images/recommend-products-based-on-number-of-user-choices_image1.png)
    6. **Click `Publish`** to update the preview and the live quiz.

=== "Standalone"

    1. **Create one collection for each outcome.** Each collection holds the products for one outcome. Name them `1/10 choices selected`, `2/10 choices selected`, and so on.
    2. **Add one hidden choice per collection.** They all go in the final question of the quiz.
    3. **Link each choice to its collection.** See [Link Collections](/reference/quiz-builder/link-collections/).
    4. **Hide those choices with custom CSS.** The choices are there for the script, not for the customer. See [how to customize the quiz design](/how-to-guides/customize-quiz-design/).
    5. **Add custom JavaScript to the final question.** The script counts the choices the customer selected across the quiz. It then clicks the hidden choice that matches that number. See [how to add JavaScript to the quiz](/how-to-guides/add-javascript/).

        ![Custom JavaScript field in the question settings](/images/recommend-products-based-on-number-of-user-choices_image1.png)
    6. **Click `Publish`** to update the preview and the live quiz.

## Find the choice IDs with JavaScript

=== "Shopify"

    Add this to the Custom JavaScript section of a question, then take the quiz with the browser console open (F12):

    ```javascript
    console.log('All answers by block:', quiz.answers.byBlock);
    ```

    It lists every block ID and its value. Each answer carries a `.choicesRefs` array holding the selected choice IDs. See [Find block and question IDs](/how-to-guides/add-javascript/#find-block-and-question-ids).

=== "Shopify (Legacy)"

    To see the choice IDs selected for each slide, open the JavaScript console and search for them:

    ![Choice IDs for a slide in the JavaScript console](/images/recommend-products-based-on-number-of-user-choices_image2.png)

    Type `prq.quizSlides()` in the console to list every slide with its ID. See [Find block and question IDs](/how-to-guides/add-javascript/#find-block-and-question-ids).

=== "WooCommerce"

    To see the choice IDs selected for each slide, open the JavaScript console and search for them:

    ![Choice IDs for a slide in the JavaScript console](/images/recommend-products-based-on-number-of-user-choices_image2.png)

    Type `prq.quizSlides()` in the console to list every slide with its ID. See [Find block and question IDs](/how-to-guides/add-javascript/#find-block-and-question-ids).

=== "Magento"

    To see the choice IDs selected for each slide, open the JavaScript console and search for them:

    ![Choice IDs for a slide in the JavaScript console](/images/recommend-products-based-on-number-of-user-choices_image2.png)

    Type `prq.quizSlides()` in the console to list every slide with its ID. See [Find block and question IDs](/how-to-guides/add-javascript/#find-block-and-question-ids).

=== "BigCommerce"

    To see the choice IDs selected for each slide, open the JavaScript console and search for them:

    ![Choice IDs for a slide in the JavaScript console](/images/recommend-products-based-on-number-of-user-choices_image2.png)

    Type `prq.quizSlides()` in the console to list every slide with its ID. See [Find block and question IDs](/how-to-guides/add-javascript/#find-block-and-question-ids).

=== "Standalone"

    To see the choice IDs selected for each slide, open the JavaScript console and search for them:

    ![Choice IDs for a slide in the JavaScript console](/images/recommend-products-based-on-number-of-user-choices_image2.png)

    Type `prq.quizSlides()` in the console to list every slide with its ID. See [Find block and question IDs](/how-to-guides/add-javascript/#find-block-and-question-ids).

---
This article explains how to recommend products based on the number of choices the customer selects.
