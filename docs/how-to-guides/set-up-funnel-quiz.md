---
description: "Complete guide to setting up a RevenueHunt funnel quiz with dynamic product upvoting system."
icon: material/filter-variant
---

# How to Set Up Funnel Quiz

A Funnel Quiz helps your customers find the best product by assigning "upvotes" to products as they answer questions. The quiz counts these upvotes and recommends the most relevant products at the end.

!!! info "Use this method for:"

    - Helping customers narrow down a large product catalog
    - Most quizzes, especially product finders
    - Your first product recommendation quiz
    - Quizzes without complex branching


## ✍🏻 Upvoting system

An **upvote** is the signal a choice gives a product.

1. You link products, variants or collections to each choice.
2. A customer picks that choice, and every linked item gets one upvote.
3. The Results page lists them, highest upvote count first.

An empty Results page means either nothing was linked to the choices the customer made, or [exclusions](#exclusion) removed everything.

Two settings refine the list:

- [A minimum upvote count](/how-to-guides/only-recommend-products-with-minimum-votes/) hides products that did not get enough upvotes.
- [Exclusions](#exclusion) keep a product out entirely, even when another choice upvoted it.

**When two products have the same number of upvotes**

=== "Shopify"

    By default the app randomizes their order.

    To use your own order instead, set `Catalog mode` to `Preserve collection order` in [Settings > Catalog](/reference/app-settings/#catalog). Products then appear in the order you arranged them in your Shopify collections.

    Click `Import now` after you change the setting. The new order applies only after a fresh import.

=== "Shopify (Legacy)"

    The app randomizes their order.

=== "WooCommerce"

    The app randomizes their order.

=== "Magento"

    The app randomizes their order.

=== "BigCommerce"

    The app randomizes their order.

=== "Standalone"

    The app randomizes their order.


**Understand Inclusion and Exclusion**

### Upvote inclusion


=== "Shopify"

    To link products or collections to choices, open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) and go to the `Upvotes` section.

    ![how to recommend products upvote](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    Click `+ Add upvote type` to add a new upvote type.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotemain](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotemain.png)

    How the upvotes work for each upvoted item:

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown.png)

    - **Main Products / All variants of the same product at once**: every variant of a product is upvoted when its linked choice is selected.
    - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Collections**: Every product within a linked collection receives an upvote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives an upvote when their linked choice is selected.
    - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives an upvote when their linked choice is selected.
    - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives an upvote when their linked choice is selected.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall.png)

    !!! tip

        You can also recommend pure text results by setting up different sections on the results page and controlling visibility of each section with Display logic. This option is not dependent on the upvoting system but rather on custom scoring system or conditional logic.




=== "Shopify (Legacy)"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the upvotes work for each included linked item:

    - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Collections**: Every product within a linked collection receives an upvote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives an upvote when their linked choice is selected.
    - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives an upvote when their linked choice is selected.
    - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives an upvote when their linked choice is selected.
    - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.

=== "WooCommerce"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.


    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the upvotes work for each included linked item:

    - **Simple Products** - Individual products receive an upvote when their linked choice is selected.
    - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Product Bundles**: A bundle is treated as an individual product. Every bundle receives one upvote when their linked choice is selected.
    - **Affiliate Products** - Individual products receive an upvote when their linked choice is selected. On the results page the customer is redirected to the affiliate link (not the store link).
    - **Categories**: Every product within a linked category receives an upvote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives an upvote when their linked choice is selected.
    - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.

=== "Magento"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.


    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the upvotes work for each included linked item:

    - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Categories**: Every product within a linked category receives an upvote when their linked choice is selected.

