---
icon: material/numeric
description: "Learn how to structure RevenueHunt quiz questions to recommend products based on numerical answers."
---

# How to Recommend Products Based on Numerical Inputs

Recommending products based on numerical answers (like age or room size) can be tricky if you use open-ended input fields. This guide will show you how to structure these questions in your quiz to trigger tailored recommendations using finite answer choices.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/m92ELGhOq38?si=H7vJC9sn44PVQfd7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "Shopify (Legacy)"

=== "WooCommerce"

=== "Magento"

=== "BigCommerce"

=== "Standalone"


## Why you need a structured approach

=== "Shopify"

    An open-ended numerical question, such as [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date), lets the customer enter any value. **You cannot link a recommendation to an answer like that.** A structured approach is needed instead.

    ![open-ended numerical question](https://loom.com/i/934b3a724c0346829baf78e6261f22e4?workflows_screenshot=true)

    A question such as "What is your age?" or "How big is your room?" looks useful. Because the customer can type any number, you cannot tie a product recommendation to the answer.

=== "Shopify (Legacy)"

    An open-ended numerical question, such as [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date), lets the customer enter any value. **You cannot link a recommendation to an answer like that.** A structured approach is needed instead.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    A question such as "What is your age?" or "How big is your room?" looks useful. Because the customer can type any number, you cannot tie a product recommendation to the answer.

=== "WooCommerce"

    An open-ended numerical question, such as [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date), lets the customer enter any value. **You cannot link a recommendation to an answer like that.** A structured approach is needed instead.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    A question such as "What is your age?" or "How big is your room?" looks useful. Because the customer can type any number, you cannot tie a product recommendation to the answer.

=== "Magento"

    An open-ended numerical question, such as [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date), lets the customer enter any value. **You cannot link a recommendation to an answer like that.** A structured approach is needed instead.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    A question such as "What is your age?" or "How big is your room?" looks useful. Because the customer can type any number, you cannot tie a product recommendation to the answer.

=== "BigCommerce"

    An open-ended numerical question, such as [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date), lets the customer enter any value. **You cannot link a recommendation to an answer like that.** A structured approach is needed instead.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    A question such as "What is your age?" or "How big is your room?" looks useful. Because the customer can type any number, you cannot tie a product recommendation to the answer.

=== "Standalone"

    An open-ended numerical question, such as [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date), lets the customer enter any value. **You cannot link a recommendation to an answer like that.** A structured approach is needed instead.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    A question such as "What is your age?" or "How big is your room?" looks useful. Because the customer can type any number, you cannot tie a product recommendation to the answer.

## Use finite choices instead

=== "Shopify"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What is your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](https://loom.com/i/7606561efb5a4012860717b5ec6a468f?workflows_screenshot=true)

    !!! example "Example - Year of Birth"

        Change "What is your year of birth?" from an input field to a dropdown with:

        - 1990
        - 1991
        - 1992
        - 1993
        - 1994
        - 1995
        - 1996

        This lets you assign relevant products to each year.

        ![use dropdown question to ask year of birth](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_yearbirthquestion_dropdown.png)

    Once you switch to finite answers, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants or collections to each choice
    - Set up [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.

    !!! tip "Use Quiz Copilot to Help"

        For a broader question such as “What is your room size?”, use Quiz Copilot to break it down into more useful options. It can suggest follow-up questions or ranges without you having to write them all manually.

        !!! example "Example - Room Size Ranges"

            Create a dropdown for room sizes like:

            - Less than 50 sq ft
            - 51–100 sq ft
            - 101–150 sq ft
            - More than 150 sq ft

            Quiz Copilot can generate these for you automatically and help match them to recommendations.

            ![use quiz copilot to generate room size ranges](https://loom.com/i/8f81da1d43544435a45e5709b01fb436?workflows_screenshot=true)

=== "Shopify (Legacy)"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What is your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

    Once you switch to finite answers, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.

=== "WooCommerce"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What is your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

    Once you switch to finite answers, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.

=== "Magento"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What is your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

    Once you switch to finite answers, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.

=== "BigCommerce"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What is your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

    Once you switch to finite answers, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.

=== "Standalone"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What is your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_dropdown.png)

    Once you switch to finite answers, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.

## Finalize the setup

=== "Shopify"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

=== "Shopify (Legacy)"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

=== "WooCommerce"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

=== "Magento"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

=== "BigCommerce"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

=== "Standalone"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

## Custom calculations

=== "Shopify"

    The RevenueHunt app cannot calculate a result from a numerical input on its own.

    Your developer can use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. That covers a quiz that needs a calculation from a precise number, such as BMI or a dosage.

    The script reads the quiz answers with `console.log()`, works out the result in JavaScript, then prints it into an HTML element.

    [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has an example of a BMI calculator on the results page.

=== "Shopify (Legacy)"

    The RevenueHunt app cannot calculate a result from a numerical input on its own.

    Your developer can use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. That covers a quiz that needs a calculation from a precise number, such as BMI or a dosage.

    The script reads the quiz answers with `console.log()`, works out the result in JavaScript, then prints it into an HTML element.

    [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has an example of a BMI calculator on the results page.

=== "WooCommerce"

    The RevenueHunt app cannot calculate a result from a numerical input on its own.

    Your developer can use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. That covers a quiz that needs a calculation from a precise number, such as BMI or a dosage.

    The script reads the quiz answers with `console.log()`, works out the result in JavaScript, then prints it into an HTML element.

    [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has an example of a BMI calculator on the results page.

=== "Magento"

    The RevenueHunt app cannot calculate a result from a numerical input on its own.

    Your developer can use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. That covers a quiz that needs a calculation from a precise number, such as BMI or a dosage.

    The script reads the quiz answers with `console.log()`, works out the result in JavaScript, then prints it into an HTML element.

    [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has an example of a BMI calculator on the results page.

=== "BigCommerce"

    The RevenueHunt app cannot calculate a result from a numerical input on its own.

    Your developer can use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. That covers a quiz that needs a calculation from a precise number, such as BMI or a dosage.

    The script reads the quiz answers with `console.log()`, works out the result in JavaScript, then prints it into an HTML element.

    [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has an example of a BMI calculator on the results page.

=== "Standalone"

    The RevenueHunt app cannot calculate a result from a numerical input on its own.

    Your developer can use [Custom JavaScript](/how-to-guides/add-javascript/) on the results page. That covers a quiz that needs a calculation from a precise number, such as BMI or a dosage.

    The script reads the quiz answers with `console.log()`, works out the result in JavaScript, then prints it into an HTML element.

    [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/#example-2-insert-calculations) has an example of a BMI calculator on the results page.

---
This article explains how to recommend products based on numerical inputs in your quiz.

