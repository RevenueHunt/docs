---
icon: material/numeric-5
---

# One Minute Tutorials

For quick questions, check out our "One Minute Tutorials" playlist.

[Playlist: One Minute Tutorials](https://www.youtube.com/playlist?list=PL6WeHwvdARR4BGEQDKHId-i_dTm5vMdEj){ .md-button }

This is a list of topics that are covered in the playlist.

- App Intro | Walkthrough [learn more](#app-intro)
- Building the Quiz
    - Using the Quiz Builder,  Adding & Editing Questions [learn more](#using-the-quiz-builder-adding--editing-questions)
    - How Recommendations Work, Link Products & Collections [learn more](#how-recommendations-work-link-products--collections)
    - Editing Quiz Design, Adding Custom CSS code [learn more](#editing-quiz-design-adding-custom-css-code)
    - Editing the Results Page, Adding Product Blocks, Adding Logos, Using Markdown Language [learn more](#editing-the-results-page-adding-product-blocks-adding-logos-using-markdown-language)
    - Excluding Products from recommendations [learn more](#excluding-products-from-recommendations)
    - Creating Automatic Collections in Shopify [learn more](#creating-automatic-collections-in-shopify)
    - Using Product Slots on the Results Page [learn more](#using-product-slots-on-the-results-page)
    - Asking for Marketing Consent [learn more](#asking-for-marketing-consent)
- Publishing the Quiz: 
    - Link Popup in Website Menu [learn more](#link-popup-in-website-menu)
    - Link Popup as a Button [learn more](#link-popup-as-a-button)
    - Link popup for Social Media [learn more](#link-popup-quiz-for-social-media)
    - Inline on a New Page [learn more](#inline-on-a-new-page)
    - Inline on the Main Page [learn more](#inline-quiz-on-homepage)
    - Automatic Popup Quiz on Homepage [learn more](#automatic-popup-quiz-on-homepage)
    - Chat Popup Quiz on Homepage [learn more](#chat-popup-quiz-on-homepage)
- Syncing Products and Collections [learn more](#syncing-products-and-collections)
- Checking Quiz Metrics, Responses, and Exporting responses as CSV [learn more](#checking-quiz-metrics-responses-and-exporting-responses-as-csv)
- Using Jump Logic [learn more](#using-jump-logic)
- Using Skip Logic [learn more](#using-skip-logic)
- Using Block Logic [learn more](#using-block-logic)

##  App Intro 

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/UMCpGlbjrUA?si=O_AFUg1J9poNpm3d" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Building the Quiz
 
###  Using the Quiz Builder, Adding & Editing Questions

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/CkvnOEWX1a4?si=-d1MioWsU0DPaH6B" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

1. Let’s add a new quiz from your [dashboard](/reference/dashboard/).
2. [Quiz Builder](/reference/quiz-builder/) is where you’ll create your quiz. 
3. Click on the `+` plus sign and choose a question type. 
4. You can edit the question and you’ll see how it looks in the preview.
5. To change [question settings](/reference/quiz-builder/questions/#question-settings), click on :material-wrench:, a little wrench icon. Here, you can change things like adding a question description or an image.
6. To make the quiz more personal you can add a `Name question` and recall the answer in other parts of the quiz using [information recalls (@)](/how-to-guides/use-information-recalls/).
7. To select the best cleanser, you may want to know the client's age, skin type and the environment they live in. `Multiple-choice questions` may be the best way to find out this information. Let’s ask about a skin type. 
8. Finally, we should find out the environment they live in. To make the quiz more interesting, we’ll use a `Picture question` here. 
9. Don’t forget to add an `email question`! That’s how you’ll collect valuable leads for your marketing campaigns. In the [question settings](/reference/quiz-builder/questions/#question-settings) you can make this one optional.
10. Once you have all your questions you can move them around by drag and drop. 
11. Make sure to keep the quiz short. Customers typically drop out after question 8 and almost nobody gets to question 12. There’s power in simplicity!

### How Recommendations Work, Link Products & Collections

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/bdt75wZnAZA?si=U1Ksxf_7ZS7BCDbn" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Once you’re happy with the design, you can add products to each question. It is a very important step! 

1. Our [success checklist](/reference/dashboard/#success-checklist) will remind you if there are no products associated with the answers.
2. To add a product, go to the [Link Products](/reference/quiz-builder/link-products/) tab and click on the blank space after the answer.
3. Your synced products will appear as a list. Scroll down to select items or just start typing the name.
4. Multiple products can be assigned to the same answer.
5. Product Recommendation Quiz works like a [voting system](/how-to-guides/recommend-products/). 
    - Products are linked to each choice. 
    - When a customer picks that choice, all linked products receive one vote.
    - After the customer takes the quiz, the results page will show the products sorted by the number of votes.
    - If there is a draw in the number of votes, the app will randomize the products.
6. Make sure to link products to each question and choice in the quiz. 
7. You can test different answering routes and results by clicking on the `Publish` button to update the preview/live quiz and then `Preview`.


Once your quiz is built and styled, you should add products and collections to individual choices.

1. To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections](/reference/quiz-builder/link-collections/) tab. 
2. For the age question, you can link the *youth* and *anti-aging* collections created earlier.
3. Then, let’s link the *skin type* collections.
4. You can link one or more collections to the same choice.
5. Continue like this and make sure that each choice in the quiz has products or collections linked, otherwise you may end up with empty results.
6. Product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 
    - Products are linked to each choice.
    - When a customer picks that choice all the linked products receive one vote.
    - This includes all the products inside the linked collection. 
    - At the end, the results page will show slots with products sorted by the number of votes.


### Editing Quiz Design, Adding Custom CSS code

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/XU08ZCm3ZHM?si=YfKI5UOFS391nGV9" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Now let’s make the quiz pretty. 

1. You can change the look of your quiz in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
2. In the [My Themes gallery](/reference/quiz-builder/quiz-design/#my-themes), you’ll see some premade themes that you can choose from.
3. Or you can create your own design by clicking [Edit Theme](/reference/quiz-builder/quiz-design/#edit-theme).
4. To make the quiz match the store’s style let’s:
    - edit the font, 
    - change the background color, 
    - remove or add a background image, 
    - and change the color of the buttons and choices. 
5. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make the quiz unique.
6. All the changes you make will be saved automatically.
7. Once you’re done, you can change the name of your theme and it will be saved in [My Themes gallery](/reference/quiz-builder/quiz-design/#my-themes). You’ll be able to apply it to other quizzes that you create.

### Editing the Results Page, Adding Product Blocks, Adding Logos, Using Markdown Language

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/CZtWnLzw-Ko?si=VxH6PxRxp-G2GCeJ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Speaking of results. Make sure to also edit the Results Page.

1. Just like in the Quiz Builder, you can add multiple sections to your [Results Page](/reference/quiz-builder/results-page/). 
2. Click on a `+` plus sign to select a block type. 
    - In `content blocks`, you can write insightful information about the product recommended.
    - With an `image block`, you can add your brand’s logo.
    - In the `Products block`, you can select how many products will be recommended. 
3. You can use the [Markdown language](/how-to-guides/use-markdown/) to make your quiz pop. Markdowns allow you to add **boldness** or *emphasis* to your text but also insert links, images, and videos. For more information about the Markdown language, check our [How-To documentation](/how-to-guides/) section.
4. The [Result Page settings](/reference/quiz-builder/results-page/) allow you to further customize the quiz with a background image.


### Excluding Products from Recommendations

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/gRWKNg2PXzo?si=pbmMjBSAsYe1GjQe" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/recommend-products/#exclusion) feature. 

1. To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question. 
2. Tap on the greyed `exclude products` text and a white bar will appear. 
3. Simply add the products that contain an allergen.

Now, when a customer says he’s sensitive to *aloe vera*, all the products that contain it will be excluded from the possible recommendations. 

❗Be careful when using exclusions. Once a product has been excluded it won't show on the results page, even if it was upvoted in another question.



### Creating Automatic Collections in Shopify

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/EHyoUbSoNrE?si=pA7L6KwHYlFnMhJT" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers. 
2. For the slots to work correctly, you’ll have to **create four collections** and include all the corresponding products in them. For example:
    - a *Cleansers* collection should have all the cleansing products, 
    - a *Toners* collection should have all the toning products, 
    - a *Serums* collection should have all the serums, etc.
3. To create a collection, click on the top-right button. Check [this article](https://help.shopify.com/en/manual/products/collections) for detailed instructions on managing collections in Shopify.
4. Give it a name and a description. 
5. Next, you’ll select how to add products to a collection. You can do that **manually**, selecting each product one by one, or you can make an **automatic collection** based on a product tag. 
6. To create a *Cleansers* collection, we’ll choose the tag to be equal to the word `cleanser`. Shopify will automatically add all the products with this tag to the collection. 
7. You can create the toners, serums and moisturizer collections the same way.
8. You can have more than one collection that includes some of the same products. An *anti-aging* or *oily skin* collection can be composed of several cleansers, serums or moisturizers.


### Using Product Slots on the Results Page

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/mftleqOI3ig?si=JHf0CMpJQblMEBUg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Now let’s add a space for products.

1. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.
2. Use `+` to add a `Product Slots Block` and create four different slots for each of the products. 
3. In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:
    - Edit the slot name, 
    - Add a description,
    - And select how many products should be recommended in each slot.
4. Slots won’t work unless you `include collections` to each of them. It’s how they know which products to choose.
    - Include the *Cleansers* collection in the Cleansers Slot
    - Include the *Toners* collection in the Toners Slot
    - Include the *Serums* collection in the Serum Slot, etc.
5. Make sure that the products in these collections are [linked to the answers](#link-collections) in the quiz. Otherwise, the slots will produce empty results.
6. Follow the same steps to create a morning routine.

### Asking For Marketing Consent

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/Bi7pkk2SZ3k?si=BDV94fWXY64FDxMY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

To send contacts to Klaviyo your quiz needs to have an `email question`. 

1. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/) tab.
2. You can [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz. For example:
    - You can inform the customer in the [question description](/how-to-guides/ask-for-marketing-consent#option-1-question-description) that by providing the email address they agree to receive marketing information.
    - Or you can add a [marketing checkmark](/how-to-guides/ask-for-marketing-consent#option-2-marketing-checkmark) by joining two slides together. 



## Publishing the Quiz

### Link Popup in Website Menu

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/g2Gvtsp0LGo?si=PkuvFU3uXlsdsBNW" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
3. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
4. **Navigate to Your Site's Menus Settings**: From your Shopify dashboard, go to `Content > Menus`. Open the menu you wish to add the quiz link to.
5. **Add a New Menu Item**: Click on the `Add menu item` button. In the label field, type in a title for your quiz link, such as “Take Our Quiz” and then click on `Save`.
6. **Insert the Popup Link Code**: Paste the previously copied code into the link field.
7. **Save Your Changes**: Don't forget to click the `Save` button to apply the changes to your navigation menu.

### Link Popup as a Button

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/mLms8xRzYCE?si=zc2bIF1Gc0VtEOOQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then to `Link > Show Instructions for legacy themes`. Click on `Get the code` to copy the link provided.
2. **Access Theme Customization**: Log in to your Shopify admin dashboard. Navigate to `Online Store > Themes`. Find your current theme and click on the `Customize` button.
3. **Activate App Embeds**: Within the theme customization area, go to `App Embeds`. Look for the Link Popup Quiz option and toggle it on. This action will automatically add the `embed.js` script to your site, enabling quiz links to load in an iframe popup.
4.  **Navigate to Themes**: Go to `Online Store > Themes`.
5. **Enter Theme Customization**: Find the theme you wish to edit and click on the **"Customize"** button.
6. **Add a New Section**: Click on **"Add section"** and select **"Image banner"** (or a similar option) from the list.
7. **Insert a Button Block**: Within the "Image banner" section, add a new block and choose the **"Button"** option.
8. **Paste the Quiz Link**: Click on the newly added button block to edit its settings. Paste the link to your quiz in the appropriate field.
9. **Save Changes**: Make sure to save your changes by clicking on the **"Save"** button.


### Link Popup Quiz for Social Media

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/PkWI1OnP6gg?si=F9jPLQ9VY0EYA3-x" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Obtain the Popup Link Code**: Go to the `Share` section of the app, then open the `External` tile and `Show Instructions for legacy themes`. 
2. **Customize Popup Dimensions**: Set the width and height according to your preference or the requirements of the social media platform you intend to use.
3. **Generate popup link**: Click on the `Get the code` button to create your unique quiz link. This link is now ready to be shared to your social media.
4. **Share on Social Media**: Copy the generated link. Paste this link into your social media posts on Twitter, Instagram, Facebook, or any other platform you wish to use.


### Inline on a New Page 

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/Zy1ZFpdtLiQ?si=a_iq_ZUL5801DDHC" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Obtain Inline Embed Code**: From the quiz builder, click `Share`, select `Inline` mode, and `Show Instructions for Legacy Themes` to copy the HTML embed code.
2. **Insert Quiz into Page**: Navigate to `Online Store > Pages` and select the page to embed the quiz. Click `Show HTML` and paste the embed code into the code editor.
3. **Single Quiz Per Page**: To avoid issues, embed only one quiz per page. If using a non-Shopify version of the quiz, ensure the `embed.js` code is added to your site's header.


### Inline Quiz on Homepage

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/SGEfb-EPCcE?si=yLdROzT8iIKpOJ1I" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Navigate to Theme Customization**: Go to `Online Store > Themes` in your Shopify dashboard. Click the `Customize` button for your active theme.
2. **Add Inline Quiz Section**: Click `+ Add Section`, then scroll to `Apps` and find `Inline Quiz from RevenueHunt`. Select it to add to your homepage.
3. **Configure Quiz Settings**: Click on the added quiz section to configure. Select the desired Quiz ID to embed and adjust settings like quiz height, disable auto scroll, or fix quiz height for consistent results page height.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.


### Automatic Popup Quiz on Homepage

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/ZAK781-T1Z8?si=L1iK4ksmv-9ewQoh" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
3. **Embed Popup Quiz**: Select `Automatic Popup Quiz`, enter the Quiz ID, adjust settings, and activate the toggle.
4. **Save Changes**: Ensure all changes are saved before exiting the theme editor.


### Chat Popup Quiz on Homepage

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/oQyIiA2GwjY?si=w1hOh4WgBAmZfQ7V" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


1. **Copy Quiz ID**: Go to your RevenueHunt app [dashboard](/reference/dashboard/), select a quiz and click the `...` button. Copy your Quiz ID.
2. **Open Store Themes**: Go to `Online Store > Themes`, click `Customize`, then open `App Embeds`.
3. **Embed the Chat Button Quiz**: Select `Chat Button Quiz` from the list.
4. **Customize the Chat Button**: Enter your Quiz ID into the appropriate field. Adjust the chat button settings as needed. Activate the chat button by toggling it on.
5. **Save Changes**: Ensure all changes are saved before exiting the theme editor.


## Syncing Products and Collections

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/i-CHRHuRcAs?si=M5IIDEF2SsFgsxVe" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Once you’ve made changes to your products and collections, you should [sync them](/how-to-guides/sync-catalog/) with the app. 

1. The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).
2. The sync may take between 30 to 60 minutes.
3. Once it’s finished, all your products and collections will be up to date in the app.

*Note: Your store is also fully synced every 24 hours.*

## Checking Quiz Metrics, Responses, and Exporting responses as CSV

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/3BPO0a5qsHM?si=-s991O0c7CPGb-BE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

The [`Metrics`](/reference/quiz-builder/metrics/) panel is where you’ll be able to analyze quiz responses.

- Scroll down in [`analytics`](/reference/quiz-builder/metrics/#analytics) to see a general overview of your results, like how many people viewed your quiz, how many people started it, and the number of responses. 
- The [`responses`](/reference/quiz-builder/metrics/#responses) tab lets you dive deeper into individual respondents to see how they answered each question.
- You can download all responses to a CSV file by clicking [here](/how-to-guides/download-quiz-responses/).

## Using Jump Logic

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/HfYhbWB21Qg?si=4Q7Eyt5GxCN1F8En" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Let’s start with Jump Logic.

1. To display text advice in the quiz, you’ll need a `Statement question`.
2. Make it longer by adding a description.
3. One statement will be needed for each type of skin advice.

Now, how can we make only one block appear, instead of all of them, one after the other? We can use [Jump Logic](/how-to-guides/use-jump-logic/).

1. Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab and select a question. 
2. Let’s add the first [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) condition:
    - If the answer to `‘How does your skin feel on an average day?’` is `‘Dry and tight all over’` then *Dry skin* advice should appear. 
3. Click on the `+` plus sign to add another statement that can be true. This creates an additional `OR` conditional statement.
    - If the answer to `‘How does your skin feel on an average day?’` is `‘Oily all over’` then *Oily skin* advice should appear. 
4. The `OR` separator between conditions means that only one of these has to be true for the logic to work.
5. Let’s add conditions for the *Combination* and *Normal* skin.
6. To ensure the customer doesn’t see all four statements additional [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) should be added to each of them. 
7. Click on a `statement` question.
8. In the `Always jump to…` section, indicate the question or a page that should preceed it.
9. Do the same for the other three statements.
10. Now that all is set, let’s update the preview/live quiz with the top-right `Publish` button and test it with `Preview`.
    - First, select `Dry skin`. 
    - Now let’s go back and select `Oily skin`.

It seems that everything works correctly, well done!

You’ve successfully added Jump Logic to your quiz. Your customers will now be able to see this personalized advice whenever they take the quiz.

[Jump Logic](/how-to-guides/use-jump-logic/) is a powerful tool. It can also be used to:

- redirect the customer to another, external URL directly from the quiz,
- create branching in the quiz to send the customer to different answering paths,
- create branching to link different products to the same choices,
- or send customers to different Result Pages.

## Using Skip Logic

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/bHYDwwTIuWg?si=qAQGXDeB0-ZvciL5" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


For linear quizzes, using [Skip Logic](/how-to-guides/use-skip-logic/) instead is recommended.

To achieve the same effect you can set up your statements to be shown one after another.

1. Navigate to the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab, select a question and open the [Skip Logic](/reference/quiz-builder/conditional-logic/#skip-logic) menu.
2. Then, add a Skip Logic rule to each statement. For example, when selecting a *Dry skin* statement, the rule states:
    - If the answer question `‘How does your skin feel on an average day?’` **IS NOT**  `Dry and tight all over`, then this question is skipped.
    - This implies that the *Dry skin* statement will **NOT** be skipped only if the answer to that question is `Dry and thigh all over`. In all other cases, the statement will **NOT** be shown.
3. Similar rules shall be applied to the statements about the *Oily*, *Combination*, and *Normal* skin.
4. Once all is set up, make sure to publish the changes with the top-right `Publish` button.
5. Let’s test the quiz with the `Preview` button.

It worked! The correct statement is shown and all the others are skipped based on the skin type the customer selected in the previous question.

[Skip logic](/how-to-guides/use-skip-logic/) can also be used to:

- show or hide a number of follow-up questions,
- show or hide follow-up content based on questions that allow multiple answers.

## Using Block Logic

<div class="videoWrapper">
<iframe src="https://www.youtube.com/embed/JVAg0KfkX5Q?si=pjwegAOgeb2wUlwn" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


Logic can also be applied to the contents of your [Results Page](/reference/quiz-builder/results-page/). 

With [Block logic](/how-to-guides/use-block-logic/), you can show or hide elements of your results page based on the customer's answers.

1. Let’s add four `Content blocks` with the skin type advice to your [Results Page](/reference/quiz-builder/results-page/).
2. You can edit the block text with [Markdown language](/how-to-guides/use-markdown/).
3. Now, how can we make only one block appear, instead of all of them? We can add [Block logic](/reference/quiz-builder/conditional-logic/#block-logic).
4. To do that, activate it in the lower right corner with the `...` button. 
5. Let’s add the first logic condition.
    - If the answer to `‘How does your skin feel on an average day?’` is `‘Dry and tight all over’` then this block (*Dry skin block*) will be **Visible**. 
    - In all other cases, it will be **Hidden**. 
6. Now, let’s add similar rules to other content blocks.
7. Let’s publish the changes with the top-right `Publish` button and test the quiz again with `Preview`.

You’ve now successfully used Block logic to show and hide content on the Results page.

[Block Logic](/how-to-guides/use-block-logic/) is a powerful tool that can also be used to:

- show different image results depending on customer answers
- or show product blocks with different numbers of recommendations. 

