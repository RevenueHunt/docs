---
icon: material/numeric-5
description: "When to use a personality or 'type' quiz, why they get shared, how a scoring quiz actually works, what the result page should do, and how to plan one that collects useful data and routes shoppers to the right outcome."
---

# Personality Quizzes: What They're For and How to Plan One

Personality and "type" quizzes ("What's your skin type?", "Find your scent profile", "Which plan fits you?") are some of the most engaging quizzes you can run. They get shared, they feel like fun rather than a sales pitch, and every answer is a declared preference you can use later.

This is a **planning** guide: how to decide whether one fits your goal and how to design it. The app setup differs between the Built for Shopify and Legacy versions, so the step-by-step build lives in the version-specific guides under [Setting it up](#setting-it-up).

---

<div class="rh-stats">
  <div class="rh-stat"><span class="rh-stat-num">2.75x</span><span class="rh-stat-label">conversion vs a typical store</span></div>
  <div class="rh-stat"><span class="rh-stat-num">75%</span><span class="rh-stat-label">of top quizzes require email</span></div>
  <div class="rh-stat"><span class="rh-stat-num">1 in 5</span><span class="rh-stat-label">orders land 30+ days later</span></div>
</div>

## Why personality quizzes work

They earn their place for three reasons a standard product quiz can't match:

- **They feel like fun, not a funnel.** With no obvious sales pressure, cold audiences who would skip a "find a product" quiz will happily take a "what's your type" one, so completion runs high.
- **People share their type.** A result that says something about *them* gets screenshotted and sent to friends. That's free, high-trust traffic back to your quiz, which is why these formats go viral when a product recommendation rarely does.
- **Every answer is still declared data.** Behind the fun, you're collecting the same zero-party data as any quiz. The type itself is a ready-made [segment](/customer-success/use-customer-tags-in-quiz/) you can act on for months.

---

## First, what's it *for*?

A personality quiz can serve very different goals, and the goal changes how you design it. Be clear which one is yours:

- **Gather leads / go viral.** Lead with fun and shareability, and ask for the email so the shopper can "see their type." Optimize for completion and social sharing.
- **Get to know your customers.** Prioritize questions whose answers become useful [segments](/customer-success/use-customer-tags-in-quiz/) you'll actually act on.
- **Improve your product or plan new features.** Read the aggregate patterns in your results to learn what customers want, then stock, bundle, or build accordingly.

If you can't name which of these you're after, decide that before you build anything.

---

## Personality quiz ideas by category

The "type" changes by catalog, but the format travels everywhere:

| Category | A "type" quiz that works |
|----------|--------------------------|
| [Beauty & skincare](/customer-success/quiz-for-beauty-skincare/) | Your skin type, or "what's your skin personality" |
| Fragrance | Find your scent profile |
| [Fashion](/customer-success/quiz-for-fashion-apparel/) | Your style persona |
| [Supplements & wellness](/customer-success/quiz-for-supplements-wellness/) | Your wellness type, or what your routine is missing |
| Coffee | Your coffee personality and roast match |
| [B2B / plans](/customer-success/quiz-for-b2b-compatibility/) | Which plan or tier fits you |

---

## How a scoring quiz actually works

A personality quiz is a **scoring quiz**, and it works differently from a standard product-recommendation quiz:

- A **product-recommendation quiz** ranks *products* by the votes each answer gives them, and shows the top products.
- A **scoring (personality) quiz** routes the shopper by the *pattern of their answers*. You attach **variables and scores** to each answer (for example, each choice adds a point to `dry`, `oily`, or `combination`). The quiz tallies them, and the shopper sees the result for their winning outcome.

Those are two separate mechanisms. A personality quiz is built on scoring, not on product votes.

<div style="margin:24px auto; max-width:420px;">
<svg viewBox="0 0 420 360" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;" role="img" aria-labelledby="sct scd" preserveAspectRatio="xMidYMid meet">
  <title id="sct">How a scoring quiz picks an outcome</title>
  <desc id="scd">Each answer adds points to outcome variables. The outcome with the highest score, here Oily, becomes the result the shopper sees.</desc>
  <defs>
    <marker id="sc-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#94a3b8"/></marker>
  </defs>
  <g font-family="system-ui, sans-serif">
    <text x="20" y="34" font-size="17" font-weight="700" fill="#16161D">Answers add up; highest score wins</text>
    <text x="20" y="92" font-size="15" fill="#334155">Dry</text>
    <rect x="150" y="76" width="70" height="26" rx="4" fill="#cbd5e1"/>
    <text x="20" y="142" font-size="15" font-weight="700" fill="#16161D">Oily</text>
    <rect x="150" y="126" width="200" height="26" rx="4" fill="#904E95"/>
    <text x="356" y="146" font-size="13" font-weight="700" fill="#904E95">winner</text>
    <text x="20" y="192" font-size="15" fill="#334155">Combination</text>
    <rect x="150" y="176" width="45" height="26" rx="4" fill="#cbd5e1"/>
    <line x1="210" y1="214" x2="210" y2="252" stroke="#cbd5e1" stroke-width="2" marker-end="url(#sc-arrow)"/>
    <rect x="70" y="256" width="280" height="80" rx="10" fill="#F6F0F7" stroke="#904E95" stroke-width="1.5"/>
    <text x="210" y="291" font-size="15" fill="#334155" text-anchor="middle">Result shown:</text>
    <text x="210" y="315" font-size="16" font-weight="700" fill="#16161D" text-anchor="middle">Oily skin routine</text>
  </g>
</svg>
<div class="rh-caption">Each answer adds points to an outcome; the highest-scoring outcome becomes the result the shopper sees.</div>
</div>

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

!!! example "A scent-profile quiz, planned"
    **Outcomes:** Fresh / Floral / Woody / Oriental.
    **Questions that separate them:** the season you prefer, day vs. night, a scent memory you love, how bold you like things. Each choice scores toward one profile.
    **Each outcome maps to:** a recommended set of fragrances in that family (the recommendation), a `scent: woody` tag (the segment), and a follow-up email styled to that profile (the message).
    That's a quiz that's fun to take *and* makes money. Drop any outcome that wouldn't have all three.

---

## Design the result to be shared and to sell

The result page is where a personality quiz either pays off or stays a toy. Make it do both jobs:

- **Name and flatter the type first.** People share a result that says something good about them. Give the type a memorable name and a short, positive description *before* you recommend anything.
- **Then recommend the matching set.** The type is the hook; the [recommended products or routine](/customer-success/recommend-bundles-kits/) are the payoff. Tie each pick back to the type so it reads as "made for you."
- **Invite the share.** A "share your type" prompt with a link to the quiz turns one taker into free traffic. Personality results get shared far more than product recommendations, so don't waste the moment.
- **Gate it on email only if lead-gen is the goal.** Asking for the email to "see your type" captures the lead, but weigh it against completion. If virality is the point, a softer ask keeps more people sharing.

---

## Turn the type into a segment

This is where a personality quiz pays off beyond engagement:

- **[Tag the outcome](/customer-success/use-customer-tags-in-quiz/)** (for example `skin-type: dry`) so it becomes a segment.
- **[Sync it to your CRM](/how-to-guides/send-leads-to-klaviyo/)** as a profile property to power targeted email and SMS flows.
- Use the same segments to [sharpen your ads](/customer-success/use-quiz-data-for-ads/).

---

## Measure it

A personality quiz earns its keep on two fronts, so track both:

- **Completion and sharing** justify the format. If a "type" quiz isn't finishing well or getting shared, the questions probably feel like a survey, not fun.
- **Whether each type's segment converts** proves it's revenue, not just entertainment. Watch the per-type segments in the [quiz metrics panel](/customer-success/track-quiz-metrics-for-better-conversions/) and in your CRM. A type that never converts is an outcome that maps nowhere.

---

## Do / Don't

- **Do** define your outcomes before writing a single question. It's the only way every result leads somewhere that makes you money (a recommendation, a segment, a flow) instead of a dead end. If two "types" end up with the same products, you've added friction for no payoff.
- **Do** keep it to 5-8 questions. Completion is where the value is: a longer quiz collects more data points from far fewer people, so you end up with *less* usable data, not more.
- **Do** name the type and invite the share. The shareable result is the free traffic engine that sets this format apart.
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

## Frequently asked questions

### What's the difference between a personality quiz and a product-recommendation quiz?

A personality (scoring) quiz routes the shopper by the pattern of their answers, using variables and scores. A product-recommendation quiz ranks products by the votes each answer gives them. They are two separate mechanisms.

### How many outcomes should a personality quiz have?

Three to six. Each outcome should map to a real recommendation, segment, or message. If a result leads nowhere, it is just entertainment.

### How do I get people to share their result?

Name the type something people want to be associated with, describe it positively, and add a "share your type" prompt with a link to the quiz on the results page. Personality results get shared far more than product recommendations.

### How do I set up the scoring?

You assign variables and scores to each answer, then surface the winning outcome. The exact steps differ between the Built for Shopify and Legacy versions, so follow the version-specific setup guides.

---

**Where to go next:** use the types you've collected to [grow your list and cut ad costs →](/customer-success/use-quiz-data-for-ads/)
