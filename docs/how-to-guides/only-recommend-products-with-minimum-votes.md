---
description: "Step-by-step guide to limit RevenueHunt product recommendations by showing only products with a minimum number of upvotes."
icon: material/vote-outline
---

# How to Only Recommend Products with X Upvotes or More

A results page shows the best matches it has, however weak those matches are. If a customer answers in a way nothing really fits, they still get a list, and it is a list of near misses.

A minimum holds those back. A product has to collect a set number of upvotes before it can be recommended at all, so the customer sees strong matches or none.

## Work out the number you need

Every choice a customer selects gives one upvote to each product linked to that choice. The minimum is counted against that total, so the number you want depends on how your products are linked.

Take a skincare quiz with three questions that upvote, and three products linked like this.

| Product | Linked to the choices |
|---|---|
| Hydrating Serum | Dry skin, Dryness, Full routine |
| Gentle Cleanser | Dry skin, Oily skin, Combination skin |
| Clay Mask | Oily skin, Acne |

A customer answers **Dry skin**, then **Dryness**, then **Full routine**. The upvotes land like this.

| Product | Upvotes | Where they came from |
|---|---|---|
| Hydrating Serum | 3 | All three answers matched |
| Gentle Cleanser | 1 | Only the skin type matched |
| Clay Mask | 0 | Nothing matched |

The minimum then decides what the customer sees.

| Minimum | What the results page shows |
|---|---|
| 1 | Hydrating Serum and Gentle Cleanser |
| 2 | Hydrating Serum only |
| 3 | Hydrating Serum only |
| 4 | Nothing, because no product collected four |

!!! tip "Where to start"

    Count the questions that upvote products. That is the most any product can collect from a customer who picks one choice per question. Set the minimum above it and the block empties for everyone.

    Half of that count is a reasonable first try. Take the quiz a few times, answering as your customers would, and raise it until the near misses stop appearing.

