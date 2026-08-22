---
description: "CSS class reference for customizing RevenueHunt quizzes, with selectors for the Built for Shopify version and for the legacy version of the app."
---

# CSS Structure Reference Guide

This page lists the CSS classes and selectors in the RevenueHunt quiz app. Use
them to customize how your quizzes look.

!!! note "Two versions, two sets of selectors"

    The `💎 Built for Shopify` version and the legacy version of the app build
    their quiz markup differently. A selector from one version does not work on
    the other. Choose your platform tab in each section.

## Global CSS variables

=== "Shopify"

    !!! note "Theme variables are a legacy feature"

        The Built for Shopify version does not use this variable system. Set
        colors and fonts in Quiz design.

=== "Shopify (Legacy)"

    **Theme variables**

    The legacy app sets its theme with CSS variables on `:root`. The app updates
    them from the settings you choose in the Quiz Builder.

    | Variable | Description |
    |----------|-------------|
    | `--bg-col` | Main background color |
    | `--btn-bg` | Background color for buttons and progress bars |
    | `--btn-col` | Text color for buttons |
    | `--tit-col` | Color for questions and titles |
    | `--bg-li` | RGB values for answer choices, used with opacity |
    | `--font-txt` | Font for body text |
    | `--font-tit` | Font for titles |
    | `--bg-img` | Background image URL |

    **Examples**

    ```css
    /* Answer choice color at 15% opacity */
    .lq-choice {
        background: rgba(var(--bg-li), 0.15);
    }
    ```

=== "WooCommerce"

    **Theme variables**

    The legacy app sets its theme with CSS variables on `:root`. The app updates
    them from the settings you choose in the Quiz Builder.

    | Variable | Description |
    |----------|-------------|
    | `--bg-col` | Main background color |
    | `--btn-bg` | Background color for buttons and progress bars |
    | `--btn-col` | Text color for buttons |
    | `--tit-col` | Color for questions and titles |
    | `--bg-li` | RGB values for answer choices, used with opacity |
    | `--font-txt` | Font for body text |
    | `--font-tit` | Font for titles |
    | `--bg-img` | Background image URL |

    **Examples**

    ```css
    /* Answer choice color at 15% opacity */
    .lq-choice {
        background: rgba(var(--bg-li), 0.15);
    }
    ```

=== "Magento"

    **Theme variables**

    The legacy app sets its theme with CSS variables on `:root`. The app updates
    them from the settings you choose in the Quiz Builder.

    | Variable | Description |
    |----------|-------------|
    | `--bg-col` | Main background color |
    | `--btn-bg` | Background color for buttons and progress bars |
    | `--btn-col` | Text color for buttons |
    | `--tit-col` | Color for questions and titles |
    | `--bg-li` | RGB values for answer choices, used with opacity |
    | `--font-txt` | Font for body text |
    | `--font-tit` | Font for titles |
    | `--bg-img` | Background image URL |

    **Examples**

    ```css
    /* Answer choice color at 15% opacity */
    .lq-choice {
        background: rgba(var(--bg-li), 0.15);
    }
    ```

=== "BigCommerce"

    **Theme variables**

    The legacy app sets its theme with CSS variables on `:root`. The app updates
    them from the settings you choose in the Quiz Builder.

    | Variable | Description |
    |----------|-------------|
    | `--bg-col` | Main background color |
    | `--btn-bg` | Background color for buttons and progress bars |
    | `--btn-col` | Text color for buttons |
    | `--tit-col` | Color for questions and titles |
    | `--bg-li` | RGB values for answer choices, used with opacity |
    | `--font-txt` | Font for body text |
    | `--font-tit` | Font for titles |
    | `--bg-img` | Background image URL |

    **Examples**

    ```css
    /* Answer choice color at 15% opacity */
    .lq-choice {
        background: rgba(var(--bg-li), 0.15);
    }
    ```

=== "Standalone"

    **Theme variables**

    The legacy app sets its theme with CSS variables on `:root`. The app updates
    them from the settings you choose in the Quiz Builder.

    | Variable | Description |
    |----------|-------------|
    | `--bg-col` | Main background color |
    | `--btn-bg` | Background color for buttons and progress bars |
    | `--btn-col` | Text color for buttons |
    | `--tit-col` | Color for questions and titles |
    | `--bg-li` | RGB values for answer choices, used with opacity |
    | `--font-txt` | Font for body text |
    | `--font-tit` | Font for titles |
    | `--bg-img` | Background image URL |

    **Examples**

    ```css
    /* Answer choice color at 15% opacity */
    .lq-choice {
        background: rgba(var(--bg-li), 0.15);
    }
    ```

## Top-level container structure

=== "Shopify"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `main#quiz-{quizId}` | Main quiz container with dynamic ID |
    | `.quiz` | Base quiz class - always present |
    | `.mobile` | Applied when viewport < 480px |
    | `.quiz-question` | Applied when showing question pages |
    | `.quiz-result` | Applied when showing results pages |
    | `.quiz-modal` | Modal type quiz styling |
    | `.quiz-inline` | Inline type quiz styling |
    | `.use-font-family-heading` | When custom heading font is set |
    | `.use-font-family-body` | When custom body font is set |

    **Examples**

    ```css
    /* Style all quiz text */
    .quiz {
        font-size: 16px;
        line-height: 1.5;
    }

    /* Mobile-specific styling */
    .quiz.mobile {
        padding: 10px;
    }

    /* Target specific quiz instance */
    #quiz-abc123 {
        background: #f0f0f0;
    }
    ```

