# How to Only Recommend Products with X Votes or More

It is possible to limit the number of recommended products on the results page by only showing products that received X votes or more (a certain minimum number of votes). This allows you to filter the quiz recommendations and only show the real winners. 

To activate this setting in your quiz follow the instructions below.

=== "Shopify"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). 
    2. Make sure you understand how our [recommendations algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    2. Open the [Advanced Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how to only recommend product with min votes results page settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings). 
    5. Open the [Product/Slot Block settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how to only recommend product with min votes block settings.png](/images/how to only recommend product with min votes block settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.


    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how to only recommend product with min votes show random products.png)

=== "Shopify V2"


    !!! warning

        Version 2 of the RevenueHunt app is not yet available. It is currently in the beta testing phase. Learn more [here](https://docs.revenuehunt.com/customer-success/shopify-v2-beta/).

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). 
    2. Make sure you understand how our [recommendations algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page).
    2. Open the [Product Block Settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings_1).
    3. Scroll down to find the `Minimum number of votes` setting.
        ![how to only recommend product with min votes results page settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    4. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
    
        ![how to only recommend product with min votes block settings.png](/images/how to recommend products with 4 votes minimum.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    5. Update the preview/live quiz with these new settings by clicking `Save` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.


=== "WooCommerce"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). 
    2. Make sure you understand how our [recommendations algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    2. Open the [Advanced Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how to only recommend product with min votes results page settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings). 
    5. Open the [Product/Slot Block settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how to only recommend product with min votes block settings.png](/images/how to only recommend product with min votes block settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.


    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how to only recommend product with min votes show random products.png)

=== "Magento"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). 
    2. Make sure you understand how our [recommendations algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    2. Open the [Advanced Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how to only recommend product with min votes results page settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings). 
    5. Open the [Product/Slot Block settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how to only recommend product with min votes block settings.png](/images/how to only recommend product with min votes block settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.


    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how to only recommend product with min votes show random products.png)

=== "BigCommerce"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). 
    2. Make sure you understand how our [recommendations algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    2. Open the [Advanced Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how to only recommend product with min votes results page settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings). 
    5. Open the [Product/Slot Block settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how to only recommend product with min votes block settings.png](/images/how to only recommend product with min votes block settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.


    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how to only recommend product with min votes show random products.png)

=== "Standalone"

    1. Make sure that you have a **Product Block** or a **Product Slot Block** that recommends products on your [results page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page). 
    2. Make sure you understand how our [recommendations algorithm](https://docs.revenuehunt.com/how-to-guides/recommend-products/) works.

        ??? question "How do I get the right recommendations?"

            Our product recommendation algorithm works like a voting system:

            - Products are linked to each choice
            - When a customer picks a choice, all linked products receive one vote
            - After the customer takes the quiz, the results page will show the most voted products sorted by the number of votes
            - If no products have been linked or all the products have been excluded, the results page will appear empty
            - If there's a draw in the number of votes, the app will randomize the order of products.

    2. To activate the `Minimum nuber of votes` setting navigate to the [Results Page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    2. Open the [Advanced Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings).
    3. Scroll down to find the `Minimum number of votes` setting and activate it by clicking the toggle.
        ![how to only recommend product with min votes results page settings](/images/how to only recommend product with min votes results page settings.png)

    4. Once this option is active, the **Products Block** (or a **Slots Block**) on your results page will show extra setting in the [Block Settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings). 
    5. Open the [Product/Slot Block settings](https://docs.revenuehunt.com/reference/quiz-builder/#block-settings) and find the `Min. Number of Votes`. 
    6. Click on a dropdown and select a number. You can change the number of minumun votes to the number that fits your quiz setup. 
        ![how to only recommend product with min votes block settings.png](/images/how to only recommend product with min votes block settings.png)

        !!! example
        
            For example, if you have 4 questions in your quiz and you select 4 as a min. number of votes, only products that receive **4 votes or more** (aka match the answers in all questions) will be shown. If a product receives 3 votes, it will not be shown. If a product receives 5 votes it will be shown.

    7. Update the preview/live quiz with these new settings by clicking `Publish` in the top-right corner.

    From now on, only products that receive this minimum number of votes will show up as a recommendation on the results page.


    !!! warning

        The Minimum number of votes setting is only available if you choose not to recommend products when results are empty in the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) > Advanced > `Recommendation Settings`.
        ![how to only recommend product with min votes show random products](/images/how to only recommend product with min votes show random products.png)

---
By following this guide, you can easily filter your recommendations by minimum number of votes. 