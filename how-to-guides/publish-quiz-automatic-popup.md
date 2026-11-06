---
description: "Learn how to set up automatic RevenueHunt quiz popups that appear after a delay or on exit intent."
icon: material/timer-play-outline
---

# How to Set Up Automatic Popups

An automatic popup opens the quiz on its own, a few seconds after the customer arrives. You choose where it runs: the home page, one page, or every page.

!!! info "How often a customer sees it"

    A popup opens once per session. It does not reappear if the customer moves to another page, unless you turn `Exit Intent` on, or allow [repeated displays](#repeated-popup-displays-per-session).

    Automatic popups are intrusive, which is why once per session is the default.

!!! note "Before you start"

    You need a quiz built in the RevenueHunt app, and access to your theme editor. Editing theme source code can break a storefront, so bring in a developer if a step is beyond you.

## Auto-popup on the main page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/HeHWWdbxvYI?si=yfWxXGhQEiRz6IDH" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **With the home page template open, click `Add section`, open the `Apps` tab, and add `Auto Popup Quiz (Block)`.**

        ![Adding the Auto Popup Quiz (Block) section from the Apps tab](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_embed.png)

    3. **Set up the popup.**

        ![The automatic popup settings in the theme editor](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup Delay` | How many seconds to wait before the popup opens |
        | `Popup Width` and `Height` | The size of the popup, as a percentage of the screen |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Trigger Popup on Exit Intent` | Opens the popup when the customer moves to leave the page |

    4. **Click `Save`.**

    5. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/ZAK781-T1Z8?si=NAy4XjfDeisEw0w-" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    **With the app embed**

    1. **Copy your Quiz ID.** In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and copy the ID.

    2. **Go to `Online Store > Themes`, click `Customize`, then open `App embeds`.**

    3. **Turn on `Auto Popup Quiz (Legacy)`, paste the Quiz ID, and set the delay and size.**

        The plain `Automatic Popup Quiz` embed serves the Built for Shopify version. A legacy quiz opened through it reports that it does not exist.

    4. **Click `Save`.**

    5. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

    **With pasted code**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **In `Themes > Customize`, add a `Custom content` section, then a `Custom HTML` or `Custom liquid` block.**

    4. **Paste the popup code into that block.**

    5. **Click `Save`.**

    6. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages`, find your front page and click `Edit`.**

    4. **Add a `Custom HTML` block and paste the code into it.**

    5. **Click `Update`.**

    6. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Content > Blocks` and click `Add New Block`.**

    5. **Fill in the block title, identifier and store view, then click `Edit with Page Builder`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the block.**

    9. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Storefront > Web Pages` and open your main page.**

    5. **Switch to the `HTML` editor and paste the code in.**

    6. **Save the page.**

    7. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In your store editor, open the main page.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

## Auto-popup on a specific page

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/0mJ4KiHQFq8?si=xWPSV0l6JDcVIcGN" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Pages` and click `Add page`.** Name it, for example `Automatic Popup Page`, set it to `Visible`, and save.

    2. **Go to `Online Store > Themes` and click `Customize`.**

    3. **Open the page template menu and click `+ Create a new template`.** Give it a name you will remember, such as `Automatic Quiz Popup`.

    4. **In that template, click `Add section`, open the `Apps` tab, and add `Auto Popup Quiz (Block)`.**

        ![Adding the Auto Popup Quiz (Block) section from the Apps tab](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_embed.png)

    5. **Set up the popup.**

        ![The automatic popup settings in the theme editor](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup Delay` | How many seconds to wait before the popup opens |
        | `Popup Width` and `Height` | The size of the popup, as a percentage of the screen |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Trigger Popup on Exit Intent` | Opens the popup when the customer moves to leave the page |

    6. **Click `Save`.**

    7. **Go back to `Online Store > Pages`, open your page, and set `Page Template` to the template you built.**

        ![Assigning the new template to the page](/images/how_to_shopifyv2_publish_automatic_popup_on_specific_page_template.png)

    8. **Click `Save`.**

    9. **Open that page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **In Shopify, go to `Online Store > Pages`, open the page, click `Show HTML`, and paste the code in.**

    4. **Click `Save`.**

    5. **Open that page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **In your WordPress admin, open `Pages`, find the page you want the popup on and click `Edit`.**

    4. **Add a `Custom HTML` block and paste the code into it.**

    5. **Click `Update`.**

    6. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In your Magento admin, go to `Content > Pages` and open the page, or click `Add New Page`.**

    5. **Open the `Content` tab and click `Edit with Page Builder`.**

    6. **Drag a row in from `Elements > Rows`, then drag `HTML Code` onto that row.**

    7. **Click the gear icon to open `HTML settings`, then paste the code under `Enter HTML, CSS or JavaScript code`.**

    8. **Save the page.**

    9. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In BigCommerce, go to `Storefront > Web Pages` and open the page, or click `Create a Web Page`.**

    5. **Under `Web Page Details > Page Content`, switch to the `HTML` editor and paste the code in.**

    6. **Save the page.**

    7. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In your store editor, open the page you want the popup on.**

    5. **Find a `Custom HTML` element and paste the code into its settings.**

    6. **Save the page.**

    7. **Open the page in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

## Auto-popup on all pages

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/-675UKK1uJI?si=hb4rRFFhwkk53a9p" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Open `App embeds` and turn on `Automatic Popup Quiz`.** Leave `Auto Popup Quiz (Legacy)` off. That one serves quizzes from the legacy app.

        ![The App embeds list, with Automatic Popup Quiz turned on](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic.png)

    3. **Set up the popup.**

        ![The automatic popup settings in the theme editor](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup Delay` | How many seconds to wait before the popup opens |
        | `Popup Width` and `Height` | The size of the popup, as a percentage of the screen |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Trigger Popup on Exit Intent` | Opens the popup when the customer moves to leave the page |

    4. **Click `Save`.**

    5. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

    The popup now runs on every page that uses this theme.

    !!! note "Which quiz opens"

        Your default quiz opens, unless you name another one.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, set the `Quiz ID`. See [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **Go to `Online Store > Themes` and click `Actions > Edit code`.**

    4. **Open `theme.liquid` or `footer.liquid`, and paste the code just before the closing `</body>` tag.**

    5. **Click `Save`.**

    6. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "WooCommerce"

    A popup on every page needs a plugin that can run one site-wide, such as Popup Maker or Elementor.

    1. **Install and activate a popup plugin from your WordPress admin.**

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In the plugin, create a new popup and name it.**

    5. **Add a `Custom HTML` block to the popup and paste the code into it.**

    6. **Set the plugin to show the popup on every page.**

    7. **Publish the popup.**

    8. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "Magento"

    A popup on every page needs an extension that can run one site-wide.

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Install a popup extension from the Magento Marketplace**, with Composer or by uploading it to your server.

    3. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    4. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    5. **In the extension settings, create a new popup and paste the code into it.**

    6. **Set the extension to show the popup on every page.** Its display timing and triggers are set here too.

    7. **Save the extension settings.**

    8. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

=== "BigCommerce"

    **With the Script Manager**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **In BigCommerce, go to `Storefront > Script Manager` and click `Create a Script`.**

    4. **Fill the script in.** Give it a name, set `Location on Page` to `Footer`, and set the pages to `All Pages`.

    5. **Paste the popup code into `Script Contents`, then save.**

    6. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

    **By editing the theme files**

    Use this one if you need more control than the Script Manager gives you.

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **Go to `Storefront > My Themes`, then `Advanced > Edit Theme Files`.**

    4. **Open `footer.html` under `Templates`, and paste the code just before the closing `</body>` tag.**

    5. **Save the file and deploy the theme.**

    6. **Clear your browser cache, then open your store in a private browsing window and wait for the popup.**

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **In your store editor, open your theme footer.**

    5. **Paste the popup code into the footer, so it loads on every page.**

    6. **Save the theme.**

    7. **Open your store in a private browsing window and wait for the popup.** A popup shows once per session, so a fresh window is the only way to see it again.

## FAQs

### Open a specific quiz

=== "Shopify"

    An automatic popup opens your default quiz. To open another one, put its ID in the `Quiz ID (optional)` field of the popup settings in the theme editor.

    ![The Quiz ID field in the automatic popup settings](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

    !!! note "Shopify Markets"

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for the customer's market opens instead of your store default.

=== "Shopify (Legacy)"

    Generate the popup code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it, as `data-quiz-id`.

=== "WooCommerce"

    Generate the popup code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it, as `data-quiz-id`.

=== "Magento"

    Generate the popup code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it, as `data-quiz-id`.

=== "BigCommerce"

    Generate the popup code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it, as `data-quiz-id`.

=== "Standalone"

    Generate the popup code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open, then use that code. The quiz ID is baked into it, as `data-quiz-id`.

### Show popup on exit intent

=== "Shopify"

    Exit intent opens the popup when the customer moves the cursor towards the tab or window controls, rather than after a delay.

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Open `App embeds` and turn on `Automatic Popup Quiz`.**

        ![The App embeds list, with Automatic Popup Quiz turned on](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_automatic.png)

    3. **Turn `Trigger Popup on Exit Intent` on, and adjust the width and height if you need to.**

        ![The exit intent toggle in the automatic popup settings](/images/manual_shopifyV2_quizbuilder_share_publish_automatic_options.png)

    4. **Click `Save`.**

    5. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

=== "Shopify (Legacy)"

    **With the app embed**

    1. **Copy your Quiz ID.** In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and copy the ID.

    2. **Go to `Online Store > Themes`, click `Customize`, then open `App embeds`.**

    3. **Turn on `Auto Popup Quiz (Legacy)`, paste the Quiz ID, and turn `Exit intent` on.**

    4. **Click `Save`.**

    5. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

    **With pasted code**

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Turn `Exit intent` on in the settings, then click `Get code`.** Copy the HTML it gives you.

    3. **In `Themes > Customize`, add a `Custom content` section, then a `Custom HTML` or `Custom liquid` block.**

    4. **Paste the popup code into that block.**

    5. **Click `Save`.**

    6. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    2. **Turn `Exit intent` on in the settings, then click `Get code`.** Copy the HTML it gives you.

    3. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    4. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Turn `Exit intent` on in the settings, then click `Get code`.** Copy the HTML it gives you.

    4. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    5. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Turn `Exit intent` on in the settings, then click `Get code`.** Copy the HTML it gives you.

    4. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    5. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Turn `Exit intent` on in the settings, then click `Get code`.** Copy the HTML it gives you.

    4. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    5. **Open your store, then move the cursor up towards the tab bar.** The popup should open.

### Repeated popup displays per session

=== "Shopify"

    This version shows the popup once per session and offers no way to change that.

    The one exception is exit intent, which can fire again on the same visit. See [Show popup on exit intent](#show-popup-on-exit-intent).

=== "Shopify (Legacy)"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic), then `Show Instructions for Legacy Themes`.**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **Add `data-aggressive="true"` to the popup code.** The popup then keeps returning during the session until the customer finishes the quiz.

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **In `Themes > Customize`, add a `Custom content` section, then a `Custom HTML` or `Custom liquid` block.**

    5. **Paste the popup code into that block.**

    6. **Click `Save`.**

    7. **Open your store, dismiss the popup, and carry on browsing.** It should come back.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    2. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    3. **Add `data-aggressive="true"` to the popup code.** The popup then keeps returning during the session until the customer finishes the quiz.

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    4. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    5. **Open your store, dismiss the popup, and carry on browsing.** It should come back.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **Add `data-aggressive="true"` to the popup code.** The popup then keeps returning during the session until the customer finishes the quiz.

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    6. **Open your store, dismiss the popup, and carry on browsing.** It should come back.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **Add `data-aggressive="true"` to the popup code.** The popup then keeps returning during the session until the customer finishes the quiz.

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    6. **Open your store, dismiss the popup, and carry on browsing.** It should come back.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and pick [`Automatic`](/reference/quiz-builder/share-publish/#automatic).**

    3. **Set the popup delay, width and height, then click `Get code`.** Copy the HTML it gives you.

    4. **Add `data-aggressive="true"` to the popup code.** The popup then keeps returning during the session until the customer finishes the quiz.

        ```html
        <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
        ```

    5. **Put the code on your store**, on the [home page](#auto-popup-on-the-main-page), a [specific page](#auto-popup-on-a-specific-page) or [every page](#auto-popup-on-all-pages).

    6. **Open your store, dismiss the popup, and carry on browsing.** It should come back.

### The quiz you are looking for does not exist

![The error a quiz shows when the popup points at a quiz it cannot find](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    This error means the popup is being served by the embed for the other version of the app.

    1. **Go to `Online Store > Themes > Customize > App embeds` and check which popup embed is on.** For a quiz built here, `Automatic Popup Quiz` is the right one.

        ![The two automatic popup embeds in the App embeds list](/images/how_to_publish_shipifyV2_V1publisherrorautromaticpopup.png)

    2. **Turn `Auto Popup Quiz (Legacy)` off and turn `Automatic Popup Quiz` on.** The legacy embed serves quizzes from the legacy app, so it cannot find a quiz built in this version.

    3. **Click `Save`, then reload your store.**

=== "Shopify (Legacy)"

    This error means the popup cannot find the quiz, either because it is unpublished or because the wrong embed is on.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Go to `Online Store > Themes > Customize > App embeds` and turn on `Auto Popup Quiz (Legacy)`.** The plain `Automatic Popup Quiz` embed serves quizzes from the Built for Shopify version, so it cannot find a legacy quiz.

    4. **Paste the Quiz ID into the `Quiz ID` field.**

        ![Pasting the Quiz ID into the legacy popup embed settings](/images/how_to_publish_shipifyV2_V1publisherrorautomaticpopupv1.png)

    5. **Click `Save`, then reload the page.**

=== "WooCommerce"

    This error means the popup cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "Magento"

    This error means the popup cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "BigCommerce"

    This error means the popup cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

=== "Standalone"

    This error means the popup cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Regenerate the code from [`Share`](/reference/quiz-builder/share-publish/) and paste it in again.** An old code can point at a quiz that has since changed.

    3. **Check the `embed.js` script is on the page.** Add it through a custom HTML element if it is missing.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    4. **Save the page, then reload it.**

---

This article explains how to open a quiz as an automatic popup, where to run it, and what to check when it does not appear.