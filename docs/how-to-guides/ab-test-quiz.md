---
description: "Learn how to A/B test your RevenueHunt quiz to optimize conversions and find the best-performing quiz version."
icon: material/ab-testing
---

# How to A/B Test Your Product Recommendation Quiz

An A/B test, also called a split test, runs two versions of a quiz side by side and keeps whichever performs better.

The app has no A/B testing feature of its own. You build the test by hand: copy the quiz, change one thing in the copy, publish both, and split your traffic between them.

!!! info "Before you start"

    - A quiz you are ready to test, and somewhere to [publish it](/how-to-guides/publish-quiz/).
    - An analytics tool such as [Google Analytics](/how-to-guides/integrate-google-analytics/) or [Meta Pixel](/how-to-guides/integrate-meta-pixel/).
    - For a random split, access to the code of your website, or a developer who has it.

## Build the two versions

=== "Shopify"

    1. **Build the quiz you expect to perform best.** This is version A.

    2. **Open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Duplicate`.** The copy is version B.

    3. **Change one element of version B.** The title, the color scheme, the order of the questions, the wording of a single question: pick one.

    4. **Click the top-right `Save` button.**

    !!! warning "One element per test"

        Change two things at once and a difference in the results cannot tell you which one caused it.

=== "Shopify (Legacy)"

    1. **Build the quiz you expect to perform best.** This is version A.

    2. **Open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Make a copy`.** The copy is version B.

    3. **Change one element of version B.** The title, the color scheme, the order of the questions, the wording of a single question: pick one.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! warning "One element per test"

        Change two things at once and a difference in the results cannot tell you which one caused it.

=== "WooCommerce"

    1. **Build the quiz you expect to perform best.** This is version A.

    2. **Open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Make a copy`.** The copy is version B.

    3. **Change one element of version B.** The title, the color scheme, the order of the questions, the wording of a single question: pick one.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! warning "One element per test"

        Change two things at once and a difference in the results cannot tell you which one caused it.

=== "Magento"

    1. **Build the quiz you expect to perform best.** This is version A.

    2. **Open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Make a copy`.** The copy is version B.

    3. **Change one element of version B.** The title, the color scheme, the order of the questions, the wording of a single question: pick one.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! warning "One element per test"

        Change two things at once and a difference in the results cannot tell you which one caused it.

