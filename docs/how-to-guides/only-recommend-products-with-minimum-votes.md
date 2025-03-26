# How to Only Recommend Products with X Votes or More

It is possible to limit the number of recommended products on the results page by only showing products that received X votes or more (a certain minimum number of votes). This allows you to filter the quiz recommendations and only show the real winners. 

To activate this setting in your quiz follow the instructions below.

=== "Shopify"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](/reference/quiz-builder/results-page/). 
    2. Make sure you understand how our [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](/reference/quiz-builder/questions/#block-settings). 
    5. Open the [Product/Slot Block settings](/reference/quiz-builder/questions/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how_to_only_recommend_product_with_min_votes_block_settings.png](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "Shopify V2"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](/reference/quiz-builder/results-page/). 
    2. Make sure you understand how our [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page](/reference/quiz-builder/results-page/).
    2. Open the [Product Block Settings](/reference/quiz-builder/results-page/#block-settings).
    3. Scroll down to find the `Minimum number of votes` setting.
        ![how to only recommend product with min votes results page settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    4. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
    
        ![how_to_only_recommend_product_with_min_votes_block_settings.png](/images/how_to_recommend_products_with_4_votes_minimum.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    5. Update the preview/live quiz with these new settings by clicking `Save` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

=== "WooCommerce"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](/reference/quiz-builder/results-page/). 
    2. Make sure you understand how our [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](/reference/quiz-builder/questions/#block-settings). 
    5. Open the [Product/Slot Block settings](/reference/quiz-builder/questions/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how_to_only_recommend_product_with_min_votes_block_settings.png](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "Magento"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](/reference/quiz-builder/results-page/). 
    2. Make sure you understand how our [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](/reference/quiz-builder/questions/#block-settings). 
    5. Open the [Product/Slot Block settings](/reference/quiz-builder/questions/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how_to_only_recommend_product_with_min_votes_block_settings.png](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "BigCommerce"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](/reference/quiz-builder/results-page/). 
    2. Make sure you understand how our [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](/reference/quiz-builder/questions/#block-settings). 
    5. Open the [Product/Slot Block settings](/reference/quiz-builder/questions/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how_to_only_recommend_product_with_min_votes_block_settings.png](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

=== "Standalone"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](/reference/quiz-builder/results-page/). 
    2. Make sure you understand how our [recommendations algorithm](/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](/reference/quiz-builder/results-page/).
    2. Open the [Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](/reference/quiz-builder/questions/#block-settings). 
    5. Open the [Product/Slot Block settings](/reference/quiz-builder/questions/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how_to_only_recommend_product_with_min_votes_block_settings.png](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.

    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](/reference/quiz-builder/results-page/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

---
By following this guide, you can easily filter your recommendations by minimum number of votes. 