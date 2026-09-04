---
description: "RevenueHunt quizzes follow WCAG 2.1 Level AAA accessibility guidelines for keyboard navigation and inclusive design."
---

# Accessibility

RevenueHunt quizzes follow **WCAG 2.1 Level AAA** guidelines.

!!! info "Shared responsibility"

    Final accessibility compliance also depends on your theme, your quiz customization, and your embedding method. Colors, fonts, image-only choices and custom code can affect accessibility. So can other overlays on your site. This page covers what RevenueHunt provides, and how to keep your own setup accessible.

## Keyboard navigation

Customers can complete the whole quiz with only a keyboard:

- **Tab / Shift+Tab** - Move between interactive elements
- **Arrow keys** - Navigate between quiz choices
- **Enter / Space** - Select choices and submit answers
- **Logical tab order** - Focus moves in a natural, predictable order

Every question type is navigable with a keyboard, including dropdowns, sliders, date pickers and number inputs.

!!! tip "Avoiding focus issues"

    Theme overlays such as chat widgets or newsletter popups can steal focus while the quiz is open. Pause competing overlays while the quiz is active.

## Screen reader support

Quizzes work with common screen readers, including VoiceOver (macOS and iOS), NVDA (Windows) and TalkBack (Android):

- All interactive elements have descriptive labels
- Dynamic content changes, such as errors and selections, are announced automatically
- Validation errors are announced immediately when they occur
- Selection states are communicated clearly
- Progress is indicated, for example "Question 2 of 6"

### Best practice: use text labels

Give every choice a meaningful text label, not only an image. If you use image choices, keep a text label so screen readers can describe the option.

[:fontawesome-solid-arrow-right: Questions](/reference/quiz-builder/questions/)

## Focus management

- **Visible focus indicators** - Clear outline on all interactive elements
- **Logical focus order** - Matches the visual layout
- **No keyboard traps** - The customer can always move focus away

## Form accessibility

- All form fields have associated labels
- Validation errors are linked to their inputs
- Required fields are indicated to assistive technology
- Standard inputs support browser autofill

## Visual accessibility

### Color contrast

All eight built-in color schemes meet contrast requirements:

| Element | Minimum contrast |
|---------|-----------------|
| Body text | 4.5:1 |
| Headings | 4.5:1 |
| Buttons | 3:1 |

!!! warning "Custom colors"

    If you customize quiz colors, use a [contrast checker](https://webaim.org/resources/contrastchecker/) to confirm that text meets the 4.5:1 ratio.

[:fontawesome-solid-arrow-right: Quiz Design](/reference/quiz-builder/quiz-design/)

### Text scaling

Quiz text scales with browser zoom and system font preferences:

- Works at 200% browser zoom
- Respects system font size preferences
- Uses relative units for proper scaling

### Touch targets

Interactive elements meet WCAG 2.1 Level AAA touch target requirements:

| Element | Minimum size |
|---------|-------------|
| Choice options | 44px (meets Level AAA) |
| Buttons & inputs | 48px (exceeds Level AAA) |

Spacing between targets is wide enough to prevent accidental taps.

## Motion & animation

- The quiz respects the `prefers-reduced-motion` browser setting
- All animations are disabled when reduced motion is preferred
- No media plays automatically before the customer interacts with the quiz

## Language support

### Right-to-left (RTL) languages

Quizzes automatically adjust layout for RTL languages including Arabic, Hebrew, Persian, Urdu, Pashto, and Kurdish.

### Multiple languages

Quizzes support 11+ languages with proper text direction.

[:fontawesome-solid-arrow-right: Change Quiz Language](/how-to-guides/change-quiz-language/)

## Customizable accessibility text

Customize the text a screen reader reads out in [`Quiz settings > Quiz content`](/reference/quiz-builder/quiz-settings/#messages-quiz-content), under `Accessibility`:

| Setting | Purpose |
|---------|---------|
| `Quiz complete` | Read out on the quiz complete slide |
| `Previous question` | Label for the back button |
| `No previous question` | Read out when there is no earlier question to go back to |
| `Next question` | Label for the forward button |
| `Answer before proceeding` | Read out when an answer is required |

## Testing your quiz

Test your quiz in five ways:

- **Keyboard only** - Complete the quiz with only Tab, Arrow keys, Enter and Space
- **Screen reader** - Test with VoiceOver on macOS, or NVDA on Windows
- **Browser zoom** - Check the quiz at 200% zoom
- **Color contrast** - Check custom colors with a [contrast checker](https://webaim.org/resources/contrastchecker/)
- **Mobile** - Test tap targets on a real device

## Standards

The RevenueHunt quiz renderer follows:

- **WCAG 2.1 Level AAA** - Web Content Accessibility Guidelines
- **Section 508** - US federal accessibility requirements
- **ADA** - Americans with Disabilities Act guidelines

## Need help?

If you find an accessibility problem, report it to customer support.

[:fontawesome-solid-arrow-right: Contact support](/how-to-guides/contact-customer-support/)

!!! info "VPAT documentation"

    RevenueHunt does not provide a formal VPAT document. To review a specific accessibility concern with your live quiz, [contact customer support](/how-to-guides/contact-customer-support/).

---

← [Back to the App Manual](/reference/)

← Previous: [Feedback](/reference/feedback/)
Next: [CSS Structure](/reference/css-structure/) →
