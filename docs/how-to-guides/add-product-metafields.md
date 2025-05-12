---
icon: material/focus-field-horizontal
---

# How to Add Product Metafields/Attributes


=== "Shopify"

    !!! note

        The app can only sync and show the custom text product metafields.

    [Metafields](https://help.shopify.com/en/manual/custom-data/metafields) in Shopify are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Metafields make this possible.

    If you're looking to import product metafields from your store into the Product Recommendation Quiz to display them on your quiz's results page, follow the steps outlined below:

=== "Shopify V2"

    !!! note

        The app can only sync and show the string, single_line_text_field, multi_line_text_field, date, and number product metafields. Rich_text_fields metafields are not currently supported.

    [Metafields](https://help.shopify.com/en/manual/custom-data/metafields) in Shopify are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Metafields make this possible.

    In Shopify V2, the process for adding and displaying metafields is streamlined. Follow the steps outlined below to import product metafields from your store into the Product Recommendation Quiz and display them on your quiz's results page:

=== "WooCommerce"

    [Attributes](https://woocommerce.com/document/managing-product-taxonomies/#product-attributes) in Woocommerce are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Attributes make this possible.

    If you're looking to import product attributes from your store into the Product Recommendation Quiz to display them on your quiz's results page, follow the steps outlined below:

## Step 1: Enable Metafields Display

=== "Shopify"

    First, enable the display of metafields for individual products:

    1. Navigate to your [Results Page Settings > Basic](/reference/quiz-builder/results-page/#basic-settings).
    2. Open the `Individual Product Settings` section.
    3. Activate the `show metafields` toggle.

    ![Enable Metafields Display](/images/how_to_add_metafields_step_1.gif)

=== "Shopify V2"

    To enable the display of metafields for individual products:

    1. Navigate to the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.
    2. Add a [product block](/reference/quiz-builder/results-page/#products-products-variants-collections) and open its settings.
    3. In the Product components layout, click `+ block`and add the `Metafield`section.
      ![Add Metafield block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_addblock.png){width=50%}
    4. From the `Select metafield` section, select the metafield you want to display.
    5. Alternatively, you can add a `Text` block to your product layout and add the metafield value manually as a [content dynamic source](/how-to-guides/use-information-recalls/) to make it part of a block of text.
    6. Save the changes with the top-right `Save` button.
    
    From now on the selcted metafiled will be dynamically displayed in the product block as part of the recommended product.


=== "WooCommerce"

    First, enable the display of attributes for individual products:

    1. Navigate to your [Results Page Settings > Basic](/reference/quiz-builder/results-page/#basic-settings).
    2. Open the `Individual Product Settings` section.
    3. Activate the `show metafields` toggle.

## Step 2: Open App Settings

=== "Shopify"

    Open [App Settings > Catalogue](/reference/app-settings/#catalogue) to access the settings to manage your catalog.

=== "Shopify V2"

    
    Not needed in Shopify V2.

=== "WooCommerce"

    Open [App Settings > Catalogue](/reference/app-settings/#catalogue) to access the settings to manage your catalog.

## Step 3: Select Metafields / Attributes

=== "Shopify"

    Select the Metafields namespaces you want to sync with the app by clicking the toggle icon next to each.

    ![Select Metafields](/images/how_to_add_metafields_step_3.gif)

=== "Shopify V2"

    Not needed in Shopify V2.

=== "WooCommerce"

    Activate the `Pass attribute information to result page` setting by clicking the toggle.

    ![how to add attributes woo step 1](/images/how_to_add_metafields_woo_step_1.png)

## Step 4: Sync the Catalog

=== "Shopify"

    Update your catalog with the new metafields by triggering a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.

=== "Shopify V2"

    If you're missing custom metafileds from the list of available metafields, you can force a catalog sync:

    1. Go to [App Settings > Catalogue](/reference/app-settings/#catalogue).
    2. Click the `Import catalogue` button to trigger a manual sync.

=== "WooCommerce"

    Update your catalog with the new attributes by triggering a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.

## Step 5: Implement Custom JavaScript on the Results Page

=== "Shopify"

    To display the metafield values on your results page, [custom JavaScript](/how-to-guides/add-javascript/) is required:

    1. Your developer will need to write custom JavaScript code to render the metafield value in the desired location on the results page.
    2. This customization falls outside the support scope of our app.

    Here's a sample code that replaces the product description with the `descriptors-subtitle` metafield. This code should be added in the [Custom JavaScript](/how-to-guides/add-javascript/) input under [Results Page Settings > Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings):

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

=== "Shopify V2"

    Not needed in Shopify V2.

=== "WooCommerce"

    To display the metafield values on your results page, [custom JavaScript](/how-to-guides/add-javascript/) is required:

    1. Your developer will need to write custom JavaScript code to render the metafield value in the desired location on the results page.
    2. This customization falls outside the support scope of our app.

    Here's a sample code that replaces the product description with the `descriptors-subtitle` metafield. This code should be added in the [Custom JavaScript](/how-to-guides/add-javascript/) input under [Results Page Settings > Advanced Settings](/reference/quiz-builder/results-page/#advanced-settings):

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

---
Following these steps will enable you to display specific metafields on your quiz's results page, enhancing your product presentations based on unique attributes or compliance needs.

 