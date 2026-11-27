---
description: "RevenueHunt quizzes are built to meet WCAG 2.2 Level AA, covering keyboard navigation, screen readers, focus, contrast and touch targets."
---

# Accessibility

The quiz in the `💎Built for Shopify` version of the RevenueHunt app is built to meet **WCAG 2.2 Level AA**. Content that conforms to WCAG 2.2 also conforms to WCAG 2.1. The [Accessibility Conformance Report](/reference/accessibility-conformance-report/) rates each criterion, including the ones the quiz only partially supports.

This page covers the `💎Built for Shopify` version of the RevenueHunt app, where all accessibility work happens. The legacy app does not receive accessibility updates. To move a quiz across, see [How to Migrate a Legacy Quiz](/how-to-guides/migrate-shopify-legacy-quiz/).

!!! info "Shared responsibility"

    Final accessibility compliance also depends on your theme, your quiz customization, and your embedding method. Colors, fonts, image-only choices and custom code can affect accessibility. So can other overlays on your site. This page covers what RevenueHunt provides, and how to keep your own setup accessible.

## Keyboard navigation

Customers can complete the whole quiz with only a keyboard:

- **Tab / Shift+Tab** - Move between interactive elements
- **Arrow keys** - Navigate between quiz choices. In a dropdown, arrow keys move between options. In a single-select dropdown on Windows, an arrow key also chooses the option and moves to the next question.
- **Enter / Space** - Select choices and submit answers
- **Escape** - Close a popup quiz. If a dropdown is open, Escape closes the dropdown first.
- **Logical tab order** - Focus moves in a natural, predictable order

Every question type is navigable with a keyboard, including dropdowns, sliders, date pickers, number inputs and file uploads. On the results page, the product buttons and the cart buttons also work with a keyboard.

!!! tip "Avoiding focus issues"

    Theme overlays such as chat widgets or newsletter popups can steal focus while the quiz is open. Pause competing overlays while the quiz is active.

## Screen reader support

Quizzes give screen readers, such as VoiceOver, NVDA and TalkBack, what they need to read the quiz:

- All interactive elements have descriptive labels
- Errors, progress and cart changes are announced automatically
- Validation errors are announced immediately when they occur
- Selection states are communicated clearly
- Progress is indicated, for example "Question 2 of 6"
- Changes to the progress and to the cart count are announced
- Each heading on the results page is read once

### Best practice: use text labels

Give every choice a meaningful text label, not only an image. If you use image choices, keep a text label so screen readers can describe the option.

[:fontawesome-solid-arrow-right: Questions](/reference/quiz-builder/questions/)

## Focus management

- **Visible focus indicators** - Clear outline on all interactive elements
- **Logical focus order** - Matches the visual layout
- **No keyboard traps** - The customer can always move focus away. In a popup quiz, the customer leaves by closing the popup.

### Popup quizzes

A popup quiz keeps the keyboard focus inside the popup while it is open:

- When the popup opens, focus starts on the close button.
- Tab and Shift+Tab move focus only between the elements inside the popup, never to the page behind it.
- Escape closes the popup. If a dropdown is open, Escape closes the dropdown first.
- When the popup closes, focus returns to the button or link that opened it.

## Form accessibility

- All form fields have associated labels
- Field errors are linked to their field
- Required text, email, number, phone and date fields are indicated to assistive technology
- Standard inputs support browser autofill

## Visual accessibility

### Color contrast

All eight built-in color schemes meet the WCAG 2.2 Level AA minimum contrast ratios:

| Element | Minimum contrast |
|---------|-----------------|
| Text, including button text, answers and placeholders | 4.5:1 |
| Large text (18pt, or 14pt bold) | 3:1 |
| Focus outline, checkboxes and other control borders | 3:1 |

The keyboard focus outline uses the `Choice selected background` color, under `Choices` in Quiz Design. Pick a color with at least 3:1 contrast against your quiz background so the outline stays visible.

