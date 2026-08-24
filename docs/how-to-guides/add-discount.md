---
description: "Step-by-step guide to add discount codes to your RevenueHunt quiz questions and results page for automatic or manual checkout application."
icon: material/sale
---

# How to Add a Discount to Your Quiz


=== "Shopify"

    With the Built for Shopify version of the RevenueHunt app, you can:

    - **add your Shopify discount code** to be applied automatically at checkout,
    - **add a discount code as text** to quiz questions or results page,
    - **add the discount code to the [result emails](/reference/quiz-builder/notifications/#to-respondent)**.

    A discount applied to a product in Shopify Products shows on the quiz results page on its own. Otherwise the discount code is applied at checkout, and *the reduced price is visible at the checkout stage only*.



=== "Shopify (Legacy)"

    A discount coupon in your quiz gives the customer a special offer, on the results page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "WooCommerce"

    A discount coupon in your quiz gives the customer a special offer, on the results page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.


    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "Magento"

    A discount coupon in your quiz gives the customer a special offer, on the results page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "BigCommerce"

    A discount coupon in your quiz gives the customer a special offer, on the results page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

=== "Standalone"

    A discount coupon in your quiz gives the customer a special offer, on the results page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This guide explains how to implement Discount Coupons for Checkout with the RevenueHunt app.

    !!! tip "Include Discount Code as text"

        You can also add the discount code as text to the quiz questions or results page by typing the discount code in the text field. Then customers will be able to copy and paste the discount code at checkout.

## Set up discount on the results page

=== "Shopify"


    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/F8rN6jOveOw?si=zZyYtDmydJoeqrg-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    ### Automatic discount code

    You can add a discount code to be applied automatically at checkout when users finish the quiz and proceed to cart.


    !!! warning "Discount code is only applied at Shopify checkout"

        The discount code will not be visible on the quiz preview or the results page. It is applied automatically when the customer proceeds to Shopify checkout.


    1. **Create a Discount code in Shopify**: Create the code in Shopify before you add it to the results page.

        !!! warning "Create a Discount code in Shopify"

            You need to create a discount code in Shopify first before adding it to the quiz results page.

        - Navigate to the Shopify admin panel and select the `Discounts` tab.
        - Click on `Create Discount` to set up a new discount code.
        - Choose the type of discount (e.g., percentage, fixed amount). Enter a discount code name (e.g., `quiz123`) or specify the discount amount (e.g., 20%).
        - Select applicable products from your catalog.
        - Save the discount settings and copy the discount code.

        ![how to add discount in shopify](https://loom.com/i/f7b4f7a482ea4dab8c0b23370bce4c68?workflows_screenshot=true)

    2. **Configuring the Discount code in Quiz results Page**: Configure the code on the results page, so it applies at checkout.

        - Open the RevenueHunt Quizzes app and open your quiz by clicking `Customize`.
        - Navigate to the ['Results page > Results page settings'](/reference/quiz-builder/results-page/#results-page-settings) by clicking on the Results page name.

            ![Results Page settings panel](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings.png)

        - Scroll to the `Discount code` settings section.

            ![Discount code field in the Results Page settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings_discountcode.png)
        - Paste the copied discount code from Shopify into the designated field.

        ![how to add discount automatic](https://loom.com/i/7ae5a8e6a81e4836a0c4c8e7fa9bd66f?workflows_screenshot=true)

        - Save the changes with the top-right `Save` button to apply the discount code to the quiz results.

    3. **Testing the Discount code**: Test the live quiz to ensure the discount code is applied correctly at checkout.

        - After setting up the discount code, visit your website and take a sample quiz.
        - Proceed to the cart and then to checkout.
        - Verify that the discount code `quiz123` is automatically applied to eligible products in the cart.

        ![how to add discount automatic checkout](https://loom.com/i/79773fc2fa9241dab298e8de28aa1b35?workflows_screenshot=true)

        !!! warning "Discount code only works on live quiz"

            The discount code will not be visible on the quiz preview or the results page. It is applied automatically when the customer proceeds to Shopify checkout.

    ### Discount code as text

    You can add a discount code as text within a [text block](/reference/quiz-builder/results-page/#text) on the Quiz results page. Users will be able to copy and paste the discount code at checkout.

    1. Open the [Results page](/reference/quiz-builder/results-page/).
    2. Click on `Add block`.
    3. Select `Text` block.
    4. Add the discount code to the text field.
    5. Save the changes with the top-right `Save` button.

    ![how to add discount text block](/images/how_to_shopifyv2_add_discount_as_text.png)


    ### Discount code with JavaScript

    !!! tip "Check JavaScript guide"

        Check this article to learn how to add custom JavaScript to the results page: [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

    You can use JavaScript to add a discount code to the results page.

    1. Open the [Results page](/reference/quiz-builder/results-page/).
    2. Open the Results page settings.
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

    Select the `manual` option for a discount code in Shopify. The app can only sync with codes created that way.

    !!! note

        These discounts are managed in Shopify, not in the app.

    **Step 2: Configure Your Discount Code on the Results Page**

    You can add Static or Dynamic discount codes to your quiz.

    **Static Discount**

    1. Navigate to [Results Page Settings > Discount Settings](/reference/quiz-builder/results-page/#discounts-settings) and access the Discount Code Settings section.
    2. Enter the discount code in the `Code` field. It is applied at checkout.

        ![how to add discount static](/images/manual_quizbuilder_resultspage_settings_discount_discountcode.png){width="300"}

        `Visible discount` - Select the `discount %` from the dropdown. The percentage discount will be visible on the results page products. The discount code will be automatically redeemed at checkout.

        `Code` - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first.

    **Dynamic Discount**

    The results page supports several Shopify discount codes, applied according to the cart's total value.

    1. Create your Shopify discount codes first, as [Set up discount on the results page](#set-up-discount-on-the-results-page) explains.

        !!! note

            Only manual discount codes work with the app.

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

    !!! tip

        For more on adding custom JavaScript to a results page, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

    !!! example
        You can use this function

        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF');

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.


=== "WooCommerce"

    **Step 1: Generate a Discount Code**

    A WooCommerce store needs [the Advanced Coupons for WooCommerce plugin](https://wordpress.org/plugins/advanced-coupons-for-woocommerce-free/) for this to work.

    Create a coupon code, then go to the URL Coupons section. Point Redirect To URL at your cart page. Copy the URI, which is the end part of the URL, without the protocol and your domain name:

    ![how to add discount woo step 1](/images/how_to_add_discount_woo_step_1.png)

    Example: if the Coupon URL which appears is `https://yourdomain.com/coupon/codexyz/`, then the part you need to copy is `/coupon/codexyz/`.

    **Step 2: Configure Your Discount Code on the Results Page**

    Then in the Product Recommendation Quiz, go to the [Results Page Settings > Checkout Settings](/reference/quiz-builder/results-page/) and paste the copied URI in the `Cart URL` field.

    ![how to add discount woo step 2](/images/how_to_add_discount_woo_step_2.png)

    The coupon code is then applied when the customer finishes the quiz and goes to the cart. They are sent to the cart page in your store.

    **Step 3: Publish Changes**

    1. Click the top-right [`Publish` button](/reference/quiz-builder/questions/) to apply your changes to the live quiz/preview.

    **Alternatively**

    Your developer can also add a discount code to the Results page with custom JavaScript. For more, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).


    !!! tip

        For more on adding custom JavaScript to a results page, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

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

    !!! tip

        For more on adding custom JavaScript to a results page, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

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

    !!! tip

        For more on adding custom JavaScript to a results page, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

    !!! example
        You can use this function

        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF');

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.


=== "Standalone"

    It is not currently possible to add discount coupons into your quiz built with Standalone version of the RevenueHunt app.

    Your developer can still add a discount code to the Results page with custom JavaScript. For more, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).


    !!! tip

        For more on adding custom JavaScript to a results page, see [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/).

    !!! example
        You can use this function

        ```html

        /* set specific discount code \*/
        prq.setDiscountCode('10-OFF');

        ```
        to add a custom coupon or a discount code to the results page and apply it to all the products. Note, that this coupon code needs to be first set up in your store.


## Include discount codes in Follow-up emails

=== "Shopify"

    You can put the discount code in the follow-up email that carries the quiz results. The customer can then copy the code and paste it at checkout.

    Go to [Quiz settings](/reference/quiz-builder/quiz-settings/), open the [Emails to respondents](/reference/quiz-builder/notifications/#to-respondent) tab, and add your discount code to the message.

    !!! tip

        To set up and customize the quiz result email, see [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).


=== "Shopify (Legacy)"

    You can put the discount code in the follow-up email and on the results page. The customer can then copy the code and paste it at checkout.

    Go to the [Quiz Builder](/reference/quiz-builder/), open the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and add your discount code to the message.

    !!! tip

        To set up and customize the quiz result email, see [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "WooCommerce"

    You can put the discount code in the follow-up email and on the results page. The customer can then copy the code and paste it at checkout.

    Go to the [Quiz Builder](/reference/quiz-builder/), open the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and add your discount code to the message.

    !!! tip

        To set up and customize the quiz result email, see [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "Magento"

    You can put the discount code in the follow-up email and on the results page. The customer can then copy the code and paste it at checkout.

    Go to the [Quiz Builder](/reference/quiz-builder/), open the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and add your discount code to the message.

    !!! tip

        To set up and customize the quiz result email, see [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "BigCommerce"

    You can put the discount code in the follow-up email and on the results page. The customer can then copy the code and paste it at checkout.

    Go to the [Quiz Builder](/reference/quiz-builder/), open the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and add your discount code to the message.

    !!! tip

        To set up and customize the quiz result email, see [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "Standalone"

    You can put the discount code in the follow-up email and on the results page. The customer can then copy the code and paste it at checkout.

    Go to the [Quiz Builder](/reference/quiz-builder/), open the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab, and add your discount code to the message.

    !!! tip

        To set up and customize the quiz result email, see [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

## Apply discount only if customer leaves their email

=== "Shopify"

    Yes. Send the customer to one of two results pages, depending on whether they answer the email question. The default page carries no discount, and the second page carries the discount code.

    1. **Create multiple results pages**: Go to [`Results Page Settings -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`. A second results page is added.

        ![Multiple Results Pages activated in the Results Page settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_multipleresultspages.png)

    2. **Add the discount code to Results page 2 only**: Leave *Results page 1* as the default. Open *Results page 2* settings, go to the `Discount code` section and paste your Shopify code. Create it in Shopify first, as [Set up discount on the results page](#set-up-discount-on-the-results-page) describes.

    3. **Add a discount question**: In the [Quiz builder](/reference/quiz-builder/), add a `Yes` or `No` choice question asking whether the customer wants a discount.

        !!! example "Sample question"

            Question: Would you like a discount?

            - Choice 1: Yes
            - Choice 2: No

    4. **Add an email question**: Add an email question so customers can leave their email.

        ![Question types menu in the Quiz builder](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questiontypes.png)

    5. **Add Jump logic to the discount question**: Open the question's `Conditional logic` and add a rule:

        - If the customer answers `Yes`, they continue to the email question.
        - If the customer answers `No`, they jump straight to *Results page 1 (no discount)*.

        !!! example "Two rules on the discount question"

            - IF the answer to `Do you want a discount?` IS `Yes` THEN jump to `Question: What is your email?`
            - `+ Add another rule (OR)`, then IF the answer to `Do you want a discount?` IS `No` THEN jump to `Results page 1`.

            Leave `Default destination` on the email question, so an unanswered question still moves the customer forward.

    6. **Add Jump logic to the email question**: Set the email question to `Always jump to` *Results page 2 (discount)*. Everyone who leaves an email then lands on the page with the code.

        !!! example "One rule on the email question"

            Set `Default destination` to `Results page 2`. No condition is needed here, because every customer who reaches this question is being sent to the same place.

    7. **Save and test**: Save your changes and test the flow with the `Preview` button.

    !!! tip "Simpler alternative"

        If the discount does not have to be blocked completely, add the code as a Text block on the results page. Then use [Display logic](/how-to-guides/use-display-logic/) to show that block only to customers who answered a certain way.

    !!! info "Products discounted in Shopify"

        If you have a discount applied to certain products in your store, these reduced prices are reflected on the quiz results page automatically.


=== "Shopify (Legacy)"

    In the RevenueHunt app, you can apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`. The [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen appears, and a second Results page is added.
        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Leave *Results Page 1* as the default. Put the discount on *Results Page 2*. Open `Results Page 2 Settings -> Discount code settings -> Discount code` and click `add`. You can then edit the `Visible % discount` and add the code.

        !!! warning

            Set the discount up in your Shopify store first. See [Set up discount on the results page](#set-up-discount-on-the-results-page).

    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`.

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    5. **Add Jump Logic**: Send the customer to *Results Page 1* or *Results Page 2*, based on their answer. This needs two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Add Jump Logic to the email question. Use `Always Jump to...` to send the customer to *Results Page 2 (discount)*.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "WooCommerce"

    In the RevenueHunt app, you can apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`. The [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen appears, and a second Results page is added.
        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow [Set up discount on the results page](#set-up-discount-on-the-results-page) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`.
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    5. **Add Jump Logic**: Send the customer to *Results Page 1* or *Results Page 2*, based on their answer. This needs two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Add Jump Logic to the email question. Use `Always Jump to...` to send the customer to *Results Page 2 (discount)*.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "Magento"

    In the RevenueHunt app, you can apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`. The [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen appears, and a second Results page is added.
        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow [Set up discount on the results page](#set-up-discount-on-the-results-page) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`.
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    5. **Add Jump Logic**: Send the customer to *Results Page 1* or *Results Page 2*, based on their answer. This needs two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Add Jump Logic to the email question. Use `Always Jump to...` to send the customer to *Results Page 2 (discount)*.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "BigCommerce"

    In the RevenueHunt app, you can apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`. The [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen appears, and a second Results page is added.
        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow [Set up discount on the results page](#set-up-discount-on-the-results-page) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`.
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    5. **Add Jump Logic**: Send the customer to *Results Page 1* or *Results Page 2*, based on their answer. This needs two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Add Jump Logic to the email question. Use `Always Jump to...` to send the customer to *Results Page 2 (discount)*.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

=== "Standalone"

    In the RevenueHunt app, you can apply a discount at checkout only for the customers who leave their email in the quiz. To set this up you need to follow these steps:

    1. **Create multiple results pages**: To do that, go to the [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`. The [Multiple Results Pages Settings](/reference/quiz-builder/results-page/#multiple-results-pages-settings) screen appears, and a second Results page is added.
        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}
    2. You can then rename the page and edit it by clicking `edit`.
        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)
    3. **Add discount code**: Follow [Set up discount on the results page](#set-up-discount-on-the-results-page) to add a discount code to your quiz.
    4. **Add a discount question**: Next, navigate to the [Quiz Builder](/reference/quiz-builder/) and add a `discount question` by clicking `+`.
        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Add an email question**: Then, add an `email question` by clicking `+`.
        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    5. **Add Jump Logic**: Send the customer to *Results Page 1* or *Results Page 2*, based on their answer. This needs two Jump Logic statements.

        !!! tip

            To learn more about Jump Logic, check [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

    6. **FIRST JUMP LOGIC – DISCOUNT QUESTION**: To add Jump Logic to the discount question, click the `conditional logic` button. In the `Jump Logic` menu, select `Add Jump Logic`. Add the following logic condition:
        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - If the customer answers ‘Yes’ to the discount question, they will automatically go to the next question (the email question).
        - If the customer answers ‘No’ to the discount question, they will be automatically redirected to the *Results Page 1 (no discount)*.

    7. **SECOND JUMP LOGIC – EMAIL QUESTION**: Add Jump Logic to the email question. Use `Always Jump to...` to send the customer to *Results Page 2 (discount)*.
        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)
    8. **Test the quiz**: Once the discounts are set up, update the preview/live quiz with the `Publish` button. Then, test the quiz by clicking the `Preview` button in the top right corner of the app.

---
By following these steps, you can integrate discounts into your quiz, improve customer engagement and potentially increase conversions.

