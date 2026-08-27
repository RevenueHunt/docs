---
icon: material/hanger
description: "Complete guide to recommending accurate clothing sizes in RevenueHunt quiz based on measurements."
---

# How to Recommend Sizes Based on Measurements

=== "Shopify"

    Recommending the right size in a RevenueHunt quiz (for bras, clothing, footwear, or any fit-based product) requires a structured approach. This article explains why an open-ended measurement input does not work. It covers how to design questions that give accurate size recommendations, and what to do when you need a precise calculation.

=== "Shopify (Legacy)"

    Recommending the right size in a RevenueHunt quiz (for bras, clothing, footwear, or any fit-based product) requires a structured approach. This article explains why an open-ended measurement input does not work. It covers how to design questions that give accurate size recommendations, and what to do when you need a precise calculation.

=== "WooCommerce"

    Recommending the right size in a RevenueHunt quiz (for bras, clothing, footwear, or any fit-based product) requires a structured approach. This article explains why an open-ended measurement input does not work. It covers how to design questions that give accurate size recommendations, and what to do when you need a precise calculation.

=== "Magento"

    Recommending the right size in a RevenueHunt quiz (for bras, clothing, footwear, or any fit-based product) requires a structured approach. This article explains why an open-ended measurement input does not work. It covers how to design questions that give accurate size recommendations, and what to do when you need a precise calculation.

=== "BigCommerce"

    Recommending the right size in a RevenueHunt quiz (for bras, clothing, footwear, or any fit-based product) requires a structured approach. This article explains why an open-ended measurement input does not work. It covers how to design questions that give accurate size recommendations, and what to do when you need a precise calculation.

=== "Standalone"

    Recommending the right size in a RevenueHunt quiz (for bras, clothing, footwear, or any fit-based product) requires a structured approach. This article explains why an open-ended measurement input does not work. It covers how to design questions that give accurate size recommendations, and what to do when you need a precise calculation.


## Why open-ended questions do not work