=== "Shopify (Legacy)"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.widget` | Top-level wrapper for the quiz |
    | `.builder-container-preview` | Top-level wrapper inside the Quiz Builder preview |
    | `.lq-quiz` | Main quiz container |
    | `.lq-slide` | An individual question or content slide |
    | `.lq-wrapper` | Inner padding container for content, usually 650px maximum width |
    | `.lq-box` | Vertically centered cell inside the slide |

    **Examples**

    ```css
    /* Adds quiz border */
    .lq-quiz {
        border-style: solid;
        border-color: red;
    }
    ```

=== "WooCommerce"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.widget` | Top-level wrapper for the quiz |
    | `.builder-container-preview` | Top-level wrapper inside the Quiz Builder preview |
    | `.lq-quiz` | Main quiz container |
    | `.lq-slide` | An individual question or content slide |
    | `.lq-wrapper` | Inner padding container for content, usually 650px maximum width |
    | `.lq-box` | Vertically centered cell inside the slide |

    **Examples**

    ```css
    /* Adds quiz border */
    .lq-quiz {
        border-style: solid;
        border-color: red;
    }
    ```

=== "Magento"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.widget` | Top-level wrapper for the quiz |
    | `.builder-container-preview` | Top-level wrapper inside the Quiz Builder preview |
    | `.lq-quiz` | Main quiz container |
    | `.lq-slide` | An individual question or content slide |
    | `.lq-wrapper` | Inner padding container for content, usually 650px maximum width |
    | `.lq-box` | Vertically centered cell inside the slide |

    **Examples**

    ```css
    /* Adds quiz border */
    .lq-quiz {
        border-style: solid;
        border-color: red;
    }
    ```

=== "BigCommerce"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.widget` | Top-level wrapper for the quiz |
    | `.builder-container-preview` | Top-level wrapper inside the Quiz Builder preview |
    | `.lq-quiz` | Main quiz container |
    | `.lq-slide` | An individual question or content slide |
    | `.lq-wrapper` | Inner padding container for content, usually 650px maximum width |
    | `.lq-box` | Vertically centered cell inside the slide |

    **Examples**

    ```css
    /* Adds quiz border */
    .lq-quiz {
        border-style: solid;
        border-color: red;
    }
    ```

=== "Standalone"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.widget` | Top-level wrapper for the quiz |
    | `.builder-container-preview` | Top-level wrapper inside the Quiz Builder preview |
    | `.lq-quiz` | Main quiz container |
    | `.lq-slide` | An individual question or content slide |
    | `.lq-wrapper` | Inner padding container for content, usually 650px maximum width |
    | `.lq-box` | Vertically centered cell inside the slide |

    **Examples**

    ```css
    /* Adds quiz border */
    .lq-quiz {
        border-style: solid;
        border-color: red;
    }
    ```

## Question structure

=== "Shopify"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.question-wrapper` | Main question wrapper container |
    | `.question-wrapper-hide-next-button` | When next button is hidden |
    | `.question-wrapper-split` | Split layout (image + content) |
    | `.question-wrapper-split-desktop-left` | Desktop image on left |
    | `.question-wrapper-split-desktop-right` | Desktop image on right |
    | `.question-wrapper-split-mobile-above` | Mobile image above text |
    | `.question-wrapper-split-mobile-below` | Mobile image below text |
    | `.question-wrapper-split-mobile-hidden` | Mobile image hidden |
    | `.question-navigation-item` | Individual question slide container |
    | `.question-preview` | Question preview container |
    | `.question` | Main question element |
    | `.question-split` | Question with split layout |
    | `.content.question-content` | Question content area |
    | `.content-split` | Split layout content area |

    **Examples**

    ```css
    /* Customize split layout spacing */
    .question-wrapper-split {
        gap: 2rem;
    }

    /* Question container padding */
    .question {
        padding: 1.5rem;
    }

    /* Mobile question adjustments */
    .question.mobile {
        margin: 0.5rem;
    }
    ```

=== "Shopify (Legacy)"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `h1` | Main question text |
    | `.lq-slide-description` | Description text under a question |
    | `.lq-featured` | Featured image inside a question |
    | `.lq-input` | Standard text, email and number input fields |

    **Split layout selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-split` | Applied when the layout splits an image or video and the question |
    | `.lq-splitted` | Container for the question half of a split layout |

=== "WooCommerce"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `h1` | Main question text |
    | `.lq-slide-description` | Description text under a question |
    | `.lq-featured` | Featured image inside a question |
    | `.lq-input` | Standard text, email and number input fields |

    **Split layout selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-split` | Applied when the layout splits an image or video and the question |
    | `.lq-splitted` | Container for the question half of a split layout |

=== "Magento"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `h1` | Main question text |
    | `.lq-slide-description` | Description text under a question |
    | `.lq-featured` | Featured image inside a question |
    | `.lq-input` | Standard text, email and number input fields |

    **Split layout selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-split` | Applied when the layout splits an image or video and the question |
    | `.lq-splitted` | Container for the question half of a split layout |

=== "BigCommerce"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `h1` | Main question text |
    | `.lq-slide-description` | Description text under a question |
    | `.lq-featured` | Featured image inside a question |
    | `.lq-input` | Standard text, email and number input fields |

    **Split layout selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-split` | Applied when the layout splits an image or video and the question |
    | `.lq-splitted` | Container for the question half of a split layout |

