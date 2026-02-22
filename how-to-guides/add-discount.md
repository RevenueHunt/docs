---
icon: material/sale
---

# How to Add a Discount to Your Quiz


=== "Shopify"

    With the Built for Shopify version of the RevenueHunt app, it is possible to:
    
    - **add your Shopify discount code** to be applied automatically at checkout,
    - **add a discount code as text** to quiz questions or results page,
    - **add the discount code to the [result emails](/reference/quiz-builder/notifications/#to-respondent)**.

    If you have a discount applied to certain products in your store via Shopify Products, these reduced prices will be reflected in the quiz results page automatically. Otherwise, the discount code will be applied automatically at checkout and *reduced prices will be visible at checkout stage only*.



=== "Shopify (Legacy)"

    Adding discount coupons into your quiz allows customers to enjoy special offers on the results page or through a follow-up email. 

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.
    
    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "WooCommerce"

    Adding discount coupons into your quiz allows customers to enjoy special offers on the results page or through a follow-up email. 

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    
    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "Magento"

    Adding discount coupons into your quiz allows customers to enjoy special offers on the results page or through a follow-up email. 

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "BigCommerce"

    Adding discount coupons into your quiz allows customers to enjoy special offers on the results page or through a follow-up email. 

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "Standalone"

    Adding discount coupons into your quiz allows customers to enjoy special offers on the results page or through a follow-up email. 

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

## Set Up Discount on the Results Page

=== "Shopify"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/F8rN6jOveOw?si=zZyYtDmydJoeqrg-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ### Automatic Discount Code

    You can add a discount code to be applied automatically at checkout when users finish the quiz and proceed to cart.

    !!! warning "Create a Discount Code in Shopify"

        You need to create a discount code in Shopify first before adding it to the quiz results page.

    1. **Create a Discount Code in Shopify**: You need to create a discount code in Shopify first before adding it to the quiz results page.

        - Navigate to the Shopify admin panel and select the `Discounts` tab.
        - Click on `Create Discount` to set up a new discount code.
        - Choose the type of discount (e.g., percentage, fixed amount). Enter a discount code name (e.g., `quiz123`) or specify the discount amount (e.g., 20%).
        - Select applicable products from your catalog.
        - Save the discount settings and copy the discount code.

        ![how to add discount in shopify](https://loom.com/i/f7b4f7a482ea4dab8c0b23370bce4c68?workflows_screenshot=true)

    2. **Configuring the Discount Code in Quiz Results Page**: You need to configure the discount code in the quiz results page before it can be applied automatically at checkout.

        - Open the RevenueHunt Quizzes app and open your quiz by clicking `Customize`.
        - Navigate to the ['Results page > Results page settings'](/reference/quiz-builder/results-page/#results-page-settings) by clicking on the Results page name.

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings.png)

        - Scroll to the `Discount code` settings section.

            ![manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings_discountcode](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings_discountcode.png)
        - Paste the copied discount code from Shopify into the designated field.

        ![how to add discount automatic](https://loom.com/i/7ae5a8e6a81e4836a0c4c8e7fa9bd66f?workflows_screenshot=true)

        - Save the changes with the top-right `Save` button to apply the discount code to the quiz results.

    3. **Testing the Discount Code**: Test the live quiz to ensure the discount code is applied correctly at checkout.

        - After setting up the discount code, visit your website and take a sample quiz.
        - Proceed to the cart and then to checkout.
        - Verify that the discount code `quiz123` is automatically applied to eligible products in the cart.

        ![how to add discount automatic checkout](https://loom.com/i/79773fc2fa9241dab298e8de28aa1b35?workflows_screenshot=true)

        !!! warning "Discount Code only works on live quiz"
        
            The discount code will be applied automatically at checkout only. The discount will not be visible on quiz preview.

    ### Discount Code as Text

    You can add a discount code as text within a [text block](/reference/quiz-builder/results-page/#text) on the quiz Results page. Users will be able to copy and paste the discount code at checkout.

    1. Open the [Results Page](/reference/quiz-builder/results-page/).
    2. Click on `Add block`.
    3. Select `Text` block.
    4. Add the discount code to the text field.
    5. Save the changes with the top-right `Save` button.

    ![how to add discount text block](/images/how_to_shopifyv2_add_discount_as_text.png)


    ### Discount Code with JavaScript

    !!! tip "Check JavaScript guide"

        Check this article to learn how to add custom JavaScript to the results page: [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

    You can use JavaScript to add a discount code to the results page.

    1. Open the [Results Page](/reference/quiz-builder/results-page/).
    2. Open the Results Page settings.
    3. Scroll down to the `Custom JavaScript` section.
    4. Ask your developer to use the `await Quiz.applyDiscountCode()` function to apply the discount code to the Custom JavaScript block. 

        !!! tip "Get help with custom JavaScript"

            Click on `✨Get help with custom JavaScript` to open a chat window with the Quiz Copilot AI. It can directly write JavaScript code for you.

    5. Save the changes with the top-right `Save` button.
    

    !!! info "Products Discounted in Shopify Products"
    
        If you have a discount applied to certain products in your store, these reduced prices will be reflected in the quiz results page automatically.


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/36ed1600df294287bf24d94bc438d4c3?sid=7c53ed8e-ab4c-4276-88bd-0509cdf954b9" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Step 1: Generate a Discount Code**

    To create a Shopify discount code, refer to [this helpful guide](https://help.shopify.com/en/manual/discounts/create-discount-codes#create-a-fixed-value-or-percentage-discount). Activation of this code is necessary before integrating it with your quiz to ensure functionality at checkout. 

    It's essential to select the `manual` option for discount codes in Shopify, as our app can only synchronize with manually created codes.

    !!! note

        Please remember, that the management of these discounts is handled through Shopify, not directly within our app.

    **Step 2: Configure Your Discount Code on the Results Page**

    You can add Static or Dynamic discount codes to your quiz.

    **Static Discount**

    1. Navigate to [Results Page Settings > Discount Settings](/reference/quiz-builder/results-page/#discounts-settings) and access the Discount Code Settings section. 
    2. Here, you'll find a `Code` field. This field is for entering the discount code that will be automatically applied at checkout.

        ![how to add discount static](/images/manual_quizbuilder_resultspage_settings_discount_discountcode.png){width="300"}

        `Visible discount` - Select the `discount %` from the dropdown. The percentage discount will be visible on the results page products. The discount code will be automatically redeemed at checkout.

        `Code` - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first.

    **Dynamic Discount**

    Our system supports the addition of multiple Shopify discount codes on the results page, applied dynamically according to the cart's total value. 

    1. Start by creating your Shopify discount codes as explained in [Step 1](#step-1-generating-a-discount-code-in-shopify). 
        
        !!! note

            Remember, only manual discount codes are compatible with our app.

    2. Proceed to the quiz's Results Page tab. Within [Results Page Settings > Discounts](/reference/quiz-builder/results-page/#discounts-settings), activate Dynamic Discounts. Click "activate" to open the discount menu.

        ![how to add discount dynamic](/images/manual_quizbuilder_resultspage_settings_discount_dynamicdiscounts.png){width="300"}

        `Enable notifications` - A toast notification will appear when a customer qualifies for a discount. Toggle to enable/disable.

        `Encourage discounts` - The notification will also include a message telling the customer how close they are to receiving the next highest discount. Toggle to enable/disable.

        **Discount [A] Settings**

        `Discount code` - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first.

        `Discount percentage` - Type the discount %. The percentage discount will be visible in the results page products. The discount code will be automatically redeemed at checkout.

        `Min. value in cart` - Type the value of products added to the cart on the results page above which the discount will be applied.

        `+ / add another discount` - Adds a new dynamic discount (Discount [B]).

        `bin / delete this discount` - deletes this dynamic discount.

        `add a discount` - Adds a new dynamic discount below (Discount [B]).

        `deactivate` - Deactivates dynamic discounts.

    **Step 3: Publish Changes**

    1. Click the top-right [`Publish` button](/reference/quiz-builder/questions/) to apply your changes to the live quiz/preview.

    **Alternatively**

    Your developer can also add a discount code to the results page using custom JavaScript code added to the Results page.
    
    !!! info

        Check out [this article](/how-to-guides/add-javascript/) for more information on how to add custom JavaScript code to your results page.

    !!! example 
        You can use this function 
        
        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF'); 

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.


=== "WooCommerce"

    **Step 1: Generate a Discount Code**

    If your store is built on WooCommerce, you’ll need [the Advanced Coupons for WooCommerce plugin](https://wordpress.org/plugins/advanced-coupons-for-woocommerce-free/) for this to work.

    Create a coupon code, then navigate to the URL Coupons section. Make sure the Redirect To URL points to your cart page. Copy the URI (it’s the end part of the URL, excluding the https + your domain name):

    ![how to add discount woo step 1](/images/how_to_add_discount_woo_step_1.png)

    Example: if the Coupon URL which appears is `https://yourdomain.com/coupon/codexyz/`, then the part you need to copy is `/coupon/codexyz/`. 

    **Step 2: Configure Your Discount Code on the Results Page**

    Then in the Product Recommendation Quiz, go to the [Results Page Settings > Checkout Settings](/reference/quiz-builder/results-page/) and paste the copied URI in the `Cart URL` field.

    ![how to add discount woo step 2](/images/how_to_add_discount_woo_step_2.png)

    This will apply the coupon code when your customers finish the quiz and proceed to cart, then it will redirect them automatically to the cart page in your store.

    **Step 3: Publish Changes**

    1. Click the top-right [`Publish` button](/reference/quiz-builder/questions/) to apply your changes to the live quiz/preview.

    **Alternatively**

    Your developer can also add a discount code to the results page using custom JavaScript code added to the Results page. Check out [this article](/how-to-guides/add-javascript/) for more information.

    
    !!! info

        Check out [this article](/how-to-guides/add-javascript/) for more information on how to add custom JavaScript code to your results page.

    !!! example 
        You can use this function 
        
        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF'); 

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.


=== "Magento"

    It is not currently possible to add discount coupons into your quiz built with RevenueHunt app for Magento.

    Your developer can, however, add a discount code to the results page using custom JavaScript code added to the Results page. 
    
    !!! info

        Check out [this article](/how-to-guides/add-javascript/) for more information on how to add custom JavaScript code to your results page.

    !!! example 
        You can use this function 
        
        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF'); 

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.

=== "BigCommerce"

    It is not currently possible to add discount coupons into your quiz built with RevenueHunt app for BigCommerce.

    Your developer can, however, add a discount code to the results page using custom JavaScript code added to the Results page. 
    
    !!! info

        Check out [this article](/how-to-guides/add-javascript/) for more information on how to add custom JavaScript code to your results page.

    !!! example 
        You can use this function 
        
        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF'); 

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.
 

=== "Standalone"

    It is not currently possible to add discount coupons into your quiz built with Standalone version of the RevenueHunt app.

    Your developer can, however, add a discount code to the results page using custom JavaScript code added to the Results page. Check out [this article](/how-to-guides/add-javascript/) for more information.

    
    !!! info

        Check out [this article](/how-to-guides/add-javascript/) for more information on how to add custom JavaScript code to your results page.

    !!! example 
        You can use this function 
        
        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF'); 

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.


## Include Discount Codes in Follow-Up Emails

=== "Shopify"

    To further personalize the customer experience, you can incorporate the discount code within the follow-up email sent to the customer with quiz results. This allows customers to conveniently copy and paste the code at checkout.

    Simply go to the [Quiz Settings](/reference/quiz-builder/quiz-settings/), find the [Emails to respondents](/reference/quiz-builder/notifications/#to-respondent) tab, and edit the message to include your discount code text.

    !!! info

        Check out [this article](/how-to-guides/send-result-emails/) for more information on how to set up and customize the quiz result email.


=== "Shopify (Legacy)"

    To further personalize the customer experience, you can incorporate the discount code within the follow-up email and results page. This allows customers to conveniently copy and paste the code at checkout.

    Simply go to the [Quiz Builder](/reference/quiz-builder/), find the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and edit the message to include your discount code text.

    !!! info

        Check out [this article](/how-to-guides/send-result-emails/) for more information on how to set up and customize the quiz result email.

=== "WooCommerce"

    To further personalize the customer experience, you can incorporate the discount code within the follow-up email and results page. This allows customers to conveniently copy and paste the code at checkout.

    Simply go to the [Quiz Builder](/reference/quiz-builder/), find the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and edit the message to include your discount code text.

    !!! info

        Check out [this article](/how-to-guides/send-result-emails/) for more information on how to set up and customize the quiz result email.

=== "Magento"

    To further personalize the customer experience, you can incorporate the discount code within the follow-up email and results page. This allows customers to conveniently copy and paste the code at checkout.

    Simply go to the [Quiz Builder](/reference/quiz-builder/), find the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and edit the message to include your discount code text.

    !!! info

        Check out [this article](/how-to-guides/send-result-emails/) for more information on how to set up and customize the quiz result email.

=== "BigCommerce"

    To further personalize the customer experience, you can incorporate the discount code within the follow-up email and results page. This allows customers to conveniently copy and paste the code at checkout.

    Simply go to the [Quiz Builder](/reference/quiz-builder/), find the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and edit the message to include your discount code text.

    !!! info

        Check out [this article](/how-to-guides/send-result-emails/) for more information on how to set up and customize the quiz result email.

=== "Standalone"

    To further personalize the customer experience, you can incorporate the discount code within the follow-up email and results page. This allows customers to conveniently copy and paste the code at checkout.

    Simply go to the [Quiz Builder](/reference/quiz-builder/), find the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and edit the message to include your discount code text.

    !!! info

        Check out [this article](/how-to-guides/send-result-emails/) for more information on how to set up and customize the quiz result email.

## Apply Discount Only if Customer Leaves Their Email

=== "Shopify"

    It is not currently possible to add discount coupons into your quiz built with the new version of the RevenueHunt app for Shopify. 
    
    If you have a discount applied to certain products in your store, these reduced prices will be reflected in the quiz results page automatically.


=== "Shopify (Legacy)"

    In RevenueHunt app, it is possible to apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click ``Activate`. [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen will appear and a second Results page will be added.
        ![how to add discount multiple result pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount result pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: In this case, *Results Page 1* will be left as default with no discount and the discount will be applied to *Results Page 2*. To do that, open the `Results Page 2 Settings -> Discount code settings -> Discount code` and click `add`. You can then edit the `Visible % discount` and add the code.

        !!! warning

            For the discount to work, you need to set it up first in your Shopify store. Check the [first part of this article](#how-to-add-a-discounts-to-your-quiz) for instructions.

    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`. 

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)
        
    5. **Add Jump Logic**: Now you can redirect customers to either the *Results Page 1 (no discount)* or the *Results Page 2 (discount)* depending on their answer to the discount question. To do that you’ll need to add two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [this article](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Next, you’ll have to add Jump Logic to the email question. In this case, it is enough to always send the customer to the *Results Page 2 (discount)* with the `Always Jump to...` function.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "WooCommerce"

    In RevenueHunt app, it is possible to apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click ``Activate`. [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen will appear and a second Results page will be added.
        ![how to add discount multiple result pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount result pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow the instructions in the [first part of this article](#how-to-add-a-discounts-to-your-quiz) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`. 
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)
        
    5. **Add Jump Logic**: Now you can redirect customers to either the *Results Page 1 (no discount)* or the *Results Page 2 (discount)* depending on their answer to the discount question. To do that you’ll need to add two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [this article](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Next, you’ll have to add Jump Logic to the email question. In this case, it is enough to always send the customer to the *Results Page 2 (discount)* with the `Always Jump to...` function.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "Magento"

    In RevenueHunt app, it is possible to apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click ``Activate`. [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen will appear and a second Results page will be added.
        ![how to add discount multiple result pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount result pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow the instructions in the [first part of this article](#how-to-add-a-discounts-to-your-quiz) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`. 
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)
        
    5. **Add Jump Logic**: Now you can redirect customers to either the *Results Page 1 (no discount)* or the *Results Page 2 (discount)* depending on their answer to the discount question. To do that you’ll need to add two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [this article](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Next, you’ll have to add Jump Logic to the email question. In this case, it is enough to always send the customer to the *Results Page 2 (discount)* with the `Always Jump to...` function.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "BigCommerce"

    In RevenueHunt app, it is possible to apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click ``Activate`. [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen will appear and a second Results page will be added.
        ![how to add discount multiple result pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount result pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow the instructions in the [first part of this article](#how-to-add-a-discounts-to-your-quiz) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`. 
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)
        
    5. **Add Jump Logic**: Now you can redirect customers to either the *Results Page 1 (no discount)* or the *Results Page 2 (discount)* depending on their answer to the discount question. To do that you’ll need to add two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [this article](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Next, you’ll have to add Jump Logic to the email question. In this case, it is enough to always send the customer to the *Results Page 2 (discount)* with the `Always Jump to...` function.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "Standalone"

    In RevenueHunt app, it is possible to apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click ``Activate`. [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen will appear and a second Results page will be added.
        ![how to add discount multiple result pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount result pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow the instructions in the [first part of this article](#how-to-add-a-discounts-to-your-quiz) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`. 
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)
        
    5. **Add Jump Logic**: Now you can redirect customers to either the *Results Page 1 (no discount)* or the *Results Page 2 (discount)* depending on their answer to the discount question. To do that you’ll need to add two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [this article](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Next, you’ll have to add Jump Logic to the email question. In this case, it is enough to always send the customer to the *Results Page 2 (discount)* with the `Always Jump to...` function.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

---
By following these steps, you can integrate discounts into your quiz, improve customer engagement and potentially increase conversions.

