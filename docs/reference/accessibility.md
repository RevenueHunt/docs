# Accessibility

RevenueHunt quizzes are built with accessibility best practices in mind, following **WCAG 2.1 Level AA** guidelines. Our quiz renderer includes proper labels, logical focus order, visible focus states, and keyboard navigation support.

!!! note "Shared Responsibility"
    Final accessibility compliance also depends on your theme, quiz customization, and embedding method. Colors, fonts, image-only choices, custom CSS/JS, and other overlays on your site can impact accessibility. This guide covers what we provide and best practices for maintaining accessibility.

## Keyboard Navigation

Users can complete the entire quiz using only a keyboard:

- **Tab / Shift+Tab** - Move between all interactive elements (buttons, inputs, choices)
- **Arrow Keys** - Navigate between quiz choices (up/down/left/right)
- **Enter / Space** - Select choices and submit answers
- **Logical Tab Order** - Focus moves top-to-bottom in a natural, predictable order

!!! tip "Avoiding Focus Issues"
    Theme overlays like chat widgets or newsletter popups can steal focus while the quiz is open. For the best experience, pause competing overlays while the quiz is active.

## Screen Reader Support

Quizzes work with popular screen readers including VoiceOver (macOS/iOS), NVDA (Windows), and TalkBack (Android):

- **ARIA Labels** - All interactive elements have descriptive labels announcing their purpose
- **Role Attributes** - Proper semantic roles (`listbox`, `option`, `button`, `heading`) help screen readers understand the quiz structure
- **Selection State** - Screen readers announce when choices are selected via `aria-selected`
- **Multi-Select Indication** - When multiple choices are allowed, this is announced via `aria-multiselectable`
- **Progress Indication** - Quiz progress is understandable in text (e.g., "Step 2 of 6")

### Best Practice: Use Text Labels

Every choice should have a meaningful text label, not just images. In the Quiz Builder, each choice has a **"Choice label"** field for visible text. If you use image choices, keep a meaningful label so screen readers aren't forced to guess.

[:fontawesome-solid-arrow-right: Learn more about Questions](/reference/quiz-builder/questions/)

## Focus Management

Our quiz includes proper focus handling:

- **Logical Focus Order** - Top-to-bottom flow matching the visual layout
- **Visible Focus State** - Clear focus indicators on all interactive elements
- **No Keyboard Traps** - Users can always navigate away from any element
- **Focus Restoration** - Focus returns appropriately after interactions

## Form Accessibility

Input fields are designed for accessibility:

- **Input Labels** - All form fields have associated labels for screen reader users
- **Autocomplete Support** - Standard input types (name, email, phone) support browser autofill
- **Clear Error Messages** - Validation errors show clear error text (not just color changes)
- **Required Field Indication** - Required questions show clear error messaging when incomplete

## Visual Accessibility

### Color Contrast

All 8 built-in color schemes are designed with contrast in mind:

| Element | Target Contrast Ratio |
|---------|----------------------|
| Body text | 4.5:1 or higher |
| Headings | 4.5:1 or higher |
| Buttons | 3:1 or higher |
| Form inputs | 4.5:1 or higher |

