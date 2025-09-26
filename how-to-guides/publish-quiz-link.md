# How to Set Up a Quiz Link Popup on Your Store

This guide will walk you through the process of setting up a **Quiz Link Popup** on your eCommerce store. 

!!! info "What's a Link Popup?"

    Link Popup allows your customers to access a quiz through a popup by clicking on a link within your site's navigation menu, a button, a banner or any page or blog post. It's a great way to engage visitors and collect valuable data.


!!! note 
    Before you start, ensure you have a quiz created and the necessary permissions to edit themes, pages and navigation settings

=== "Shopify"

    In short, to add a link popup to your store, you need to:

    - Enable the `Link Popup Quiz` app embed in your store theme and then

    - Use `#quiz-QUIZID` as the link in the navigation menu item, a button, a banner or any page or blog post to open the quiz as a popup.

=== "Shopify V2"

    In short, to add a link popup to your store, you need to:

    - Enable the `Link Popup Quiz` app embed in your store theme and then

    - Use `#quiz` as the link in the navigation menu item, a button, a banner or any page or blog post to open the quiz as a popup.

    Link popup can be opened on every page (activate `Link Popup Quiz` in `App Embeds`) or on a specific page (add a `Link Popup Quiz` section to a page template) in your store.

=== "WooCommerce"

    In short, to add a link popup to your store, you need to:

    - Generate a link popup code from the `Share` section of the app
    
    - Paste the link in the navigation menu item, a button, a banner or any page or blog post to open the quiz as a popup.
    

=== "Magento"

    In short, to add a link popup to your store, you need to:

    - Generate a link popup code from the `Share` section of the app
    
    - Paste the link in the navigation menu item, a button, a banner or any page or blog post to open the quiz as a popup.

=== "BigCommerce"

    In short, to add a link popup to your store, you need to:

    - Generate a link popup code from the `Share` section of the app
    
    - Paste the link in the navigation menu item, a button, a banner or any page or blog post to open the quiz as a popup.

=== "Standalone"

    In short, to add a link popup to your store, you need to:

    - Generate a link popup code from the `Share` section of the app
    
    - Paste the link in the navigation menu item, a button, a banner or any page or blog post to open the quiz as a popup.


## Link Popup in Website Menu

### On Every Page

!!! info "What's a Link Popup in menu that opens on every page?"

    It's a link that will open the quiz as a popup over any page in your store when a link in the navigation menu is clicked.

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/g2Gvtsp0LGo?si=bzoClxr1kagdcocL" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz Legacy option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        ![how to publish quiz link popup app embeds](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)
    4. **Navigate to Your Site's Menus Settings**: From your Shopify dashboard, go to `Content > Menus`. Open the menu you wish to add the quiz link to.
        ![how to publish link popup shopify v2 menu](/images/how_to_publish_link_popup_shopify_v2_menu.png)
    5. **Add a New Menu Item**: Click on the `Add menu item` button. In the label field, type in a title for your quiz link, such as "Take Our Quiz".
    6. **Insert the Popup Link Code**: Paste the previously copied code into the link field and then click on `Save`.
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)
    7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.

=== "Shopify V2"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/62bc3199622c41dfae377858ffa49056?sid=8bdae408-efdc-44fb-9077-d99cccb81838" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    !!! info "Short Instructions"
    
        To add a popup link to a menu item in Shopify, activate the `Link Popup Quiz` in `App Embeds` of your theme and then simply type the `#quiz` as the link and save your changes. 
            
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)
            
        When clicked, the default quiz for your store will open. 
        
        **Note:** If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

        If you'd like a specific quiz to open instead of the default, check [this section](#open-a-specific-quiz).

    Step by step instructions:

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        ![how to publish quiz link popup app embeds](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)
    3. In `Link Popup Quiz` section, you can adjust the popup options:

        ![manual_shopifyV2_quizbuilder_share_publish_linkpopup_options](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        `Popup width (% of screen)` - Controls the width of the quiz popup window as a percentage of the user's screen width.

        `Popup height (% of screen)` - Controls the height of the quiz popup window as a percentage of the user's screen height.

        `Popup z-index` - Determines the stacking order of the quiz popup relative to other elements on the webpage.

        `Quiz ID (optional)` - Enter a quiz ID to show a specific quiz. Leave blank to load the default.

        `Manage app` - Opens the RevenueHunt dashboard with full settings and options.

    3. Click on `Save` to save the changes.
    4. **Navigate to Your Site's Menus Settings**: From your Shopify dashboard, go to `Content > Menus`. Open the menu you wish to add the quiz link to.
        ![how to publish link popup shopify v2 menu](/images/how_to_publish_link_popup_shopify_v2_menu.png)
    5. **Add a New Menu Item**: Click on the `Add menu item` button. In the label field, type in a title for your quiz link, such as "Take Our Quiz".
    6. **Insert the #quiz Code**: Type `#quiz` into the link field and then click on `Save`.
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)

        !!! warning
            Don't add the full URL into the `Link` filed. It should only contain the `#quiz` text and **not** a full URL like `http://yourwebsite.com/#quiz`.

        !!! note

            When clicked, #quiz will open the default quiz for your store. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. If you'd like a specific quiz to open instead of the default, check [this section](#open-a-specific-quiz).

    7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.


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