!!! warning "Custom colors"

    If you customize quiz colors, use a [contrast checker](https://webaim.org/resources/contrastchecker/) to confirm that each text color meets 4.5:1 against the color behind it.

    A quiz keeps the colors it was saved with. Check any quiz created before November 2026 and any quiz migrated from the legacy app.

[:fontawesome-solid-arrow-right: Quiz Design](/reference/quiz-builder/quiz-design/)

### Text scaling

Quiz text scales with browser zoom:

- Works at 200% browser zoom
- Fits a screen 320 pixels wide without scrolling sideways

### Touch targets

Every interactive element meets the 24 by 24 pixel minimum in WCAG 2.2 Level AA, or has an equivalent control that does:

| Element | Minimum height |
|---------|-------------|
| Choice options | 44px |
| Most buttons | 48px |

Spacing between targets is wide enough to prevent accidental taps.

## Motion & animation

- The quiz respects the `prefers-reduced-motion` browser setting
- All animations are disabled when reduced motion is preferred
- No media plays automatically before the customer interacts with the quiz

## Language support

### Right-to-left (RTL) languages

Quizzes automatically adjust layout for RTL languages including Arabic, Hebrew, Persian, Urdu, Pashto, and Kurdish.

### Multiple languages

A quiz can be shown in each language your store publishes, with the right text direction for each.

[:fontawesome-solid-arrow-right: Change Quiz Language](/how-to-guides/change-quiz-language/)

## Customizable accessibility text

Customize the text a screen reader reads out in [`Quiz settings > Quiz content`](/reference/quiz-builder/quiz-settings/#messages-quiz-content), under `Accessibility`:

| Setting | Purpose |
|---------|---------|
| `Previous question` | Label for the back button |
| `No previous question` | Read out when there is no earlier question to go back to |
| `Next question` | Label for the forward button |
| `Answer before proceeding` | Read out when an answer is required |
| `Quiz navigation buttons` | Name of the navigation bar |
| `Results bottom bar` | Name of the bar at the bottom of the results page |
| `Quiz progress` | Name of the progress bar |
| `Question choices` | Name of an answer list when its question has no heading |
| `Remove {{label}}` | Label for the button that removes a selected option from a dropdown |
| `Remove one {{label}}` | Label for the button that removes one product from the cart |

## Testing your quiz

Test your quiz in five ways:

- **Keyboard only** - Complete the quiz with only Tab, Arrow keys, Enter and Space
- **Screen reader** - Test with VoiceOver on macOS, or NVDA on Windows
- **Browser zoom** - Check the quiz at 200% zoom
- **Color contrast** - Check custom colors with a [contrast checker](https://webaim.org/resources/contrastchecker/)
- **Mobile** - Test tap targets on a real device

## Standards

The RevenueHunt quiz is built to meet **WCAG 2.2 Level AA**, the Web Content Accessibility Guidelines. Content that conforms to WCAG 2.2 also conforms to WCAG 2.1. Two US requirements point to WCAG:

- **Section 508** - US federal accessibility requirements, which require WCAG 2.0 Level A and Level AA
- **ADA** - The US Department of Justice names WCAG as helpful guidance for making websites accessible under the Americans with Disabilities Act

## Need help?

If you find an accessibility problem, report it to customer support.

[:fontawesome-solid-arrow-right: Contact support](/how-to-guides/contact-customer-support/)

!!! tip "VPAT® and Accessibility Conformance Report"

    For a VPAT®, see the [Accessibility Conformance Report](/reference/accessibility-conformance-report/). It follows VPAT® 2.5Rev, WCAG edition, and rates the quiz against every WCAG 2.2 Level A and AA criterion.

---

← [Back to the App Manual](/reference/)

← Previous: [Feedback](/reference/feedback/)
Next: [Accessibility Conformance Report](/reference/accessibility-conformance-report/) →
