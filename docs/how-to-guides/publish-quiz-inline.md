# How to Embed an Inline Quiz on Your Shopify Store

This guide provides step-by-step instructions for embedding an inline quiz on various sections of your Shopify store, including the homepage, a new page, a specific collection page, and how to manage the quiz's size and autoscroll behavior. 

Make sure you have:

- Access to your Shopify store's admin dashboard.
- An existing quiz created with the Shop Quiz app.
- Familiarity with Shopify's theme customization options.

## Embedding an Inline Quiz on the Homepage

### Option 1: Through Shopify Theme

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/SGEfb-EPCcE?si=ZmignNyehGwF4Ysa" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from Shop Quiz: Product Recommender`. Select it to add to your homepage.
3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable auto scroll, or fix quiz height for consistent results page height.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual Embedding

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
2. **Add Custom HTML Section**: In the Shopify theme customizer, click `Add section` then select `Custom content`. Remove default content and add a `Custom HTML` section.
3. **Embed the Quiz**: Paste the copied HTML code into the `HTML` input of the Custom HTML section and save.

## Embedding an Inline Quiz on a New Page

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/Zy1ZFpdtLiQ?si=15XisaE-Y-9-6JTf" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
2. **Insert Quiz into Page**: Navigate to `Online Store > Pages` and select the page to embed the quiz. Click `Show HTML` and paste the embed code into the code editor.
3. **Single Quiz Per Page**: To avoid issues, embed only one quiz per page. If using a non-Shopify version of the quiz, ensure the `embed.js` code is added to your site's header.

## Embedding an Inline Quiz on a Specific Collection Page

### Option 1: In Collection Description

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
2. **Embed Directly**: Add the inline embed code to the HTML field of the collection description to display the quiz under the collection name.

### Option 2: Through a New Collection Theme

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
2. **Create Custom Collection Theme**: Have a developer create a new theme template incorporating the quiz code, then apply this template to the desired collection page.

## Fixing the Size of the Inline Quiz

To prevent the quiz from adjusting size based on content, manually set a fixed width and height in the quiz settings or embed code.

### Option 1: Through Shopify Theme

1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from Shop Quiz: Product Recommender`. Select it to add to your homepage.
3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable auto-scroll, or fix quiz height for consistent results page height. Check the `Fixed size` option.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual Embedding

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes`.
2. **Configure Quiz Settings**: Set a desired quiz height and check the `Fixed size` option.
3. **Get new code**: Click `Get code` and copy the new HTML embed code.
4. **Embed the Quiz**: Paste the copied HTML code wherever you like on your website.

## Preventing Autoscroll in Inline Quiz

### Option 1: Through Shopify Theme

1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from Shop Quiz: Product Recommender`. Select it to add to your homepage.
3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings. Uncheck the `Automatic Scroll into View` option.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual Adjustment

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes`.
2. **Get new code**: Click `Get code` and copy the new HTML embed code.
3. **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with. For example:
```html
<div class="rh-widget rh-inline" data-url="https://admin.revenuehunt.com/public/quiz/dbqHqN" data-autoscroll="false" style="margin: 10px auto; width: 100%; height: 600px; display: flex;"></div>
```
4. **Embed the Quiz**: Paste the adjusted HTML code wherever you like on your website.

---
By following these steps, you can successfully integrate an interactive inline quiz into your Shopify store.
