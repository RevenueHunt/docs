---
icon: material/numeric-5
description: "When to use a personality or 'type' quiz, how a scoring quiz actually works, and how to plan one that collects useful data and routes shoppers to the right outcome."
---

# Personality Quizzes: What They're For and How to Plan One

Personality and "type" quizzes ("What's your skin type?", "Find your scent profile", "Which plan fits you?") are some of the most engaging quizzes you can run. They get shared, they feel like fun rather than a sales pitch, and every answer is a declared preference you can use later.

This is a **planning** guide: how to decide whether one fits your goal and how to design it. The app setup differs between the Built for Shopify and Legacy versions, so the step-by-step build lives in the version-specific guides under [Setting it up](#setting-it-up).

---

## First, what's it *for*?

A personality quiz can serve very different goals, and the goal changes how you design it. Be clear which one is yours:

- **Gather leads / go viral.** Lead with fun and shareability, and ask for the email so the shopper can "see their type." Optimize for completion and social sharing.
- **Get to know your customers.** Prioritize questions whose answers become useful [segments](/customer-success/use-customer-tags-in-quiz/) you'll actually act on.
- **Improve your product or plan new features.** Read the aggregate patterns in your results to learn what customers want, then stock, bundle, or build accordingly.

If you can't name which of these you're after, decide that before you build anything.

---

## How a scoring quiz actually works

A personality quiz is a **scoring quiz**, and it works differently from a standard product-recommendation quiz:

- A **product-recommendation quiz** ranks *products* by the votes each answer gives them, and shows the top products.
- A **scoring (personality) quiz** routes the shopper by the *pattern of their answers*. You attach **variables and scores** to each answer (for example, each choice adds a point to `dry`, `oily`, or `combination`). The quiz tallies them, and the shopper sees the result for their winning outcome.

Those are two separate mechanisms. A personality quiz is built on scoring, not on product votes.

There are a few common ways to turn the score into a result. You don't choose this now, but knowing they exist helps you plan:

- **Winning variable** (classic personality type): the variable with the highest tally wins, and the matching result is shown.
- **Score range**: a numeric total falls into a band (for example 13-17 = "oily").
- **Dedicated result pages**: when each outcome deserves its own full page, the quiz routes there.

Which one you use, and exactly how it's configured, depends on your app version (see [Setting it up](#setting-it-up)).

---

## How to plan one

1. **Define your outcomes first.** List the 3-6 results a shopper can land on (for skin type: Dry / Oily / Combination / Sensitive / Normal). Work backwards from these.
2. **Write questions that tell the outcomes apart.** Every question should push toward one outcome more than the others. If an answer doesn't help distinguish between types, cut it. Keep to **5-8 questions** so completion stays high.
3. **Decide what each outcome maps to.** A recommendation, a segment, a message, or all three. Same test as any [data worth collecting](/customer-success/what-data-to-collect/): if a result leads nowhere, it's just entertainment.
4. **Decide how different the results need to look.** If each type just needs its own write-up and a few products, a single results page is enough. If a type deserves a full, distinct page, plan for that. This is what determines which setup pattern you'll use.

---

## Turn the type into a segment

This is where a personality quiz pays off beyond engagement:

- **[Tag the outcome](/customer-success/use-customer-tags-in-quiz/)** (for example `skin-type: dry`) so it becomes a segment.
- **[Sync it to your CRM](/how-to-guides/send-leads-to-klaviyo/)** as a profile property to power targeted email and SMS flows.
- Use the same segments to [sharpen your ads](/customer-success/use-quiz-data-for-ads/).

---

## Do / Don't

- **Do** define your outcomes before writing a single question. It's the only way every result leads somewhere that makes you money (a recommendation, a segment, a flow) instead of a dead end. If two "types" end up with the same products, you've added friction for no payoff.
- **Do** keep it to 5-8 questions. Completion is where the value is: a longer quiz collects more data points from far fewer people, so you end up with *less* usable data, not more.
- **Do** tag and sync every outcome. The shareable quiz is nice, but the segment is what keeps selling for months afterward. Skip this and you've built entertainment, not a revenue engine.
- **Don't** confuse it with a product-recommendation quiz. If your real goal is "show the right product," a vote-based [recommendation quiz](/customer-success/what-data-to-collect/) gets there faster. Reach for scoring only when the *type itself* is the point.
- **Don't** ask questions that don't change the result. Every extra question costs you completions, so an answer that doesn't move someone toward a type is leaking leads for nothing.
- **Don't** let a type be a dead end. An outcome with no recommendation, no follow-up, and no segment is a sale you paid to acquire and then walked away from.

---

## Setting it up

Assigning scores and surfacing the right result is configured in the app, and the steps differ between the **Built for Shopify** version (which supports scoring and variables natively) and the **Legacy** version. Follow the guide for your version rather than a one-size-fits-all recipe:

- [Building a Skin Type Quiz](/tutorials/skintype-quiz/), a worked example of a scoring personality quiz
- [Conditional Logic reference](/reference/quiz-builder/conditional-logic/), which shows the version-specific Display Logic and Jump Logic used to surface results
- RevenueHunt's [scoring and personality-type quiz setup guide](https://revenuehunt.com/scoring-quiz-setup/){target=_blank}

---

**Learn more:** [A complete guide to personality-type quizzes](https://revenuehunt.com/guide-to-building-a-personality-type-quiz-with-revenuehunt/){target=_blank}

**Where to go next:** use the types you've collected to [grow your list and cut ad costs →](/customer-success/use-quiz-data-for-ads/)