=== "BigCommerce"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.


    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the upvotes work for each included linked item:

    - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Categories**: Every product within a linked category receives an upvote when their linked choice is selected.
    - **Tags**: Every product within a linked tag receives an upvote when their linked choice is selected.

    !!! tip

        You can also use custom fields as tags within the app by following [these instructions](//how-to-guides/use-custom-fields-as-tags/)

=== "Standalone"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.


    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    How the upvotes work for each included linked item:

    - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Collections**: Every product within a linked collection receives an upvote when their linked choice is selected.

!!! warning

    A variant can be upvoted twice by one choice: once through the Upvote tab directly, and again through a collection that contains it. That choice then gives it **2 upvotes**.

### Exclusion

=== "Shopify"

    To exclude products or collections from choices, open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) and go to the `Exclude` section.

    ![how to recommend products exclusion](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    Click `+ Add exclude type` to add a new exclude type.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain.png)

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown.png)

    Once you select a product, collection or other item, it joins the excluded list. It never appears as a recommendation, even if another choice upvotes it.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall.png)


=== "Shopify (Legacy)"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

=== "WooCommerce"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

=== "Magento"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

=== "BigCommerce"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

=== "Standalone"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)


    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

!!! warning

    Once a choice excludes a product, it **never shows** as a recommendation, even if another choice upvotes it.

!!! example

    If you want the recommended products to be filtered out by question, you can do that using the `exclude` feature. For example, if you want to show only recommendations within a certain price range, you can use the exclude collections feature as in the example below.
    ![how to recommend products exclusion example](/images/how_to_recommend_products_exclusion_example.png)
    A customer who says they do not want to spend more than $100 then sees no products above that price.

## Funnel quiz

The upvoting system recommends products by counting how many times each one is "upvoted for" through customer quiz choices. Each quiz choice can be linked to specific product variants, and every time a customer selects a choice, the associated products receive one upvote.