!!! warning "Multiple selection changes the arithmetic"

    A question with [`Allow Multiple Selection`](/reference/quiz-builder/questions/#multiple-choice) turned on gives an upvote for every choice the customer picks, not one for the question. One question can then hand a single product three or four upvotes on its own.

    A minimum that equals your question count no longer means a product matched every question.

??? question "How the upvote count is worked out"

    - Products are linked to each choice.
    - When a customer picks a choice, every product linked to it gains one upvote.
    - The results page shows the products with the most upvotes first.
    - Products on equal upvotes appear in a random order.
    - If nothing is linked, or everything is excluded, the results page comes back empty.

    See [how to recommend products](/how-to-guides/recommend-products/).

## Set the minimum

=== "Shopify"

    The minimum is a setting on the block itself, so there is nothing to switch on elsewhere. Your [results page](/reference/quiz-builder/results-page/) needs a `Products` block.

    1. **Open your [results page](/reference/quiz-builder/results-page/) and click the `Products` block.**

    2. **Find `Min. number of upvotes` in the block settings.**

        ![The Min. number of upvotes setting in the Products block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products.png)

    3. **Set the number, with the slider or the field beside it.**

    4. **Click the top-right `Save` button.**

    5. **Take the quiz and check that only the strongest matches come back.** A product below the minimum should not appear at all.

=== "Shopify (Legacy)"

    The minimum is switched on for the whole results page, then set on each block. Your [results page](/reference/quiz-builder/results-page/) needs a `Products` block or a slot block.

    !!! warning "One results page setting has to come first"

        `Minimum number of votes` only appears on a block while the results page is set to show nothing when there are no matches.

        Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and check that `Recommendations Settings` is on `If no results, no products` rather than `If no results, random products`.

        ![The no results options in Recommendations Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and turn `Minimum number of votes` on.** Each product and slot block then gains a minimum of its own.

        ![The Minimum number of votes toggle in the Advanced tab](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    3. **Close the settings, then click the `Products` block you want to limit.**

    4. **Pick a number from `Min. number of votes` in the [block settings](/reference/quiz-builder/results-page/#block-settings).**

        ![The Min. number of votes dropdown in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

    5. **Repeat for every other product or slot block that needs a minimum.**

    6. **Click the top-right `Publish` button.**

    7. **Take the quiz and check that only the strongest matches come back.** A product below the minimum should not appear at all.

=== "WooCommerce"

    The minimum is switched on for the whole results page, then set on each block. Your [results page](/reference/quiz-builder/results-page/) needs a `Products` block or a slot block.

    !!! warning "One results page setting has to come first"

        `Minimum number of votes` only appears on a block while the results page is set to show nothing when there are no matches.

        Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and check that `Recommendations Settings` is on `If no results, no products` rather than `If no results, random products`.

        ![The no results options in Recommendations Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and turn `Minimum number of votes` on.** Each product and slot block then gains a minimum of its own.

        ![The Minimum number of votes toggle in the Advanced tab](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    3. **Close the settings, then click the `Products` block you want to limit.**

    4. **Pick a number from `Min. number of votes` in the [block settings](/reference/quiz-builder/results-page/#block-settings).**

        ![The Min. number of votes dropdown in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

    5. **Repeat for every other product or slot block that needs a minimum.**

    6. **Click the top-right `Publish` button.**

    7. **Take the quiz and check that only the strongest matches come back.** A product below the minimum should not appear at all.

=== "Magento"

    The minimum is switched on for the whole results page, then set on each block. Your [results page](/reference/quiz-builder/results-page/) needs a `Products` block or a slot block.

    !!! warning "One results page setting has to come first"

        `Minimum number of votes` only appears on a block while the results page is set to show nothing when there are no matches.

        Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and check that `Recommendations Settings` is on `If no results, no products` rather than `If no results, random products`.

        ![The no results options in Recommendations Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and turn `Minimum number of votes` on.** Each product and slot block then gains a minimum of its own.

        ![The Minimum number of votes toggle in the Advanced tab](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    3. **Close the settings, then click the `Products` block you want to limit.**

    4. **Pick a number from `Min. number of votes` in the [block settings](/reference/quiz-builder/results-page/#block-settings).**

        ![The Min. number of votes dropdown in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

    5. **Repeat for every other product or slot block that needs a minimum.**

    6. **Click the top-right `Publish` button.**

    7. **Take the quiz and check that only the strongest matches come back.** A product below the minimum should not appear at all.

=== "BigCommerce"

    The minimum is switched on for the whole results page, then set on each block. Your [results page](/reference/quiz-builder/results-page/) needs a `Products` block or a slot block.

    !!! warning "One results page setting has to come first"

        `Minimum number of votes` only appears on a block while the results page is set to show nothing when there are no matches.

        Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and check that `Recommendations Settings` is on `If no results, no products` rather than `If no results, random products`.

        ![The no results options in Recommendations Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and turn `Minimum number of votes` on.** Each product and slot block then gains a minimum of its own.

        ![The Minimum number of votes toggle in the Advanced tab](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    3. **Close the settings, then click the `Products` block you want to limit.**

    4. **Pick a number from `Min. number of votes` in the [block settings](/reference/quiz-builder/results-page/#block-settings).**

        ![The Min. number of votes dropdown in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

    5. **Repeat for every other product or slot block that needs a minimum.**

    6. **Click the top-right `Publish` button.**

    7. **Take the quiz and check that only the strongest matches come back.** A product below the minimum should not appear at all.

=== "Standalone"

    The minimum is switched on for the whole results page, then set on each block. Your [results page](/reference/quiz-builder/results-page/) needs a `Products` block or a slot block.

    !!! warning "One results page setting has to come first"

        `Minimum number of votes` only appears on a block while the results page is set to show nothing when there are no matches.

        Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and check that `Recommendations Settings` is on `If no results, no products` rather than `If no results, random products`.

        ![The no results options in Recommendations Settings](/images/how_to_only_recommend_product_with_min_votes_show_random_products.png)

    1. **Open your results page in the [Quiz Builder](/reference/quiz-builder/) and click the cog icon.**

    2. **Open the [`ADVANCED`](/reference/quiz-builder/results-page/#advanced-settings) tab and turn `Minimum number of votes` on.** Each product and slot block then gains a minimum of its own.

        ![The Minimum number of votes toggle in the Advanced tab](/images/how_to_only_recommend_product_with_min_votes_results_page_settings.png)

    3. **Close the settings, then click the `Products` block you want to limit.**

    4. **Pick a number from `Min. number of votes` in the [block settings](/reference/quiz-builder/results-page/#block-settings).**

        ![The Min. number of votes dropdown in the block settings](/images/how_to_only_recommend_product_with_min_votes_block_settings.png)

    5. **Repeat for every other product or slot block that needs a minimum.**

    6. **Click the top-right `Publish` button.**

    7. **Take the quiz and check that only the strongest matches come back.** A product below the minimum should not appear at all.

## When nothing clears the bar

A minimum can leave a block with nothing to show. That is the point of it, but decide what the customer reads instead.

=== "Shopify"

    Fill in `No recommendations message` in the [block settings](/reference/quiz-builder/results-page/#block-settings). It shows in place of the products, and it accepts HTML and Liquid, so you can name the customer or their answer in it.

    Leave it empty and the customer simply sees no products.

    !!! tip "Give them somewhere to go"

        A block that can empty is worth pairing with a line that offers a next step, such as browsing a collection or contacting you.

=== "Shopify (Legacy)"

    By default the block shows this instead of the products.

    !!! example "The default empty message"

        Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us.

    Edit that wording in [Quiz settings > Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

    To drop the block from the page altogether when it has nothing to show, turn on `Hide block when no products are recommended` in the [block settings](/reference/quiz-builder/results-page/#block-settings).

=== "WooCommerce"

    By default the block shows this instead of the products.

    !!! example "The default empty message"

        Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us.

    Edit that wording in [Quiz settings > Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

    To drop the block from the page altogether when it has nothing to show, turn on `Hide block when no products are recommended` in the [block settings](/reference/quiz-builder/results-page/#block-settings).

=== "Magento"

    By default the block shows this instead of the products.

    !!! example "The default empty message"

        Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us.

    Edit that wording in [Quiz settings > Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

    To drop the block from the page altogether when it has nothing to show, turn on `Hide block when no products are recommended` in the [block settings](/reference/quiz-builder/results-page/#block-settings).

=== "BigCommerce"

    By default the block shows this instead of the products.

    !!! example "The default empty message"

        Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us.

    Edit that wording in [Quiz settings > Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

    To drop the block from the page altogether when it has nothing to show, turn on `Hide block when no products are recommended` in the [block settings](/reference/quiz-builder/results-page/#block-settings).

=== "Standalone"

    By default the block shows this instead of the products.

    !!! example "The default empty message"

        Based on your answers, we need a little more time to give you our recommendations. Please get in touch with us.

    Edit that wording in [Quiz settings > Messages](/reference/quiz-builder/quiz-settings/#messages-quiz-content).

    To drop the block from the page altogether when it has nothing to show, turn on `Hide block when no products are recommended` in the [block settings](/reference/quiz-builder/results-page/#block-settings).

---

This article explains how to hold a weak match back from the results page. You set the upvotes a product needs before it can be recommended.