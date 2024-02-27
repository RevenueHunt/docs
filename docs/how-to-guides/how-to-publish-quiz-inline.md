# How to Embed an Inline Quiz on Your Shopify Store

This guide provides step-by-step instructions for embedding an inline quiz on various sections of your Shopify store, including the homepage, a new page, a specific collection page, and how to manage the quiz's size and autoscroll behavior. Inline quizzes can enhance user engagement by offering personalized recommendations or collecting feedback directly within your store's interface.

Make sure you have:

- Access to your Shopify store's admin dashboard.
- An existing quiz created with the Shop Quiz app.
- Familiarity with Shopify's theme customization options.

## Embedding an Inline Quiz on the Homepage

### Option 1: Through Shopify Theme

1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from Shop Quiz: Product Recommender`. Select it to add to your homepage.
3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable autoscroll, or fix quiz height for consistent results page height.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual Embedding

1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
2. **Add Custom HTML Section**: In the Shopify theme customizer, click `Add section` then select `Custom content`. Remove default content and add a `Custom HTML` section.
3. **Embed the Quiz**: Paste the copied HTML code into the `HTML` input of the Custom HTML section and save.

## Embedding an Inline Quiz on a New Page

1. **Copy Embed Code**: Use the same method as above to obtain the inline embed code for the quiz.
2. **Insert Quiz into Page**: Navigate to `Online Store > Pages` and select the page to embed the quiz. Click `Show HTML` and paste the embed code into the code editor.
3. **Single Quiz Per Page**: To avoid issues, embed only one quiz per page. If using a non-Shopify version of the quiz, ensure the `embed.js` code is added to your site's header.

## Embedding an Inline Quiz on a Specific Collection Page

### Option 1: In Collection Description

- **Embed Directly**: Add the inline embed code to the HTML field of the collection description to display the quiz under the collection name.

### Option 2: Through a New Collection Theme

- **Create Custom Collection Theme**: Have a developer create a new theme template incorporating the quiz code, then apply this template to the desired collection page.

## Adjusting the Size of the Inline Quiz

- **Fix Quiz Size**: To prevent the quiz from adjusting size based on content, manually set a fixed width and height in the quiz settings or embed code. Use the `Fixed size` option in the app to generate the appropriate code.

## Preventing Autoscroll in Inline Quiz

### Option 1: Through Shopify Theme

- **Disable Autoscroll**: Uncheck the auto-scroll option in the quiz's theme customization settings.

### Option 2: Manual Adjustment

- **Adjust Embed Code**: Add `data-autoscroll="false"` to the quiz's embed code to prevent automatic scrolling when the quiz is interacted with.

By following these steps, you can successfully integrate an interactive inline quiz into your Shopify store, enhancing the user experience and potentially increasing engagement and conversions. Always test the quiz functionality across different themes and devices to ensure optimal performance and user experience.
