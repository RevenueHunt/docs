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

    1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
    2. Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and open the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    3. Under [Advanced](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](https://docs.revenuehunt.com/reference/quiz-builder/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the resutls page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab in your Quiz Builder. 
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different resutls pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.



=== "Shopify V2"

    1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
    2. Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab.
    3. Scroll down and click `+ Add results page`. A second results page will appear below the first.

        ![multi result pages shopify v2 activate multi results page](/images/how to multi result pages shopify v2 activate multi results page.png)
    4. Once you've added your result pages **you'll need to add [**Jump Logic**](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab in your Quiz Builder. 
    5. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/how to multi result pages shopify v2 jump logic multi results page.png)

        To learn more about using Jump Logic, check [this handy guide](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/).

    6. Once Jump Logic is set up and leading the customers to different resutls pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.


=== "WooCommerce"

    1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
    2. Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and open the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    3. Under [Advanced](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](https://docs.revenuehunt.com/reference/quiz-builder/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the resutls page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab in your Quiz Builder. 
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different resutls pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.


=== "Magento"

    1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
    2. Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and open the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    3. Under [Advanced](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](https://docs.revenuehunt.com/reference/quiz-builder/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the resutls page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab in your Quiz Builder. 
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different resutls pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.


=== "BigCommerce"

    1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
    2. Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and open the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    3. Under [Advanced](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](https://docs.revenuehunt.com/reference/quiz-builder/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the resutls page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab in your Quiz Builder. 
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different resutls pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.


=== "Standalone"

    1. Open the [Quiz Builder](https://docs.revenuehunt.com/reference/quiz-builder/).
    2. Go to the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) tab and open the [Results Page Settings](https://docs.revenuehunt.com/reference/quiz-builder/#results-page-settings).
    3. Under [Advanced](https://docs.revenuehunt.com/reference/quiz-builder/#advanced-settings) tab scroll down to **Multiple Results Pages** and click `activate`. 
    4. A new tab called [`MULTIPLE RESULTS PAGES`](https://docs.revenuehunt.com/reference/quiz-builder/#multiple-results-pages-settings) will appear. Click on it to open the Multiple Results Pages menu.
    5. In the menu, you will see all the results pages created in this quiz.

        ![manual_quizbuilder_resultspage_settings_multipleresultspages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="500"}

    6. The default results page will be `Results Page 1`. It will be marked with `This is currently the default Results Page` text. You can click and edit this text to rename the resutls page for easier identification.
    7. To create an additional result page click the `Create new Results Page` button.
    8. A second results page will appear. To set this results page as the new default, click the `set` button. To edit the contents of this reuslts page click `edit`. The quiz builder will switch to this results page and you will be able to set up different settings for each of your results page such as discounts, contents, product blocks or settings.
    9. Once you've added your result pages **you'll need to add [**Jump Logic**](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/) to your quiz in order to redirect users to the correct results page**. Go to the [Conditonal Logic](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) tab in your Quiz Builder. 
    10. Scroll down the list of questtion and find the last question before the results. Open the question and add Jump Logic rules that will redirect the user to a specific results page. 
    
        ![manual_quizbuilder_conditionallogic_jumplogicrule_goto](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png){width="500"}

        To learn more about using Jump Logic, check [this handy guide](https://docs.revenuehunt.com/how-to-guides/use-jump-logic/).

    11. Once Jump Logic is set up and leading the customers to different resutls pages, publish the changes with the top-right `Publish` button to updated the preview/live quiz.