!!! warning "Custom Colors"
    If you customize quiz colors, ensure your choices maintain sufficient contrast:

    - Aim for **4.5:1** for normal text (WCAG AA requirement)
    - Ensure disabled/placeholder text has sufficient contrast
    - Don't rely on color alone to communicate selection or error states

    Use a [contrast checker](https://webaim.org/resources/contrastchecker/) to verify your color choices.

[:fontawesome-solid-arrow-right: Customize Quiz Design](/reference/quiz-builder/quiz-design/)

### Font Sizes & Readability

Quiz text is sized for readability:

- **Headings** - 24px to 40px depending on size setting
- **Body Text** - 14px to 22px depending on size setting
- **Mobile Optimization** - Text scales appropriately on smaller screens

**Best practices for custom styling:**

- Keep body text around **16px or larger**
- Avoid using images of text
- Maintain comfortable line-height and spacing

[:fontawesome-solid-arrow-right: Quiz Design Settings](/reference/quiz-builder/quiz-design/)

### Touch Targets (Mobile)

Interactive elements are sized for easy tapping:

- Buttons and choices have adequate tap target sizes
- Sufficient spacing prevents accidental taps on adjacent elements

**Best practice:** Keep options accessible with large clickable areas, especially for consent UI.

## Motion & Animation

For users sensitive to motion:

- **Reduced Motion Support** - The quiz respects the `prefers-reduced-motion` browser setting
- **No Auto-Playing Media** - Animations don't auto-play without user interaction
- **User-Controlled Progression** - Quiz advances only when the user takes action

**Best practice:** Avoid conveying essential information only through animation.

## Language Support

### Right-to-Left (RTL) Languages

Quizzes automatically adjust layout for RTL languages:

- Arabic (ar)
- Hebrew (he)
- Persian/Farsi (fa)
- Urdu (ur)
- Pashto (ps)
- Kurdish (ku)

The quiz detects the language setting and mirrors the interface appropriately.

### Multiple Languages

Quizzes support 11+ languages with proper text direction and localized content.

[:fontawesome-solid-arrow-right: Change Quiz Language](/how-to-guides/change-quiz-language/)

## Consent & Transparency

When collecting personal information:

- Include a clear opt-out option for marketing consent
- Add a privacy policy link in the quiz content
- Make consent checkboxes clearly labeled and accessible

[:fontawesome-solid-arrow-right: Ask for Marketing Consent](/how-to-guides/ask-for-marketing-consent/)

[:fontawesome-solid-arrow-right: Marketing Consent Best Practices](/customer-success/ask-marketing-consent/)

## Customizable Accessibility Text

Merchants can customize screen reader text for key quiz interactions in **Quiz Builder > Quiz Settings > Accessibility**:

| Setting | Purpose |
|---------|---------|
| Quiz Complete | Announced when quiz is finished |
| No Previous Question | Announced at first question |
| Previous Question | Label for back button |
| Answer Before Proceeding | Prompt when answer is required |
| Next Question | Label for next button |
| Navigation Buttons | Description of navigation area |
| Results Bottom Bar | Description of results actions |

## Testing Your Quiz

We recommend testing your quiz for accessibility:

1. **Keyboard Only** - Complete the quiz using only Tab, Arrow keys, Enter, and Space
2. **Screen Reader** - Test with VoiceOver (Mac) or NVDA (Windows)
3. **Browser Zoom** - Verify the quiz works at 200% zoom
4. **Color Contrast** - If using custom colors, verify with a [contrast checker](https://webaim.org/resources/contrastchecker/)
5. **Mobile** - Test tap targets on actual mobile devices

## Standards

Our quiz renderer is built following these standards:

- **WCAG 2.1 Level AA** - Web Content Accessibility Guidelines
- **Section 508** - US federal accessibility requirements
- **ADA** - Americans with Disabilities Act digital accessibility guidelines

## Need Help?

We continuously work to improve accessibility, and if you ever notice an issue, please let us know—our team will address it promptly.

[:fontawesome-solid-arrow-right: Contact Customer Support](/how-to-guides/contact-customer-support/)

!!! info "VPAT Documentation"
    We don't currently provide a formal VPAT (Voluntary Product Accessibility Template) document. However, we're happy to help review any specific accessibility concerns you have with your live quiz setup. [Contact our support team](/how-to-guides/contact-customer-support/) and we'll work with you to address your needs.

---

**Related Articles:**

- [Questions Reference](/reference/quiz-builder/questions/)
- [Quiz Design Settings](/reference/quiz-builder/quiz-design/)
- [Change Quiz Language](/how-to-guides/change-quiz-language/)
- [Ask for Marketing Consent](/how-to-guides/ask-for-marketing-consent/)
