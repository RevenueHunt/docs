---
description: "How to add and edit the welcome screen (welcome page) of your RevenueHunt quiz - the intro slide with your headline, image and Start button."
icon: material/page-layout-header
---

# How to Add a Welcome Screen to Your Quiz

The welcome screen is the first slide of your quiz: a short headline, a line of supporting text and a button that starts the quiz. Merchants also call it the welcome page, the welcome slide or the start screen. In the Quiz Builder it is a question type called `Welcome Message`.

A welcome screen is optional. If your quiz doesn't have one, it opens directly on your first question.

!!! tip "Why it's worth adding"

    The welcome screen is where customers decide whether the quiz is worth their time. Tell them what they get and how long it takes. See [How to Reduce Quiz Drop-off](/customer-success/reduce-dropoff/) for what to put on it.

## Add a welcome screen

=== "Shopify"

    1. Open your quiz in the **Quiz Builder**.
    2. Click `+ Add question`.
    3. Under **Messages**, choose `Welcome Message`.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_welcome](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_welcome.png){width="500"}

    4. Click `Save` in the top-right corner to update the preview and the live quiz.

=== "Shopify (Legacy)"

    1. Open your quiz in the **Quiz Builder**.
    2. Click `+` / `Add new question`.

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Choose `Welcome Message`.
    4. Click `Publish` in the top menu to update the preview and the live quiz.

=== "WooCommerce"

    1. Open your quiz in the **Quiz Builder**.
    2. Click `+` / `Add new question`.

        ![quiz builder add questions](/images/manual_quizbuilder_quizbuilder_addquestions.png){width="300"}

    3. Choose `Welcome Message`.
    4. Click `Publish` in the top menu to update the preview and the live quiz.

=== "Magento"

    1. Open your quiz in the **Quiz Builder**.
    2. Click `+` / `Add new question`.
    3. Choose `Welcome Message`.
    4. Click `Publish` in the top menu to update the preview and the live quiz.

=== "BigCommerce"

    1. Open your quiz in the **Quiz Builder**.
    2. Click `+` / `Add new question`.
    3. Choose `Welcome Message`.
    4. Click `Publish` in the top menu to update the preview and the live quiz.

=== "Standalone"

    1. Open your quiz in the **Quiz Builder**.
    2. Click `+` / `Add new question`.
    3. Choose `Welcome Message`.
    4. Click `Publish` in the top menu to update the preview and the live quiz.

!!! note

    The welcome screen has to be the first slide in your question list to show before your questions. If you add it to an existing quiz, check its position in the list.

## Write the welcome copy

