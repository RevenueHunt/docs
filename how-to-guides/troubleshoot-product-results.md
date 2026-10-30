---
icon: material/printer-pos-wrench
description: "Step-by-step guide to troubleshoot RevenueHunt product recommendation issues in your quiz."
---

# How to Troubleshoot Product Recommendations in Your Quiz

A single quiz response records every choice the customer made and every product those choices upvoted. Reading one tells you why a product was recommended, or why it never appeared.

!!! info "What decides a recommendation"

    Products reach the results page through the [upvoting system](/how-to-guides/set-up-funnel-quiz/#upvoting-system), and blocks are shown or hidden by [display logic](/reference/quiz-builder/results-page/#display-logic-display-section-logic). A missing product is nearly always one of those two.

## Check why a product was recommended

!!! tip "Open the responses in a second window"

    Keep the [Responses section](/reference/quiz-builder/metrics/#responses) of the [App manual](/reference/) open alongside your quiz while you work through this.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/5RFclBk7-LA?si=YwBMN6n0c87QrZRZ" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Responses](/reference/quiz-builder/metrics/#responses) section.** Go to the [dashboard](/reference/quiz-builder/), pick a quiz, click `...`, then click `Responses`.

        ![manual_shopifyV2_quizbuilder_openresponses](/images/manual_shopifyV2_quizbuilder_openresponses.png)

    2. **Click a date to open that response.** The list holds the latest responses, newest first.

        ![manual_shopifyV2_quizbuilder_responses](/images/manual_shopifyV2_quizbuilder_responses.png)

        !!! note "Test responses leave the list after an hour"

            Responses from the admin and from quiz previews are removed automatically, so they never count towards your plan limit.

    3. **Click `Analyze response` to open [Quiz Copilot](/how-to-guides/use-quiz-copilot/).** Ask it anything about the response. It reads the answers, names the likely cause, and suggests what to change.

    4. **Open the `Why was a product recommended or not in this response?` section.**

        ![manual_shopifyV2_quizbuilder_responses_sample1](/images/manual_shopifyV2_quizbuilder_responses_sample1.png)

    5. **Decide which product to explain.** Either one that appeared and should not have, or one you expected and did not get.

    6. **Search for it in `SELECT PRODUCT TO CHECK` and select it from the results.** The color tells you where it stands.

        | Color | What it means |
        |---|---|
        | **Green** | The product received upvotes from the quiz choices. |
        | **Red** | The product was excluded from the recommendations. |
        | **White** | The product received no upvotes, so it could not be recommended. |

    7. **Read the panel that opens.**

        ![how to troubleshoot quiz results search products](/images/manual_shopifyV2_quizbuilder_responses_sample1_checkproduct.png)

        The panel shows:

        - The collections or categories the product belongs to.
        - How many upvotes it received, and why it was recommended or left out.
        - The questions and choices that drove those upvotes, including the collections or categories that upvoted or excluded it.
        - The results page, slot or product block that placed it.

    The color and the panel together tell you what happened. Either the product sits in the wrong group, or a choice you had forgotten about excluded it.

    !!! tip "The two usual causes"

        A product is normally in the wrong collection or category, or it was excluded somewhere in the quiz settings. Both are easy to miss and easy to fix.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Go to [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.**

    2. **Open the [Responses](/reference/quiz-builder/metrics/#responses) tab.** The left-hand menu holds the last 100 responses, by date.

    3. **Click a date to open that response.**

    4. **Open the `Why was a product recommended or not in this response?` section.**

    5. **Open the Results Page for that response.** The link sits at the bottom of the response details.

        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)

    6. **Decide which product to explain.** Either one that appeared and should not have, or one you expected and did not get.

    7. **Search for it in `SELECT PRODUCT TO CHECK` and select it from the results.** The section sits at the top of the response, and the color tells you where the product stands.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        | Color | What it means |
        |---|---|
        | **Green** | The product received upvotes from the quiz choices. |
        | **Red** | The product was excluded from the recommendations. |
        | **White** | The product received no upvotes, so it could not be recommended. |

    8. **Read the panel that opens.**

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        The panel shows:

        - The collections or categories the product belongs to.
        - How many upvotes it received, and why it was recommended or left out.
        - The questions and choices that drove those upvotes, including the collections or categories that upvoted or excluded it.
        - The results page, slot or product block that placed it.

    The color and the panel together tell you what happened. Either the product sits in the wrong group, or a choice you had forgotten about excluded it.

    !!! tip "The two usual causes"

        A product is normally in the wrong collection or category, or it was excluded somewhere in the quiz settings. Both are easy to miss and easy to fix.

    Two more actions are worth knowing about:

    - **Recalculate Recommendations.** Once you have changed the quiz, or the collections and categories behind it, this replays the response against the new setup.
    - **Resend Notifications.** This sends the revised recommendations out again, to your CRM or by email.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Go to [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.**

    2. **Open the [Responses](/reference/quiz-builder/metrics/#responses) tab.** The left-hand menu holds the last 100 responses, by date.

    3. **Click a date to open that response.**

    4. **Open the `Why was a product recommended or not in this response?` section.**

    5. **Open the Results Page for that response.** The link sits at the bottom of the response details.

        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)

    6. **Decide which product to explain.** Either one that appeared and should not have, or one you expected and did not get.

    7. **Search for it in `SELECT PRODUCT TO CHECK` and select it from the results.** The section sits at the top of the response, and the color tells you where the product stands.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        | Color | What it means |
        |---|---|
        | **Green** | The product received upvotes from the quiz choices. |
        | **Red** | The product was excluded from the recommendations. |
        | **White** | The product received no upvotes, so it could not be recommended. |

    8. **Read the panel that opens.**

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        The panel shows:

        - The collections or categories the product belongs to.
        - How many upvotes it received, and why it was recommended or left out.
        - The questions and choices that drove those upvotes, including the collections or categories that upvoted or excluded it.
        - The results page, slot or product block that placed it.

    The color and the panel together tell you what happened. Either the product sits in the wrong group, or a choice you had forgotten about excluded it.

    !!! tip "The two usual causes"

        A product is normally in the wrong collection or category, or it was excluded somewhere in the quiz settings. Both are easy to miss and easy to fix.

    Two more actions are worth knowing about:

    - **Recalculate Recommendations.** Once you have changed the quiz, or the collections and categories behind it, this replays the response against the new setup.
    - **Resend Notifications.** This sends the revised recommendations out again, to your CRM or by email.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Go to [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.**

    2. **Open the [Responses](/reference/quiz-builder/metrics/#responses) tab.** The left-hand menu holds the last 100 responses, by date.

    3. **Click a date to open that response.**

    4. **Open the `Why was a product recommended or not in this response?` section.**

    5. **Open the Results Page for that response.** The link sits at the bottom of the response details.

        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)

    6. **Decide which product to explain.** Either one that appeared and should not have, or one you expected and did not get.

    7. **Search for it in `SELECT PRODUCT TO CHECK` and select it from the results.** The section sits at the top of the response, and the color tells you where the product stands.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        | Color | What it means |
        |---|---|
        | **Green** | The product received upvotes from the quiz choices. |
        | **Red** | The product was excluded from the recommendations. |
        | **White** | The product received no upvotes, so it could not be recommended. |

    8. **Read the panel that opens.**

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        The panel shows:

        - The collections or categories the product belongs to.
        - How many upvotes it received, and why it was recommended or left out.
        - The questions and choices that drove those upvotes, including the collections or categories that upvoted or excluded it.
        - The results page, slot or product block that placed it.

    The color and the panel together tell you what happened. Either the product sits in the wrong group, or a choice you had forgotten about excluded it.

    !!! tip "The two usual causes"

        A product is normally in the wrong collection or category, or it was excluded somewhere in the quiz settings. Both are easy to miss and easy to fix.

    Two more actions are worth knowing about:

    - **Recalculate Recommendations.** Once you have changed the quiz, or the collections and categories behind it, this replays the response against the new setup.
    - **Resend Notifications.** This sends the revised recommendations out again, to your CRM or by email.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Go to [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.**

    2. **Open the [Responses](/reference/quiz-builder/metrics/#responses) tab.** The left-hand menu holds the last 100 responses, by date.

    3. **Click a date to open that response.**

    4. **Open the `Why was a product recommended or not in this response?` section.**

    5. **Open the Results Page for that response.** The link sits at the bottom of the response details.

        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)

    6. **Decide which product to explain.** Either one that appeared and should not have, or one you expected and did not get.

    7. **Search for it in `SELECT PRODUCT TO CHECK` and select it from the results.** The section sits at the top of the response, and the color tells you where the product stands.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        | Color | What it means |
        |---|---|
        | **Green** | The product received upvotes from the quiz choices. |
        | **Red** | The product was excluded from the recommendations. |
        | **White** | The product received no upvotes, so it could not be recommended. |

    8. **Read the panel that opens.**

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        The panel shows:

        - The collections or categories the product belongs to.
        - How many upvotes it received, and why it was recommended or left out.
        - The questions and choices that drove those upvotes, including the collections or categories that upvoted or excluded it.
        - The results page, slot or product block that placed it.

    The color and the panel together tell you what happened. Either the product sits in the wrong group, or a choice you had forgotten about excluded it.

    !!! tip "The two usual causes"

        A product is normally in the wrong collection or category, or it was excluded somewhere in the quiz settings. Both are easy to miss and easy to fix.

    Two more actions are worth knowing about:

    - **Recalculate Recommendations.** Once you have changed the quiz, or the collections and categories behind it, this replays the response against the new setup.
    - **Resend Notifications.** This sends the revised recommendations out again, to your CRM or by email.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/35a595634ca5404d922c725590e96c89?sid=ca0b9ad7-eea5-43b1-9597-6dfa9aee4a2b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Go to [Metrics](/reference/quiz-builder/metrics/) in the Quiz Builder.**

    2. **Open the [Responses](/reference/quiz-builder/metrics/#responses) tab.** The left-hand menu holds the last 100 responses, by date.

    3. **Click a date to open that response.**

    4. **Open the `Why was a product recommended or not in this response?` section.**

    5. **Open the Results Page for that response.** The link sits at the bottom of the response details.

        ![how to troubleshoot quiz results preview results](/images/how_to_troubleshoot_quiz_results_preview_results.gif)

    6. **Decide which product to explain.** Either one that appeared and should not have, or one you expected and did not get.

    7. **Search for it in `SELECT PRODUCT TO CHECK` and select it from the results.** The section sits at the top of the response, and the color tells you where the product stands.

        ![how to troubleshoot quiz results search products](/images/how_to_troubleshoot_quiz_results_search_products.gif)

        | Color | What it means |
        |---|---|
        | **Green** | The product received upvotes from the quiz choices. |
        | **Red** | The product was excluded from the recommendations. |
        | **White** | The product received no upvotes, so it could not be recommended. |

    8. **Read the panel that opens.**

        ![how to troubleshoot quiz results information](/images/how_to_troubleshoot_quiz_results_information.gif)

        The panel shows:

        - The collections or categories the product belongs to.
        - How many upvotes it received, and why it was recommended or left out.
        - The questions and choices that drove those upvotes, including the collections or categories that upvoted or excluded it.
        - The results page, slot or product block that placed it.

    The color and the panel together tell you what happened. Either the product sits in the wrong group, or a choice you had forgotten about excluded it.

    !!! tip "The two usual causes"

        A product is normally in the wrong collection or category, or it was excluded somewhere in the quiz settings. Both are easy to miss and easy to fix.

    Two more actions are worth knowing about:

    - **Recalculate Recommendations.** Once you have changed the quiz, or the collections and categories behind it, this replays the response against the new setup.
    - **Resend Notifications.** This sends the revised recommendations out again, to your CRM or by email.

---

This article explains how to read a quiz response, and work out why a product was recommended or missing.