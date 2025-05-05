---
icon: material/palette-outline
---

# How to Customize the Quiz Design

You can change the quiz's appearance to fit your store's style. 

Use the customization options in the [Quiz Design](/reference/quiz-builder/quiz-design/) tab or add your own style with [CSS](#add-custom-css-code) or [JavaScript](/how-to-guides/add-javascript/). You can modify any part of the quiz or results page with custom CSS.

Remember, you can also include custom images and styles for each question via the [question settings](/reference/quiz-builder/questions/#question-settings).

## Quiz Design Tab

=== "Shopify"

    1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
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

=== "Shopify V2"

    ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign.png)

    In the [Quiz Design](/reference/quiz-builder/quiz-design/) section of the quiz builder you can change how the quiz `Questions` or the `Results Page` look. 
    
    ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_toggle](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_toggle.png)

    Switch between previews of the quiz questions and the results page to see your customizations in action as you edit.

    Choose from a selection of predefined color schemes for your quiz or click `Change` to pick a new scheme. 
    
    ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_colorscheme](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_colorscheme.png)
    
    This allows you to set a tone that resonates with your brand’s identity.

    The Quiz Design section is divided into two main customization categories: **`Basic`** and **`Advanced`**.

    **Basic Customizations**

    In the `Basic` customization menu, you can adjust fundamental design elements such as colors, fonts, backgrounds, and navigation.

    !!! info

        In Shopify V2, the font for the headings and body of the quiz is inherited from the store Shopify theme.

    - **Font**: Select a font from the available list to give your quiz a unique character.
    - **Primary Colors / Choices / Inputs**: Click on any color block to bring up a color picker and adjust hues to your preference.

        ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_colors_picker](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_colors_picker.png)
    - **Background**: Customize your quiz background by selecting a color or uploading an image. You can also adjust opacity to achieve the desired visual effect.

        ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_background](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_background.png)
    - **Navigation**: Change the colors of the navigation bar’s background and border for consistency across the user experience.
    - **Progress Indicators**: Enable or disable the progress bar and percentage text as needed.
    - **Arrows and Transitions**: Set the orientation and style of arrows and transitions to enhance user interaction.
    - **Animations**: Choose from various animations to add smooth transitions between questions, enhancing user engagement.

        ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_animations](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_animations.png)

=== "WooCommerce"

    1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
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

=== "Magento"

    1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
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

=== "BigCommerce"

    1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
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

=== "Standalone"

    1. **Open Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab. In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.
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

