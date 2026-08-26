---
description: "Step-by-step guide to add a chat button that opens a RevenueHunt quiz popup on your ecommerce store."
icon: material/chat-outline
---

# How to Add a Quiz Popup via a Chat-Like Button on Your Store

This article explains how to add a chat button that opens the quiz. It covers both the theme-based method and the manual one.

!!! info "What is a Chat Button?"

    It is a button that opens the quiz popup when a customer clicks it.

!!! note "Before you start"

    Before you start, you need a quiz created with the RevenueHunt app and access to the theme editor.

## Chat button on the homepage

!!! info "What is a Chat Button on the Homepage?"

    It is a chat-like button that appears on the homepage of your store. Clicking it opens the quiz popup.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/WGfNlVPFA_Q?si=anpiVruoyxR8cKyy" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the `💎Built for Shopify` version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button. Make sure you are editing the `Default` theme or the theme that is applied to your main page.
    2. **Add a Section**: Then, `+ Add section`, click the `Apps`. From the list, pick the `Chat Button Quiz`.

        ![manual_shopifyv2_pagelevel_chat_add](/images/manual_shopifyv2_pagelevel_chat_add.png)
    3. **Configure Popup Settings**:

        ![manual_shopifyV2_quizbuilder_share_publish_chat_options](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

        - Adjust the chat `color`, the icon and the chat position
        - Add a `greetings message`
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
        - Set the `Popup Delay` (in seconds) - how long to wait before showing the popup
        - Set the `Quiz ID` (optional) to show a specific quiz. Leave blank to load the default.
        - Toggle `Trigger Popup on Exit Intent` if you want the popup to appear when users try to leave the page
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.

    !!! note

        When a customer comes to your store, the default quiz opens automatically, based on your settings.

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

        To show a specific quiz, set the `Quiz ID` in the popup settings. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    ### Option 1: through the Shopify theme

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/oQyIiA2GwjY?si=X5Pd4YUR5O-sby3u" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed the Chat Button Quiz**: Select `Chat Button Quiz` from the list.
    4. **Customize the Chat Button**: Enter your Quiz ID into the appropriate field. Adjust the chat button settings as needed. Activate the chat button by toggling it on.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    ### Option 2: manual

    1. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code. paste this code into the HTML of your desired pages.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

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
        Without it, the quiz does not load on your website.
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
        Without it, the quiz does not load on your website.
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
        Without it, the quiz does not load on your website.
    2. **Obtain Chat Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code. Copy the code.
    4. In your store customization options find the main page.
    5. Find a `Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the chat icon popup quiz will be visible on the main page.

## Chat button on all pages

!!! info "What is a Chat Button on All Pages?"

    It is a chat-like button that appears on all pages of your store. Clicking it opens the quiz popup.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/RM0MySN9PUU?si=wtcWwFSvN25coodT" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the `💎Built for Shopify` version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Edit the `Default` theme, or the theme applied to most of your pages. In the theme customization area, go to `App Embeds`. Find `Chat Popup Quiz` and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_chat.png)
    3. **Configure Popup Settings**:

        ![manual_shopifyV2_quizbuilder_share_publish_chat_options](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

        - Adjust the chat `color`, the icon and the chat position
        - Add a `greetings message`
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Quiz ID` (optional) to show a specific quiz. Leave blank to load the default.
        - Set the `Popup z-index` to control layering with other elements
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.

    !!! note

        When a customer comes to your store, the default quiz opens automatically, based on your settings.

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

        To show a specific quiz, set the `Quiz ID` in the popup settings. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    To show the chat button across your whole store, follow [Option 2: manual](#option-2-manual). Insert the code before the `</body>` closing tag in your theme.

=== "WooCommerce"

    To show the chat button across your whole store, follow [Option 2: manual](#option-2-manual). Insert the code before the `</body>` closing tag in your theme.

=== "Magento"

    To show the chat button across your whole store, follow [Option 2: manual](#option-2-manual). Insert the code before the `</body>` closing tag in your theme.

=== "BigCommerce"

    To show the chat button across your whole store, follow [Option 2: manual](#option-2-manual). Insert the code before the `</body>` closing tag in your theme.

=== "Standalone"

    To show the chat button across your whole store, follow [Option 2: manual](#option-2-manual). Insert the code before the `</body>` closing tag in your theme.

## Chat button on a specific page

!!! info "What is a Chat Button on a Specific Page?"

    It is a chat-like button that appears on a specific page of your store. Clicking it opens the quiz popup.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/rbweJaslzvo?si=0EZZDjAhO8FfQt3R" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the `💎Built for Shopify` version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. In Shopify, go to `Online Theme > Customize`. From the `Home page` menu at the top, go to `Pages`. Click the page template you want the chat popup on, or create a new one.
    2. Then, `+ Add section`, click the `Apps`. From the list, pick the `Chat Button Quiz`.

        ![manual_shopifyv2_pagelevel_chat_add](/images/manual_shopifyv2_pagelevel_chat_add.png)

    3. You can adjust the chat button options:

        ![manual_shopifyv2_pagelevel_chat_added](/images/manual_shopifyv2_pagelevel_chat_added.png)

        ![manual_shopifyV2_quizbuilder_share_publish_chat_options](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

        `Chat Button Color` - Adjust the color of the chat button by selecting one from the tool or adding a #color.

        `Chat Icon Color` - Adjust the color of the chat icon by selecting one from the tool or adding a #color.

        `Hide after quiz completion` - Hide the chat button after the customer reaches the results page. Toggle to activate.

        `Show notification dot` - Show the small red notification dot on the chat icon. Toggle to activate.

        `Greeting message` - Show and edit the greeting message displayed next to the chat icon. Leave it empty to hide

        `Quiz ID (optional)` - Enter a quiz ID to show a specific quiz. Leave blank to load the default.

    4. Click on `Save` to save the changes. From now on, the chat popup will show up on that page or any page that uses the same template.
    5. Remember to apply the new page template to the page you want to add the chat popup to. To add a new page to your store go to `Online Store > Pages` and click on `+ Add Page`. In the page template section select the template you created, set the visibility to `Visible` and click on `Save`.

    !!! note

        When a customer comes to your store, the default quiz opens automatically, based on your settings.

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

        To show a specific quiz, set the `Quiz ID` in the popup settings. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Obtain Chat Button Embed Code**: From the quiz builder, click `Share`, select `Chat button` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code.
    3. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

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
        Without it, the quiz does not load on your website.
    2. **Obtain Chat Button Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your Magento dashboard go to `Content` > `Pages`. Click `Add New Page` or open an existing page.
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
        Without it, the quiz does not load on your website.
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
        Without it, the quiz does not load on your website.
    2. **Obtain Chat Button Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Chat button`](/reference/quiz-builder/share-publish/#chat) mode.
    3. **Generate Popup Code**: Adjust settings like color, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the page you want the quiz to show on.
    5. Find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the chat button will be visible on that page.

## FAQs

### Open a specific quiz

=== "Shopify"

    By default, a chat button shows the default quiz for your store.

    !!! note

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

    To **open a specific quiz**, add a Quiz ID in the `Quiz ID (optional)` field. That field is in the `Chat Button Quiz` settings in the theme editor.

    ![manual_shopifyV2_quizbuilder_share_publish_chat_options](/images/manual_shopifyV2_quizbuilder_share_publish_chat_options.png)

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.

=== "Shopify (Legacy)"

    To open a specific quiz as a chat button, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "WooCommerce"

    To open a specific quiz as a chat button, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "Magento"

    To open a specific quiz as a chat button, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "BigCommerce"

    To open a specific quiz as a chat button, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "Standalone"

    To open a specific quiz as a chat button, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

### The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the `💎Built for Shopify` version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    If you see the error "The quiz you are looking for does not exist" when you activate a chat button quiz:

    1. Check that you activated `Chat Button Quiz` in Online Store > Theme > Customize > `App Embeds`. Do **not** activate the legacy `Chat Button Quiz Legacy`.
        ![how_to_publish_shipifyV2_V1publisherrorchatbutton](/images/how_to_publish_shipifyV2_V1publisherrorchatpopup.png)

        If the wrong chat button quiz is activated, that error appears when you link to a `💎Built for Shopify` quiz.

        To solve this simply deactivate the `Chat Button Quiz Legacy` and activate the `Chat Button Quiz` one.
    2. Save the changes.

=== "Shopify (Legacy)"

    If you see the error "The quiz you are looking for does not exist" when you activate a chat button quiz:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` select the `Chat Button Quiz` option.
    3. Paste the Quiz ID in the `Quiz ID` field. *Note: the Quiz ID is case-sensitive.*
        ![how_to_publish_shipifyV2_V1publisherrorchatbutton](/images/how_to_publish_shipifyV2_V1publisherrorchatv1.png)
    4. Save your changes and refresh the page.

=== "WooCommerce"

    If you see the error "The quiz you are looking for does not exist" when you activate a chat button quiz:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Magento"

    If you see the error "The quiz you are looking for does not exist" when you activate a chat button quiz:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "BigCommerce"

    If you see the error "The quiz you are looking for does not exist" when you activate a chat button quiz:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Standalone"

    If you see the error "The quiz you are looking for does not exist" when you activate a chat button quiz:

    1. Make sure you have added our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    3. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    4. Save the changes and refresh the page.

---
By following these instructions, you can successfully add a chat-like button to your Shopify/ecommerce store that opens a quiz popup.