### On a Specific Page

!!! info "What's a Link Popup in menu that opens on a specific page?"

    It's a link that will open the quiz as a popup over a specific page **only** (or any page that carries the same template) when a link in the navigation menu is clicked.

=== "Shopify"

    With the legacy version of the RevenueHunt app for Shopify the `embed.js` script is automatically added to the whole website when you activate the `Link Popup Quiz` in `App Embeds` of your theme. Therefore, the link popup will open over any page in your store and there's no automatic way to open it over a specific page only. 
    
    
    !!! info "Add the embed.js to a specific page"

        Your developer can, however, add the following `embed.js` to a cusotm liquid or HTML element of a specific page template to open the quiz as a popup over that page only.
        
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        
        Without it, the quiz won't be loaded on your website.


=== "Shopify V2"
    
    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    Step by step instructions:

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. From the `Home page` menu on top, go to `Pages` and click on the page template you want to add the link popup to or create a new page template.
    3. Once in the page template editor, click on `+ Add section`, click the `Apps`. From the list, pick the `Link Popup Quiz`.
            ![how to publish quiz link popup app embeds](/images/manual_shopifyv2_pagelevel_linkpopup_add.png)
    4. In `Link Popup Quiz` section, you can adjust the popup options:

        ![manual_shopifyV2_quizbuilder_share_publish_linkpopup_options](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        `Popup width (% of screen)` - Controls the width of the quiz popup window as a percentage of the user's screen width.

        `Popup height (% of screen)` - Controls the height of the quiz popup window as a percentage of the user's screen height.

        `Popup z-index` - Determines the stacking order of the quiz popup relative to other elements on the webpage.

        `Quiz ID (optional)` - Enter a quiz ID to show a specific quiz. Leave blank to load the default.

        `Manage app` - Opens the RevenueHunt dashboard with full settings and options.

    5. Click on `Save` to save the changes.
    6. **Navigate to Your Site's Menus Settings**: From your Shopify dashboard, go to `Content > Menus`. Open the menu you wish to add the quiz link to.
        ![how to publish link popup shopify v2 menu](/images/how_to_publish_link_popup_shopify_v2_menu.png)
    7. **Add a New Menu Item**: Click on the `Add menu item` button. In the label field, type in a title for your quiz link, such as "Take Our Quiz".
    8. **Insert the #quiz Code**: Type `#quiz` into the link field and then click on `Save`.
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2.png)

        !!! warning
            Don't add the full URL into the `Link` filed. It should only contain the `#quiz` text and **not** a full URL like `http://yourwebsite.com/#quiz`.

        !!! note

            When clicked, #quiz will open the default quiz for your store. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. If you'd like a specific quiz to open instead of the default, check [this section](#open-a-specific-quiz).

    9. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu. From now on the quiz link in the menu will only open the quiz as a popup over the page that carries the same template.
    10. Remember to apply the new page template to the page you want to add the link popup to.

=== "WooCommerce"

    1. Add the following embed.js script to a specific page template in your store.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    2.  Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    3. Go to the `Appearance` tab and open the `Menus`.
    4. Pick a menu and add a `Custom Link`. Paste the copied link into the `URL` section and edit the link text, for example, you can call it "Coffee Quiz".
        ![how to publish quiz woo link-popup menu](/images/how_to_publish_quiz_woo_link-popup_menu.png)
    5. Make sure to save the changes with the `Save Menu` button.

