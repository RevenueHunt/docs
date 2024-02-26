#  How to Add Product Metafileds.

Some stores use Metafields (Shopify) to display certain product properties.

For example, in Germany, it is mandatory to display the grundpreis or “per 100ml price” for cosmetic products. Ecommerce platforms don’t show this by default, but metafields /attributes let you display it.

If you wish to import product metafields / attributes from your store into the Shop Quiz in order to display them on your quiz’s results page, you have to take the following steps:

## Step 1: Show Metafileds

Navigate to your [Results Page Settings > Basic](https://docs.revenuehunt.com/reference/quiz-builder/#basic-settings) > Individual Product Settings and activate the “show metafields” toggle.

![how to add product metafileds step 1](/images/how to add metafields step 1.gif)

## Step 2. Open Settings

Open the [App Settigns > Catalogue](https://docs.revenuehunt.com/reference/app-settings/#catalogue).

## Step 3. Choose Metafields / Attributes

Select the Metafields namespaces that you want to sync by clicking the toggle icon:

![how to add product metafileds step 3](/images/how to add metafields step 3.gif)

## Step 4. Sync the catalog

It is necessary to sync the catalog to update it with the new metafields. Check [How to run a catalog sync]() for detailed insctructions.

## Step 5. Add JavaScript to the Results Page

You’ll need to use custom JavaScript code to **render the metafield value** in the corresponding position in the results page. This has to be custom built by your developer, since it’s [out of our app’s support scope]().

Here’s a code sample which replaces the product description with the *descriptors-subtitle* metafield. It has to be added in the Custom JavaScript input, under Results Page Settings > Advanced Settings:

  window.recommendedProducts = prq.recommendedProducts();

  var products = document.querySelectorAll('.lq-product');

  for (let i = 0; i < products.length; i++) {
    let id = products[i].id;
    let oneId = id.match(/^\d/) ? ("#\\3" + id.charAt(0) + " " + id.substring(1)) : "#" + id;
    let product = window.recommendedProducts.find(product => product.id === id);


  if (product.metafields['descriptors-subtitle']) {
    let toEdit = document.querySelectorAll( oneId + ' .lq-hcont');

  for (let j = 0; j < toEdit.length; j++) {

  if (!toEdit[j].hasAttribute("edited")) {
    toEdit[j].insertAdjacentHTML('beforeend', product.metafields['descriptors-subtitle']);
  toEdit[j].setAttribute("edited", "true");
  }
  }
  }
  }

![how to add product metafileds step 5](/images/how_to_add_metafields_step5.png)

 