---
description: "Add specific products and variants to quiz choices in RevenueHunt with upvote weighting settings."
---

# Link Products

=== "Shopify"

    To link products or product variants to choices, go to [Questions](/reference/quiz-builder/questions/), select a multiple-choice question, then a choice, and open [`Choice settings`](/reference/quiz-builder/questions/#choice-settings).

    ![Opening the Choice settings for a choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_multiplechoice_choicesettings.png)

    Choose the weight of this choice:

    `Upvotes weighting` - Sets a default weight for this choice. For example, if the weight is set to 2, every product or variant this choice upvotes receives double upvotes.

    **Upvote**

    ![The Upvotes section of the Choice settings](/images/manual_shopifyV2_linkproducts.png)

    Use the Upvotes section to choose which products or variants to link to this choice:

    `Upvotes` - Lists all the products or product variants linked to this choice.

    ![The list of upvoted items for a choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotemain.png)

    `+ Add upvote type` - Click to choose what to upvote. For this page, pick `Products` or `Product variants`. A new section then opens, where you pick items from your Shopify catalog. The menu also offers `Collections`, `Tags`, `Variants` and `Vendors`, covered in [Link Collections](/reference/quiz-builder/link-collections/).

    ![The Add upvote type menu](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedropdown.png)

    Toggle the products or variants to be upvoted to add them to the upvoted list.

    ![Toggling products on to link them to a choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproducts.png)

    Upvoted products or variants are listed in the upvoted section.

    ![Upvoted products listed under the choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_upvotedproductsall.png)

    **Exclude**

    ![The Exclude section of the Choice settings](/images/manual_shopifyV2_excludeproducts.png)

    Use the Exclude section to choose which products or variants to exclude from this choice:

    `Exclude` - Lists all the products or product variants excluded in this choice.

    ![The list of excluded items for a choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludemain.png)

    `+ Add exclude type` - Click to choose what to exclude. It offers the same six types as `+ Add upvote type`. A new section then opens, where you pick items from your Shopify catalog.

    ![The Add exclude type menu](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedropdown.png)

    Toggle the products or variants to be excluded to add them to the excluded list.

    ![Toggling products on to exclude them from a choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludeproducts.png)

    Excluded products or variants are listed in the excluded section.

    ![Excluded products listed under the choice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_excludedproductsall.png)

    !!! warning "Be careful with exclusions"

        Once a product is excluded from a choice, it never shows on the results page, even if another choice upvoted it.

    !!! info "Missing products?"

        Run a [catalog sync](/how-to-guides/sync-catalog/) to bring new products and variants into the app.

=== "Shopify (Legacy)"

    ![The Link Products tab in the legacy app](/images/manual_quizbuilder_linkproducts.png)

    In the Link Products tab, you can link individual product variants from your store to choices.

    Once a product variant is linked to a choice and the customer picks that choice, that product variant receives one upvote.

    To link a product to a choice, click the white dropdown bar and start typing the name.

    ![Searching for a product to link to a choice](/images/manual_quizbuilder_linkproducts_search.png)

    Select a product variant and it is added to the choice. You can link several product variants to the same choice.

    ![manual_quizbuilder_linkproducts_linked](/images/manual_quizbuilder_linkproducts_linked.png)

    To remove a linked product, click `x` next to the product name.

    `excluded products` - Opens the dropdown that lets you exclude products from a choice.

    ![manual_quizbuilder_linkproducts_exclude](/images/manual_quizbuilder_linkproducts_exclude.png)

    !!! warning "Be careful with exclusions"

        Once a product is excluded from a choice, it never shows on the results page, even if another choice upvoted it.

    !!! info "Missing products?"

        Run a [catalog sync](/how-to-guides/sync-catalog/) to bring new products and variants into the app.

=== "WooCommerce"

    ![manual_wooquizbuilder_linkproducts](/images/manual_wooquizbuilder_linkproducts.png)

    In the Link Products tab, you can link individual product variants from your store to choices.

    Once a product variant is linked to a choice and the customer picks that choice, that product variant receives one upvote.

    To link a product to a choice, click the white dropdown bar and start typing the name.

    ![manual_woo_quizbuilder_linkproducts_pickproducts](/images/manual_woo_quizbuilder_linkproducts_pickproducts.png)

    Select a product variant and it is added to the choice. You can link several product variants to the same choice.

    ![manual_woo_quizbuilder_linkproducts_linked_products](/images/manual_woo_quizbuilder_linkproducts_linked_products.png)

    To remove a linked product, click `x` next to the product name.

    `excluded products` - Opens the dropdown that lets you exclude products from a choice.

    ![manual_woo_quizbuilder_linkproducts_excludeproducts](/images/manual_woo_quizbuilder_linkproducts_excludeproducts.png)

    !!! warning "Be careful with exclusions"

        Once a product is excluded from a choice, it never shows on the results page, even if another choice upvoted it.

    !!! info "Missing products?"

        Run a [catalog sync](/how-to-guides/sync-catalog/) to bring new products and variants into the app.

=== "Magento"

    ![The Link Products tab in the legacy app](/images/manual_quizbuilder_linkproducts.png)

    In the Link Products tab, you can link individual product variants from your store to choices.

    Once a product variant is linked to a choice and the customer picks that choice, that product variant receives one upvote.

    To link a product to a choice, click the white dropdown bar and start typing the name.

    ![Searching for a product to link to a choice](/images/manual_quizbuilder_linkproducts_search.png)

    Select a product variant and it is added to the choice. You can link several product variants to the same choice.

    ![manual_quizbuilder_linkproducts_linked](/images/manual_quizbuilder_linkproducts_linked.png)

    To remove a linked product, click `x` next to the product name.

    `excluded products` - Opens the dropdown that lets you exclude products from a choice.

    ![manual_quizbuilder_linkproducts_exclude](/images/manual_quizbuilder_linkproducts_exclude.png)

    !!! warning "Be careful with exclusions"

        Once a product is excluded from a choice, it never shows on the results page, even if another choice upvoted it.

    !!! info "Missing products?"

        Run a [catalog sync](/how-to-guides/sync-catalog/) to bring new products and variants into the app.

=== "BigCommerce"

    ![The Link Products tab in the legacy app](/images/manual_quizbuilder_linkproducts.png)

    In the Link Products tab, you can link individual product variants from your store to choices.

    Once a product variant is linked to a choice and the customer picks that choice, that product variant receives one upvote.

    To link a product to a choice, click the white dropdown bar and start typing the name.

    ![Searching for a product to link to a choice](/images/manual_quizbuilder_linkproducts_search.png)

    Select a product variant and it is added to the choice. You can link several product variants to the same choice.

    ![manual_quizbuilder_linkproducts_linked](/images/manual_quizbuilder_linkproducts_linked.png)

    To remove a linked product, click `x` next to the product name.

    `excluded products` - Opens the dropdown that lets you exclude products from a choice.

    ![manual_quizbuilder_linkproducts_exclude](/images/manual_quizbuilder_linkproducts_exclude.png)

    !!! warning "Be careful with exclusions"

        Once a product is excluded from a choice, it never shows on the results page, even if another choice upvoted it.

    !!! info "Missing products?"

        Run a [catalog sync](/how-to-guides/sync-catalog/) to bring new products and variants into the app.

=== "Standalone"

    ![manual_standalone_quizbuilder_linkproducts](/images/manual_standalone_quizbuilder_linkproducts.png)

    In the Link Products tab, you can link individual product variants from your catalog to choices.

    Once a product variant is linked to a choice and the customer picks that choice, that product variant receives one upvote.

    To link a product to a choice, click the white dropdown bar and start typing the name.

    ![manual_standalone_quizbuilder_linkproducts_pickproducts](/images/manual_standalone_quizbuilder_linkproducts_pickproducts.png)

    Select a product variant and it is added to the choice. You can link several product variants to the same choice.

    ![manual_standalone_quizbuilder_linkproducts_linked_products](/images/manual_standalone_quizbuilder_linkproducts_linked_products.png)

    To remove a linked product, click `x` next to the product name.

    `excluded products` - Opens the dropdown that lets you exclude products from a choice.

    ![manual_standalone_quizbuilder_linkproducts_excludeproducts](/images/manual_standalone_quizbuilder_linkproducts_excludeproducts.png)

    !!! warning "Be careful with exclusions"

        Once a product is excluded from a choice, it never shows on the results page, even if another choice upvoted it.

    !!! info "Missing products?"

        Run a [catalog sync](/how-to-guides/sync-catalog/) to bring new products and variants into the app.

---

← [Back to Quiz Builder Index](/reference/quiz-builder/)


← Previous: [Link Collections / Link Categories](/reference/quiz-builder/link-collections/)
Next: [Customer Tags](/reference/quiz-builder/customer-tags/) →
