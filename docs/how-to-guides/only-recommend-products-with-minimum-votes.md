---
description: "Step-by-step guide to limit RevenueHunt product recommendations by showing only products with a minimum number of upvotes."
icon: material/vote-outline
---

# How to Only Recommend Products with X Upvotes or More

You can limit the recommendations on the results page to products that received X upvotes or more. This filter lets you show only the strongest matches.

To activate this setting in your quiz:

=== "Shopify"

    1. Make sure your [results page](/reference/quiz-builder/results-page/) has a **Product block** or a **Product Slot block**.
    2. Make sure you understand how the [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            The recommendation algorithm works like an upvoting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one upvote
            - After the customer takes the quiz, the results page shows the products with the most upvotes first
            - If no products are linked, or all products are excluded, the results page is empty
            - If there is a draw in the number of upvotes, the app randomizes the order of the products.

    3. Open the [Results page](/reference/quiz-builder/results-page/).
    4. Open the [Product block Settings](/reference/quiz-builder/results-page/#block-settings).
    5. Scroll down to the `Min. number of upvotes` setting.
        ![Min. number of upvotes in the product block settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    6. Click the dropdown, or use the slider, to select a number. You can change the minimum to whatever suits your quiz.

        !!! example

            Your quiz has 4 questions, and you set the minimum to 4. Only products with **4 upvotes or more** are shown, so a product has to match the answer to every question. A product with 3 upvotes is not shown. A product with 5 upvotes is shown.

    7. Click `Save` in the top-right corner to update the preview and the live quiz.

    From now on, only products that receive this minimum number of upvotes will show up as a recommendation on the results page.

=== "Shopify (Legacy)"

    1. Make sure your [results page](/reference/quiz-builder/results-page/) has a **Product Block** or a **Product Slot Block**.
    2. Make sure you understand how the [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            The recommendation algorithm works like an upvoting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one upvote
            - After the customer takes the quiz, the results page shows the products with the most upvotes first
            - If no products are linked, or all products are excluded, the results page is empty
            - If there is a draw in the number of upvotes, the app randomizes the order of the products.

    3. Open the [Results Page settings](/reference/quiz-builder/results-page/).
    4. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    5. Scroll down to the `Minimum number of votes` setting and turn the toggle on.
        ![Minimum number of votes in the Advanced Settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    6. The **Products Block**, or a **Slots Block**, on your results page now shows an extra setting in the [Block Settings](/reference/quiz-builder/results-page/#block-settings).
    7. Open the [Product/Slot Block settings](/reference/quiz-builder/results-page/#block-settings) and find `Min. number of votes`.
    8. Click the dropdown and select a number. You can change the minimum to whatever suits your quiz.
        ![Min. number of votes in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example

            Your quiz has 4 questions, and you set the minimum to 4. Only products with **4 upvotes or more** are shown, so a product has to match the answer to every question. A product with 3 upvotes is not shown. A product with 5 upvotes is shown.

    9. Click `Publish` in the top-right corner to update the preview and the live quiz.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The `Minimum number of votes` setting is available only if you choose not to recommend products when the results are empty. That option is in [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![Show random products in the Recommendation Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "WooCommerce"

    1. Make sure your [results page](/reference/quiz-builder/results-page/) has a **Product Block** or a **Product Slot Block**.
    2. Make sure you understand how the [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            The recommendation algorithm works like an upvoting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one upvote
            - After the customer takes the quiz, the results page shows the products with the most upvotes first
            - If no products are linked, or all products are excluded, the results page is empty
            - If there is a draw in the number of upvotes, the app randomizes the order of the products.

    3. Open the [Results Page settings](/reference/quiz-builder/results-page/).
    4. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    5. Scroll down to the `Minimum number of votes` setting and turn the toggle on.
        ![Minimum number of votes in the Advanced Settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    6. The **Products Block**, or a **Slots Block**, on your results page now shows an extra setting in the [Block Settings](/reference/quiz-builder/results-page/#block-settings).
    7. Open the [Product/Slot Block settings](/reference/quiz-builder/results-page/#block-settings) and find `Min. number of votes`.
    8. Click the dropdown and select a number. You can change the minimum to whatever suits your quiz.
        ![Min. number of votes in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example

            Your quiz has 4 questions, and you set the minimum to 4. Only products with **4 upvotes or more** are shown, so a product has to match the answer to every question. A product with 3 upvotes is not shown. A product with 5 upvotes is shown.

    9. Click `Publish` in the top-right corner to update the preview and the live quiz.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The `Minimum number of votes` setting is available only if you choose not to recommend products when the results are empty. That option is in [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![Show random products in the Recommendation Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "Magento"

    1. Make sure your [results page](/reference/quiz-builder/results-page/) has a **Product Block** or a **Product Slot Block**.
    2. Make sure you understand how the [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            The recommendation algorithm works like an upvoting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one upvote
            - After the customer takes the quiz, the results page shows the products with the most upvotes first
            - If no products are linked, or all products are excluded, the results page is empty
            - If there is a draw in the number of upvotes, the app randomizes the order of the products.

    3. Open the [Results Page settings](/reference/quiz-builder/results-page/).
    4. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    5. Scroll down to the `Minimum number of votes` setting and turn the toggle on.
        ![Minimum number of votes in the Advanced Settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    6. The **Products Block**, or a **Slots Block**, on your results page now shows an extra setting in the [Block Settings](/reference/quiz-builder/results-page/#block-settings).
    7. Open the [Product/Slot Block settings](/reference/quiz-builder/results-page/#block-settings) and find `Min. number of votes`.
    8. Click the dropdown and select a number. You can change the minimum to whatever suits your quiz.
        ![Min. number of votes in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example

            Your quiz has 4 questions, and you set the minimum to 4. Only products with **4 upvotes or more** are shown, so a product has to match the answer to every question. A product with 3 upvotes is not shown. A product with 5 upvotes is shown.

    9. Click `Publish` in the top-right corner to update the preview and the live quiz.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The `Minimum number of votes` setting is available only if you choose not to recommend products when the results are empty. That option is in [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![Show random products in the Recommendation Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "BigCommerce"

    1. Make sure your [results page](/reference/quiz-builder/results-page/) has a **Product Block** or a **Product Slot Block**.
    2. Make sure you understand how the [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            The recommendation algorithm works like an upvoting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one upvote
            - After the customer takes the quiz, the results page shows the products with the most upvotes first
            - If no products are linked, or all products are excluded, the results page is empty
            - If there is a draw in the number of upvotes, the app randomizes the order of the products.

    3. Open the [Results Page settings](/reference/quiz-builder/results-page/).
    4. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    5. Scroll down to the `Minimum number of votes` setting and turn the toggle on.
        ![Minimum number of votes in the Advanced Settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    6. The **Products Block**, or a **Slots Block**, on your results page now shows an extra setting in the [Block Settings](/reference/quiz-builder/results-page/#block-settings).
    7. Open the [Product/Slot Block settings](/reference/quiz-builder/results-page/#block-settings) and find `Min. number of votes`.
    8. Click the dropdown and select a number. You can change the minimum to whatever suits your quiz.
        ![Min. number of votes in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example

            Your quiz has 4 questions, and you set the minimum to 4. Only products with **4 upvotes or more** are shown, so a product has to match the answer to every question. A product with 3 upvotes is not shown. A product with 5 upvotes is shown.

    9. Click `Publish` in the top-right corner to update the preview and the live quiz.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The `Minimum number of votes` setting is available only if you choose not to recommend products when the results are empty. That option is in [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![Show random products in the Recommendation Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "Standalone"

    1. Make sure your [results page](/reference/quiz-builder/results-page/) has a **Product Block** or a **Product Slot Block**.
    2. Make sure you understand how the [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            The recommendation algorithm works like an upvoting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one upvote
            - After the customer takes the quiz, the results page shows the products with the most upvotes first
            - If no products are linked, or all products are excluded, the results page is empty
            - If there is a draw in the number of upvotes, the app randomizes the order of the products.

    3. Open the [Results Page settings](/reference/quiz-builder/results-page/).
    4. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    5. Scroll down to the `Minimum number of votes` setting and turn the toggle on.
        ![Minimum number of votes in the Advanced Settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    6. The **Products Block**, or a **Slots Block**, on your results page now shows an extra setting in the [Block Settings](/reference/quiz-builder/results-page/#block-settings).
    7. Open the [Product/Slot Block settings](/reference/quiz-builder/results-page/#block-settings) and find `Min. number of votes`.
    8. Click the dropdown and select a number. You can change the minimum to whatever suits your quiz.
        ![Min. number of votes in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example

            Your quiz has 4 questions, and you set the minimum to 4. Only products with **4 upvotes or more** are shown, so a product has to match the answer to every question. A product with 3 upvotes is not shown. A product with 5 upvotes is shown.

    9. Click `Publish` in the top-right corner to update the preview and the live quiz.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The `Minimum number of votes` setting is available only if you choose not to recommend products when the results are empty. That option is in [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![Show random products in the Recommendation Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

---
By following this guide, you can easily filter your recommendations by minimum number of votes. 