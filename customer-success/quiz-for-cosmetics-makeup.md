---
title: "Cosmetics & Makeup Quiz Playbook: What the Best Quizzes Do"
description: "A data-backed playbook for makeup and cosmetics brands, built from 121 real RevenueHunt quizzes: shade and undertone questions, the benchmark build, and the conversion numbers to beat."
---

# A Quiz Playbook for Cosmetics & Makeup Brands

Makeup lives or dies on the *match*: the wrong shade, undertone, or finish is an instant return and a lost customer. Shoppers can't reliably self-diagnose their undertone from a product grid, so they hesitate or guess. A quiz turns "which shade is me?" into a few quick questions and hands back a confident match: a shade finder, a colour-season result, or a full face in their tones.

This playbook is built from **121 real cosmetics and makeup quizzes** running on RevenueHunt.

<div class="rh-stats">
  <div class="rh-stat"><span class="rh-stat-num">6%</span><span class="rh-stat-label">median quiz→order conversion</span></div>
  <div class="rh-stat"><span class="rh-stat-num">23%</span><span class="rh-stat-label">conversion for the top 10%</span></div>
  <div class="rh-stat"><span class="rh-stat-num">5</span><span class="rh-stat-label">median number of questions</span></div>
  <div class="rh-stat"><span class="rh-stat-num">79%</span><span class="rh-stat-label">recommend a set, not one product</span></div>
</div>

