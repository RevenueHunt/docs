---
icon: material/numeric
description: "Learn how to structure RevenueHunt quiz questions to recommend products based on numerical answers."
---

# How to Recommend Products Based on Numerical Inputs

A quiz cannot link a recommendation to a number the customer types. Ask for a range instead of a figure, and the answers become finite enough to carry products.

<div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/m92ELGhOq38?si=H7vJC9sn44PVQfd7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

The walkthrough shows the `💎Built for Shopify` version of the app.

## Why an open-ended number does not work

A [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) question lets the customer enter any value at all. **There is no answer to attach a product to.**

"What is your age?" and "How big is your room?" look like useful questions. Because the customer can type any figure, neither one can drive a recommendation.

=== "Shopify"

    ![open-ended numerical question](https://loom.com/i/934b3a724c0346829baf78e6261f22e4?workflows_screenshot=true)

=== "Shopify (Legacy)"

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

=== "WooCommerce"

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

=== "Magento"

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

=== "BigCommerce"

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

=== "Standalone"

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

## Use finite choices instead

Ask the same thing with a multiple-choice, dropdown or slider question. Offer ranges, or a fixed set of values, so that every answer is one you can link products to.

!!! example "Age ranges"

    Change "What is your age?" from an input field to a dropdown with these choices:

    - Under 20
    - 21-30
    - 31-40
    - Over 40

=== "Shopify"

    ![use dropdown question to ask age ranges](https://loom.com/i/7606561efb5a4012860717b5ec6a468f?workflows_screenshot=true)

=== "Shopify (Legacy)"

    ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

=== "WooCommerce"

    ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

=== "Magento"

    ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

=== "BigCommerce"

    ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

=== "Standalone"

    ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

!!! example "Year of birth"

    Where the exact value matters, list the values themselves. Change "What is your year of birth?" from an input field to a dropdown with one choice per year:

    - 1990
    - 1991
    - 1992
    - 1993
    - 1994
    - 1995
    - 1996

    ![use dropdown question to ask year of birth](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_yearbirthquestion_dropdown.png)

Once the answers are finite, you can:

- [Upvote](/reference/quiz-builder/link-products/) products, variants or collections from each choice
- Switch the question between dropdown, multiple-choice and slider in the [Block settings](/reference/quiz-builder/questions/#block-settings)
- Edit the labels in the [Choice settings](/reference/quiz-builder/questions/#choice-settings)
- Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) from the customer's answer

!!! tip "Quiz Copilot can suggest the ranges"

    In the `💎Built for Shopify` version, Quiz Copilot turns a broad question such as "What is your room size?" into ranges for you. It also suggests the follow-up questions to go with them.

    For room size, that might be:

    - Less than 50 sq ft
    - 51-100 sq ft
    - 101-150 sq ft
    - More than 150 sq ft

    ![use quiz copilot to generate room size ranges](https://loom.com/i/8f81da1d43544435a45e5709b01fb436?workflows_screenshot=true)

## Custom calculations

The app cannot calculate a result from a number on its own. A quiz that works out a BMI, a dosage or any other figure needs [custom JavaScript](/how-to-guides/add-javascript/) and a developer.

The script reads the quiz answers, works the result out in JavaScript, then writes it into an HTML element on the results page.

[How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has a worked BMI calculator.

---

This article explains how to recommend products based on numerical inputs in your quiz.