=== "Standalone"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `h1` | Main question text |
    | `.lq-slide-description` | Description text under a question |
    | `.lq-featured` | Featured image inside a question |
    | `.lq-input` | Standard text, email and number input fields |

    **Split layout selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-split` | Applied when the layout splits an image or video and the question |
    | `.lq-splitted` | Container for the question half of a split layout |

## Question blocks

=== "Shopify"

    **Text block selectors**

    | Selector | Description |
    |----------|-------------|
    | `#qbt-{ref}` | Text block with unique reference ID |
    | `.text.question-text` | Text block base class |
    | `.question-text-large` | Large text size |
    | `.question-text-medium` | Medium text size |
    | `.question-text-small` | Small text size |
    | `.question-text--left` | Left aligned text |
    | `.question-text--center` | Center aligned text |
    | `.question-text--right` | Right aligned text |

    **Heading block selectors**

    | Selector | Description |
    |----------|-------------|
    | `#qbh-{ref}` | Heading block with unique reference ID |
    | `.heading.question-heading` | Heading block container |
    | `.heading.question-heading h1/h2/h3` | Actual heading text elements |
    | `.heading__small.question-heading__small h3` | Small heading text (h3) |
    | `.heading__medium.question-heading__medium h2` | Medium heading text (h2) |
    | `.heading__large.question-heading__large h1` | Large heading text (h1) |
    | `.heading__left.question-heading__left` | Left aligned heading |
    | `.heading__center.question-heading__center` | Center aligned heading |
    | `.heading__right.question-heading__right` | Right aligned heading |

    **Button block selectors**

    | Selector | Description |
    |----------|-------------|
    | `#qbb-{ref}` | Button block with unique reference ID |
    | `.question-button__container` | Button container |
    | `.button.question_button` | Button element |
    | `.question-button--left` | Left aligned button |
    | `.question-button--center` | Center aligned button |
    | `.question-button--right` | Right aligned button |
    | `.button_text` | Button text span |

    **Examples**

    ```css
    /* Style all question heading text */
    .heading.question-heading h1,
    .heading.question-heading h2,
    .heading.question-heading h3 {
        color: black;
        font-weight: bold;
    }

    /* Style heading container */
    .heading.question-heading {
        margin-bottom: 2rem;
        padding: 1rem;
    }

    /* Target specific heading size */
    .heading__medium.question-heading__medium h2 {
        font-size: 2rem;
        color: #333;
    }

    /* Customize question buttons */
    .question_button {
        border-radius: 8px;
        padding: 12px 24px;
    }
    ```

=== "Shopify (Legacy)"

    !!! note "Blocks are a Built for Shopify feature"

        Questions in the legacy app are not modular. A question holds its choices
        directly, so there are no text, heading or button block selectors.

=== "WooCommerce"

    !!! note "Blocks are a Built for Shopify feature"

        Questions in the legacy app are not modular. A question holds its choices
        directly, so there are no text, heading or button block selectors.

=== "Magento"

    !!! note "Blocks are a Built for Shopify feature"

        Questions in the legacy app are not modular. A question holds its choices
        directly, so there are no text, heading or button block selectors.

=== "BigCommerce"

    !!! note "Blocks are a Built for Shopify feature"

        Questions in the legacy app are not modular. A question holds its choices
        directly, so there are no text, heading or button block selectors.

=== "Standalone"

    !!! note "Blocks are a Built for Shopify feature"

        Questions in the legacy app are not modular. A question holds its choices
        directly, so there are no text, heading or button block selectors.

## Choice blocks

=== "Shopify"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `#qbc-{ref}` | Choice block container with unique reference ID |
    | `.question-choice_list` | Choice list container |
    | `.question-choice_list--multiple-choice` | Multiple-choice type |
    | `.question-choice_list--picture-choice` | Picture choice type |
    | `.question-choice_list--slider-choice` | Slider choice type |
    | `.question-choice_list--scroll-snap` | Horizontal scroll layout |
    | `.picture-choice-{N}-choices` | Dynamic class based on choice count |
    | `.picture-choice__tiny` | Tiny picture size |
    | `.picture-choice__small` | Small picture size |
    | `.picture-choice__medium` | Medium picture size |
    | `.picture-choice__large` | Large picture size |

    **Individual choice selectors**

    | Selector | Description |
    |----------|-------------|
    | `#qbcc-{ref}` | Individual choice with unique reference ID |
    | `.question-choice__label` | Choice label wrapper |
    | `.question-choice__label-selected` | Selected choice state |
    | `.question-choice__label-content` | Choice content area |
    | `.question-choice__label-thumbnail` | Choice image thumbnail |
    | `.question-block__choice-error-message` | Error message container |

    **Examples**

    ```css
    /* Style choice options */
    .question-choice__label {
        border: 1px solid #ddd;
        border-radius: 6px;
    }

    /* Selected choice styling */
    .question-choice__label-selected {
        background: #007bff;
        color: white;
    }

    /* Picture choice thumbnails */
    .question-choice__label-thumbnail {
        border-radius: 8px;
        overflow: hidden;
    }
    ```

