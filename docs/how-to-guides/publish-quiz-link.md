# How to Set Up a Quiz Link Popup on Your Store

This guide will walk you through the process of setting up a **Quiz Link Popup** on your eCommerce store. 

This feature allows your customers to access a quiz through a popup by clicking on a link within your site's navigation menu, a button, a banner or any page or blog post. It's a great way to engage visitors and collect valuable data.

Before you start, ensure you have:

- access to your eCommerce store's admin dashboard
- the necessary permissions to edit themes, pages and navigation settings

## Link Popup in Website Menu

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/V4gV44ZKu5Y?si=OgHU3u1HtToMFXfO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
    4. **Navigate to Your Site's Navigation Settings**: From your Shopify dashboard, go to `Online Store > Navigation`. Open the menu list you wish to add the quiz link to.
    5. **Add a New Menu Item**: Click on the `Add menu item` button. In the name field, type in a title for your quiz link, such as “Take Our Quiz”.
    6. **Insert the Popup Link Code**: Paste the previously copied code into the link field.
    7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.

=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link`.
    2.  Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    3. Go to the `Appearance` tab and open the `Menus`.
    4. Pick a menu and add a `Custom Link`. Paste the copied link into the `URL` section and edit the link text, for example, you can call it "Coffee Quiz".
        ![how to publish quiz woo link-popup menu](/images/how to publish quiz woo link-popup menu.png)
    5. Make sure to save the changes with the `Save Menu` button.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link`.
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your `Catalog > Categories` and follow [Adobe instructions](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/navigation/navigation-top) to create a new menu level or a custom menu item. Use the link copied from the app to create this menu item.
    5. Remember to save the changes. 

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link`.
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your `Storefront > Web Pages` menu and click `Create a Web Page`.
    5. Under `Page Type` select that This Page Will `Link to Another website or document`. 
    6. Under `Web Page Details` use the Quiz Name as `Page Name` then paste the link copied from the app in the `Link` field.
    7. Under `Navigation Menu Options` tick the box to show this web page on the navigation menu. Choose a Parent Page if you like or leave with No Parent Page.
    5. Remember to save the changes with `Save & Exit`.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link`.
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your eCommerce platform Navigation Menu settings and add a new item. Paste the link copied from the app.
    5. Remember to save the changes.



## Link Popup as "Take the Quiz" Button

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/s0kxmOEz6iE?si=ZBLFAG9qXFYDXukW" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
    4.  **Navigate to Themes**: Go to `Online Store > Themes`.
    5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Paste the link to your quiz in the appropriate field.
    9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button.

---
You've successfully set up a Quiz Link Popup on your eCommerce store. Don’t forget to click on the “Save” button so the changes are reflected in your store.