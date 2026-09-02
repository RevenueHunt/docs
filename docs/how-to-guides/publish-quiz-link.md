---
description: "Learn how to set up a RevenueHunt quiz link popup that opens when visitors click menu items or buttons."
icon: material/link-variant
---

# How to Set Up a Quiz Link Popup on Your Store

A link popup opens the quiz over the page the customer is already on. The link can sit in your navigation menu, on a button, a banner, a page or a blog post.

!!! note "Before you start"

    You need a quiz built in the RevenueHunt app, and permission to edit your themes, pages and navigation.

=== "Shopify"

    Two things make a link popup work here.

    1. **Turn on the `Link Popup Quiz` app embed in your theme**, for every page. For one page only, add a `Link Popup Quiz` section to that page template instead.

    2. **Use `#quiz` as the link.** It goes in a menu item, a button, a banner, a page or a blog post.

=== "Shopify (Legacy)"

    Two things make a link popup work here.

    1. **Turn on the `Link Popup Quiz (Legacy)` app embed in your theme.**

    2. **Use `#quiz-QUIZID` as the link.** It goes in a menu item, a button, a banner, a page or a blog post.

=== "WooCommerce"

    Two things make a link popup work here.

    1. **Generate a link from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    2. **Paste that link into a menu item, a button, a banner, a page or a blog post.**

=== "Magento"

    Two things make a link popup work here.

    1. **Generate a link from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    2. **Paste that link into a menu item, a button, a banner, a page or a blog post.**

=== "BigCommerce"

    Two things make a link popup work here.

    1. **Generate a link from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    2. **Paste that link into a menu item, a button, a banner, a page or a blog post.**

=== "Standalone"

    Two things make a link popup work here.

    1. **Generate a link from the [`Share`](/reference/quiz-builder/share-publish/) section of the app.**

    2. **Paste that link into a menu item, a button, a banner, a page or a blog post.**

## Link popup in website menu

### On every page

