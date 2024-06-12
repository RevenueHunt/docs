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

    1. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
    4. **Navigate to Your Site's Navigation Settings**: From your Shopify dashboard, go to `Online Store > Navigation`. Open the menu list you wish to add the quiz link to.
    5. **Add a New Menu Item**: Click on the `Add menu item` button. In the name field, type in a title for your quiz link, such as “Take Our Quiz”.
    6. **Insert the Popup Link Code**: Paste the previously copied code into the link field.
    7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.

=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
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
    2. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your `Catalog > Categories` and follow [Adobe instructions](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/navigation/navigation-top) to create a new menu level or a custom menu item. Use the link copied from the app to create this menu item.
    5. Remember to save the changes. 

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
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
    2. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your eCommerce platform Navigation Menu settings and add a new item. Paste the link copied from the app.
    5. Remember to save the changes.



## Link Popup as "Take the Quiz" Button

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/s0kxmOEz6iE?si=ZBLFAG9qXFYDXukW" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
    4.  **Navigate to Themes**: Go to `Online Store > Themes`.
    5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Paste the link to your quiz in the appropriate field.
    9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button.

=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
    2. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    3. In WordPress, go to `Pages` and find the page that corresponds to the Front Page. Click 'Edit'.
    4. In the WordPress Page Builder add a `Buttons` block. This will automatically add one button to your page builder.
    5. Edit the button text and settings, for example, write "Take the Quiz".
    6. Then, add a `Link` to the element. Under `Search or type URL` paste the code copied from the app. Accept with enter.
    7. Remember to save the changes and update the live page.
    8. From now on, whenever someone clicks on the button, a quiz popup will open.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. In your Magento dashbaord go to `Content` > `Blocks`. Click `Add New Block`.
    5. Edit the Block Title, Identifier and Store View and click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Buttons`. Drag the button onto the Row.
    8. Edit the Button Text and click the gear icon to open `button settings`.
    9. Under `Button Link` paste the link copied from the app. 
    10. Remember to save the changes.
    11. From now on, whenever someone clicks on the button, a quiz popup will open.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Find the main page.
    5. Switch to the `HTML` editor. Find the place where you want to add the button and add the following HTML code. Remember to replace the `#quiz-QUIZID` with the link copied from the app.
        ```html
        <a class="button" href="#quiz-QUIZID">Take the Quiz</a>
        ```
    6. Save the changes.
    7. From now on, whenever someone clicks on the button, a quiz popup will open.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share) section of the app, then to [`Link`](https://docs.revenuehunt.com/reference/quiz-builder/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. In your store customization options find the main page.
    5. Find the place where you want to add the button and find the button element. Add button text and paste the link copied from the app.
    6. (alternatively) Find an HTML element and add the following HTML code. Remember to replace the `#quiz-QUIZID` with the link copied from the app.
        ```html
        <a class="button" href="#quiz-QUIZID">Take the Quiz</a>
        ```
    6. Save the changes.
    7. From now on, whenever someone clicks on the button, a quiz popup will open.


## Popup Displays Behind Website Header

If the Quiz Popup displays behind your website header or the `X` closing button is not visible it's likely that your website's header has an unusually high z-index. This is not something that can be fixed from the app's end but rather from your website's end.

Here's what you can do:

- **Decrease the Z-index of your website's header.** You may need to check your theme files or contact your theme developer to do this.
- **Move the `X` closing sign lower.** You can move the `X` quiz closing sign lower on the popup with a bit of custom HTML/CSS code that can be added to your website's theme or an empty HTML/custom liquid block on the page where the quiz popup is shown. Here's a sample code:
    ```html
    <style>
    .rh-widget span {
    top: 150px !important;
    }
    </style>
    ```
- **Publish the quiz inline with a page instead.** If you don't want to make changes you can publish the quiz inline on a new page in your store. This way the quiz will be a part of it and you can link to that quiz page from other parts of your website. Check the instructions [here](https://docs.revenuehunt.com/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).



---
You've successfully set up a Quiz Link Popup on your eCommerce store. Don’t forget to click on the “Save” button so the changes are reflected in your store.