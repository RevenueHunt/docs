# How to Embed an Inline Quiz on Your Store

This guide provides step-by-step instructions for embedding an inline quiz on various sections of your store, including the homepage, a new page, a specific collection page, and how to manage the quiz's size and autoscroll behavior.

!!! info "What's an Inline Quiz?"

    An inline quiz is a quiz embedded directly into a page (an element on the page).

!!! note "Before you start"

    Make sure you have an existing quiz created with the RevenueHunt app and access to your store's theme customization options.

=== "Shopify (Legacy)"

    In short, to embed an inline quiz on your store, you need to:

    - Open Shopify Theme Customizer.

    - Add a section to the homepage or a specific page template and select the `Inline Quiz` by RevenueHunt from the list.

=== "Shopify"

    In short, to embed an inline quiz on your store, you need to:

    - Open Shopify Theme Customizer.
    
    - Add a section to the homepage or a specific page template and select the `Inline Quiz` by RevenueHunt from the list.

=== "WooCommerce"

    In short, to embed an inline quiz on your store, you need to:

    - Generate an embed code from the `Share` section of the app
    
    - Paste the embed code into  an HTML element of the page where you want the quiz to show.

=== "Magento"

    In short, to embed an inline quiz on your store, you need to:

    - Add an embed.js script to the page where you want the quiz to show.
    
    - Generate an embed code from the `Share` section of the app
    
    - Paste the embed code into  an HTML element of the page where you want the quiz to show.

=== "BigCommerce"

    In short, to embed an inline quiz on your store, you need to:

    - Add an embed.js script to the page where you want the quiz to show.
    
    - Generate an embed code from the `Share` section of the app
    
    - Paste the embed code into  an HTML element of the page where you want the quiz to show.

=== "Standalone"

    In short, to embed an inline quiz on your store, you need to:

    - Add an embed.js script to the page where you want the quiz to show.
    
    - Generate an embed code from the `Share` section of the app
    
    - Paste the embed code into  an HTML element of the page where you want the quiz to show.

## Embed an Inline Quiz on the Homepage

!!! info "What's an inline quiz on the homepage?"

    An inline quiz on the homepage is a quiz embedded directly into the homepage. Place the quiz on your homepage to start collecting leads from first-time visitors.

