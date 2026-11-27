---
description: "RevenueHunt Accessibility Conformance Report (VPAT® 2.5Rev, WCAG edition) for the Built for Shopify version of the app: a rating and remarks for every WCAG 2.2 Level A and AA criterion."
---

# RevenueHunt Accessibility Conformance Report

**WCAG Edition (Based on VPAT® Version 2.5Rev)**

This report covers the quiz in the `💎Built for Shopify` version of the RevenueHunt app. It describes how the quiz conforms to the Web Content Accessibility Guidelines (WCAG) 2.0, 2.1 and 2.2, at Level A and Level AA. It follows the ITI Voluntary Product Accessibility Template (VPAT®) 2.5Rev, WCAG edition.

| Field | Details |
|---|---|
| **Product** | The `💎Built for Shopify` version of the RevenueHunt app |
| **Product description** | A product recommendation quiz that you add to your Shopify store. Customers answer questions and see recommended products on a results page. |
| **Version** | The live version of the app on the report date. The app updates continuously. |
| **Scope** | The quiz your customers see on your store: inline, popup and full-page quizzes, every question type, and the results page |
| **Report date** | November 2026 |
| **Contact** | Email team@revenuehunt.com, or see [How to Contact Customer Support](/how-to-guides/contact-customer-support/) |

## Notes

- **What this report covers.** The report covers the quiz your customers see, in the `💎Built for Shopify` version of the RevenueHunt app. It does not cover the Quiz builder in your Shopify admin. It also does not cover the RevenueHunt app for WooCommerce or the legacy version of the RevenueHunt app for Shopify. Those do not receive accessibility updates. To move a legacy quiz, see [How to Migrate a Legacy Quiz](/how-to-guides/migrate-shopify-legacy-quiz/).
- **Ratings assume the default settings.** Accessibility also depends on choices you make in the Quiz builder: colors, the text and images you add, and your store's theme. Where a criterion depends on your configuration, the remarks say what to check.
- **Optional features that do not meet WCAG.** Three optional question settings, all off by default, do not meet WCAG. If you need to conform, leave them off:
    - `Auto-advance question`: moves to the next question after a delay (WCAG 2.2.1 Timing Adjustable).
    - `Display bar value tooltip`: shows a slider's value in a tooltip (WCAG 1.4.13 Content on Hover or Focus). Escape does not close the tooltip, and it disappears when the pointer moves onto it.
    - `Hide checkbox/radio`: hides the check mark on picture choices, so a selected picture is shown by color only (WCAG 1.4.1 Use of Color).