=== "Shopify"

    The welcome screen is built from [blocks](/reference/quiz-builder/questions/#block-settings), the same way every other slide is.

    - Click the `Heading` block to write your main line, and set its `Size` and `Alignment`.
    - Click the `Text` block for the supporting sentence. To add one, click `+ Add block` and choose `Text`.
    - Both blocks support [information recalls](/how-to-guides/use-information-recalls/) and [Liquid templates](/reference/quiz-builder/questions/#liquid-templates) if you want to pull in dynamic content.

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "Shopify (Legacy)"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Type your main line in the question field on the slide.
    3. Toggle `Show Description` on to reveal a second text field below it, and add your supporting sentence there.

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "WooCommerce"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Type your main line in the question field on the slide.
    3. Toggle `Show Description` on to reveal a second text field below it, and add your supporting sentence there.

    Keep it to one clear promise and one line of detail. Long welcome copy is a common cause of drop-off.

=== "Magento"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Type your main line in the question field on the slide.
    3. Toggle `Show Description` on to reveal a second text field below it, and add your supporting sentence there.

=== "BigCommerce"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Type your main line in the question field on the slide.
    3. Toggle `Show Description` on to reveal a second text field below it, and add your supporting sentence there.

=== "Standalone"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Type your main line in the question field on the slide.
    3. Toggle `Show Description` on to reveal a second text field below it, and add your supporting sentence there.

## Add a logo or a background image

=== "Shopify"

    **For a logo or an inline image**, click `+ Add block`, choose `Image`, and upload your file. The image sits in the flow of the slide with the rest of your blocks.

    **For a background or split-screen image**, click the slide to open its settings, then use `Image upload`:

    1. Click `Select image`, then `Add image` in the popup, and upload your file. You can also pick from images already in your quiz gallery.
    2. Set `Layout` to `background` to place it behind the text, or `split` to put it beside the text.
    3. Use `Opacity` to fade it back so your copy stays readable.
    4. For `split`, set `Position (desktop)` to `left` or `right`, and `Position (mobile)` to `above`, `below` or `hidden`.

    See [How to Add/Adjust Images](/how-to-guides/add-adjust-images/) for sizing recommendations.

=== "Shopify (Legacy)"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Next to `Image`, click `Add` and upload your file. Images should be a maximum of 1000px x 1000px.
    3. Choose the placement:

        - `above` - on top of the slide, above your text.
        - `below` - under your text.
        - `background` - behind everything, replacing the default quiz background.
        - `split` - beside your text, splitting the slide in two. On mobile the image moves to the top.

    4. Use `Image Opacity` to fade the image back so your copy stays readable.

    You can also add a `Video` here instead, as a `responsive`, `widget` or `background` element.

=== "WooCommerce"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Next to `Image`, click `Add` and upload your file. Images should be a maximum of 1000px x 1000px.
    3. Choose the placement: `above`, `below`, `background` or `split`.
    4. Use `Image Opacity` to fade the image back so your copy stays readable.

    You can also add a `Video` here instead, as a `responsive`, `widget` or `background` element.

=== "Magento"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Next to `Image`, click `Add` and upload your file. Images should be a maximum of 1000px x 1000px.
    3. Choose the placement: `above`, `below`, `background` or `split`.
    4. Use `Image Opacity` to fade the image back so your copy stays readable.

=== "BigCommerce"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Next to `Image`, click `Add` and upload your file. Images should be a maximum of 1000px x 1000px.
    3. Choose the placement: `above`, `below`, `background` or `split`.
    4. Use `Image Opacity` to fade the image back so your copy stays readable.

=== "Standalone"

    1. Click the slide, then open `question settings` / the `wrench icon`.
    2. Next to `Image`, click `Add` and upload your file. Images should be a maximum of 1000px x 1000px.
    3. Choose the placement: `above`, `below`, `background` or `split`.
    4. Use `Image Opacity` to fade the image back so your copy stays readable.

## Change the Start button text

=== "Shopify"

    Click the `Button` block on the slide and edit `Button text`. Use `Alignment` to move it left, right or center.

    Write the button as the action the customer is taking - "Find my match" or "Start the quiz" - rather than a bare "Next".

=== "Shopify (Legacy)"

    Click the slide, open `question settings` / the `wrench icon`, and edit `Button Text`.

    Write the button as the action the customer is taking - "Find my match" or "Start the quiz" - rather than a bare "Next".

=== "WooCommerce"

    Click the slide, open `question settings` / the `wrench icon`, and edit `Button Text`.

    Write the button as the action the customer is taking - "Find my match" or "Start the quiz" - rather than a bare "Next".

=== "Magento"

    Click the slide, open `question settings` / the `wrench icon`, and edit `Button Text`.

=== "BigCommerce"

    Click the slide, open `question settings` / the `wrench icon`, and edit `Button Text`.

=== "Standalone"

    Click the slide, open `question settings` / the `wrench icon`, and edit `Button Text`.

## Remove the welcome screen

Removing the welcome screen makes your first question the first thing customers see.

=== "Shopify"

    Click the slide to open its settings, click `...`, then click `Remove`. To keep it but reuse it later, click `Duplicate` first.

=== "Shopify (Legacy)"

    Click the slide, open `more options` / `...`, then click `Delete`. Click `Duplicate` instead if you want to keep a copy.

=== "WooCommerce"

    Click the slide, open `more options` / `...`, then click `Delete`. Click `Duplicate` instead if you want to keep a copy.

=== "Magento"

    Click the slide, open `more options` / `...`, then click `Delete`.

=== "BigCommerce"

    Click the slide, open `more options` / `...`, then click `Delete`.

=== "Standalone"

    Click the slide, open `more options` / `...`, then click `Delete`.

## Related guides

- [Create Your First Quiz](/how-to-guides/create-first-quiz/)
- [Customize Quiz Design](/how-to-guides/customize-quiz-design/)
- [Add & Adjust Images](/how-to-guides/add-adjust-images/)
- [How to Reduce Quiz Drop-off](/customer-success/reduce-dropoff/)
- [Quiz Builder - Questions reference](/reference/quiz-builder/questions/)
