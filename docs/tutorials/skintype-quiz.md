---
icon: material/numeric-3
description: "Create a skin type determination quiz with RevenueHunt that assigns scores and recommends personalized products."
---

# Building a Skin Type Quiz with RevenueHunt App

=== "Shopify"

    In this tutorial you will learn how to build a quiz that finds the customer's skin type and recommends the right products.

    !!! info "What you will learn"

        - how to build a personality-type quiz
        - how to assign scores and variables to choices
        - how to add a separate results page section for each result
        - how to use display logic to show the right section for the customer's answers
        - how to show fixed products on the results page
        - how to troubleshoot quiz results
        - how to publish the quiz as a linked button on your Shopify website

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/hRnkKBIzWFc?si=A6p-yYVTu4ZXPqc_" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    This tutorial covers quiz setup, variable assignment, results configuration, and adding the quiz to a Shopify store.


    ## Plan the quiz

    Before you build the quiz, plan what you want to show at the end.

    For each skin type, write a short description and decide which products to recommend. The five types are dry, oily, combination, normal and sensitive.

    You set these up on the results page later, so have them ready in advance.

    ??? example "Sample Skin Types & Recommendations Matrix:"

        | Skin Type          | Heading                | Description                                                                                                                                                                                                                                   | Recommended Products |
        |--------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
        | 🌵 Dry Skin         | You have Dry Skin       | Your skin tends to feel tight, rough or flaky, especially after washing. It may need extra TLC in the form of rich moisturizers and gentle, hydrating cleansers. Look for ingredients like hyaluronic acid, glycerin, and ceramides to help restore moisture and improve texture.<br><br>**Tip:** Avoid over-exfoliating and opt for creamy, non-stripping products. | 1. Relaxing Night Cream<br>2. Ultra Facial Deep Moisture Balm<br>3. Vitamin C Serum |
        | 🌼 Normal Skin      | You have Normal Skin    | Lucky you! Your skin feels balanced, neither too oily nor too dry. You may have occasional concerns, but overall, your skin is low-maintenance. Focus on maintaining that balance with a simple, consistent skincare routine.<br><br>**Tip:** Keep it steady with gentle cleansers, light hydration, and sunscreen. | 1. Morning Cleanser<br>2. Fresh Rose Deep Hydration Toner<br>3. Organix Facial Moisturizer |
        | 💧 Oily Skin        | You have Oily Skin      | Your skin produces more oil than average, especially in the T-zone. Shine and breakouts might be common, but the upside is slower visible aging! Stick with lightweight, non-comedogenic products that help balance oil without stripping your skin.<br><br>**Tip:** Use gel-based moisturizers, salicylic acid, and clay masks to manage oil and minimize pores. | 1. Balancing Force Oil Control Toner<br>2. Oil-Free Moisture-Combination Skin<br>3. Neutrogena Oil-Free Acne Face Wash |
        | 🌗 Combination Skin | You have Combination Skin | Your skin is a mix, oily in some spots such as the T-zone and dry or normal in others. You will benefit from targeting different areas with different products or using lightweight, balanced formulas.<br><br>**Tip:** Try multi-masking or spot-treating for a tailored approach to your skin’s varying needs. | 1. Oil-Free Moisture-Combination Skin<br>2. Super Antioxidant Serum<br>3. United State Balancing Tonic |
        | 🌸 Sensitive Skin   | You have Sensitive Skin | Your skin reacts easily, whether to weather changes, new products or stress. Redness, itching, or stinging might be common for you. A minimalist routine with soothing ingredients is your best friend.<br><br>**Tip:** Choose fragrance-free, hypoallergenic products with calming ingredients like aloe vera, chamomile, or calendula. | 1. Redness-Relief Refreshing Cleansing Lotion<br>2. Aloe Soothing Toner<br>3. Soothing Serum |


    ## Build the quiz

    Now build the quiz.

    1. Go to the [Quiz builder](/reference/quiz-builder/) > [Questions](/reference/quiz-builder/questions/).
    2. Add [multiple-choice questions](/reference/quiz-builder/questions/#multiple-choice) with 5 choices each. Each question and choice should give a clue about the customer's skin type.

        !!! tip
            To learn how to use the Quiz builder and add questions, see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).


        !!! example "Sample Questions:"

            Question 1: How does your skin feel when you wake up in the morning?

            - Choice 1: Tight
            - Choice 2: Normal
            - Choice 3: Oily
            - Choice 4: Combination
            - Choice 5: Sensitive

            Question 2: How does your skin usually look by midday?

            - Choice 1: Still tight
            - Choice 2: Same as in the morning
            - Choice 3: Shiny
            - Choice 4: T-zone shiny
            - Choice 5: Red and irritated



    ## Assign variables to choices

    Now assign variables and scores to each choice.

    1. Click on a choice to open the [Choice settings](/reference/quiz-builder/questions/#choice-settings).
    2. Scroll to `Scores & Calculations` and add a new variable.
    3. Click the `Search or create variable` search bar and type a variable name, for example `dry_skin`, `normal_skin` or `oily_skin`. A dropdown then offers `Create a new variable "xxx"`. Click it to add the variable.
    4. Assign a score of 1 to the matching variable.
    5. Repeat the process for each choice in that question and move on to the next question in your quiz.

        !!! note

            The variable with the highest total score determines the result.

        !!! example "Sample Scores & Variables:"

            Question 1: How does your skin feel when you wake up in the morning?

            - Choice 1: Tight (variable `dry_skin` +1)
            - Choice 2: Normal (variable `normal_skin` +1)
            - Choice 3: Oily (variable `oily_skin` +1)
            - Choice 4: Combination (variable `combination_skin` +1)
            - Choice 5: Sensitive (variable `sensitive_skin` +1)

            Question 2: How does your skin usually look by midday?

            - Choice 1: Still tight (variable `dry_skin` +1)
            - Choice 2: Same as in the morning (variable `normal_skin` +1)
            - Choice 3: Shiny (variable `oily_skin` +1)
            - Choice 4: T-zone shiny (variable `combination_skin` +1)
            - Choice 5: Red and irritated (variable `sensitive_skin` +1)


    ## Add sections to results page

    Now edit the Results page.

    1. Go to the [Results page](/reference/quiz-builder/results-page/).
    2. Click `+ Add section` to add a new section to your results page.
    3. Add five sections, one for each skin type.
    4. In each section, add:
        - A [heading](/reference/quiz-builder/results-page/#heading),
        - A short [text description](/reference/quiz-builder/results-page/#text) of what that means,
        - A [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections)
    5. In the [Product block settings](/reference/quiz-builder/results-page/#product-product-variants-collections), choose the Recommendations System to be `Fixed Recommendations`.
    6. In the [Product Slot](/reference/quiz-builder/results-page/#results-slot) settings, select the `Max. recommended items` and click on `Select products` to manually select the products that match that skin type.
    7. Repeat the process for each skin type section.



    ## Add display logic

    Now tell the app *when* to show each section.

    1. Click a specific section to open the `Results Section` settings.
    2. Go to [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) and click `+ Add condition (OR)`.
    3. Show the section when its variable has the highest score. Set the default visibility of every section to hidden.

        Set the conditions like this:

        - IF `the variable with the highest score` `IS` `dry_skin` THEN this section is VISIBLE.
        - Default visibility should be `HIDDEN`.

    4. Repeat this for each skin type section using their corresponding variable.

        !!! example "Sample Display logic:"

            - IF `the variable with the highest score` `IS` `dry_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `normal_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `oily_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `combination_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.
            - IF `the variable with the highest score` `IS` `sensitive_skin` THEN this section is VISIBLE. Default visibility should be `HIDDEN`.

    5. Save the changes with the `Save` button.

    ## Preview

    Once everything is set up, click `Preview` to test your quiz.

    Choose different answers to simulate different skin types, and make sure the correct section and products are shown on the results page.


    ## Troubleshoot results

    If you see the wrong result, double-check your variables and scoring in the [Questions](/reference/quiz-builder/questions/) tab.

    If you need help debugging, go to the [Responses](/reference/quiz-builder/metrics/#responses) tab and open [Analysis](/reference/quiz-builder/metrics/#response-analysis).

    This section:

    - shows you which variables were scored during a quiz session and in which answer,
    - shows logic behind sections visibility,
    - gives you an overview of the quiz results,
    - gives you access to [Quiz Copilot](/how-to-guides/use-quiz-copilot/), an AI assistant that can help you analyze the response.

    You can adjust scores or questions based on the analysis.



    ## Publish the quiz as link button

    In Shopify, link a button or a menu item to `#quiz` to make the quiz open as a popup.

    1. Set the quiz as default by going to the [Dashboard](/reference/dashboard/) and clicking on the `Set as default` button.
    2. Go to the [Publish](/reference/quiz-builder/share-publish/) tab and open `Add the quiz as a link-triggered popup` for step-by-step instructions.
    3. In Shopify, go to `Online Store > Themes`, and click `Customize` on your current theme.
    4. Go to `App Embeds` in the left sidebar. Find the `Link Popup Quiz` app embed and toggle it on. This loads the quiz script, so that the quiz opens in a popup when the link is clicked.
    5. In the theme editor, choose a section that contains a button, such as `Rich text`.
    6. Edit the section heading and the text on the button.
    7. In the `Button Link` field, type `#quiz`. Nothing else, and not a full URL.

        !!! warning
            Do not link the full URL, such as `https://your-store.com/#quiz`. The quiz does not open that way. Use the `#quiz` hash on its own.
    8. Once done, click `Save`.

    Your quiz is now live, and a popup link on your site opens it.

    You have created a skin type quiz with personalized product recommendations.

    !!! tip
        The [Create New Quiz](/reference/dashboard/#new-quiz) section has a ready-made template for this quiz. Use it as a starting point and customize it.



=== "Shopify (Legacy)"

    Scoring system is not available in the legacy version of the RevenueHunt app for Shopify. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead.

    !!! tip
        To recommend products based on the number of choices a customer makes, see [Winning variable quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). That section covers this version.


    !!! tip
        To add custom JavaScript to the Results Page, see [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "WooCommerce"

    Scoring system is not available in the RevenueHunt app for WooCommerce. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead.


    !!! tip
        To recommend products based on the number of choices a customer makes, see [Winning variable quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). That section covers this version.


    !!! tip
        To add custom JavaScript to the Results Page, see [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Magento"

    Scoring system is not available in the RevenueHunt app for Magento. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead.


    !!! tip
        To recommend products based on the number of choices a customer makes, see [Winning variable quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). That section covers this version.


    !!! tip
        To add custom JavaScript to the Results Page, see [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).



=== "BigCommerce"

    Scoring system is not available in the RevenueHunt app for BigCommerce. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead.


    !!! tip
        To recommend products based on the number of choices a customer makes, see [Winning variable quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). That section covers this version.


    !!! tip
        To add custom JavaScript to the Results Page, see [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).


=== "Standalone"

    Scoring system is not available in the Standalone version of the RevenueHunt app. For this reason building a personality-type quiz or a scoring quiz like this one is not possible with the off-the-shelf solution.

    Your developer can implement a custom scoring system with JavaScript on the Results Page instead.


    !!! tip
        To recommend products based on the number of choices a customer makes, see [Winning variable quiz](/how-to-guides/set-up-scoring-quiz/#winning-variable-quiz). That section covers this version.


    !!! tip
        To add custom JavaScript to the Results Page, see [How to Add Custom JavaScript to the Results Page](/how-to-guides/add-javascript/).

---
This article explains how to build a quiz that finds the customer skin type and recommends the right products.







