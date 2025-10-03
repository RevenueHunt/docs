---
icon: material/focus-field-horizontal
---

# How to Add Product Metafields/Attributes

This article explains how to add product metafields/attributes to products on your quiz's results page.


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/BdyXTeel1WM?si=XC-LEQ5PUEvPwOUC" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! note

        The app can only sync and show the string, single_line_text_field, multi_line_text_field, date, and number product metafields. Rich_text_fields metafields are not currently supported.

    [Metafields](https://help.shopify.com/en/manual/custom-data/metafields) in Shopify are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Metafields make this possible.

    In the `💎Built for Shopify` version of the RevenueHunt app, the process for adding and displaying metafields is streamlined. Follow the steps outlined below to import product metafields from your store into the Product Recommendation Quiz and display them on your quiz's results page:

    **Step 1: Enable Metafields Display**

    To enable the display of metafields for individual products:

    1. Navigate to the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.
    2. Add a [Product block](/reference/quiz-builder/results-page/#products-products-variants-collections) and open its settings.
    3. In the [`Product components layout`](/reference/quiz-builder/results-page/#product-components-layout), click `+ block`and add the `Metafield`section.
      ![Add Metafield block](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_addblock.png){width=50%}
    4. From the `Select metafield` section, select the metafield you want to display.
    5. Alternatively, you can add a `Text` block to your product layout and add the metafield value manually as a [content dynamic source](/how-to-guides/use-information-recalls/) to make it part of a block of text. 
    6. Save the changes with the top-right `Save` button.
    
    From now on the selcted metafiled will be dynamically displayed in the product block as part of the recommended product.


    !!! tip

        If you're missing custom metafileds from the list of available metafields, you can force a catalog sync:

        1. Go to [App Settings > Catalogue](/reference/app-settings/#catalogue).
        2. Click the `Import catalogue` button to trigger a manual sync.



=== "Shopify (Legacy)"

    !!! note

        The app can only sync and show the custom text product metafields.

    [Metafields](https://help.shopify.com/en/manual/custom-data/metafields) in Shopify are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Metafields make this possible.

    If you're looking to import product metafields from your store into the Product Recommendation Quiz to display them on your quiz's results page, follow the steps outlined below:

    **Step 1: Enable Metafields Display**

    First, enable the display of metafields for individual products:

    1. Navigate to your [Results Page Settings > Basic](/reference/quiz-builder/results-page/#basic-settings).
    2. Open the `Individual Product Settings` section.
    3. Activate the `show metafields` toggle.

    ![Enable Metafields Display](/images/how_to_add_metafields_step_1.gif)

    **Step 2: Open App Settings**

    Open [App Settings > Catalogue](/reference/app-settings/#catalogue) to access the settings to manage your catalog.

    **Step 3: Select Metafields**

    Select the Metafields namespaces you want to sync with the app by clicking the toggle icon next to each.

    ![Select Metafields](/images/how_to_add_metafields_step_3.gif)

    **Step 4: Sync the Catalog**

    Update your catalog with the new metafields by triggering a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.

    **Step 5: Implement Custom JavaScript on the Results Page**

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


=== "WooCommerce"

    [Attributes](https://woocommerce.com/document/managing-product-taxonomies/#product-attributes) in Woocommerce are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Attributes make this possible.

    If you're looking to import product attributes from your store into the Product Recommendation Quiz to display them on your quiz's results page, follow the steps outlined below:

    **Step 1: Enable Attributes Display**

    First, enable the display of attributes for individual products:

    1. Navigate to your [Results Page Settings > Basic](/reference/quiz-builder/results-page/#basic-settings).
    2. Open the `Individual Product Settings` section.
    3. Activate the `show metafields` toggle.

    **Step 2: Open App Settings**

    Open [App Settings > Catalogue](/reference/app-settings/#catalogue) to access the settings to manage your catalog.

    **Step 3: Select  Attributes**

    Activate the `Pass attribute information to result page` setting by clicking the toggle.

    ![how to add attributes woo step 1](/images/how_to_add_metafields_woo_step_1.png)

    **Step 4: Sync the Catalog**

    Update your catalog with the new attributes by triggering a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.

    **Step 5: Implement Custom JavaScript on the Results Page**

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


## How to Use Metafields as Smart Collections

=== "Shopify"

    Shopify allows you to use **product metafields** as conditions when creating **smart collections**. 

    !!! info "Smart collections from metafields"

        Check official Shopify documentation for more information: [Smart collections from metafields](https://help.shopify.com/en/manual/custom-data/metafields/smart-collections).
    
    This is useful if you want to organize products by custom attributes (like `Skin Concern = Acne` or `Subscription Eligible = True`) and then connect those collections to your RevenueHunt quiz.

    !!! info "Supported Metafield Types"

        You can use the following product metafield types in smart collections:

        * Single line text
        * Single line text (list)
        * True or false (boolean)
        * Integer
        * Decimal
        * Rating

    Step by step guide:

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/53e88df6033b4c71b2834562df1f3e0f?sid=ced7456d-d8ed-4e83-8cb9-17bd31e34a86" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    1. **Create Product Metafields**: In Shopify Admin, go to `Settings → Custom data → Products`. 
    
        - Click `Add definition`.
        - Select a supported metafield type (see above) and add a clear name (e.g. `Skin Concern`, `Organic Certified`, `SPF Rating`).
        - Save the metafield definition.

    2. **Add Metafield Values to Products**: Open a product in Shopify Admin. Scroll down to the `Metafields` section. Enter the value for the metafield you created. Example: `Skin Concern = Acne`. Repeat for all relevant products.
    3. **Create a Smart Collection Using Metafields**: Go to `Products → Collections`. 
    
        - Click `Create collection`. 
        - Choose `Automated collection`. 
        - Under `Conditions`, open the field dropdown and select `Product metafields`. 
        - Select your metafield (e.g. `Skin Concern`). 
        - Define the condition (e.g. `equals → Acne`). 
        - Save the collection. Now, Shopify automatically groups products based on metafield values.
    4. **Use Smart Collections in RevenueHunt**: Open your quiz in the RevenueHunt app. Edit a question and add a Choice. Instead of linking individual products, select the Shopify collection you created. Example: Quiz answer “Acne-prone skin” → Collection `Skin Concern = Acne`. Save and publish your quiz.


=== "Shopify (Legacy)"

    Shopify allows you to use **product metafields** as conditions when creating **smart collections**. 

    !!! info "Smart collections from metafields"

        Check official Shopify documentation for more information: [Smart collections from metafields](https://help.shopify.com/en/manual/custom-data/metafields/smart-collections).
    
    This is useful if you want to organize products by custom attributes (like `Skin Concern = Acne` or `Subscription Eligible = True`) and then connect those collections to your RevenueHunt quiz.

    !!! info "Supported Metafield Types"

        You can use the following product metafield types in smart collections:

        * Single line text
        * Single line text (list)
        * True or false (boolean)
        * Integer
        * Decimal
        * Rating

    Step by step guide:

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/53e88df6033b4c71b2834562df1f3e0f?sid=ced7456d-d8ed-4e83-8cb9-17bd31e34a86" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>


    1. **Create Product Metafields**: In Shopify Admin, go to `Settings → Custom data → Products`. 
    
        - Click `Add definition`.
        - Select a supported metafield type (see above) and add a clear name (e.g. `Skin Concern`, `Organic Certified`, `SPF Rating`).
        - Save the metafield definition.

    2. **Add Metafield Values to Products**: Open a product in Shopify Admin. Scroll down to the `Metafields` section. Enter the value for the metafield you created. Example: `Skin Concern = Acne`. Repeat for all relevant products.
    3. **Create a Smart Collection Using Metafields**: Go to `Products → Collections`. 
    
        - Click `Create collection`. 
        - Choose `Automated collection`. 
        - Under `Conditions`, open the field dropdown and select `Product metafields`. 
        - Select your metafield (e.g. `Skin Concern`). 
        - Define the condition (e.g. `equals → Acne`). 
        - Save the collection. Now, Shopify automatically groups products based on metafield values.
    4. **Sync changes**: Open your quiz in the RevenueHunt app and run a quick [catalog sync](/how-to-guides/sync-catalog/). 
    5. **Link Smart Collections in RevenueHunt**: Go to the [Link Collections](/reference/quiz-builder/link-collections/) tab in the Quiz Builder and link the smart collection to a choice.
    6. Click `Publish` to save your changes.




=== "WooCommerce"

    You can use attributes as categories in the RevenueHunt app for WooCommerce.

    To do that: 

    1. Open [App Settings > Catalogue](/reference/app-settings/#catalogue) to access the settings to manage your catalog.
    2. Activate the `Use attributes as categories` setting by clicking the toggle.

      ![how to add attributes woo step 1](/images/how_to_add_metafields_woo_step_1.png)
    3. Update your catalog with the new attributes by triggering a [catalog sync](/how-to-guides/sync-catalog/) from your dashboard.
    4. Go to the [Link Collections](/reference/quiz-builder/link-collections/) tab in the Quiz Builder and link the attributes to a choice.
    5. Click `Publish` to save your changes.



---
Following these steps will enable you to display specific metafields on your quiz's results page, ensuring compliance with local regulations and improving your product presentations.
 