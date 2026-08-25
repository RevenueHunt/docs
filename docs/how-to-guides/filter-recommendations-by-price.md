---
description: "Learn how to filter product recommendations by price in your RevenueHunt quiz results page using price-based collections."
icon: material/filter
---

# How to Filter Recommendations by Price


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/zfrq6Dh65S0?si=L-XkEXprRKs33ALk" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to filter the recommendations on your results page by price.

    It explains how to filter quiz recommendations by price in Shopify. It covers creating collections for each price range, and configuring the quiz to filter recommendations on them.

    1. **Adding a Price Filtering Question**: Click `Customize` to open the quiz, then open the [Questions](/reference/quiz-builder/questions/) section. Click `+ Add question` and add a multiple-choice question titled "What is your desired price range for your skincare routine?". Give each option a price range, then save.

        !!! example "Price Filtering Question"

            Provide three options:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_question_example.png)

    2. **Creating Price-Based Collections in Shopify**: Go to Shopify, then `Products > Collections`.

        - Click `Add collection` to create a new collection for products.
        - Name the collection (for example, Under 20 euros) and choose to create a **smart** collection with the condition.

            !!! example "Sample Smart Collection Conditions"

                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

                ![Smart collection condition on price](/images/how_to_filter_by_price_smart_collection_example.png)

        - Save the collection.
        - Repeat the process to create:
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each collection after setting the conditions.

    3. **Configuring the Quiz to Filter Recommendations**: Return to the RevenueHunt app and open your quiz. Locate the price question and expand it to configure options. Under [Choice settings](/reference/quiz-builder/questions/#choice-settings), find the `Upvotes` section and click `Upvote > Collections`. Upvote and exclude the collections for each price range. Click `Save` to save the changes.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the collection for products under 20 euros. Exclude collections for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the collection for products between 20 and 50 euros. Exclude collections for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the collection for products over 50 euros. Exclude collections for products under 20 euros and between 20 and 50 euros.

            ![Upvoting and excluding a collection per choice](https://loom.com/i/f2089b6648004d739a40997d7ebf81ec?workflows_screenshot=true)

    4. **Testing the Price Filter Functionality**: Preview the quiz. Pick the option for products over 50 euros and check that only those products appear. Repeat for the other ranges.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalogue import](/how-to-guides/sync-catalog/) in case of wrong recommendations.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    This article explains how to filter the recommendations on your results page by price.

    It explains how to filter quiz recommendations by price in Shopify. It covers creating collections for each price range, and configuring the quiz to filter recommendations on them.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a multiple-choice question titled "What is your desired price range for your skincare routine?". Give each option a price range, then save.

        !!! example "Price Filtering Question"

            Provide three options:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in Shopify**: Go to Shopify, then `Products > Collections`.

        - Click `Add collection` to create a new collection for products.
        - Name the collection (for example, Under 20 euros) and choose to create a **smart** collection with the condition.

            !!! example "Sample Smart Collection Conditions"

                For example, `Price` `is less than` `20 euros`.

                or `Price` `is greater than` `50 euros`.

                or `Price` `is between` `20 euros` and `50 euros`.

                ![Smart collection condition on price](/images/how_to_filter_by_price_smart_collection_example.png)

        - Save the collection.
        - Repeat the process to create:
            - A collection for products between 20 and 50 euros (Price `> 20` and Price `< 50`).
            - A collection for products over 50 euros (Price `> 50`).
        - Save each collection after setting the conditions.

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new collections. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the RevenueHunt app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the collections for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the collection for products under 20 euros. Exclude collections for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the collection for products between 20 and 50 euros. Exclude collections for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the collection for products over 50 euros. Exclude collections for products under 20 euros and between 20 and 50 euros.

            ![Upvoting and excluding a collection per choice](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz. Pick the option for products over 50 euros and check that only those products appear. Repeat for the other ranges.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.




=== "WooCommerce"


    This article explains how to filter the recommendations on your results page by price.

    It explains how to filter quiz recommendations by price in WooCommerce. It covers creating categories for each price range, and configuring the quiz to filter recommendations on them.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a multiple-choice question titled "What is your desired price range for your skincare routine?". Give each option a price range, then save.

        !!! example "Price Filtering Question"

            Provide three options:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Categories in WooCommerce**: In your WooCommerce admin, go to **Products → Categories**. Create one product category per price range.

        - Name the category (for example, **Under 20 euros**).
        - Save the category.
        - Edit your products and assign them to the corresponding price category:
            - Products priced under 20 euros → assign to **Under 20 euros**.
            - Products priced between 20 and 50 euros → assign to **20–50 euros**.
            - Products priced over 50 euros → assign to **Over 50 euros**.

        !!! example "Sample Price-Based Categories"

            - Category: **Under 20 euros** → all products with a price `< 20`.
            - Category: **20–50 euros** → all products with a price between `20` and `50`.
            - Category: **Over 50 euros** → all products with a price `> 50`.

        - Repeat the process until every product you want to recommend is assigned to the correct price category.


    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the RevenueHunt app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![Upvoting and excluding a collection per choice](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz. Pick the option for products over 50 euros and check that only those products appear. Repeat for the other ranges.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.


=== "Magento"


    This article explains how to filter the recommendations on your results page by price.

    It explains how to filter quiz recommendations by price in Magento. It covers creating categories for each price range, and configuring the quiz to filter recommendations on them.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a multiple-choice question titled "What is your desired price range for your skincare routine?". Give each option a price range, then save.

        !!! example "Price Filtering Question"

            Provide three options:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Categories in Magento**: In your Magento admin, go to **Catalog → Categories**. Create one product category per price range.

        - Click **Add Subcategory** under the relevant parent category (for example, under your main “Skincare” category).
        - Name the category (for example, **Under 20 euros**) and save it.
        - In the **Products in Category** section, assign products to the corresponding price category:
            - Products priced under 20 euros → assign to **Under 20 euros**.
            - Products priced between 20 and 50 euros → assign to **20–50 euros**.
            - Products priced over 50 euros → assign to **Over 50 euros**.
        - Save the category.

        !!! example "Sample Price-Based Categories"

            - Category: **Under 20 euros** → all products with a price `< 20`.
            - Category: **20–50 euros** → all products with a price between `20` and `50`.
            - Category: **Over 50 euros** → all products with a price `> 50`.

        - Repeat this process until all products you want to recommend through the quiz are assigned to the correct price category.

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the RevenueHunt app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![Upvoting and excluding a collection per choice](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz. Pick the option for products over 50 euros and check that only those products appear. Repeat for the other ranges.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.



=== "BigCommerce"

    This article explains how to filter the recommendations on your results page by price.

    It explains how to filter quiz recommendations by price in BigCommerce. It covers creating categories for each price range, and configuring the quiz to filter recommendations on them.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a multiple-choice question titled "What is your desired price range for your skincare routine?". Give each option a price range, then save.

        !!! example "Price Filtering Question"

            Provide three options:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Categories in BigCommerce**: In your BigCommerce control panel, go to **Products → Product Categories**. Create one product category per price range.

        - Click **Add a Category**.
        - Name the category (for example, **Under 20 euros**) and save it.
        - Edit your products and assign them to the corresponding price category:
            - Products priced under 20 euros → assign to **Under 20 euros**.
            - Products priced between 20 and 50 euros → assign to **20–50 euros**.
            - Products priced over 50 euros → assign to **Over 50 euros**.
        - Save the changes.

        !!! example "Sample Price-Based Categories"

            - Category: **Under 20 euros** → all products with a price `< 20`.
            - Category: **20–50 euros** → all products with a price between `20` and `50`.
            - Category: **Over 50 euros** → all products with a price `> 50`.

        - Repeat this process until all products you want to recommend through the quiz are assigned to the correct price category.


    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the RevenueHunt app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![Upvoting and excluding a collection per choice](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz. Pick the option for products over 50 euros and check that only those products appear. Repeat for the other ranges.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.



=== "Standalone"


    This article explains how to filter the recommendations on your results page by price.

    It explains how to filter quiz recommendations by price in the Standalone version. It covers creating collections for each price range, and configuring the quiz to filter recommendations on them.

    1. **Adding a Price Filtering Question**: Open the [Quiz Builder](/reference/quiz-builder/). Click `+` to add a multiple-choice question titled "What is your desired price range for your skincare routine?". Give each option a price range, then save.

        !!! example "Price Filtering Question"

            Provide three options:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![filter by price example](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Creating Price-Based Collections in Standalone**: Go to Standalone app, [Success Checklist](/reference/dashboard/#success-checklist) and create collections for each price range.


        !!! tip "How do I add products to Standalone RevenueHunt App?"

            Follow this guide to learn how to add products and collections to the Standalone version of the RevenueHunt app: [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/)

    3. **Catalog Sync**: Run the [catalog sync](/how-to-guides/sync-catalog/) from the success checklist to import new categories. After syncing, refresh the quiz page.

    4. **Configuring the Quiz to Filter Recommendations**: Return to the RevenueHunt app and open your quiz. Open the [Link Collections](/reference/quiz-builder/link-collections/) section. Find the `Upvotes` section and upvote and exclude the categories for each price range.

        !!! example "Configuring the Quiz to Filter Recommendations"

            - For the 'Under 20 euros' choice: Upvote the category for products under 20 euros. Exclude categories for products between 20 and 50 euros and over 50 euros.
            - For the '20 to 50 euros' choice: Upvote the category for products between 20 and 50 euros. Exclude categories for products under 20 euros and over 50 euros.
            - For the 'Over 50 euros' choice: Upvote the category for products over 50 euros. Exclude categories for products under 20 euros and between 20 and 50 euros.

            ![Upvoting and excluding a collection per choice](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    4. **Testing the Price Filter Functionality**: Preview the quiz. Pick the option for products over 50 euros and check that only those products appear. Repeat for the other ranges.

        !!! tip "Troubleshooting"

            Check the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool in case of wrong recommendations.

            It may also be necessary to run a quick [catalog sync](/how-to-guides/sync-catalog/) in case of wrong recommendations.



---

This article explains how to filter recommendations by price in your quiz results page.