=== "Shopify (Legacy)"

    **Main selectors**

    Choices render as a list. `.lq-choices` is the `<ul>`, and each choice is an `<li>`.

    | Selector | Description |
    |----------|-------------|
    | `.lq-choices` | List container for answers |
    | `.lq-choice` | An individual answer choice |
    | `.lq-selected` | Applied to an answer choice when it is selected |
    | `.lq-letter` | The circle or square icon holding the choice letter |
    | `.lq-picture-choice` | Applied when the choices contain images |
    | `.lq-images` | List container for picture choices |
    | `.lq-img` | The image container inside a picture choice |

    **Examples**

    ```css
    /* Change the styles of the choices */
    li.lq-choice {
        /* your CSS rules go here */
    }

    /* Change the styles of the picture choices */
    .lq-images li.lq-choice {
        /* your CSS rules go here */
    }

    /* Multiple-choice questions: change the selected option background */
    li.lq-selected .lq-letter {
        background-color: gray;
    }
    ```

=== "WooCommerce"

    **Main selectors**

    Choices render as a list. `.lq-choices` is the `<ul>`, and each choice is an `<li>`.

    | Selector | Description |
    |----------|-------------|
    | `.lq-choices` | List container for answers |
    | `.lq-choice` | An individual answer choice |
    | `.lq-selected` | Applied to an answer choice when it is selected |
    | `.lq-letter` | The circle or square icon holding the choice letter |
    | `.lq-picture-choice` | Applied when the choices contain images |
    | `.lq-images` | List container for picture choices |
    | `.lq-img` | The image container inside a picture choice |

    **Examples**

    ```css
    /* Change the styles of the choices */
    li.lq-choice {
        /* your CSS rules go here */
    }

    /* Change the styles of the picture choices */
    .lq-images li.lq-choice {
        /* your CSS rules go here */
    }

    /* Multiple-choice questions: change the selected option background */
    li.lq-selected .lq-letter {
        background-color: gray;
    }
    ```

=== "Magento"

    **Main selectors**

    Choices render as a list. `.lq-choices` is the `<ul>`, and each choice is an `<li>`.

    | Selector | Description |
    |----------|-------------|
    | `.lq-choices` | List container for answers |
    | `.lq-choice` | An individual answer choice |
    | `.lq-selected` | Applied to an answer choice when it is selected |
    | `.lq-letter` | The circle or square icon holding the choice letter |
    | `.lq-picture-choice` | Applied when the choices contain images |
    | `.lq-images` | List container for picture choices |
    | `.lq-img` | The image container inside a picture choice |

    **Examples**

    ```css
    /* Change the styles of the choices */
    li.lq-choice {
        /* your CSS rules go here */
    }

    /* Change the styles of the picture choices */
    .lq-images li.lq-choice {
        /* your CSS rules go here */
    }

    /* Multiple-choice questions: change the selected option background */
    li.lq-selected .lq-letter {
        background-color: gray;
    }
    ```

=== "BigCommerce"

    **Main selectors**

    Choices render as a list. `.lq-choices` is the `<ul>`, and each choice is an `<li>`.

    | Selector | Description |
    |----------|-------------|
    | `.lq-choices` | List container for answers |
    | `.lq-choice` | An individual answer choice |
    | `.lq-selected` | Applied to an answer choice when it is selected |
    | `.lq-letter` | The circle or square icon holding the choice letter |
    | `.lq-picture-choice` | Applied when the choices contain images |
    | `.lq-images` | List container for picture choices |
    | `.lq-img` | The image container inside a picture choice |

    **Examples**

    ```css
    /* Change the styles of the choices */
    li.lq-choice {
        /* your CSS rules go here */
    }

    /* Change the styles of the picture choices */
    .lq-images li.lq-choice {
        /* your CSS rules go here */
    }

    /* Multiple-choice questions: change the selected option background */
    li.lq-selected .lq-letter {
        background-color: gray;
    }
    ```

=== "Standalone"

    **Main selectors**

    Choices render as a list. `.lq-choices` is the `<ul>`, and each choice is an `<li>`.

    | Selector | Description |
    |----------|-------------|
    | `.lq-choices` | List container for answers |
    | `.lq-choice` | An individual answer choice |
    | `.lq-selected` | Applied to an answer choice when it is selected |
    | `.lq-letter` | The circle or square icon holding the choice letter |
    | `.lq-picture-choice` | Applied when the choices contain images |
    | `.lq-images` | List container for picture choices |
    | `.lq-img` | The image container inside a picture choice |

    **Examples**

    ```css
    /* Change the styles of the choices */
    li.lq-choice {
        /* your CSS rules go here */
    }

    /* Change the styles of the picture choices */
    .lq-images li.lq-choice {
        /* your CSS rules go here */
    }

    /* Multiple-choice questions: change the selected option background */
    li.lq-selected .lq-letter {
        background-color: gray;
    }
    ```

## Background and navigation

