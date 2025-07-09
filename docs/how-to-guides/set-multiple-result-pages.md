---
icon: material/file-document-multiple
---

# How to Set Up Multiple Result Pages

With the RevenueHunt app it is possible to set up Multiple Results Pages. To add an extra Results Page to your quiz follow the instructions below.

!!! warning

    Adding multiple results pages increases complexity, may lead to unexpected product recommendations, and can impact quiz loading speed. **For maximum conversions and sales, we recommend using only one results page.**

    However, multiple results pages can be beneficial in certain scenarios:

    - Personalized discounts: Show different discounts (or no discount) based on customer preferences or responses.
    - Email collection strategies: Offer unique results based on whether the customer leaves their email address or not.
    - Simplifying conditional logic: If you have a long list of similar conditional blocks, using multiple results pages can make it easier to organize and manage logic by giving each page a clear name.
    - Special cases: Some businesses, like medical & supplements companies, might use separate results pages to inform customers when they are not eligible for certain products, e.g., "You're not qualified for X due to [specific reason]."

    Carefully consider your quiz goals before enabling this feature to ensure it aligns with your business objectives.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).
    3. Under [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the results page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](/reference/quiz-builder/conditional-logic/) tab in your Quiz Builder. 

        ![how_to_legacy_multiple_result_pages_jumplogic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different results pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.

=== "Shopify V2"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/7851abaea4964d51bc41d0738281da9d?sid=7ef0fec7-3d95-46b9-b64a-949a82d66322" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Go to the [Results Page](/reference/quiz-builder/results-page/) tab.
    3. Scroll down and click `+ Add results page`. A second results page will appear below the first.

        ![multi result pages shopify v2 activate multi results page](/images/how_to_multi_result_pages_shopify_v2_activate_multi_results_page.png)
    4. Once you've added your result pages **you'll need to add [**Jump Logic**](/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](/reference/quiz-builder/conditional-logic/) tab in your Quiz Builder. 

        ![how_to_shopifyV2_multiple_result_pages_jumplogic](/images/how_to_shopifyV2_multiple_result_pages_jumplogic.png)
    5. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/how_to_multi_result_pages_shopify_v2_jump_logic_multi_results_page.png)

        To learn more about using Jump Logic, check [this handy guide](/how-to-guides/use-jump-logic/).

    6. Once Jump Logic is set up and leading the customers to different results pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).
    3. Under [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the results page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](/reference/quiz-builder/conditional-logic/) tab in your Quiz Builder. 
    
        ![how_to_legacy_multiple_result_pages_jumplogic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different results pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).
    3. Under [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the results page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](/reference/quiz-builder/conditional-logic/) tab in your Quiz Builder. 

        ![how_to_legacy_multiple_result_pages_jumplogic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different results pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).
    3. Under [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the results page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](/reference/quiz-builder/conditional-logic/) tab in your Quiz Builder. 

        ![how_to_legacy_multiple_result_pages_jumplogic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different results pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/af13990661614b4eb7e2964989d1d1e7?sid=5deeb33c-eb7e-412b-8903-f403d5a5cb81" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. Open the [Quiz Builder](/reference/quiz-builder/).
    2. Go to the [Results Page](/reference/quiz-builder/results-page/) tab and open the [Results Page Settings](/reference/quiz-builder/results-page/).
    3. Under [Advanced](/reference/quiz-builder/results-page/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the results page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](/reference/quiz-builder/conditional-logic/) tab in your Quiz Builder. 

        ![how_to_legacy_multiple_result_pages_jumplogic](/images/how_to_legacy_multiple_result_pages_jumplogic.png)
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different results pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.

---
This article explains how to set up multiple results pages in the RevenueHunt app.