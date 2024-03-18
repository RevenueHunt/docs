# How to Customize the Quiz Design

You can edit the quiz design to match your store’s look & feel. To do that, you can use our built-in customization oprions in the Quiz Design tab or add your own custom styling via the CSS or JavaScript console. Any elemnt of the quiz or the resutls apge can be edited with custom CSS code.

Keep in mind that you can add custom images and styling rules to each question via the question settings.

## Quiz Design Tab

1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-design) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
2. **Customize the look**: You can choose from any of our pre-designed themes in the `My Themes` tab or create your own. 
3. **Edit Theme**: Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.
    ![quiz builder quiz design edit theme](/images/manual_quizbuilder_quizdesign_edittheme.png)

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
    ![quiz builder quiz design my themes](/images/manual_quizbuilder_quizdesign_mythemes.png)

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

## Individual Question Settings

Besides the global Quiz Design settings you can also upload a custom image to each question individually via the [question settings](https://docs.revenuehunt.com/reference/quiz-builder/#question-settings). Additionally, it's possible to add custom JavaScript.

## Results Page Settings


If you find our app's resutls page to be a bit limiting, you can also consider building your own resutls page in your store and directing all the quiz data there via the [Callback Function](). The Callback function allows you to receive all the quiz data in a JSON format on any page you want.

## Customization Examples

Check out [these examples](https://revenuehunt.com/templates/#customization) to see what designs are possible with our app.

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