- **Colors on existing quizzes.** A quiz keeps the colors it was saved with. Since 4 November 2026, the built-in color schemes meet the contrast ratios in this report. Use a [contrast checker](https://webaim.org/resources/contrastchecker/) to check a quiz created before then, a quiz migrated from the legacy app and a quiz with custom colors. To update a quiz that uses a built-in color scheme, select the color scheme again in Quiz design.

## Evaluation methods used

- Automated scans with axe-core 4.14 of every question type and the results page, at desktop width and at 320 pixels wide. The scans test the WCAG 2.0, 2.1 and 2.2 Level A and AA rules.
- Automated browser tests on a Shopify store that complete a quiz with keyboard actions, without a mouse. The tests check the names, roles, states and announcements that screen readers receive.
- Inspection of the browser's accessibility tree in Google Chrome, which is what screen readers read.
- Layout tests at 200% text size, with the WCAG text spacing override, and at 320 pixels wide.
- A focus test that presses Tab through every control and checks that no focused control is hidden.
- Touch tests in WebKit with iPhone and iPad emulation.
- Contrast ratios calculated for the text and control color pairs in the eight built-in color schemes, including faded secondary text.
- Unit tests for the names, states and announcements of each control.

RevenueHunt evaluated the product internally. Testing was automated. It did not include a session with a screen reader operated by a person.

## WCAG 2.x report

The criteria are scoped for full pages, complete processes and accessibility-supported ways of using technology, as the WCAG 2.0 Conformance Requirements describe. The quiz is a part of a store page, so criteria that apply to the whole page depend on the store's theme.

## Applicable standards

| Standard | Included in report |
|---|---|
| Web Content Accessibility Guidelines 2.0 | Level A: Yes. Level AA: Yes. Level AAA: No |
| Web Content Accessibility Guidelines 2.1 | Level A: Yes. Level AA: Yes. Level AAA: No |
| Web Content Accessibility Guidelines 2.2 | Level A: Yes. Level AA: Yes. Level AAA: No |

## Terms

- **Supports:** The functionality of the product has at least one method that meets the criterion without known defects or meets with equivalent facilitation.
- **Partially Supports:** Some functionality of the product does not meet the criterion.
- **Does Not Support:** The majority of product functionality does not meet the criterion.
- **Not Applicable:** The criterion is not relevant to the product.

## Table 1: success criteria, level A

| Criteria | Conformance level | Remarks and explanations |
|---|---|---|
| 1.1.1 Non-text Content (2.0, 2.1, 2.2) | Supports | Images the quiz adds are named or hidden from screen readers. A product image without alt text is named after its product. A product's review stars are read as the rating, for example "4.5 / 5". Images you add to questions and choices need alt text from you. |
| 1.2.1 Audio-only and Video-only (Prerecorded) (2.0, 2.1, 2.2) | Not Applicable | The quiz has no audio or video of its own. Video you add to a question is your responsibility. |
| 1.2.2 Captions (Prerecorded) (2.0, 2.1, 2.2) | Not Applicable | The quiz has no audio or video of its own. Video you add to a question is your responsibility. |
| 1.2.3 Audio Description or Media Alternative (Prerecorded) (2.0, 2.1, 2.2) | Not Applicable | The quiz has no audio or video of its own. Video you add to a question is your responsibility. |
| 1.3.1 Info and Relationships (2.0, 2.1, 2.2) | Supports | Each question is a named region with a heading. Answer lists, dropdowns, sliders and fields are named after their question. Selected answers are announced as selected. |
| 1.3.2 Meaningful Sequence (2.0, 2.1, 2.2) | Supports | The reading order matches the visual order. |
| 1.3.3 Sensory Characteristics (2.0, 2.1, 2.2) | Supports | Quiz instructions do not rely on shape, position or sound. |
| 1.4.1 Use of Color (2.0, 2.1, 2.2) | Partially Supports | Answer lists and picture choices show a check mark when selected. In a button-scale slider, the selected button is shown by color only. On picture choices, leave `Hide checkbox/radio` off so the check mark stays. |
| 1.4.2 Audio Control (2.0, 2.1, 2.2) | Not Applicable | The quiz plays no audio automatically. |
| 2.1.1 Keyboard (2.0, 2.1, 2.2) | Supports | Every question type, the results page and the cart buttons work with a keyboard. |
| 2.1.2 No Keyboard Trap (2.0, 2.1, 2.2) | Supports | A popup quiz keeps focus inside while open, and Escape or the close button leaves it. |
| 2.1.4 Character Key Shortcuts (2.1, 2.2) | Not Applicable | The quiz has no single-character keyboard shortcuts. |
| 2.2.1 Timing Adjustable (2.0, 2.1, 2.2) | Supports | The quiz has no time limits. The optional `Auto-advance question` setting adds one. Leave it off to conform. |
| 2.2.2 Pause, Stop, Hide (2.0, 2.1, 2.2) | Supports | Animations are short. They are turned off when the customer's device asks for reduced motion. |
| 2.3.1 Three Flashes or Below Threshold (2.0, 2.1, 2.2) | Supports | The quiz does not flash. |
| 2.4.1 Bypass Blocks (2.0, 2.1, 2.2) | Not Applicable | The quiz is part of a store page. Skip links are provided by the store's theme. |
| 2.4.2 Page Titled (2.0, 2.1, 2.2) | Not Applicable | The quiz is always part of a store page, including full-page quizzes, so the page title is set by the store's theme. A popup quiz is a dialog with its own name. |
| 2.4.3 Focus Order (2.0, 2.1, 2.2) | Supports | After each answer, focus moves to the next question's heading, when the question has one. A popup quiz starts focus on its close button and returns focus to the button that opened it. |
| 2.4.4 Link Purpose (In Context) (2.0, 2.1, 2.2) | Supports | Product links and buttons are named after their product, for example "Add to cart" followed by the product name. |
| 2.5.1 Pointer Gestures (2.1, 2.2) | Supports | No action needs a multi-point or path-based gesture. |
| 2.5.2 Pointer Cancellation (2.1, 2.2) | Supports | Buttons act on release, not on press. On touch screens, the phone country list chooses a country when the finger lifts, and moving the finger cancels. |
| 2.5.3 Label in Name (2.1, 2.2) | Supports | Every control's name contains its visible text. |
| 2.5.4 Motion Actuation (2.1, 2.2) | Not Applicable | No action is triggered by device motion. |
| 3.1.1 Language of Page (2.0, 2.1, 2.2) | Not Applicable | The page language is set by the store's theme, and the quiz inherits it. |
| 3.2.1 On Focus (2.0, 2.1, 2.2) | Supports | Moving focus never changes the question or submits anything. |
| 3.2.2 On Input (2.0, 2.1, 2.2) | Partially Supports | Choosing an answer moves to the next question without warning when the question has only one input and that input is single-select: a list of choices, a dropdown, a rating or a button scale. In a single-select dropdown on Windows, an arrow key chooses an option, so the quiz moves on before the customer sees the whole list. Focus then moves to the heading of the new question, which screen readers announce. The `Previous question` button goes back. |
| 3.2.6 Consistent Help (2.2) | Not Applicable | The quiz does not include a help mechanism. |
| 3.3.1 Error Identification (2.0, 2.1, 2.2) | Supports | Errors are shown in text and announced to screen readers. Errors in text, email, number, phone, date and file upload fields are linked to their field. |
| 3.3.2 Labels or Instructions (2.0, 2.1, 2.2) | Supports | Every field, answer list, dropdown and slider is named after its question. Required text, email, number, phone and date fields are indicated to assistive technology. |
| 3.3.7 Redundant Entry (2.2) | Supports | Answers are kept when the customer goes back. By default, the customer's previous answers are pre-filled when they retake the quiz. |
| 4.1.1 Parsing (2.0, 2.1) | Supports | For WCAG 2.0 and 2.1, the September 2023 errata update indicates this criterion is always supported. In WCAG 2.2, this criterion is obsolete and removed. |
| 4.1.2 Name, Role, Value (2.0, 2.1, 2.2) | Supports | Choices, dropdowns, fields, sliders and buttons expose their name, role and state. A slider announces the chosen label, and the selected rating or button is announced as selected. An open dropdown is linked to its list of options. The list renders outside the quiz's shadow DOM, so the link uses ARIA element reflection instead of an ID. Some older testing tools, such as axe-core 4.10, report a missing `aria-controls` attribute. axe-core 4.14 reads the link correctly. |

## Table 2: success criteria, level AA

| Criteria | Conformance level | Remarks and explanations |
|---|---|---|
| 1.2.4 Captions (Live) (2.0, 2.1, 2.2) | Not Applicable | The quiz has no live audio or video. |
| 1.2.5 Audio Description (Prerecorded) (2.0, 2.1, 2.2) | Not Applicable | The quiz has no audio or video of its own. Video you add to a question is your responsibility. |
| 1.3.4 Orientation (2.1, 2.2) | Supports | The quiz works in portrait and landscape. |
| 1.3.5 Identify Input Purpose (2.1, 2.2) | Supports | Name, email and phone fields declare their purpose, so browsers can fill them in. |
| 1.4.3 Contrast (Minimum) (2.0, 2.1, 2.2) | Supports | All text in the eight built-in color schemes meets 4.5:1. Custom colors are your responsibility, as described in Colors on existing quizzes, under Notes. |
| 1.4.4 Resize Text (2.0, 2.1, 2.2) | Supports | At 200% text size, no text is cut off and nothing scrolls sideways. |
| 1.4.5 Images of Text (2.0, 2.1, 2.2) | Supports | The quiz shows text as text. Images of text that you add are your responsibility. |
| 1.4.10 Reflow (2.1, 2.2) | Supports | At 320 pixels wide, the quiz and results fit without scrolling sideways. |
| 1.4.11 Non-text Contrast (2.1, 2.2) | Supports | In the built-in color schemes, the focus outline, checkboxes, input fields, progress bar and review stars meet 3:1. The focus outline uses the `Choice selected background` color. If you change it, keep at least 3:1 against your quiz background. |
| 1.4.12 Text Spacing (2.1, 2.2) | Supports | With the WCAG text spacing override, no text is cut off. |
| 1.4.13 Content on Hover or Focus (2.1, 2.2) | Supports | The quiz shows no hover content by default. The optional `Display bar value tooltip` setting does not meet this criterion. Leave it off to conform. |
| 2.4.5 Multiple Ways (2.0, 2.1, 2.2) | Not Applicable | The quiz is part of a store page. Site navigation is provided by the store's theme. |
| 2.4.6 Headings and Labels (2.0, 2.1, 2.2) | Supports | Questions and results have headings, and every control has a label. |
| 2.4.7 Focus Visible (2.0, 2.1, 2.2) | Supports | Every choice, button and link shows a focus outline. |
| 2.4.11 Focus Not Obscured (Minimum) (2.2) | Supports | When the customer presses Tab, no focused control is hidden behind the navigation bar or the results bottom bar. |
| 2.5.7 Dragging Movements (2.2) | Supports | A single tap on a slider sets its value, without dragging. Sliders also work with the keyboard. |
| 2.5.8 Target Size (Minimum) (2.2) | Supports | Choices are at least 44 pixels tall, and most buttons 48 pixels. Every target is at least 24 by 24 pixels or has an equivalent control. |
| 3.1.2 Language of Parts (2.0, 2.1, 2.2) | Partially Supports | When you choose a language other than English for the quiz's messages, the quiz declares it to screen readers. Otherwise the quiz uses the store page's language, so a quiz in a different language from the store is read in the store's language. Some screen reader labels are always in English, such as the question number, "Quiz Results", the popup close button and the country names in the phone field. |
| 3.2.3 Consistent Navigation (2.0, 2.1, 2.2) | Supports | The navigation bar is the same on every question. |
| 3.2.4 Consistent Identification (2.0, 2.1, 2.2) | Supports | Controls with the same function have the same name throughout the quiz. |
| 3.3.3 Error Suggestion (2.0, 2.1, 2.2) | Supports | Error messages say what is needed, for example a valid email address or how many choices to pick. |
| 3.3.4 Error Prevention (Legal, Financial, Data) (2.0, 2.1, 2.2) | Not Applicable | The quiz does not submit legal commitments or payments. Checkout happens in Shopify. |
| 3.3.8 Accessible Authentication (Minimum) (2.2) | Not Applicable | The quiz has no sign-in. |
| 4.1.3 Status Messages (2.1, 2.2) | Supports | Progress, errors and cart changes are announced without moving focus. |

## Legal disclaimer

This report describes the RevenueHunt quiz as of the report date. Your store's overall accessibility also depends on your theme, your quiz configuration and other apps on your store. VPAT® is a registered service mark of the Information Technology Industry Council (ITI).

---

← [Back to the App Manual](/reference/)

← Previous: [Accessibility](/reference/accessibility/)
Next: [CSS Structure](/reference/css-structure/) →
