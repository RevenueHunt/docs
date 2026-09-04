---
description: "Learn how to add and adjust images in your RevenueHunt quiz to improve visual appeal and optimize image quality for better performance."
icon: material/image-area
---

# How to Add and Adjust Images in the Quiz

A quiz can carry images in five places, and each one is set up differently.

This article explains how to add each kind, and how to keep the images sharp on every screen.

## Images in the quiz

- **[Quiz background image](#quiz-background-image)** sits behind the whole quiz. You upload it in the [Quiz design tab](/reference/quiz-builder/quiz-design/).

- **[Question background or split image](#question-backgroundsplit-image)** sits behind one question, or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

- **[Image block](#image-blocks)** places a single picture inside a [question](/reference/quiz-builder/questions/) or on the [results page](/reference/quiz-builder/results-page/).

- **[Picture choice](#picture-choices)** gives every choice in a multiple-choice question its own image. See the [Picture choice block](/reference/quiz-builder/questions/#picture-choice).

- **[Product image](#product-image)** comes from your catalog, and shows in a [Product, Variants or Collection block](/reference/quiz-builder/results-page/#product-product-variants-collections) on the results page.

### Quiz background image

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/RNFq-2HCRro?si=4xZDwSz-GxDNlE7H" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The background image sits behind the whole quiz. You upload it in the [Quiz design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_shopifyv2_improve_image_quality_backgroudimagequiz](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign.png)

    1. **Open the [Quiz design tab](/reference/quiz-builder/quiz-design/).**

    2. **Click `Background`.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_background](/images/manual_shopifyV2_quizbuilder_quizbuilder_quizdesign_basic_background_imageuploaded.png)

    3. **Click the color to change the background color.**

        !!! tip "Pick the color before the image"

            The background color shows through the image once you lower its opacity. A light color leaves the image clearer, a dark one makes it subtler.

    4. **Click `Select image` and upload the background image.**

    5. **Set how strongly it shows with the opacity slider.**

    6. **Click `Change` to swap the image later, or `Remove` to take it out.**

    !!! tip "Background images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a large, high-resolution image, at least 1920x1080px.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

=== "Shopify (Legacy)"

    The background image sits behind the whole quiz. You upload it in the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. **Open your quiz and go to the [Quiz Design tab](/reference/quiz-builder/quiz-design/).** It controls how the Questions and the Results Page look.

    2. **Open the theme editor.** It holds the color palette, the font and the background image.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

    3. **Click `Background` and pick the background color.** To use a color of your own, paste its hex code, for example #ecb3b3.

    4. **Click `Add` next to `Background image` and upload the image.** It can be up to 1000x1000px and 2MB. A further menu appears once an image is there.

    5. **Set how strongly it shows with the `Background Opacity` slider.**

    !!! tip "Background images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "WooCommerce"

    The background image sits behind the whole quiz. You upload it in the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. **Open your quiz and go to the [Quiz Design tab](/reference/quiz-builder/quiz-design/).** It controls how the Questions and the Results Page look.

    2. **Open the theme editor.** It holds the color palette, the font and the background image.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

    3. **Click `Background` and pick the background color.** To use a color of your own, paste its hex code, for example #ecb3b3.

    4. **Click `Add` next to `Background image` and upload the image.** It can be up to 1000x1000px and 2MB. A further menu appears once an image is there.

    5. **Set how strongly it shows with the `Background Opacity` slider.**

    !!! tip "Background images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Magento"

    The background image sits behind the whole quiz. You upload it in the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. **Open your quiz and go to the [Quiz Design tab](/reference/quiz-builder/quiz-design/).** It controls how the Questions and the Results Page look.

    2. **Open the theme editor.** It holds the color palette, the font and the background image.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

    3. **Click `Background` and pick the background color.** To use a color of your own, paste its hex code, for example #ecb3b3.

    4. **Click `Add` next to `Background image` and upload the image.** It can be up to 1000x1000px and 2MB. A further menu appears once an image is there.

    5. **Set how strongly it shows with the `Background Opacity` slider.**

    !!! tip "Background images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "BigCommerce"

    The background image sits behind the whole quiz. You upload it in the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. **Open your quiz and go to the [Quiz Design tab](/reference/quiz-builder/quiz-design/).** It controls how the Questions and the Results Page look.

    2. **Open the theme editor.** It holds the color palette, the font and the background image.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

    3. **Click `Background` and pick the background color.** To use a color of your own, paste its hex code, for example #ecb3b3.

    4. **Click `Add` next to `Background image` and upload the image.** It can be up to 1000x1000px and 2MB. A further menu appears once an image is there.

    5. **Set how strongly it shows with the `Background Opacity` slider.**

    !!! tip "Background images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Standalone"

    The background image sits behind the whole quiz. You upload it in the [Quiz Design tab](/reference/quiz-builder/quiz-design/).

    ![how_to_improve_image_quality_backgroudimagequiz](/images/how_to_improve_image_quality_backgroudimagequiz.png)

    1. **Open your quiz and go to the [Quiz Design tab](/reference/quiz-builder/quiz-design/).** It controls how the Questions and the Results Page look.

    2. **Open the theme editor.** It holds the color palette, the font and the background image.

        ![manual_quizbuilder_quizdesign_edittheme](/images/manual_quizbuilder_quizdesign_edittheme.png){width="300"}

    3. **Click `Background` and pick the background color.** To use a color of your own, paste its hex code, for example #ecb3b3.

    4. **Click `Add` next to `Background image` and upload the image.** It can be up to 1000x1000px and 2MB. A further menu appears once an image is there.

    5. **Set how strongly it shows with the `Background Opacity` slider.**

    !!! tip "Background images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

### Question background/split image

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/rQEVMLzez2U?si=HoNlj3KwQ67yKAUk" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Each question can carry its own image, either behind the question or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

    ![how_to_shopifyv2_improve_image_quality_backgroudimagequestion](/images/manual_shopifyV2_quizbuilder_quizbuilder_questionsettings.png)

    1. **Open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    2. **Click `Image upload`.**

    3. **Click `Select image` and upload the image.** You can also pick one you have already used, from the quiz gallery.

    4. **Choose `background` or `split` under `Image position`.** A background image sits behind the question, a split image takes half the screen.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage.png)

    5. **Set how strongly it shows with the `Image opacity` slider.**

    6. **Click `Change` to swap the image later, or `Remove` to take it out.**

    !!! tip "Question images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a large, high-resolution image, at least 1920x1080px.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    ??? info "The background and split image settings"

        **Background image**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_backgroundimage.png)

        `Layout` - Place the image behind the question as a `background`, or `split` the screen in half with it.

        `Opacity` - Sets how strongly the image shows.

        **Split image**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_splitimage](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questionsettings_splitimage.png)

        `Layout` - Place the image behind the question as a `background`, or `split` the screen in half with it.

        `Opacity` - Sets how strongly the image shows.

        `Position (desktop)` - Put the image `left` or `right` of the question on a desktop.

        `Position (mobile)` - Put the image `above` or `below` the question on a phone, or `hidden`.

        Switch between the two views with the `desktop` and `mobile` icons above the preview.

=== "Shopify (Legacy)"

    Each question can carry its own image, either behind the question or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. **Go to the [Quiz Builder](/reference/quiz-builder/) and click the question you want to illustrate.**

    2. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Find the `Image` section and click `Add` to upload the image.** It can be up to 1000x1000px. A further menu appears once an image is there.

    4. **Choose where the image goes.**

        `above` - Above the question, at the top of the slide.

        `below` - Below the question, above the choices.

        `background` - Behind the whole slide. This overrides the quiz background.

        `split` - Beside the question, dividing the slide in two. On a phone the image moves above the question.

    5. **Set how strongly it shows with the `Image Opacity` slider.**

    !!! tip "Question images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background or split image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "WooCommerce"

    Each question can carry its own image, either behind the question or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. **Go to the [Quiz Builder](/reference/quiz-builder/) and click the question you want to illustrate.**

    2. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Find the `Image` section and click `Add` to upload the image.** It can be up to 1000x1000px. A further menu appears once an image is there.

    4. **Choose where the image goes.**

        `above` - Above the question, at the top of the slide.

        `below` - Below the question, above the choices.

        `background` - Behind the whole slide. This overrides the quiz background.

        `split` - Beside the question, dividing the slide in two. On a phone the image moves above the question.

    5. **Set how strongly it shows with the `Image Opacity` slider.**

    !!! tip "Question images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background or split image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Magento"

    Each question can carry its own image, either behind the question or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. **Go to the [Quiz Builder](/reference/quiz-builder/) and click the question you want to illustrate.**

    2. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Find the `Image` section and click `Add` to upload the image.** It can be up to 1000x1000px. A further menu appears once an image is there.

    4. **Choose where the image goes.**

        `above` - Above the question, at the top of the slide.

        `below` - Below the question, above the choices.

        `background` - Behind the whole slide. This overrides the quiz background.

        `split` - Beside the question, dividing the slide in two. On a phone the image moves above the question.

    5. **Set how strongly it shows with the `Image Opacity` slider.**

    !!! tip "Question images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background or split image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "BigCommerce"

    Each question can carry its own image, either behind the question or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. **Go to the [Quiz Builder](/reference/quiz-builder/) and click the question you want to illustrate.**

    2. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Find the `Image` section and click `Add` to upload the image.** It can be up to 1000x1000px. A further menu appears once an image is there.

    4. **Choose where the image goes.**

        `above` - Above the question, at the top of the slide.

        `below` - Below the question, above the choices.

        `background` - Behind the whole slide. This overrides the quiz background.

        `split` - Beside the question, dividing the slide in two. On a phone the image moves above the question.

    5. **Set how strongly it shows with the `Image Opacity` slider.**

    !!! tip "Question images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background or split image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

=== "Standalone"

    Each question can carry its own image, either behind the question or beside it. You upload it in the [question settings](/reference/quiz-builder/questions/#question-settings).

    ![how_to_improve_image_quality_backgroudimagequestion](/images/how_to_improve_image_quality_backgroudimagequestion.png)

    1. **Go to the [Quiz Builder](/reference/quiz-builder/) and click the question you want to illustrate.**

    2. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Find the `Image` section and click `Add` to upload the image.** It can be up to 1000x1000px. A further menu appears once an image is there.

    4. **Choose where the image goes.**

        `above` - Above the question, at the top of the slide.

        `below` - Below the question, above the choices.

        `background` - Behind the whole slide. This overrides the quiz background.

        `split` - Beside the question, dividing the slide in two. On a phone the image moves above the question.

    5. **Set how strongly it shows with the `Image Opacity` slider.**

    !!! tip "Question images on small screens"

        The quiz is responsive, so it adjusts to desktop, tablet and mobile screens. The same image can crop or scale differently on each one.

        - Use a high-resolution image, up to 1000x1000px and 2MB.
        - Avoid images with text in them, because the text can be cut off.
        - Keep anything that matters, such as a logo, near the center.
        - Choose soft, neutral pictures that do not compete with the quiz text.
        - Open the quiz on a phone and a desktop before you publish it.

        A plain background usually survives every screen size best.

    !!! tip "A background or split image at a higher resolution"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can load a background image at whatever resolution you want.

        ```css
        .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
            background-image: url('https://your-image-url.com/image.jpg');
            background-size: cover;
            background-position: center;
        }
        ```

    !!! tip "A different image on mobile and desktop"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) can also load a different image per screen size. A developer writes a media query for the smaller screen.

        ```css
        @media (max-width: 768px) {
            .lq-bg-img, .lq-bg-img-only, .widget .lq-bg-img, .widget .lq-bg-img-only {
                background-image: url('https://your-image-url.com/image-mobile.jpg');
            }
        }
        ```

### Image blocks

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/Cg-85oQ1mPA?si=vqCVMwIC4jDM3ITy" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    An Image block places a single picture inside a [question](/reference/quiz-builder/questions/), or in a section of the [results page](/reference/quiz-builder/results-page/).

    ![how to](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_image.png)

    1. **Open the [Questions](/reference/quiz-builder/questions/) or [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.**

    2. **Click `+ Add block`.**

    3. **Click `Image`.** The block is added to the question, or to the section on the results page.

    4. **Open the block settings.**

    5. **Click `Select image` and upload the picture.** You can also pick one you have already used, from the quiz gallery.

    6. **Click `Change` to swap the image later, or `Remove` to take it out.**

    7. **Write the `Alt text`.** A screen reader reads it aloud to a customer who cannot see the image.

    8. **Set the size in the `Image height` dropdown.** The choices are `Tiny`, `Small`, `Medium`, `Large` and `Adapt to image`.

        !!! tip "Adapt to image"

            `Adapt to image` keeps the picture at the size you uploaded it, rather than fitting it to a preset height.

    9. **Align the image left, right or center.**

=== "Shopify (Legacy)"

    **In a question**

    You can put an image in a question through the [question settings](/reference/quiz-builder/questions/#question-settings), or with [Markdown](/how-to-guides/use-markdown/) in the question description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    *Through the question settings*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Find the `Image` section and click `Add` to upload the picture.**

    5. **Choose whether it goes `above`, `below`, in the `background` or in a `split`.**

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Turn on the `question description` toggle.**

    5. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    6. **Click the top-right `Publish` button.**

    **On the Results Page**

    You can put an image on the [Results Page](/reference/quiz-builder/results-page/) with an Image Block, or with [Markdown](/how-to-guides/use-markdown/) in a Content block.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    *With an Image Block*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block`.**

    4. **Click `Image`.** The block is added to the Results Page.

    5. **Click `Add` and upload the picture.** The slider next to it sets how strongly the image shows.

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block` and select a `Content` block.**

    4. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    5. **Click the top-right `Publish` button.**

=== "WooCommerce"

    **In a question**

    You can put an image in a question through the [question settings](/reference/quiz-builder/questions/#question-settings), or with [Markdown](/how-to-guides/use-markdown/) in the question description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    *Through the question settings*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Find the `Image` section and click `Add` to upload the picture.**

    5. **Choose whether it goes `above`, `below`, in the `background` or in a `split`.**

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Turn on the `question description` toggle.**

    5. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    6. **Click the top-right `Publish` button.**

    **On the Results Page**

    You can put an image on the [Results Page](/reference/quiz-builder/results-page/) with an Image Block, or with [Markdown](/how-to-guides/use-markdown/) in a Content block.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    *With an Image Block*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block`.**

    4. **Click `Image`.** The block is added to the Results Page.

    5. **Click `Add` and upload the picture.** The slider next to it sets how strongly the image shows.

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block` and select a `Content` block.**

    4. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    5. **Click the top-right `Publish` button.**

=== "Magento"

    **In a question**

    You can put an image in a question through the [question settings](/reference/quiz-builder/questions/#question-settings), or with [Markdown](/how-to-guides/use-markdown/) in the question description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    *Through the question settings*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Find the `Image` section and click `Add` to upload the picture.**

    5. **Choose whether it goes `above`, `below`, in the `background` or in a `split`.**

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Turn on the `question description` toggle.**

    5. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    6. **Click the top-right `Publish` button.**

    **On the Results Page**

    You can put an image on the [Results Page](/reference/quiz-builder/results-page/) with an Image Block, or with [Markdown](/how-to-guides/use-markdown/) in a Content block.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    *With an Image Block*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block`.**

    4. **Click `Image`.** The block is added to the Results Page.

    5. **Click `Add` and upload the picture.** The slider next to it sets how strongly the image shows.

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block` and select a `Content` block.**

    4. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    5. **Click the top-right `Publish` button.**

=== "BigCommerce"

    **In a question**

    You can put an image in a question through the [question settings](/reference/quiz-builder/questions/#question-settings), or with [Markdown](/how-to-guides/use-markdown/) in the question description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    *Through the question settings*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Find the `Image` section and click `Add` to upload the picture.**

    5. **Choose whether it goes `above`, `below`, in the `background` or in a `split`.**

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Turn on the `question description` toggle.**

    5. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    6. **Click the top-right `Publish` button.**

    **On the Results Page**

    You can put an image on the [Results Page](/reference/quiz-builder/results-page/) with an Image Block, or with [Markdown](/how-to-guides/use-markdown/) in a Content block.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    *With an Image Block*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block`.**

    4. **Click `Image`.** The block is added to the Results Page.

    5. **Click `Add` and upload the picture.** The slider next to it sets how strongly the image shows.

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block` and select a `Content` block.**

    4. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    5. **Click the top-right `Publish` button.**

=== "Standalone"

    **In a question**

    You can put an image in a question through the [question settings](/reference/quiz-builder/questions/#question-settings), or with [Markdown](/how-to-guides/use-markdown/) in the question description.

    ![how_to_improve_image_quality_imageblock](/images/how_to_improve_image_quality_imageblock.png)

    *Through the question settings*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Find the `Image` section and click `Add` to upload the picture.**

    5. **Choose whether it goes `above`, `below`, in the `background` or in a `split`.**

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click the question you want to illustrate.**

    3. **Click the `wrench` icon to open the [question settings](/reference/quiz-builder/questions/#question-settings).**

    4. **Turn on the `question description` toggle.**

    5. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    6. **Click the top-right `Publish` button.**

    **On the Results Page**

    You can put an image on the [Results Page](/reference/quiz-builder/results-page/) with an Image Block, or with [Markdown](/how-to-guides/use-markdown/) in a Content block.

    ![how_to_improve_image_quality_imageblock_resultspage](/images/how_to_improve_image_quality_imageblock_resultspage.png)

    *With an Image Block*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block`.**

    4. **Click `Image`.** The block is added to the Results Page.

    5. **Click `Add` and upload the picture.** The slider next to it sets how strongly the image shows.

    6. **Click the top-right `Publish` button.**

    *With Markdown*

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab.**

    3. **Click `+ Add block` and select a `Content` block.**

    4. **Write the image into the text field that appears.**

        ```markdown
        ![Image description](https://your-image-url.com/image.jpg)
        ```

        Replace the address with the address of your own image.

    5. **Click the top-right `Publish` button.**

### Picture choices

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/pRIPY4pLoMw?si=EbnsHRRnzSf_NKHX" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A Picture choice block gives every choice in a multiple-choice question its own image.

    ![how_to_shopifyv2_improve_image_quality_picturechoicequestions](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_blocksettings_picturechoice.png)

    1. **Open the question you want to illustrate, or click `+ Add question` to make a new one.**

    2. **Click `+ Add block`, then click `Picture choice`.**

    3. **Click `+ Add choice`.**

    4. **Click `Select image` and upload the picture for that choice.** You can also pick one you have already used, from the quiz gallery.

    5. **Click `Change` to swap the image later, or `Remove` to take it out.**

    6. **Repeat for every choice.**

    7. **Open the [`Picture Choice Settings`](/reference/quiz-builder/questions/#picture-choice) and go to the advanced settings.**

    8. **Pick a `Picture size/ratio`.** The choices are `Tiny icon 24px`, `Small icon 48px`, `Medium icon 1:1` and `Large icon 4:3`.

        !!! info "Medium adds a mobile layout setting"

            Choosing `Medium (1:1)` reveals a `Mobile layout` option, which shows the choices on a phone as a `Carousel`, `One per row` or `Two per row`.

    9. **Turn on any of the display options you need.**

        - `Hide checkbox/radio` takes the checkbox or radio button off each picture.
        - `Hide image label` takes the text off each picture.
        - `Fit full image in box (no cropping)` shows the whole picture rather than cropping it to the box.
        - `Enable horizontal carousel on mobile` turns the choices into a row a customer swipes through on a phone.

        !!! tip "Check the mobile options on the mobile view"

            Switch to it with the `mobile` icon above the preview.

=== "Shopify (Legacy)"

    A Picture Choice block gives every choice in a multiple-choice question its own image.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click `+ Add new question`.**

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Click `Picture choice`.** This is a multiple-choice slide whose choices are clickable images, each with a picture of your own.

    4. **Click `+ Add choice`.**

    5. **Click `+ image` and upload the picture for that choice.**

    6. **Repeat for every choice.**

    7. **Click the top-right `Publish` button.**

    !!! warning "Use square images"

        Square pictures up to 400x400px work best. A picture that is not square is cropped to a square. Crop it yourself in an image editor first, so the crop does not cut off what matters.

        The app compresses whatever you upload, so the quiz still loads quickly.

=== "WooCommerce"

    A Picture Choice block gives every choice in a multiple-choice question its own image.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click `+ Add new question`.**

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Click `Picture choice`.** This is a multiple-choice slide whose choices are clickable images, each with a picture of your own.

    4. **Click `+ Add choice`.**

    5. **Click `+ image` and upload the picture for that choice.**

    6. **Repeat for every choice.**

    7. **Click the top-right `Publish` button.**

    !!! warning "Use square images"

        Square pictures up to 400x400px work best. A picture that is not square is cropped to a square. Crop it yourself in an image editor first, so the crop does not cut off what matters.

        The app compresses whatever you upload, so the quiz still loads quickly.

=== "Magento"

    A Picture Choice block gives every choice in a multiple-choice question its own image.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click `+ Add new question`.**

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Click `Picture choice`.** This is a multiple-choice slide whose choices are clickable images, each with a picture of your own.

    4. **Click `+ Add choice`.**

    5. **Click `+ image` and upload the picture for that choice.**

    6. **Repeat for every choice.**

    7. **Click the top-right `Publish` button.**

    !!! warning "Use square images"

        Square pictures up to 400x400px work best. A picture that is not square is cropped to a square. Crop it yourself in an image editor first, so the crop does not cut off what matters.

        The app compresses whatever you upload, so the quiz still loads quickly.

=== "BigCommerce"

    A Picture Choice block gives every choice in a multiple-choice question its own image.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click `+ Add new question`.**

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Click `Picture choice`.** This is a multiple-choice slide whose choices are clickable images, each with a picture of your own.

    4. **Click `+ Add choice`.**

    5. **Click `+ image` and upload the picture for that choice.**

    6. **Repeat for every choice.**

    7. **Click the top-right `Publish` button.**

    !!! warning "Use square images"

        Square pictures up to 400x400px work best. A picture that is not square is cropped to a square. Crop it yourself in an image editor first, so the crop does not cut off what matters.

        The app compresses whatever you upload, so the quiz still loads quickly.

=== "Standalone"

    A Picture Choice block gives every choice in a multiple-choice question its own image.

    ![how_to_improve_image_quality_picturechoicequestions](/images/how_to_improve_image_quality_picturechoicequestions.png)

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Click `+ Add new question`.**

        ![manual_quizbuilder_quizbuilder_addquestions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Click `Picture choice`.** This is a multiple-choice slide whose choices are clickable images, each with a picture of your own.

    4. **Click `+ Add choice`.**

    5. **Click `+ image` and upload the picture for that choice.**

    6. **Repeat for every choice.**

    7. **Click the top-right `Publish` button.**

    !!! warning "Use square images"

        Square pictures up to 400x400px work best. A picture that is not square is cropped to a square. Crop it yourself in an image editor first, so the crop does not cut off what matters.

        The app compresses whatever you upload, so the quiz still loads quickly.

### Product image

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/CeN1xrE3XpE?si=9nNUSjPGJDreQctq" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A Product, Variants or Collection block shows a picture from your catalog on the results page.

    ![how_to_shopifyv2_improve_image_quality_productimages](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_products_slotitemcompositon1.png)

    1. **Open the [Results page](/reference/quiz-builder/results-page/) tab in the quiz builder.**

    2. **Click `+ Add block`.**

    3. **Click `Product`, `Variant` or `Collection`.** The block is added to the results page.

    4. **Open the [block settings](/reference/quiz-builder/results-page/#product-product-variants-collections).**

    5. **Choose which parts of the product to show, under [`Product components layout`](/reference/quiz-builder/results-page/#slot-item-composition).** Drag a part to move it up or down.

        ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_image](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_blocksettings_productcomponents_image.png)

    6. **Open `Image` and adjust how the picture is shown.**

        `Picture size/ratio` - `Medium (1:1)`, or `Original` as uploaded to Shopify.

        `Shape` - `Square` or `Original`.

        `Source` - `Variant` shows the picture of the selected variant, and falls back to the product picture when that variant has none. `Product` always shows the main product picture.

        `Optimize images size` - Compresses the picture for the quiz. Clear it to serve the picture at its original weight.

    !!! note "The pictures come from your catalog"

        A product slot shows the first picture of the product, variant or collection, exactly as uploaded to your Shopify products and collections. You cannot replace it from inside the quiz.

    !!! tip "No picture on a recommended collection"

        Check that the Shopify collection itself has an image.

=== "Shopify (Legacy)"

    Product pictures on the Results Page come straight from your Shopify catalog. A product slot shows the first picture of the product or variant, exactly as uploaded to your Shopify Products section.

    !!! tip "Change the size of a product picture"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can resize the slot.

        ```css
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

=== "WooCommerce"

    Product pictures on the Results Page come straight from your WooCommerce catalog. A product slot shows the first picture of the product or variant, exactly as uploaded to your WooCommerce Products section.

    !!! tip "Change the size of a product picture"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can resize the slot.

        ```css
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

=== "Magento"

    Product pictures on the Results Page come straight from your Magento catalog. A product slot shows the first picture of the product or variant, exactly as uploaded to your Magento Products section.

    !!! tip "Change the size of a product picture"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can resize the slot.

        ```css
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

=== "BigCommerce"

    Product pictures on the Results Page come straight from your BigCommerce catalog. A product slot shows the first picture of the product or variant, exactly as uploaded to your BigCommerce Products section.

    !!! tip "Change the size of a product picture"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can resize the slot.

        ```css
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

=== "Standalone"

    Product pictures on the Results Page come straight from your Standalone catalog or Google Product Feed. A product slot shows the first picture of the product or variant, exactly as uploaded to your Standalone Products section or Google Product Feed.

    !!! tip "Change the size of a product picture"

        The [Custom CSS console](/reference/quiz-builder/quiz-design/#edit-theme) in the Quiz Design tab can resize the slot.

        ```css
        .lq-results .lq-slot li {
            max-width: 500px !important;
        }
        ```

---

This article explains how to add a background image, a question image, an image block, picture choices and a product image to a quiz. It also covers image quality.