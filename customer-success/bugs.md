---
icon: material/bug-outline
---


# Known Bugs & Limitations

We’re constantly improving the RevenueHunt app. Below you’ll find a list of known bugs (unresolved issues) and current limitations (expected behaviors by design).

## 🐞 Known Bugs

=== "Shopify"

    These are the known bugs that we are aware of and are working to fix:

    - **Words/characters index changing while writing (scrambled text)**: Sometimes, while writing on the text inputs of the quiz builder (header, title, text block…) the words or individual characters can “lose” the index continuity and get scrambled.

        !!! note "Status"
            Under investigation.

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

    - **iPad 10th gen not scrolling properly**: Scrolling is not acting correctly on iPad10th gen (safari) navigation.

        !!! note "Status"
            Under investigation.

    - **Product Quantity Display Issue**: When a product is removed from the cart drawer, the product quantity displayed on the quiz results page is not updated accordingly.

        !!! note "Status"
            Under investigation.


    - **User Name Display Issue in Email**: Instead of showing the name of the person who completed the quiz, it’s displaying the question reference like: "Hey Q2: BEFORE WE BEGIN___".
    
        !!! note "Status"
            Under investigation.


    - **Quiz Completion Behavior**: Closing a pop-up quiz before finishing can cause the website background to turn white, requiring a manual refresh.

        !!! note "Status"
            Likely theme/cart conflict. Under investigation.

    - **Error on Results Page**: In some cases, users encounter an error when responses are saved and they’re redirected to the results page.

        !!! note "Status"
            Intermittent, under investigation.



=== "Shopify (Legacy)"

    These are the known bugs that we are aware of and are working to fix:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

    - **Thank You and Order Status Pages Script**: The script settings for these pages have been updated. Contact support to implement the latest version of the script on your Thank You and Order Status pages.
    
        !!! note "Status"
            Manual fix required. [Contact support](/how-to-guides/contact-customer-support/) to fix.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple result pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.


    - **Klaviyo Data Appended**: Recommended product data gets added to Klaviyo profile as custom properties every time a quiz is taken, the data is not replaced every time.

        !!! note "Status"
            Fixed in Built for Shopify version of the RevenueHunt app; not backported to v1.



=== "WooCommerce"

    These are the known bugs that we are aware of and are working to fix:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

    - **Return Key Behavior**: When pressing the return key to make a new line on the css when on an input question, it will act as an enter on the input and move to the results page tab.

        !!! note "Status"
            Under investigation.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple result pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.


=== "Magento"

    These are the known bugs that we are aware of and are working to fix:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple result pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.


=== "BigCommerce"

    These are the known bugs that we are aware of and are working to fix:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple result pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.


=== "Standalone"

    These are the known bugs that we are aware of and are working to fix:

    - **GA4 Tracking**: GA4 tracking is not working properly.
    
        !!! note "Status"
            Since Google transitioned from **Universal Analytics** to **GA4**, event tracking reliability has significantly decreased. The implementation code may be correct and events may fire as expected, but GA4 can still fail to read, process, or report them accurately. 
            
            If this occurs, we recommend **contacting Google Support**, as the issue is likely on their end.

    - **Custom JavaScript on Multiple Results Pages**: Custom JavaScript code may not save properly when multiple result pages are configured. The saving works correctly when applied to the default results page.
    
        !!! note "Status"
            Under investigation.




## ⚖️ Current Limitations (By Design)

=== "Shopify"

    These are not bugs but important to know:


    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Shopify Markets Integration**: Quizzes can be assigned to different markets, but merchants must configure them manually. Automatic detection per market is not yet supported.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but doesn’t override merchant settings.



=== "Shopify (Legacy)"

    These are not bugs but important to know:


    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but doesn’t override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Can’t automatically assign quizzes to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.

    - **Shop Minis Deprecation**: Shopify is sunsetting Shop Minis integrations, impacting merchants who used the app within Shop.


=== "WooCommerce"

    These are not bugs but important to know:

    - **Only one product can be added to cart**: WooCommerce API doesn't allow us to add multiple products to the cart at once.

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but doesn’t override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Can’t automatically assign quizzes to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.



=== "Magento"

    These are not bugs but important to know:

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but doesn’t override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Can’t automatically assign quizzes to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.


=== "BigCommerce"

    These are not bugs but important to know:


    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but doesn’t override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Can’t automatically assign quizzes to different markets or currencies. Merchants had to duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.


=== "Standalone"

    These are not bugs but important to know:

    - **Add to cart functionality is not available**: Standalone version of the RevenueHunt app doesn't have the add to cart functionality. Userse can open the recommended products page and add the products to the cart from there.

    - **One Klaviyo List per Quiz**: Each quiz can only sync to a single Klaviyo list at a time. For multiple lists, segmentation must be handled inside Klaviyo.

    - **Email Delivery via AWS SES**: Emails are one-off transactional messages triggered by quiz submissions. The app does not support newsletters or recurring campaigns.

    - **Results Precision**: Recommendation accuracy depends on how merchants configure upvotes, logic, and product slots. The app provides flexibility but doesn’t override merchant settings.

    - **Single Language**: No native multi-language support. Merchants have to manually duplicate quizzes for different locales.
    
    - **No Market Assignment**: Can’t automatically assign quizzes to different markets or currencies. Merchants have to manually duplicate quizzes for different locales.

    - **Quiz Builder Performance Constraints**: Quizzes with large product catalogs or complex logic could slow down load times.





!!! info "Support"

    We’ll continue to update this page as fixes roll out or limitations are lifted.

    If you encounter an issue not listed here, please [contact our support team](/how-to-guides/contact-customer-support/).

---
This article explains the known bugs and limitations of the RevenueHunt app.







