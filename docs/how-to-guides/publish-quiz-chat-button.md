# How to Add a Quiz Popup via a Chat-Like Button on Your Shopify Store

Enhance your Shopify store's interactivity by integrating a chat-like button that triggers a quiz popup. This guide provides step-by-step instructions on how to implement this feature, offering both theme-based and manual methods.

Make sure you have:

- Access to your Shopify store's admin dashboard.
- An existing quiz created with the Shop Quiz app.
- Familiarity with Shopify's theme customization options.

## Chat Button on the Homepage

### Option 1: Through Shopify Theme

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/oQyIiA2GwjY?si=X5Pd4YUR5O-sby3u" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

1. **Copy Quiz ID**: Go to your Shop Quiz [dashboard](https://docs.revenuehunt.com/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
3. **Embed the Chat Button Quiz**: Select `Chat Button Quiz` from the list.
4. **Customize the Chat Button**: Enter your Quiz ID into the appropriate field. Adjust the chat button settings as needed. Activate the chat button by toggling it on.
5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

### Option 2: Manual

1. **Obtain Chat Embed Code**: From the quiz builder, click `Share`, select `Chat button` mode, and `Show Instructions for Legacy Themes`.
2. **Generate Popup Code**: Adjust settings like welcome message, width or height and click `Get code` to generate an HTML code.
3. **Open Store Themes**: In `Themes`, click `Customize`, add a `Custom content` section, then a `Custom HTML`/`Custom liquid` block.
4. **Paste Popup Code**: In the HTML/custom liquid block, paste your popup code. paste this code into the HTML of your desired pages.
5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.

## Chat Button on All Pages

If you want the chat button to appear across your entire store, follow the [Manual Instructions](#option-2-manual) and insert the code before the `</body>` closing tag in your shop’s theme.

---
By following these instructions, you can successfully add a chat-like button to your Shopify store that opens a quiz popup.
