---
description: "How to add and edit the welcome screen (welcome page) of your RevenueHunt quiz - the intro slide with your headline, image and Start button."
icon: material/page-layout-header
---

# How to Add a Welcome Screen to Your Quiz

The welcome screen is the first slide of your quiz: a short headline, a line of supporting text and a button that starts the quiz. Merchants also call it the welcome page, the welcome slide or the start screen. In the Quiz builder it is a question type called `Welcome Message`.

A welcome screen is optional. Without one, the quiz opens on your first question.

!!! tip "Why it is worth adding"

    The welcome screen is where customers decide whether the quiz is worth their time. Tell them what they get and how long it takes. See [how to reduce quiz drop-off](/customer-success/reduce-dropoff/) for what to put on it.

## Add a welcome screen

=== "Shopify"

    1. **Open your quiz in the Quiz builder.**

    2. **Click `+ Add question`.**

    3. **Choose `Welcome Message`, under `Messages`.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_welcome](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_welcome.png){width="500"}

    4. **Click the top-right `Save` button.** This updates both the preview and the live quiz.

=== "Shopify (Legacy)"

    1. **Open your quiz in the Quiz Builder.**

    2. **Click `+` / `Add new question`.**

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Choose `Welcome Message`.**

    4. **Click `Publish` in the top menu.** This updates both the preview and the live quiz.

=== "WooCommerce"

    1. **Open your quiz in the Quiz Builder.**

    2. **Click `+` / `Add new question`.**

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Choose `Welcome Message`.**

    4. **Click `Publish` in the top menu.** This updates both the preview and the live quiz.

=== "Magento"

    1. **Open your quiz in the Quiz Builder.**

    2. **Click `+` / `Add new question`.**

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Choose `Welcome Message`.**

    4. **Click `Publish` in the top menu.** This updates both the preview and the live quiz.

=== "BigCommerce"

    1. **Open your quiz in the Quiz Builder.**

    2. **Click `+` / `Add new question`.**

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Choose `Welcome Message`.**

    4. **Click `Publish` in the top menu.** This updates both the preview and the live quiz.

=== "Standalone"

    1. **Open your quiz in the Quiz Builder.**

    2. **Click `+` / `Add new question`.**

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. **Choose `Welcome Message`.**

    4. **Click `Publish` in the top menu.** This updates both the preview and the live quiz.

!!! note "It has to be the first slide"

    The welcome screen only comes before your questions if it sits first in the question list. If you add one to a quiz you already built, check where it landed.

## Write the welcome copy