=== "Shopify"

    You might ask customers to type an exact measurement: "Enter your underbust measurement in inches". Using that number to return a size does not work, because an open-ended [Number](/reference/quiz-builder/questions/#number) question does not support product recommendations.

    The quiz recommendation engine works by linking each answer choice to a fixed list of products. When a customer selects that answer, every product in the list receives one upvote. The product with the most upvotes at the end is recommended.

    **A typed number cannot be linked to anything in advance**. A customer can enter any value, so there is no product list to attach to it. The upvoting system has nothing to count.

    This applies to any question where the answer is unpredictable: exact measurements, dates and free text. To recommend products, every possible answer must be defined by you before the quiz goes live.

    ??? info "Why can I not use open-ended inputs for size recommendations?"

        An open-ended number field lets a customer type any value, so those answers cannot be linked to specific products. Use predefined choices instead. See [How to Recommend Products Based on Numerical Inputs](/how-to-guides/recommend-products-based-on-numerical-inputs/).

        <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/m92ELGhOq38?si=H7vJC9sn44PVQfd7" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>



=== "Shopify (Legacy)"

    You might ask customers to type an exact measurement: "Enter your underbust measurement in inches". Using that number to return a size does not work, because an open-ended [Number](/reference/quiz-builder/questions/#number) question does not support product recommendations.

    The quiz recommendation engine works by linking each answer choice to a fixed list of products. When a customer selects that answer, every product in the list receives one upvote. The product with the most upvotes at the end is recommended.

    **A typed number cannot be linked to anything in advance**. A customer can enter any value, so there is no product list to attach to it. The upvoting system has nothing to count.

    This applies to any question where the answer is unpredictable: exact measurements, dates and free text. To recommend products, every possible answer must be defined by you before the quiz goes live.

=== "WooCommerce"

    You might ask customers to type an exact measurement: "Enter your underbust measurement in inches". Using that number to return a size does not work, because an open-ended [Number](/reference/quiz-builder/questions/#number) question does not support product recommendations.

    The quiz recommendation engine works by linking each answer choice to a fixed list of products. When a customer selects that answer, every product in the list receives one upvote. The product with the most upvotes at the end is recommended.

    **A typed number cannot be linked to anything in advance**. A customer can enter any value, so there is no product list to attach to it. The upvoting system has nothing to count.

    This applies to any question where the answer is unpredictable: exact measurements, dates and free text. To recommend products, every possible answer must be defined by you before the quiz goes live.

=== "Magento"

    You might ask customers to type an exact measurement: "Enter your underbust measurement in inches". Using that number to return a size does not work, because an open-ended [Number](/reference/quiz-builder/questions/#number) question does not support product recommendations.

    The quiz recommendation engine works by linking each answer choice to a fixed list of products. When a customer selects that answer, every product in the list receives one upvote. The product with the most upvotes at the end is recommended.

    **A typed number cannot be linked to anything in advance**. A customer can enter any value, so there is no product list to attach to it. The upvoting system has nothing to count.

    This applies to any question where the answer is unpredictable: exact measurements, dates and free text. To recommend products, every possible answer must be defined by you before the quiz goes live.

=== "BigCommerce"

    You might ask customers to type an exact measurement: "Enter your underbust measurement in inches". Using that number to return a size does not work, because an open-ended [Number](/reference/quiz-builder/questions/#number) question does not support product recommendations.

    The quiz recommendation engine works by linking each answer choice to a fixed list of products. When a customer selects that answer, every product in the list receives one upvote. The product with the most upvotes at the end is recommended.

    **A typed number cannot be linked to anything in advance**. A customer can enter any value, so there is no product list to attach to it. The upvoting system has nothing to count.

    This applies to any question where the answer is unpredictable: exact measurements, dates and free text. To recommend products, every possible answer must be defined by you before the quiz goes live.

=== "Standalone"

    You might ask customers to type an exact measurement: "Enter your underbust measurement in inches". Using that number to return a size does not work, because an open-ended [Number](/reference/quiz-builder/questions/#number) question does not support product recommendations.

    The quiz recommendation engine works by linking each answer choice to a fixed list of products. When a customer selects that answer, every product in the list receives one upvote. The product with the most upvotes at the end is recommended.

    **A typed number cannot be linked to anything in advance**. A customer can enter any value, so there is no product list to attach to it. The upvoting system has nothing to count.

    This applies to any question where the answer is unpredictable: exact measurements, dates and free text. To recommend products, every possible answer must be defined by you before the quiz goes live.


## Use ranges instead of exact numbers

=== "Shopify"

    To make size recommendations work, **replace any measurement input with a dropdown or multiple-choice question**. Instead of asking for an exact number, offer predefined measurement ranges as answer choices.

    !!! example "Example - Bra Size Quiz"

        Instead of "Enter your underbust measurement", use a dropdown:

        - Under 27" / Under 69 cm
        - 27–28" / 69–71 cm
        - 29–30" / 74–76 cm
        - 31–32" / 79–81 cm
        - 33–34" / 84–86 cm
        - 35–36" / 89–91 cm

        Each option maps to a fixed band size. You can then [upvote](/reference/quiz-builder/link-products/) every product variant with that band to the choice.

        ![measurement range dropdown question](/images/how_to_recommend_sizes_dropdown_ranges.png)

    Once you use finite answer choices, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants, or collections to each choice
    - Set up [Jump logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the customer's selection

    !!! tip "Use Quiz Copilot to generate the choices for you"

        If you are working with a large number of size variants, you can use [Quiz CoPilot](/how-to-guides/use-quiz-copilot/) to generate the choices for you.

        Open Quiz Copilot from the quiz editor and share your product list and sizing logic. Ask it to generate the choices for you.

        Copilot will generate the choices for you automatically and help match them to recommendations.

=== "Shopify (Legacy)"

    To make size recommendations work, **replace any measurement input with a dropdown or multiple-choice question**. Instead of asking for an exact number, offer predefined measurement ranges as answer choices.

    !!! example "Example - Bra Size Quiz"

        Instead of "Enter your underbust measurement", use a dropdown:

        - Under 27" / Under 69 cm
        - 27–28" / 69–71 cm
        - 29–30" / 74–76 cm
        - 31–32" / 79–81 cm
        - 33–34" / 84–86 cm
        - 35–36" / 89–91 cm

        Each option maps to a fixed band size. You can then [upvote](/reference/quiz-builder/link-products/) every product variant with that band to the choice.

        ![measurement range dropdown question](/images/how_to_recommend_sizes_dropdown_ranges.png)

    Once you use finite answer choices, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants, or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the customer's selection

=== "WooCommerce"

    To make size recommendations work, **replace any measurement input with a dropdown or multiple-choice question**. Instead of asking for an exact number, offer predefined measurement ranges as answer choices.

    !!! example "Example - Bra Size Quiz"

        Instead of "Enter your underbust measurement", use a dropdown:

        - Under 27" / Under 69 cm
        - 27–28" / 69–71 cm
        - 29–30" / 74–76 cm
        - 31–32" / 79–81 cm
        - 33–34" / 84–86 cm
        - 35–36" / 89–91 cm

        Each option maps to a fixed band size. You can then [upvote](/reference/quiz-builder/link-products/) every product variant with that band to the choice.

        ![measurement range dropdown question](/images/how_to_recommend_sizes_dropdown_ranges.png)

    Once you use finite answer choices, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants, or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the customer's selection

=== "Magento"

    To make size recommendations work, **replace any measurement input with a dropdown or multiple-choice question**. Instead of asking for an exact number, offer predefined measurement ranges as answer choices.

    !!! example "Example - Bra Size Quiz"

        Instead of "Enter your underbust measurement", use a dropdown:

        - Under 27" / Under 69 cm
        - 27–28" / 69–71 cm
        - 29–30" / 74–76 cm
        - 31–32" / 79–81 cm
        - 33–34" / 84–86 cm
        - 35–36" / 89–91 cm

        Each option maps to a fixed band size. You can then [upvote](/reference/quiz-builder/link-products/) every product variant with that band to the choice.

        ![measurement range dropdown question](/images/how_to_recommend_sizes_dropdown_ranges.png)

    Once you use finite answer choices, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants, or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the customer's selection

=== "BigCommerce"

    To make size recommendations work, **replace any measurement input with a dropdown or multiple-choice question**. Instead of asking for an exact number, offer predefined measurement ranges as answer choices.

    !!! example "Example - Bra Size Quiz"

        Instead of "Enter your underbust measurement", use a dropdown:

        - Under 27" / Under 69 cm
        - 27–28" / 69–71 cm
        - 29–30" / 74–76 cm
        - 31–32" / 79–81 cm
        - 33–34" / 84–86 cm
        - 35–36" / 89–91 cm

        Each option maps to a fixed band size. You can then [upvote](/reference/quiz-builder/link-products/) every product variant with that band to the choice.

        ![measurement range dropdown question](/images/how_to_recommend_sizes_dropdown_ranges.png)

    Once you use finite answer choices, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants, or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the customer's selection

=== "Standalone"

    To make size recommendations work, **replace any measurement input with a dropdown or multiple-choice question**. Instead of asking for an exact number, offer predefined measurement ranges as answer choices.

    !!! example "Example - Bra Size Quiz"

        Instead of "Enter your underbust measurement", use a dropdown:

        - Under 27" / Under 69 cm
        - 27–28" / 69–71 cm
        - 29–30" / 74–76 cm
        - 31–32" / 79–81 cm
        - 33–34" / 84–86 cm
        - 35–36" / 89–91 cm

        Each option maps to a fixed band size. You can then [upvote](/reference/quiz-builder/link-products/) every product variant with that band to the choice.

        ![measurement range dropdown question](/images/how_to_recommend_sizes_dropdown_ranges.png)

    Once you use finite answer choices, you can:

    - [Upvote](/reference/quiz-builder/link-products/) specific products, variants, or collections to each choice
    - Set up [Jump Logic](/reference/quiz-builder/conditional-logic/#jump-logic) or [Display Logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic) based on the customer's selection


## Map out your products before you start

=== "Shopify"

    Every answer choice needs a pre-written list of product variants, so **you must know your full size catalog before building a single question**. The quiz engine assigns upvotes at setup time, not when a customer answers. You cannot assign products to an answer you have not defined yet.

    Before opening the quiz builder:

    1. List every size variant you carry (e.g. 28A, 28B … 44DD)
    2. Identify the attributes that determine size for your product. Bras use band and cup, clothing uses waist and hip, shoes use length and width.
    3. Design one question per attribute, with dropdown options covering the full range of your catalog
    4. For each answer option, write out which product variants it should upvote for

    !!! tip "Use an AI assistant to generate the mapping"

        If you carry many size variants, mapping them manually is tedious. Share your full product list with an AI assistant (like ChatGPT, Claude, or Gemini) and ask it to generate the mapping for you.

        Try a prompt like:

        > "I sell bras in these sizes: [paste your size list]. I have two quiz questions: underbust measurement and bust difference. For each dropdown option, list every product variant that should receive an upvote."

=== "Shopify (Legacy)"

    Every answer choice needs a pre-written list of product variants, so **you must know your full size catalogue before building a single question**. The quiz engine assigns upvotes at setup time, not when a customer answers. You cannot assign products to an answer you have not defined yet.

    Before opening the quiz builder:

    1. List every size variant you carry (e.g. 28A, 28B … 44DD)
    2. Identify the attributes that determine size for your product. Bras use band and cup, clothing uses waist and hip, shoes use length and width.
    3. Design one question per attribute, with dropdown options covering the full range of your catalogue
    4. For each answer option, write out which product variants it should upvote for

    !!! tip "Use an AI assistant to generate the mapping"

        If you carry many size variants, mapping them manually is tedious. Share your full product list with an AI assistant (like ChatGPT, Claude, or Gemini) and ask it to generate the mapping for you.

        Try a prompt like:

        > "I sell bras in these sizes: [paste your size list]. I have two quiz questions: underbust measurement and bust difference. For each dropdown option, list every product variant that should receive an upvote."

=== "WooCommerce"

    Every answer choice needs a pre-written list of product variants, so **you must know your full size catalogue before building a single question**. The quiz engine assigns upvotes at setup time, not when a customer answers. You cannot assign products to an answer you have not defined yet.

    Before opening the quiz builder:

    1. List every size variant you carry (e.g. 28A, 28B … 44DD)
    2. Identify the attributes that determine size for your product. Bras use band and cup, clothing uses waist and hip, shoes use length and width.
    3. Design one question per attribute, with dropdown options covering the full range of your catalogue
    4. For each answer option, write out which product variants it should upvote for

    !!! tip "Use an AI assistant to generate the mapping"

        If you carry many size variants, mapping them manually is tedious. Share your full product list with an AI assistant (like ChatGPT, Claude, or Gemini) and ask it to generate the mapping for you.

        Try a prompt like:

        > "I sell bras in these sizes: [paste your size list]. I have two quiz questions: underbust measurement and bust difference. For each dropdown option, list every product variant that should receive an upvote."

=== "Magento"

    Every answer choice needs a pre-written list of product variants, so **you must know your full size catalogue before building a single question**. The quiz engine assigns upvotes at setup time, not when a customer answers. You cannot assign products to an answer you have not defined yet.

    Before opening the quiz builder:

    1. List every size variant you carry (e.g. 28A, 28B … 44DD)
    2. Identify the attributes that determine size for your product. Bras use band and cup, clothing uses waist and hip, shoes use length and width.
    3. Design one question per attribute, with dropdown options covering the full range of your catalogue
    4. For each answer option, write out which product variants it should upvote for

    !!! tip "Use an AI assistant to generate the mapping"

        If you carry many size variants, mapping them manually is tedious. Share your full product list with an AI assistant and ask it to generate the mapping for you.

        Try a prompt like:

        > "I sell bras in these sizes: [paste your size list]. I have two quiz questions: underbust measurement and bust difference. For each dropdown option, list every product variant that should receive an upvote."

=== "BigCommerce"

    Every answer choice needs a pre-written list of product variants, so **you must know your full size catalogue before building a single question**. The quiz engine assigns upvotes at setup time, not when a customer answers. You cannot assign products to an answer you have not defined yet.

    Before opening the quiz builder:

    1. List every size variant you carry (e.g. 28A, 28B … 44DD)
    2. Identify the attributes that determine size for your product. Bras use band and cup, clothing uses waist and hip, shoes use length and width.
    3. Design one question per attribute, with dropdown options covering the full range of your catalogue
    4. For each answer option, write out which product variants it should upvote for

    !!! tip "Use an AI assistant to generate the mapping"

        If you carry many size variants, mapping them manually is tedious. Share your full product list with an AI assistant (like ChatGPT, Claude, or Gemini) and ask it to generate the mapping for you.

        Try a prompt like:

        > "I sell bras in these sizes: [paste your size list]. I have two quiz questions: underbust measurement and bust difference. For each dropdown option, list every product variant that should receive an upvote."

=== "Standalone"

    Every answer choice needs a pre-written list of product variants, so **you must know your full size catalogue before building a single question**. The quiz engine assigns upvotes at setup time, not when a customer answers. You cannot assign products to an answer you have not defined yet.

    Before opening the quiz builder:

    1. List every size variant you carry (e.g. 28A, 28B … 44DD)
    2. Identify the attributes that determine size for your product. Bras use band and cup, clothing uses waist and hip, shoes use length and width.
    3. Design one question per attribute, with dropdown options covering the full range of your catalogue
    4. For each answer option, write out which product variants it should upvote for

    !!! tip "Use an AI assistant to generate the mapping"

        If you carry many size variants, mapping them manually is tedious. Share your full product list with an AI assistant (like ChatGPT, Claude, or Gemini) and ask it to generate the mapping for you.

        Try a prompt like:

        > "I sell bras in these sizes: [paste your size list]. I have two quiz questions: underbust measurement and bust difference. For each dropdown option, list every product variant that should receive an upvote."


## Add a tiebreaker question

=== "Shopify"

    Two well-designed measurement questions will produce a clear winner in most cases, but not always. When a customer's measurements sit exactly at the boundary between two sizes, two products can end up with the same upvote count. Without a tiebreaker, the result is arbitrary.

    **A tiebreaker question must have two properties:**

    - Its answer is **independent** of every other question - it describes something about the customer that is true regardless of their measurements
    - Its product list is **fixed and absolute**: it never changes based on what the customer answered elsewhere

    !!! example "Example - Body Frame as a Tiebreaker"

        For a bra quiz, "How would you describe your overall body frame?" works well:

        - Petite / small frame → upvotes for all 28, 30, 32 band sizes
        - Average / medium frame → upvotes for all 32, 34, 36 band sizes
        - Athletic / muscular frame → upvotes for all 34, 36, 38 band sizes
        - Plus / fuller frame → upvotes for all 38, 40, 42, 44 band sizes

        These lists are written in advance and never change. The question is answerable without knowing anything about the customer's measurements.

    !!! warning "Avoid questions whose answers depend on other questions"

        A question like "Does your current bra band feel too tight?" seems useful. Acting on it, by adding an upvote to the next band size up, needs to know what the first question answered. That is logic, not a static list, and **it cannot exist in the upvoting system**. Any tiebreaker question must be answerable in isolation, with a product list that is the same for every customer who picks that option.

=== "Shopify (Legacy)"

    Two well-designed measurement questions will produce a clear winner in most cases, but not always. When a customer's measurements sit exactly at the boundary between two sizes, two products can end up with the same upvote count. Without a tiebreaker, the result is arbitrary.

    **A tiebreaker question must have two properties:**

    - Its answer is **independent** of every other question - it describes something about the customer that is true regardless of their measurements
    - Its product list is **fixed and absolute**: it never changes based on what the customer answered elsewhere

    !!! example "Example - Body Frame as a Tiebreaker"

        For a bra quiz, "How would you describe your overall body frame?" works well:

        - Petite / small frame → upvotes for all 28, 30, 32 band sizes
        - Average / medium frame → upvotes for all 32, 34, 36 band sizes
        - Athletic / muscular frame → upvotes for all 34, 36, 38 band sizes
        - Plus / fuller frame → upvotes for all 38, 40, 42, 44 band sizes

        These lists are written in advance and never change. The question is answerable without knowing anything about the customer's measurements.

    !!! warning "Avoid questions whose answers depend on other questions"

        A question like "Does your current bra band feel too tight?" seems useful. Acting on it, by adding an upvote to the next band size up, needs to know what the first question answered. That is logic, not a static list, and **it cannot exist in the upvoting system**. Any tiebreaker question must be answerable in isolation, with a product list that is the same for every customer who picks that option.

=== "WooCommerce"

    Two well-designed measurement questions will produce a clear winner in most cases, but not always. When a customer's measurements sit exactly at the boundary between two sizes, two products can end up with the same upvote count. Without a tiebreaker, the result is arbitrary.

    **A tiebreaker question must have two properties:**

    - Its answer is **independent** of every other question - it describes something about the customer that is true regardless of their measurements
    - Its product list is **fixed and absolute**: it never changes based on what the customer answered elsewhere

    !!! example "Example - Body Frame as a Tiebreaker"

        For a bra quiz, "How would you describe your overall body frame?" works well:

        - Petite / small frame → upvotes for all 28, 30, 32 band sizes
        - Average / medium frame → upvotes for all 32, 34, 36 band sizes
        - Athletic / muscular frame → upvotes for all 34, 36, 38 band sizes
        - Plus / fuller frame → upvotes for all 38, 40, 42, 44 band sizes

        These lists are written in advance and never change. The question is answerable without knowing anything about the customer's measurements.

    !!! warning "Avoid questions whose answers depend on other questions"

        A question like "Does your current bra band feel too tight?" seems useful. Acting on it, by adding an upvote to the next band size up, needs to know what the first question answered. That is logic, not a static list, and **it cannot exist in the upvoting system**. Any tiebreaker question must be answerable in isolation, with a product list that is the same for every customer who picks that option.

=== "Magento"

    Two well-designed measurement questions will produce a clear winner in most cases, but not always. When a customer's measurements sit exactly at the boundary between two sizes, two products can end up with the same upvote count. Without a tiebreaker, the result is arbitrary.

    **A tiebreaker question must have two properties:**

    - Its answer is **independent** of every other question - it describes something about the customer that is true regardless of their measurements
    - Its product list is **fixed and absolute**: it never changes based on what the customer answered elsewhere

    !!! example "Example - Body Frame as a Tiebreaker"

        For a bra quiz, "How would you describe your overall body frame?" works well:

        - Petite / small frame → upvotes for all 28, 30, 32 band sizes
        - Average / medium frame → upvotes for all 32, 34, 36 band sizes
        - Athletic / muscular frame → upvotes for all 34, 36, 38 band sizes
        - Plus / fuller frame → upvotes for all 38, 40, 42, 44 band sizes

        These lists are written in advance and never change. The question is answerable without knowing anything about the customer's measurements.

    !!! warning "Avoid questions whose answers depend on other questions"

        A question like "Does your current bra band feel too tight?" seems useful. Acting on it, by adding an upvote to the next band size up, needs to know what the first question answered. That is logic, not a static list, and **it cannot exist in the upvoting system**. Any tiebreaker question must be answerable in isolation, with a product list that is the same for every customer who picks that option.

=== "BigCommerce"

    Two well-designed measurement questions will produce a clear winner in most cases, but not always. When a customer's measurements sit exactly at the boundary between two sizes, two products can end up with the same upvote count. Without a tiebreaker, the result is arbitrary.

    **A tiebreaker question must have two properties:**

    - Its answer is **independent** of every other question - it describes something about the customer that is true regardless of their measurements
    - Its product list is **fixed and absolute**: it never changes based on what the customer answered elsewhere

    !!! example "Example - Body Frame as a Tiebreaker"

        For a bra quiz, "How would you describe your overall body frame?" works well:

        - Petite / small frame → upvotes for all 28, 30, 32 band sizes
        - Average / medium frame → upvotes for all 32, 34, 36 band sizes
        - Athletic / muscular frame → upvotes for all 34, 36, 38 band sizes
        - Plus / fuller frame → upvotes for all 38, 40, 42, 44 band sizes

        These lists are written in advance and never change. The question is answerable without knowing anything about the customer's measurements.

    !!! warning "Avoid questions whose answers depend on other questions"

        A question like "Does your current bra band feel too tight?" seems useful. Acting on it, by adding an upvote to the next band size up, needs to know what the first question answered. That is logic, not a static list, and **it cannot exist in the upvoting system**. Any tiebreaker question must be answerable in isolation, with a product list that is the same for every customer who picks that option.

=== "Standalone"

    Two well-designed measurement questions will produce a clear winner in most cases, but not always. When a customer's measurements sit exactly at the boundary between two sizes, two products can end up with the same upvote count. Without a tiebreaker, the result is arbitrary.

    **A tiebreaker question must have two properties:**

    - Its answer is **independent** of every other question - it describes something about the customer that is true regardless of their measurements
    - Its product list is **fixed and absolute**: it never changes based on what the customer answered elsewhere

    !!! example "Example - Body Frame as a Tiebreaker"

        For a bra quiz, "How would you describe your overall body frame?" works well:

        - Petite / small frame → upvotes for all 28, 30, 32 band sizes
        - Average / medium frame → upvotes for all 32, 34, 36 band sizes
        - Athletic / muscular frame → upvotes for all 34, 36, 38 band sizes
        - Plus / fuller frame → upvotes for all 38, 40, 42, 44 band sizes

        These lists are written in advance and never change. The question is answerable without knowing anything about the customer's measurements.

    !!! warning "Avoid questions whose answers depend on other questions"

        A question like "Does your current bra band feel too tight?" seems useful. Acting on it, by adding an upvote to the next band size up, needs to know what the first question answered. That is logic, not a static list, and **it cannot exist in the upvoting system**. Any tiebreaker question must be answerable in isolation, with a product list that is the same for every customer who picks that option.


## Alternative: custom JavaScript calculation

=== "Shopify"

    The upvoting approach may not be precise enough when your sizing logic needs exact measurement formulas. Use [Custom JavaScript](/how-to-guides/add-javascript/) to calculate the result on the results page instead.

    JavaScript can take typed measurements from a [Number](/reference/quiz-builder/questions/#number) question, apply any formula or condition, and show a calculated result. That includes a recommended product, with no upvotes involved.

    !!! info "Custom JavaScript is available on paid plans only"

        The [Custom JavaScript](/how-to-guides/add-javascript/) feature is not available on the free plan. If you are on a free plan, the upvoting approach with measurement ranges described in this article is the recommended method.

        [View pricing and plans →](https://revenuehunt.com/pricing/)

    ??? tip "Already on a paid plan? Copilot can write the code for you"

        If your product size mapping is ready, you do not need to write the JavaScript yourself. Open Quiz Copilot from the quiz editor and share your product list and sizing logic. Ask it to generate a JavaScript block that takes the customer's measurement inputs and returns the correct size recommendation.

        Copilot will produce ready-to-paste code. You can ask it to handle edge cases, out-of-stock fallbacks, or sister size suggestions, all in plain language.

    See the [Custom JavaScript guide](/how-to-guides/add-javascript/) for full documentation, including a worked example of a calculation-based result.

=== "Shopify (Legacy)"

    The upvoting approach may not be precise enough when your sizing logic needs exact measurement formulas. Use [Custom JavaScript](/how-to-guides/add-javascript/) to calculate the result on the results page instead.

    JavaScript can take typed measurements from a [Number](/reference/quiz-builder/questions/#number) question, apply any formula or condition, and show a calculated result. That includes a recommended product, with no upvotes involved.


    See the [Custom JavaScript guide](/how-to-guides/add-javascript/) for full documentation, including a worked example of a calculation-based result.

=== "WooCommerce"

    The upvoting approach may not be precise enough when your sizing logic needs exact measurement formulas. Use [Custom JavaScript](/how-to-guides/add-javascript/) to calculate the result on the results page instead.

    JavaScript can take typed measurements from a [Number](/reference/quiz-builder/questions/#number) question, apply any formula or condition, and show a calculated result. That includes a recommended product, with no upvotes involved.

    See the [Custom JavaScript guide](/how-to-guides/add-javascript/) for full documentation, including a worked example of a calculation-based result.

=== "Magento"

    The upvoting approach may not be precise enough when your sizing logic needs exact measurement formulas. Use [Custom JavaScript](/how-to-guides/add-javascript/) to calculate the result on the results page instead.

    JavaScript can take typed measurements from a [Number](/reference/quiz-builder/questions/#number) question, apply any formula or condition, and show a calculated result. That includes a recommended product, with no upvotes involved.


    See the [Custom JavaScript guide](/how-to-guides/add-javascript/) for full documentation, including a worked example of a calculation-based result.

=== "BigCommerce"

    The upvoting approach may not be precise enough when your sizing logic needs exact measurement formulas. Use [Custom JavaScript](/how-to-guides/add-javascript/) to calculate the result on the results page instead.

    JavaScript can take typed measurements from a [Number](/reference/quiz-builder/questions/#number) question, apply any formula or condition, and show a calculated result. That includes a recommended product, with no upvotes involved.

    See the [Custom JavaScript guide](/how-to-guides/add-javascript/) for full documentation, including a worked example of a calculation-based result.

=== "Standalone"

    The upvoting approach may not be precise enough when your sizing logic needs exact measurement formulas. Use [Custom JavaScript](/how-to-guides/add-javascript/) to calculate the result on the results page instead.

    JavaScript can take typed measurements from a [Number](/reference/quiz-builder/questions/#number) question, apply any formula or condition, and show a calculated result. That includes a recommended product, with no upvotes involved.

    See the [Custom JavaScript guide](/how-to-guides/add-javascript/) for full documentation, including a worked example of a calculation-based result.

---

This article explains how to recommend sizes based on measurements using the quiz upvoting system.
