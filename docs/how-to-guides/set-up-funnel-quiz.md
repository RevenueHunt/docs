---
description: "Complete guide to setting up a RevenueHunt funnel quiz with dynamic product upvoting system."
icon: material/filter-variant
---

# How to Set Up a Funnel Quiz

A funnel quiz helps a customer find the right product. Every choice the customer makes gives an upvote to the products linked to that choice. At the end, the quiz recommends the products with the most upvotes.

!!! info "Use this method for:"

    - Helping customers narrow down a large product catalog
    - Most quizzes, especially product finders
    - Your first product recommendation quiz
    - Quizzes without complex branching

There are five ways to build one. They all count upvotes the same way, and differ only in how the questions are arranged and how the results page is built.

| Method | Use it when |
|---|---|
| [Funnel quiz](#funnel-quiz) | Every customer answers the same questions and gets one list of recommendations |
| [Funnel quiz with slots](#funnel-quiz-with-slots) | The result is a routine or a set, such as a cleanser, then a serum, then a moisturizer |
| [Funnel quiz that skips slides](#funnel-quiz-that-skips-slides) | Follow-up questions apply only to the concerns the customer selected |
| [Funnel quiz with branching](#funnel-quiz-with-branching) | Different answers send the customer down different paths |
| [Funnel quiz that shows custom text based on choices](#funnel-quiz-that-shows-custom-text-based-on-choices) | The text on the results page has to change with the answers |

## Upvoting system

An **upvote** is the signal a choice gives a product. This is how an upvote becomes a recommendation:

1. You link products, variants or collections to each choice.
2. A customer picks that choice, and every linked item gets one upvote.
3. The results page lists them, highest upvote count first.

!!! info "An empty results page has two causes"

    Either nothing was linked to the choices the customer made, or [Exclusions](#exclusion) removed everything that was upvoted.

Two settings refine the list:

- [A minimum upvote count](/how-to-guides/only-recommend-products-with-minimum-votes/) hides products that did not get enough upvotes.
- [Exclusions](#exclusion) keep a product out entirely, even when another choice upvoted it.

### When two products have the same upvote count

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

Upvote inclusion and exclusion decide which products can be recommended at all. Inclusion adds a product to the upvote count. Exclusion keeps it out of the results, whatever its count.

### Upvote inclusion

=== "Shopify"

    To link products or collections to choices, open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) and go to the `Upvotes` section.

    ![how to recommend products upvote](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    1. **Click `+ Add upvote type`.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotemain](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotemain.png)

    2. **Choose what the choice upvotes.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown.png)

    3. **Select the products, collections or tags themselves.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall.png)

    What each upvote type does:

    - **Main Products / All variants of the same product at once** - the whole product is upvoted, not one variant. Every variant of it receives the upvote when the linked choice is selected.
    - **Product variants** - an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Collections** - every product in a linked collection receives an upvote when its linked choice is selected.
    - **Tags** - every product with a linked tag receives an upvote when its linked choice is selected.
    - **Variant collections** - created automatically by the app. Every product in a linked variant collection receives an upvote when its linked choice is selected.
    - **Vendor collections** - created automatically by the app. Every product in a linked vendor collection receives an upvote when its linked choice is selected.

    !!! tip "Recommending text instead of products"

        A quiz can also recommend pure text. Add one section per result to the results page, then control which section appears with Display logic. Text results do not use the upvoting system. They use the [scoring system](/how-to-guides/set-up-scoring-quiz/) or conditional logic instead.

=== "Shopify (Legacy)"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    What each upvote type does:

    - **Product variants** - an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Collections** - every product in a linked collection receives an upvote when its linked choice is selected.
    - **Tags** - every product with a linked tag receives an upvote when its linked choice is selected.
    - **Variant collections** - created automatically by the app. Every product in a linked variant collection receives an upvote when its linked choice is selected.
    - **Vendor collections** - created automatically by the app. Every product in a linked vendor collection receives an upvote when its linked choice is selected.
    - **All variants of the same product at once** - every variant of a product is upvoted at once when its linked choice is selected.

    !!! note "Upvoting all variants at once"

        `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) has to be active before **All variants of the same product at once** appears in the Link Products section.

=== "WooCommerce"

    Products or categories added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    What each upvote type does:

    - **Simple Products** - an individual product receives an upvote when its linked choice is selected.
    - **Product variants** - an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Product Bundles** - a bundle counts as one product, and receives one upvote when its linked choice is selected.
    - **Affiliate Products** - an individual product receives an upvote when its linked choice is selected. On the results page the customer goes to the affiliate link, not to the store link.
    - **Categories** - every product in a linked category receives an upvote when its linked choice is selected.
    - **Tags** - every product with a linked tag receives an upvote when its linked choice is selected.
    - **All variants of the same product at once** - every variant of a product is upvoted at once when its linked choice is selected.

    !!! note "Upvoting all variants at once"

        `Use top-level product` in [Quiz Settings](/reference/quiz-builder/quiz-settings/) has to be active before **All variants of the same product at once** appears in the Link Products section.

=== "Magento"

    Products or categories added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    What each upvote type does:

    - **Product variants** - an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Categories** - every product in a linked category receives an upvote when its linked choice is selected.

=== "BigCommerce"

    Products or categories added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    What each upvote type does:

    - **Product variants** - an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Categories** - every product in a linked category receives an upvote when its linked choice is selected.
    - **Tags** - every product with a linked tag receives an upvote when its linked choice is selected.

    !!! tip "Using custom fields as tags"

        See [BigCommerce: Use Custom Fields as Tags](/how-to-guides/use-custom-fields-as-tags/).

=== "Standalone"

    Products or collections added in the `include/upvotes` field of the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab are upvoted in the final recommendations.

    ![how to recommend products inclusion](/images/how_to_recommend_products_inclusion.png)

    What each upvote type does:

    - **Product variants** - an individual variant receives an upvote when its linked choice is selected. Only variants link to choices directly, but the results page can group variants under their parent product.
    - **Collections** - every product in a linked collection receives an upvote when its linked choice is selected.

!!! warning "One choice can upvote the same variant twice"

    A variant can be upvoted twice by one choice: once through the Upvote tab directly, and again through a collection that contains it. That choice then gives it **2 upvotes**.

### Exclusion

=== "Shopify"

    To exclude products or collections from a choice, open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) and go to the `Exclude` section.

    ![how to recommend products exclusion](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    1. **Click `+ Add exclude type`.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain.png)

    2. **Choose what the choice excludes.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown.png)

    3. **Select the products, collections or tags themselves.** Each one joins the excluded list.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall.png)

=== "Shopify (Legacy)"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to keep products or collections out of the recommendations. This is useful for items with allergens or sensitive ingredients.

=== "WooCommerce"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to keep products or collections out of the recommendations. This is useful for items with allergens or sensitive ingredients.

=== "Magento"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to keep products or collections out of the recommendations. This is useful for items with allergens or sensitive ingredients.

=== "BigCommerce"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to keep products or collections out of the recommendations. This is useful for items with allergens or sensitive ingredients.

=== "Standalone"

    ![how to recommend products exclusion](/images/how_to_recommend_products_exclusion.png)

    Use the `exclude` field of the [Link Products/Collections/Exclude](/reference/quiz-builder/link-products/) tab to keep products or collections out of the recommendations. This is useful for items with allergens or sensitive ingredients.

!!! warning "An exclusion always wins"

    Once a choice excludes a product, it **never shows** as a recommendation, even if another choice upvotes it.

!!! example "Filtering recommendations by price"

    Exclusions can filter the recommendations question by question. To keep the results inside a budget, exclude a collection of products above that price from the matching choice.

    ![how to recommend products exclusion example](/images/how_to_recommend_products_exclusion_example.png)

    A customer who says they do not want to spend more than $100 then sees no products above that price.
## Funnel quiz

Every customer answers the same questions. Each choice upvotes the products linked to it, and the results page lists the products with the most upvotes first.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_funnel](/images/how_to_shopify_v2_recommendations_funnel.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/j-Ecp4NeTfQ?si=gTp7uWal22QfKFVC" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The results page can show **product variants**, **main products** and **collections**.

    1. **Link products to your choices.** Open the [Upvote](/reference/quiz-builder/link-products/) tab, then upvote the relevant products for each choice.

        ![how to recommend products inclusion](/images/how_to_shopifyv2_setuprecommendations_linkcollections.png)

        !!! tip "Link one collection instead of twenty products"

            Create a hidden collection in Shopify for each choice, and put only the relevant products in it. One collection per choice is easier to maintain than a long list of single products.

        !!! info "What each upvote type does"

            See [Upvote inclusion](#upvote-inclusion) for how variants, collections, tags and vendor collections are counted, and [Exclusion](#exclusion) for how to keep a product out of the results.

    2. **Edit the results page.** Open the [Results page](/reference/quiz-builder/results-page/) tab and add a heading, a content block, an image block or an HTML block.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage.png)

        !!! tip "Editing the results page"

            See [how to edit the results page](/how-to-guides/edit-results-page/).

    3. **Add a `Products Block`.** Click `+ Add Block` and select [`Products Block`](/reference/quiz-builder/results-page/#product-product-variants-collections).

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes_products](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocktypes_products.png)

    4. **Set `Recommendation system` to `Upvotes` in the block settings.** The block then lists the products by upvote count, most upvoted first.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    5. **Choose how many products to show in the [slot settings](/reference/quiz-builder/questions/#block-settings).** Every products block has one default `Slot`, and that slot holds the recommended products.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slot](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slot.png)

        The results page then shows the products like this, sorted by upvote count:

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

        !!! note "Recommending a routine instead of a list"

            A products block can also show products in clear steps, such as a **skincare routine**. Give a slot a **Segment Filter** and it recommends the most upvoted product from the collection linked to it. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

    6. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    7. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    8. **Check a recommendation in the [Responses](/reference/quiz-builder/metrics/#responses) section.** The built-in search tool shows why a product was recommended, or why it was missing.

        ![how to recommend products built for shopify revenuehunt app troubleshoot results](/images/manual_shopifyV2_quizbuilder_responses_sample1_checkproduct.png)

        !!! tip "Troubleshooting the results"

            See [how to troubleshoot quiz results](/how-to-guides/troubleshoot-product-results/) for how to use this tool.

    !!! tip "Refining the results"

        - **Set a minimum upvote count.** Show only the products that reached it. See [how to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use exclusions.** [Exclusions](#exclusion) keep unwanted products out of the results, even when an earlier choice upvoted them.

=== "Shopify (Legacy)"

    The results page can show **product variants**, **main products** and **[Recharge subscription products](/how-to-guides/recommend-subscription-products/)**.

    The quiz **cannot recommend collections** of products. You can, however, [recommend products from one collection only](/how-to-guides/recommend-skincare-routine-slots/).

    1. **Link products to your choices.** Go to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab, then upvote the relevant products for each choice.

        See [Upvote inclusion](#upvote-inclusion) for what each upvote type does, and [Exclusion](#exclusion) for how to keep a product out of the results.

    2. **Edit the Results Page.** In the [Results Page](/reference/quiz-builder/results-page/) tab, add a heading, a content block, an image block or an HTML block.

        !!! tip "Editing the Results Page"

            See [how to edit the results page](/how-to-guides/edit-results-page/).

    3. **Add a `Product Block` to the Results Page.** It lists the products by upvote count, most upvoted first.

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

    4. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

        !!! tip "Recommending a routine instead of a list"

            A `Product Slot Block` divides the recommendations into slots, such as the steps of a skincare routine. Each slot recommends the most upvoted product from the collection linked to it. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    5. **Click [`Publish/Save`](/reference/quiz-builder/questions/) in the top-right menu.** This updates both the preview and the live quiz.

    6. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    7. **Check a recommendation with the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section.** It shows why a product was recommended, or why it was missing.

        !!! tip "Troubleshooting the results"

            See [how to troubleshoot quiz results](/how-to-guides/troubleshoot-product-results/) for how to use this tool.

    !!! tip "Refining the results"

        - **Set a minimum upvote count.** Show only the products that reached it. See [how to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use exclusions.** [Exclusions](#exclusion) keep unwanted products out of the results, even when an earlier choice upvoted them.

=== "WooCommerce"

    The results page can show **simple products**, **variable products**, **grouped products**, **external/affiliate products** and **[WooCommerce subscription products](/how-to-guides/recommend-subscription-products/)**.

    The quiz **cannot recommend categories** of products. You can, however, [recommend products from one category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    !!! warning "One variant type per product"

        The app syncs only one type of variant per variable product. If a product varies by both size and color, the app syncs the size variants only.

    1. **Link products to your choices.** Go to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab, then upvote the relevant products for each choice.

        See [Upvote inclusion](#upvote-inclusion) for what each upvote type does, and [Exclusion](#exclusion) for how to keep a product out of the results.

    2. **Edit the Results Page.** In the [Results Page](/reference/quiz-builder/results-page/) tab, add a heading, a content block, an image block or an HTML block.

        !!! tip "Editing the Results Page"

            See [how to edit the results page](/how-to-guides/edit-results-page/).

    3. **Add a `Product Block` to the Results Page.** It lists the products by upvote count, most upvoted first.

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

    4. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

        !!! tip "Recommending a routine instead of a list"

            A `Product Slot Block` divides the recommendations into slots, such as the steps of a skincare routine. Each slot recommends the most upvoted product from the collection linked to it. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    5. **Click [`Publish/Save`](/reference/quiz-builder/questions/) in the top-right menu.** This updates both the preview and the live quiz.

    6. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    7. **Check a recommendation with the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section.** It shows why a product was recommended, or why it was missing.

        !!! tip "Troubleshooting the results"

            See [how to troubleshoot quiz results](/how-to-guides/troubleshoot-product-results/) for how to use this tool.

    !!! tip "Refining the results"

        - **Set a minimum upvote count.** Show only the products that reached it. See [how to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use exclusions.** [Exclusions](#exclusion) keep unwanted products out of the results, even when an earlier choice upvoted them.

=== "Magento"

    The results page can show **product variants** and **main products**.

    The quiz **cannot recommend categories** of products. You can, however, [recommend products from one category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    1. **Link products to your choices.** Go to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab, then upvote the relevant products for each choice.

        See [Upvote inclusion](#upvote-inclusion) for what each upvote type does, and [Exclusion](#exclusion) for how to keep a product out of the results.

    2. **Edit the Results Page.** In the [Results Page](/reference/quiz-builder/results-page/) tab, add a heading, a content block, an image block or an HTML block.

        !!! tip "Editing the Results Page"

            See [how to edit the results page](/how-to-guides/edit-results-page/).

    3. **Add a `Product Block` to the Results Page.** It lists the products by upvote count, most upvoted first.

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

    4. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

        !!! tip "Recommending a routine instead of a list"

            A `Product Slot Block` divides the recommendations into slots, such as the steps of a skincare routine. Each slot recommends the most upvoted product from the collection linked to it. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    5. **Click [`Publish/Save`](/reference/quiz-builder/questions/) in the top-right menu.** This updates both the preview and the live quiz.

    6. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    7. **Check a recommendation with the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section.** It shows why a product was recommended, or why it was missing.

        !!! tip "Troubleshooting the results"

            See [how to troubleshoot quiz results](/how-to-guides/troubleshoot-product-results/) for how to use this tool.

    !!! tip "Refining the results"

        - **Set a minimum upvote count.** Show only the products that reached it. See [how to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use exclusions.** [Exclusions](#exclusion) keep unwanted products out of the results, even when an earlier choice upvoted them.

=== "BigCommerce"

    The results page can show **product variants** and **main products**.

    The quiz **cannot recommend categories** of products. You can, however, [recommend products from one category, tag or attribute](/how-to-guides/recommend-skincare-routine-slots/).

    1. **Link products to your choices.** Go to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab, then upvote the relevant products for each choice.

        See [Upvote inclusion](#upvote-inclusion) for what each upvote type does, and [Exclusion](#exclusion) for how to keep a product out of the results.

    2. **Edit the Results Page.** In the [Results Page](/reference/quiz-builder/results-page/) tab, add a heading, a content block, an image block or an HTML block.

        !!! tip "Editing the Results Page"

            See [how to edit the results page](/how-to-guides/edit-results-page/).

    3. **Add a `Product Block` to the Results Page.** It lists the products by upvote count, most upvoted first.

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

    4. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

        !!! tip "Recommending a routine instead of a list"

            A `Product Slot Block` divides the recommendations into slots, such as the steps of a skincare routine. Each slot recommends the most upvoted product from the collection linked to it. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    5. **Click [`Publish/Save`](/reference/quiz-builder/questions/) in the top-right menu.** This updates both the preview and the live quiz.

    6. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    7. **Check a recommendation with the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section.** It shows why a product was recommended, or why it was missing.

        !!! tip "Troubleshooting the results"

            See [how to troubleshoot quiz results](/how-to-guides/troubleshoot-product-results/) for how to use this tool.

    !!! tip "Refining the results"

        - **Set a minimum upvote count.** Show only the products that reached it. See [how to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use exclusions.** [Exclusions](#exclusion) keep unwanted products out of the results, even when an earlier choice upvoted them.

=== "Standalone"

    The results page can show **product variants** and **main products**.

    The quiz **cannot recommend collections** of products. You can, however, [recommend products from one collection only](/how-to-guides/recommend-skincare-routine-slots/).

    1. **Link products to your choices.** Go to the [Link Products/Collections/Upvote](/reference/quiz-builder/link-products/) tab, then upvote the relevant products for each choice.

        See [Upvote inclusion](#upvote-inclusion) for what each upvote type does, and [Exclusion](#exclusion) for how to keep a product out of the results.

    2. **Edit the Results Page.** In the [Results Page](/reference/quiz-builder/results-page/) tab, add a heading, a content block, an image block or an HTML block.

        !!! tip "Editing the Results Page"

            See [how to edit the results page](/how-to-guides/edit-results-page/).

    3. **Add a `Product Block` to the Results Page.** It lists the products by upvote count, most upvoted first.

        ![how to recommend products product block](/images/how_to_recommend_products_product_block.png){width="500"}

    4. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

        !!! tip "Recommending a routine instead of a list"

            A `Product Slot Block` divides the recommendations into slots, such as the steps of a skincare routine. Each slot recommends the most upvoted product from the collection linked to it. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

            ![how to recommend products slots block](/images/how_to_recommend_products_slots_block.png)

    5. **Click [`Publish/Save`](/reference/quiz-builder/questions/) in the top-right menu.** This updates both the preview and the live quiz.

    6. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    7. **Check a recommendation with the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section.** It shows why a product was recommended, or why it was missing.

        !!! tip "Troubleshooting the results"

            See [how to troubleshoot quiz results](/how-to-guides/troubleshoot-product-results/) for how to use this tool.

    !!! tip "Refining the results"

        - **Set a minimum upvote count.** Show only the products that reached it. See [how to only recommend products with X upvotes or more](/how-to-guides/only-recommend-products-with-minimum-votes/).
        - **Use exclusions.** [Exclusions](#exclusion) keep unwanted products out of the results, even when an earlier choice upvoted them.

## Funnel quiz with slots

The quiz counts the upvotes, then fills every slot with the highest upvoted product that matches that slot. Use it to recommend a full routine, such as a cleanser, then a serum, then a moisturizer.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_funnel_with_slots](/images/how_to_shopify_v2_recommendations_funnel_with_slots.png){width=500}

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/YPuWvufx_8I?si=IAcwxOPePM1Nn2yw" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **List the steps your routine needs.** A skincare routine might be cleansers, toners, serums and moisturizers.

    2. **[Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each step.**

    3. **Add the matching products to each collection.** Every cleanser goes in the Cleansers collection.

    4. **Open the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    5. **Choose a template, or start from scratch.** A template such as Basic or Advanced Skincare Quiz arrives with its questions already written.

    6. **Name the quiz.** You can rename it later.

    7. **Add your questions in the [Quiz builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    8. **Open a multiple-choice question in [Questions](/reference/quiz-builder/questions/) and select a choice.**

    9. **Link the relevant products or collections in the [Choice settings](/reference/quiz-builder/questions/#choice-settings).** Every choice needs at least one product or collection.

        ![how_to_shopifyv2_setuprecommendations_linkcollections](/images/how_to_shopifyv2_setuprecommendations_linkcollections.png)

    10. **Open the [Results page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    11. **Add a `Products Block`.** Click the `+` button.

    12. **Add one slot per routine step in the [block settings](/reference/quiz-builder/questions/#block-settings).** For each slot:

        - Add a title and a description
        - Add a segment with the product collection for that step
        - Choose how many products to recommend, usually one

        ![how to recommend slots slot block](/images/how_to_recommend_slots_shopify_v2_set_up_filters.png)

    13. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    14. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    15. **Check the recommendations with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in the `Responses` section.**

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps your routine needs.** A skincare routine might be cleansers, toners, serums and moisturizers.

    2. **[Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each step.**

        ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

    3. **Add the matching products to each collection.** Every cleanser goes in the Cleansers collection.

    4. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new collections.

    5. **Open the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    6. **Choose a template, or start from scratch.** A template such as Basic or Advanced Skincare Quiz arrives with its questions already written.

    7. **Name the quiz.** You can rename it later.

    8. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    9. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    10. **Link the relevant product variants or collections to each choice.** Every choice needs at least one product or collection.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    11. **Open the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    12. **Add a `Product Slots Block`.** Click the `+` button.

    13. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings).** For each slot:

        - Add a title and a description
        - Link the product collection for that step in the `Include` section
        - Choose how many products to recommend, usually one

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    15. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    16. **Check the recommendations with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.**

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps your routine needs.** A skincare routine might be cleansers, toners, serums and moisturizers.

    2. **[Create a category in your WooCommerce store](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) for each step.**

    3. **Add the matching products to each category.** Every cleanser goes in the Cleansers category.

    4. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new categories.

    5. **Open the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    6. **Choose a template, or start from scratch.** A template such as Basic or Advanced Skincare Quiz arrives with its questions already written.

    7. **Name the quiz.** You can rename it later.

    8. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    9. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    10. **Link the relevant product variants or categories to each choice.** Every choice needs at least one product or category.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    11. **Open the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    12. **Add a `Product Slots Block`.** Click the `+` button.

    13. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings).** For each slot:

        - Add a title and a description
        - Link the product category for that step in the `Include` section
        - Choose how many products to recommend, usually one

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    15. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    16. **Check the recommendations with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.**

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps your routine needs.** A skincare routine might be cleansers, toners, serums and moisturizers.

    2. **[Create a category in your Magento store](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) for each step.**

    3. **Add the matching products to each category.** Every cleanser goes in the Cleansers category.

    4. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new categories.

    5. **Open the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    6. **Choose a template, or start from scratch.** A template such as Basic or Advanced Skincare Quiz arrives with its questions already written.

    7. **Name the quiz.** You can rename it later.

    8. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    9. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    10. **Link the relevant product variants or categories to each choice.** Every choice needs at least one product or category.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    11. **Open the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    12. **Add a `Product Slots Block`.** Click the `+` button.

    13. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings).** For each slot:

        - Add a title and a description
        - Link the product category for that step in the `Include` section
        - Choose how many products to recommend, usually one

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    15. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    16. **Check the recommendations with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.**

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps your routine needs.** A skincare routine might be cleansers, toners, serums and moisturizers.

    2. **[Create a category in your BigCommerce store](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) for each step.**

    3. **Add the matching products to each category.** Every cleanser goes in the Cleansers category.

    4. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new categories.

    5. **Open the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    6. **Choose a template, or start from scratch.** A template such as Basic or Advanced Skincare Quiz arrives with its questions already written.

    7. **Name the quiz.** You can rename it later.

    8. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    9. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    10. **Link the relevant product variants or categories to each choice.** Every choice needs at least one product or category.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    11. **Open the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    12. **Add a `Product Slots Block`.** Click the `+` button.

    13. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings).** For each slot:

        - Add a title and a description
        - Link the product category for that step in the `Include` section
        - Choose how many products to recommend, usually one

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    15. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    16. **Check the recommendations with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.**

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps your routine needs.** A skincare routine might be cleansers, toners, serums and moisturizers.

    2. **Create a collection in your Standalone account, through the [Catalogue](/reference/dashboard/#success-checklist) tab or a Google Product Feed for each step.**

    3. **Add the matching products to each collection.** Every cleanser goes in the Cleansers collection.

    4. **Run a [catalog sync](/how-to-guides/sync-catalog/).** This is what tells the app about your new collections.

    5. **Open the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    6. **Choose a template, or start from scratch.** A template such as Basic or Advanced Skincare Quiz arrives with its questions already written.

    7. **Name the quiz.** You can rename it later.

    8. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    9. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    10. **Link the relevant product variants or collections to each choice.** Every choice needs at least one product or collection.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    11. **Open the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    12. **Add a `Product Slots Block`.** Click the `+` button.

    13. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/questions/#block-settings).** For each slot:

        - Add a title and a description
        - Link the product collection for that step in the `Include` section
        - Choose how many products to recommend, usually one

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    15. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz in a new window.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    16. **Check the recommendations with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.**
## Funnel quiz that skips slides

Skip logic hides the follow-up questions that do not apply to a customer. Ask about skin concerns first, then show only the questions that match the concerns the customer selected.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_skiplogic.png](/images/how_to_shopify_v2_recommendations_skiplogic.png){width=500}

![how_to_hide_content_with_logic_shopifyv2_skip_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_skip_logic_flow.png)

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/5T-yW7c0OFs?si=_HxY8mZT9DHL25k2" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The quiz shows different follow-up questions depending on what the customer chose, and skips the questions that do not apply.

    1. **Add a multiple-choice question about the customer's main concerns.**

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_mulriplechoice.png)

    2. **Add a choice for each concern.** For a skincare quiz: Acne, Pigmentation, Blackheads and Flaky Skin.

    3. **Turn on `Allow Multiple Selection` in the [multiple-choice settings](/reference/quiz-builder/questions/#multiple-choice).** The customer can then pick more than one concern.

    4. **Add one follow-up question per concern.** Keep them in the same order as the choices in the first question.

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_followup.png)

    5. **Write each follow-up question for its own concern.**

    6. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the first follow-up question.**

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_skiplogic.png)

    7. **Find `Skip logic` in the menu on the right, and click `+ Add another rule (OR)`.**

    8. **Set the rule to `IF the response to` the concerns question `is not` that question's own concern.**

        !!! example "The rule on the acne question"

            `IF the response to` `Skin Concerns` `is not` `Acne`.

            The question is then skipped for everyone who did not pick acne.

    9. **Repeat for every follow-up question, each reading its own concern.**

    10. **Link products to your choices in the [Upvote](/reference/quiz-builder/link-products/) tab.** Upvote the relevant products for each choice.

        ![how to set up a funnel quiz with skip logic](/images/how_to_shopifyv2_skiplogicquiz_linkproduct.png)

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    11. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and select two concerns.** Check that only the matching follow-up questions appear.

    13. **Repeat the preview with other combinations of concerns.**

    14. **Check the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if a result looks wrong.** It shows why a question was shown or skipped, and why a product was recommended.

=== "Shopify (Legacy)"

    The quiz shows different follow-up questions depending on what the customer chose, and skips the questions that do not apply.

    1. **Add a multiple-choice question about the customer's main concerns.**

    2. **Add a choice for each concern.** For a skincare quiz: Acne, Pigmentation, Blackheads and Flaky Skin.

    3. **Turn on `Allow Multiple Selection` in the multiple-choice settings.** The customer can then pick more than one concern.

    4. **Add one follow-up question per concern.** Keep them in the same order as the choices in the first question.

    5. **Write each follow-up question for its own concern.**

    6. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the first follow-up question.**

    7. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    8. **Set the rule to `IF response to` the concerns question `is not` that question's own concern.**

        !!! example "The rule on the acne question"

            `IF response to` `Skin Concerns` `is not` `Acne`.

            The question is then skipped for everyone who did not pick acne.

    9. **Repeat for every follow-up question, each reading its own concern.**

    10. **Link products to your choices in the [Link Products](/reference/quiz-builder/link-products/) tab.** Link the relevant products or variants to each choice.

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and select two concerns.** Check that only the matching follow-up questions appear.

    13. **Repeat the preview with other combinations of concerns.**

    14. **Check the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if a result looks wrong.** It shows why a question was shown or skipped, and why a product was recommended.

=== "WooCommerce"

    The quiz shows different follow-up questions depending on what the customer chose, and skips the questions that do not apply.

    1. **Add a multiple-choice question about the customer's main concerns.**

    2. **Add a choice for each concern.** For a skincare quiz: Acne, Pigmentation, Blackheads and Flaky Skin.

    3. **Turn on `Allow Multiple Selection` in the multiple-choice settings.** The customer can then pick more than one concern.

    4. **Add one follow-up question per concern.** Keep them in the same order as the choices in the first question.

    5. **Write each follow-up question for its own concern.**

    6. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the first follow-up question.**

    7. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    8. **Set the rule to `IF response to` the concerns question `is not` that question's own concern.**

        !!! example "The rule on the acne question"

            `IF response to` `Skin Concerns` `is not` `Acne`.

            The question is then skipped for everyone who did not pick acne.

    9. **Repeat for every follow-up question, each reading its own concern.**

    10. **Link products to your choices in the [Link Products](/reference/quiz-builder/link-products/) tab.** Link the relevant simple, variable or grouped products to each choice.

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and select two concerns.** Check that only the matching follow-up questions appear.

    13. **Repeat the preview with other combinations of concerns.**

    14. **Check the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if a result looks wrong.** It shows why a question was shown or skipped, and why a product was recommended.

=== "Magento"

    The quiz shows different follow-up questions depending on what the customer chose, and skips the questions that do not apply.

    1. **Add a multiple-choice question about the customer's main concerns.**

    2. **Add a choice for each concern.** For a skincare quiz: Acne, Pigmentation, Blackheads and Flaky Skin.

    3. **Turn on `Allow Multiple Selection` in the multiple-choice settings.** The customer can then pick more than one concern.

    4. **Add one follow-up question per concern.** Keep them in the same order as the choices in the first question.

    5. **Write each follow-up question for its own concern.**

    6. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the first follow-up question.**

    7. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    8. **Set the rule to `IF response to` the concerns question `is not` that question's own concern.**

        !!! example "The rule on the acne question"

            `IF response to` `Skin Concerns` `is not` `Acne`.

            The question is then skipped for everyone who did not pick acne.

    9. **Repeat for every follow-up question, each reading its own concern.**

    10. **Link products to your choices in the [Link Products](/reference/quiz-builder/link-products/) tab.** Link the relevant products or variants to each choice.

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and select two concerns.** Check that only the matching follow-up questions appear.

    13. **Repeat the preview with other combinations of concerns.**

    14. **Check the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if a result looks wrong.** It shows why a question was shown or skipped, and why a product was recommended.

=== "BigCommerce"

    The quiz shows different follow-up questions depending on what the customer chose, and skips the questions that do not apply.

    1. **Add a multiple-choice question about the customer's main concerns.**

    2. **Add a choice for each concern.** For a skincare quiz: Acne, Pigmentation, Blackheads and Flaky Skin.

    3. **Turn on `Allow Multiple Selection` in the multiple-choice settings.** The customer can then pick more than one concern.

    4. **Add one follow-up question per concern.** Keep them in the same order as the choices in the first question.

    5. **Write each follow-up question for its own concern.**

    6. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the first follow-up question.**

    7. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    8. **Set the rule to `IF response to` the concerns question `is not` that question's own concern.**

        !!! example "The rule on the acne question"

            `IF response to` `Skin Concerns` `is not` `Acne`.

            The question is then skipped for everyone who did not pick acne.

    9. **Repeat for every follow-up question, each reading its own concern.**

    10. **Link products to your choices in the [Link Products](/reference/quiz-builder/link-products/) tab.** Link the relevant products or variants to each choice.

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and select two concerns.** Check that only the matching follow-up questions appear.

    13. **Repeat the preview with other combinations of concerns.**

    14. **Check the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if a result looks wrong.** It shows why a question was shown or skipped, and why a product was recommended.

=== "Standalone"

    The quiz shows different follow-up questions depending on what the customer chose, and skips the questions that do not apply.

    1. **Add a multiple-choice question about the customer's main concerns.**

    2. **Add a choice for each concern.** For a skincare quiz: Acne, Pigmentation, Blackheads and Flaky Skin.

    3. **Turn on `Allow Multiple Selection` in the multiple-choice settings.** The customer can then pick more than one concern.

    4. **Add one follow-up question per concern.** Keep them in the same order as the choices in the first question.

    5. **Write each follow-up question for its own concern.**

    6. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the first follow-up question.**

    7. **Open the `Skip Logic` tab and click `Add Skip Logic`.**

    8. **Set the rule to `IF response to` the concerns question `is not` that question's own concern.**

        !!! example "The rule on the acne question"

            `IF response to` `Skin Concerns` `is not` `Acne`.

            The question is then skipped for everyone who did not pick acne.

    9. **Repeat for every follow-up question, each reading its own concern.**

    10. **Link products to your choices in the [Link Products](/reference/quiz-builder/link-products/) tab.** Link the relevant products or variants to each choice.

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and select two concerns.** Check that only the matching follow-up questions appear.

    13. **Repeat the preview with other combinations of concerns.**

    14. **Check the [built-in search tool](/reference/quiz-builder/metrics/#responses) in the `Responses` section if a result looks wrong.** It shows why a question was shown or skipped, and why a product was recommended.

## Funnel quiz with branching

Jump logic sends the customer down a different path depending on their answers. Each branch asks its own questions, and the recommendations still come from the upvotes collected along the way.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_jumplogic](/images/how_to_shopify_v2_recommendations_jumplogic.png){width=500}

=== "Shopify"

    1. **Create every question each branch needs in the [Quiz builder](/reference/quiz-builder/).**

    2. **Add every choice each question needs.**

        !!! info "Question order does not matter yet"

            Jump logic sets the order the customer sees, so the order you add the questions in is not the order they are asked in.

    3. **Go to the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab and select the question the branches start from.**

        ![how_to_hide_content_with_logic_shopifyv2_jump_logic_flow](/images/how_to_hide_content_with_logic_shopifyv2_jump_logic_flow.png)

    4. **Find `Jump Logic` in the menu on the right, and click `+ Add another rule (OR)`.**

    5. **Set the rule to `IF the response to` that question `is` one answer, `THEN go to` the first question of that answer's branch.**

        !!! example "The rule that opens the oily skin branch"

            `IF the response to` `What is your skin type?` `is` `Oily`, `THEN go to` `Oily Skin Concerns`.

    6. **Click `+ Add another rule (OR)` again for every other answer that opens a branch.**

    7. **End every branch with a question that collects an email or phone number, or with the results page.**

    8. **Open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) of each choice and upvote the relevant products or collections.**

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    9. **Add a `Products Block` to the results page.**

    10. **Set `Recommendation system` to `Upvotes`, then choose how many products to show.**

    11. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and take every branch.** Check that the right questions appear, and that the recommendations match the answers.

    13. **Check the logic with the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/).**

    !!! tip "Grouping the recommendations"

        Slots arrange the recommendations into fixed positions instead of one list. Give a slot a Segment Filter to control which products it can recommend. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

=== "Shopify (Legacy)"

    1. **Create every question each branch needs in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Add every choice each question needs.**

        !!! info "Question order does not matter yet"

            Jump Logic sets the order the customer sees, so the order you add the questions in is not the order they are asked in.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question the branches start from.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` that question `is` one answer, `THEN go to` the first question of that answer's branch.**

        !!! example "The rule that opens the oily skin branch"

            `IF response to` `What is your skin type?` `is` `Oily`, `THEN go to` `Oily Skin Concerns`.

    6. **Click the `+` button to add a rule for every other answer that opens a branch.**

    7. **End every branch with a question that collects an email or phone number, or with the Results Page.**

    8. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    9. **Add a `Product Block` to the Results Page.**

    10. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and take every branch.** Check that the right questions appear, and that the recommendations match the answers.

    13. **Check the logic with the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/).**

    !!! tip "Grouping the recommendations"

        Slots arrange the recommendations into fixed positions instead of one list, such as a cleanser, then a serum, then a moisturizer. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

=== "WooCommerce"

    1. **Create every question each branch needs in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Add every choice each question needs.**

        !!! info "Question order does not matter yet"

            Jump Logic sets the order the customer sees, so the order you add the questions in is not the order they are asked in.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question the branches start from.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` that question `is` one answer, `THEN go to` the first question of that answer's branch.**

        !!! example "The rule that opens the oily skin branch"

            `IF response to` `What is your skin type?` `is` `Oily`, `THEN go to` `Oily Skin Concerns`.

    6. **Click the `+` button to add a rule for every other answer that opens a branch.**

    7. **End every branch with a question that collects an email or phone number, or with the Results Page.**

    8. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    9. **Add a `Product Block` to the Results Page.**

    10. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and take every branch.** Check that the right questions appear, and that the recommendations match the answers.

    13. **Check the logic with the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/).**

    !!! tip "Grouping the recommendations"

        Slots arrange the recommendations into fixed positions instead of one list, such as a cleanser, then a serum, then a moisturizer. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

=== "Magento"

    1. **Create every question each branch needs in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Add every choice each question needs.**

        !!! info "Question order does not matter yet"

            Jump Logic sets the order the customer sees, so the order you add the questions in is not the order they are asked in.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question the branches start from.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` that question `is` one answer, `THEN go to` the first question of that answer's branch.**

        !!! example "The rule that opens the oily skin branch"

            `IF response to` `What is your skin type?` `is` `Oily`, `THEN go to` `Oily Skin Concerns`.

    6. **Click the `+` button to add a rule for every other answer that opens a branch.**

    7. **End every branch with a question that collects an email or phone number, or with the Results Page.**

    8. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    9. **Add a `Product Block` to the Results Page.**

    10. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and take every branch.** Check that the right questions appear, and that the recommendations match the answers.

    13. **Check the logic with the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/).**

    !!! tip "Grouping the recommendations"

        Slots arrange the recommendations into fixed positions instead of one list, such as a cleanser, then a serum, then a moisturizer. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

=== "BigCommerce"

    1. **Create every question each branch needs in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Add every choice each question needs.**

        !!! info "Question order does not matter yet"

            Jump Logic sets the order the customer sees, so the order you add the questions in is not the order they are asked in.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question the branches start from.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` that question `is` one answer, `THEN go to` the first question of that answer's branch.**

        !!! example "The rule that opens the oily skin branch"

            `IF response to` `What is your skin type?` `is` `Oily`, `THEN go to` `Oily Skin Concerns`.

    6. **Click the `+` button to add a rule for every other answer that opens a branch.**

    7. **End every branch with a question that collects an email or phone number, or with the Results Page.**

    8. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    9. **Add a `Product Block` to the Results Page.**

    10. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and take every branch.** Check that the right questions appear, and that the recommendations match the answers.

    13. **Check the logic with the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/).**

    !!! tip "Grouping the recommendations"

        Slots arrange the recommendations into fixed positions instead of one list, such as a cleanser, then a serum, then a moisturizer. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

=== "Standalone"

    1. **Create every question each branch needs in the [Quiz Builder](/reference/quiz-builder/).**

    2. **Add every choice each question needs.**

        !!! info "Question order does not matter yet"

            Jump Logic sets the order the customer sees, so the order you add the questions in is not the order they are asked in.

    3. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) settings of the question the branches start from.**

    4. **Open the `Jump Logic` section and click `Add Jump Logic`.**

    5. **Set the rule to `IF response to` that question `is` one answer, `THEN go to` the first question of that answer's branch.**

        !!! example "The rule that opens the oily skin branch"

            `IF response to` `What is your skin type?` `is` `Oily`, `THEN go to` `Oily Skin Concerns`.

    6. **Click the `+` button to add a rule for every other answer that opens a branch.**

    7. **End every branch with a question that collects an email or phone number, or with the Results Page.**

    8. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Only the questions the customer saw are counted"

            A question the customer never sees upvotes nothing. The quiz counts upvotes only from the questions it showed.

    9. **Add a `Product Block` to the Results Page.**

    10. **Choose how many products to show in the [Product Block settings](/reference/quiz-builder/questions/#block-settings).**

    11. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    12. **Preview the quiz and take every branch.** Check that the right questions appear, and that the recommendations match the answers.

    13. **Check the logic with the [Response Analysis tool](/how-to-guides/troubleshoot-product-results/).**

    !!! tip "Grouping the recommendations"

        Slots arrange the recommendations into fixed positions instead of one list, such as a cleanser, then a serum, then a moisturizer. See [how to recommend a skincare routine with slots](/how-to-guides/recommend-skincare-routine-slots/).

## Funnel quiz that shows custom text based on choices

Display logic shows and hides individual blocks on the results page, so the text can change with the answers. Every customer answers the same questions, and every answer combination needs its own rule.

This method uses the [upvoting system](#upvoting-system).

![how_to_shopify_v2_recommendations_funnel_displaylogic](/images/how_to_shopify_v2_recommendations_funnel_displaylogic.png){width=500}

=== "Shopify"

    !!! warning "Not the best fit for a personality quiz"

        The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

    1. **Create every question the quiz needs in the [Quiz builder](/reference/quiz-builder/), with all of its choices.**

    2. **Open the [Choice settings](/reference/quiz-builder/questions/#choice-settings) of each choice and upvote the relevant products.**

        !!! info "Every question counts here"

            Every customer sees every question in this method, so the quiz counts upvotes from all of them.

    3. **Add a `Products Block` to the results page and set `Recommendation system` to `Upvotes`.**

    4. **Add one section per answer combination to the results page.** Put the text, image or HTML blocks for that combination inside its own section.

    5. **Add a display logic rule to each content block in the block settings.** Combine the conditions with AND and OR.

        !!! example "How a display logic rule reads"

            Show this block if:

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice C*

            **OR**

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice D*

            In practice: when "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    6. **Write a rule for every possible answer combination.**

        !!! warning "Every route needs a rule"

            This method needs a display logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    7. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    8. **Preview the quiz with different answer combinations.** Check that the right content appears each time.

    9. **Check the logic with [Response Analysis](/how-to-guides/troubleshoot-product-results/).**

=== "Shopify (Legacy)"

    !!! warning "Not the best fit for a personality quiz"

        The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

    1. **Create every question the quiz needs in the [Quiz Builder](/reference/quiz-builder/), with all of its choices.**

    2. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Every question counts here"

            Every customer sees every question in this method, so the quiz counts upvotes from all of them.

    3. **Add a `Product Block` to the Results Page and set `Recommendation system` to `Upvotes`.**

    4. **Add a content block, an image block or an HTML block for each answer combination.**

    5. **Add a Display Logic rule to each content block in the block settings.** Combine the conditions with AND and OR.

        !!! example "How a display logic rule reads"

            Show this block if:

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice C*

            **OR**

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice D*

            In practice: when "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    6. **Write a rule for every possible answer combination.**

        !!! warning "Every route needs a rule"

            This method needs a Display Logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    7. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    8. **Preview the quiz with different answer combinations.** Check that the right content appears each time.

    9. **Check the logic with [Response Analysis](/how-to-guides/troubleshoot-product-results/).**

=== "WooCommerce"

    !!! warning "Not the best fit for a personality quiz"

        The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

    1. **Create every question the quiz needs in the [Quiz Builder](/reference/quiz-builder/), with all of its choices.**

    2. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Every question counts here"

            Every customer sees every question in this method, so the quiz counts upvotes from all of them.

    3. **Add a `Product Block` to the Results Page and set `Recommendation system` to `Upvotes`.**

    4. **Add a content block, an image block or an HTML block for each answer combination.**

    5. **Add a Display Logic rule to each content block in the block settings.** Combine the conditions with AND and OR.

        !!! example "How a display logic rule reads"

            Show this block if:

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice C*

            **OR**

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice D*

            In practice: when "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    6. **Write a rule for every possible answer combination.**

        !!! warning "Every route needs a rule"

            This method needs a Display Logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    7. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    8. **Preview the quiz with different answer combinations.** Check that the right content appears each time.

    9. **Check the logic with [Response Analysis](/how-to-guides/troubleshoot-product-results/).**

=== "Magento"

    !!! warning "Not the best fit for a personality quiz"

        The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

    1. **Create every question the quiz needs in the [Quiz Builder](/reference/quiz-builder/), with all of its choices.**

    2. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Every question counts here"

            Every customer sees every question in this method, so the quiz counts upvotes from all of them.

    3. **Add a `Product Block` to the Results Page and set `Recommendation system` to `Upvotes`.**

    4. **Add a content block, an image block or an HTML block for each answer combination.**

    5. **Add a Display Logic rule to each content block in the block settings.** Combine the conditions with AND and OR.

        !!! example "How a display logic rule reads"

            Show this block if:

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice C*

            **OR**

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice D*

            In practice: when "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    6. **Write a rule for every possible answer combination.**

        !!! warning "Every route needs a rule"

            This method needs a Display Logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    7. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    8. **Preview the quiz with different answer combinations.** Check that the right content appears each time.

    9. **Check the logic with [Response Analysis](/how-to-guides/troubleshoot-product-results/).**

=== "BigCommerce"

    !!! warning "Not the best fit for a personality quiz"

        The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

    1. **Create every question the quiz needs in the [Quiz Builder](/reference/quiz-builder/), with all of its choices.**

    2. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Every question counts here"

            Every customer sees every question in this method, so the quiz counts upvotes from all of them.

    3. **Add a `Product Block` to the Results Page and set `Recommendation system` to `Upvotes`.**

    4. **Add a content block, an image block or an HTML block for each answer combination.**

    5. **Add a Display Logic rule to each content block in the block settings.** Combine the conditions with AND and OR.

        !!! example "How a display logic rule reads"

            Show this block if:

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice C*

            **OR**

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice D*

            In practice: when "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    6. **Write a rule for every possible answer combination.**

        !!! warning "Every route needs a rule"

            This method needs a Display Logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    7. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    8. **Preview the quiz with different answer combinations.** Check that the right content appears each time.

    9. **Check the logic with [Response Analysis](/how-to-guides/troubleshoot-product-results/).**

=== "Standalone"

    !!! warning "Not the best fit for a personality quiz"

        The number of rules grows with every question. For a personality quiz, try the [🎯 Custom Scoring System (Most Upvoted Variable)](/how-to-guides/set-up-scoring-quiz/) or [🧩 Fixed Recommendations with Display logic](/how-to-guides/set-up-fixed-recommendations-quiz/) instead.

    1. **Create every question the quiz needs in the [Quiz Builder](/reference/quiz-builder/), with all of its choices.**

    2. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab and link the relevant products, variants or collections to each choice.**

        !!! info "Every question counts here"

            Every customer sees every question in this method, so the quiz counts upvotes from all of them.

    3. **Add a `Product Block` to the Results Page and set `Recommendation system` to `Upvotes`.**

    4. **Add a content block, an image block or an HTML block for each answer combination.**

    5. **Add a Display Logic rule to each content block in the block settings.** Combine the conditions with AND and OR.

        !!! example "How a display logic rule reads"

            Show this block if:

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice C*

            **OR**

            *Question 1* is *Choice A* **AND** *Question 2* is *Choice B* **AND** *Question 3* is *Choice D*

            In practice: when "Skin Type" is "Oily" **AND** "Main Concern" is "Acne", show the skincare routine for oily, acne-prone skin.

    6. **Write a rule for every possible answer combination.**

        !!! warning "Every route needs a rule"

            This method needs a Display Logic rule for each way through the quiz. A combination you miss has no rule to show its block.

    7. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    8. **Preview the quiz with different answer combinations.** Check that the right content appears each time.

    9. **Check the logic with [Response Analysis](/how-to-guides/troubleshoot-product-results/).**

---
This article explains how to set up a quiz that recommends products based on customer choices using a built-in upvoting system.