!!! info "How to read these benchmarks"
    Figures come from **121 cosmetics/makeup quizzes** built with RevenueHunt (Built for Shopify), measured over the last 180 days and deduplicated to one quiz per store. Numbers are **medians** unless labelled "top 10%" (the 90th percentile). For the wider category picture, see the [State of Product Recommendation Quizzes report](https://revenuehunt.com/state-of-product-recommendation-quizzes/){target=_blank}.

<div style="margin:24px auto; max-width:460px;">
<svg viewBox="0 0 460 118" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;" role="img" aria-labelledby="t-dev-makeup d-dev-makeup" preserveAspectRatio="xMidYMid meet">
  <title id="t-dev-makeup">Where makeup quiz traffic comes from</title>
  <desc id="d-dev-makeup">Device mix for makeup quizzes: mobile 88%, desktop 9%, tablet 2%.</desc>
  <g font-family="system-ui, sans-serif">
    <text x="20" y="28" font-size="15.5" font-weight="700" fill="#16161D">Where makeup quiz traffic comes from</text>
    <rect x="20" y="46" width="369.6" height="34" fill="#904E95" stroke="#ffffff" stroke-width="1.5"/>
    <text x="204.8" y="68" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">88%</text>
    <rect x="389.6" y="46" width="37.8" height="34" fill="#cbd5e1" stroke="#ffffff" stroke-width="1.5"/>
    <rect x="427.4" y="46" width="8.4" height="34" fill="#e2e8f0" stroke="#ffffff" stroke-width="1.5"/>
    <rect x="20" y="90" width="12" height="12" rx="2" fill="#904E95"/>
    <text x="38" y="100" font-size="12.5" fill="#334155">Mobile 88%</text>
    <rect x="170" y="90" width="12" height="12" rx="2" fill="#cbd5e1"/>
    <text x="188" y="100" font-size="12.5" fill="#334155">Desktop 9%</text>
    <rect x="320" y="90" width="12" height="12" rx="2" fill="#e2e8f0"/>
    <text x="338" y="100" font-size="12.5" fill="#334155">Tablet 2%</text>
  </g>
</svg>
<div class="rh-caption">Device mix for makeup quizzes. 88% is mobile, so design mobile-first.</div>
</div>

---

## The benchmark build

The top makeup quizzes by revenue share a tight, fast shape, the shortest of the beauty categories:

!!! success "What the top makeup quizzes have in common"
    - **5 questions**, around **4.4 answer choices** each
    - A **set or palette recommendation**, not a single item. **79%** of quizzes do this
    - Typically **4 products** on the results page
    - **Email gated** before results in the top performers
    - **Picture questions** for the visual signals (undertone, eye colour, shade)

Makeup quizzes are short because the match is mostly visual, a few well-chosen picture questions get there faster than a long interview.

---

## How your quiz stacks up

Performance percentiles across all 121 cosmetics/makeup quizzes.

| Metric | Bottom 25% | Median | Top 25% | Top 10% |
|---|---|---|---|---|
| **Completion rate** | 71% | 74% | 99% | 100% |
| **Conversion (quiz→order)** | 2% | 6% | 13% | 23% |
| **Revenue per completion** | $0.78 | $3.84 | $9.27 | $20 |
| **Average order value** | $41 | $65 | $94 | $150 |

!!! tip "Completion is the makeup weak spot"
    Median completion is **74%**, lower than skincare (88%) or haircare (97%). Makeup quizzes lose people mid-flow more often, usually to questions that are too long or shades that are hard to judge from text. Use **picture choices** for undertone, eye colour, and shade, and keep to ~5 questions. That's the cheapest completion win in this category.

---

## The questions that matter

The most common questions in top makeup quizzes are overwhelmingly *visual*, they ask shoppers to recognise, not describe:

- **What's your skin undertone?** Warm, cool, neutral. The single highest-value question for a shade match.
- **Select the eye colour closest to your own.** A picture question that drives palette and shade recommendations.
- **What's your go-to colour palette?** Reads their taste, so the result feels chosen for them.
- **What are you shopping for?** Routes between face, eyes, lips before recommending.
- **What does a typical day look like?** Natural vs full glam changes the finish and coverage you recommend.

Every one maps to a product, a segment, or a message, the [data-worth-collecting](/customer-success/what-data-to-collect/) test. Lean on [picture choice questions](/reference/quiz-builder/questions/#question-types) wherever the answer is something the shopper can *see* better than name.

---

## Recommend a coordinated set

**79% of makeup quizzes recommend a set**, not a single product, and it makes sense: makeup is bought in looks. Once you know undertone and palette, you can recommend a coordinated face (base, eyes, lips) that works together.

- Use slots for the steps of a look and let the app rank each by the shopper's answers. See [Set up recommendations](/how-to-guides/set-up-recommendations/) and the [bundles, kits & routines](/customer-success/recommend-bundles-kits/) playbook.
- Keep the results page to about **4 products**, the benchmark count, so the choice stays easy.
- Tie each pick to an answer ("this shade because your undertone is warm") to build confidence in the match.

<div style="margin:24px auto; max-width:460px;">
<svg viewBox="0 0 460 118" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;" role="img" aria-labelledby="t-rec-makeup d-rec-makeup" preserveAspectRatio="xMidYMid meet">
  <title id="t-rec-makeup">How makeup quizzes recommend</title>
  <desc id="d-rec-makeup">Recommendation style for makeup quizzes: set/routine 79%, single 21%.</desc>
  <g font-family="system-ui, sans-serif">
    <text x="20" y="28" font-size="15.5" font-weight="700" fill="#16161D">How makeup quizzes recommend</text>
    <rect x="20" y="46" width="331.8" height="34" fill="#904E95" stroke="#ffffff" stroke-width="1.5"/>
    <text x="185.9" y="68" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">79%</text>
    <rect x="351.8" y="46" width="88.2" height="34" fill="#cbd5e1" stroke="#ffffff" stroke-width="1.5"/>
    <text x="395.9" y="68" font-size="13" font-weight="700" fill="#16161D" text-anchor="middle">21%</text>
    <rect x="20" y="90" width="12" height="12" rx="2" fill="#904E95"/>
    <text x="38" y="100" font-size="12.5" fill="#334155">Set/routine 79%</text>
    <rect x="170" y="90" width="12" height="12" rx="2" fill="#cbd5e1"/>
    <text x="188" y="100" font-size="12.5" fill="#334155">Single 21%</text>
  </g>
</svg>
<div class="rh-caption">Share of makeup quizzes by recommendation style. Most recommend a set rather than a single product.</div>
</div>

---

## Get the email right

Makeup quizzes are split on email, leaning toward *not* gating:

- **45% don't ask** for an email · **37% gate** it before results · **18%** make it optional.
- That reflects a more impulse-led, lower-AOV category (median order $65) where completion is already fragile and merchants are wary of adding friction.

<div style="margin:24px auto; max-width:460px;">
<svg viewBox="0 0 460 200" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; display:block;" role="img" aria-labelledby="egt-makeup egd-makeup" preserveAspectRatio="xMidYMid meet">
  <title id="egt-makeup">Email strategy across makeup quizzes</title>
  <desc id="egd-makeup">Share of makeup quizzes by email approach: none 45%, gated 37%, optional 18%.</desc>
  <g font-family="system-ui, sans-serif">
    <text x="20" y="30" font-size="15.5" font-weight="700" fill="#16161D">Email strategy across makeup quizzes</text>
    <text x="20" y="69" font-size="14" fill="#334155">None</text>
    <rect x="132" y="52" width="117.0" height="24" rx="4" fill="#904E95"/>
    <text x="257.0" y="69" font-size="14" font-weight="700" fill="#16161D">45%</text>
    <text x="20" y="109" font-size="14" fill="#334155">Gated</text>
    <rect x="132" y="92" width="96.2" height="24" rx="4" fill="#cbd5e1"/>
    <text x="236.2" y="109" font-size="14" font-weight="700" fill="#16161D">37%</text>
    <text x="20" y="149" font-size="14" fill="#334155">Optional</text>
    <rect x="132" y="132" width="46.8" height="24" rx="4" fill="#cbd5e1"/>
    <text x="186.8" y="149" font-size="14" font-weight="700" fill="#16161D">18%</text>
    <text x="20" y="188" font-size="11" fill="#64748b">Gated = email required before results · Optional = skippable · None = no email ask</text>
  </g>
</svg>
<div class="rh-caption">How makeup quizzes handle the email ask. The accented bar is the most common approach in this category.</div>
</div>

!!! tip "The makeup default"
    Because completion is the soft spot here, lead with **optional** email rather than a hard gate: you still capture a large share of finishers, without scaring off the shoppers you're already struggling to keep through to the result. Whatever you choose, send the shade-match result by email so the look is one tap from cart later, connect [Klaviyo](/how-to-guides/send-leads-to-klaviyo/).

---

## What the top and bottom quizzes look like

!!! success "📈 Best in class"
    A makeup store (~768 responses/180d) runs a longer, **18-question** quiz with branching and a **gated** email, recommending a set. The result: **$26 revenue per completion**, **27% conversion**, **100% completion**. Proof that a long quiz *can* work, but only when branching keeps each shopper's path short and every answer is mapped.

!!! danger "📉 What kills a makeup quiz"
    A makeup store (~567 responses/180d) runs a **21-question** quiz that **gates the email** before any result. Conversion: **0%**. Two problems compound: it's too long, and it demands an email before delivering value. Shorten toward 5 questions and show the match first.

---

## Turn shade data into repeat revenue

Undertone and palette are durable segments, they don't change between purchases:

- **[Tag undertone, palette, and finish](/customer-success/use-customer-tags-in-quiz/)** so each shopper becomes a reusable segment.
- **[Convert and retain](/customer-success/convert-leads-to-customers/)** by emailing new shades and limited drops in their exact tones, a personal pull, not a blast.
- **[Sharpen your ads](/customer-success/use-quiz-data-for-ads/)** by targeting each colour segment with products made for them.

**88% of makeup quiz traffic is mobile**, the highest of any beauty category, so picture questions and big tap targets aren't optional.

---

## Do / Don't

- **Do** use picture questions for undertone, eye colour, and shade. The match is visual, and it's the biggest completion lever in this category.
- **Do** keep it to ~5 questions, the shortest benchmark in beauty, to protect the soft 74% completion rate.
- **Do** recommend a coordinated set of ~4 products. 79% of quizzes do, and looks sell better than singles.
- **Don't** gate the email before delivering the match. With completion already fragile, a hard gate is what produces 0% conversion.
- **Don't** stretch past a handful of questions unless branching keeps each path short, as the best-in-class example does.

---

## Templates & setup

- [Quiz templates by industry](https://revenuehunt.com/templates/){target=_blank}, including shade-finder and colour-match starting points
- [Question types](/reference/quiz-builder/questions/#question-types), set up picture choice questions
- [Set up recommendations](/how-to-guides/set-up-recommendations/) to build a coordinated look
- [Plan a personality quiz](/customer-success/personality-quizzes/) for a "find your colour season" hook

## Frequently asked questions

### What questions should a makeup quiz ask?

Skin undertone, eye colour, go-to palette, what they're shopping for, and their everyday look. Make the visual ones (undertone, eye colour, shade) picture questions. Keep it to about 5 questions.

### Why is my makeup quiz losing people halfway?

Median makeup completion is only 74%, usually because questions are too long or shades are hard to judge from text. Switch visual questions to picture choices and cut the quiz toward 5 questions.

### Should a makeup quiz recommend one product or a set?

A coordinated set, 79% of quizzes do. Once you know undertone and palette, recommend a face that works together (base, eyes, lips), about 4 products, each tied to an answer.

### What's a good conversion rate for a makeup quiz?

The median is 6% (completion → order), the top 25% reach 13%, and the top 10% hit 23%. Fixing completion (picture questions, shorter quiz) is usually the fastest way to move it.

---

**Where to go next:** maximize each order with the [bundles, kits & routines playbook →](/customer-success/recommend-bundles-kits/)
