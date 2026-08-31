---
description: "Step-by-step guide to add product metafields and attributes to your RevenueHunt quiz results page for enhanced product information display."
icon: material/focus-field-horizontal
---

# How to Add Product Metafields/Attributes

A metafield, called an attribute in some stores, holds a product property your store does not show by default. This article explains how to put one on the quiz results page, and how to build collections from metafield values.

## Show a metafield on the results page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/BdyXTeel1WM?si=XC-LEQ5PUEvPwOUC" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    [Metafields](https://help.shopify.com/en/manual/custom-data/metafields) hold product properties that a storefront does not show by default. A cosmetic product sold in Germany, for example, has to show the "Grundpreis", the `per 100ml` price.

    !!! warning "The metafield needs Storefront API access"

        Open the metafield definition in Shopify and make it readable through the Storefront API. Without that, the live quiz cannot read the value.

    !!! note "What the app can read"

        The app syncs and shows `string`, `single_line_text_field`, `multi_line_text_field`, `date` and `number` metafields. `rich_text_field` is not supported.

        Inside a variant slot, a metafield block shows the parent product's metafield, not a variant-level one.

    1. **Open the [Results page](/reference/quiz-builder/results-page/) tab in the Quiz builder.**

    2. **Add a [Product block](/reference/quiz-builder/results-page/#product-product-variants-collections) and open its settings.**

    3. **In [`Product components layout`](/reference/quiz-builder/results-page/#slot-item-composition), click `+ block` and add `Metafield`.**

        ![Add Metafield block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

        ![Add Metafield block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon2.png)

    4. **Pick the metafield under `Select metafield`.**

        ![Add Metafield block](/images/howto_shopifyv2_add_metafileds_selectmetafield.png)

    5. **Click the top-right `Save` button.**

    The metafield then shows in the product block, alongside the rest of the product.

    !!! tip "Put the value inside a sentence of your own"

        Add a `Text` block to the product layout, and insert the metafield as a [content dynamic source](/how-to-guides/use-information-recalls/).

        ![Add Metafield block](/images/howto_shopifyv2_add_metafileds_text_adddynamicsourcemetafiled.png)

    !!! tip "A metafield missing from the list"

        Force a catalog sync. Open [App settings > Catalog](/reference/app-settings/#catalog) and click `Import catalog`.

    !!! info "A unit price needs no metafield"

        `Unit price` is a setting of its own, under [Slot item composition](/reference/quiz-builder/results-page/#slot-item-composition).

=== "Shopify (Legacy)"

    [Metafields](https://help.shopify.com/en/manual/custom-data/metafields) hold product properties that a storefront does not show by default. A cosmetic product sold in Germany, for example, has to show the "Grundpreis", the `per 100ml` price.

    !!! note "What the app can read"

        This version syncs and shows custom text metafields only.

    1. **Go to [Results Page Settings > Basic](/reference/quiz-builder/results-page/#basic-settings).**

    2. **Open `Individual Product Settings` and turn on the `show metafields` toggle.**

        ![Enable Metafields Display](/images/how_to_add_metafields_step_1.gif)

    3. **Open [App Settings > Catalogue](/reference/app-settings/#catalog).**

    4. **Turn on the toggle beside every metafield namespace you want to sync.**

        ![Select Metafields](/images/how_to_add_metafields_step_3.gif)

    5. **Run a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.**

    6. **Ask your developer to render the metafield with [custom JavaScript](/how-to-guides/add-javascript/).** Nothing appears on the results page until they do.

        !!! warning "Outside the support scope"

            This version does not place the values on the results page for you, and the code that does it is not covered by app support.

        The sample below appends the `descriptors-subtitle` value to each recommended product. It goes in the [Custom JavaScript](/how-to-guides/add-javascript/) field, under [Results Page Settings > Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).

        ```javascript
        window.recommendedProducts = prq.recommendedProducts();
        var products = document.querySelectorAll('.lq-product');

        for (let i = 0; i < products.length; i++) {
          let id = products[i].id;
          let oneId = id.match(/^\d/) ? ("#\\3" + id.charAt(0) + " " + id.substring(1)) : "#" + id;
          let product = window.recommendedProducts.find(product => product.id === id);

          if (product.metafields['descriptors-subtitle']) {
            let toEdit = document.querySelectorAll(oneId + ' .lq-hcont');

            for (let j = 0; j < toEdit.length; j++) {
              if (!toEdit[j].hasAttribute("edited")) {
                toEdit[j].insertAdjacentHTML('beforeend', '<span>' + product.metafields['descriptors-subtitle'] + '</span>');
                toEdit[j].setAttribute("edited", "true");
              }
            }
          }
        }
        ```

        ![Implement Custom JavaScript](/images/how_to_add_metafields_step5.png)

=== "WooCommerce"

    [Attributes](https://woocommerce.com/document/managing-product-taxonomies/#product-attributes) in WooCommerce hold product properties that a storefront does not show by default. A cosmetic product sold in Germany, for example, has to show the "Grundpreis", the `per 100ml` price.

    1. **Go to [Results Page Settings > Basic](/reference/quiz-builder/results-page/#basic-settings).**

    2. **Open `Individual Product Settings` and turn on the `show metafields` toggle.**

    3. **Open [App Settings > Catalogue](/reference/app-settings/#catalog).**

    4. **Turn on `Pass attribute information to result page`.**

        ![how to add attributes woo step 1](/images/how_to_add_metafields_woo_step_1.png)

    5. **Run a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.**

    6. **Ask your developer to render the attribute with [custom JavaScript](/how-to-guides/add-javascript/).** Nothing appears on the results page until they do.

        !!! warning "Outside the support scope"

            This version does not place the values on the results page for you, and the code that does it is not covered by app support.

        The sample below appends the `descriptors-subtitle` value to each recommended product. It goes in the [Custom JavaScript](/how-to-guides/add-javascript/) field, under [Results Page Settings > Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings).

        ```javascript
        window.recommendedProducts = prq.recommendedProducts();
        var products = document.querySelectorAll('.lq-product');

        for (let i = 0; i < products.length; i++) {
          let id = products[i].id;
          let oneId = id.match(/^\d/) ? ("#\\3" + id.charAt(0) + " " + id.substring(1)) : "#" + id;
          let product = window.recommendedProducts.find(product => product.id === id);

          if (product.metafields['descriptors-subtitle']) {
            let toEdit = document.querySelectorAll(oneId + ' .lq-hcont');

            for (let j = 0; j < toEdit.length; j++) {
              if (!toEdit[j].hasAttribute("edited")) {
                toEdit[j].insertAdjacentHTML('beforeend', '<span>' + product.metafields['descriptors-subtitle'] + '</span>');
                toEdit[j].setAttribute("edited", "true");
              }
            }
          }
        }
        ```

        ![Implement Custom JavaScript](/images/how_to_add_metafields_step5.png)

=== "Magento"

    !!! note "Not available on this platform"

        This version of the app does not import product attributes, so they cannot be shown on the results page.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version of the app does not import product custom fields, so they cannot be shown on the results page.

=== "Standalone"

    !!! note "Not available on this platform"

        This version has no store to import metafields from. Add the product details you need straight into the [Catalogue](https://admin.revenuehunt.com/catalogue), as [How to Add Products in Standalone RevenueHunt App](/how-to-guides/add-products-gpf/) describes.

## Use metafields as smart collections

=== "Shopify"

    Shopify can use a product metafield as the condition of a smart collection. Group products by a property such as `Skin Concern = Acne` or `Subscription Eligible = True`, then point a quiz choice at the collection.

    !!! info "Metafield types a smart collection accepts"

        - Single line text
        - Single line text (list)
        - True or false (boolean)
        - Integer
        - Decimal
        - Rating

        See the Shopify documentation on [smart collections from metafields](https://help.shopify.com/en/manual/custom-data/metafields/smart-collections).

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/53e88df6033b4c71b2834562df1f3e0f?sid=ced7456d-d8ed-4e83-8cb9-17bd31e34a86" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **In your Shopify admin, go to `Settings > Custom data > Products` and click `Add definition`.** Pick one of the types above and give it a clear name, such as `Skin Concern`, `Organic Certified` or `SPF Rating`.

    2. **Open a product, scroll to `Metafields`, and fill the value in.** For example `Skin Concern = Acne`. Repeat for every product it applies to.

    3. **Go to `Products > Collections` and click `Create collection`.**

    4. **Choose `Automated collection`.**

    5. **Under `Conditions`, select `Product metafields`, pick your metafield, and set the test.** For example `Skin Concern` `equals` `Acne`.

    6. **Save the collection.** Shopify now keeps it up to date as products change.

    7. **Open your quiz, edit a question and add a choice.**

    8. **Link the new collection to that choice, instead of picking products one by one.** An answer of `Acne-prone skin` then points at the `Skin Concern = Acne` collection.

    9. **Click the top-right `Save` button.**

=== "Shopify (Legacy)"

    Shopify can use a product metafield as the condition of a smart collection. Group products by a property such as `Skin Concern = Acne` or `Subscription Eligible = True`, then point a quiz choice at the collection.

    !!! info "Metafield types a smart collection accepts"

        - Single line text
        - Single line text (list)
        - True or false (boolean)
        - Integer
        - Decimal
        - Rating

        See the Shopify documentation on [smart collections from metafields](https://help.shopify.com/en/manual/custom-data/metafields/smart-collections).

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/53e88df6033b4c71b2834562df1f3e0f?sid=ced7456d-d8ed-4e83-8cb9-17bd31e34a86" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **In your Shopify admin, go to `Settings > Custom data > Products` and click `Add definition`.** Pick one of the types above and give it a clear name, such as `Skin Concern`, `Organic Certified` or `SPF Rating`.

    2. **Open a product, scroll to `Metafields`, and fill the value in.** For example `Skin Concern = Acne`. Repeat for every product it applies to.

    3. **Go to `Products > Collections` and click `Create collection`.**

    4. **Choose `Automated collection`.**

    5. **Under `Conditions`, select `Product metafields`, pick your metafield, and set the test.** For example `Skin Concern` `equals` `Acne`.

    6. **Save the collection.** Shopify now keeps it up to date as products change.

    7. **Run a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.**

    8. **Open the [Link Collections](/reference/quiz-builder/link-collections/) tab in the Quiz Builder and link the collection to a choice.**

    9. **Click the top-right `Publish` button.**

=== "WooCommerce"

    A WooCommerce attribute can act as a category, so a quiz choice points at every product carrying that attribute value.

    1. **Open [App Settings > Catalogue](/reference/app-settings/#catalog).**

    2. **Turn on `Use attributes as categories`.**

        ![how to add attributes woo step 1](/images/how_to_add_metafields_woo_step_1.png)

    3. **Run a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.**

    4. **Open the [Link Categories](/reference/quiz-builder/link-collections/) tab in the Quiz Builder and link an attribute to a choice.**

    5. **Click the top-right `Publish` button.**

=== "Magento"

    !!! note "Not available on this platform"

        This version cannot build a collection from product attributes on its own.

        Create the categories you need in your store, then link them to a choice in the [Link Categories](/reference/quiz-builder/link-collections/) tab.

=== "BigCommerce"

    !!! note "Not available on this platform"

        This version cannot build a collection from product attributes on its own.

        Create the categories you need in your store, then link them to a choice in the [Link Categories](/reference/quiz-builder/link-collections/) tab.

=== "Standalone"

    !!! note "Not available on this platform"

        This version has no store to build collections from. Create them by hand in the [Catalogue](https://admin.revenuehunt.com/catalogue) instead.

---

This article explains how to show a product metafield on the quiz results page. It also covers building collections from metafield values.