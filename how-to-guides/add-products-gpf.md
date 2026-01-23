# How to Add Products in Standalone RevenueHunt App

This guide explains different methods to add products in the Standalone version of the RevenueHunt quiz app. You can either add products manually or import them from Google Merchant Center as a valid data source/XML file.

## Add Products Manually

This tutorial will guide you through the process of manually adding products and collections to your quiz using the RevenueHunt catalog.


**Step 1: Access the Success Checklist**: 

1. In your RevenueHunt dashboard, look for any of these icons: ❓❗✅ 🔄
2. Click on the 🔄 icon to open the Sync section of the Success Checklist

![dashboard standalone success checklist](/images/manual_standalone_succcesschecklist.png){width="500"}

**Step 2: Navigate to the Catalog**:

1. In the Success Checklist, locate and click the `View Catalog` button
2. This will open the **[Catalogue](https://admin.revenuehunt.com/catalogue)** section where you can manage your products

![dashbaord standalone success checklist products](/images/manual_standalone_succcesschecklist_products.png){width="500"}

**Step 3: Add New Products**:

1. In the Catalog section, click the `+ add new product` button
2. Enter a name for your new product when prompted
3. Click `Create` to confirm
4. Fill in all the required product details that match your eCommerce store
5. Your changes will be saved automatically

![manual_standalone_succcesschecklist_catalogue_add_product](/images/manual_standalone_succcesschecklist_catalogue_add_product.png)

**Step 4: Create Collections**:

1. In the Catalog section, click the `+ add new collection` button
2. Enter a name for your new collection when prompted
3. Click `Create` to confirm
4. Use the dropdown menu to select which existing products should be included in this collection
5. Your changes will be saved automatically

![manual_standalone_succcesschecklist_catalogue_add_collection](/images/manual_standalone_succcesschecklist_catalogue_add_collection.png)

**Next Steps**:

After adding your products and collections, you can:

- [Start building your quiz](/how-to-guides/create-first-quiz/)
- [Set up product recommendations](/how-to-guides/set-up-recommendations/)
- [Customize your quiz design](/how-to-guides/customize-quiz-design/)


## Add Products via Google Merchant Center

<div style="position: relative; padding-bottom: 56.289308176100626%; height: 0;"><iframe src="https://www.loom.com/embed/5817998bfddb47c7a13d1adb28beeb05?sid=584e70a7-c306-407a-a76e-7b370108c0c8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

This section will guide you through the process of importing your products from Google Merchant Center into your RevenueHunt quiz app.

**Step 1: Access the Success Checklist**:

1. In your RevenueHunt dashboard, look for any of these icons: ❓❗✅ 🔄
2. Click on the 🔄 icon to open the Sync section of the Success Checklist

![dashboard standalone success checklist](/images/manual_standalone_succcesschecklist.png){width="500"}

**Step 2: Navigate to Google Product Feed**:

1. In the Success Checklist, locate the `>activate Google Product Feed` option
2. Click to begin the process of connecting your Google Product Feed

![dashbaord standalone success checklist products](/images/manual_standalone_succcesschecklist_products.png){width="500"}

**Step 3: Set Up Google Product Feed**:

1. Paste your Google Product Feed (source) URL in the `Add your Google Product Feed:` field. It should be a valid Google Product Feed link that ends with `.xml`.

    ![manual_standalone_succcesschecklist_productfeed](/images/manual_standalone_succcesschecklist_productfeed.png)


    !!! warning 

        You cannot just upload any data source file to the RevenueHunt app. The file must be a **valid Google Product Feed XML file**. Check this [guide](https://support.google.com/merchants/answer/12631822?hl=en) to learn more about the best practices for creating a valid Google Product Feed.
    

    !!! info "How do I find my Google Product Feed URL?"

        To find your Google Product Feed URL in Google Merchant Center:

        1. Log into your account at [https://merchants.google.com/](https://merchants.google.com/)
        2. Click `Products`, then `Manage product sources`.
        3. Click the name of your desired data source to open the data source settings.
        4. Under `Data source setup` check the `File URL` field and copy the URL.
        5. Paste the URL into the `File URL` field in the RevenueHunt app.
        6. Click `Save` to save the changes.

    !!! tip "Host the file somewhere public"

        Alternatively, you can also host your XML file somewhere public. For example:

        - Shopify (if your store is on Shopify): Go to `Settings` → `Files` in your Shopify admin. Upload `google_product_feed.xml`. Copy the URL Shopify gives you (it will look like `https://cdn.shopify.com/s/files/.../google_product_feed.xml`).

        - Your own website / hosting: Upload the file via FTP, cPanel File Manager, or your CMS’s media upload.

        - Cloud storage: Use Dropbox, Google Drive (with direct link), or Amazon S3 — but make sure the link is public and ends with `.xml`.

2. Once the link is added, the app will automatically upload products and collections to your quiz account.


    !!! warning "Your Google Product Feed doesn't work?"

        First, make sure that your file is a valid Google Product Feed XML file. Review the Google [Documentation](https://support.google.com/merchants/answer/12631822?hl=en) guide.

        You should also try [this validation service](https://developers.google.com/product-review-feeds/validation/) to check for problems.

        If you still have issues, please [contact our support team](/how-to-guides/contact-customer-support/) and we'll be happy to help you.


**Next Steps**:

After adding your products and collections, you can:

- [Start building your quiz](/how-to-guides/create-first-quiz/)
- [Set up product recommendations](/how-to-guides/set-up-recommendations/)
- [Customize your quiz design](/how-to-guides/customize-quiz-design/)



---
This article explains how to add products to your quiz using the Standalone version of the RevenueHunt app. You can either add products manually or import them from Google Merchant Center.








