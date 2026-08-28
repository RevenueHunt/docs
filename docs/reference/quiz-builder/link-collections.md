---
description: "Link product collections to quiz choices in RevenueHunt with upvote weighting for product recommendations."
---

# Link Collections / Link Categories

=== "Shopify"

    To link collections of products to choices, go to [Questions](/reference/quiz-builder/questions/), select a multiple-choice question, then a choice and open the [`Choice Settings`](/reference/quiz-builder/questions/#choice-settings).

    ![manual_shopifyv2_openchoicesettings](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    Choose the weight of this choice:

    `Upvotes weighting` - Sets a default weight of this choice. For example, if the weight is set to 2, all the upvoted products from a collection receive x2 (double) upvotes from this choice.

    **Upvote**

    ![manual_shopifyV2_linkcollections_upvote](/images/manual_shopifyV2_linkcollections_upvote.png)

    Use the Upvotes section to choose which collections to link to this choice:

    `Upvotes` - lists all the collections, tags, variants collections or vendors that are linked to this choice.

    ![manual_shopifyV2_quizbuilder_quizbuilder_upvotecollections](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotemain.png)

    `+ Add upvote type` - Click to choose an item to upvote. You can upvote entire collections, tags, variants collections or vendors collections to a choice. A new section then opens, where you pick collections, tags, variants or vendors from your Shopify catalog.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown.png)

    ![manual_shopifyV2_quizbuilder_linkcollections_upvotecollections](/images/manual_shopifyV2_quizbuilder_linkcollections_upvotecollections.png)

    Toggle the collections to be upvoted to add them to the upvoted list.

    Upvoted collections will be listed in the upvoted section.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall.png)

    !!! note

        You can upvote entire collections, and also recommend a whole collection to the customer.
    
    **Exclude**

    ![manual_shopifyV2_linkcollections_exclude](/images/manual_shopifyV2_linkcollections_exclude.png)

    Use the Exclude section to choose which collections to exclude from this choice:

    `Exclude` - lists all the products, product variants, collections, tags, variants collections or vendors that are excluded in this choice.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain.png)

    `+ Add exclude type` - Click to choose an item to exclude. You can exclude entire collections, tags, variants collections or vendors from a choice. A new section then opens, where you pick the items to exclude from your Shopify catalog.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown.png)

    Toggle the collections to be excluded to add them to the excluded list.

    ![manual_shopifyV2_quizbuilder_linkcollections_upvotecollections](/images/manual_shopifyV2_quizbuilder_linkcollections_upvotecollections.png)

    Excluded collections will be listed in the excluded section.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall.png)

    !!! warning

        Be careful with exclusions. Once a product is excluded from a choice, it never shows on the results page. This applies even if another choice upvoted it.


=== "Shopify (Legacy)"

    ![quiz builder link collections](/images/manual_quizbuilder_linkcollections.png)

    In the Link Collections tab, you can link entire collections of products from your store to choices. This includes Shopify collections, tags, virtual vendors, and variants collections.

    Once a collection is linked to a choice and the customer picks that choice, all the products in that collection will receive 1 upvote.

    To link a collection to a choice click on the white dropdown bar and start typing the name.

    ![quiz builder link collections search](/images/manual_quizbuilder_linkcollections_search.png)

    Select a collection and it will be automatically added to the choice. 

    `Moisturizers(1)` - The number in brackets is how many product variants are in that collection.

    You can link several collections to the same choice, but be careful. A product in two collections linked to the same choice gets 2 upvotes, one from each collection.

    ![quiz builder link collections linked collections](/images/manual_quizbuilder_linkcollections_linked.png)

    To remove a linked collection click `x` next to the collection name.

    `excluded collections` - Opens the dropdown which lets you exclude collections of products from a choice.

    ![quiz builder link collections exclude](/images/manual_quizbuilder_linkcollections_exclude.png)

    Be careful with exclusions. Once a collection is excluded from a choice, its products never show on the results page. This applies even if another choice upvoted them.

    **Missing collections, or collections showing (0) products?** - You may need to run a [Catalog Sync](/how-to-guides/sync-catalog/) to update the app.

=== "WooCommerce"

    ![quiz builder woo link categories](/images/manual_woo_quizbuilder_linkcategories.png)

    In the Link Categories tab, you can link entire categories of products from your store to choices. This includes WooCommerce categories, tags and attributes.

    Once a category is linked to a choice and the customer picks that choice, all the products in that category will receive 1 upvote.

    To link a category to a choice click on the white dropdown bar and start typing the name.

    ![quiz builder link collections search](/images/manual_woo_quizbuilder_linkcategories_pickcategory.png)

    Select a category and it will be automatically added to the choice. 

    `Moisturizers(1)` - The number in brackets is how many product variants are in that category.

    You can link several categories to the same choice, but be careful. A product in two categories linked to the same choice gets 2 upvotes, one from each category.

    ![quiz builder woo link categories linked](/images/manual_woo_quizbuilder_linkcategories_linked_categories.png)

    To remove a linked category click `x` next to the category name.

    `excluded collections` - Opens the dropdown which lets you exclude categories of products from a choice.

    ![quiz builder link collections exclude](/images/manual_woo_quizbuilder_linkcategories_excludecategories.png)

    Be careful with exclusions. Once a category is excluded from a choice, its products never show on the results page. This applies even if another choice upvoted them.

    **Missing categories, or categories showing (0) products?** - You may need to run a [Catalog Sync](/how-to-guides/sync-catalog/) to update the app.