=== "Shopify (Legacy)"

    **Option 1: Through Shopify Theme**

    <div class="videoWrapper"><iframe src="https://www.youtube.com/embed/SGEfb-EPCcE?si=ZmignNyehGwF4Ysa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
    2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from RevenueHunt`. Select it to add to your homepage.
    3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    **Option 2: Manual Embedding**

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
    2. **Add Custom HTML Section**: In the Shopify theme customizer, click `Add section` then select `Custom content`. Remove default content and add a `Custom HTML` section.
    3. **Embed the Quiz**: Paste the copied HTML code into the `HTML` input of the Custom HTML section and save.

=== "Shopify"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.youtube.com/embed/OCX0EgfERpc?si=w4RwuW79QYodjRWz" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
    2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from RevenueHunt`. Select it to add to your homepage.
        ![how to publish inline quiz shopify v2 main page](/images/how_to_publish_inline_quiz_shopify_v2_main_page.png)

    3. The default quiz for your store will be rendered. 
    
        !!! note 
            If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

            If you want to render a specific quiz, you can do so by providing a specific quiz ID in the `Quiz ID` field. Check this [section](#embed-a-specific-quiz) for more information.

    4. In the `Inline Quiz` section, you can adjust the inline quiz settings.
        ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

        `Quiz height` - The initial height of the quiz. If the quiz is not tall enough, after the first question, it will expand to fit the content.

        `Quiz height (unit)` - The unit of the quiz height. Default is `Pixels (px)`. You can change it to `Viewport height percentage (vh)`.

        `Fixed height` - Keeps the quiz height fixed. Turn off to allow automatic height adjustment.

        `Full width quiz` - Makes the quiz span the full width of the page. Off by default (Shopify recommended). 

        `Auto-scroll on retake quiz` - Enable this to make the quiz auto-scroll when the user retakes the quiz. Select the scrolling behavior (`Disabled`, `Top of the page`, `Top of the quiz`).

        `Auto-scroll on question change` - Enable this to make the quiz auto-scroll when the user navigates to another question. Select the scrolling behavior (`Disabled`, `Top of the page`, `Top of the quiz`).

        `Quiz ID (optional)` - Enter a quiz ID to show a specific quiz. Leave blank to load the default.

        `Manage app` - Opens the RevenueHunt dashboard with full settings and options.

    5. Click on `Save` to save the changes. From now on, the inline quiz will be visible on all the pages that use the `Default page` template.
    
        ![how to publish inline quiz shopify v2 main page 2](/images/how_to_publish_inline_quiz_shopify_v2_main_page_2.png)

=== "WooCommerce"

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    3. In WordPress, open `Pages` and find the Front Page. Click `Edit` to open the page.
    4. In the editor, find a `Custom HTML` element and add it to the page in a place where you want the quiz to show.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the inline quiz will be visible on the main page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your Magento dashboard go to `Content` > `Blocks`. Click `Add New Block`.
    5. Edit the Block Title, Identifier and Store View and click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the inline quiz will be visible on the main page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Find the main page.
    5. Switch to the `HTML` editor. Find the place where you want to add the quiz and paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on the main page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your store customization options find the main page.
    5. Find the place where you want to add the quiz and find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on the main page.

## Embed an Inline Quiz on a Dedicated Landing Page

!!! info "What's an inline quiz on a dedicated landing page?"

    An inline quiz on a dedicated landing page is a quiz widget embedded directly into a new page in your store. Create a dedicated landing page for the quiz to drive traffic from paid ads or marketing campaigns.


=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/Zy1ZFpdtLiQ?si=15XisaE-Y-9-6JTf" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
    2. **Insert Quiz into Page**: Navigate to `Online Store > Pages` and select the page to embed the quiz. Click `Show HTML` and paste the embed code into the code editor.
    3. **Single Quiz Per Page**: To avoid issues, embed only one quiz per page. If using a non-Shopify version of the quiz, ensure the `embed.js` code is added to your site's header.

=== "Shopify"

    <div style="position: relative; padding-bottom: 53.125%; height: 0;"><iframe src="https://www.youtube.com/embed/d6Q9K0AHyHo?si=f06WCz5pWXLR1eQ-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.

    2. **Create a New Page Template**: click on the `Templates` menu in the header.
        ![Create a new Page template](/images/landing-page-create-a.png)
        Navigate to `Pages` and click on the `Create template` link. Name your template (e.g., quiz-page) and set it as "Based on" your Default page template. 
        ![Create a new Page template](/images/landing-page-create-b.png)
    
    3. **Add Inline Quiz Section**: Click on the `Add section` link and from the `Apps` section, find `Inline Quiz` from RevenueHunt. Select it to add to your quiz page template.
        ![Add section inline quiz](/images/landing-page-add-section-app-inline-quiz.png)

    4. The default quiz for your store will be rendered. 
    
        !!! note 
            If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.

            If you want to render a specific quiz, you can do so by providing a specific quiz ID in the `Quiz ID` field. Check this [section](#embed-a-specific-quiz) for more information.

    5. **Configure Quiz Settings**: Click on the added quiz section to configure. Adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height.

    6. **Assign the Template to a Page**: Go to `Online Store > Pages`. Click `Add page` or select an existing page to edit. In the Template section on the right, choose your new template from the Theme template dropdown. Click `Save` and then `View Template`. 
        ![how to publish inline quiz shopify v2 new page](/images/how_to_publish_inline_quiz_shopify_v2_new_page.png)

        The default quiz for your store will be rendered. If you’ve configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead.
        ![how to publish inline quiz shopify v2 main page 2](/images/how_to_publish_inline_quiz_shopify_v2_main_page_2.png)

    7. **Save Changes**: Ensure all changes are saved before exiting the theme editor.
    
        Now, that page will use the custom template with the quiz you created, allowing for a different layout or style within the same theme.

=== "WooCommerce"

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    3. In WordPress, open `Pages` and click `Add New Page`.
    4. In the editor, add a page title. Then, find a `Custom HTML` element and add it to the page in a place where you want the quiz to show.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the inline quiz will be visible on that page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your Magento dashbaord go to `Content` > `Pages`. Click `Add New Page`.
    5. Edit the Page Title and open the `Content` tab. Click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the inline quiz will be visible on that page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Click `Create a Web Page`.
    5. Under `Web Page Details` > `Page Content` switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your store customization options find the `Pages` menu and create a new page.
    5. In the page editor find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that page.

!!! tip

    You can add a link to this page to your website menu or use the link to this new page in your marketing campaigns.

## Embed an Inline Quiz on a Specific Collection/Category

!!! info "What's an inline quiz on a specific collection/category?"

    An inline quiz on a specific collection/category is a quiz widget embedded directly into a specific collection/category page in your store.

=== "Shopify (Legacy)"

    **Option 1: In Collection Description**

    1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
    2. **Embed Directly**: Add the inline embed code to the HTML field of the collection description to display the quiz under the collection name.

    **Option 2: Through a New Collection Theme**

    1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
    2. **Create Custom Collection Theme**: Have a developer create a new theme template incorporating the quiz code, then apply this template to the desired collection page.

=== "Shopify"

    1. To add a inline quiz to a specific collection page, in Shopify, go to `Online Theme > Customize`. From the `Home page` menu on top, go to `Collections > Create template` and create a new collection template.
    2. In the collection template editor, click on `+ Add section`, click the `Apps`. From the list, pick the `Inline Quiz`.
    3. In the `Inline Quiz` section, you can adjust the inline quiz settings or provide a specific quiz ID.
    4. Save the changes.
    5. Apply the new collection template to the collection you want to add the inline quiz to.
    5. From now on, the inline quiz will be visible on that collection page.

=== "WooCommerce"

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    3. Follow [these instructions](https://woocommerce.com/document/allow-html-in-term-category-tag-descriptions/) to enable HTML in category descriptions. 
    3. Go back to your WordPress dashboard. Open `WooCommerce`> `Products`> `Categories`. 
    4. Select a category and click `Edit`. Paste the code copied from the app in the description field.
    5. Save the changes. 
    6. From now on, the inline quiz will be visible on that category page.

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your Magento dashbaord go to `Catalog` > `Categories`. Select a category.
    5. Open the `Content` tab. Click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the inline quiz will be visible on that category page.

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In BigCommerce, go to `Products` > `Product Categories`. Select a category and open it.
    5. Under `Category Details` > `Description` switch to the `HTML` editor. 
    6. Paste the HTML code copied from the app.
    7. Save the changes.
    8. From now on, the inline quiz will be visible on that category page.

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your store customization options find the `Product Categories` menu and open the category settings.
    5. In the category description check for an HTML editor and paste the code copied from the app.
    6. (alternatively) In the category page editor find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that category page.

## FAQs

### Embed a Specific Quiz

=== "Shopify (Legacy)"

    To embed a specific quiz, just **add the **Quiz ID** to the `Inline Quiz (Legacy)` settings and save the changes.

    ![how_to_publish_quiz_inline_settings](/images/how_to_publish_quiz_inline_settings.png)

    
    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.

    
=== "Shopify"

    By default when you embed the inline quiz, the default quiz for your store will show. 
    
    !!! note

        If you've configured [Shopify Markets](/reference/app-settings/#__tabbed_5_2), the default quiz for that specific market will be shown instead. 

    If instead you want to **embed a specific quiz**, you need to add a Quiz ID in the `Quiz ID (optional)` field in the `Inline Quiz` settings in the theme editor.

    ![manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings](/images/manual_shopifyV2_quizbuilder_share_publish_onlinestore_inline_settings.png)

    !!! info "Quiz ID"

        To find your Quiz ID, go to the [Dashboard](/reference/dashboard/), find the quiz you want to open. Then, click on the `...` three dots next to the quiz and select "Copy Quiz ID".

        Keep in mind that the Quiz ID is case-sensitive.
    

=== "WooCommerce"

    To embed a specific quiz, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.

=== "Magento"

    To embed a specific quiz, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.

    

=== "BigCommerce"

    To embed a specific quiz, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.
   

=== "Standalone"

    To embed a specific quiz, just generate the embed code from the [`Share`](/reference/quiz-builder/share-publish/) tab of the desired quiz and add it to the page where you want the quiz to show.

    
    

### Fixing the Size of the Inline Quiz

To prevent the quiz from adjusting size based on content, manually set a fixed width and height in the quiz settings or embed code.

=== "Shopify (Legacy)"

    **Option 1: Through Shopify Theme**

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
    2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from RevenueHunt`. Select it to add to your homepage.
    3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height. Check the `Fixed size` option.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    **Option 2: Manual Embedding**

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode, and `Show Instructions for Legacy Themes`.
    2. **Configure Quiz Settings**: Set a desired quiz height and check the `Fixed size` option.
    3. **Get new code**: Click `Get code` and copy the new HTML embed code.
    4. **Embed the Quiz**: Paste the copied HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).

=== "Shopify"

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
    2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz` from RevenueHunt. Select it to add to your homepage.
    3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height. Check the `Fixed size` option.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.   

=== "WooCommerce"

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. **Configure Quiz Settings**: Set a desired quiz height and check the `Fixed size` option.
    3. **Get new code**: Click `Get code` and copy the new HTML embed code.
    4. **Embed the Quiz**: Paste the copied HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Configure Quiz Settings**: Set a desired quiz height and check the `Fixed size` option.
    4. **Get new code**: Click `Get code` and copy the new HTML embed code.
    5. **Embed the Quiz**: Paste the copied HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).    

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Configure Quiz Settings**: Set a desired quiz height and check the `Fixed size` option.
    4. **Get new code**: Click `Get code` and copy the new HTML embed code.
    5. **Embed the Quiz**: Paste the copied HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).    

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Configure Quiz Settings**: Set a desired quiz height and check the `Fixed size` option.
    4. **Get new code**: Click `Get code` and copy the new HTML embed code.
    5. **Embed the Quiz**: Paste the copied HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).

