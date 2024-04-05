---
icon: material/palette-outline
---

# How to Customize the Quiz Design

You can change the quiz's appearance to fit your store's style. 

Use the customization options in the [Quiz Design](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-design) tab or add your own style with [CSS](#add-custom-css-code) or [JavaScript](https://docs.revenuehunt.com/how-to-guides/add-javascript/). You can modify any part of the quiz or results page with custom CSS.

Remember, you can also include custom images and styles for each question via the [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).

## Quiz Design Tab

1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-design) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
2. **Customize the look**: You can choose from any of our pre-designed themes in the `My Themes` tab or create your own. 
3. **Edit Theme**: Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.
    ![quiz builder quiz design edit theme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="500"}

    - ***Wine*** - Displays the name of your current theme.
    - **Font** - Shows a dropdown of available fonts. Pick a font from the list to change it.
    - **Question** - Opens a color menu that allows you to change the color of quiz questions. You can add a custom color by pasting the #number of the color (for example, #ecb3b3)
    - **Choices** - Opens a color menu that allows you to change the color of quiz choices.  You can add a custom color by pasting the #number of the color (for example, #ecb3b3)
    - **Button** - Opens a color menu that allows you to change the color of quiz buttons (next, star quiz, add to cart, etc.).  You can add a custom color by pasting the #number of the color (for example, #ecb3b3)
    - **Background** - Opens a color menu that allows you to change the color of the quiz background. You can add a custom color by pasting the #number of the color (for example, #ecb3b3).
    - **Background image** - Click "Add" to upload a background image. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated.
    - **Background Opacity** - A slider that allows you to adjust the opacity of the uploaded background image.
    - **Custom CSS** - Opens a CSS console, where you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS. To find a selector for the element, inspect it in your browser by right-clicking. 

4. **My Themes**: All themes that you’ve created or edited will appear in the `My Themes` tab. 
    ![quiz builder quiz design my themes](/images/manual_quizbuilder_quizdesign_mythemes.png){width="500"}

5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.


### Add Custom CSS code

Via the CSS console, you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS.

1. **Open the Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-design) tab.
2. **Open the CSS console**: In the theme editor, click on the `add` button in the Custom CSS section. This should open an input where you can add your custom CSS to the quiz. Your developer will be able to add custom CSS which will override the default styles of the quiz.
3. **Find an element selector**:  To find a selector for the element, inspect it in your browser by right-clicking.
4. **Add specificity to your CSS rules**: You can add specificity to your CSS rules, so that they are applied only to the quiz or a certain question. For example:
    ```html
    #quiz  p {color: red;}
    ```

    will change the color of all the paragraphs in the quiz to red.

    ```html
    #question-AbC7Zde  p {color: red;}
    ```

    will change the color of a paragraph to red ONLY for question `AbC7Zde`, where `AbC7Zde` is the question ID. You can find a specific question ID in Quiz Builder > [Question setttings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).

5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

### Upload a Google Font

