---
description: "Learn how to add products manually or import them from Google Merchant Center to your RevenueHunt Standalone app catalog."
icon: material/package-variant-plus
---

# How to Add Products in Standalone RevenueHunt App

This article explains how to add products in the Standalone version of the RevenueHunt app. Add them by hand, or import them from Google Merchant Center as a Google Product Feed XML file.

## Add products manually

=== "Shopify"

    !!! note "Not available on this platform"

        Your products come from Shopify. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "Shopify (Legacy)"

    !!! note "Not available on this platform"

        Your products come from Shopify. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Your products come from WooCommerce. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "Magento"

    !!! note "Not available on this platform"

        Your products come from Magento. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Your products come from BigCommerce. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "Standalone"

    These steps add products and collections to your quiz by hand, through the RevenueHunt catalogue.


    **Step 1: Access the Success Checklist**:

    1. In your RevenueHunt dashboard, look for any of these icons: ❓❗✅ 🔄
    2. Click on the 🔄 icon to open the Sync section of the Success Checklist

    ![Sync section of the Success Checklist](/images/manual_standalone_succcesschecklist.png){width="500"}

    **Step 2: Navigate to the Catalog**:

    1. In the Success Checklist, locate and click the `View Catalog` button
    2. The **[Catalogue](https://admin.revenuehunt.com/catalogue)** section opens, where you manage your products

    ![View Catalog button in the Success Checklist](/images/manual_standalone_succcesschecklist_products.png){width="500"}

    **Step 3: Add New Products**:

    1. In the Catalogue section, click `+ add new product`
    2. Enter a name for your new product when prompted
    3. Click `Create` to confirm
    4. Fill in all the required product details that match your ecommerce store
    5. Your changes save automatically

    ![Add new product in the Catalogue](/images/manual_standalone_succcesschecklist_catalogue_add_product.png)

    **Step 4: Create Collections**:

    1. In the Catalogue section, click `+ add new collection`
    2. Enter a name for your new collection when prompted
    3. Click `Create` to confirm
    4. Use the dropdown menu to select which existing products should be included in this collection
    5. Your changes save automatically

    ![Add new collection in the Catalogue](/images/manual_standalone_succcesschecklist_catalogue_add_collection.png)

    **Next Steps**:

    After adding your products and collections, you can:

    - [Start building your quiz](/how-to-guides/create-first-quiz/)
    - [Set up product recommendations](/how-to-guides/set-up-recommendations/)
    - [Customize your quiz design](/how-to-guides/customize-quiz-design/)

## Add products via Google Merchant Center

=== "Shopify"

    !!! note "Not available on this platform"

        Your products come from Shopify. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "Shopify (Legacy)"

    !!! note "Not available on this platform"

        Your products come from Shopify. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "WooCommerce"

    !!! note "Not available on this platform"

        Your products come from WooCommerce. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "Magento"

    !!! note "Not available on this platform"

        Your products come from Magento. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "BigCommerce"

    !!! note "Not available on this platform"

        Your products come from BigCommerce. The app imports them for you, so there is nothing to add by hand. See [How to Import Your Catalogue](/how-to-guides/sync-catalog/).

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.289308176100626%; height: 0;"><iframe src="https://www.loom.com/embed/5817998bfddb47c7a13d1adb28beeb05?sid=584e70a7-c306-407a-a76e-7b370108c0c8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    These steps import your products from Google Merchant Center into the RevenueHunt app.

    **Step 1: Access the Success Checklist**:

    1. In your RevenueHunt dashboard, look for any of these icons: ❓❗✅ 🔄
    2. Click on the 🔄 icon to open the Sync section of the Success Checklist

    ![Sync section of the Success Checklist](/images/manual_standalone_succcesschecklist.png){width="500"}

    **Step 2: Navigate to Google Product Feed**:

    1. In the Success Checklist, locate the `>activate Google Product Feed` option
    2. Click it to start connecting your Google Product Feed

    ![View Catalog button in the Success Checklist](/images/manual_standalone_succcesschecklist_products.png){width="500"}

    **Step 3: Set Up Google Product Feed**:

    1. Paste your Google Product Feed (source) URL in the `Add your Google Product Feed:` field. It should be a valid Google Product Feed link that ends with `.xml`.

        ![Google Product Feed URL field](/images/manual_standalone_succcesschecklist_productfeed.png)


        !!! warning

            Not every data source file works. It must be a **valid Google Product Feed XML file**. For the rules, see the [Google Merchant Center feed specification](https://support.google.com/merchants/answer/12631822?hl=en).


        !!! info "How do I find my Google Product Feed URL?"

            To find your Google Product Feed URL in Google Merchant Center:

            1. Log into your account at [https://merchants.google.com/](https://merchants.google.com/)
            2. Click `Products`, then `Manage product sources`.
            3. Click the name of your desired data source to open the data source settings.
            4. Under `Data source setup` check the `File URL` field and copy the URL.
            5. Paste the URL into the `File URL` field in the RevenueHunt app.
            6. Click `Save` to save the changes.

        !!! tip "Host the file somewhere public"

            You can also host the XML file somewhere public. For example:

            - Shopify (if your store is on Shopify): Go to `Settings` → `Files` in your Shopify admin. Upload `google_product_feed.xml`. Copy the URL Shopify gives you. It looks like `https://cdn.shopify.com/s/files/.../google_product_feed.xml`.

            - Your own website or hosting: Upload the file over FTP, through cPanel File Manager, or with the media upload of your CMS.

            - Cloud storage: Use Dropbox, Google Drive with a direct link, or Amazon S3. The link has to be public and end with `.xml`.

    2. Once the link is added, the app uploads your products and collections to the quiz account.


        !!! warning "Your Google Product Feed does not work?"

            First, check that your file is a valid Google Product Feed XML file, against the [Google Merchant Center feed specification](https://support.google.com/merchants/answer/12631822?hl=en).

            The [Google feed validation service](https://developers.google.com/product-review-feeds/validation/) also checks for problems.

            If the problem continues, [contact support](/how-to-guides/contact-customer-support/).


    **Next Steps**:

    After adding your products and collections, you can:

    - [Start building your quiz](/how-to-guides/create-first-quiz/)
    - [Set up product recommendations](/how-to-guides/set-up-recommendations/)
    - [Customize your quiz design](/how-to-guides/customize-quiz-design/)


---
This article explains how to add products to your quiz using the Standalone version of the RevenueHunt app. You can either add products manually or import them from Google Merchant Center.








