---
icon: material/file-document-multiple
description: "Learn how to set up multiple results pages in RevenueHunt to show personalized content."
---

# How to Set Up Multiple Results Pages

A quiz can show more than one results page, with different content on each. Follow the instructions below to add one.

!!! warning

    A second results page adds complexity, can produce unexpected product recommendations, and slows the quiz down. **One results page sells best.**

    A second page is worth adding in a few cases:

    - Personalized discounts: Show different discounts (or no discount) based on customer preferences or responses.
    - Email collection strategies: Offer unique results based on whether the customer leaves their email address or not.
    - Simpler conditional logic: a long list of similar conditional blocks is easier to manage as several named pages.
    - Special cases: a medical or supplements company may need a page telling the customer they are not eligible for a product, and why.

    Weigh that against your quiz goals before you turn this on.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/CBQctZEPHfA?si=WEZfhN4Mkn0f0Nfg" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz builder](/reference/quiz-builder/).**
    2. **Go to the [Results page](/reference/quiz-builder/results-page/) tab.**
    3. **Scroll down and click `+ Add results page`.** A second page appears below the first.

        ![The Add results page button on the results page tab](/images/how_to_multi_result_pages_shopify_v2_activate_multi_results_page.png)
    4. **Open the [Conditional logic](/reference/quiz-builder/conditional-logic/) tab.** Extra pages do nothing on their own. [Jump logic](/how-to-guides/use-jump-logic/) is what sends each customer to the right one.

        ![The Conditional logic tab in the quiz builder](/images/how_to_shopifyV2_multiple_result_pages_jumplogic.png)
    5. **Find the last question before the results, and add Jump logic rules there.** Each rule sends the customer to a particular results page.

        ![Adding a Jump logic rule that points at a results page](/images/how_to_multi_result_pages_shopify_v2_jump_logic_multi_results_page.png)

        [How to use jump logic](/how-to-guides/use-jump-logic/) covers the rules in full.

    6. **Click the top-right `Save` button** to update the preview and the live quiz.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).**
    3. **On the [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab, scroll to `Multiple Results Pages` and click `activate`.**
    4. **Click the new [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) tab.** The menu lists every results page in this quiz.

        ![The Multiple Results Pages menu](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    5. **Click `This is currently the default Results Page` to rename `Results Page 1`.** That page is the default until you change it.
    6. **Click `Create new Results Page` to add another.**
    7. **Click `set` to make the new page the default, or `edit` to change its contents.** The quiz builder switches to that page, where you set its own discounts, content, product blocks and settings.
    8. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.** Extra pages do nothing on their own. [Jump Logic](/how-to-guides/use-jump-logic/) is what sends each customer to the right one.

        ![The Conditional Logic tab in the quiz builder](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    9. **Find the last question before the results, and add Jump Logic rules there.** Each rule sends the customer to a particular results page.

        ![A Jump Logic rule pointing at a results page](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        [How to use jump logic](/how-to-guides/use-jump-logic/) covers the rules in full.

    10. **Click the top-right `Publish` button** to update the preview and the live quiz.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).**
    3. **On the [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab, scroll to `Multiple Results Pages` and click `activate`.**
    4. **Click the new [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) tab.** The menu lists every results page in this quiz.

        ![The Multiple Results Pages menu](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    5. **Click `This is currently the default Results Page` to rename `Results Page 1`.** That page is the default until you change it.
    6. **Click `Create new Results Page` to add another.**
    7. **Click `set` to make the new page the default, or `edit` to change its contents.** The quiz builder switches to that page, where you set its own discounts, content, product blocks and settings.
    8. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.** Extra pages do nothing on their own. [Jump Logic](/how-to-guides/use-jump-logic/) is what sends each customer to the right one.

        ![The Conditional Logic tab in the quiz builder](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    9. **Find the last question before the results, and add Jump Logic rules there.** Each rule sends the customer to a particular results page.

        ![A Jump Logic rule pointing at a results page](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        [How to use jump logic](/how-to-guides/use-jump-logic/) covers the rules in full.

    10. **Click the top-right `Publish` button** to update the preview and the live quiz.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).**
    3. **On the [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab, scroll to `Multiple Results Pages` and click `activate`.**
    4. **Click the new [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) tab.** The menu lists every results page in this quiz.

        ![The Multiple Results Pages menu](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    5. **Click `This is currently the default Results Page` to rename `Results Page 1`.** That page is the default until you change it.
    6. **Click `Create new Results Page` to add another.**
    7. **Click `set` to make the new page the default, or `edit` to change its contents.** The quiz builder switches to that page, where you set its own discounts, content, product blocks and settings.
    8. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.** Extra pages do nothing on their own. [Jump Logic](/how-to-guides/use-jump-logic/) is what sends each customer to the right one.

        ![The Conditional Logic tab in the quiz builder](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    9. **Find the last question before the results, and add Jump Logic rules there.** Each rule sends the customer to a particular results page.

        ![A Jump Logic rule pointing at a results page](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        [How to use jump logic](/how-to-guides/use-jump-logic/) covers the rules in full.

    10. **Click the top-right `Publish` button** to update the preview and the live quiz.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).**
    3. **On the [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab, scroll to `Multiple Results Pages` and click `activate`.**
    4. **Click the new [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) tab.** The menu lists every results page in this quiz.

        ![The Multiple Results Pages menu](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    5. **Click `This is currently the default Results Page` to rename `Results Page 1`.** That page is the default until you change it.
    6. **Click `Create new Results Page` to add another.**
    7. **Click `set` to make the new page the default, or `edit` to change its contents.** The quiz builder switches to that page, where you set its own discounts, content, product blocks and settings.
    8. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.** Extra pages do nothing on their own. [Jump Logic](/how-to-guides/use-jump-logic/) is what sends each customer to the right one.

        ![The Conditional Logic tab in the quiz builder](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    9. **Find the last question before the results, and add Jump Logic rules there.** Each rule sends the customer to a particular results page.

        ![A Jump Logic rule pointing at a results page](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        [How to use jump logic](/how-to-guides/use-jump-logic/) covers the rules in full.

    10. **Click the top-right `Publish` button** to update the preview and the live quiz.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**
    2. **Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).**
    3. **On the [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab, scroll to `Multiple Results Pages` and click `activate`.**
    4. **Click the new [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) tab.** The menu lists every results page in this quiz.

        ![The Multiple Results Pages menu](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    5. **Click `This is currently the default Results Page` to rename `Results Page 1`.** That page is the default until you change it.
    6. **Click `Create new Results Page` to add another.**
    7. **Click `set` to make the new page the default, or `edit` to change its contents.** The quiz builder switches to that page, where you set its own discounts, content, product blocks and settings.
    8. **Open the [Conditional Logic](/reference/quiz-builder/conditional-logic/) tab.** Extra pages do nothing on their own. [Jump Logic](/how-to-guides/use-jump-logic/) is what sends each customer to the right one.

        ![The Conditional Logic tab in the quiz builder](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    9. **Find the last question before the results, and add Jump Logic rules there.** Each rule sends the customer to a particular results page.

        ![A Jump Logic rule pointing at a results page](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        [How to use jump logic](/how-to-guides/use-jump-logic/) covers the rules in full.

    10. **Click the top-right `Publish` button** to update the preview and the live quiz.

---
This article explains how to set up multiple results pages in the RevenueHunt app.