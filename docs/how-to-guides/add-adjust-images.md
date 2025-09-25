---
icon: material/image-area
---


# How to Add and Adjust Images in the Quiz


There are several ways you can add images to your quiz in the RevenueHunt app.

This article explains how you can add images to your quiz and provides tips on how to optimize the image quality for the best quiz performance.


## Images in the Quiz

There are the different ways you can add images to your quiz in the RevenueHunt app:

- **[Quiz Background image](/how-to-guides/add-adjust-images/#quiz-background-image)** - You can uplaod a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

- **[Question Background/Split image](/how-to-guides/add-adjust-images/#question-backgroundsplit-image)** - You can upload a background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).

- **[Image Block](/how-to-guides/add-adjust-images/#image-blocks)** - You can upload an individual image via an Image Block directly into one of the quiz [questions](/reference/quiz-builder/questions/) or [results page](/reference/quiz-builder/results-page/).

- **[Picture Choice](/how-to-guides/add-adjust-images/#picture-choices)** - You can add a [Picture Choice block](/reference/quiz-builder/questions/#picture-choice) to your question, which will allow you to add an image to each choice in that multiple choice question.

- **[Product Image](/how-to-guides/add-adjust-images/#product-image)** - You can also add a [Product/Variants/Collection Block](/reference/quiz-builder/results-page/#product-image-in-productvariantscollection-blocks) to your quiz results page, which will allow you to display a product/variant/collection image in the results page.


### Quiz Background Image

=== "Shopify"

    You can upload a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. Open your quiz and navigate to the [Quiz Design tab](/reference/quiz-builder/quiz-design/). In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.

    2. Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

        `Background` - Opens a color menu that allows you to change the color of the quiz background. You can add a custom color by pasting the #number of the color (for example, #ecb3b3).
        
        `Background image` - Click "Add" to upload a background image. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated.

        `Background Opacity` - A slider that allows you to adjust the opacity of the uploaded background image.

    !!! tip "Background image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload a background image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different background images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod a different background image for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/RNFq-2HCRro?si=4xZDwSz-GxDNlE7H" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can upload a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_shopifyv2_improve_image_quality_backgroudimagequiz](/images/how_to_shopifyv2_improve_image_quality_backgroudimagequiz.png)

    1. Open the [Quiz Design tab](/reference/quiz-builder/quiz-design/)

    2. Click on `Background`

    3. Change the background color by clicking on the color. 

        !!! tip "Background color"

            The color of the background matters if you want to adjust the image opacity. A light colored background will make the image more visible, while a dark background will make the image more subtle. 

    5. Upload a background image by clicking `Select image`.

    4. Adjust the background opacity with the slider.

    6. Once uploaded, click `Change` to change the image or `Remove` to remove it. 

    !!! tip "Background image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use large, high-resolution images: at least 1920x1080px (Full HD)

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!

=== "WooCommerce"


    You can upload a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. Open your quiz and navigate to the [Quiz Design tab](/reference/quiz-builder/quiz-design/). In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.

    2. Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

        `Background` - Opens a color menu that allows you to change the color of the quiz background. You can add a custom color by pasting the #number of the color (for example, #ecb3b3).
        
        `Background image` - Click "Add" to upload a background image. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated.

        `Background Opacity` - A slider that allows you to adjust the opacity of the uploaded background image.

    !!! tip "Background image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload a background image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different background images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod a different background image for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Magento"


    You can upload a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. Open your quiz and navigate to the [Quiz Design tab](/reference/quiz-builder/quiz-design/). In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.

    2. Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

        `Background` - Opens a color menu that allows you to change the color of the quiz background. You can add a custom color by pasting the #number of the color (for example, #ecb3b3).
        
        `Background image` - Click "Add" to upload a background image. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated.

        `Background Opacity` - A slider that allows you to adjust the opacity of the uploaded background image.

    !!! tip "Background image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload a background image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different background images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod a different background image for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "BigCommerce"


    You can upload a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. Open your quiz and navigate to the [Quiz Design tab](/reference/quiz-builder/quiz-design/). In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.

    2. Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

        `Background` - Opens a color menu that allows you to change the color of the quiz background. You can add a custom color by pasting the #number of the color (for example, #ecb3b3).
        
        `Background image` - Click "Add" to upload a background image. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated.

        `Background Opacity` - A slider that allows you to adjust the opacity of the uploaded background image.

    !!! tip "Background image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload a background image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different background images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod a different background image for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Standalone"


    You can upload a background image for the whole quiz via the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. Open your quiz and navigate to the [Quiz Design tab](/reference/quiz-builder/quiz-design/). In the Quiz Design section of the quiz builder you can change how the quiz Questions or the Results Page look.

    2. Our theme editor allows you to pick one of our multiple color palettes, choose from multiple fonts and add a default background image to your quiz.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

        `Background` - Opens a color menu that allows you to change the color of the quiz background. You can add a custom color by pasting the #number of the color (for example, #ecb3b3).
        
        `Background image` - Click "Add" to upload a background image. Image should be max 1000px x 1000px and 2MB. An extra menu appears once activated.

        `Background Opacity` - A slider that allows you to adjust the opacity of the uploaded background image.

    !!! tip "Background image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload a background image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different background images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod a different background image for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```



### Question Background/Split Image

=== "Shopify"

    You can upload a different background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).  

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and click on the question you want to add an image to.

    2. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    3. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question. An extra menu appears once activated.

        `above` - Places the uplaoded image above the question, on top of the slide.

        `below` - Places the uplaoded image below the question, above the choices.

        `background` - Places the uplaoded image on the background of the slide (overrides the defautl quiz background).

        `split` - Places the uploaded image on the side of the slide. Splits the sldie into two. On mobile, the image is placed on top of the question.

        `Image Opacity` - A slider which allows to adjust the opacity of the uplaoded image.

    
    !!! tip "Uploaded image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **uploaded images may crop or scale differently depending on the device**.

        To ensure your uploaded images look great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload  a background/split image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod different images for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```



=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/rQEVMLzez2U?si=HoNlj3KwQ67yKAUk" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can upload a different background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).  

    ![how_to_shopifyv2_improve_image_quality_backgroudimagequestion](/images/how_to_shopifyv2_improve_image_quality_backgroudimagequestion.png)

    1. Open the [Question settings](/reference/quiz-builder/questions/#picture-choice)

    2. Click on `Image upload`

    3. Click `Select image` to upload a background image to this quiz question from your computer. You can also chose from existing images from your quiz gallery.

    4. In `Image position` you can choose between two options: `background` (for a full background image) or `split` (for a split image).  Each option has it's own settings explained below.

    5. Once uploaded click `Change`to change the image or `Remove` to remove it. 

    6. You can also adjust the `Image opacity` with the slider.

    !!! tip "Background/Split image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **background images may crop or scale differently depending on the device**.

        To ensure your background looks great across all devices, we recommend:

        ✅ Use large, high-resolution images: at least 1920x1080px (Full HD)

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!

    **Background image settings**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage.png){width="300"}

    `Image layout` - Place the image as a `background` or `split` the screen in half with the image. 

    `Image opacity` - Use the slider to change opacity percentage of the uplaoded image.

    **Split image settings**

    ![manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_splitimage](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_splitimage.png)

    `Image layout` - Place the image as a `background` or `split` the screen in half with the image. 

    `Image opacity` - Use the slider to change opacity percentage of the uplaoded image.

    `Image position (desktop)` - Choose whether the image should be placed `left` or `right` of the question on desktop.

    `Image position (mobile)` - Choose whether the image should be placed `above`, `below` a question or `hidden` on mobile.

    !!! tip
        Switch between the desktop and mobile view by clicking the `desktop` or `mobile` icon in the top right corner of the middle screen.

=== "WooCommerce"

    You can upload a different background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).  

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and click on the question you want to add an image to.

    2. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    3. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question. Image should be max 1000px x 1000px. An extra menu appears once activated.

        `above` - Places the uplaoded image above the question, on top of the slide.

        `below` - Places the uplaoded image below the question, above the choices.

        `background` - Places the uplaoded image on the background of the slide (overrides the defautl quiz background).

        `split` - Places the uploaded image on the side of the slide. Splits the sldie into two. On mobile, the image is placed on top of the question.

        `Image Opacity` - A slider which allows to adjust the opacity of the uplaoded image.


    !!! tip "Uploaded image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **uploaded images may crop or scale differently depending on the device**.

        To ensure your uploaded images look great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload  a background/split image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod different images for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Magento"

    You can upload a different background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).  

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and click on the question you want to add an image to.

    2. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    3. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question. Image should be max 1000px x 1000px. An extra menu appears once activated.

        `above` - Places the uplaoded image above the question, on top of the slide.

        `below` - Places the uplaoded image below the question, above the choices.

        `background` - Places the uplaoded image on the background of the slide (overrides the defautl quiz background).

        `split` - Places the uploaded image on the side of the slide. Splits the sldie into two. On mobile, the image is placed on top of the question.

        `Image Opacity` - A slider which allows to adjust the opacity of the uplaoded image.


    !!! tip "Uploaded image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **uploaded images may crop or scale differently depending on the device**.

        To ensure your uploaded images look great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload  a background/split image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod different images for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "BigCommerce"

    You can upload a different background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).  

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and click on the question you want to add an image to.

    2. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    3. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question. Image should be max 1000px x 1000px. An extra menu appears once activated.

        `above` - Places the uplaoded image above the question, on top of the slide.

        `below` - Places the uplaoded image below the question, above the choices.

        `background` - Places the uplaoded image on the background of the slide (overrides the defautl quiz background).

        `split` - Places the uploaded image on the side of the slide. Splits the sldie into two. On mobile, the image is placed on top of the question.

        `Image Opacity` - A slider which allows to adjust the opacity of the uplaoded image.


    !!! tip "Uploaded image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **uploaded images may crop or scale differently depending on the device**.

        To ensure your uploaded images look great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload  a background/split image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod different images for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Standalone"

    You can upload a different background image to each question in the quiz via the [question settings](/reference/quiz-builder/questions/#picture-choice).  

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. Go to the [Quiz Builder](/reference/quiz-builder/) and click on the question you want to add an image to.

    2. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    3. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question. Image should be max 1000px x 1000px. An extra menu appears once activated.

        `above` - Places the uplaoded image above the question, on top of the slide.

        `below` - Places the uplaoded image below the question, above the choices.

        `background` - Places the uplaoded image on the background of the slide (overrides the defautl quiz background).

        `split` - Places the uploaded image on the side of the slide. Splits the sldie into two. On mobile, the image is placed on top of the question.

        `Image Opacity` - A slider which allows to adjust the opacity of the uplaoded image.



    !!! tip "Uploaded image Tip"

        Our app uses a **responsive design**, meaning your quiz will adjust to different screen sizes (desktop, tablet, and mobile). Because of this, **uploaded images may crop or scale differently depending on the device**.

        To ensure your uploaded images look great across all devices, we recommend:

        ✅ Use high-resolution images of **max. 1000px x 1000px size**.

        ✅ Avoid images with text — it might be cut off or obscured

        ✅ If needed, keep important elements (like logos or text) centered

        ✅ Use soft, neutral backgrounds that won’t clash with quiz content

        ✅ Test your quiz on different devices to see how the image behaves

        Remember, simpler is often better for responsive backgrounds!     

    !!! tip "Higher resolution images"
        
        You can use [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css) to upload  a background/split image for the whole quiz in a desired resolution.

        Sample code:

        ```html	
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "Different images for mobile and desktop"

        With Custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css), you can also uplaod different images for mobile and desktop. For this your developer can use CSS media queries to target different screen sizes.

        Sample code:

        ```html
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```




### Image Blocks

=== "Shopify"

    **QUESTIONS**

    You can upload images to quiz questions via the [question settings](/reference/quiz-builder/questions/#picture-choice) or using [Markdowns](/how-to-guides/use-markdown/) in the Question Description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    **Add Image via Question settings**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question from your computer.

    5. Select the image orientation to be either `above`, `below`, `background` or `split`.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Activate the `question description` toggle.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.


    **RESULTS PAGE**

    You can also uplad images to the [Results page](/reference/quiz-builder/results-page/) via Image Block on the Results page or using [Markdowns](/how-to-guides/use-markdown/) in the Content blocks.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    **Add Image via Image Block**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Click on `Image` block and a new block will be added to the results page.

    5. Click `Add` to upload an image from your computer. You can adjust the image opacity with the slider.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Select a `Content` block.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Cg-85oQ1mPA?si=vqCVMwIC4jDM3ITy" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can upload an individual image via an Image Block directly into one of the quiz [questions](/reference/quiz-builder/questions/) or [results page](/reference/quiz-builder/results-page/).

    ![how to](/images/how_to_shopifyv2_improve_image_quality_imageblock.png)

    1. Navigate to [Questions](/reference/quiz-builder/questions/) or [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.
    2. Click `+ Add block` to see a list of available blocks.

    3. Click on `Image` block and a new block will be added to the question or a section on the results page.

    4. Open the Image block settings.

    5. Click `Select image` to upload an image from your computer or pick one from your in-app image gallery.

    6. Once uploaded, click `Change` to replace the image or `Remove` to delete it. 

    7. Add in `Alt text` to make the image more accessible. *Note: Alt text is used by screen readers to describe the image to visually impaired users.*

    8. You can adjust the image size in the `Image height`dropdown. You can choose between `Tiny`, `Small`, `Medium`, `Large` or `Adapt to image`. 

        !!! tip "Adapt to image"

            `Adapt to image` will adjust the image size to the original size of the image. Pick this option if you want to keep the original image size and resolution.

    9. You can change the alignement of the image left, right or center.

=== "WooCommerce"

    **QUESTIONS**

    You can upload images to quiz questions via the [question settings](/reference/quiz-builder/questions/#picture-choice) or using [Markdowns](/how-to-guides/use-markdown/) in the Question Description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    **Add Image via Question settings**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question from your computer.

    5. Select the image orientation to be either `above`, `below`, `background` or `split`.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Activate the `question description` toggle.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.


    **RESULTS PAGE**

    You can also uplad images to the [Results page](/reference/quiz-builder/results-page/) via Image Block on the Results page or using [Markdowns](/how-to-guides/use-markdown/) in the Content blocks.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    **Add Image via Image Block**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Click on `Image` block and a new block will be added to the results page.

    5. Click `Add` to upload an image from your computer. You can adjust the image opacity with the slider.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Select a `Content` block.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.

=== "Magento"

    **QUESTIONS**

    You can upload images to quiz questions via the [question settings](/reference/quiz-builder/questions/#picture-choice) or using [Markdowns](/how-to-guides/use-markdown/) in the Question Description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    **Add Image via Question settings**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question from your computer.

    5. Select the image orientation to be either `above`, `below`, `background` or `split`.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Activate the `question description` toggle.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.


    **RESULTS PAGE**

    You can also uplad images to the [Results page](/reference/quiz-builder/results-page/) via Image Block on the Results page or using [Markdowns](/how-to-guides/use-markdown/) in the Content blocks.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    **Add Image via Image Block**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Click on `Image` block and a new block will be added to the results page.

    5. Click `Add` to upload an image from your computer. You can adjust the image opacity with the slider.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Select a `Content` block.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.

=== "BigCommerce"

    **QUESTIONS**

    You can upload images to quiz questions via the [question settings](/reference/quiz-builder/questions/#picture-choice) or using [Markdowns](/how-to-guides/use-markdown/) in the Question Description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    **Add Image via Question settings**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question from your computer.

    5. Select the image orientation to be either `above`, `below`, `background` or `split`.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Activate the `question description` toggle.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.


    **RESULTS PAGE**

    You can also uplad images to the [Results page](/reference/quiz-builder/results-page/) via Image Block on the Results page or using [Markdowns](/how-to-guides/use-markdown/) in the Content blocks.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    **Add Image via Image Block**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Click on `Image` block and a new block will be added to the results page.

    5. Click `Add` to upload an image from your computer. You can adjust the image opacity with the slider.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Select a `Content` block.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.

=== "Standalone"

    **QUESTIONS**

    You can upload images to quiz questions via the [question settings](/reference/quiz-builder/questions/#picture-choice) or using [Markdowns](/how-to-guides/use-markdown/) in the Question Description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    **Add Image via Question settings**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Find the `Image` section in the question settings and click `Add` to upload a featured image to the question from your computer.

    5. Select the image orientation to be either `above`, `below`, `background` or `split`.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Click on the question you want to add an image to.

    3. Click on the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).

    4. Activate the `question description` toggle.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.


    **RESULTS PAGE**

    You can also uplad images to the [Results page](/reference/quiz-builder/results-page/) via Image Block on the Results page or using [Markdowns](/how-to-guides/use-markdown/) in the Content blocks.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    **Add Image via Image Block**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Click on `Image` block and a new block will be added to the results page.

    5. Click `Add` to upload an image from your computer. You can adjust the image opacity with the slider.

    6. Click `Publish` to save the changes.

    **Add Image via Markdown**

    1. Open the [Quiz Builder](/reference/quiz-builder/).

    2. Go the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    3. Click on the `+ Add block` button to see a list of available blocks.

    4. Select a `Content` block.

    5. In the new text field that appears, add the following markdown code:

        ```markdown	
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace `https://your-image-url.com/image.jpg` with the URL of the image you want to upload.

    6. Click `Publish` to save the changes.



### Picture Choices

=== "Shopify"

    You can add a Picture Choice block to your question, which will allow you to add an image to each choice in that multiple choice question.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click `+ Add new question` to see a list of available questions.

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Click on `Picture choice` to add a picture choice block to the question. Pictures Choices are a Multiple choice slide which displays choices as clickable images. You can uplaod your own image to each choice. 

        !!! warning "Image size"

            It'sd recommended to uplaod square images, max. 400px x 400px.

            If your images are not square, they will be cropped to a square. You can adjust them in a free online image editor before uploading.

            RevenueHunt app optimizes the uploaded images to load faster.

    4. Click on `+ Add choice` to add a new choice to the picture choice block.

    5. Click on `+ image` to upload an image from your computer.

    6. Add more choices by clicking `+ Add choice` and repeat the process.


=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/pRIPY4pLoMw?si=EbnsHRRnzSf_NKHX" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can add a Picture Choice block to your question, which will allow you to add an image to each choice in that multiple choice question.

    ![how_to_shopifyv2_improve_image_quality_picturechoicequestions](/images/how_to_shopifyv2_improve_image_quality_picturechoicequestions.png)

    1. Open the [Question settings](/reference/quiz-builder/questions/#picture-choice)

    2. Click `+ Add question` to see a list of available questions or `+ Add block` to see a list of available blocks.

    3. Click on `Picture choice` to add a picture choice block to the question.

    4. Click on `+ Add choice` to add a new choice to the picture choice block.

    5. Click on `Select image` to upload an image from your computer or pick one from your in-app image gallery.

    6. Once uploaded, click `Change` to replace the image or `Remove` to delete it. 

    6. Open the [`Picture Choice Settings`](/reference/quiz-builder/questions/#picture-choice) and go the Advanced settings.

    7. Under `Picture size/ratio` you can choose between `Tiny icon 24px`, `Small icon 48px`, `Medium icon 1:1` or `Large icon 4:3`.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice_picturesizeratio](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice_picturesizeratio.png)

        If you select `Medium (1:1)` in the `Picture size/ratio` dropdown, an additional option for chosing a Mobile layout will appear. There you can choose how this block will be displayed on mobile devices - either as a `Carousel`, `One per row` or `Two per row`.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice_mobilelayout](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice_mobilelayout.png)

    8. You can also check the:

        - `Hide checkbox/radio` to hide the checkbox/radio element from picture choices.
        - `Hide image label` to hide the text below each picture choice.
        - `Fit full image in box (no cropping)` to display the image in the box without cropping.

    9. You can also enable the horizontal carousel on mobile by checking the `Enable horizontal carousel on mobile` option. 

        !!! tip
            Make sure to switch to the mobile view by clicking the `mobile` icon in the top right corner of the middle screen.

=== "WooCommerce"

    You can add a Picture Choice block to your question, which will allow you to add an image to each choice in that multiple choice question.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click `+ Add new question` to see a list of available questions.

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Click on `Picture choice` to add a picture choice block to the question. Pictures Choices are a Multiple choice slide which displays choices as clickable images. You can uplaod your own image to each choice. 

        !!! warning "Image size"

            It'sd recommended to uplaod square images, max. 400px x 400px.

            If your images are not square, they will be cropped to a square. You can adjust them in a free online image editor before uploading.

            RevenueHunt app optimizes the uploaded images to load faster.

    4. Click on `+ Add choice` to add a new choice to the picture choice block.

    5. Click on `+ image` to upload an image from your computer.

    6. Add more choices by clicking `+ Add choice` and repeat the process.

=== "Magento"

    You can add a Picture Choice block to your question, which will allow you to add an image to each choice in that multiple choice question.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click `+ Add new question` to see a list of available questions.

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Click on `Picture choice` to add a picture choice block to the question. Pictures Choices are a Multiple choice slide which displays choices as clickable images. You can uplaod your own image to each choice. 

        !!! warning "Image size"

            It'sd recommended to uplaod square images, max. 400px x 400px.

            If your images are not square, they will be cropped to a square. You can adjust them in a free online image editor before uploading.

            RevenueHunt app optimizes the uploaded images to load faster.

    4. Click on `+ Add choice` to add a new choice to the picture choice block.

    5. Click on `+ image` to upload an image from your computer.

    6. Add more choices by clicking `+ Add choice` and repeat the process.

=== "BigCommerce"

    You can add a Picture Choice block to your question, which will allow you to add an image to each choice in that multiple choice question.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click `+ Add new question` to see a list of available questions.

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Click on `Picture choice` to add a picture choice block to the question. Pictures Choices are a Multiple choice slide which displays choices as clickable images. You can uplaod your own image to each choice. 

        !!! warning "Image size"

            It'sd recommended to uplaod square images, max. 400px x 400px.

            If your images are not square, they will be cropped to a square. You can adjust them in a free online image editor before uploading.

            RevenueHunt app optimizes the uploaded images to load faster.

    4. Click on `+ Add choice` to add a new choice to the picture choice block.

    5. Click on `+ image` to upload an image from your computer.

    6. Add more choices by clicking `+ Add choice` and repeat the process.

=== "Standalone"

    You can add a Picture Choice block to your question, which will allow you to add an image to each choice in that multiple choice question.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Click `+ Add new question` to see a list of available questions.

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Click on `Picture choice` to add a picture choice block to the question. Pictures Choices are a Multiple choice slide which displays choices as clickable images. You can uplaod your own image to each choice. 

        !!! warning "Image size"

            It'sd recommended to uplaod square images, max. 400px x 400px.

            If your images are not square, they will be cropped to a square. You can adjust them in a free online image editor before uploading.

            RevenueHunt app optimizes the uploaded images to load faster.

    4. Click on `+ Add choice` to add a new choice to the picture choice block.

    5. Click on `+ image` to upload an image from your computer.

    6. Add more choices by clicking `+ Add choice` and repeat the process.




### Product Image 

=== "Shopify"

    Product Images displayed on the Results page are taken directly from your Shopify catalog. Product slots diplsay the first image of the product or variant uploaded to your Shopify Products section.

    !!! tip

        You can adjust the product image settings with custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css).

        Sample code to adjust the product image size:

        ```html
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/CeN1xrE3XpE?si=9nNUSjPGJDreQctq" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    You can add a Product/Variants/Collection Block to your quiz results page, which will allow you to display a product image in the results page.

    ![how_to_shopifyv2_improve_image_quality_productimages](/images/how_to_shopifyv2_improve_image_quality_productimages.png    )

    1. Navigate to [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.

    2. Click `+ Add block` to see a list of available blocks.

    3. Click on `Product` (or `Variant` or `Collection`) block and a new block will be added to the results page.

    4. Open the [Product/Variant/Collection block settings](/reference/quiz-builder/results-page/#products-products-variants-collections).

    5. Under [`Product components layout`](/reference/quiz-builder/results-page/#product-components-layout) you can select which elements of the product slot should be displayed. Click and drag an element to change it's position within the slot.

    6. Under `+ Add block` you can add an extra block to the product slot. All the data are synced directly from your Shopify catalog.

    7. Under `Image` you can adjust the image size.

        `Picture size/ratio` - Choose the picture size for this block. Choose between `Medium (1:1)` or `Original` picture size (as uploaded to your Shopify Product).

        `Optimize images size` - Select this option to optimize the image size for the quiz. If unchecked, the image will be displayed in the original size.

        !!! note
            Product images are taken directly from your Shopify catalog. Product slots diplsay the first image of the product, variant or a collection as uploaded to your Shopify Products/Collections section. 


        !!! tip
            If you don't see any images when recommending collections, make sure that you have uploaded images to your Shopify collection.


=== "WooCommerce"

    Product Images displayed on the Results page are taken directly from your WooCommerce catalog. Product slots diplsay the first image of the product or variant uploaded to your WooCommerce Products section.

    !!! tip

        You can adjust the product image settings with custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css).

        Sample code to adjust the product image size:

        ```html
        .lq-results .lq-slot li {
            max-width: 500px !important;        
        }
        ```

=== "Magento"

    Product Images displayed on the Results page are taken directly from your Magento catalog. Product slots diplsay the first image of the product or variant uploaded to your Magento Products section.

    !!! tip

        You can adjust the product image settings with custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css).

        Sample code to adjust the product image size:

        ```html 
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

=== "BigCommerce"

    Product Images displayed on the Results page are taken directly from your BigCommerce catalog. Product slots diplsay the first image of the product or variant uploaded to your BigCommerce Products section.

    !!! tip

        You can adjust the product image settings with custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css).

        Sample code to adjust the product image size:

        ```html
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ``` 

=== "Standalone"

    Product Images displayed on the Results page are taken directly from your Standalone catalog or Google Product Feed. Product slots diplsay the first image of the product or variant uploaded to your Standalone Products section or Google Product Feed.

    !!! tip

        You can adjust the product image settings with custom CSS in [Quiz Design > Custom CSS console](/reference/quiz-builder/quiz-design/#custom-css).

        Sample code to adjust the product image size:

        ```html
        .lq-results .lq-slot li {   
            max-width: 500px !important;
        }
        ```




---
This article explains how you can add images to your quiz and provides tips on how to optimize the image quality for the best quiz performance.
