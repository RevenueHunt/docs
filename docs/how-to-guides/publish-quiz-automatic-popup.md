# How to Set Up Automatic Popups

This guide walks you through setting up automatic popups on your eCommerce store, including popups that appear based on time spent on a page, across all pages, on the homepage, with exit intent, and options for showing popups multiple times per session.

!!! info "What's an Automatic Popup?"
    It's a quiz popup that appears after X seconds. The popup is shown only once per session unless `Exit Intent` option is enabled in the popup settings. Automatic popups can significantly enhance user engagement by presenting timely content or interactive elements like quizzes. 

!!! warning

    Automatic popups can be very intrusive which is why, by default, they are shown only once per customer session.

!!! note "Before you start"

    Before you start ensure you have a quiz created with the RevenueHunt app, access to the theme editor and (optional) basic understanding of HTML for editing themes.

    *Note: Directly editing your Shopify or other eCommerce theme's source code can potentially disrupt your store's functionality. If unsure about some steps, consider hiring a developer.*

## Auto-Popup on the Main Page

!!! info "What's an Automatic Popup Quiz on the Main Page?"
    It's a quiz popup that appears after X seconds on the main page of your store. The popup is shown only once per session unless `Exit Intent` option is enabled in the popup settings.

=== "Shopify"

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

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/880f7b6a3db24435a1538b87ddc56bd4?sid=2de0509f-30fc-446c-8ccd-bd657fcc66eb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Make sure you are editing the `Default` theme or the theme that is applied to the main page. Within the theme customization area, go to `App Embeds`. Look for the `Automatic Popup Quiz` option and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic.png)
    3. **Configure Popup Settings**: 

        ![manual_shopifyV2_quizbuilder_share_publish_automatic_options](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        - Set the `Popup Delay` (in seconds) - how long to wait before showing the popup
        - Adjust the `Popup Width` and `Height` (as percentage of screen)
        - Set the `Popup z-index` to control layering with other elements
        - Set the `Quiz ID` (optional) to show a specific quiz. Leave blank to load the default.
        - Toggle `Trigger Popup on Exit Intent` if you want the popup to appear when users try to leave the page
    4. **Save Changes**: Click on the `Save` button to ensure all changes are saved before exiting the theme editor.


    !!! note
        When visitors come to your store, the default quiz for your store will open automatically based on your settings. 
    
        If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

        If you want to show a specific quiz, you can do so by setting the `Quiz ID` in the popup settings. Check this [section](#open-a-specific-quiz) for more information.

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
        Without it, the quiz won't be loaded on your website.
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
        Without it, the quiz won't be loaded on your website.
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
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the main page.
    5. Find a `Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on the main page.

## Auto-Popup on a Specific Page

!!! info "What's an Automatic Popup Quiz on a Specific Page?"
    It's a quiz popup that appears after X seconds on a specifc page of your store. The popup is shown only once per session unless `Exit Intent` option is enabled in the popup settings.


=== "Shopify"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/101aaaaa8adf4eda82066581dd7e3cd7?sid=4d52599b-cb29-475d-9ecd-a1eeb813ec5d" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Create a new page**: Navigate to Shopify `Online Store > Pages`. Click on `Add New Page` to create a new page (e.g., `Automatic Pop-up Page`). Set the visibility to `Visible` and save the changes.
    2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    3. **Create a new template**: Go to `Online Store > Themes > Customize`. Access the Homepage menu > Pages and click `+ Create a new template`. Name the template something like `Automatic Quiz Pop-up Template` and edit it.
    4. **Add a section for the app embed**: In the new template, add a section for the app embed called `Automatic Pop-up Quiz (Block)` by Revenue Hunt Quizzes. This will enable the quiz pop-up on the specified page.

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

        ![how_to_shopifyv2_publish_automatic_popup_on_specific_page_tempalte](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_tempalte.png)
    8. **Save Changes**: Click on the `Save` button to ensure all changes are saved before exiting the theme editor.
    9. **Test the Automatic Pop-up**: To view the Automatic Pop-up, ensure you are in an incognito or private browsing window, as pop-ups are shown only once per user session.

    !!! note
        When visitors come to your store, the default quiz for your store will open automatically based on your settings. 
    
        If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

        If you want to show a specific quiz, you can do so by setting the `Quiz ID` in the popup settings. Check this [section](#open-a-specific-quiz) for more information.


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
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your Magento dashbaord go to `Content` > `Pages`. Click `Add New Page` or open an existing page.
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
        Without it, the quiz won't be loaded on your website.
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
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the page you want the quiz to show on.
    5. Find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on that page.

## Auto-Popup on All Pages

!!! info "What's an Automatic Popup Quiz on All Pages?"
    It's a quiz popup that appears after X seconds on all pages of your store that have the same template/theme applied. The popup is shown only once per session unless `Exit Intent` option is enabled in the popup settings.

=== "Shopify"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Edit Theme's Source Code**: Navigate to `Online Store > Themes`, click `Actions > Edit Code` to access the theme editor.
    4. **Locate and Edit File**: Find the `</body>` tag in `theme.liquid` or `footer.liquid`. Paste the popup code just before this tag.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.loom.com/embed/880f7b6a3db24435a1538b87ddc56bd4?sid=2de0509f-30fc-446c-8ccd-bd657fcc66eb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

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

    The popup will now appear across all pages that have the same template/theme applied according to the configured settings.

    !!! note
        When visitors come to your store, the default quiz for your store will open automatically based on your settings. 
    
        If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

        If you want to show a specific quiz, you can do so by setting the `Quiz ID` in the popup settings. Check this [section](#open-a-specific-quiz) for more information.


=== "WooCommerce"

    1. **Install a Popup Plugin**: First, you'll need a plugin that can create and manage popups. Popular options include 'Popup Maker' or 'Elementor' if you're looking for something with more design flexibility. Install and activate your chosen plugin through the WordPress dashboard.
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
        Without it, the quiz won't be loaded on your website.
    1. **Find and Install a Popup Extension**: Search the Magento Marketplace for a popup extension that fits your needs. Extensions like "Magento 2 Popup Extension" by Mageplaza or similar can be used. Download and install the extension via Composer or by uploading it to your server.
    2. **Configure the Extension**: Once installed, navigate to the backend of your Magento store. Go to the extension settings via the admin panel. Here you can create a new popup and configure its settings.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Embed the Quiz**: In the popup configuration, insert the HTML or JavaScript code for your quiz. This could will be the code generated from your "Product Recommendation Quiz".
    4. **Set Display Rules**: Configure the extension to show the popup on all pages. You might also set additional conditions like display timing, animation effects, and user interaction triggers (e.g., exit intent, time on site).
    5. **Save and Test**: After setting up everything, save your changes and test the popup on your live site to ensure it works correctly across different pages and devices.

=== "BigCommerce"

    **Using Script Manager**

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
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
        Without it, the quiz won't be loaded on your website.
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
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the option to edit your store's theme.
    5. In the footer add the HTML code copied from the app. This will ensure the popup shows up on all pages in your store.
    6. Save the changes.



## FAQs

### Open a Specific Quiz

=== "Shopify"

    To open a specific quiz as an automatic popup, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.
    
=== "Shopify V2"

    By default when add an automatic popup, the default quiz for your store will show. 
    
    !!! note

        If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. 

    If instead you want to **open a specific quiz**, you need to add a Quiz ID in the `Quiz ID (optional)` field in the `Automatic Popup Quiz` settings in the theme editor.

    ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic_settings](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.
    

=== "WooCommerce"

    To open a specific quiz as an automatic popup, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.

=== "Magento"

    To open a specific quiz as an automatic popup, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.

    

=== "BigCommerce"

    To open a specific quiz as an automatic popup, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.
   

=== "Standalone"

    To open a specific quiz as an automatic popup, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.

### Show Popup on Exit Intent

=== "Shopify"

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

=== "Shopify V2"


    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
    2. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the `Automatic Popup Quiz` option and toggle it on.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic.png)
    3. **Configure Exit Intent**: 

        ![manual_shopifyV2_quizbuilder_share_publish_automatic_options](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        - Toggle on the `Trigger Popup on Exit Intent` option
        - Adjust other settings like `Popup Width` and `Height` as needed
    4. **Save Changes**: Click on the Save button to ensure all changes are saved before exiting the theme editor.

    The popup will now appear when visitors show exit intent (moving cursor towards closing the tab/window).

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    3. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).      

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).  

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).      


### Repeated Popup Displays per Session

=== "Shopify"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    5. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    6. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "Shopify V2"

    It is not possible to show the popup more than once per session in Shopify V2 unless you activate the `Exit intent` option following the instructions [here](#show-popup-on-exit-intent).

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).     

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).     

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).    

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Automatic`](/reference/quiz-builder/share-publish/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).    

### The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `App Embeds` select the `Automatic Popup Quiz` option.
    3. Paste the Quiz ID in the `Quiz ID` field. *Note: the Quiz ID is case-sensitive.*
        ![how_to_publish_shipifyV2_V1publisherrorautomaticpopupv1](/images/how_to_publish_shipifyV2_V1publisherrorautomaticpopupv1.png)
    4. Save your changes and refresh the page.
    
=== "Shopify V2"

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Ensure that you have activated the `Automatic Popup Quiz` in the  Online Store > Theme > Customize > `App Embeds` and **not** the the legacy `Automatic Popup Quiz Legacy`.
        ![how_to_publish_shipifyV2_V1publisherrorautomaticpopup](/images/how_to_publish_shipifyV2_V1publisherrorautromaticpopup.png)

        If a wrong automatic popup quiz is activated, you will see the error message "The quiz you are looking for does not exist" when trying to link to a V2 quiz. 
        
        To solve this simply deactivate the `Automatic Popup Quiz Legacy` and activate the `Automatic Popup Quiz` one. 
    2. Save the changes.

=== "WooCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Magento"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "BigCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Standalone"

    If you see the error message "The quiz you are looking for does not exist" when trying to activate an automatic popup quiz, follow these steps:

    1. Make sure you have added our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    3. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    4. Save the changes and refresh the page.   


---
By following these steps, you can enhance your eCommerce store's interactivity and user engagement through well-timed automatic popups.