=== "Shopify"

    The welcome screen is built from [blocks](/reference/quiz-builder/questions/#block-settings), the same way every other slide is.

    - Click the `Heading` block to write your main line, and set its `Size` and `Alignment`.
    - Click `+ Add block` and choose `Text` for the supporting sentence.
    - Both blocks take [information recalls](/how-to-guides/use-information-recalls/) and [Liquid templates](/reference/quiz-builder/questions/#liquid-templates), if you want to pull in something dynamic.

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "Shopify (Legacy)"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Type your main line into the question field on the slide.**

    3. **Turn on `Show Description`, and write your supporting sentence in the field that appears below it.**

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "WooCommerce"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Type your main line into the question field on the slide.**

    3. **Turn on `Show Description`, and write your supporting sentence in the field that appears below it.**

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "Magento"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Type your main line into the question field on the slide.**

    3. **Turn on `Show Description`, and write your supporting sentence in the field that appears below it.**

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "BigCommerce"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Type your main line into the question field on the slide.**

    3. **Turn on `Show Description`, and write your supporting sentence in the field that appears below it.**

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "Standalone"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Type your main line into the question field on the slide.**

    3. **Turn on `Show Description`, and write your supporting sentence in the field that appears below it.**

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

## Add a logo or a background image

=== "Shopify"

    **For a logo or an inline image**

    Click `+ Add block`, choose `Image`, and upload your file. The image then sits in the flow of the slide, with the rest of your blocks.

    **For a background or split-screen image**

    1. **Click the slide to open its settings, then click `Image upload`.**

    2. **Click `Select image`, then `Add image` in the popup, and upload your file.** You can also pick one already in your quiz gallery.

    3. **Set `Layout` to `background` to place it behind the text, or `split` to put it beside the text.**

    4. **Fade it back with `Opacity`, so your copy stays readable.**

    5. **For a `split` image, set `Position (desktop)` and `Position (mobile)`.** On a desktop the image goes `left` or `right`, and on a phone it goes `above`, `below` or `hidden`.

    See [how to add/adjust images](/how-to-guides/add-adjust-images/) for what size to upload.

=== "Shopify (Legacy)"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Click `Add` next to `Image` and upload your file.** An image can be up to 1000px by 1000px.

    3. **Choose where the image goes.**

        `above` - On top of the slide, above your text.

        `below` - Under your text.

        `background` - Behind everything, replacing the default quiz background.

        `split` - Beside your text, splitting the slide in two. On a phone the image moves to the top.

    4. **Fade it back with `Image Opacity`, so your copy stays readable.**

    !!! tip "A video works here too"

        The same setting takes a video instead of an image, as a `responsive`, `widget` or `background` element.

    See [how to add/adjust images](/how-to-guides/add-adjust-images/) for what size to upload.

=== "WooCommerce"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Click `Add` next to `Image` and upload your file.** An image can be up to 1000px by 1000px.

    3. **Choose where the image goes.**

        `above` - On top of the slide, above your text.

        `below` - Under your text.

        `background` - Behind everything, replacing the default quiz background.

        `split` - Beside your text, splitting the slide in two. On a phone the image moves to the top.

    4. **Fade it back with `Image Opacity`, so your copy stays readable.**

    !!! tip "A video works here too"

        The same setting takes a video instead of an image, as a `responsive`, `widget` or `background` element.

    See [how to add/adjust images](/how-to-guides/add-adjust-images/) for what size to upload.

=== "Magento"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Click `Add` next to `Image` and upload your file.** An image can be up to 1000px by 1000px.

    3. **Choose where the image goes.**

        `above` - On top of the slide, above your text.

        `below` - Under your text.

        `background` - Behind everything, replacing the default quiz background.

        `split` - Beside your text, splitting the slide in two. On a phone the image moves to the top.

    4. **Fade it back with `Image Opacity`, so your copy stays readable.**

    !!! tip "A video works here too"

        The same setting takes a video instead of an image, as a `responsive`, `widget` or `background` element.

    See [how to add/adjust images](/how-to-guides/add-adjust-images/) for what size to upload.

=== "BigCommerce"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Click `Add` next to `Image` and upload your file.** An image can be up to 1000px by 1000px.

    3. **Choose where the image goes.**

        `above` - On top of the slide, above your text.

        `below` - Under your text.

        `background` - Behind everything, replacing the default quiz background.

        `split` - Beside your text, splitting the slide in two. On a phone the image moves to the top.

    4. **Fade it back with `Image Opacity`, so your copy stays readable.**

    !!! tip "A video works here too"

        The same setting takes a video instead of an image, as a `responsive`, `widget` or `background` element.

    See [how to add/adjust images](/how-to-guides/add-adjust-images/) for what size to upload.

=== "Standalone"

    1. **Click the slide, then click the `wrench` icon to open the question settings.**

    2. **Click `Add` next to `Image` and upload your file.** An image can be up to 1000px by 1000px.

    3. **Choose where the image goes.**

        `above` - On top of the slide, above your text.

        `below` - Under your text.

        `background` - Behind everything, replacing the default quiz background.

        `split` - Beside your text, splitting the slide in two. On a phone the image moves to the top.

    4. **Fade it back with `Image Opacity`, so your copy stays readable.**

    !!! tip "A video works here too"

        The same setting takes a video instead of an image, as a `responsive`, `widget` or `background` element.

    See [how to add/adjust images](/how-to-guides/add-adjust-images/) for what size to upload.

## Change the start button text

=== "Shopify"

    Click the `Button` block on the slide and edit `Button text`. `Alignment` moves it left, right or center.

=== "Shopify (Legacy)"

    Click the slide, click the `wrench` icon to open the question settings, and edit `Button Text`.

=== "WooCommerce"

    Click the slide, click the `wrench` icon to open the question settings, and edit `Button Text`.

=== "Magento"

    Click the slide, click the `wrench` icon to open the question settings, and edit `Button Text`.

=== "BigCommerce"

    Click the slide, click the `wrench` icon to open the question settings, and edit `Button Text`.

=== "Standalone"

    Click the slide, click the `wrench` icon to open the question settings, and edit `Button Text`.

!!! tip "Name the action, not the step"

    Write the button as the action the customer is taking, such as `Find my match` or `Start the quiz`, rather than a bare `Next`.

## Remove the welcome screen

Removing the welcome screen makes your first question the first thing customers see.

=== "Shopify"

    Click the slide to open its settings, click `...`, then click `Remove`. To keep it for later instead, click `Duplicate` first.

=== "Shopify (Legacy)"

    Click the slide, open `more options` / `...`, then click `Delete`. To keep a copy instead, click `Duplicate` first.

=== "WooCommerce"

    Click the slide, open `more options` / `...`, then click `Delete`. To keep a copy instead, click `Duplicate` first.

=== "Magento"

    Click the slide, open `more options` / `...`, then click `Delete`. To keep a copy instead, click `Duplicate` first.

=== "BigCommerce"

    Click the slide, open `more options` / `...`, then click `Delete`. To keep a copy instead, click `Duplicate` first.

=== "Standalone"

    Click the slide, open `more options` / `...`, then click `Delete`. To keep a copy instead, click `Duplicate` first.

## Related guides

- [Create Your First Quiz](/how-to-guides/create-first-quiz/)
- [Customize Quiz Design](/how-to-guides/customize-quiz-design/)
- [Add & Adjust Images](/how-to-guides/add-adjust-images/)
- [How to reduce quiz drop-off](/customer-success/reduce-dropoff/)
- [Quiz Builder - Questions reference](/reference/quiz-builder/questions/)

---

This article explains how to add a welcome screen to a quiz, what to put on it, and how to remove it again.