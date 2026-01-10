# Accessibility

RevenueHunt quizzes are built with accessibility best practices in mind, following **WCAG 2.1 Level AA** guidelines.

!!! note "Shared Responsibility"
    Final accessibility compliance also depends on your theme, quiz customization, and embedding method. Colors, fonts, image-only choices, custom CSS/JS, and other overlays on your site can impact accessibility. This guide covers what we provide and best practices for maintaining accessibility.

## Keyboard Navigation

Users can complete the entire quiz using only a keyboard:

- **Tab / Shift+Tab** - Move between interactive elements
- **Arrow Keys** - Navigate between quiz choices
- **Enter / Space** - Select choices and submit answers
- **Logical Tab Order** - Focus moves in a natural, predictable order

All question types are fully navigable via keyboard, including dropdowns, sliders, date pickers, and number inputs.

!!! tip "Avoiding Focus Issues"
    Theme overlays like chat widgets or newsletter popups can steal focus while the quiz is open. For the best experience, pause competing overlays while the quiz is active.

## Screen Reader Support

Quizzes work with popular screen readers including VoiceOver (macOS/iOS), NVDA (Windows), and TalkBack (Android):

- All interactive elements have descriptive labels
- Dynamic content changes (errors, selections) are announced automatically
- Validation errors are announced immediately when they occur
- Selection states are communicated clearly
- Progress is indicated (e.g., "Question 2 of 6")

### Best Practice: Use Text Labels

Every choice should have a meaningful text label, not just images. If you use image choices, keep a meaningful label so screen readers can describe the option.

[:fontawesome-solid-arrow-right: Learn more about Questions](/reference/quiz-builder/questions/)

## Focus Management

- **Visible Focus Indicators** - Clear outline on all interactive elements
- **Logical Focus Order** - Matches the visual layout
- **No Keyboard Traps** - Users can always navigate away

## Form Accessibility

- All form fields have associated labels
- Validation errors are linked to their inputs
- Required fields are indicated to assistive technology
- Standard inputs support browser autofill

## Visual Accessibility

### Color Contrast

All 8 built-in color schemes meet contrast requirements:

| Element | Minimum Contrast |
|---------|-----------------|
| Body text | 4.5:1 |
| Headings | 4.5:1 |
| Buttons | 3:1 |

!!! warning "Custom Colors"
    If you customize quiz colors, use a [contrast checker](https://webaim.org/resources/contrastchecker/) to verify your choices meet the 4.5:1 ratio for text.

[:fontawesome-solid-arrow-right: Customize Quiz Design](/reference/quiz-builder/quiz-design/)

### Text Scaling

Quiz text scales with browser zoom and user font preferences:

- Works at 200% browser zoom
- Respects system font size preferences
- Uses relative units for proper scaling

### Touch Targets

Interactive elements meet WCAG 2.1 Level AAA touch target requirements:

| Element | Minimum Size |
|---------|-------------|
| Choice options | 44px (meets Level AAA) |
| Buttons & inputs | 48px (exceeds Level AAA) |

All interactive elements meet or exceed the WCAG 2.5.5 Level AAA requirement of 44px minimum. Adequate spacing between targets prevents accidental taps.

## Motion & Animation

- Quiz respects the `prefers-reduced-motion` browser setting
- All animations are disabled when reduced motion is preferred
- No auto-playing media without user interaction

## Language Support

### Right-to-Left (RTL) Languages

Quizzes automatically adjust layout for RTL languages including Arabic, Hebrew, Persian, Urdu, Pashto, and Kurdish.

### Multiple Languages

Quizzes support 11+ languages with proper text direction.

[:fontawesome-solid-arrow-right: Change Quiz Language](/how-to-guides/change-quiz-language/)

## Customizable Accessibility Text

Customize screen reader text in **Quiz Builder > Quiz Settings > Accessibility**:

| Setting | Purpose |
|---------|---------|
| Quiz Complete | Announced when quiz is finished |
| Previous/Next Question | Labels for navigation buttons |
| Answer Before Proceeding | Prompt when answer is required |

## Testing Your Quiz

We recommend testing your quiz:

1. **Keyboard Only** - Complete using only Tab, Arrow keys, Enter, and Space
2. **Screen Reader** - Test with VoiceOver (Mac) or NVDA (Windows)
3. **Browser Zoom** - Verify at 200% zoom
4. **Color Contrast** - Verify custom colors with a [contrast checker](https://webaim.org/resources/contrastchecker/)
5. **Mobile** - Test tap targets on actual devices

## Standards

Our quiz renderer follows:

- **WCAG 2.1 Level AA** - Web Content Accessibility Guidelines
- **Section 508** - US federal accessibility requirements
- **ADA** - Americans with Disabilities Act guidelines

## Need Help?

If you notice an accessibility issue, please let us know—our team will address it promptly.

[:fontawesome-solid-arrow-right: Contact Customer Support](/how-to-guides/contact-customer-support/)

!!! info "VPAT Documentation"
    We don't provide a formal VPAT document, but we're happy to help review specific accessibility concerns with your live quiz setup. [Contact our support team](/how-to-guides/contact-customer-support/).

---

**Related Articles:**

- [Questions Reference](/reference/quiz-builder/questions/)
- [Quiz Design Settings](/reference/quiz-builder/quiz-design/)
- [Change Quiz Language](/how-to-guides/change-quiz-language/)