=== "BigCommerce"

    1. **Build the quiz you expect to perform best.** This is version A.

    2. **Open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Make a copy`.** The copy is version B.

    3. **Change one element of version B.** The title, the color scheme, the order of the questions, the wording of a single question: pick one.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! warning "One element per test"

        Change two things at once and a difference in the results cannot tell you which one caused it.

=== "Standalone"

    1. **Build the quiz you expect to perform best.** This is version A.

    2. **Open the `...` menu on the [Dashboard](/reference/dashboard/) and click `Make a copy`.** The copy is version B.

    3. **Change one element of version B.** The title, the color scheme, the order of the questions, the wording of a single question: pick one.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz.

    !!! warning "One element per test"

        Change two things at once and a difference in the results cannot tell you which one caused it.

## Publish both versions and split the traffic

There are two routes. Which one fits depends on whether you can edit the code of your website.

**A page each, and no code**

1. **Publish version A as an [inline quiz on its own page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).**

2. **Publish version B the same way, on a second page.**

3. **Send traffic to both pages.** Link one from your navigation and the other from an email, or point two ad campaigns at them.

This split is only as even as the traffic you send. It suits a test where you can aim comparable audiences at each page.

**A random split, and some code**

1. **Create one entry point, such as a button or a link.** See [How to Set Up a Quiz Link Popup on Your Store](/how-to-guides/publish-quiz-link/).

2. **Ask a developer to add a snippet that sends each new customer to version A or version B at random.**

3. **Ask them to keep each customer on the same version.** Someone who comes back and gets re-randomized blurs the two sets of figures into each other.

This route splits the traffic evenly, and it is the one to use when both versions face the same audience.

## Measure the result

=== "Shopify"

    1. **Decide which number settles the test, before it starts.** Completion rate, conversion rate or revenue per response: pick one.

    2. **Read the built-in figures for each version.** Open the `...` menu on the Dashboard and click [`Analytics`](/reference/quiz-builder/metrics/#analytics), which records starts, completions, conversion rate and drop-off for that quiz.

    3. **Connect each version to your analytics tool.** [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) follow the customer past the quiz, to the sale.

    4. **Wait until both versions have collected enough responses.** A handful on each side proves nothing.

    5. **Compare the two versions on the number you picked.**

=== "Shopify (Legacy)"

    1. **Decide which number settles the test, before it starts.** Completion rate, conversion rate or total cart value: pick one.

    2. **Read the built-in figures for each version.** Open the [`Metrics`](/reference/quiz-builder/metrics/) tab in the Quiz Builder, which records starts, completions, completion rate and total cart value for that quiz.

    3. **Connect each version to your analytics tool.** [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) follow the customer past the quiz, to the sale.

    4. **Wait until both versions have collected enough responses.** A handful on each side proves nothing.

    5. **Compare the two versions on the number you picked.**

=== "WooCommerce"

    1. **Decide which number settles the test, before it starts.** Completion rate, conversion rate or total cart value: pick one.

    2. **Read the built-in figures for each version.** Open the [`Metrics`](/reference/quiz-builder/metrics/) tab in the Quiz Builder, which records starts, completions, completion rate and total cart value for that quiz.

    3. **Connect each version to your analytics tool.** [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) follow the customer past the quiz, to the sale.

    4. **Wait until both versions have collected enough responses.** A handful on each side proves nothing.

    5. **Compare the two versions on the number you picked.**

=== "Magento"

    1. **Decide which number settles the test, before it starts.** Completion rate, conversion rate or total cart value: pick one.

    2. **Read the built-in figures for each version.** Open the [`Metrics`](/reference/quiz-builder/metrics/) tab in the Quiz Builder, which records starts, completions, completion rate and total cart value for that quiz.

    3. **Connect each version to your analytics tool.** [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) follow the customer past the quiz, to the sale.

    4. **Wait until both versions have collected enough responses.** A handful on each side proves nothing.

    5. **Compare the two versions on the number you picked.**

=== "BigCommerce"

    1. **Decide which number settles the test, before it starts.** Completion rate, conversion rate or total cart value: pick one.

    2. **Read the built-in figures for each version.** Open the [`Metrics`](/reference/quiz-builder/metrics/) tab in the Quiz Builder, which records starts, completions, completion rate and total cart value for that quiz.

    3. **Connect each version to your analytics tool.** [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) follow the customer past the quiz, to the sale.

    4. **Wait until both versions have collected enough responses.** A handful on each side proves nothing.

    5. **Compare the two versions on the number you picked.**

=== "Standalone"

    1. **Decide which number settles the test, before it starts.** Completion rate, conversion rate or total cart value: pick one.

    2. **Read the built-in figures for each version.** Open the [`Metrics`](/reference/quiz-builder/metrics/) tab in the Quiz Builder, which records starts, completions, completion rate and total cart value for that quiz.

    3. **Connect each version to your analytics tool.** [Google Analytics](/how-to-guides/integrate-google-analytics/) and [Meta Pixel](/how-to-guides/integrate-meta-pixel/) follow the customer past the quiz, to the sale.

    4. **Wait until both versions have collected enough responses.** A handful on each side proves nothing.

    5. **Compare the two versions on the number you picked.**

## Apply what you learned

Fold the winning change into your main quiz, then pick the next single element to test.

!!! tip "What makes a test worth trusting"

    - Change one element per test.
    - Run both versions over the same period. A week measured against a weekend is not a comparison.
    - Collect a sample large enough that a few responses either way could not flip the result.

---

This article explains how to A/B test a quiz in the RevenueHunt app. It covers creating two versions, publishing both, splitting traffic between them and comparing the results.