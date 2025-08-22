---
icon: material/numeric
---


# How to Recommend Products Based on Numerical Inputs

Recommending products based on numerical answers (like age or room size) can be tricky if you use open-ended input fields. This guide will show you how to structure these questions in your quiz to trigger tailored recommendations using finite answer choices.

=== "Shopify" 


=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/6bcdb3d771c74d49adb72a56910ba07f?sid=6b9950ee-7ef5-4483-8af4-6c14f32f87c7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

=== "WooCommerce" 


=== "Magento" 


=== "BigCommerce" 


=== "Standalone" 



## Why You Need a Structured Approach

=== "Shopify" 

    Open-ended numerical questions like [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) allow users to enter any value — but that flexibility comes with a cost: **you can't directly link recommendations to those answers**. To deliver accurate product suggestions, you'll need a structured approach.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    Questions like "What's your age?", "What's your birth date?" or "How big is your room?" might seem useful, but since users can input any number, you can't associate specific product recommendations with those responses.


=== "Shopify V2"

    Open-ended numerical questions like [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) allow users to enter any value — but that flexibility comes with a cost: **you can't directly link recommendations to those answers**. To deliver accurate product suggestions, you'll need a structured approach.

    ![open-ended numerical question](https://loom.com/i/934b3a724c0346829baf78e6261f22e4?workflows_screenshot=true)

    Questions like "What's your age?", "What's your birth date?" or "How big is your room?" might seem useful, but since users can input any number, you can't associate specific product recommendations with those responses.

=== "WooCommerce" 

    Open-ended numerical questions like [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) allow users to enter any value — but that flexibility comes with a cost: **you can't directly link recommendations to those answers**. To deliver accurate product suggestions, you'll need a structured approach.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    Questions like "What's your age?", "What's your birth date?" or "How big is your room?" might seem useful, but since users can input any number, you can't associate specific product recommendations with those responses.


=== "Magento" 

    Open-ended numerical questions like [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) allow users to enter any value — but that flexibility comes with a cost: **you can't directly link recommendations to those answers**. To deliver accurate product suggestions, you'll need a structured approach.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    Questions like "What's your age?", "What's your birth date?" or "How big is your room?" might seem useful, but since users can input any number, you can't associate specific product recommendations with those responses.

=== "BigCommerce" 

    Open-ended numerical questions like [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) allow users to enter any value — but that flexibility comes with a cost: **you can't directly link recommendations to those answers**. To deliver accurate product suggestions, you'll need a structured approach.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    Questions like "What's your age?", "What's your birth date?" or "How big is your room?" might seem useful, but since users can input any number, you can't associate specific product recommendations with those responses.

=== "Standalone" 

    Open-ended numerical questions like [Number](/reference/quiz-builder/questions/#number) or [Date](/reference/quiz-builder/questions/#date) allow users to enter any value — but that flexibility comes with a cost: **you can't directly link recommendations to those answers**. To deliver accurate product suggestions, you'll need a structured approach.

    ![open-ended numerical question](/images/how_to_recommend_products_based_on_numerical_inputs_shopify_agequestion_number.png)

    Questions like "What's your age?", "What's your birth date?" or "How big is your room?" might seem useful, but since users can input any number, you can't associate specific product recommendations with those responses.

## Use Finite Choices Instead

=== "Shopify"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What's your age?" from an input field to a dropdown with:

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

=== "Shopify V2"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What's your age?" from an input field to a dropdown with:

        - Under 20
        - 21–30
        - 31–40
        - Over 40

        This lets you assign relevant products to each range.

        ![use dropdown question to ask age ranges](https://loom.com/i/7606561efb5a4012860717b5ec6a468f?workflows_screenshot=true)

    !!! example "Example - Year of Birth"

        Change "What's your year of birth?" from an input field to a dropdown with:

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
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This is how to make sure that the product recommendation logic works in your quiz.


    !!! tip "Use Quiz Co-Pilot to Help"

        If you’re working with broader questions like “What’s your room size?”, use Quiz Co-Pilot to break it down into more useful options. It can suggest follow-up questions or ranges without you having to write them all manually.

        !!! example "Example - Room Size Ranges"

            Create a dropdown for room sizes like:

            - Less than 50 sqft
            - 51–100 sqft
            - 101–150 sqft
            - More than 150 sqft

            Quiz Co-Pilot can generate these for you automatically and help match them to recommendations.

            ![use quiz copilot to generate room size ranges](https://loom.com/i/8f81da1d43544435a45e5709b01fb436?workflows_screenshot=true)



=== "WooCommerce"

    To make recommendations work, **use multiple choice or dropdown questions**. Instead of asking for a number, offer predefined numbers or ranges.

    !!! example "Example - Age Ranges"

        Change "What's your age?" from an input field to a dropdown with:

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

        Change "What's your age?" from an input field to a dropdown with:

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

        Change "What's your age?" from an input field to a dropdown with:

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

        Change "What's your age?" from an input field to a dropdown with:

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


## Finalize the Setup

=== "Shopify"

    After generating options, you can:

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/questions/#block-settings)
    - Tweak the answer labels in [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Assign products to each choice via the [Choice Settings](/reference/quiz-builder/questions/#choice-settings)
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the user's choices

    This helps users select a range easily while ensuring you offer relevant products.

=== "Shopify V2"

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

    - Switch between question types (dropdown, multiple choice, etc.) via [Block Settings](/reference/quiz-builder/block-settings/)
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

## Custom Calculations

=== "Shopify"

    RevenueHunt Quizzes currently doesn't have a feature that would allow custom result calculations based on numerical user input.

    If you're building a quiz that requires custom calculations based on a precise numerical user input, for example a BMI calculation or dosage calculation, your developer can use the [Custom JavaScript](/how-to-guides/add-javascript/) feature to add custom logic to your quiz results page. This approach involves accessing the quiz answers via the `console.log()` on the results page, programing custom behaviors on the result page with JavaScript and printing an output onto an HTML element. 

    In our [JavaScript guide](/how-to-guides/add-javascript/) we provide an example of adding a [BMI calculator](/how-to-guides/add-javascript/#example-2-insert-calculations) to your results page. 

=== "Shopify V2"

    RevenueHunt Quizzes currently doesn't have a feature that would allow custom result calculations based on numerical user input.

    If you're building a quiz that requires custom calculations based on a precise numerical user input, for example a BMI calculation or dosage calculation, your developer can use the [Custom JavaScript](/how-to-guides/add-javascript/) feature to add custom logic to your quiz results page. This approach involves accessing the quiz answers via the `console.log()` on the results page, programing custom behaviors on the result page with JavaScript and printing an output onto an HTML element. 

    In our [JavaScript guide](/how-to-guides/add-javascript/) we provide an example of adding a [BMI calculator](/how-to-guides/add-javascript/#example-2-insert-calculations) to your results page. 

=== "WooCommerce"

    RevenueHunt Quizzes currently doesn't have a feature that would allow custom result calculations based on numerical user input.

    If you're building a quiz that requires custom calculations based on a precise numerical user input, for example a BMI calculation or dosage calculation, your developer can use the [Custom JavaScript](/how-to-guides/add-javascript/) feature to add custom logic to your quiz results page. This approach involves accessing the quiz answers via the `console.log()` on the results page, programing custom behaviors on the result page with JavaScript and printing an output onto an HTML element. 

    In our [JavaScript guide](/how-to-guides/add-javascript/) we provide an example of adding a [BMI calculator](/how-to-guides/add-javascript/#example-2-insert-calculations) to your results page. 

=== "Magento"

    RevenueHunt Quizzes currently doesn't have a feature that would allow custom result calculations based on numerical user input.

    If you're building a quiz that requires custom calculations based on a precise numerical user input, for example a BMI calculation or dosage calculation, your developer can use the [Custom JavaScript](/how-to-guides/add-javascript/) feature to add custom logic to your quiz results page. This approach involves accessing the quiz answers via the `console.log()` on the results page, programing custom behaviors on the result page with JavaScript and printing an output onto an HTML element. 

    In our [JavaScript guide](/how-to-guides/add-javascript/) we provide an example of adding a [BMI calculator](/how-to-guides/add-javascript/#example-2-insert-calculations) to your results page. 

=== "BigCommerce"

    RevenueHunt Quizzes currently doesn't have a feature that would allow custom result calculations based on numerical user input.

    If you're building a quiz that requires custom calculations based on a precise numerical user input, for example a BMI calculation or dosage calculation, your developer can use the [Custom JavaScript](/how-to-guides/add-javascript/) feature to add custom logic to your quiz results page. This approach involves accessing the quiz answers via the `console.log()` on the results page, programing custom behaviors on the result page with JavaScript and printing an output onto an HTML element. 

    In our [JavaScript guide](/how-to-guides/add-javascript/) we provide an example of adding a [BMI calculator](/how-to-guides/add-javascript/#example-2-insert-calculations) to your results page. 

=== "Standalone"

    RevenueHunt Quizzes currently doesn't have a feature that would allow custom result calculations based on numerical user input.

    If you're building a quiz that requires custom calculations based on a precise numerical user input, for example a BMI calculation or dosage calculation, your developer can use the [Custom JavaScript](/how-to-guides/add-javascript/) feature to add custom logic to your quiz results page. This approach involves accessing the quiz answers via the `console.log()` on the results page, programing custom behaviors on the result page with JavaScript and printing an output onto an HTML element. 

    In our [JavaScript guide](/how-to-guides/add-javascript/) we provide an example of adding a [BMI calculator](/how-to-guides/add-javascript/#example-2-insert-calculations) to your results page. 

---
This article explains how to recommend products based on numerical inputs in your quiz.