### Preventing Autoscroll in Inline Quiz

=== "Shopify (Legacy)"

    **Option 1: Through Shopify Theme**

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
    2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from RevenueHunt`. Select it to add to your homepage.
    3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings. Uncheck the `Automatic Scroll into View` option.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

    **Option 2: Manual Adjustment**

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode, and `Show Instructions for Legacy Themes`.
    2. **Get new code**: Click `Get code` and copy the new HTML embed code.
    3. **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with. For example:
        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```
    4. **Embed the Quiz**: Paste the adjusted HTML code wherever you like on your website.

=== "Shopify"

    1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
    2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz` from RevenueHunt. Select it to add to your homepage.
    3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings. Uncheck the `Automatic Scroll into View` option.
    4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

=== "WooCommerce"

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. **Get new code**: Click `Get code` and copy the new HTML embed code.
    3. **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with. For example:
        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```
    4. **Embed the Quiz**: Paste the adjusted HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).

=== "Magento"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Get new code**: Click `Get code` and copy the new HTML embed code.
    4. **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with. For example:
        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```
    5. **Embed the Quiz**: Paste the adjusted HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).

=== "BigCommerce"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Get new code**: Click `Get code` and copy the new HTML embed code.
    4. **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with. For example:
        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```
    5. **Embed the Quiz**: Paste the adjusted HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).

