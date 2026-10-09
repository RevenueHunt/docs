---
icon: material/slot-machine-outline
description: "Learn how to recommend personalized skincare routines using RevenueHunt product slot blocks."
---

# How to Recommend a Skincare Routine with Slots

A [Product Slots Block](/reference/quiz-builder/results-page/#block-types) groups the recommendations into fixed positions, one per step of a routine. A skincare routine might run cleanser, then toner, then serum, then moisturizer.

Each slot holds one group of products and shows the most upvoted product from it. Skincare is the example here, but the same setup fits anything sold as a set.

!!! info "How the recommendations are picked"

    Each choice upvotes the products linked to it, and each slot shows the most upvoted product from its own group. See [Upvoting system](/how-to-guides/set-up-funnel-quiz/#upvoting-system) for the whole algorithm, including ties, minimum upvote counts and exclusions.

![how to recommend slots example](/images/how_to_recommend_slots_example.png)

You can take the [example Skincare Quiz](https://skincarequiz.myshopify.com/#quiz-rkHm6Y) to see the result.

## Build the routine quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/YPuWvufx_8I?si=IAcwxOPePM1Nn2yw" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **List the steps of the routine.** For skincare, that is usually cleansers, toners, serums and moisturizers.

    2. **[Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each step.**

        Each collection holds only the products for that step: every cleanser in *Cleansers*, every serum in *Serums*. A product can sit in more than one collection.

        ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

    3. **Go to the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    4. **Choose a template, or start from scratch.** The Basic and Advanced Skincare Quiz templates arrive with their questions already written.

    5. **Name the quiz.** You can rename it later.

    6. **Add your questions in the [Quiz builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    7. **Open a multiple-choice question in [Questions](/reference/quiz-builder/questions/), select a choice, then open its [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

        ![manual_shopifyV2_quizbuilder_quizbuilder_upvotecollections](/images/manual_shopifyV2_quizbuilder_quizbuilder_upvotecollections.png)

    8. **Link the relevant product variants or collections to that choice.** Every choice needs at least one, or it upvotes nothing.

        ![how to recommend slots link products](/images/how_to_recommend_slots_shopify_v2_link_products.png)

    9. **Go to the [Results page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    10. **Add a `Product Block` with the `+` button.**

    11. **Add one slot per routine step in the [`Product Block settings`](/reference/quiz-builder/results-page/#block-settings).** A four-step routine needs four slots.

    12. **Give each slot a title and a description.**

    13. **Add a segment with that step's collection to each slot, in the `Add segment` section.** A slot recommends from its segment only.

        ![how to recommend slots slot block](/images/how_to_shopifyV2_recommend_routine_with_slots.png)

    14. **Choose how many products each slot recommends.** One per slot works best.

    15. **Click [`Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    16. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    17. **Check a recommendation with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in the `Responses` section.** It shows why a product was recommended, or why it was missing.

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps of the routine.** For skincare, that is usually cleansers, toners, serums and moisturizers.

    2. **[Create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for each step.**

        Each collection holds only the products for that step: every cleanser in *Cleansers*, every serum in *Serums*. A product can sit in more than one collection.

        ![how to recommend slots cleansers collection](/images/how_to_recommend_slots_cleansers_collection.png)

        !!! warning "Sync before you build"

            Run a [catalog sync](/how-to-guides/sync-catalog/) once the collections exist. The app cannot link a collection it has not imported yet.

    3. **Go to the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    4. **Choose a template, or start from scratch.** The Basic and Advanced Skincare Quiz templates arrive with their questions already written.

    5. **Name the quiz.** You can rename it later.

    6. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    7. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    8. **Link the relevant product variants or collections to every choice.** Every choice needs at least one, or it upvotes nothing.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    9. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    10. **Add a `Product Slots Block` with the `+` button.**

    11. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/results-page/#block-settings).** A four-step routine needs four slots.

    12. **Give each slot a title and a description.**

    13. **Link that step's collection to each slot, in the `Include` section.** A slot recommends from the collection you include only.

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Choose how many products each slot recommends.** One per slot works best.

    15. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    16. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    17. **Check a recommendation with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.** It shows why a product was recommended, or why it was missing.

=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps of the routine.** For skincare, that is usually cleansers, toners, serums and moisturizers.

    2. **[Create a category in your WooCommerce store](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) for each step.**

        Each category holds only the products for that step: every cleanser in *Cleansers*, every serum in *Serums*. A product can sit in more than one category.

        !!! warning "Sync before you build"

            Run a [catalog sync](/how-to-guides/sync-catalog/) once the categories exist. The app cannot link a category it has not imported yet.

    3. **Go to the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    4. **Choose a template, or start from scratch.** The Basic and Advanced Skincare Quiz templates arrive with their questions already written.

    5. **Name the quiz.** You can rename it later.

    6. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    7. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    8. **Link the relevant product variants or categories to every choice.** Every choice needs at least one, or it upvotes nothing.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    9. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    10. **Add a `Product Slots Block` with the `+` button.**

    11. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/results-page/#block-settings).** A four-step routine needs four slots.

    12. **Give each slot a title and a description.**

    13. **Link that step's category to each slot, in the `Include` section.** A slot recommends from the category you include only.

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Choose how many products each slot recommends.** One per slot works best.

    15. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    16. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    17. **Check a recommendation with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.** It shows why a product was recommended, or why it was missing.

=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps of the routine.** For skincare, that is usually cleansers, toners, serums and moisturizers.

    2. **[Create a category in your Magento store](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) for each step.**

        Each category holds only the products for that step: every cleanser in *Cleansers*, every serum in *Serums*. A product can sit in more than one category.

        !!! warning "Sync before you build"

            Run a [catalog sync](/how-to-guides/sync-catalog/) once the categories exist. The app cannot link a category it has not imported yet.

    3. **Go to the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    4. **Choose a template, or start from scratch.** The Basic and Advanced Skincare Quiz templates arrive with their questions already written.

    5. **Name the quiz.** You can rename it later.

    6. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    7. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    8. **Link the relevant product variants or categories to every choice.** Every choice needs at least one, or it upvotes nothing.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    9. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    10. **Add a `Product Slots Block` with the `+` button.**

    11. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/results-page/#block-settings).** A four-step routine needs four slots.

    12. **Give each slot a title and a description.**

    13. **Link that step's category to each slot, in the `Include` section.** A slot recommends from the category you include only.

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Choose how many products each slot recommends.** One per slot works best.

    15. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    16. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    17. **Check a recommendation with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.** It shows why a product was recommended, or why it was missing.

=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps of the routine.** For skincare, that is usually cleansers, toners, serums and moisturizers.

    2. **[Create a category in your BigCommerce store](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) for each step.**

        Each category holds only the products for that step: every cleanser in *Cleansers*, every serum in *Serums*. A product can sit in more than one category.

        !!! warning "Sync before you build"

            Run a [catalog sync](/how-to-guides/sync-catalog/) once the categories exist. The app cannot link a category it has not imported yet.

    3. **Go to the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    4. **Choose a template, or start from scratch.** The Basic and Advanced Skincare Quiz templates arrive with their questions already written.

    5. **Name the quiz.** You can rename it later.

    6. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    7. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    8. **Link the relevant product variants or categories to every choice.** Every choice needs at least one, or it upvotes nothing.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    9. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    10. **Add a `Product Slots Block` with the `+` button.**

    11. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/results-page/#block-settings).** A four-step routine needs four slots.

    12. **Give each slot a title and a description.**

    13. **Link that step's category to each slot, in the `Include` section.** A slot recommends from the category you include only.

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Choose how many products each slot recommends.** One per slot works best.

    15. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    16. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    17. **Check a recommendation with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.** It shows why a product was recommended, or why it was missing.

=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **List the steps of the routine.** For skincare, that is usually cleansers, toners, serums and moisturizers.

    2. **Create a collection for each step in your Standalone account.** Use the [Catalogue](/reference/dashboard/#success-checklist) tab or a Google Product Feed.

        Each collection holds only the products for that step: every cleanser in *Cleansers*, every serum in *Serums*. A product can sit in more than one collection.

        !!! warning "Sync before you build"

            Run a [catalog sync](/how-to-guides/sync-catalog/) once the collections exist. The app cannot link a collection it has not imported yet.

    3. **Go to the app [dashboard](/reference/dashboard/) and click [`add new quiz`](/reference/dashboard/#new-quiz).**

    4. **Choose a template, or start from scratch.** The Basic and Advanced Skincare Quiz templates arrive with their questions already written.

    5. **Name the quiz.** You can rename it later.

    6. **Add your questions in the [Quiz Builder](/reference/quiz-builder/).** Click `+ Add question`, then pick a [question type](/reference/quiz-builder/questions/#question-types).

    7. **Go to the [Link Products](/reference/quiz-builder/link-products/) tab, or the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**

    8. **Link the relevant product variants or collections to every choice.** Every choice needs at least one, or it upvotes nothing.

        ![how to recommend slots link products](/images/how_to_recommend_slots_link_products.png)

    9. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and add your design elements.** Headings, logos and content blocks.

    10. **Add a `Product Slots Block` with the `+` button.**

    11. **Add one slot per routine step in the [`Slot Block settings`](/reference/quiz-builder/results-page/#block-settings).** A four-step routine needs four slots.

    12. **Give each slot a title and a description.**

    13. **Link that step's collection to each slot, in the `Include` section.** A slot recommends from the collection you include only.

        ![how to recommend slots slot block](/images/how_to_recommend_slots_slot_block.png)

    14. **Choose how many products each slot recommends.** One per slot works best.

    15. **Click [`Publish/Save`](/reference/quiz-builder/questions/).** This updates both the preview and the live quiz.

    16. **Click [`Preview`](/reference/quiz-builder/questions/) and take the quiz.**

        !!! note "Test responses do not count towards your quota"

            You can test the quiz as often as you like, as long as you open a new preview window each time. Responses you make as an admin are removed automatically after one hour.

    17. **Check a recommendation with the [built-in search bar](/how-to-guides/troubleshoot-product-results/) in `Metrics > Responses`.** It shows why a product was recommended, or why it was missing.

!!! tip "Recommending from one group only"

    A slot can also carry the whole recommendation on its own. Give a single slot one group, and the quiz recommends the most upvoted product from that group and nothing else.

---

This article explains how to set up a quiz that recommends products in steps on the results page, such as a skincare routine.