=== "Magento"

    1. Add the following embed.js script to a specific page template in your store.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your `Catalog > Categories` and follow [Adobe instructions](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/navigation/navigation-top) to create a new menu level or a custom menu item. Use the link copied from the app to create this menu item.
    5. Remember to save the changes. 

=== "BigCommerce"

    1. Add the following embed.js script to a specific page template in your store.
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

    1. Add the following embed.js script to a specific page template in your store.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    3. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    4. Navigate to your eCommerce platform Navigation Menu settings and add a new item. Paste the link copied from the app.
    5. Remember to save the changes.

## Link Popup as "Take the Quiz" Button

### On Every Page

!!! info "What's a Link Popup that opens via a button on every page?"
    It's a link that will open the quiz as a popup over every page in your store when a button is clicked.

=== "Shopify"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mLms8xRzYCE?si=3I-QqmPeaeIavpHO" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz Legacy option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        	![how to publish quiz link popup app embeds](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)
    4.  **Navigate to Themes**: Go to `Online Store > Themes`.
    5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Paste the link to your quiz in the appropriate field.
    9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/eaf80c4430474a049f05089eb12186db?sid=e280e84e-bcb4-4253-a92c-26b93056dfb1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>
    
    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    !!! info "Short Instructions"
    
        To add a popup link to a button in Shopify, activate the `Link Popup Quiz` in `App Embeds` of your theme and then simply type the `#quiz` as the link and save your changes. 
            
        ![how to publish link popup shopify v2](/images/how_to_publish_link_popup_shopify_v2_button.png)
            
        When clicked, the default quiz for your store will open. 
        
        **Note:** If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. 
        
        If you'd like a specific quiz to open instead of the default, check [this section](#open-a-specific-quiz).

    Step by step instructions:

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Activate App Embeds**: Go to `Online Store > Theme > Customize`. Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
        	![how to publish quiz link popup app embeds](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)
    4.  **Navigate to Themes**: Go to `Online Store > Themes`.
    5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Type `#quiz` in the appropriate link field.
        ![how to publish link popup shopify v2 button](/images/how_to_publish_link_popup_shopify_v2_button.png)

        !!! warning
            Don't add the full URL into the `Link` filed. It should only contain the `#quiz` text and **not** a full URL like `http://yourwebsite.com/#quiz`.

        When clicked, the default quiz for your store will open. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

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


### On a Specific Page

!!! info "What's a Link Popup that opens via a button on a specific page?"
    It's a link that will open the quiz as a popup over a specific page (only) when a button is clicked.

=== "Shopify"

    With the legacy version of the RevenueHunt app for Shopify the `embed.js` script is automatically added to the whole website when you activate the `Link Popup Quiz` in `App Embeds` of your theme. Therefore, the link popup will open over any page in your store and there's no automatic way to open it over a specific page only. 
    
    
    !!! info "Add the embed.js to a specific page"

        Your developer can, however, add the following `embed.js` to a cusotm liquid or HTML element of a specific page template to open the quiz as a popup over that page only.
        
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        
        Without it, the quiz won't be loaded on your website.

