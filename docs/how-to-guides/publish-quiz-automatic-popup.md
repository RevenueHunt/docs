---
description: "Learn how to set up automatic RevenueHunt quiz popups that appear after a delay or on exit intent."
icon: material/timer-play-outline
---

# How to Set Up Automatic Popups

This article explains how to set up automatic popups on your store. It covers popups on the homepage, on a specific page and on all pages, exit intent, and how often a popup can appear.

!!! info "What is an Automatic Popup?"

    It is a quiz popup that appears after X seconds. The popup is shown only once per session, unless the `Exit Intent` option is enabled in the popup settings.

!!! warning

    Automatic popups can be very intrusive which is why, by default, they are shown only once per customer session.

!!! note "Before you start"

    Before you start, you need a quiz created with the RevenueHunt app and access to the theme editor. A basic understanding of HTML helps when you edit a theme.

    *Note: Directly editing your Shopify or other ecommerce theme's source code can potentially disrupt your store's functionality. If unsure about some steps, consider hiring a developer.*

## Auto-popup on the main page

!!! info "What is an Automatic Popup Quiz on the Main Page?"

    It is a quiz popup that appears after X seconds on the main page of your store. The popup is shown only once per session, unless the `Exit Intent` option is enabled in the popup settings.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HeHWWdbxvYI?si=yfWxXGhQEiRz6IDH" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the Built for Shopify version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Add a section for the app embed**: In the Home page Template, add the RevenueHunt `Auto Popup Quiz` app embed. The quiz popup is then enabled on the home page.

        ![how_to_shopifyv2_publish_automatic_popup_on_specific_page_embed](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_embed.png)
    3. **Configure Popup Settings**:

        ![manual_shopifyV2_quizbuilder_share_publish_automatic_options](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        - Set the `Popup Delay` (in seconds) - how long to wait before showing the popup
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
        - Set the `Quiz ID` (optional) to show a specific quiz. Leave blank to load the default.
        - Toggle `Trigger Popup on Exit Intent` if you want the popup to appear when users try to leave the page
    4. **Save Changes**: Click on the `Save` button to ensure all changes are saved before exiting the theme editor.
    5. **Test the Automatic Popup**: Open an incognito or private browsing window. A popup is shown only once per session.

    !!! note

        When a customer comes to your store, the default quiz opens automatically, based on your settings.

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

        To show a specific quiz, set the `Quiz ID` in the popup settings. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    **Option 1: Through Shopify Theme**

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/ZAK781-T1Z8?si=NAy4XjfDeisEw0w-" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID, adjust settings, and activate the toggle.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    **Option 2: Manual**

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    3. In WordPress, open `Pages` and find the Front Page. Click `Edit` to open the page.
    4. In the editor, find a `Custom HTML` element and add it to the page.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the automatic popup quiz will be visible on the main page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your Magento dashboard go to `Content` > `Blocks`. Click `Add New Block`.
    5. Edit the Block Title, Identifier and Store View and click `Edit with Page Builder`.
    6. Select `Elements` > `Rows` and drag a row into the canvas.
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app.
    10. Remember to save the changes.
    11. From now on, the automatic popup quiz will be visible on the main page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Find the main page.
    5. Switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup will be visible on the main page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the main page.
    5. Find a `Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on the main page.

## Auto-popup on a specific page

!!! info "What is an Automatic Popup Quiz on a Specific Page?"

    It is a quiz popup that appears after X seconds on a specific page of your store. The popup is shown only once per session, unless the `Exit Intent` option is enabled in the popup settings.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/0mJ4KiHQFq8?si=xWPSV0l6JDcVIcGN" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the Built for Shopify version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. **Create a new page**: Navigate to Shopify `Online Store > Pages`. Click on `Add New Page` to create a new page (e.g., `Automatic Popup Page`). Set the visibility to `Visible` and save the changes.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Create a new template**: Go to `Online Store > Themes > Customize`. Access the Homepage menu > Pages and click `+ Create a new template`. Name the template something like `Automatic Quiz Popup Template` and edit it.
    4. **Add a section for the app embed**: In the new template, add the RevenueHunt `Automatic Popup Quiz (Block)` app embed. The quiz popup is then enabled on that page.

        ![how_to_shopifyv2_publish_automatic_popup_on_specific_page_embed](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_embed.png)
    5. **Configure Popup Settings**:

        ![manual_shopifyV2_quizbuilder_share_publish_automatic_options](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        - Set the `Popup Delay` (in seconds) - how long to wait before showing the popup
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
        - Set the `Quiz ID` (optional) to show a specific quiz. Leave blank to load the default.
        - Toggle `Trigger Popup on Exit Intent` if you want the popup to appear when users try to leave the page
    6. **Save Changes**: Click on the `Save` button to ensure all changes are saved before exiting the theme editor.
    7. **Assign the template to the page**: Go to `Online Store > Pages` and select the page you created. Under `Page Template` select the template you created.

        ![how_to_shopifyv2_publish_automatic_popup_on_specific_page_template](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_template.png)
    8. **Save Changes**: Click on the `Save` button to ensure all changes are saved before exiting the theme editor.
    9. **Test the Automatic Popup**: Open an incognito or private browsing window. A popup is shown only once per session.

    !!! note

        When a customer comes to your store, the default quiz opens automatically, based on your settings.

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

        To show a specific quiz, set the `Quiz ID` in the popup settings. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    3. In WordPress, open `Pages` and find the page where you want the popup to show. Click `Edit` to open the page.
    4. In the editor, find a `Custom HTML` element and add it to the page.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the automatic popup quiz will be visible on that page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your Magento dashboard go to `Content` > `Pages`. Click `Add New Page` or open an existing page.
    5. Edit the Page and open the `Content` tab. Click `Edit with Page Builder`.
    6. Select `Elements` > `Rows` and drag a row into the canvas.
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app.
    10. Remember to save the changes.
    11. From now on, the automatic popup quiz will be visible on that page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Click `Create a Web Page` or pen an existing page.
    5. Under `Web Page Details` > `Page Content` switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on that page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the page you want the quiz to show on.
    5. Find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on that page.

## Auto-popup on all pages

!!! info "What is an Automatic Popup Quiz on All Pages?"

    It is a quiz popup that appears after X seconds on all pages of your store that have the same template/theme applied. The popup is shown only once per session, unless the `Exit Intent` option is enabled in the popup settings.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/-675UKK1uJI?si=hb4rRFFhwkk53a9p" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the Built for Shopify version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Make sure you are editing the `Default` theme for your store. Within the theme customization area, go to `App Embeds`. Look for the `Automatic Popup Quiz` option and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic.png)
    3. **Configure Popup Settings**:

        ![manual_shopifyV2_quizbuilder_share_publish_automatic_options](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        - Set the `Popup Delay` (in seconds) - how long to wait before showing the popup
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
        - Set the `Quiz ID` (optional) to show a specific quiz. Leave blank to load the default.
        - Toggle `Trigger Popup on Exit Intent` if you want the popup to appear when users try to leave the page
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.
    5. **Test the Automatic Popup**: Open an incognito or private browsing window. A popup is shown only once per session.

    The popup will now appear across all pages that have the same template/theme applied according to the configured settings.

    !!! note

        When a customer comes to your store, the default quiz opens automatically, based on your settings.

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

        To show a specific quiz, set the `Quiz ID` in the popup settings. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Edit Theme's Source Code**: Navigate to `Online Store > Themes`, click `Actions > Edit Code` to access the theme editor.
    4. **Locate and Edit File**: Find the `</body>` tag in `theme.liquid` or `footer.liquid`. Paste the popup code just before this tag.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Install a Popup Plugin**: You need a plugin that creates and manages popups, such as Popup Maker or Elementor. Install and activate it from the WordPress dashboard.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Create a New Popup**: Navigate to the popup plugin's section in your WordPress dashboard. Select the option to create a new popup. Name your popup and start designing it. Most popup plugins offer a visual editor to customize the look and layout.
    5. **Embed the Quiz**: In the popup editor, add a `custom HTML` block  and paste the code copied from the app.
    6. **Set Popup Conditions**: Configure when and where the popup should appear on your site.
    7. **Publish and Test**: After configuring your popup, publish it. Then, visit your site to ensure the popup appears as expected and that the quiz functions properly within the popup.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    1. **Find and Install a Popup Extension**: Search the Magento Marketplace for a popup extension that fits your needs. Extensions like "Magento 2 Popup Extension" by Mageplaza or similar can be used. Download and install the extension via Composer or by uploading it to your server.
    2. **Configure the Extension**: Once installed, navigate to the backend of your Magento store. Go to the extension settings via the admin panel. Here you can create a new popup and configure its settings.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Embed the Quiz**: In the popup configuration, insert the HTML or JavaScript code for your quiz. This could will be the code generated from your "Product Recommendation Quiz".
    4. **Set Display Rules**: Configure the extension to show the popup on all pages. You can also set conditions such as display timing, animation, and triggers like exit intent or time on site.
    5. **Save and Test**: Save your changes. Test the popup on your live site, on different pages and devices.

=== "BigCommerce"

    **Using Script Manager**

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    1. **Access the Script Manager**: Log into your BigCommerce admin dashboard. Navigate to `Storefront` > `Script Manager`.
    2. **Create a New Script**: Click on `Create a Script`. Fill in the details:
    - Name: Give your script a name, e.g., "Product Recommendation Quiz".
    - Location on Page: Choose Footer to ensure the script loads at the end of the page, which is typical for popups.
    - Select Pages where script will be added: Choose All Pages to ensure the popup appears throughout your site.
    3. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    4. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    5. **Insert the Popup Code**: In the Script Content area, paste the HTML code for your popup. This will include the quiz code from your quiz builder.
    6. **Save and Test**: Save your script settings. Visit your store's front end in an incognito window to ensure the popup appears correctly on all pages.

    **Modifying Theme Files**

    Alternatively, if you need more control or if the Script Manager does not meet your requirements, you can modify the theme files directly:

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Access the Theme Files**: Navigate to `Storefront` > `My Themes`. Click on `Advanced` > `Edit Theme Files`.
    4. **Modify the Footer File**: Locate the file typically named `footer.html` or similar under the `Templates` directory. Paste your popup's HTML code just before the closing </body> tag.
    5. **Save and Deploy**: Save your changes and preview them. Once confirmed, deploy the changes live.
    6. **Testing**: Clear your browser cache and check the popup functionality across different pages and devices to ensure consistent behavior.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the option to edit your store's theme.
    5. In the footer add the HTML code copied from the app. This will ensure the popup shows up on all pages in your store.
    6. Save the changes.

## FAQs

### Open a specific quiz

=== "Shopify"

    By default, an automatic popup shows the default quiz for your store.

    !!! note

        If you have set up [Shopify Markets](/reference/app-settings/#shopify-markets), the default quiz for that market is shown instead.

    To **open a specific quiz**, add a Quiz ID in the `Quiz ID (optional)` field. That field is in the `Automatic Popup Quiz` settings in the theme editor.

    ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic_settings](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.

=== "Shopify (Legacy)"

    To open a specific quiz as an automatic popup, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "WooCommerce"

    To open a specific quiz as an automatic popup, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "Magento"

    To open a specific quiz as an automatic popup, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "BigCommerce"

    To open a specific quiz as an automatic popup, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

=== "Standalone"

    To open a specific quiz as an automatic popup, generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of that quiz. Add the code to the page where you want the quiz.

### Show popup on exit intent

=== "Shopify"

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the Built for Shopify version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the `Automatic Popup Quiz` option and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic.png)
    3. **Configure Exit intent**:

        ![manual_shopifyV2_quizbuilder_share_publish_automatic_options](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        - Toggle on the `Trigger Popup on Exit Intent` option
        - Adjust other settings like `Popup Width` and `Height` as needed
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.

    The popup now appears when a customer moves the cursor to close the tab or window.

=== "Shopify (Legacy)"

    **Option 1: Through Shopify Theme**

    1. **Copy Quiz ID**: Go to your RevenueHunt [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID and activate the `Exit intent` option in your popup settings.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    **Option 2: Manual**

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    3. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

### Repeated popup displays per session

=== "Shopify"

    In the Built for Shopify version of the RevenueHunt app you cannot show the popup more than once per session. The exception is the `Exit intent` option. See [Show Popup on Exit intent](#show-popup-on-exit-intent).

=== "Shopify (Legacy)"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example:

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    5. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    6. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example:

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example:

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example:

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example:

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#auto-popup-on-the-main-page), [specific page](#auto-popup-on-a-specific-page) or [all pages](#auto-popup-on-all-pages).

### The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    !!! warning "Shopify 1.0 Theme Compatibility"
        A quiz created with the Built for Shopify version of the RevenueHunt app cannot be published on a Shopify 1.0 theme. Shopify 1.0 themes do not support app embeds, which this integration needs. App embeds are an Online Store 2.0 feature, and they let you add app functionality without touching any code. To use them, upgrade to an Online Store 2.0 theme.

    If you see the error "The quiz you are looking for does not exist" when you activate an automatic popup quiz:

    1. Check that you activated `Automatic Popup Quiz` in Online Store > Theme > Customize > `App Embeds`. Do **not** activate the legacy `Automatic Popup Quiz Legacy`.
        ![how_to_publish_shipifyV2_V1publisherrorautomaticpopup](/images/how_to_publish_shipifyV2_V1publisherrorautromaticpopup.png)

        If the wrong automatic popup quiz is activated, that error appears when you link to a Built for Shopify quiz.

        To solve this simply deactivate the `Automatic Popup Quiz Legacy` and activate the `Automatic Popup Quiz` one.
    2. Save the changes.

=== "Shopify (Legacy)"

    If you see the error "The quiz you are looking for does not exist" when you activate an automatic popup quiz:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` select the `Automatic Popup Quiz` option.
    3. Paste the Quiz ID in the `Quiz ID` field. *Note: the Quiz ID is case-sensitive.*
        ![how_to_publish_shipifyV2_V1publisherrorautomaticpopupv1](/images/how_to_publish_shipifyV2_V1publisherrorautomaticpopupv1.png)
    4. Save your changes and refresh the page.

=== "WooCommerce"

    If you see the error "The quiz you are looking for does not exist" when you activate an automatic popup quiz:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding the embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Magento"

    If you see the error "The quiz you are looking for does not exist" when you activate an automatic popup quiz:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding the embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "BigCommerce"

    If you see the error "The quiz you are looking for does not exist" when you activate an automatic popup quiz:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding the embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Standalone"

    If you see the error "The quiz you are looking for does not exist" when you activate an automatic popup quiz:

    1. Make sure you have added the embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    3. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    4. Save the changes and refresh the page.

---
By following these steps, you can enhance your ecommerce store's interactivity and user engagement through well-timed automatic popups.