The menu item then opens the quiz over any page in your store.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/NYwDShgRQEs?si=-7q-Mcf1NmiOQDVp" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Open `App embeds` and turn on `Link Popup Quiz`.** That adds the `embed.js` script to your store, so any `#quiz` link opens the popup.

        ![The Link Popup Quiz embed in the App embeds list](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)

    3. **Set the popup up.**

        ![The Link Popup Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup width (% of screen)` | How wide the popup opens |
        | `Popup height (% of screen)` | How tall the popup opens |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    4. **Click `Save`.**

    5. **Go to `Content > Menus` and open the menu you want the link in.**

        ![The Menus screen in the Shopify admin](/images/how_to_publish_link_popup_shopify_v2_menu.png)

    6. **Click `Add menu item` and give it a label**, such as `Take the quiz`.

    7. **Type `#quiz` into the link field, then click `Save`.**

        ![A menu item with #quiz as its link](/images/how_to_publish_link_popup_shopify_v2.png)

        !!! warning "The field takes the fragment, not a URL"

            Put `#quiz` in the link field on its own. A full address such as `http://yourwebsite.com/#quiz` does not open the popup.

    8. **Click `Save` on the menu.**

    9. **Open your store and click the new menu item.** The quiz should open in a popup.

    !!! note "Which quiz opens"

        `#quiz` opens your default quiz.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, see [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/g2Gvtsp0LGo?si=bzoClxr1kagdcocL" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, open the [`Link` tab](/reference/quiz-builder/share-publish/#link), then `Show Instructions for legacy themes`.**

    2. **Click `Get the code`** and copy the link.

    3. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    4. **Open `App embeds` and turn on `Link Popup Quiz (Legacy)`.** That adds the `embed.js` script to your store.

        The plain `Link Popup Quiz` embed serves the Built for Shopify version, so a legacy quiz opened through it reports that it does not exist.

        ![The Link Popup Quiz embeds in the App embeds list](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)

    5. **Go to `Content > Menus` and open the menu you want the link in.**

        ![The Menus screen in the Shopify admin](/images/how_to_publish_link_popup_shopify_v2_menu.png)

    6. **Click `Add menu item` and give it a label**, such as `Take the quiz`.

    7. **Paste the copied link into the link field, then click `Save`.**

        ![A menu item with the quiz link](/images/how_to_publish_link_popup_shopify_v2.png)

    8. **Click `Save` on the menu.**

    9. **Open your store and click the new menu item.** The quiz should open in a popup.

=== "WooCommerce"

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    2. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    3. **In your WordPress admin, go to `Appearance > Menus`.**

    4. **Pick a menu, add a `Custom Link`, and paste the link into the `URL` field.** Give it a link text, such as `Take the quiz`.

        ![Adding a custom link to a WordPress menu](/images/how_to_publish_quiz_woo_link-popup_menu.png)

    5. **Click `Save Menu`.**

    6. **Open your store and click the new menu item.** The quiz should open in a popup.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Go to `Catalog > Categories` and add the link as a menu item.** See the Adobe Commerce documentation on [the top navigation](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/navigation/navigation-top).

    5. **Save the category.**

    6. **Open your store and click the new menu item.** The quiz should open in a popup.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Go to `Storefront > Web Pages` and click `Create a Web Page`.**

    5. **Under `Page Type`, choose `Link to Another website or document`.**

    6. **Under `Web Page Details`, put the quiz name in `Page Name` and paste the link into the `Link` field.**

    7. **Under `Navigation Menu Options`, tick the box that shows this page in the navigation menu.** Pick a parent page, or leave it with none.

    8. **Click `Save & Exit`.**

    9. **Open your store and click the new menu item.** The quiz should open in a popup.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open your store navigation settings, add a new item, and paste the link into it.**

    5. **Save the menu.**

    6. **Open your store and click the new menu item.** The quiz should open in a popup.

### On a specific page

The menu item then opens the quiz over one page only. Any other page built on the same template counts as that page.

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    A `Link Popup Quiz` section on one page template keeps the popup to that page, and to any other page built on the same template.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Open the page template menu and pick the template you want, or create one.**

    3. **Click `Add section`, open the `Apps` group, and add `Link Popup Quiz`.**

        ![Adding the Link Popup Quiz section from the Apps group](/images/manual_shopifyv2_pagelevel_linkpopup_add.png)

    4. **Set the popup up.**

        ![The Link Popup Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup width (% of screen)` | How wide the popup opens |
        | `Popup height (% of screen)` | How tall the popup opens |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    5. **Click `Save`.**

    6. **Apply the template to your page.** In `Online Store > Pages`, open the page and pick that template.

    7. **Go to `Content > Menus` and open the menu you want the link in.**

        ![The Menus screen in the Shopify admin](/images/how_to_publish_link_popup_shopify_v2_menu.png)

    8. **Click `Add menu item`, give it a label, and type `#quiz` into the link field.**

        ![A menu item with #quiz as its link](/images/how_to_publish_link_popup_shopify_v2.png)

        !!! warning "The field takes the fragment, not a URL"

            Put `#quiz` in the link field on its own. A full address such as `http://yourwebsite.com/#quiz` does not open the popup.

    9. **Click `Save` on the menu.**

    10. **Open that page and click the menu item.** The quiz should open there, and nowhere else.

    !!! note "Which quiz opens"

        `#quiz` opens your default quiz.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, see [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    Turning `Link Popup Quiz (Legacy)` on in `App embeds` adds the `embed.js` script to the whole store, so the popup opens over any page. There is no setting that limits it to one.

    !!! info "Limiting it to one page"

        A developer can leave the app embed off and add the script to a single page template instead, in a custom liquid or HTML block. The popup then opens on that page only.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

        Follow [On every page](#on-every-page) for the rest of the steps.

=== "WooCommerce"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **In your WordPress admin, go to `Appearance > Menus`.**

    5. **Pick a menu, add a `Custom Link`, and paste the link into the `URL` field.** Give it a link text, such as `Take the quiz`.

        ![Adding a custom link to a WordPress menu](/images/how_to_publish_quiz_woo_link-popup_menu.png)

    6. **Click `Save Menu`.**

    7. **Open that page and click the menu item.** The quiz should open there, and nowhere else.

=== "Magento"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Go to `Catalog > Categories` and add the link as a menu item.** See the Adobe Commerce documentation on [the top navigation](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog/navigation/navigation-top).

    5. **Save the category.**

    6. **Open that page and click the menu item.** The quiz should open there, and nowhere else.

=== "BigCommerce"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Go to `Storefront > Web Pages` and click `Create a Web Page`.**

    5. **Under `Page Type`, choose `Link to Another website or document`.**

    6. **Under `Web Page Details`, put the quiz name in `Page Name` and paste the link into the `Link` field.**

    7. **Under `Navigation Menu Options`, tick the box that shows this page in the navigation menu.**

    8. **Click `Save & Exit`.**

    9. **Open that page and click the menu item.** The quiz should open there, and nowhere else.

=== "Standalone"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open your store navigation settings, add a new item, and paste the link into it.**

    5. **Save the menu.**

    6. **Open that page and click the menu item.** The quiz should open there, and nowhere else.

## Link popup as "take the quiz" button

### On home page

The button sits on your home page. The app embed makes `#quiz` work across the store, so the same link works anywhere else you put it.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/P853mRgPwr8?si=ElHwiQdpN7ZPRNWT" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    2. **Open `App embeds` and turn on `Link Popup Quiz`.** That adds the `embed.js` script to your store, so any `#quiz` link opens the popup.

        ![The Link Popup Quiz embed in the App embeds list](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)

    3. **Set the popup up.**

        ![The Link Popup Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup width (% of screen)` | How wide the popup opens |
        | `Popup height (% of screen)` | How tall the popup opens |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    4. **Click `Add section` and pick `Image banner`**, or another section that can hold a button.

    5. **Add a `Button` block inside that section.**

    6. **Click the button block and type `#quiz` into its link field.**

        ![A button with #quiz as its link](/images/how_to_publish_link_popup_shopify_v2_button.png)

        !!! warning "The field takes the fragment, not a URL"

            Put `#quiz` in the link field on its own. A full address such as `http://yourwebsite.com/#quiz` does not open the popup.

    7. **Click `Save`.**

    8. **Open the page and click the button.** The quiz should open in a popup.

    !!! note "Which quiz opens"

        `#quiz` opens your default quiz.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, see [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/mLms8xRzYCE?si=xR8VSCXvLDvXKfWc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder, open the [`Link` tab](/reference/quiz-builder/share-publish/#link), then `Show Instructions for legacy themes`.**

    2. **Click `Get the code`** and copy the link.

    3. **In your Shopify admin, go to `Online Store > Themes` and click `Customize` on your live theme.**

    4. **Open `App embeds` and turn on `Link Popup Quiz (Legacy)`.**

        The plain `Link Popup Quiz` embed serves the Built for Shopify version, so a legacy quiz opened through it reports that it does not exist.

        ![The Link Popup Quiz embeds in the App embeds list](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_linkpopup.png)

    5. **Click `Add section` and pick `Image banner`**, or another section that can hold a button.

    6. **Add a `Button` block inside that section, and paste the link into its link field.**

        ![A button with the quiz link](/images/how_to_publish_link_popup_shopify_v2_button.png)

    7. **Click `Save`.**

    8. **Open the page and click the button.** The quiz should open in a popup.

=== "WooCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page you want the button on, in your page editor.**

    5. **Add a `Button` block and paste the link into its `URL` field.**

    6. **Click `Update`.**

    7. **Open the page and click the button.** The quiz should open in a popup.

=== "Magento"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page in `Content > Pages` and click `Edit with Page Builder`.**

    5. **Drag a `Buttons` element in, then paste the link into its `Link` field.**

    6. **Save the page.**

    7. **Open the page and click the button.** The quiz should open in a popup.

=== "BigCommerce"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page in `Storefront > Web Pages`.**

    5. **Switch to the `HTML` editor and add a link or button that points at the copied link.**

    6. **Save the page.**

    7. **Open the page and click the button.** The quiz should open in a popup.

=== "Standalone"

    1. **Add the `embed.js` script before the closing `</head>` tag of your store header.** The quiz does not load without it.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page in your store editor.**

    5. **Add a button and paste the link into its link field.**

    6. **Save the page.**

    7. **Open the page and click the button.** The quiz should open in a popup.

### On a specific page

The button opens the quiz over one page only. Any other page built on the same template counts as that page.

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    A `Link Popup Quiz` section on one page template keeps the popup to that page, and to any other page built on the same template.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Open the page template menu and pick the template you want, or create one.**

    3. **Click `Add section`, open the `Apps` group, and add `Link Popup Quiz`.**

        ![Adding the Link Popup Quiz section from the Apps group](/images/manual_shopifyv2_pagelevel_linkpopup_add.png)

    4. **Set the popup up.**

        ![The Link Popup Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

        | Setting | What it does |
        |---|---|
        | `Popup width (% of screen)` | How wide the popup opens |
        | `Popup height (% of screen)` | How tall the popup opens |
        | `Popup z-index` | Which other elements the popup sits in front of |
        | `Quiz ID (optional)` | The quiz to open. Leave it empty for your default quiz |
        | `Manage app` | Opens the RevenueHunt dashboard |

    5. **Add a `Button` block to that template, and type `#quiz` into its link field.**

        ![A button with #quiz as its link](/images/how_to_publish_link_popup_shopify_v2_button.png)

        !!! warning "The field takes the fragment, not a URL"

            Put `#quiz` in the link field on its own. A full address such as `http://yourwebsite.com/#quiz` does not open the popup.

    6. **Click `Save`.**

    7. **Apply the template to your page.** In `Online Store > Pages`, open the page and pick that template.

    8. **Open that page and click the button.** The quiz should open there, and nowhere else.

    !!! note "Which quiz opens"

        `#quiz` opens your default quiz.

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for that market opens instead.

        To open a particular quiz, see [Open a specific quiz](#open-a-specific-quiz).

=== "Shopify (Legacy)"

    Turning `Link Popup Quiz (Legacy)` on in `App embeds` adds the `embed.js` script to the whole store, so the popup opens over any page. There is no setting that limits it to one.

    !!! info "Limiting it to one page"

        A developer can leave the app embed off and add the script to a single page template instead, in a custom liquid or HTML block. The popup then opens on that page only.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

        Follow [On home page](#on-home-page) for the rest of the steps.

=== "WooCommerce"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page you want the button on, in your page editor.**

    5. **Add a `Button` block and paste the link into its `URL` field.**

    6. **Click `Update`.**

    7. **Open that page and click the button.** The quiz should open there, and nowhere else.

=== "Magento"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page in `Content > Pages` and click `Edit with Page Builder`.**

    5. **Drag a `Buttons` element in, then paste the link into its `Link` field.**

    6. **Save the page.**

    7. **Open that page and click the button.** The quiz should open there, and nowhere else.

=== "BigCommerce"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page in `Storefront > Web Pages`.**

    5. **Switch to the `HTML` editor and add a link or button that points at the copied link.**

    6. **Save the page.**

    7. **Open that page and click the button.** The quiz should open there, and nowhere else.

=== "Standalone"

    1. **Add the `embed.js` script to the page template you want the popup on.** The quiz does not load without it, and putting it on one template keeps the popup to that page.

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    2. **Open [`Share`](/reference/quiz-builder/share-publish/) in the quiz builder and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    3. **Set the popup width, height and z-index, then click `Get the code`.** Copy the link it gives you.

    4. **Open the page in your store editor.**

    5. **Add a button and paste the link into its link field.**

    6. **Save the page.**

    7. **Open that page and click the button.** The quiz should open there, and nowhere else.

## FAQs

### Open a specific quiz

=== "Shopify"

    `#quiz` opens your default quiz. To open another one, either use `#quiz-QUIZID` as the link, or put the ID in the `Quiz ID (optional)` field of the `Link Popup Quiz` settings.

    ![The Quiz ID field in the Link Popup Quiz settings](/images/manual_shopifyV2_quizbuilder_share_publish_linkpopup_options.png)

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

    !!! note "Shopify Markets"

        With [Shopify Markets](/reference/app-settings/#shopify-markets) set up, the default quiz for the customer's market opens instead of your store default.

=== "Shopify (Legacy)"

    Generate the link from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open. The quiz is named in the link itself, as `#quiz-QUIZID`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "WooCommerce"

    Generate the link from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open. The quiz is named in the link itself, as `#quiz-QUIZID`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "Magento"

    Generate the link from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open. The quiz is named in the link itself, as `#quiz-QUIZID`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "BigCommerce"

    Generate the link from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open. The quiz is named in the link itself, as `#quiz-QUIZID`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

=== "Standalone"

    Generate the link from the [`Share`](/reference/quiz-builder/share-publish/) tab of the quiz you want to open. The quiz is named in the link itself, as `#quiz-QUIZID`.

    !!! info "Finding the Quiz ID"

        In the [Dashboard](/reference/dashboard/), click the `...` beside the quiz and select `Copy Quiz ID`. The ID is case-sensitive.

### Popup displays behind website header

The popup can open behind your store header, or with its `X` button hidden. That means the header is stacked in front of it, and the fix is the popup z-index.

=== "Shopify"

    The z-index decides which elements sit in front of which. Raise the popup one until it clears the header.

    1. **In your Shopify admin, go to `Online Store > Themes` and click `Customize`.**

    2. **Open `App embeds` and find the `Link Popup Quiz` settings.**

    3. **Raise `Popup z-index`.** Try `1000`, then `10000`.

        ![The z-index field in the Link Popup Quiz settings](/images/how_to_publish_quiz_link_popup_zindex_setting.png)

    4. **Click `Save`, then open the popup and check it sits in front of the header.**

    !!! note "Do not raise it further than you need"

        A z-index set very high can cover things you want visible, such as a chat widget. The right value depends on your theme.

    If the z-index does not fix it, put the quiz [inline on a page of its own](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) instead, and link to that page.

=== "Shopify (Legacy)"

    There is no z-index setting here, so the fix is in your theme. Three things to try, in this order.

    **Lower the z-index of your store header.** That is a theme change, so check your theme files or ask your theme developer.

    **Move the `X` button down.** Add this CSS to your theme, or to an empty HTML or custom liquid block on the page that shows the popup.

    ```html
    <style>
    .rh-widget span {
    top: 150px !important;
    }
    </style>
    ```

    **Put the quiz inline instead.** Publish it [on a page of its own](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) and link to that page. The quiz is then part of the page, with no popup to stack.

=== "WooCommerce"

    There is no z-index setting here, so the fix is in your theme. Three things to try, in this order.

    **Lower the z-index of your store header.** That is a theme change, so check your theme files or ask your theme developer.

    **Move the `X` button down.** Add this CSS to your theme, or to an empty HTML block on the page that shows the popup.

    ```html
    <style>
    .rh-widget span {
    top: 150px !important;
    }
    </style>
    ```

    **Put the quiz inline instead.** Publish it [on a page of its own](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) and link to that page. The quiz is then part of the page, with no popup to stack.

=== "Magento"

    There is no z-index setting here, so the fix is in your theme. Three things to try, in this order.

    **Lower the z-index of your store header.** That is a theme change, so check your theme files or ask your theme developer.

    **Move the `X` button down.** Add this CSS to your theme, or to an empty HTML block on the page that shows the popup.

    ```html
    <style>
    .rh-widget span {
    top: 150px !important;
    }
    </style>
    ```

    **Put the quiz inline instead.** Publish it [on a page of its own](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) and link to that page. The quiz is then part of the page, with no popup to stack.

=== "BigCommerce"

    There is no z-index setting here, so the fix is in your theme. Three things to try, in this order.

    **Lower the z-index of your store header.** That is a theme change, so check your theme files or ask your theme developer.

    **Move the `X` button down.** Add this CSS to your theme, or to an empty HTML block on the page that shows the popup.

    ```html
    <style>
    .rh-widget span {
    top: 150px !important;
    }
    </style>
    ```

    **Put the quiz inline instead.** Publish it [on a page of its own](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) and link to that page. The quiz is then part of the page, with no popup to stack.

=== "Standalone"

    There is no z-index setting here, so the fix is in your theme. Three things to try, in this order.

    **Lower the z-index of your store header.** That is a theme change, so check your theme files or ask your theme developer.

    **Move the `X` button down.** Add this CSS to your theme, or to an empty HTML block on the page that shows the popup.

    ```html
    <style>
    .rh-widget span {
    top: 150px !important;
    }
    </style>
    ```

    **Put the quiz inline instead.** Publish it [on a page of its own](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page) and link to that page. The quiz is then part of the page, with no popup to stack.

### Linking to multiple quizzes

One page can hold links to several different quizzes, each opening its own.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/b65c503f49ed4664875df3e6addd8380?sid=6d7edd43-ec04-4dfd-848e-2a7337980800" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Use `#quiz-QUIZID` in place of `#quiz`, with a different ID on each link.

    1. **Open the [Dashboard](/reference/dashboard/) and find the quiz you want to link to.**

    2. **Click the `...` beside it and select `Copy Quiz ID`.**

        ![The quiz management menu, with Copy Quiz ID](/images/manual_shopifyV2_quizmanagementoptions.png)

    3. **Build the link as `#quiz-QUIZID`.** A quiz with the ID `DmHLGj` gives you `#quiz-DmHLGj`.

    4. **Add it to a menu item or a button**, following the steps above for either one.

    5. **Click each link in turn and check the right quiz opens.**

    !!! example "What this is good for"

        - A different quiz per product category, such as one for skincare and one for makeup.
        - Two versions of a quiz side by side, while you [A/B test](/how-to-guides/ab-test-quiz/) them.
        - A seasonal or promotional quiz running alongside your main one.

    !!! warning "The field takes the fragment, not a URL"

        Put `#quiz-QUIZID` in the link field on its own. A full address such as `http://yourwebsite.com/#quiz-QUIZID` does not open the popup.

=== "Shopify (Legacy)"

    Each quiz has its own link, so generate one per quiz.

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) for the first quiz, open the [`Link` tab](/reference/quiz-builder/share-publish/#link), then `Show Instructions for legacy themes`.**

    2. **Click `Get the code`** and copy the link.

    3. **Repeat for every other quiz you want to link to.**

    4. **Put each link on its own menu item, button or page element.**

    5. **Click each link in turn and check the right quiz opens.**

=== "WooCommerce"

    Each quiz has its own link, so generate one per quiz.

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) for the first quiz and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    2. **Click `Get the code`** and copy the link.

    3. **Repeat for every other quiz you want to link to.**

    4. **Put each link on its own menu item, button or page element.**

    5. **Click each link in turn and check the right quiz opens.**

=== "Magento"

    Each quiz has its own link, so generate one per quiz.

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) for the first quiz and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    2. **Click `Get the code`** and copy the link.

    3. **Repeat for every other quiz you want to link to.**

    4. **Put each link on its own menu item, button or page element.**

    5. **Click each link in turn and check the right quiz opens.**

=== "BigCommerce"

    Each quiz has its own link, so generate one per quiz.

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) for the first quiz and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    2. **Click `Get the code`** and copy the link.

    3. **Repeat for every other quiz you want to link to.**

    4. **Put each link on its own menu item, button or page element.**

    5. **Click each link in turn and check the right quiz opens.**

=== "Standalone"

    Each quiz has its own link, so generate one per quiz.

    1. **Open [`Share`](/reference/quiz-builder/share-publish/) for the first quiz and open the [`Link` tab](/reference/quiz-builder/share-publish/#link).**

    2. **Click `Get the code`** and copy the link.

    3. **Repeat for every other quiz you want to link to.**

    4. **Put each link on its own menu item, button or page element.**

    5. **Click each link in turn and check the right quiz opens.**

### The quiz you are looking for does not exist

![The error a quiz shows when the link points at a quiz it cannot find](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify"

    !!! warning "Shopify 1.0 themes cannot run this"

        A quiz built in the Built for Shopify version needs an app embed or an app section, and both are Online Store 2.0 features. A Shopify 1.0 theme supports neither.

        Upgrade to an Online Store 2.0 theme to use them.

    This error means the link is being served by the embed for the other version of the app.

    1. **Go to `Online Store > Themes > Customize > App embeds` and check which link embed is on.** For a quiz built here, `Link Popup Quiz` is the right one.

        ![The two link popup embeds in the App embeds list](/images/how_to_publish_shipifyV2_V1publisherrorlinkpopup.png)

    2. **Turn `Link Popup Quiz (Legacy)` off and turn `Link Popup Quiz` on.**

    3. **Click `Save`.**

    4. **Check your link is `#quiz`, or `#quiz-QUIZID` with a valid ID.**

=== "Shopify (Legacy)"

    This error means the link cannot find the quiz. The quiz may be unpublished, the wrong embed may be on, or the ID may be wrong.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Go to `Online Store > Themes > Customize > App embeds` and turn on `Link Popup Quiz (Legacy)`.** The plain `Link Popup Quiz` embed serves the Built for Shopify version.

    3. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    4. **Check your link ends in `#quiz-QUIZID`, with that ID.**

    5. **Click `Save`, then reload the page.**

=== "WooCommerce"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

    4. **Check the `embed.js` script is on the page.**

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    5. **Save the page, then reload it.**

=== "Magento"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

    4. **Check the `embed.js` script is on the page.**

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    5. **Save the page, then reload it.**

=== "BigCommerce"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

    4. **Check the `embed.js` script is on the page.**

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    5. **Save the page, then reload it.**

=== "Standalone"

    This error means the link cannot find the quiz.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and check the quiz is published**, with the top-right `Publish` button.

    2. **Copy the `Quiz ID` from [Quiz settings](/reference/quiz-builder/quiz-settings/#general).** The ID is case-sensitive.

    3. **Check your link ends in `#quiz-QUIZID`, with that ID.**

    4. **Check the `embed.js` script is on the page.**

        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```

    5. **Save the page, then reload it.**

---

This article explains how to open a quiz from a link, in a menu or on a button. It also covers what to check when the popup does not appear.