=== "Shopify"

    Via the CSS console, you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS.

    1. **Open the Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
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

        will change the color of a paragraph to red ONLY for question `AbC7Zde`, where `AbC7Zde` is the question ID. You can find a specific question ID in Quiz Builder > [Question setttings](/reference/quiz-builder/questions/#question-settings).

    5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

=== "Shopify V2"

    **Advanced Customizations**

    For those with coding knowledge, the `Advanced` customization panel within the [Quiz Design](/reference/quiz-builder/quiz-design/) offers the flexibility to input custom CSS, allowing you to override the default styles. This option provides maximum control over every detail of your quiz’s appearance.

    ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_advanced](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_advanced.png)

    - **Find an Element Selector**: To target a specific element in your quiz, right-click on it in your browser and select `Inspect` to view the element’s selector.

    - **Add Specificity to CSS Rules**: Use specific selectors to apply styles only to particular parts of your quiz. For example:
    ```css
    #quiz p { color: red; }
    ```
        This rule will change the color of all paragraphs in the quiz to red.

        To style a paragraph in only one specific question, use the question's unique ID:

        ```css
        #question-AbC7Zde p { color: red; }
        ```
        In this case, the color of the paragraph will change to red only for the question with ID `AbC7Zde`. You can find a question’s ID in [`Quiz Builder > Question Settings`](/reference/quiz-builder/questions/#question-settings).

    - Once you've made your changes, click the `Save` button at the top right to apply them to your live or preview quiz.

    To add custom CSS code to a speciifc quiz section only, go to [`Question Settings`](/reference/quiz-builder/questions/#question-settings) or [`Results Page Settings`](/reference/quiz-builder/results-page/).

=== "WooCommerce"

    Via the CSS console, you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS.

    1. **Open the Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
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

        will change the color of a paragraph to red ONLY for question `AbC7Zde`, where `AbC7Zde` is the question ID. You can find a specific question ID in Quiz Builder > [Question setttings](/reference/quiz-builder/questions/#question-settings).

    5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

=== "Magento"

    Via the CSS console, you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS.

    1. **Open the Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
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

        will change the color of a paragraph to red ONLY for question `AbC7Zde`, where `AbC7Zde` is the question ID. You can find a specific question ID in Quiz Builder > [Question setttings](/reference/quiz-builder/questions/#question-settings).

    5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

=== "BigCommerce"

    Via the CSS console, you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS.

    1. **Open the Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
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

        will change the color of a paragraph to red ONLY for question `AbC7Zde`, where `AbC7Zde` is the question ID. You can find a specific question ID in Quiz Builder > [Question setttings](/reference/quiz-builder/questions/#question-settings).

    5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

=== "Standalone"

    Via the CSS console, you can add any custom styling rules. Any element of the quiz or the resutls page can be customized via CSS.

    1. **Open the Quiz Design tab**: Open your quiz and navigate to the [Quiz Design](/reference/quiz-builder/quiz-design/) tab.
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

        will change the color of a paragraph to red ONLY for question `AbC7Zde`, where `AbC7Zde` is the question ID. You can find a specific question ID in Quiz Builder > [Question setttings](/reference/quiz-builder/questions/#question-settings).

    5. **Publish the changes**: Click the top-right `Publish` button to apply the changes to the preview/live quiz.

### Upload a Google Font

1. **Find a Google Font**: To upload a custom Google Font to the quiz, first navigate to the font’s page. For example: [Quicksand](https://fonts.google.com/specimen/Quicksand).
2. **Copy Font code**: Then, select the styles you want to be applied and copy the import font URL and font family CSS rules.
3. **Write CSS code**: To add a Google font to the quiz elements (h1-h6, p) use this sample code:
    ```html
    @import url('https://fonts.googleapis.com/css2?family=Quicksand&display=swap');

    .quicksand-font {
    font-family: "Quicksand", serif;
    font-optical-sizing: auto;
    font-weight: 400;
    font-style: normal;
    }

    h1, h2, h3, h4, h5, h6, p, button, div{
    font-family: 'Quicksand', sans-serif ;
    }
    ```
5. **Paste the code in Quiz Design > CSS console**: Navigate to the Quiz Design > Custom CSS section of the app and paste the code into the custom CSS field on top of the stylesheet.
6. **Publish the changes**: Click the top-right `Publish / Save` button to apply the changes to the preview/live quiz.

## Styling Quiz Text

=== "Shopify"

    You can use [Markdown Language](/how-to-guides/use-markdown/) for basic styling of text in the quiz. 

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

=== "Shopify V2"

    To personalize the text within each question, open the [**`Block Settings`**](/reference/quiz-builder/questions/#block-settings) for each content block. 
    
    Each block type — Heading, Text, or Button —has unique customization options that let you control the styling and positioning of text elements.

    **Heading Block**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_heading](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_heading.png)

    To add a heading to your question, select the `Heading` block. The `Block Settings` for the heading allow you to:

    - **Style Text**: You can bold, italicize, underline, or strikethrough text within the heading, as well as insert links and pull content dynamically from other parts of the quiz.
    - **Size and Alignment**: Adjust the heading size and choose from alignment options (left, center, or right) to fit your design needs.

    **Text Block**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_text](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_text.png)

    Use the `Text` block to add regular text content to your question. Within the [**`Block Settings`**](/reference/quiz-builder/questions/#block-settings) for text, you can:

    - **Format Text**: Similar to the heading block, you can bold, italicize, underline, or strikethrough text, add links, and dynamically source content.
    - **Size and Alignment**: Change the text size and alignment to suit the layout and readability of your quiz.

    **Button Block**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_button](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_button.png)

    To include a button within your question, select the `Button` block. The [**`Block Settings`**](/reference/quiz-builder/questions/#block-settings) for buttons allow you to:

    - **Button Text**: Customize the default text displayed on the button to reflect the action you want users to take.
    - **Button Alignment**: Adjust the button's position (left, center, or right) for a balanced layout within the quiz.

    By adjusting these settings, you can tailor the styling of each text element to enhance user experience and reinforce your brand’s design.

=== "WooCommerce"

    You can use [Markdown Language](/how-to-guides/use-markdown/) for basic styling of text in the quiz. 

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

=== "Magento"

    You can use [Markdown Language](/how-to-guides/use-markdown/) for basic styling of text in the quiz. 

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

=== "BigCommerce"

    You can use [Markdown Language](/how-to-guides/use-markdown/) for basic styling of text in the quiz. 

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

=== "Standalone"

    You can use [Markdown Language](/how-to-guides/use-markdown/) for basic styling of text in the quiz. 

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

=== "Shopify"

    You can add images to your quiz in serveral ways. 

    - **Upload images/videos via question settings**: You can add a unique image to every question through the Quiz Builder by accessing the [question settings](/reference/quiz-builder/questions/#question-settings).
    - **Embed images/videos via Markdown Language**: You can embed unique ijmages or videos into text blocks in your question description or the resutls page with Markdown language.
        - Images:
        ```html
        ![alt text](https://www.example.com/path/to/image.jpg)
        ```
        - Videos
        ```html
        ![](https://youtu.be/0_tO8HgJiLQ)  
        ```

=== "Shopify V2"

    Enhance your quiz with visual elements by using the **Image** and **Picture Choice** blocks. These options allow you to add standalone images or offer picture-based answer choices, making your quiz more engaging and visually appealing.

    **Image Block**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_image](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_image.png)

    To add an image within a question, use the `Image` block. The [**`Block Settings`**](/reference/quiz-builder/questions/#block-settings) for images offer the following customization options:

    - **Upload or Select an Image**: Click `Select image` to upload an image from your computer or choose from your in-app image gallery. Once uploaded, you can click `Change` to replace the image or `Remove` to delete it.
    - **Image Size**: Adjust the image height using the `Image height` dropdown to scale the image as needed.
    - **Alignment**: Use `Image Alignment` to position the image to the left, center, or right within the block for optimal layout.

    **Picture Choice Block**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice.png)

    The `Picture Choice` block lets you offer visual choices for multiple-choice questions, enhancing interactivity. [**`Block Settings`**](/reference/quiz-builder/questions/#block-settings) for picture choices include:

    - **Picture Size/Ratio**: Choose the size and aspect ratio of the images in this block, from Tiny icon (24px), Small icon (48px), Medium (1:1), or Large (4:3).
    - **Hide Checkbox/Radio**: Hide the checkbox or radio selection indicator for picture choices.
    - **Hide Image Label**: Hide the text label displayed under each picture choice for a cleaner design.

    To upload an image to each choice, open the [**`Choice Settings`**](/reference/quiz-builder/questions/#choice-settings).

    **Adding a Background Image**

    You can add a background image to a specific question or to the entire quiz.

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage.png)

    To add a background image to a specific question go to the [**`Question Settings`**](/reference/quiz-builder/questions/#question-settings):

    - **Select a Background Image**: Click `Select image` in the question management settings, then click `Add image` to upload a background image from your computer. Alternatively, choose an existing image from your quiz gallery. Once uploaded, click `Change` to replace the image or `Remove` to delete it.
    - **Background Position**: Set the image to cover the entire background or split the screen, displaying the image on one half and content on the other.
    - **Background Opacity**: Adjust the opacity of the background image using the slider to control transparency and blend it with the quiz content.

    To add a background image to the whole quiz open the [Quiz Design](#quiz-design-tab) tab.

    These settings allow you to control how images appear and interact within your quiz, making it visually engaging.

=== "WooCommerce"

    You can add images to your quiz in serveral ways. 

    - **Upload images/videos via question settings**: You can add a unique image to every question through the Quiz Builder by accessing the [question settings](/reference/quiz-builder/questions/#question-settings).
    - **Embed images/videos via Markdown Language**: You can embed unique ijmages or videos into text blocks in your question description or the resutls page with Markdown language.
        - Images:
        ```html
        ![alt text](https://www.example.com/path/to/image.jpg)
        ```
        - Videos
        ```html
        ![](https://youtu.be/0_tO8HgJiLQ)  
        ```

=== "Magento"

    You can add images to your quiz in serveral ways. 

    - **Upload images/videos via question settings**: You can add a unique image to every question through the Quiz Builder by accessing the [question settings](/reference/quiz-builder/questions/#question-settings).
    - **Embed images/videos via Markdown Language**: You can embed unique ijmages or videos into text blocks in your question description or the resutls page with Markdown language.
        - Images:
        ```html
        ![alt text](https://www.example.com/path/to/image.jpg)
        ```
        - Videos
        ```html
        ![](https://youtu.be/0_tO8HgJiLQ)  
        ```

=== "BigCommerce"

    You can add images to your quiz in serveral ways. 

    - **Upload images/videos via question settings**: You can add a unique image to every question through the Quiz Builder by accessing the [question settings](/reference/quiz-builder/questions/#question-settings).
    - **Embed images/videos via Markdown Language**: You can embed unique ijmages or videos into text blocks in your question description or the resutls page with Markdown language.
        - Images:
        ```html
        ![alt text](https://www.example.com/path/to/image.jpg)
        ```
        - Videos
        ```html
        ![](https://youtu.be/0_tO8HgJiLQ)  
        ```

=== "Standalone"

    You can add images to your quiz in serveral ways. 

    - **Upload images/videos via question settings**: You can add a unique image to every question through the Quiz Builder by accessing the [question settings](/reference/quiz-builder/questions/#question-settings).
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

In addition to the overall Quiz Design options, you can add a unique image to every question through the Quiz Builder by accessing the [question settings](/reference/quiz-builder/questions/#question-settings).

The question settings also allow you to incorporate [custom JavaScript](/how-to-guides/add-javascript/) into your quiz design.

## Results Page Design

The Results Page also has its own customization options. 

!!! tip

    Check [this article](/how-to-guides/edit-results-page/) to learn more about styling your results page.

In addition to the basic elements, you can set a unique background image for each result page through the [results page settings](/reference/quiz-builder/results-page/). You can also use these settings to apply [custom JavaScript](/how-to-guides/add-javascript/) to your quiz design.

If you find the default results page too restrictive, you might want to **create a custom results page** on your site and direct all quiz data to it using the [Callback Function](/how-to-guides/use-callback-function/). This function enables you to collect all quiz responses in JSON format on any page you choose.

## Customization Examples

We offer complete flexibility to developers for personalizing both the quiz and the results page. Take a look at [these examples](https://revenuehunt.com/templates/#customization) to discover the various designs you can achieve with our app using some creativity and CSS code.

## Useful CSS Codes

=== "Shopify"

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

=== "Shopify V2"

=== "WooCommerce"

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

=== "Magento"

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

=== "BigCommerce"

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

=== "Standalone"

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