=== "Shopify V2"

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    Step by step instructions:

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. From the `Home page` menu on top, go to `Pages` and click on the page template you want to add the link popup to or create a new page template.
    3. Once in the page template editor, click on `+ Add section`, click the `Apps`. From the list, pick the `Link Popup Quiz`.
            ![how to publish quiz link popup app embeds](/images/manual_shopifyv2_pagelevel_linkpopup_add.png)
    4. In `Link Popup Quiz` section, you can adjust the popup options:

        ![manual_shopifyV2_quizbuilder_share_publish_linkpopup_options](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        `Popup width (% of screen)` - Controls the width of the quiz popup window as a percentage of the user's screen width.

        `Popup height (% of screen)` - Controls the height of the quiz popup window as a percentage of the user's screen height.

        `Popup z-index` - Determines the stacking order of the quiz popup relative to other elements on the webpage.

        `Quiz ID (optional)` - Enter a quiz ID to show a specific quiz. Leave blank to load the default.

        `Manage app` - Opens the RevenueHunt dashboard with full settings and options.

    5. Click on `Save` to save the changes.
    6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
    7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
    8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Type `#quiz` in the appropriate link field.
        ![how to publish link popup shopify v2 button](/images/how_to_publish_link_popup_shopify_v2_button.png)

        !!! warning
            Don't add the full URL into the `Link` filed. It should only contain the `#quiz` text and **not** a full URL like `http://yourwebsite.com/#quiz`.

        !!! note
            When clicked, `#quiz` will open the default quiz for your store. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. If you'd like a specific quiz to open instead of the default, check [this section](#open-a-specific-quiz).

    9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button. From now on, whenever someone clicks on the button on this page or any other page that uses this template, a quiz popup will open.
    10. Remember to apply the new page template to the page you want to add the link popup to.

=== "WooCommerce"

    1. Add the following embed.js script to a specific page template in your store.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain the Popup Link Code**: Go to the [`Share`](/reference/quiz-builder/share-publish/) section of the app, then to [`Link`](/reference/quiz-builder/share-publish/#link).
    2. Edit the **Popup Options** and click on `Get the code` to copy the link provided.
    3. In WordPress, go to `Pages` and find the page that corresponds to the Front Page. Click 'Edit'.
    4. In the WordPress Page Builder add a `Buttons` block. This will automatically add one button to your page builder.
    5. Edit the button text and settings, for example, write "Take the Quiz".
    6. Then, add a `Link` to the element. Under `Search or type URL` paste the code copied from the app. Accept with enter.
    7. Remember to save the changes and update the live page.
    8. From now on, whenever someone clicks on the button, a quiz popup will open.

=== "Magento"

    1. Add the following embed.js script to a specific page template in your store.
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

    1. Add the following embed.js script to a specific page template in your store.
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

    1. Add the following embed.js script to a specific page template in your store.
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

## FAQs


### Open a Specific Quiz

=== "Shopify"

    To open a specific quiz, just **add the Quiz ID to the link** like this `#quiz-QUIZID`. 
    
    For example, `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another.

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.


=== "Shopify V2"

    By default when you use `#quiz` as the link, the default quiz for your store will open. 
    
    !!! note

        If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. 

    If instead you want to **open a specific quiz**, you need to  add a Quiz ID in the `Quiz ID (optional)` field in the `Link Popup Quiz settings` in the theme editor.

    ![manual_shopifyV2_quizbuilder_share_publish_linkpopup_options](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.

=== "WooCommerce"

    To open a specific quiz, just **add the Quiz ID to the link** like this `#quiz-QUIZID`. 
    
    For example, `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another.

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.

=== "Magento"

    To open a specific quiz, just **add the Quiz ID to the link** like this `#quiz-QUIZID`. 
    
    For example, `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another.

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.

=== "BigCommerce"

    To open a specific quiz, just **add the Quiz ID to the link** like this `#quiz-QUIZID`. 
    
    For example, `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another.

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.
        
=== "Standalone"

    To open a specific quiz, just **add the Quiz ID to the link** like this `#quiz-QUIZID`. 
    
    For example, `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another.

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.


### Popup Displays Behind Website Header

If the Quiz Popup displays behind your website header or the `X` closing button is not visible it's likely that your website's header has an unusually high z-index. This can be fixed either from the app settings or from your website's theme.

=== "Shopify"

    If the Quiz Popup displays behind your website header or the `X` closing button is not visible, try these solutions:

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

=== "Shopify V2"

    The z-index determines the order of elements on the page. If the quiz popup is behind your website header or the `X` closing button is not visible, you can try to change the z-index configuration option in the app settings.

    Here is how to change the z-index configuration option in the app settings:

    1. Go to your Shopify admin dashboard and navigate to `Online Store > Themes > Customize`.
    2. Within theme customization, go to `App Embeds` and find the `Link Popup Quiz` settings.
    3. Look for the z-index setting and increase the value (try with 1000 first, if that doesn't work, try 10000).
    4. Save your changes.

    ![z-index setting in V2 Link Popup](/images/how_to_publish_quiz_link_popup_zindex_setting.png)

    !!! note
        Setting the z-index too high might hide other elements like chat buttons. The ideal setting will depend on your specific theme's configuration.
        
    If adjusting the z-index setting doesn't solve the issue, try to **publish the quiz inline with a page instead.** Check the instructions [here](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).

=== "WooCommerce"

    If the Quiz Popup displays behind your website header or the `X` closing button is not visible, try these solutions:

    - **Decrease the Z-index of your website's header.** You may need to check your theme files or contact your theme developer to do this.
    - **Move the `X` closing sign lower.** You can move the `X` quiz closing sign lower on the popup with a bit of custom HTML/CSS code that can be added to your website's theme or an empty HTML block on the page where the quiz popup is shown. Here's a sample code:
        ```html
        <style>
        .rh-widget span {
        top: 150px !important;
        }
        </style>
        ```
    - **Publish the quiz inline with a page instead.** If you don't want to make changes you can publish the quiz inline on a new page in your store. This way the quiz will be a part of it and you can link to that quiz page from other parts of your website. Check the instructions [here](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).

=== "Magento"

    If the Quiz Popup displays behind your website header or the `X` closing button is not visible, try these solutions:

    - **Decrease the Z-index of your website's header.** You may need to check your theme files or contact your theme developer to do this.
    - **Move the `X` closing sign lower.** You can move the `X` quiz closing sign lower on the popup with a bit of custom HTML/CSS code that can be added to your website's theme. Here's a sample code:
        ```html
        <style>
        .rh-widget span {
        top: 150px !important;
        }
        </style>
        ```
    - **Publish the quiz inline with a page instead.** If you don't want to make changes you can publish the quiz inline on a new page in your store. This way the quiz will be a part of it and you can link to that quiz page from other parts of your website. Check the instructions [here](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).

=== "BigCommerce"

    If the Quiz Popup displays behind your website header or the `X` closing button is not visible, try these solutions:

    - **Decrease the Z-index of your website's header.** You may need to check your theme files or contact your theme developer to do this.
    - **Move the `X` closing sign lower.** You can move the `X` quiz closing sign lower on the popup with a bit of custom HTML/CSS code that can be added to your website's theme. Here's a sample code:
        ```html
        <style>
        .rh-widget span {
        top: 150px !important;
        }
        </style>
        ```
    - **Publish the quiz inline with a page instead.** If you don't want to make changes you can publish the quiz inline on a new page in your store. This way the quiz will be a part of it and you can link to that quiz page from other parts of your website. Check the instructions [here](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).

=== "Standalone"

    If the Quiz Popup displays behind your website header or the `X` closing button is not visible, try these solutions:

    - **Decrease the Z-index of your website's header.** You may need to check your theme files or contact your theme developer to do this.
    - **Move the `X` closing sign lower.** You can move the `X` quiz closing sign lower on the popup with a bit of custom HTML/CSS code that can be added to your website's theme. Here's a sample code:
        ```html
        <style>
        .rh-widget span {
        top: 150px !important;
        }
        </style>
        ```
    - **Publish the quiz inline with a page instead.** If you don't want to make changes you can publish the quiz inline on a new page in your store. This way the quiz will be a part of it and you can link to that quiz page from other parts of your website. Check the instructions [here](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page).



### Linking to Multiple Quizzes

In some cases, you might want to have links to different quizzes on the same page. This section explains how to set up multiple quiz links for different platforms.

=== "Shopify"

    For Shopify (V1), you can link to specific quizzes by creating different popup links for each quiz.
    
    1. Go to the [`Share`](/reference/quiz-builder/share-publish/) section for each quiz.
    2. Navigate to `Link > Show Instructions for legacy themes`.
    3. Click on `Get the code` to copy the unique link for that specific quiz.
    4. Add each unique link to different menu items, buttons, or page elements.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/b65c503f49ed4664875df3e6addd8380?sid=6d7edd43-ec04-4dfd-848e-2a7337980800" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    For Shopify V2, you can link to specific quizzes by using the format `#quiz-QUIZID` instead of just `#quiz`.

    1. **Find Your Quiz ID**: Go to the [dashboard](/reference/dashboard/) and locate the quiz you want to link to.
    2. **Copy the Quiz ID**: Click the `...` three dots next to the quiz and select "Copy Quiz ID."
       
       ![manual_shopifyV2_quizmanagementoptions](/images/manual_shopifyV2_quizmanagementoptions.png)
    
    3. **Create Your Link**: Use the format `#quiz-QUIZID` for your link. For example, if your quiz ID is "DmHLGj", your link would be `#quiz-DmHLGj`.
    
    4. **Add the Link**: Follow the same steps as described earlier for adding a link to a menu item or button, but use your specific quiz link instead of just `#quiz`.
    
    **Example use cases:**
    
    - Different quizzes for different product categories (e.g., "#quiz-ABC123" for skincare quiz, "#quiz-XYZ789" for makeup quiz)
    - A/B testing different quiz versions
    - Seasonal or promotional quizzes alongside your main quiz

    !!! example "Example"
        
        `https://yourstore.myshopify.com/#quiz-123` can open one quiz, while  `https://yourstore.myshopify.com/#quiz-456` can open another. 
            
        To find your Quiz ID, go to the [dashboard](/reference/dashboard/) and identify a quiz. Click on the `...` and copy the ID.

    !!! warning
        Don't add the full URL into the `Link` filed. It should only contain the `#quiz-QUIZID` text and **not** a full URL like `http://yourwebsite.com/#quiz-QUIZID`.

=== "WooCommerce"

    For WooCommerce, each quiz has its own unique link code:
    
    1. Go to the [`Share`](/reference/quiz-builder/share-publish/) section for each quiz you want to link to.
    2. Navigate to [`Link`](/reference/quiz-builder/share-publish/#link) and edit the **Popup Options**.
    3. Click on `Get the code` to copy the unique link for each quiz.
    4. Add these links to different menu items, buttons, or page elements as needed.

=== "Magento"

    For Magento, each quiz has its own unique link code:
    
    1. Go to the [`Share`](/reference/quiz-builder/share-publish/) section for each quiz you want to link to.
    2. Navigate to [`Link`](/reference/quiz-builder/share-publish/#link) and edit the **Popup Options**.
    3. Click on `Get the code` to copy the unique link for each quiz.
    4. Add each unique link to different menu items, buttons, or page elements.

=== "BigCommerce"

    For BigCommerce, each quiz has its own unique link code:
    
    1. Go to the [`Share`](/reference/quiz-builder/share-publish/) section for each quiz you want to link to.
    2. Navigate to [`Link`](/reference/quiz-builder/share-publish/#link) and edit the **Popup Options**.
    3. Click on `Get the code` to copy the unique link for each quiz.
    4. Add these links to different web pages, menu items, buttons, or other elements as needed.

=== "Standalone"

    For standalone implementations, each quiz has its own unique link code:
    
    1. Go to the [`Share`](/reference/quiz-builder/share-publish/) section for each quiz you want to link to.
    2. Navigate to [`Link`](/reference/quiz-builder/share-publish/#link) and edit the **Popup Options**.
    3. Click on `Get the code` to copy the unique link for each quiz.
    4. Add these links to different menu items, buttons, or page elements as needed.

### The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` section active the `Link Popup Quiz`. 
    3. Check the Quiz Link. Ensure that the link you've added to your menu or a button is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*
    4. Save your changes and refresh the page.
    
=== "Shopify V2"

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that you have activated the `Link Popup Quiz` in the  Online Store > Theme > Customize > `App Embeds` section and **not** the the legacy `Link Popup Quiz Legacy`.
        ![docs/images/how_to_publish_shipifyV2_V1publisherrorlinkpopup.png](/images/how_to_publish_shipifyV2_V1publisherrorlinkpopup.png)

        If a wrong link popup is activated, you will see the error message "The quiz you are looking for does not exist" when trying to link to a V2 quiz. 
        
        To solve this simply deactivate the `Link Popup Legacy` and activate the `Link Popup Quiz` one. Then, save the changes.
    2. Verify that the link is correctly formatted. Ensure that the link you've added to your menu or a button is correctly formatted and it follows the format `#quiz`.

=== "WooCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    3. Verify that the link is correctly formatted. Ensure that the link you've added to your menu or a button is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*        

=== "Magento"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    3. Verify that the link is correctly formatted. Ensure that the link you've added to your menu or a button is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*   

=== "BigCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    3. Verify that the link is correctly formatted. Ensure that the link you've added to your menu or a button is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*                     

=== "Standalone"

    If you see the error message "The quiz you are looking for does not exist" when trying to link to a quiz, follow these steps:

    1. Ensure you've added the following embed.js script to your website. Without it, the quiz won't be loaded on your website.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. Check that the quiz ID is correct. Go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**.
    4. Verify that the link is correctly formatted. Ensure that the link you've added to your menu or a button is correctly formatted and it follows the format `#quiz-QUIZID`. Where the Quiz ID is the ID you've copied from the Quiz Settings. *Note: the Quiz ID is case-sensitive.*   

---
This article explains how to publish a quiz created with RevenueHunt Quizzes app as a Link Popup on your website.