=== "Magento"

    ![quiz builder standalone link categories](/images/manual_standalone_quizbuilder_linkcategories.png)

    In the Link Categories tab, you can link entire categories of products from your store to choices.

    Once a category is linked to a choice and the customer picks that choice, all the products in that category will receive 1 upvote.

    To link a category to a choice click on the white dropdown bar and start typing the name.

    ![quiz builder link categories search](/images/manual_standalone_quizbuilder_linkcategories_pickcategory.png)

    Select a category and it will be automatically added to the choice. 

    `Moisturizers(1)` - The number in brackets is how many product variants are in that category.

    You can link several categories to the same choice, but be careful. A product in two categories linked to the same choice gets 2 upvotes, one from each category.

    ![quiz builder standalone link categories linked](/images/manual_standalone_quizbuilder_linkcategories_linked_categories.png)

    To remove a linked category click `x` next to the category name.

    `excluded collections` - Opens the dropdown which lets you exclude categories of products from a choice.

    ![quiz builder link cocategories exclude](/images/manual_standalone_quizbuilder_linkcategories_excludecategories.png)

    Be careful with exclusions. Once a category is excluded from a choice, its products never show on the results page. This applies even if another choice upvoted them.

    **Missing categories, or categories showing (0) products?** - You may need to run a [Catalog Sync](/how-to-guides/sync-catalog/) to update the app.

=== "BigCommerce"

    ![quiz builder standalone link categories](/images/manual_standalone_quizbuilder_linkcategories.png)

    In the Link Categories tab, you can link entire categories of products from your store to choices.

    Once a category is linked to a choice and the customer picks that choice, all the products in that category will receive 1 upvote.

    To link a category to a choice click on the white dropdown bar and start typing the name.

    ![quiz builder link categories search](/images/manual_standalone_quizbuilder_linkcategories_pickcategory.png)

    Select a category and it will be automatically added to the choice. 

    `Moisturizers(1)` - The number in brackets is how many product variants are in that category.

    You can link several categories to the same choice, but be careful. A product in two categories linked to the same choice gets 2 upvotes, one from each category.

    ![quiz builder standalone link categories linked](/images/manual_standalone_quizbuilder_linkcategories_linked_categories.png)

    To remove a linked category click `x` next to the category name.

    `excluded collections` - Opens the dropdown which lets you exclude categories of products from a choice.

    ![quiz builder link cocategories exclude](/images/manual_standalone_quizbuilder_linkcategories_excludecategories.png)

    Be careful with exclusions. Once a category is excluded from a choice, its products never show on the results page. This applies even if another choice upvoted them.

    **Missing categories, or categories showing (0) products?** - You may need to run a [Catalog Sync](/how-to-guides/sync-catalog/) to update the app.

    !!! tip

        You can also use custom fields as tags. See [BigCommerce: Use Custom Fields as Tags](/how-to-guides/use-custom-fields-as-tags/).

=== "Standalone"

    ![quiz builder standalone link categories](/images/manual_standalone_quizbuilder_linkcategories.png)

    In the Link Categories tab, you can link entire categories of products from your store to choices.

    Once a category is linked to a choice and the customer picks that choice, all the products in that category will receive 1 upvote.

    To link a category to a choice click on the white dropdown bar and start typing the name.

    ![quiz builder link categories search](/images/manual_standalone_quizbuilder_linkcategories_pickcategory.png)

    Select a category and it will be automatically added to the choice. 

    `Moisturizers(1)` - The number in brackets is how many product variants are in that category.

    You can link several categories to the same choice, but be careful. A product in two categories linked to the same choice gets 2 upvotes, one from each category.

    ![quiz builder standalone link categories linked](/images/manual_standalone_quizbuilder_linkcategories_linked_categories.png)

    To remove a linked category click `x` next to the category name.

    `excluded collections` - Opens the dropdown which lets you exclude categories of products from a choice.

    ![quiz builder link cocategories exclude](/images/manual_standalone_quizbuilder_linkcategories_excludecategories.png)

    Be careful with exclusions. Once a category is excluded from a choice, its products never show on the results page. This applies even if another choice upvoted them.

    **Missing categories, or categories showing (0) products?** - You may need to run a [Catalog Sync](/how-to-guides/sync-catalog/) to update the app.


---

← [Back to Quiz Builder](/reference/quiz-builder/)


← Previous: [Questions](/reference/quiz-builder/questions/)
Next: [Link Products](/reference/quiz-builder/link-products/) →
