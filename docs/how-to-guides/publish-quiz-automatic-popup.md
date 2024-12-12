# How to Set Up Automatic Popups

Automatic popups can significantly enhance user engagement by presenting timely content or interactive elements like quizzes. 

This guide walks you through setting up automatic popups on your eCommerce store, including popups that appear based on time spent on a page, across all pages, on the homepage, with exit intent, and options for showing popups multiple times per session.

Before You Start:

- Ensure you have administrative access to your eCommerce store.
- A quiz created with the RevenueHunt app.
- (optional) Basic understanding of HTML for editing themes.
- (optional) Access to your eCommerce theme's code editor.

!!! warning

    Directly editing your Shopify or other eCommerce theme's source code can potentially disrupt your store's functionality. If unsure about some steps, consider hiring a developer.

## Setting Up Automatic Popups

!!! warning

    Automatic popups can be very intrusive which is why, by default, they are shown only once per customer session.

## On the Main Page

=== "Shopify"

    ### Option 1: Through Shopify Theme

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/ZAK781-T1Z8?si=NAy4XjfDeisEw0w-" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](https://docs.revenuehunt.com/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID, adjust settings, and activate the toggle.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    ### Option 2: Manual

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the main page.
    5. Find a `Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on the main page.



## On a Specific Page

=== "Shopify"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the page you want the quiz to show on.
    5. Find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the automatic popup quiz will be visible on that page.

## Across All Pages

=== "Shopify"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select `Automatic` mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Edit Theme's Source Code**: Navigate to `Online Store > Themes`, click `Actions > Edit Code` to access the theme editor.
    4. **Locate and Edit File**: Find the `</body>` tag in `theme.liquid` or `footer.liquid`. Paste the popup code just before this tag.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

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
    6. **Save and Test**: Save your script settings. Visit your store’s front end in an incognito window to ensure the popup appears correctly on all pages.


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
    4. **Modify the Footer File**: Locate the file typically named `footer.html` or similar under the `Templates` directory. Paste your popup’s HTML code just before the closing </body> tag.
    5. **Save and Deploy**: Save your changes and preview them. Once confirmed, deploy the changes live.
    6. **Testing**: Clear your browser cache and check the popup functionality across different pages and devices to ensure consistent behavior.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code. Copy the HTML code.
    4. In your store customization options find the option to edit your store's theme.
    5. In the footer add the HTML code copied from the app. This will ensure the popup shows up on all pages in your store.
    6. Save the changes.


## Show Popup on Exit Intent

=== "Shopify"

    ### Option 1: Through Shopify Theme

    1. **Copy Quiz ID**: Go to your RevenueHunt [dashboard](https://docs.revenuehunt.com/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
    2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
    3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID and activate the `Exit intent` option in your popup settings.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    ### Option 2: Manual

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    2. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    3. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).      

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).  

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
    4. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).          

## Repeated Popup Displays per Session

=== "Shopify"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode, and `Show Instructions for Legacy Themes`.
    2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    3. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
    5. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
    6. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
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
    2. **Obtain Automatic Embed Code**: From the quiz builder, click [`Share`](https://docs.revenuehunt.com/reference/quiz-builder/#share), select [`Automatic`](https://docs.revenuehunt.com/reference/quiz-builder/#automatic) mode.
    3. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
    4. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Publish the quiz**: Follow the instructions to publish the quiz on the [homepage](#on-the-main-page), [specific page](#on-a-specific-page) or [across all pages](#across-all-pages).    

---
By following these steps, you can enhance your eCommerce store's interactivity and user engagement through well-timed automatic popups.