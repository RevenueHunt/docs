# CSS Structure Reference Guide

This guide provides a comprehensive overview of all CSS classes and selectors available in the `💎 Built for Shopify` RevenueHunt quiz app. Use this reference to customize the appearance of your quizzes.

## Table of Contents
- [Top-Level Container Structure](#top-level-container-structure)
- [Question Structure](#question-structure)
- [Question Blocks](#question-blocks)
- [Choice Blocks](#choice-blocks)
- [Background and Navigation](#background-and-navigation)
- [Results Structure](#results-structure)
- [Slot Components](#slot-components)
- [Animations](#animations)
- [Dynamic ID Patterns](#dynamic-id-patterns)
- [Common Use Cases](#common-use-cases)

## Top-Level Container Structure

### Main Selectors

| Selector | Description |
|----------|-------------|
| `main#quiz-{quizId}` | Main quiz container with dynamic ID |
| `.quiz` | Base quiz class - always present |
| `.mobile` | Applied when viewport < 480px |
| `.quiz-question` | Applied when showing question pages |
| `.quiz-result` | Applied when showing result pages |
| `.quiz-modal` | Modal type quiz styling |
| `.quiz-inline` | Inline type quiz styling |
| `.use-font-family-heading` | When custom heading font is set |
| `.use-font-family-body` | When custom body font is set |

### Examples

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

## Question Structure

### Main Selectors

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

### Examples

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

## Question Blocks

### Text Block Selectors

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

### Heading Block Selectors

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

### Button Block Selectors

| Selector | Description |
|----------|-------------|
| `#qbb-{ref}` | Button block with unique reference ID |
| `.question-button__container` | Button container |
| `.button.question_button` | Button element |
| `.question-button--left` | Left aligned button |
| `.question-button--center` | Center aligned button |
| `.question-button--right` | Right aligned button |
| `.button_text` | Button text span |

### Examples

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

## Choice Blocks

### Main Selectors

| Selector | Description |
|----------|-------------|
| `#qbc-{ref}` | Choice block container with unique reference ID |
| `.question-choice_list` | Choice list container |
| `.question-choice_list--multiple-choice` | Multiple choice type |
| `.question-choice_list--picture-choice` | Picture choice type |
| `.question-choice_list--slider-choice` | Slider choice type |
| `.question-choice_list--scroll-snap` | Horizontal scroll layout |
| `.picture-choice-{N}-choices` | Dynamic class based on choice count |
| `.picture-choice__tiny` | Tiny picture size |
| `.picture-choice__small` | Small picture size |
| `.picture-choice__medium` | Medium picture size |
| `.picture-choice__large` | Large picture size |

### Individual Choice Selectors

| Selector | Description |
|----------|-------------|
| `#qbcc-{ref}` | Individual choice with unique reference ID |
| `.question-choice__label` | Choice label wrapper |
| `.question-choice__label-selected` | Selected choice state |
| `.question-choice__label-content` | Choice content area |
| `.question-choice__label-thumbnail` | Choice image thumbnail |
| `.question-block__choice-error-message` | Error message container |

### Examples

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

## Background and Navigation

### Main Selectors

| Selector | Description |
|----------|-------------|
| `.question-background` | Question background base |
| `.background` | Background image position |
| `.background-split` | Split layout background |
| `.question-background-image` | Background image element |
| `.question-background-image--split` | Split layout background image |

### Navigation Bar Selectors

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

### Examples

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

## Results Structure

### Main Selectors

| Selector | Description |
|----------|-------------|
| `.content.results-content` | Main results content container |
| `#rs-{ref}` | Result section with unique reference ID |
| `.result-block__container` | Result section wrapper |
| `#rsb-{ref}` | Result block with unique reference ID |
| `.block.results-block` | Base result block class |

### Results Heading Selectors

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

### Results List Selectors

| Selector | Description |
|----------|-------------|
| `.results-slot_list` | Slot list container |
| `.results-slot_list-stacked` | Stacked layout |
| `.results-slot_list-side_by_side` | Side by side layout |
| `.results-slot_list__no_recommendations` | No recommendations state |

### Examples

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

## Slot Components

### Main Selectors

| Selector | Description |
|----------|-------------|
| `#rsbss-{ref}` | Individual slot with unique reference ID |
| `.results-slot_{width}` | Slot width classes (full, half, third) |
| `.results-slot_{N}-items` | Dynamic class based on item count |
| `.results-slot` | Individual slot item |
| `.results-slot.in-cart` | Item already in cart state |

### Product Elements

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

### Collection Elements

| Selector | Description |
|----------|-------------|
| `.slot-collection__title` | Collection title |
| `.slot-collection__image` | Collection image |

### Examples

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

## Animations

### Animation Classes

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

### Examples

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

## Dynamic ID Patterns

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
| `#r-{ref}` | Target specific result page |
| `#rs-{ref}` | Target specific result section |
| `#rsb-{ref}` | Target specific result block |
| `#rsbss-{ref}` | Target specific slot |

### Examples

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

## Common Use Cases

### Brand Color Customization

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

### Mobile-First Responsive Design

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

### Custom Typography Scale

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

### Product Grid Layout

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