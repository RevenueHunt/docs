# How to Set Up Automatic Popups for Shopify Stores

Automatic popups in Shopify can significantly enhance user engagement by presenting timely content or interactive elements like quizzes. This guide walks you through setting up automatic popups on your Shopify store, including popups that appear based on time spent on a page, across all pages, on the homepage, with exit intent, and options for showing popups multiple times per session.

Enable automatic popups on specific pages, across all pages, or on the main page of your Shopify store, with additional configurations for exit intent and repeat views.

Before You Start:

- Ensure you have administrative access to your Shopify store.
- A quiz created with the Shop Quiz app.
- (optional) Basic understanding of HTML for editing Shopify themes.
- (optional) Access to your Shopify theme's code editor.

## Safety Warning

Directly editing your Shopify theme's source code can potentially disrupt your store's functionality. If unsure about some steps, consider hiring a developer.

## Setting Up Automatic Popups

### On the Main Page

#### Option 1: Shopify Theme

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/ZAK781-T1Z8?si=NAy4XjfDeisEw0w-" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

- **Prepare**: Copy your Quiz ID.
- **Navigate and Customize**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
- **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID, adjust settings, activate the toggle, and save.

#### Option 2: Manual

- **Generate Popup Code**: As described above.
- **Customize Main Page**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML` block.
- **Paste Popup Code**: In the HTML block, paste your popup code and save.

### On a Specific Page

1. **Generate Popup Code**: From your app, navigate to `Share > Automatic` to generate the popup code.
2. **Embed Code on Page**: In Shopify, go to `Online Store > Pages`, select the page, click `Show HTML`, and paste the popup code. Save your changes.

### Across All Pages

1. **Copy Popup Code**: Obtain the code from your app.
2. **Edit Theme's Source Code**: Navigate to `Online Store > Themes`, click `Actions > Edit Code` to access the theme editor.
3. **Locate and Edit File**: Find the `</body>` tag in `theme.liquid` or `footer.liquid`. Paste the popup code just before this tag. Save your changes.


### Show Popup on Exit Intent

#### Option 1: Shopify Theme

- Activate the "Exit intent" option in your popup settings.

#### Option 2: Manual

- Same as above, with an additional step to generate a new code if necessary.

### Repeated Popup Displays per Session

- **Modify Popup Code**: To show the popup more than once per session until completion, add `data-aggressive="true"` to your popup code. Example:

  ```html
  <div id="auto-popup" data-timeout="5" data-exit-intent="true" data-aggressive="true" data-quiz-id="dbqHqN" style="display: none;"></div>
  ```

By following these steps, you can enhance your Shopify store's interactivity and user engagement through well-timed automatic popups. Customize your approach based on your store's unique needs and the specific behavior you want to encourage in your visitors. Remember, the key to effective popups is balancing visibility with user experience to avoid intrusiveness.