1. **Find a Google Font**: To upload a custom Google Font to the quiz, first navigate to the font’s page. For example: [Quicksand](https://fonts.google.com/specimen/Quicksand).
2. **Copy Font code**: Then, select the styles you want to be applied and copy the import font URL and font family CSS rules.
3. **Write CSS code**: To add a Google font to the quiz elements (h1-h6, p) use this sample code:
    ```html
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

    h1, h2, h3, h4, h5, h6, p, button, div{
    font-family: 'Quicksand', sans-serif ;
    }
    ```
5. **Paste the code in Quiz Design > CSS console**: Navigate to the Quiz Design > Custom CSS section of the app and paste the code into the custom CSS field on top of the stylesheet.
6. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

## Styling Quiz Text

You can use [Markdown Language](https://docs.revenuehunt.com/how-to-guides/use-markdown/) for basic styling of text in the quiz. 

??? question "What is Markdown Languge?"
        
    Markdown is a way to style text on the web. You control the display of the document; formatting words as bold or italic, adding images, and creating lists are just a few of the things we can do with Markdown. Mostly, Markdown is just regular text with a few non-alphabetic characters, like `#` or `*`.

If you need to include additional styling and elements in your questions, choices, and results page, you can do so using Markdown Language.

- **Headings**
    ```html
    # H1
    ## H2
    ### H3
    ```
- **Text Styling**
    ```html
    *italic text*  
    **bold text**  
    ***italic & bold text***  
    ```
- **Links**
    ```html
    [link title](https://www.example.com)
    ```
- **Images**
    ```html
    ![alt text](https://www.example.com/path/to/image.jpg)
    ```
- **Videos**
    ```html
    ![](https://youtu.be/0_tO8HgJiLQ)  
    ```

If you want to change the font or the color of certain texts or whole paragraphs, you may need to use [Custom CSS](#add-custom-css-code) code for that. 

## Adding Images and Videos

You can add images to your quiz in serveral ways. 

- **Upload images/videos via question settings**: You can add a unique image to every question through the Quiz Builder by accessing the [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).
- **Embed images/videos via Markdown Language**: You can embed unique ijmages or videos into text blocks in your question description or the resutls page with Markdown language.
    - Images:
    ```html
    ![alt text](https://www.example.com/path/to/image.jpg)
    ```
    - Videos
    ```html
    ![](https://youtu.be/0_tO8HgJiLQ)  
    ```


## Individual Question Design

In addition to the overall Quiz Design options, you can add a unique image to every question through the Quiz Builder by accessing the [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings).

The question settings also allow you to incorporate [custom JavaScript](https://docs.revenuehunt.com/how-to-guides/add-javascript/) into your quiz design.

## Results Page Design

The Results Page also has its own customization options. 

!!! tip

    Check [this article](http://127.0.0.1:8000/how-to-guides/edit-results-page/) to learn more about styling your results page.

In addition to the basic elements, you can set a unique background image for each result page through the [results page settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings). You can also use these settings to apply [custom JavaScript](https://docs.revenuehunt.com/how-to-guides/add-javascript/) to your quiz design.

If you find the default results page too restrictive, you might want to **create a custom results page** on your site and direct all quiz data to it using the [Callback Function](https://docs.revenuehunt.com/how-to-guides/use-callback-function/). This function enables you to collect all quiz responses in JSON format on any page you choose.

## Customization Examples

We offer complete flexibility to developers for personalizing both the quiz and the results page. Take a look at [these examples](https://revenuehunt.com/templates/#customization) to discover the various designs you can achieve with our app using some creativity and CSS code.

## Useful CSS Codes

Here are a few popular CSS selectors and codes to style elements in the quiz:

- Hide Progress Bar in the footer
    ```html
    /* Hide Progress Bar in the footer */
    .lq-progress-box{
    display: none;
    }
    ```
- Change the styles of the choices
    ```html
    /* Change the styles of the choices */
    li.lq-choice, li.lq-choice{
    /* your CSS rules go here */
    }
    ```
- Change the styles of the picture choices
    ```html
    .lq-images li.lq-choice, .lq-images li.lq-choice{
    /* your CSS rules go here */
    }
    ```
-  Place the footer bar at the top, for more visibility
    ```html
    .lq-footer, .lq-footer{
    position: absolute;
    width: 100%;
    top: 0;
    margin: 0;
    }
    ```
- Make "Back" and "Next" arrows point left and right
    ```html
    #nav-next .fa, #nav-back .fa {
        -webkit-transform: rotate(-90deg);
        -moz-transform: rotate(-90deg);
        -o-transform: rotate(-90deg);
        -ms-transform: rotate(-90deg);
        transform: rotate(-90deg);
    }
    ```
- Adding a custom font (you'll have to host the font in your server). If your fonts are hosted within your Shopify store, they' may appear as a "private" fonts or hosted within a site restricted for us. If you want to use that font it'd have to be hosted elsewhere, and that way you could implement them within the quiz. Alternatively, check [Upload Google Font](#upload-a-google-font).
    ```html
    @font-face {
    font-family: "Morion";
    src: url("https://yourwebsite.com/wp-content/themes/yourtheme/fonts/Morion-Light.woff2") format("woff2");
    );
    }
    h1, h2, h3, h4, h5, h6, .widget h1, .widget h2, .widget h3, .widget h4, .widget h5, .widget h6{
    font-family: Morion, serif;
    }
    ```
- Hide the "add all to cart" button 
    ```html
    /*Hide the "add all to cart" button */

    .lq-checkout.lq-add-all-to-cart {
        display: none;
    }
    ```
- Hide the product variants
    ```html
    /* this hides the product variants */
    .no-variants-dropdown {
    display: none;
    }
    .lq-variants-dropdown {
    display: none;
    }
    .lq-results .el-input, .lq-results .el-input__inner {
    display: none;
    }
    ```
-  Adds quiz border
    ```html
    /* Adds quiz border */
    .lq-quiz {
    border-style: solid;
    border-color: red;
    }
    ```
- Change Picture Choices to Icons
    ```html
    /* Change Picture Choices to Icons */

    .lq-images li, .widget .lq-images li{
    max-width: none !important;
    }

    .lq-choices .lq-img, .widget .lq-choices .lq-img{
    width: 48px !important;
    height: 48px !important;
    padding-top: 0 !important;
    background-size: 48px !important;
    background-position: left;
    margin-top: 4px;
    margin-right: 8px;
    margin-bottom: 2px;
    }

    .lq-picture-choice .lq-letter{
    display: none;
    }

    .lq-picture-choice li div{
    width: calc(100% - 65px) !important;
    margin-top: 12px;
    }

    @media (pointer: fine) {
    .lq-picture-choice li:hover{
    background-color: #333 !important;
    }

    .lq-picture-choice li:hover div{color: #fff !important;
    }

    .lq-picture-choice li:hover .lq-img{
    content: "";
    width: 100%;
    height: 100%;
    background-color:black;
    filter: invert(100%);
    -webkit-filter: invert(100%);
    }
    }

    .lq-images li, .widget .lq-images li{
    width: calc(100% - 8px) !important;
    }

    @media (min-width: 768px) {
    .builder-container-preview .lq-images li, .widget .lq-images li{
    width: calc(50% - 8px) !important;
    }
    }
    ```
- Muliptle choice questions: change the selected options background
    ```html
    /* Muliptle choice questions: change the selected options background */
    li.lq-selected .lq-letter {
    background-color: gray;
    }
    ```
- Change the color of the Retake Quiz text
    ```html
    /* Change the color of the Retake Quiz text */
    .lq-retake-quiz {
    color: black;
    }
    ```
- Change the background of the Add to Cart button
    ```html
    /* Change the background of the Add to Cart button */
    .lq-checkout {
    background-color: #ff7028;
    }
    ```
- Change the background of the singluar Add to cart buttons
    ```html
    /* Change the background of the singluar Add to cart buttons */
    .lq-btn-content {
    background-color: #ff7028;
    color: white;
    }
    ```


