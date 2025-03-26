# How to Set Up a Quiz Link Popup on Your Store

This guide will walk you through the process of setting up a **Quiz Link Popup** on your eCommerce store. 

This feature allows your customers to access a quiz through a popup by clicking on a link within your site's navigation menu, a button, a banner or any page or blog post. It's a great way to engage visitors and collect valuable data.

Before you start, ensure you have:

- access to your eCommerce store's admin dashboard
- the necessary permissions to edit themes, pages and navigation settings

## Link Popup in Website Menu

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/g2Gvtsp0LGo?si=bzoClxr1kagdcocL" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        ![how to publish quiz link popup app embeds](/images/how_to_publish_quiz_link_popup_app_embeds.png)
    4. **Navigate to Your Site's Menus Settings**: From your Shopify dashboard, go to `Content > Menus`. Open the menu you wish to add the quiz link to.
        ![how to publish link popup shopify v2 menu](/images/how_to_publish_link_popup_shopify_v2_menu.png)
    5. **Add a New Menu Item**: Click on the `Add menu item` button. In the name field, type in a title for your quiz link, such as “Take Our Quiz”.
    6. **Insert the Popup Link Code**: Paste the previously copied code into the link field.
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)
    7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.

        When clicked, the default quiz for your store will open. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

=== "Shopify V2"

    With Version 2 of the RevenueHunt app, you can easily create links to open a quiz popup anywhere on your website. 
    
    To add a popup link to a menu item or button in Shopify, simply type the `#quiz` as the link and save your changes. 
        
    ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)
        
    When clicked, the default quiz for your store will open. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

    !!! note

        To link to a specific quiz, use `#quiz-QUIZID` for Version 1 quizzes or `#quizV2-QUIZID` for Version 2 quizzes. 
            Replace `QUIZID` with the quiz ID, which you can find in the [dashboard](/reference/dashboard/) by clicking the `...` three dots next to a quiz and selecting "Copy Quiz ID."

        ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)

        To directly link to a specific quiz:

        - For quizzes created with Version 1, use: #quiz-QUIZID

        - For quizzes created with Version 2, use: #quizV2-QUIZID

        Here are examples of how your links might look:

        **Popup Links**:

        ``` html
        #quiz-DmHLGj (Version 1)
        ```
            
        ``` html
        #quizV2-BfK8Ht (Version 2)
        ```

        **Direct Page Links**:

        ``` html
        www.yourstore.com/#quiz-DmHLGj
        ```

        ``` html
        www.yourstore.com/#quizV2-BfK8Ht
        ```

            These links can be added anywhere on your website to open a quiz popup.

    Step by step instructions:

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the **Link Popup V2** Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        ![how to publish quiz link popup app embeds](/images/how_to_publish_quiz_link_popup_app_embeds.png)
    4. **Navigate to Your Site's Menus Settings**: From your Shopify dashboard, go to `Content > Menus`. Open the menu you wish to add the quiz link to.
        ![how to publish link popup shopify v2 menu](/images/how_to_publish_link_popup_shopify_v2_menu.png)
    5. **Add a New Menu Item**: Click on the `Add menu item` button. In the name field, type in a title for your quiz link, such as “Take Our Quiz”.
    6. **Insert the #quiz Code**: Type `#quiz` into the link filed and accept the link.
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)

    7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.

        When clicked, the default quiz for your store will open. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    2.  Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    3. Go to the `Appearance` tab and open the `Menus`.
    4. Pick a menu and add a `Custom Link`. Paste the copied link into the `URL` section and edit the link text, for example, you can call it "Coffee Quiz".
        ![how to publish quiz woo link-popup menu](/images/how_to_publish_quiz_woo_link-popup_menu.png)
    5. Make sure to save the changes with the `Save Menu` button.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your `Catalog > Categories` and follow [Adobe instructions](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/navigation/navigation-top) to create a new menu level or a custom menu item. Use the link copied from the app to create this menu item.
    5. Remember to save the changes. 

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
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
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your eCommerce platform Navigation Menu settings and add a new item. Paste the link copied from the app.
    5. Remember to save the changes.

## Link Popup as "Take the Quiz" Button

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mLms8xRzYCE?si=3I-QqmPeaeIavpHO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        	![how to publish quiz link popup app embeds](/images/how_to_publish_quiz_link_popup_app_embeds.png)
    4.  **Navigate to Themes**: Go to `Online Store > Themes`.
    5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Paste the link to your quiz in the appropriate field.
    9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button.

=== "Shopify V2"

    With Version 2 of the RevenueHunt app, you can easily create links to open a quiz popup anywhere on your website. 
    
    To add a popup link to a menu item or button in Shopify, simply type the `#quiz` as the link and save your changes. 
        
    ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)
        
    When clicked, the default quiz for your store will open. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

    !!! note

        To link to a specific quiz, use `#quiz-QUIZID` for Version 1 quizzes or `#quizV2-QUIZID` for Version 2 quizzes. 
            Replace `QUIZID` with the quiz ID, which you can find in the [dashboard](/reference/dashboard/) by clicking the `...` three dots next to a quiz and selecting "Copy Quiz ID."

        ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)

        To directly link to a specific quiz:

        - For quizzes created with Version 1, use: #quiz-QUIZID

        - For quizzes created with Version 2, use: #quizV2-QUIZID

        Here are examples of how your links might look:

        **Popup Links**:

        ``` html
        #quiz-DmHLGj (Version 1)
        ```
            
        ``` html
        #quizV2-BfK8Ht (Version 2)
        ```

        **Direct Page Links**:

        ``` html
        www.yourstore.com/#quiz-DmHLGj
        ```

        ``` html
        www.yourstore.com/#quizV2-BfK8Ht
        ```

            These links can be added anywhere on your website to open a quiz popup.

    Step by step instructions:

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup V2 Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        	![how to publish quiz link popup app embeds](/images/how_to_publish_quiz_link_popup_app_embeds.png)
    4.  **Navigate to Themes**: Go to `Online Store > Themes`.
    5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Type `#quiz` in the appropriate link field.
        ![how to publish link popup shopify v2 button](/images/how_to_publish_link_popup_shopify_v2_button.png)

        When clicked, the default quiz for your store will open. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

    9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button.

=== "WooCommerce"

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
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
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
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
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
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
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
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
- **Publish the quiz inline with a page instead.** If you don't want to make changes you can publish the quiz inline on a new page in your store. This way the quiz will be a part of it and you can link to that quiz page from other parts of your website. Check the instructions [here](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).

---
You've successfully set up a Quiz Link Popup on your eCommerce store. Don’t forget to click on the “Save” button so the changes are reflected in your store.