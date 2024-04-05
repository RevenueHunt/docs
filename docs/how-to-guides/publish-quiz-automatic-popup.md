# How to Set Up Automatic Popups for Shopify Stores

Automatic popups in Shopify can significantly enhance user engagement by presenting timely content or interactive elements like quizzes. 

This guide walks you through setting up automatic popups on your Shopify store, including popups that appear based on time spent on a page, across all pages, on the homepage, with exit intent, and options for showing popups multiple times per session.

Before You Start:

- Ensure you have administrative access to your Shopify store.
- A quiz created with the Shop Quiz app.
- (optional) Basic understanding of HTML for editing Shopify themes.
- (optional) Access to your Shopify theme's code editor.

!!! warning

    Directly editing your Shopify theme's source code can potentially disrupt your store's functionality. If unsure about some steps, consider hiring a developer.

## Setting Up Automatic Popups

## On the Main Page

### Option 1: Through Shopify Theme

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/ZAK781-T1Z8?si=NAy4XjfDeisEw0w-" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

1. **Copy Quiz ID**: Go to your Shop Quiz [dashboard](https://docs.revenuehunt.com/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID, adjust settings, and activate the toggle.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual

1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

## On a Specific Page

1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
3. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

## Across All Pages

1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
3. **Edit Theme's Source Code**: Navigate to `Online Store > Themes`, click `Actions > Edit Code` to access the theme editor.
4. **Locate and Edit File**: Find the `</body>` tag in `theme.liquid` or `footer.liquid`. Paste the popup code just before this tag.
5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.


## Show Popup on Exit Intent

### Option 1: Through Shopify Theme

1. **Copy Quiz ID**: Go to your Shop Quiz [dashboard](https://docs.revenuehunt.com/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID and activate the `Exit intent` option in your popup settings.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual

1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
2. **Generate Popup Code**: Adjust settings and activate the `Exit intent` option in your popup settings. Click `Get code` to generate an HTML code.
3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

## Repeated Popup Displays per Session

1. **Obtain Automatic Embed Code**: From the quiz builder, click `Share`, select `Automatic` mode, and `Show Instructions for Legacy Themes`.
2. **Generate Popup Code**: Adjust settings like popup duration, width or height and click `Get code` to generate an HTML code.
3. **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example: 

    ```html
      <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
    ```

4. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
5. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code.
6. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

---
By following these steps, you can enhance your Shopify store's interactivity and user engagement through well-timed automatic popups.