=== "Standalone"

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Get new code**: Click `Get code` and copy the new HTML embed code.
    4. **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with. For example:
        ```html
        <div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
        ```
    5. **Embed the Quiz**: Paste the adjusted HTML code wherever you like on your website. Follow instructions on How to add an inline quiz on the [Homepage](#embedding-an-inline-quiz-on-the-homepage), [New Page](#embedding-an-inline-quiz-on-a-new-page) or [Collection/Category Page](#embedding-an-inline-quiz-on-a-specific-collectioncategory-page).


### The quiz you are looking for does not exist

![docs/images/how_to_publish_shipifyV2_V1publisherror.png](/images/how_to_publish_shipifyV2_V1publisherror.png)

=== "Shopify (Legacy)"

    If you see the error message "The quiz you are looking for does not exist" when trying to embed a quiz, follow these steps:

    1. Go back to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    2. Go to [Quiz Settings](/reference/quiz-builder/quiz-settings/) and **copy the Quiz ID**. Then in Shopify, go back to Online Store > Themes > Customize and under the `+ Add Section` > `Apps` active the `Inline Quiz`. 
    3. Paste the Quiz ID in the `Quiz ID` field. *Note: the Quiz ID is case-sensitive.*
        ![how_to_publish_shipifyV2_V1publisherrorinlinev1](/images/how_to_publish_shipifyV2_V1publisherrorinlinev1.png)
    4. Save your changes and refresh the page.
    
=== "Shopify"

    !!! warning "Shopify 1.0 Theme Compatibility"
        Quizzes created with Shopify V2 cannot be published on Shopify 1.0 themes. Shopify 1.0 themes do not support app embeds, which are required for the V2 integration. App embeds are a feature available in Online Store 2.0 themes, which allow you to add app functionality without touching any code. If you want to use app embeds, you would need to upgrade to an Online Store 2.0 theme.

    If you see the error message "The quiz you are looking for does not exist" when trying to embed a quiz, follow these steps:

    1. Ensure that you have activated the `Inline Quiz` in the  Online Store > Theme > Customize > `+ Section` > `Apps` and **not** the the legacy `Inline Quiz Legacy`.
        ![how_to_publish_shipifyV2_V1publisherrorinlinequiz](/images/how_to_publish_shipifyV2_V1publisherrorinlinequiz.png)

        If a wrong inline quiz is activated, you will see the error message "The quiz you are looking for does not exist" when trying to link to a V2 quiz. 
        
        To solve this simply deactivate the `Inline Quiz Legacy` and activate the `Inline Quiz` one. 
    2. Save the changes.

=== "WooCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to embed a quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Magento"

    If you see the error message "The quiz you are looking for does not exist" when trying to embed a quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "BigCommerce"

    If you see the error message "The quiz you are looking for does not exist" when trying to embed a quiz, follow these steps:

    1. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    2. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    3. If the quiz is still not displayed,try adding our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    4. Save the changes and refresh the page.

=== "Standalone"

    If you see the error message "The quiz you are looking for does not exist" when trying to embed a quiz, follow these steps:

    1. Make sure you have added our embed.js script to the page via a custom HTML element.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
    2. Make sure to generate the correct embed code from the [Share](/reference/quiz-builder/share-publish/) section. If in doubt, regenerate the embed code and re-paste it in the page.
    3. Ensure that the quiz is published and active. Go to the [Quiz Builder](/reference/quiz-builder/) and ensure that the quiz has been published with the top right `Publish` button.
    4. Save the changes and refresh the page.   

---
By following these steps, you can successfully integrate an interactive inline quiz into your Shopify store.