=== "Shopify"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.question-background` | Question background base |
    | `.background` | Background image position |
    | `.background-split` | Split layout background |
    | `.question-background-image` | Background image element |
    | `.question-background-image--split` | Split layout background image |

    **Navigation bar selectors**

    | Selector | Description |
    |----------|-------------|
    | `.navigation-bar` | Navigation bar container |
    | `.navigation-bar__container` | Navigation bar wrapper |
    | `.navigation-bar__progress` | Progress section |
    | `.navigation-bar__progress-text` | Progress text |
    | `.navigation-bar__progress-bar` | Progress bar container |
    | `.navigation-bar__progress-bar-fill` | Progress bar fill |
    | `.navigation-bar__buttons` | Navigation buttons container |
    | `.navigation-bar__button` | Navigation button |

    **Examples**

    ```css
    /* Customize navigation bar */
    .navigation-bar {
        background: #f8f9fa;
        border-top: 1px solid #dee2e6;
    }

    /* Progress bar styling */
    .navigation-bar__progress-bar-fill {
        background: linear-gradient(to right, #007bff, #28a745);
    }

    /* Navigation buttons */
    .navigation-bar__button {
        border-radius: 4px;
        padding: 8px 16px;
    }
    ```

=== "Shopify (Legacy)"

    **Navigation and progress selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-footer` | Sticky container at the bottom |
    | `.lq-nav-button` | Back and Next buttons |
    | `.lq-progress-box` | Progress bar wrapper in the footer |
    | `.lq-progress-bar` | Progress bar background |
    | `.lq-progress-fill` | Active part of the progress bar |
    | `.lq-poweredby` | The `Powered by RevenueHunt` branding |

    **Examples**

    ```css
    /* Hide Progress Bar in the footer */
    .lq-progress-box {
        display: none;
    }

    /* Place the footer bar at the top, for more visibility */
    .lq-footer {
        position: absolute;
        width: 100%;
        top: 0;
        margin: 0;
    }
    ```

=== "WooCommerce"

    **Navigation and progress selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-footer` | Sticky container at the bottom |
    | `.lq-nav-button` | Back and Next buttons |
    | `.lq-progress-box` | Progress bar wrapper in the footer |
    | `.lq-progress-bar` | Progress bar background |
    | `.lq-progress-fill` | Active part of the progress bar |
    | `.lq-poweredby` | The `Powered by RevenueHunt` branding |

    **Examples**

    ```css
    /* Hide Progress Bar in the footer */
    .lq-progress-box {
        display: none;
    }

    /* Place the footer bar at the top, for more visibility */
    .lq-footer {
        position: absolute;
        width: 100%;
        top: 0;
        margin: 0;
    }
    ```

=== "Magento"

    **Navigation and progress selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-footer` | Sticky container at the bottom |
    | `.lq-nav-button` | Back and Next buttons |
    | `.lq-progress-box` | Progress bar wrapper in the footer |
    | `.lq-progress-bar` | Progress bar background |
    | `.lq-progress-fill` | Active part of the progress bar |
    | `.lq-poweredby` | The `Powered by RevenueHunt` branding |

    **Examples**

    ```css
    /* Hide Progress Bar in the footer */
    .lq-progress-box {
        display: none;
    }

    /* Place the footer bar at the top, for more visibility */
    .lq-footer {
        position: absolute;
        width: 100%;
        top: 0;
        margin: 0;
    }
    ```

=== "BigCommerce"

    **Navigation and progress selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-footer` | Sticky container at the bottom |
    | `.lq-nav-button` | Back and Next buttons |
    | `.lq-progress-box` | Progress bar wrapper in the footer |
    | `.lq-progress-bar` | Progress bar background |
    | `.lq-progress-fill` | Active part of the progress bar |
    | `.lq-poweredby` | The `Powered by RevenueHunt` branding |

    **Examples**

    ```css
    /* Hide Progress Bar in the footer */
    .lq-progress-box {
        display: none;
    }

    /* Place the footer bar at the top, for more visibility */
    .lq-footer {
        position: absolute;
        width: 100%;
        top: 0;
        margin: 0;
    }
    ```

=== "Standalone"

    **Navigation and progress selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-footer` | Sticky container at the bottom |
    | `.lq-nav-button` | Back and Next buttons |
    | `.lq-progress-box` | Progress bar wrapper in the footer |
    | `.lq-progress-bar` | Progress bar background |
    | `.lq-progress-fill` | Active part of the progress bar |
    | `.lq-poweredby` | The `Powered by RevenueHunt` branding |

    **Examples**

    ```css
    /* Hide Progress Bar in the footer */
    .lq-progress-box {
        display: none;
    }

    /* Place the footer bar at the top, for more visibility */
    .lq-footer {
        position: absolute;
        width: 100%;
        top: 0;
        margin: 0;
    }
    ```

## Results structure

=== "Shopify"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.content.results-content` | Main results content container |
    | `#rs-{ref}` | Result section with unique reference ID |
    | `.result-block__container` | Result section wrapper |
    | `#rsb-{ref}` | Result block with unique reference ID |
    | `.block.results-block` | Base result block class |

    **Results heading selectors**

    | Selector | Description |
    |----------|-------------|
    | `.heading.results-heading` | Result heading block container |
    | `.heading.results-heading h1/h2/h3` | Result heading text elements |
    | `.heading__small.results-heading__small h3` | Small result heading (h3) |
    | `.heading__medium.results-heading__medium h2` | Medium result heading (h2) |
    | `.heading__large.results-heading__large h1` | Large result heading (h1) |
    | `.results-heading__left` | Left aligned result heading |
    | `.results-heading__center` | Center aligned result heading |
    | `.results-heading__right` | Right aligned result heading |

    **Results list selectors**

    | Selector | Description |
    |----------|-------------|
    | `.results-slot_list` | Slot list container |
    | `.results-slot_list-stacked` | Stacked layout |
    | `.results-slot_list-side_by_side` | Side by side layout |
    | `.results-slot_list__no_recommendations` | No recommendations state |

    **Examples**

    ```css
    /* Style result heading text */
    .heading.results-heading h1,
    .heading.results-heading h2,
    .heading.results-heading h3 {
        color: #007bff;
        font-weight: 600;
    }

    /* Results container styling */
    .results-content {
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Slot layout customization */
    .results-slot_list-stacked {
        gap: 1.5rem;
    }
    ```

=== "Shopify (Legacy)"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-results` | The Results Page container |
    | `.lq-results-box` | Wrapper for the results content |
    | `.lq-retake-quiz` | Button that restarts the quiz |

    **Examples**

    ```css
    /* Change the color of the Retake Quiz text */
    .lq-retake-quiz {
        color: black;
    }
    ```

=== "WooCommerce"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-results` | The Results Page container |
    | `.lq-results-box` | Wrapper for the results content |
    | `.lq-retake-quiz` | Button that restarts the quiz |

    **Examples**

    ```css
    /* Change the color of the Retake Quiz text */
    .lq-retake-quiz {
        color: black;
    }
    ```

=== "Magento"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-results` | The Results Page container |
    | `.lq-results-box` | Wrapper for the results content |
    | `.lq-retake-quiz` | Button that restarts the quiz |

    **Examples**

    ```css
    /* Change the color of the Retake Quiz text */
    .lq-retake-quiz {
        color: black;
    }
    ```

=== "BigCommerce"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-results` | The Results Page container |
    | `.lq-results-box` | Wrapper for the results content |
    | `.lq-retake-quiz` | Button that restarts the quiz |

    **Examples**

    ```css
    /* Change the color of the Retake Quiz text */
    .lq-retake-quiz {
        color: black;
    }
    ```

=== "Standalone"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `.lq-results` | The Results Page container |
    | `.lq-results-box` | Wrapper for the results content |
    | `.lq-retake-quiz` | Button that restarts the quiz |

    **Examples**

    ```css
    /* Change the color of the Retake Quiz text */
    .lq-retake-quiz {
        color: black;
    }
    ```

## Slot components

=== "Shopify"

    **Main selectors**

    | Selector | Description |
    |----------|-------------|
    | `#rsbss-{ref}` | Individual slot with unique reference ID |
    | `.results-slot_{width}` | Slot width classes (full, half, third) |
    | `.results-slot_{N}-items` | Dynamic class based on item count |
    | `.results-slot` | Individual slot item |
    | `.results-slot.in-cart` | Item already in cart state |

    **Product elements**

    | Selector | Description |
    |----------|-------------|
    | `.slot-product__image` | Product image |
    | `.slot-product__image--{size}` | Image size variations |
    | `.slot-product__image-link` | Product image link |
    | `.slot-product__title` | Product title |
    | `.slot-product__title-link` | Product title link |
    | `.slot-product__button` | Add to cart button |
    | `.slot-product__button-add` | Add button (quantity > 0) |
    | `.slot-product__button-added--container` | Added to cart state container |
    | `.slot-product__button-remove` | Remove quantity button |
    | `.slot-product__button-item-text` | Button item text |

    **Collection elements**

    | Selector | Description |
    |----------|-------------|
    | `.slot-collection__title` | Collection title |
    | `.slot-collection__image` | Collection image |

    **Examples**

    ```css
    /* Product card styling */
    .results-slot {
        border: 1px solid #eee;
        border-radius: 8px;
        padding: 1rem;
    }

    /* Product images */
    .slot-product__image {
        border-radius: 6px;
        transition: transform 0.2s;
    }

    /* Add to cart buttons */
    .slot-product__button {
        background: #007bff;
        color: white;
        border: none;
    }

    /* Responsive slot widths */
    .results-slot_half {
        width: calc(50% - 0.5rem);
    }
    ```

=== "Shopify (Legacy)"

    **Product elements**

    | Selector | Description |
    |----------|-------------|
    | `.lq-slot` | Container for recommended products |
    | `.lq-price` | Product price display |
    | `.lq-product-description` | Product description text |
    | `.lq-variants-dropdown` | Product variant dropdown |

    **Purchase buttons**

    Three classes cover the purchase flow, and they are not interchangeable.

    | Selector | Description |
    |----------|-------------|
    | `.lq-add-to-cart` | The Add to Cart button on the Results Page. Style its size, background, border and hover state here |
    | `.lq-checkout` | The final Checkout or Buy Now button, usually in the sticky footer. It has a `:disabled` state for an empty or processing cart |
    | `.lq-checkout.lq-add-all-to-cart` | The Add all to cart button |
    | `.lq-btn-content` | The label area inside a button, between the quantity icons |
    | `.btn-minus` and `.btn-plus` | The quantity icons on the left and right of a split button |

    **Examples**

    ```css
    /* Change the background of the Add to Cart button */
    .lq-add-to-cart {
        background-color: #ff7028;
    }

    /* Hide the "add all to cart" button */
    .lq-checkout.lq-add-all-to-cart {
        display: none;
    }

    /* Fade the Checkout button while the cart is empty or processing */
    .lq-checkout:disabled {
        opacity: 0.5;
    }

    /* Leave 36px on each side for the quantity icons */
    .lq-btn-content {
        width: calc(100% - 72px);
    }
    ```

=== "WooCommerce"

    **Product elements**

    | Selector | Description |
    |----------|-------------|
    | `.lq-slot` | Container for recommended products |
    | `.lq-price` | Product price display |
    | `.lq-product-description` | Product description text |
    | `.lq-variants-dropdown` | Product variant dropdown |

    **Purchase buttons**

    Three classes cover the purchase flow, and they are not interchangeable.

    | Selector | Description |
    |----------|-------------|
    | `.lq-add-to-cart` | The Add to Cart button on the Results Page. Style its size, background, border and hover state here |
    | `.lq-checkout` | The final Checkout or Buy Now button, usually in the sticky footer. It has a `:disabled` state for an empty or processing cart |
    | `.lq-checkout.lq-add-all-to-cart` | The Add all to cart button |
    | `.lq-btn-content` | The label area inside a button, between the quantity icons |
    | `.btn-minus` and `.btn-plus` | The quantity icons on the left and right of a split button |

    **Examples**

    ```css
    /* Change the background of the Add to Cart button */
    .lq-add-to-cart {
        background-color: #ff7028;
    }

    /* Hide the "add all to cart" button */
    .lq-checkout.lq-add-all-to-cart {
        display: none;
    }

    /* Fade the Checkout button while the cart is empty or processing */
    .lq-checkout:disabled {
        opacity: 0.5;
    }

    /* Leave 36px on each side for the quantity icons */
    .lq-btn-content {
        width: calc(100% - 72px);
    }
    ```

=== "Magento"

    **Product elements**

    | Selector | Description |
    |----------|-------------|
    | `.lq-slot` | Container for recommended products |
    | `.lq-price` | Product price display |
    | `.lq-product-description` | Product description text |
    | `.lq-variants-dropdown` | Product variant dropdown |

    **Purchase buttons**

    Three classes cover the purchase flow, and they are not interchangeable.

    | Selector | Description |
    |----------|-------------|
    | `.lq-add-to-cart` | The Add to Cart button on the Results Page. Style its size, background, border and hover state here |
    | `.lq-checkout` | The final Checkout or Buy Now button, usually in the sticky footer. It has a `:disabled` state for an empty or processing cart |
    | `.lq-checkout.lq-add-all-to-cart` | The Add all to cart button |
    | `.lq-btn-content` | The label area inside a button, between the quantity icons |
    | `.btn-minus` and `.btn-plus` | The quantity icons on the left and right of a split button |

    **Examples**

    ```css
    /* Change the background of the Add to Cart button */
    .lq-add-to-cart {
        background-color: #ff7028;
    }

    /* Hide the "add all to cart" button */
    .lq-checkout.lq-add-all-to-cart {
        display: none;
    }

    /* Fade the Checkout button while the cart is empty or processing */
    .lq-checkout:disabled {
        opacity: 0.5;
    }

    /* Leave 36px on each side for the quantity icons */
    .lq-btn-content {
        width: calc(100% - 72px);
    }
    ```

=== "BigCommerce"

    **Product elements**

    | Selector | Description |
    |----------|-------------|
    | `.lq-slot` | Container for recommended products |
    | `.lq-price` | Product price display |
    | `.lq-product-description` | Product description text |
    | `.lq-variants-dropdown` | Product variant dropdown |

    **Purchase buttons**

    Three classes cover the purchase flow, and they are not interchangeable.

    | Selector | Description |
    |----------|-------------|
    | `.lq-add-to-cart` | The Add to Cart button on the Results Page. Style its size, background, border and hover state here |
    | `.lq-checkout` | The final Checkout or Buy Now button, usually in the sticky footer. It has a `:disabled` state for an empty or processing cart |
    | `.lq-checkout.lq-add-all-to-cart` | The Add all to cart button |
    | `.lq-btn-content` | The label area inside a button, between the quantity icons |
    | `.btn-minus` and `.btn-plus` | The quantity icons on the left and right of a split button |

    **Examples**

    ```css
    /* Change the background of the Add to Cart button */
    .lq-add-to-cart {
        background-color: #ff7028;
    }

    /* Hide the "add all to cart" button */
    .lq-checkout.lq-add-all-to-cart {
        display: none;
    }

    /* Fade the Checkout button while the cart is empty or processing */
    .lq-checkout:disabled {
        opacity: 0.5;
    }

    /* Leave 36px on each side for the quantity icons */
    .lq-btn-content {
        width: calc(100% - 72px);
    }
    ```

=== "Standalone"

    **Product elements**

    | Selector | Description |
    |----------|-------------|
    | `.lq-slot` | Container for recommended products |
    | `.lq-price` | Product price display |
    | `.lq-product-description` | Product description text |
    | `.lq-variants-dropdown` | Product variant dropdown |

    **Purchase buttons**

    Three classes cover the purchase flow, and they are not interchangeable.

    | Selector | Description |
    |----------|-------------|
    | `.lq-add-to-cart` | The Add to Cart button on the Results Page. Style its size, background, border and hover state here |
    | `.lq-checkout` | The final Checkout or Buy Now button, usually in the sticky footer. It has a `:disabled` state for an empty or processing cart |
    | `.lq-checkout.lq-add-all-to-cart` | The Add all to cart button |
    | `.lq-btn-content` | The label area inside a button, between the quantity icons |
    | `.btn-minus` and `.btn-plus` | The quantity icons on the left and right of a split button |

    **Examples**

    ```css
    /* Change the background of the Add to Cart button */
    .lq-add-to-cart {
        background-color: #ff7028;
    }

    /* Hide the "add all to cart" button */
    .lq-checkout.lq-add-all-to-cart {
        display: none;
    }

    /* Fade the Checkout button while the cart is empty or processing */
    .lq-checkout:disabled {
        opacity: 0.5;
    }

    /* Leave 36px on each side for the quantity icons */
    .lq-btn-content {
        width: calc(100% - 72px);
    }
    ```

## Animations

=== "Shopify"

    **Animation classes**

    | Selector | Description |
    |----------|-------------|
    | `.horizontal-forward.enter` | Horizontal forward enter animation |
    | `.horizontal-forward.exit` | Horizontal forward exit animation |
    | `.horizontal-backward.enter` | Horizontal backward enter animation |
    | `.horizontal-backward.exit` | Horizontal backward exit animation |
    | `.vertical-forward.enter` | Vertical forward enter animation |
    | `.vertical-forward.exit` | Vertical forward exit animation |
    | `.vertical-backward.enter` | Vertical backward enter animation |
    | `.vertical-backward.exit` | Vertical backward exit animation |

    **Examples**

    ```css
    /* Custom transition timing */
    .question-navigation-item {
        transition: all 0.3s ease-in-out;
    }

    /* Disable animations */
    .quiz * {
        transition: none !important;
        animation: none !important;
    }
    ```

=== "Shopify (Legacy)"

    !!! note "Animation classes are a Built for Shopify feature"

        These enter and exit classes belong to the Built for Shopify version.

=== "WooCommerce"

    !!! note "Animation classes are a Built for Shopify feature"

        These enter and exit classes belong to the Built for Shopify version.

=== "Magento"

    !!! note "Animation classes are a Built for Shopify feature"

        These enter and exit classes belong to the Built for Shopify version.

=== "BigCommerce"

    !!! note "Animation classes are a Built for Shopify feature"

        These enter and exit classes belong to the Built for Shopify version.

=== "Standalone"

    !!! note "Animation classes are a Built for Shopify feature"

        These enter and exit classes belong to the Built for Shopify version.

## Dynamic ID patterns

=== "Shopify"

    Use these patterns to target specific elements in your quiz:

    | Pattern | Description |
    |---------|-------------|
    | `#quiz-{quizId}` | Target entire quiz instance |
    | `#q-{ref}` | Target specific question page |
    | `#qbt-{ref}` | Target specific text block |
    | `#qbh-{ref}` | Target specific heading block |
    | `#qbc-{ref}` | Target specific choice block |
    | `#qbcc-{ref}` | Target specific choice option |
    | `#qbb-{ref}` | Target specific button block |
    | `#r-{ref}` | Target specific results page |
    | `#rs-{ref}` | Target specific result section |
    | `#rsb-{ref}` | Target specific result block |
    | `#rsbss-{ref}` | Target specific slot |

    **Examples**

    ```css
    /* Target specific question */
    #q-abc123 .question-text {
        font-size: 18px;
    }

    /* Style specific choice block */
    #qbc-choice456 {
        margin-bottom: 2rem;
    }

    /* Customize specific result section */
    #rs-section789 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    ```

=== "Shopify (Legacy)"

    !!! note "Dynamic ID patterns are a Built for Shopify feature"

        The legacy app targets elements by class instead.

=== "WooCommerce"

    !!! note "Dynamic ID patterns are a Built for Shopify feature"

        The legacy app targets elements by class instead.

=== "Magento"

    !!! note "Dynamic ID patterns are a Built for Shopify feature"

        The legacy app targets elements by class instead.

=== "BigCommerce"

    !!! note "Dynamic ID patterns are a Built for Shopify feature"

        The legacy app targets elements by class instead.

=== "Standalone"

    !!! note "Dynamic ID patterns are a Built for Shopify feature"

        The legacy app targets elements by class instead.

## Common use cases

=== "Shopify"

    **Brand color customization**

    ```css
    /* Primary brand colors */
    .question_button,
    .slot-product__button {
        background: var(--brand-primary, #007bff);
        color: var(--brand-text, white);
    }

    .question-choice__label-selected {
        background: var(--brand-primary, #007bff);
        border-color: var(--brand-primary, #007bff);
    }
    ```

    **Mobile-first responsive design**

    ```css
    /* Mobile base styles */
    .quiz {
        padding: 1rem;
    }
    .question {
        margin-bottom: 1rem;
    }

    /* Desktop enhancements */
    @media (min-width: 768px) {
        .quiz {
            padding: 2rem;
        }
        .question {
            margin-bottom: 2rem;
        }
    }
    ```

    **Custom typography scale**

    ```css
    /* Typography hierarchy */
    .question-heading__large {
        font-size: 2.5rem;
    }
    .question-heading__medium {
        font-size: 2rem;
    }
    .question-heading__small {
        font-size: 1.5rem;
    }
    .question-text {
        font-size: 1rem;
        line-height: 1.6;
    }
    ```

    **Product grid layout**

    ```css
    /* Responsive product grid */
    .results-slot_list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }

    .results-slot {
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    ```

    ---

    This article explains the CSS structure of the `💎 Built for Shopify` RevenueHunt quiz app.

=== "Shopify (Legacy)"

    !!! tip "More legacy CSS examples"

        For ready-made snippets you can paste in, see
        [How to Customize the Quiz Design](/how-to-guides/customize-quiz-design/).

=== "WooCommerce"

    !!! tip "More legacy CSS examples"

        For ready-made snippets you can paste in, see
        [How to Customize the Quiz Design](/how-to-guides/customize-quiz-design/).

=== "Magento"

    !!! tip "More legacy CSS examples"

        For ready-made snippets you can paste in, see
        [How to Customize the Quiz Design](/how-to-guides/customize-quiz-design/).

=== "BigCommerce"

    !!! tip "More legacy CSS examples"

        For ready-made snippets you can paste in, see
        [How to Customize the Quiz Design](/how-to-guides/customize-quiz-design/).

=== "Standalone"

    !!! tip "More legacy CSS examples"

        For ready-made snippets you can paste in, see
        [How to Customize the Quiz Design](/how-to-guides/customize-quiz-design/).
