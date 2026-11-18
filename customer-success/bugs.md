---
icon: material/bug-outline
description: "Known bugs and limitations in RevenueHunt app with status and workarounds for reported issues."
---

# Known Bugs & Limitations

The RevenueHunt app is always improving. This page lists known bugs (unresolved issues) and current limitations (expected behavior by design).

## 🐞 Known bugs

=== "Shopify"

    These are the known bugs. The RevenueHunt team is working to fix them:

    - **Words/characters index changing while writing (scrambled text)**: Sometimes, while writing on the text inputs of the quiz builder (header, title, text block…) the words or individual characters can “lose” the index continuity and get scrambled.

        !!! note "Status"
            Under investigation.

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this happens, **contact Google Support**, because the issue is likely on their side.

    - **iPad 10th gen not scrolling properly**: Scrolling is not acting correctly on iPad10th gen (safari) navigation.

        !!! note "Status"
            Under investigation.

    - **Product Quantity Display Issue**: When a product is removed from the cart drawer, the product quantity displayed on the quiz results page is not updated accordingly.

        !!! note "Status"
            Under investigation.

    - **User Name Display Issue in Email**: Instead of showing the name of the person who completed the quiz, the email shows the question reference, for example `Hey Q2: BEFORE WE BEGIN___`.
    
        !!! note "Status"
            Under investigation.

    - **Quiz Completion Behavior**: Closing a popup quiz before finishing can cause the website background to turn white, requiring a manual refresh.

        !!! note "Status"
            Likely theme/cart conflict. Under investigation.

    - **Error on Results page**: In some cases, customers see an error when their responses are saved and they are redirected to the results page.

        !!! note "Status"
            Intermittent, under investigation.

=== "Shopify (Legacy)"

    These are the known bugs. The RevenueHunt team is working to fix them:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this happens, **contact Google Support**, because the issue is likely on their side.

    - **Thank You and Order Status Pages Script**: The script settings for these pages have been updated. Contact support to implement the latest version of the script on your Thank You and Order Status pages.
    
        !!! note "Status"
            Manual fix required. [Contact support](/how-to-guides/contact-customer-support/) to fix.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple results pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.

    - **Klaviyo Data Appended**: Recommended product data gets added to Klaviyo profile as custom properties every time a quiz is taken, the data is not replaced every time.

        !!! note "Status"
            Fixed in the Built for Shopify version of the RevenueHunt app. The fix was not added to the legacy app.

=== "WooCommerce"

    These are the known bugs. The RevenueHunt team is working to fix them:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this happens, **contact Google Support**, because the issue is likely on their side.

    - **Return Key Behavior**: When pressing the return key to make a new line on the css when on an input question, it will act as an enter on the input and move to the results page tab.

        !!! note "Status"
            Under investigation.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple results pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.

=== "Magento"

    These are the known bugs. The RevenueHunt team is working to fix them:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this happens, **contact Google Support**, because the issue is likely on their side.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple results pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.

=== "BigCommerce"

    These are the known bugs. The RevenueHunt team is working to fix them:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this happens, **contact Google Support**, because the issue is likely on their side.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple results pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.

=== "Standalone"

    These are the known bugs. The RevenueHunt team is working to fix them:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this happens, **contact Google Support**, because the issue is likely on their side.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple results pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.

## ⚖️ Current limitations (by design)

=== "Shopify"

    These are not bugs but important to know:

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Shopify Markets Integration**: Quizzes can be assigned to different markets, but merchants must configure them manually. Automatic detection per market is not yet supported.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but does not override merchant settings.

=== "Shopify (Legacy)"

    These are not bugs but important to know:

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but does not override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Quizzes cannot be assigned automatically to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.

    - **Shop Minis Deprecation**: Shopify is sunsetting Shop Minis integrations, impacting merchants who used the app within Shop.

=== "WooCommerce"

    These are not bugs but important to know:

    - **Only one product can be added to cart**: The WooCommerce API does not let the app add multiple products to the cart at once.

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but does not override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Quizzes cannot be assigned automatically to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.

=== "Magento"

    These are not bugs but important to know:

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but does not override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Quizzes cannot be assigned automatically to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.

=== "BigCommerce"

    These are not bugs but important to know:

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but does not override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Quizzes cannot be assigned automatically to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.

=== "Standalone"

    These are not bugs but important to know:

    - **Add to cart functionality is not available**: The Standalone version of the RevenueHunt app has no add to cart function. Customers can open the recommended product page and add the products to the cart from there.

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but does not override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Quizzes cannot be assigned automatically to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.

!!! info "Support"

    This page is updated as fixes roll out and limitations are lifted.

    If you find an issue that is not listed here, [contact customer support](/how-to-guides/contact-customer-support/).

---
This article explains the known bugs and limitations of the RevenueHunt app.

