---
icon: material/filter-list
---

# How to Filter Recommendations by Price


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This guide explains how to filter recommendations by price in your quiz results page. 
    
    It explains how to implement a price filtering feature in a quiz using Shopify and the Revenue Hunt Quizzes app. It covers the steps to create collections based on price ranges and how to configure the quiz to filter product recommendations accordingly.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a new multiple choice question titled "What's your desired price range for your skincare routine?". Provide a price range for each option. Save the changes to ensure the question is added.

        !!! example "Price Filtering Question"

            Provide three options: 

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in Shopify** : Go to Shopify, then `Products > Collections`.

        - Click `Add collection` to create a new collection for products.
        - Name the collection (for example, Under 20 euros) and choose to create a **smart** collection with the condition. 
        
            !!! example "Sample Smart Collection Conditions"
            
                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

                ![filter by price example](/images/how_to_filter_by_price_smart_collection_example.png)

        - Save the collection.
        - Repeat the process to create: 
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each collection after setting the conditions.

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new collections. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the Revenue Hunt Quizzes app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the collections for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the collection for products under 20 euros. Exclude collections for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the collection for products between 20 and 50 euros. Exclude collections for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the collection for products over 50 euros. Exclude collections for products under 20 euros and between 20 and 50 euros.

            ![filter by collection example](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz to test the filtering functionality. Select the option for products over 50 euros to verify that only those products are displayed. Repeat the test for the other price ranges to ensure accurate filtering. Confirm that the recommendations reflect the selected price range correctly.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.




=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/0375115097c94e8fb6cdf36824ce0042?sid=9bec559f-5103-4201-b05d-a0c6e3d3a37f" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This guide explains how to filter recommendations by price in your quiz results page. 
    
    It explains how to implement a price filtering feature in a quiz using Shopify and the Revenue Hunt Quizzes app. It covers the steps to create collections based on price ranges and how to configure the quiz to filter product recommendations accordingly.

    1. **Adding a Price Filtering Question**: Open the quiz by clicking `Customize` and  open the [Questions](/reference/quiz-builder/questions/) section.  Click `+ Add question` to add a new multiple choice question titled "What's your desired price range for your skincare routine?". Provide a price range for each option. Save the changes to ensure the question is added.

        !!! example "Price Filtering Question"

            Provide three options: 

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_question_example.png)

    2. **Creating Price-Based Collections in Shopify** : Go to Shopify, then `Products > Collections`.

        - Click `Add collection` to create a new collection for products.
        - Name the collection (for example, Under 20 euros) and choose to create a **smart** collection with the condition. 
        
            !!! example "Sample Smart Collection Conditions"
            
                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

                ![filter by price example](/images/how_to_filter_by_price_smart_collection_example.png)

        - Save the collection.
        - Repeat the process to create: 
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each collection after setting the conditions.

    3. **Configuring the Quiz to Filter Recommendations**: Return to the Revenue Hunt Quizzes app and open your quiz. Locate the price question and expand it to configure options. Under [Choice settings](/reference/quiz-builder/questions/#choice-settings), find the `Upvotes` section and click `Upvote > Collections`. Upvote and exclude the collections for each price range. Click `Save` to save the changes.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the collection for products under 20 euros. Exclude collections for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the collection for products between 20 and 50 euros. Exclude collections for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the collection for products over 50 euros. Exclude collections for products under 20 euros and between 20 and 50 euros.

            ![filter by collection example](https://loom.com/i/f2089b6648004d739a40997d7ebf81ec?workflows_screenshot=true)

    4. **Testing the Price Filter Functionality**: Preview the quiz to test the filtering functionality. Select the option for products over 50 euros to verify that only those products are displayed. Repeat the test for the other price ranges to ensure accurate filtering. Confirm that the recommendations reflect the selected price range correctly.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.

=== "WooCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This guide explains how to filter recommendations by price in your quiz results page. 
    
    It explains how to implement a price filtering feature in a quiz using WooCommerce and the Revenue Hunt Quizzes app. It covers the steps to create categories based on price ranges and how to configure the quiz to filter product recommendations accordingly.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a new multiple choice question titled "What's your desired price range for your skincare routine?". Provide a price range for each option. Save the changes to ensure the question is added.

        !!! example "Price Filtering Question"

            Provide three options: 

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in WooCommerce** : Go to WooCommerce and create categories for each price range.

        - Name the category (for example, Under 20 euros) and choose to create a **smart** category with the condition. 
        
            !!! example "Sample Smart Collection Conditions"
            
                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

        - Save the category.
        - Repeat the process to create: 
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each category after setting the conditions.

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the Revenue Hunt Quizzes app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![filter by collection example](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz to test the filtering functionality. Select the option for products over 50 euros to verify that only those products are displayed. Repeat the test for the other price ranges to ensure accurate filtering. Confirm that the recommendations reflect the selected price range correctly.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.


=== "Magento"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This guide explains how to filter recommendations by price in your quiz results page. 
    
    It explains how to implement a price filtering feature in a quiz using Magento and the Revenue Hunt Quizzes app. It covers the steps to create categories based on price ranges and how to configure the quiz to filter product recommendations accordingly.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a new multiple choice question titled "What's your desired price range for your skincare routine?". Provide a price range for each option. Save the changes to ensure the question is added.

        !!! example "Price Filtering Question"

            Provide three options: 

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in Magento** : Go to Magento and create categories for each price range.

        - Name the category (for example, Under 20 euros) and choose to create a **smart** category with the condition. 
        
            !!! example "Sample Smart Collection Conditions"
            
                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

        - Save the category.
        - Repeat the process to create: 
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each category after setting the conditions.

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the Revenue Hunt Quizzes app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![filter by collection example](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz to test the filtering functionality. Select the option for products over 50 euros to verify that only those products are displayed. Repeat the test for the other price ranges to ensure accurate filtering. Confirm that the recommendations reflect the selected price range correctly.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.



=== "BigCommerce"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This guide explains how to filter recommendations by price in your quiz results page. 
    
    It explains how to implement a price filtering feature in a quiz using BigCommerce and the Revenue Hunt Quizzes app. It covers the steps to create categories based on price ranges and how to configure the quiz to filter product recommendations accordingly.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a new multiple choice question titled "What's your desired price range for your skincare routine?". Provide a price range for each option. Save the changes to ensure the question is added.

        !!! example "Price Filtering Question"

            Provide three options: 

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in BigCommerce** : Go to BigCommerce and create categories for each price range.

        - Name the category (for example, Under 20 euros) and choose to create a **smart** category with the condition. 
        
            !!! example "Sample Smart Collection Conditions"
            
                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

        - Save the category.
        - Repeat the process to create: 
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each category after setting the conditions.

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the Revenue Hunt Quizzes app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![filter by collection example](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz to test the filtering functionality. Select the option for products over 50 euros to verify that only those products are displayed. Repeat the test for the other price ranges to ensure accurate filtering. Confirm that the recommendations reflect the selected price range correctly.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.



=== "Standalone"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This guide explains how to filter recommendations by price in your quiz results page. 
    
    It explains how to implement a price filtering feature in a quiz using WooCommerce and the Revenue Hunt Quizzes app. It covers the steps to create categories based on price ranges and how to configure the quiz to filter product recommendations accordingly.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a new multiple choice question titled "What's your desired price range for your skincare routine?". Provide a price range for each option. Save the changes to ensure the question is added.

        !!! example "Price Filtering Question"

            Provide three options: 

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in Standalone** : Go to Standalone app, [Success Checklist](/reference/dashboard/#success-checklist) and create collections for each price range. 
    
        
        !!! tip "How do I add products to Standalone RevenueHunt App?"
        
            Follow this guide to learn how to add products and collections to the Standalone version of the RevenueHunt app: [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/)

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the Revenue Hunt Quizzes app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![filter by collection example](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz to test the filtering functionality. Select the option for products over 50 euros to verify that only those products are displayed. Repeat the test for the other price ranges to ensure accurate filtering. Confirm that the recommendations reflect the selected price range correctly.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.



---

This article explains how to filter recommendations by price in your quiz results page. 
