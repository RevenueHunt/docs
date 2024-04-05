---
icon: material/focus-field-horizontal
---


# How to Add Product Metafields

[Metafields](https://help.shopify.com/en/manual/custom-data/metafields) in Shopify are used by stores to display specific product properties that aren't shown by default on e-commerce platforms. For instance, in Germany, it's required to show the "grundpreis" or `per 100ml` price for cosmetic products. Metafields make this possible.

If you're looking to import product metafields from your store into the Shop Quiz to display them on your quiz's results page, follow the steps outlined below:

## Step 1: Enable Metafields Display

First, enable the display of metafields for individual products:

1. Navigate to your [Results Page Settings > Basic](https://docs.revenuehunt.com/reference/quiz-builder/#basic-settings).
2. Open the `Individual Product Settings` section.
3. Activate the `show metafields` toggle.

![Enable Metafields Display](/images/how to add metafields step 1.gif)

## Step 2: Open App Settings

Open [App Settings > Catalogue](https://docs.revenuehunt.com/reference/app-settings/#catalogue) to access the settings to manage your catalog.

## Step 3: Select Metafields

Select the Metafields namespaces you want to sync with the app by clicking the toggle icon next to each.

![Select Metafields](/images/how to add metafields step 3.gif)

## Step 4: Sync the Catalog

Update your catalog with the new metafields by triggering a [catalog sync](https://docs.revenuehunt.com/how-to-guides/sync-catalog/) from your dashboard.

## Step 5: Implement Custom JavaScript on the Results Page

To display the metafield values on your results page, [custom JavaScript](https://docs.revenuehunt.com/how-to-guides/add-javascript/) is required:

1. Your developer will need to write custom JavaScript code to render the metafield value in the desired location on the results page.
2. This customization falls outside the support scope of our app.

Here's a sample code that replaces the product description with the `descriptors-subtitle` metafield. This code should be added in the [Custom JavaScript](https://docs.revenuehunt.com/how-to-guides/add-javascript/) input under [Results Page Settings > Advanced Settings](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings):

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


 