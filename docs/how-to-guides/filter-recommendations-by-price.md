---
description: "Learn how to filter product recommendations by price in your RevenueHunt quiz results page using price-based collections."
icon: material/filter
---

# How to Filter Recommendations by Price

A quiz can keep its recommendations inside the price range the customer picked.

The method is the same everywhere. Group your products by price in your store, ask the customer which range they want, then upvote that group and exclude the others.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/zfrq6Dh65S0?si=L-XkEXprRKs33ALk" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Click `Customize`, open [Questions](/reference/quiz-builder/questions/), and add a multiple-choice question about price.** For example, "What is your desired price range?".

        !!! example "The question"

            Three choices cover most catalogs:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_question_example.png)

    2. **In your Shopify admin, go to `Products > Collections` and click `Add collection`.**

    3. **Name it after the range, and make it a smart collection with a price condition.**

        !!! example "The condition on each collection"

            `Price` `is less than` `20 euros`

            `Price` `is between` `20 euros` and `50 euros`

            `Price` `is greater than` `50 euros`

            ![Smart collection condition on price](/images/how_to_filter_by_price_smart_collection_example.png)

    4. **Repeat for each range, then save every collection.**

    5. **Back in the quiz, open the price question and expand a choice.**

    6. **Under [Choice settings](/reference/quiz-builder/questions/#choice-settings), open `Upvotes` and click `Upvote > Collections`.**

    7. **Upvote the collection for that choice, and exclude the other two.**

        !!! example "One group upvoted, the rest excluded"

            - **Under 20 euros** upvotes the under-20 collection, and excludes the other two.
            - **20 to 50 euros** upvotes the 20-to-50 collection, and excludes the other two.
            - **Over 50 euros** upvotes the over-50 collection, and excludes the other two.

            ![Upvoting one group and excluding the others](https://loom.com/i/f2089b6648004d739a40997d7ebf81ec?workflows_screenshot=true)

    8. **Click the top-right `Save` button.**

    9. **Preview the quiz and pick each range in turn.** Only the products in that range should come back.

        !!! tip "The wrong products come back"

            Open [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) to see which products were upvoted and why.

            A [catalog sync](/how-to-guides/sync-catalog/) also helps, in case the new groups have not reached the quiz yet.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/66ade08895f5478d80b2f686576642ad?sid=da3831fd-a490-4ba8-aab6-cb05bd873001" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a multiple-choice question about price.** For example, "What is your desired price range?".

        !!! example "The question"

            Three choices cover most catalogs:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **In your Shopify admin, go to `Products > Collections` and click `Add collection`.**

    3. **Name it after the range, and make it a smart collection with a price condition.**

        !!! example "The condition on each collection"

            `Price` `is less than` `20 euros`

            `Price` `is between` `20 euros` and `50 euros`

            `Price` `is greater than` `50 euros`

            ![Smart collection condition on price](/images/how_to_filter_by_price_smart_collection_example.png)

    4. **Repeat for each range, then save every collection.**

    5. **Run a [catalog sync](/how-to-guides/sync-catalog/) from the success checklist**, so the new collections reach the quiz.

    6. **Open the [Link Collections](/reference/quiz-builder/link-collections/) section, and for each choice upvote its own collection while excluding the others.**

        !!! example "One group upvoted, the rest excluded"

            - **Under 20 euros** upvotes the under-20 collection, and excludes the other two.
            - **20 to 50 euros** upvotes the 20-to-50 collection, and excludes the other two.
            - **Over 50 euros** upvotes the over-50 collection, and excludes the other two.

            ![Upvoting one group and excluding the others](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    7. **Click the top-right `Publish` button.**

    8. **Preview the quiz and pick each range in turn.** Only the products in that range should come back.

        !!! tip "The wrong products come back"

            Open [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) to see which products were upvoted and why.

            A [catalog sync](/how-to-guides/sync-catalog/) also helps, in case the new groups have not reached the quiz yet.

=== "WooCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a multiple-choice question about price.** For example, "What is your desired price range?".

        !!! example "The question"

            Three choices cover most catalogs:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **In your store admin, go to `Products > Categories`.**

    3. **Create one category per price range, with `Add new category`.**

    4. **Assign your products to the matching category.**

        - Products under 20 euros go in the under-20 category.
        - Products between 20 and 50 euros go in the 20-to-50 category.
        - Products over 50 euros go in the over-50 category.

    5. **Run a [catalog sync](/how-to-guides/sync-catalog/) from the success checklist**, so the new categories reach the quiz.

    6. **Open the [Link Categories](/reference/quiz-builder/link-collections/) section, and for each choice upvote its own category while excluding the others.**

        !!! example "One group upvoted, the rest excluded"

            - **Under 20 euros** upvotes the under-20 category, and excludes the other two.
            - **20 to 50 euros** upvotes the 20-to-50 category, and excludes the other two.
            - **Over 50 euros** upvotes the over-50 category, and excludes the other two.

            ![Upvoting one group and excluding the others](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    7. **Click the top-right `Publish` button.**

    8. **Preview the quiz and pick each range in turn.** Only the products in that range should come back.

        !!! tip "The wrong products come back"

            Open [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) to see which products were upvoted and why.

            A [catalog sync](/how-to-guides/sync-catalog/) also helps, in case the new groups have not reached the quiz yet.

=== "Magento"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a multiple-choice question about price.** For example, "What is your desired price range?".

        !!! example "The question"

            Three choices cover most catalogs:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **In your store admin, go to `Catalog > Categories`.**

    3. **Create one category per price range, with `Add Subcategory` under your main category.**

    4. **Assign your products to the matching category.**

        - Products under 20 euros go in the under-20 category.
        - Products between 20 and 50 euros go in the 20-to-50 category.
        - Products over 50 euros go in the over-50 category.

        Assign them in the `Products in Category` section, then save the category.

    5. **Run a [catalog sync](/how-to-guides/sync-catalog/) from the success checklist**, so the new categories reach the quiz.

    6. **Open the [Link Categories](/reference/quiz-builder/link-collections/) section, and for each choice upvote its own category while excluding the others.**

        !!! example "One group upvoted, the rest excluded"

            - **Under 20 euros** upvotes the under-20 category, and excludes the other two.
            - **20 to 50 euros** upvotes the 20-to-50 category, and excludes the other two.
            - **Over 50 euros** upvotes the over-50 category, and excludes the other two.

            ![Upvoting one group and excluding the others](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    7. **Click the top-right `Publish` button.**

    8. **Preview the quiz and pick each range in turn.** Only the products in that range should come back.

        !!! tip "The wrong products come back"

            Open [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) to see which products were upvoted and why.

            A [catalog sync](/how-to-guides/sync-catalog/) also helps, in case the new groups have not reached the quiz yet.

=== "BigCommerce"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a multiple-choice question about price.** For example, "What is your desired price range?".

        !!! example "The question"

            Three choices cover most catalogs:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **In your store admin, go to `Products > Product Categories`.**

    3. **Create one category per price range, with `Add a Category`.**

    4. **Assign your products to the matching category.**

        - Products under 20 euros go in the under-20 category.
        - Products between 20 and 50 euros go in the 20-to-50 category.
        - Products over 50 euros go in the over-50 category.

    5. **Run a [catalog sync](/how-to-guides/sync-catalog/) from the success checklist**, so the new categories reach the quiz.

    6. **Open the [Link Categories](/reference/quiz-builder/link-collections/) section, and for each choice upvote its own category while excluding the others.**

        !!! example "One group upvoted, the rest excluded"

            - **Under 20 euros** upvotes the under-20 category, and excludes the other two.
            - **20 to 50 euros** upvotes the 20-to-50 category, and excludes the other two.
            - **Over 50 euros** upvotes the over-50 category, and excludes the other two.

            ![Upvoting one group and excluding the others](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    7. **Click the top-right `Publish` button.**

    8. **Preview the quiz and pick each range in turn.** Only the products in that range should come back.

        !!! tip "The wrong products come back"

            Open [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) to see which products were upvoted and why.

            A [catalog sync](/how-to-guides/sync-catalog/) also helps, in case the new groups have not reached the quiz yet.

=== "Standalone"

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a multiple-choice question about price.** For example, "What is your desired price range?".

        !!! example "The question"

            Three choices cover most catalogs:

            - Under 20 euros
            - Between 20 and 50 euros
            - Over 50 euros

            ![Price filtering question with three ranges](/images/how_to_filter_by_price_filter_legacy_question_example.png)

    2. **Open the [Success Checklist](/reference/dashboard/#success-checklist) and create one collection per price range.**

        !!! tip "Filling the catalogue"

            See [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/).

    3. **Put each product in the collection that matches its price.**

        - Products under 20 euros go in the under-20 collection.
        - Products between 20 and 50 euros go in the 20-to-50 collection.
        - Products over 50 euros go in the over-50 collection.

    4. **Open the [Link Categories](/reference/quiz-builder/link-collections/) section, and for each choice upvote its own collection while excluding the others.**

        !!! example "One group upvoted, the rest excluded"

            - **Under 20 euros** upvotes the under-20 collection, and excludes the other two.
            - **20 to 50 euros** upvotes the 20-to-50 collection, and excludes the other two.
            - **Over 50 euros** upvotes the over-50 collection, and excludes the other two.

            ![Upvoting one group and excluding the others](/images/how_to_filter_by_price__legacy_filter_question_linkedcollections.png)

    5. **Click the top-right `Publish` button.**

    6. **Preview the quiz and pick each range in turn.** Only the products in that range should come back.

        !!! tip "The wrong products come back"

            Open [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) to see which products were upvoted and why.

            A [catalog sync](/how-to-guides/sync-catalog/) also helps, in case the new groups have not reached the quiz yet.

---

This article explains how to keep quiz recommendations inside the price range a customer picked.