This method uses the [upvoting system](#upvoting-system).

At the end of the quiz, the results page lists the product variants with the most upvotes first. An empty results page means no products were linked, or logic excluded them all. You can also cap how many products appear, or require a minimum number of upvotes.

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width=500}


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/j-Ecp4NeTfQ?si=gTp7uWal22QfKFVC" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The results page can show **product variants**, **main products** and **collections**.

    Follow these steps to set up your product recommendations:

    1. **Link Products to Choices**: Navigate to the [Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, upvote relevant products.

        Products or collections added in the `upvotes` field of the [Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

        ![how to recommend products inclusion](/images/how_to_shopifyv2_setuprecommendations_linkcollections.png)

        !!! tip

            Think carefully about which products are upvoted in each choice. You can create special **hidden collections** for each choice in Shopify and add only relevant products to them. Then you can link collections to choices rather than individual products for easier management.

        ??? question "How the upvotes work for each included linked item?"

            You can upvote product variants, collections, tags, variant collections, vendor collections or all variants of the same product at once.

            - **Product variants**: an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
            - **Collections**: Every product within a linked collection receives an upvote when their linked choice is selected.
            - **Tags**: Every product within a linked tag receives an upvote when their linked choice is selected.
            - **Variant collections**: Created automatically by the app, every product within a linked variant collection receives an upvote when their linked choice is selected.
            - **Vendor collections**: Created automatically by the app, every product within a linked vendor collection receives an upvote when their linked choice is selected.
            - **All variants of the same product at once**: All variants of a product get upvoted at once when their linked choice is selected. Note: A special setting called `Use top-level product` in [Quiz settings](/reference/quiz-builder/quiz-settings/) needs to be active for this option to appear in the Link Products section.

        ??? warning "How does product **exclusion** work in the upvoting system?"

            Use the `exclude` field of the [Exclude](/reference/quiz-builder/link-products/) tab to remove certain products or collections from the recommendations, useful for items with allergens or sensitive ingredients.

            ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

            !!! warning

                Once a choice excludes a product, it **never shows** as a recommendation, even if another choice upvotes it.

            !!! example

                If you want the recommended products to be filtered out by question, you can do that using the `exclude` feature. For example, if you want to show only recommendations within a certain price range, you can use the exclude collections feature as in the example below.
                ![how to recommend products exclusion example](/images/how_to_recommend_products_exclusion_example.png)
                A customer who says they do not want to spend more than $100 then sees no products above that price.

    2. **Edit the Results page**: In the [Results page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen.

        - You can add a heading, content block, image block, HTML block or a Product block.

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage.png)

        !!! tip

            Check [How to Edit the Results page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product block**: the `Products Block` lists products, variants or collections on the Results page.

        - Click `+ Add Block` and select [`Products Block`](/reference/quiz-builder/results-page/#product-product-variants-collections) to add it to your results page.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes_products](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes_products.png)

        - In Product block settings you can choose the `Recommendation system` to be `Upvotes`. The **Product block** then displays the products sorted by the number of upvotes, the most upvoted first.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

        - Every Product block has a default `Slot` holding the recommended products. [Slot settings](/reference/quiz-builder/questions/#block-settings) set **how many products to show**.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slot](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slot.png)

        - Then the results page will show the products like this, sorted by the number of upvotes:

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        !!! note

            A Product block can also show products in clear steps, such as a **skincare routine**. Give a block a **Segment Filter** and it recommends the most-upvoted product from the collection linked to it. See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).


    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section shows why a product was recommended, or why it was missing.

        ![how to recommend products built for shopify revenuehunt app troubleshoot results](/images/manual_shopifyV2_quizbuilder_responses_sample1_checkproduct.png)

        !!! tip
            Check [How to Troubleshoot Quiz results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding how inclusion and exclusion work, you can make the recommendations precise.


=== "Shopify (Legacy)"

    The results page can show **product variants**, **main products** and **[Recharge subscription products](/how-to-guides/recommend-subscription-products/)**.

    The quiz **cannot recommend collections** of products. You can, however, [recommend products from one collection only](/how-to-guides/recommend-skincare-routine-slots/).

    Follow these steps to set up your product recommendations:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can upvote product variants, collections, tags, variant collections, vendor collections, or all variants of a product at once.

    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: a `Product Block` lists the products on the Results Page, and a `Product Slot Block` divides them into slots. Start with a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show products in clear steps, such as a skincare routine. Each Slot recommends the most-upvoted product from the collection linked to it. *See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding how inclusion and exclusion work, you can make the recommendations precise.

=== "WooCommerce"

    The results page can show **simple products**, **variable products**, **grouped products**, **external/affiliate products** and **[WooCommerce subscription products](/how-to-guides/recommend-subscription-products/)**.

    The quiz **cannot recommend categories** of products. You can, however, [recommend products from one category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    !!! warning

        The app syncs only one type of variant per variable product. If a product varies by both size and color, the app syncs the size variants only.

    Follow these steps to set up your product recommendations:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can upvote product variants, collections, tags, variant collections, vendor collections, or all variants of a product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: a `Product Block` lists the products on the Results Page, and a `Product Slot Block` divides them into slots. Start with a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show products in clear steps, such as a skincare routine. Each Slot recommends the most-upvoted product from the collection linked to it. *See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding how inclusion and exclusion work, you can make the recommendations precise.

=== "Magento"

    The results page can show **product variants** and **main products**.

    The quiz **cannot recommend categories** of products. You can, however, [recommend products from one category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    Follow these steps to set up your product recommendations:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can upvote product variants, collections, tags, variant collections, vendor collections, or all variants of a product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: a `Product Block` lists the products on the Results Page, and a `Product Slot Block` divides them into slots. Start with a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show products in clear steps, such as a skincare routine. Each Slot recommends the most-upvoted product from the collection linked to it. *See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding how inclusion and exclusion work, you can make the recommendations precise.

=== "BigCommerce"

    The results page can show **product variants** and **main products**.

    The quiz **cannot recommend categories** of products. You can, however, [recommend products from one category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    Follow these steps to set up your product recommendations:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can upvote product variants, collections, tags, variant collections, vendor collections, or all variants of a product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: a `Product Block` lists the products on the Results Page, and a `Product Slot Block` divides them into slots. Start with a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show products in clear steps, such as a skincare routine. Each Slot recommends the most-upvoted product from the collection linked to it. *See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding how inclusion and exclusion work, you can make the recommendations precise.

=== "Standalone"

    The results page can show **product variants** and **main products**.

    The quiz **cannot recommend collections** of products. You can, however, [recommend products from one collection only](/how-to-guides/recommend-skincare-routine-slots/).

    Follow these steps to set up your product recommendations:

    1. **Link Products to Choices**: Navigate to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup. For each choice, link/upvote relevant products.
        - You can upvote product variants, collections, tags, variant collections, vendor collections, or all variants of a product at once.
    2. **Edit the Results Page**: In the [Results Page](/reference/quiz-builder/results-page/) tab you can edit the content of your results screen. You can add a heading, content block, image block, HTML block, Product Block or a Product Slot block.

        !!! tip

            Check [How to Edit the Results Page](/how-to-guides/edit-results-page/) for more information.

    3. **Add a Product Block**: a `Product Block` lists the products on the Results Page, and a `Product Slot Block` divides them into slots. Start with a `Product Block`.
        - **Product Block** displays the products sorted by the number of upvotes - the most upvoted products are shown first, and the least upvoted last. In [Product Block settings](/reference/quiz-builder/questions/#block-settings) you can **choose how many products you want to show** at the end of the quiz.
            ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        - **Product Slot Blocks** show products in clear steps, such as a skincare routine. Each Slot recommends the most-upvoted product from the collection linked to it. *See [How to Recommend a Skincare Routine with Slots](/how-to-guides/recommend-skincare-routine-slots/).*
            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    4. **Test the Results**: After your products are linked and the results page is set up, you can test your quiz.
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz.
        - Then click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window.

            !!! note

                You can test the quiz as much as you like as long as you always open a new preview window. These test responses done as admin are automatically removed after 1 hour to not add to your usage quota.

    5. **Troubleshoot the Results**: the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section shows why a product was recommended, or why it was missing.

        !!! tip
            Check [How to Troubleshoot Quiz Results](/how-to-guides/troubleshoot-product-results/) for detailed instructions on how to use this tool.

    6. **Refine the Results**: If you want to make the results ultra-precise, you can also:
        - **Limit the recommendations**: You can choose to limit the recommendations to only show products that received X upvotes or more in the [Results Page settings](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use Exclusions**: You can use [Exclusions](#exclusion) to make sure that unwanted products are not shown (even if they were upvoted in another choice earlier).

    By linking product variants and collections to quiz choices, and understanding how inclusion and exclusion work, you can make the recommendations precise.

## Funnel quiz with slots

The upvoting system counts each product's upvotes, then fills every slot with the highest-upvoted product that matches that slot's filter. You can recommend a full skincare routine this way.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_funnel_with_slots](/images/how_to_shopify_v2_recommendations_funnel_with_slots.png){width=500}


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/YPuWvufx_8I?si=IAcwxOPePM1Nn2yw" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Follow these steps to set up a funnel quiz with product slots in the `💎Built for Shopify` version of the RevenueHunt app:

    **Step 1: Organize Products into Collections**

    To group products into slots, create new collections in your Shopify store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each category
    3. Add relevant products to each collection (e.g., all cleansers in the Cleansers collection)

    **Step 2: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 3: Link Products to Choices**

    1. Go to [Questions](/reference/quiz-builder/questions/)
    2. Select a multiple-choice question
    3. Select a choice and open the [Choice settings](/reference/quiz-builder/questions/#choice-settings)
    4. Link relevant product variants or collections to each choice
    5. Ensure every choice has at least one product or collection linked

    ![how_to_shopifyv2_setuprecommendations_linkcollections](/images/how_to_shopifyv2_setuprecommendations_linkcollections.png)

    **Step 4: Add Product Slots to the Results page**

    1. Go to the [Results page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Block`
    4. In the [`Product Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Add segments with corresponding product collections to each slot
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_shopify_v2_set_up_filters.png)

    **Step 5: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour


=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in Shopify:

    **Step 1: Organize Products into Collections**

    To group products into slots, create new collections in your Shopify store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each category
    3. Add relevant products to each collection (e.g., all cleansers in the Cleansers collection)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your collections

    ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

    **Step 2: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 3: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or collections to each choice
    3. Ensure every choice has at least one product or collection linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 4: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product collections to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 5: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in WooCommerce:

    **Step 1: Organize Products into Categories**

    To group products into slots, create new categories in your WooCommerce store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a category in your WooCommerce store](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) for each type
    3. Add relevant products to each category (e.g., all cleansers in the Cleansers category)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your categories

    **Step 2: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 3: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or categories to each choice
    3. Ensure every choice has at least one product or category linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 4: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product categories to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 5: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in Magento:

    **Step 1: Organize Products into Categories**

    To group products into slots, create new categories in your Magento store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a category in your Magento store](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) for each type
    3. Add relevant products to each category (e.g., all cleansers in the Cleansers category)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your categories

    **Step 2: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 3: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or categories to each choice
    3. Ensure every choice has at least one product or category linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 4: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product categories to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 5: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in BigCommerce:

    **Step 1: Organize Products into Categories**

    To group products into slots, create new categories in your BigCommerce store:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. [Create a category in your BigCommerce store](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) for each type
    3. Add relevant products to each category (e.g., all cleansers in the Cleansers category)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your categories

    **Step 2: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 3: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or categories to each choice
    3. Ensure every choice has at least one product or category linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 4: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product categories to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 5: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    Follow these steps to set up a funnel quiz with product slots in Standalone mode:

    **Step 1: Organize Products into Collections**

    To group products into slots, create new collections in your Standalone account:

    1. Identify your product categories (e.g., Cleansers, Toners, Serums, Moisturizers)
    2. Create collections in your Standalone account via the [Catalogue](/reference/dashboard/#success-checklist) tab or a Google Product Feed
    3. Add relevant products to each collection (e.g., all cleansers in the Cleansers collection)
    4. Perform a [catalog sync](/how-to-guides/sync-catalog/) to update RevenueHunt with your collections

    **Step 2: Build the Quiz**

    1. Go to the app's [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz)
    2. Choose a pre-defined template (like Basic or Advanced Skincare Quiz) or start from scratch
    3. Name your quiz (can be edited later)
    4. In the [Quiz Builder](/reference/quiz-builder/), add questions by clicking `+ Add question`
    5. Select appropriate [question types](/reference/quiz-builder/questions/#question-types) for your quiz flow

    **Step 3: Link Products to Choices**

    1. Navigate to [Link Products](/reference/quiz-builder/link-products/) or [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab
    2. Link relevant product variants or collections to each choice
    3. Ensure every choice has at least one product or collection linked

    ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    **Step 4: Add Product Slots to the Results Page**

    1. Go to the [Results Page](/reference/quiz-builder/results-page/) tab
    2. Add design elements (headings, logos, content blocks)
    3. Click the `+` button to add a `Product Slots Block`
    4. In the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings):
        - Add a slot for each step in the skincare routine
        - Add title and description for each slot
        - Link corresponding product collections to each slot in the `Include` section
        - Choose how many products to recommend per slot (typically one product)

    ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    **Step 5: Test and Troubleshoot**

    1. Click [`Publish/Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
    2. Click [`Preview`](/reference/quiz-builder/questions/) to test in a new window
    3. Use the quiz's [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses` to troubleshoot recommendations
    4. Test responses as admin are automatically removed after 1 hour

## Funnel quiz that skips slides

Show different follow-up questions based on customer choices in a multiple-choice, multiple selection question. For example, ask about skin concerns and then only show follow-up questions related to the selected concerns. The algorithm counts upvotes only from questions and answers shown to each customer.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_skiplogic.png](/images/how_to_shopify_v2_recommendations_skiplogic.png){width=500}

![how_to_hide_content_with_logic_shopifyv2_skip_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/5T-yW7c0OFs?si=_HxY8mZT9DHL25k2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The quiz can use skip logic to show different follow-up questions based on what the customer chose, so it skips questions that do not apply.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_mulriplechoice.png)

        - Open the RevenueHunt app and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' in the [`multiple-choice settings`](/reference/quiz-builder/questions/#multiple-choice) to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_followup.png)

        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip logic**: Configure conditional logic for each follow-up question:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_skiplogic.png)

        - Navigate to the Conditional logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - Repeat for each follow-up question and corresponding concern

        !!! example

            If `Skin Concerns` is not `Acne`, skip the Acne questions.

    4. **Link Products to Choices**: Navigate to the [Upvote](/reference/quiz-builder/link-products/) tab within your quiz setup:

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_linkproduct.png)

        - For each choice, upvote relevant products
        - Products or collections added in the `upvotes` field are upvoted in the final recommendations
        - The quiz will count upvotes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Save`](/reference/quiz-builder/questions/) to update the preview/live quiz
        - Use the preview feature to test different combinations of selections
        - Select multiple concerns (e.g., 'Acne' and 'Blackheads') to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.


=== "Shopify (Legacy)"

    The quiz can use skip logic to show different follow-up questions based on what the customer chose, so it skips questions that do not apply.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - Repeat for each follow-up question and corresponding concern

        !!! example

            If `Skin Concerns` is not `Acne`, skip the Acne questions.

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products/variants
        - The quiz will count upvotes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.


=== "WooCommerce"

    The quiz can use skip logic to show different follow-up questions based on what the customer chose, so it skips questions that do not apply.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - Repeat for each follow-up question and corresponding concern

        !!! example

            If `Skin Concerns` is not `Acne`, skip the Acne questions.

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products (simple products, variable products, or grouped products)
        - The quiz will count upvotes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "Magento"

    The quiz can use skip logic to show different follow-up questions based on what the customer chose, so it skips questions that do not apply.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - Repeat for each follow-up question and corresponding concern

        !!! example

            If `Skin Concerns` is not `Acne`, skip the Acne questions.

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products or variants
        - The quiz will count upvotes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "BigCommerce"

    The quiz can use skip logic to show different follow-up questions based on what the customer chose, so it skips questions that do not apply.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - Repeat for each follow-up question and corresponding concern

        !!! example

            If `Skin Concerns` is not `Acne`, skip the Acne questions.

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products or variants
        - The quiz will count upvotes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.

=== "Standalone"

    The quiz can use skip logic to show different follow-up questions based on what the customer chose, so it skips questions that do not apply.

    Follow these steps to set up a funnel quiz with skip logic:

    1. **Create Initial Question**: Create a multiple-choice question about the user's main concerns:
        - Open the RevenueHunt Quiz Builder and create a new quiz
        - Add a multiple-choice question asking about main concerns (e.g., skin concerns)
        - Add options such as Acne, Pigmentation, Blackheads, Flaky Skin
        - Enable 'Allow Multiple Selection' to let users select more than one option

    2. **Add Follow-Up Questions**: For each main concern, add corresponding follow-up questions:
        - Create a question for each option (e.g., Acne, Pigmentation, etc.)
        - Ensure follow-up questions are set up in the same order as the options in the initial question
        - Customize each follow-up question to be relevant to its specific concern

    3. **Set Up Skip Logic**: Configure conditional logic for each follow-up question:
        - Navigate to the Conditional Logic tab for each follow-up question
        - Add rules to skip questions if the corresponding concern was not selected
        - Repeat for each follow-up question and corresponding concern

        !!! example

            If `Skin Concerns` is not `Acne`, skip the Acne questions.

    4. **Link Products to Choices**: Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab within your quiz setup:
        - For each choice, link relevant products or variants
        - The quiz will count upvotes only from questions that were shown to the user

    5. **Test the Quiz Logic**: After setting up questions and skip logic:
        - Click [`Publish/Save`](/reference/quiz-builder/questions/) on the top-right menu to update the preview/live quiz
        - Click [`Preview`](/reference/quiz-builder/questions/) to test the quiz in a new window
        - Select multiple concerns to verify that only relevant follow-up questions are displayed
        - Repeat with different selections to ensure the logic works correctly

    6. **Troubleshoot the Results**: Use the quiz's [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if needed:
        - Check why specific questions were shown or skipped
        - Verify that product recommendations match user selections

    By using skip logic, your quiz will only show relevant questions based on customer choices, creating a more personalized experience and more accurate product recommendations.



## Funnel quiz with branching

Branch your quiz to show different follow-up questions based on customer choices. The algorithm counts upvotes only from questions and answers shown to each customer. You can display recommendations either as a simple list or arrange them into slots for a more structured presentation.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_jumplogic](/images/how_to_shopify_v2_recommendations_jumplogic.png){width=500}

=== "Shopify"

    Follow these steps to set up a branching funnel quiz in the `💎Built for Shopify` version of the RevenueHunt app:

    **Step 1: Build Quiz Structure**

    1. Create a new quiz in the [Quiz builder](/reference/quiz-builder/)
    2. Add all questions needed for each branch
    3. Add all possible choices for each question
    4. The order does not matter yet. Jump logic sets it.

    **Step 2: Set Up Branching**

    ![how_to_hide_content_with_logic_shopifyv2_jump_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)

    1. Go to each question's settings
    2. Add Jump logic rules in the Conditional logic section:
        - Set conditions for when to jump
        - Choose destination question
        - Add multiple rules if needed
    3. Make sure each branch ends with:
        - Lead collection question, or
        - Results page

    **Step 3: Link Products**

    1. For each choice in every branch:
        - Open Choice settings
        - Add products to "Upvote" section
        - Add collections if applicable
    2. The quiz only counts upvotes from shown questions

    **Step 4: Configure Results page**

    1. Add a Products Block
    2. Set "Recommendation system" to "Upvotes"
    3. Configure number of products to show
    4. Optionally add segments for structured recommendations

    **Step 5: Test and Launch**

    1. Save changes
    2. Preview and test each branch
    3. Use Response Analysis to verify logic
    4. Publish when ready


=== "Shopify (Legacy)"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. The order does not matter yet. Jump Logic sets it.

    **Step 2: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"

        !!! example

            If the answer to `What is your skin type?` is `Oily`, jump to `Oily Skin Concerns`.

    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 3: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count upvotes from questions shown to the user

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "WooCommerce"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. The order does not matter yet. Jump Logic sets it.

    **Step 2: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"

        !!! example

            If the answer to `What is your skin type?` is `Oily`, jump to `Oily Skin Concerns`.

    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 3: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count upvotes from questions shown to the user

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "Magento"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. The order does not matter yet. Jump Logic sets it.

    **Step 2: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"

        !!! example

            If the answer to `What is your skin type?` is `Oily`, jump to `Oily Skin Concerns`.

    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 3: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count upvotes from questions shown to the user

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "BigCommerce"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. The order does not matter yet. Jump Logic sets it.

    **Step 2: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"

        !!! example

            If the answer to `What is your skin type?` is `Oily`, jump to `Oily Skin Concerns`.

    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 3: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count upvotes from questions shown to the user

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic

=== "Standalone"

    Follow these steps to set up a branching funnel quiz in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed for each branch
    2. Add all possible choices for each question
    3. The order does not matter yet. Jump Logic sets it.

    **Step 2: Set Up Branching**

    1. Navigate to the Conditional Logic tab for each question
    2. Add Jump Logic rules to create branches:
        - Format: "If answer to Question X is Y, jump to Question Z"

        !!! example

            If the answer to `What is your skin type?` is `Oily`, jump to `Oily Skin Concerns`.

    3. Ensure each branch's final question leads to:
        - An email/phone collection question, or
        - The results page

    **Step 3: Link Products**

    1. Go to [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice in every branch:
        - Link relevant products/variants
        - Link appropriate collections
    3. The quiz will only count upvotes from questions shown to the user

    **Step 4: Configure Results Page**

    1. Add a Product Block to display recommendations
    2. Set the number of products to show
    3. Optionally, arrange products into slots for structured recommendations
    4. Configure any additional display settings

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test each branch thoroughly:
        - Try all possible paths
        - Verify correct questions appear
        - Check product recommendations
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic


## Funnel quiz that shows custom text based on choices

Show or hide different text blocks on the results page based on customer choices. This approach requires predicting every possible answering route and adding display logic rules for each text block.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_funnel_displaylogic](/images/how_to_shopify_v2_recommendations_funnel_displaylogic.png){width=500}

=== "Shopify"

    !!! warning "Not recommended for personality-type quizzes"

        Not recommended for personality-type quizzes due to complexity. For this application, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) solutions.

    Follow these steps to set up a funnel quiz with custom text blocks in the `💎Built for Shopify` version of the RevenueHunt app:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz builder](/reference/quiz-builder/) and create all questions needed. Add all possible choices for each question.

    **Step 2: Link Products to Choices**

    1. For each choice open Choice settings and add products to "Upvote" section.
    2. The quiz will count upvotes from all questions

    **Step 3: Configure Results page**

    1. Add a Products Block with "Upvotes" setting for Recommendations System.
    2. Add multiple Sections to your results page for different answer combinations. To each section add text, images or HTML content blocks for different answer combinations.

    **Step 4: Set Up Display logic**

    1. For each content block, add display logic rules in the block settings. Combine conditions with AND/OR operators.

        !!! example "How a display logic rule reads"

            If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.

            In practice: if "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show this block.

    2. Cover every possible answer combination.

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    **Step 5: Test and Launch**

    1. Save changes
    2. Test thoroughly! Try different answer combinations. Verify correct content appears. Check product recommendations.
    3. Use [Response Analysis](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.


=== "Shopify (Legacy)"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 2: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, variants or collections.
    3. The quiz will count upvotes from all questions

    **Step 3: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 4: Set Up Display Logic**

    1. For each content block, add display logic rules. You can combine several conditions with AND/OR operators.

        !!! example "How a display logic rule reads"

            If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.

            In practice: if "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    2. Cover every possible answer combination.

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "WooCommerce"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 2: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, variants or collections.
    3. The quiz will count upvotes from all questions

    **Step 3: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 4: Set Up Display Logic**

    1. For each content block, add display logic rules. You can combine several conditions with AND/OR operators.

        !!! example "How a display logic rule reads"

            If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.

            In practice: if "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    2. Cover every possible answer combination.

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "Magento"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 2: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, variants or collections.
    3. The quiz will count upvotes from all questions

    **Step 3: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 4: Set Up Display Logic**

    1. For each content block, add display logic rules. You can combine several conditions with AND/OR operators.

        !!! example "How a display logic rule reads"

            If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.

            In practice: if "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    2. Cover every possible answer combination.

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "BigCommerce"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 2: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, variants or collections.
    3. The quiz will count upvotes from all questions

    **Step 3: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 4: Set Up Display Logic**

    1. For each content block, add display logic rules. You can combine several conditions with AND/OR operators.

        !!! example "How a display logic rule reads"

            If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.

            In practice: if "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    2. Cover every possible answer combination.

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.

=== "Standalone"

    Follow these steps to set up a funnel quiz with custom text blocks in Shopify:

    **Step 1: Build Quiz Structure**

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and create all questions needed.Add all possible choices for each question.

    **Step 2: Link Products to Choices**

    1. Navigate to the [Link Products](/reference/quiz-builder/link-products/) tab
    2. For each choice link relevant products, variants or collections.
    3. The quiz will count upvotes from all questions

    **Step 3: Configure Results Page**

    1. Add a Product Block to display recommendations. Set the number of products to show.
    3. Add multiple content blocks, image or HTML blocks with text for different answer combinations.

    **Step 4: Set Up Display Logic**

    1. For each content block, add display logic rules. You can combine several conditions with AND/OR operators.

        !!! example "How a display logic rule reads"

            If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice C* **OR** If the answer to *Question 1* is *Choice A* **AND** If the answer to *Question 2* is *Choice B* **AND** If the answer to *Question 3* is *Choice D*, then this block is **shown/hidden**.

            In practice: if "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    2. Cover every possible answer combination.

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    **Step 5: Test and Launch**

    1. Click "Publish/Save" to update the quiz
    2. Test thoroughly! Try different answer combinations. Verify correct content blocks appear.
    3. Use the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/) to verify logic and check product recommendations.


---
This article explains how to set up a quiz that recommends products based on customer choices using a built-in upvoting system.
