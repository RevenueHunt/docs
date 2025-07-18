# How to Add a Quiz Popup via a Chat-Like Button on Your Store

Enhance your Shopify / eCommerce store's interactivity by integrating a chat-like button that triggers a quiz popup. This guide provides step-by-step instructions on how to implement this feature, offering both theme-based and manual methods.

Make sure you have:

- Access to your eCommerce store's admin dashboard.
- An existing quiz created with the RevenueHunt app.
- Familiarity with your eCommerce website theme customization options.

## Chat Button on the Homepage

=== "Shopify"

    ### Option 1: Through Shopify Theme

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/oQyIiA2GwjY?si=X5Pd4YUR5O-sby3u" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed the Chat Button Quiz**: Select `Chat Button Quiz` from the list.
    4. **Customize the Chat Button**: Enter your Quiz ID into the appropriate field. Adjust the chat button settings as needed. Activate the chat button by toggling it on.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    ### Option 2: Manual

    1. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code. paste this code into the HTML of your desired pages.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/d836e7cc0ef841f2bf1458a52161d94f?sid=ccbf7e73-3a18-4d48-9eca-e6be27d13671" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the `Chat Popup Quiz` option and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat.png)
    3. **Configure Popup Settings**: 

        ![manual_shopifyV2_quizbuilder_share_publish_chat_options](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png){width="50%"}

        - Adjust the `color` or the chat, icon, chat positon
        - Add a `greetings message`
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
        - Set the `Popup Delay` (in seconds) - how long to wait before showing the popup
        - Toggle `Trigger Popup on Exit Intent` if you want the popup to appear when users try to leave the page
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.

    When visitors come to your store, the default quiz for your store will open automatically based on your settings. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

=== "WooCommerce"

    1. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    2. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.
    3. In WordPress, open `Pages` and find the Front Page. Click `Edit` to open the page.
    4. In the editor, find a `Custom HTML` element and add it to the page.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the chat icon popup quiz will be visible on the main page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.  
    4. In your Magento dashboard go to `Content` > `Blocks`. Click `Add New Block`.
    5. Edit the Block Title, Identifier and Store View and click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the chat icon popup quiz will be visible on the main page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.  
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Find the main page.
    5. Switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the chat icon popup quiz will be visible on the main page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.  
    4. In your store customization options find the main page.
    5. Find a `Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the chat icon popup quiz will be visible on the main page.

## Chat Button on All Pages

=== "Shopify"

    If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop's theme.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/d836e7cc0ef841f2bf1458a52161d94f?sid=ccbf7e73-3a18-4d48-9eca-e6be27d13671" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the `Chat Popup Quiz` option and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat.png)
    3. **Configure Popup Settings**: 

        ![manual_shopifyV2_quizbuilder_share_publish_chat_options](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png){width="50%"}

        - Adjust the `color` or the chat, icon, chat positon
        - Add a `greetings message`
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.

    When visitors come to your store, the default quiz for your store will open automatically based on your settings. If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.   

=== "WooCommerce"

    If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop's theme.

=== "Magento"

    If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop's theme.

=== "BigCommerce"

    If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop's theme.

=== "Standalone"

    If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop's theme.


## On a Specific Page

=== "Shopify"

    1. **Obtain Chat Button Embed Code**: From the quiz builder, click `Share`, select `Chat button` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code.
    3. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "Shopify V2"

    Unfortunately, it's not possible to apply App Embeds such as Chat Button Quiz on specific page only. App Embeds are only applied site-wide. Therefore, the Chat Button Quiz (if activated) will be visible on all pages.

=== "WooCommerce"

    1. **Obtain Chat Button Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    2. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    3. In WordPress, open `Pages` and find the page where you want the popup to show. Click `Edit` to open the page.
    4. In the editor, find a `Custom HTML` element and add it to the page.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the chat button will be visible on that page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Button Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your Magento dashbaord go to `Content` > `Pages`. Click `Add New Page` or open an existing page.
    5. Edit the Page and open the `Content` tab. Click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the chat button will be visible on that page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Button Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Click `Create a Web Page` or pen an existing page.
    5. Under `Web Page Details` > `Page Content` switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the chat button will be visible on that page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Chat Button Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the page you want the quiz to show on.
    5. Find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the chat button will be visible on that page.


## The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` select the `Chat Button Quiz` option.
    3. Paste the Quiz ID in the `Quiz ID` field. *Note: the Quiz ID is case-sensitive.*
        ![how_to_publish_shipifyV2_V1publisherrorchatbutton](/images/how_to_publish_shipifyV2_V1publisherrorchatv1.png)
    4. Save your changes and refresh the page.
    
=== "Shopify V2"

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Ensure that you have activated the `Chat Button Quiz` in the  Online Store > Theme > Customize > `App Embeds` and **not** the the legacy `Chat Button Quiz Legacy`.
        ![how_to_publish_shipifyV2_V1publisherrorchatbutton](/images/how_to_publish_shipifyV2_V1publisherrorchatpopup.png)

        If a wrong chat button quiz is activated, you will see the error message "The quiz you are looking for does not exist" when trying to link to a V2 quiz. 
        
        To solve this simply deactivate the `Chat Button Quiz Legacy` and activate the `Chat Button Quiz` one. 
    2. Save the changes.

=== "WooCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Magento"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "BigCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Standalone"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an chat button popup quiz, follow these steps:

    1. Make sure you have added our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    3. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    4. Save the changes and refresh the page.   

---
By following these instructions, you can successfully add a chat-like button to your Shopify/eCommerce store that opens a quiz popup.
