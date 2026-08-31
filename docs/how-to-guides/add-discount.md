---
description: "Step-by-step guide to add discount codes to your RevenueHunt quiz questions and results page for automatic or manual checkout application."
icon: material/sale
---

# How to Add a Discount to Your Quiz

=== "Shopify"

    A discount rewards the customer for finishing the quiz. This version can:

    - [Apply a Shopify discount code automatically at checkout](#apply-the-code-automatically-at-checkout).
    - [Show the code as text](#show-the-code-as-text) on a question or the results page, for the customer to copy.
    - [Apply the code with custom JavaScript](#apply-the-code-with-custom-javascript).
    - [Put the code in the result email](#include-the-code-in-a-follow-up-email).

    !!! info "A discount set on the product itself needs no code"

        A product discounted in Shopify shows its reduced price on the results page by itself. A discount code works differently: it is redeemed at checkout, so the customer sees the reduction only at that stage.

=== "Shopify (Legacy)"

    A discount coupon rewards the customer for finishing the quiz, with an offer on the Results Page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    There are four ways to get the code to the customer:

    - [Apply the code automatically at checkout](#apply-the-code-automatically-at-checkout).
    - [Show the code as text](#show-the-code-as-text), for the customer to copy.
    - [Apply the code with custom JavaScript](#apply-the-code-with-custom-javascript).
    - [Put the code in a follow-up email](#include-the-code-in-a-follow-up-email).

=== "WooCommerce"

    A discount coupon rewards the customer for finishing the quiz, with an offer on the Results Page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    There are four ways to get the code to the customer:

    - [Apply the code automatically at checkout](#apply-the-code-automatically-at-checkout).
    - [Show the code as text](#show-the-code-as-text), for the customer to copy.
    - [Apply the code with custom JavaScript](#apply-the-code-with-custom-javascript).
    - [Put the code in a follow-up email](#include-the-code-in-a-follow-up-email).

=== "Magento"

    A discount coupon rewards the customer for finishing the quiz, with an offer on the Results Page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This version has no discount field in the quiz, so there are three ways to get the code to the customer:

    - [Show the code as text](#show-the-code-as-text), for the customer to copy.
    - [Apply the code with custom JavaScript](#apply-the-code-with-custom-javascript).
    - [Put the code in a follow-up email](#include-the-code-in-a-follow-up-email).

=== "BigCommerce"

    A discount coupon rewards the customer for finishing the quiz, with an offer on the Results Page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This version has no discount field in the quiz, so there are three ways to get the code to the customer:

    - [Show the code as text](#show-the-code-as-text), for the customer to copy.
    - [Apply the code with custom JavaScript](#apply-the-code-with-custom-javascript).
    - [Put the code in a follow-up email](#include-the-code-in-a-follow-up-email).

=== "Standalone"

    A discount coupon rewards the customer for finishing the quiz, with an offer on the Results Page or in a follow-up email.

    ![how to add a discount example](/images/how_to_add_a_discount_example.png){width="300"}

    This version has no discount field in the quiz, so there are three ways to get the code to the customer:

    - [Show the code as text](#show-the-code-as-text), for the customer to copy.
    - [Apply the code with custom JavaScript](#apply-the-code-with-custom-javascript).
    - [Put the code in a follow-up email](#include-the-code-in-a-follow-up-email).

## Set up a discount on the results page

The results page can reach the checkout in three ways, and they combine. A code applied automatically stays invisible until checkout, so showing it as text as well tells the customer what they are getting.

### Apply the code automatically at checkout

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/F8rN6jOveOw?si=zZyYtDmydJoeqrg-" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! warning "The code stays invisible until checkout"

        It appears neither in the quiz preview nor on the results page. Shopify applies it when the customer reaches checkout. To tell the customer about it, [show it as text](#show-the-code-as-text) as well.

    1. **Open `Discounts` in your Shopify admin and click `Create discount`.**

    2. **Choose the kind of discount, such as a percentage or a fixed amount.**

    3. **Name the code, for example `quiz123`, and set the amount.**

    4. **Choose which products it applies to, then save it and copy the code.**

        ![how to add discount in shopify](https://loom.com/i/f7b4f7a482ea4dab8c0b23370bce4c68?workflows_screenshot=true)

    5. **Open your quiz in the app by clicking `Customize`.**

    6. **Click the results page name to open its [settings](/reference/quiz-builder/results-page/#results-page-settings).**

        ![Results Page settings panel](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings.png)

    7. **Scroll to `Discount code` and paste the code in.**

        ![Discount code field in the Results Page settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_resultspagesettings_discountcode.png)

        ![how to add discount automatic](https://loom.com/i/7ae5a8e6a81e4836a0c4c8e7fa9bd66f?workflows_screenshot=true)

    8. **Click the top-right `Save` button.**

    9. **Take the live quiz through to checkout, and check the code is applied.**

        ![how to add discount automatic checkout](https://loom.com/i/79773fc2fa9241dab298e8de28aa1b35?workflows_screenshot=true)

        The preview cannot show this, because the code is applied by Shopify checkout.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/36ed1600df294287bf24d94bc438d4c3?sid=7c53ed8e-ab4c-4276-88bd-0509cdf954b9" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    **Before you start**

    Create the discount code in your Shopify admin, following the [Shopify guide to discount codes](https://help.shopify.com/en/manual/discounts/create-discount-codes#create-a-fixed-value-or-percentage-discount). Choose the `manual` type, because the app reads no other kind, and activate the code before you connect it to the quiz.

    !!! note "The discount lives in Shopify"

        You create, change and end the discount in Shopify. The app only points at it.

    **A static discount, the same code for everyone**

    1. **Go to [Results Page Settings > Discount Settings](/reference/quiz-builder/results-page/#discounts-settings).**

    2. **Type your code into the `Code` field.** It is redeemed at checkout.

        ![how to add discount static](/images/manual_quizbuilder_resultspage_settings_discount_discountcode.png){width="300"}

    3. **Pick a percentage under `Visible discount`.** That figure shows on the results page products.

    4. **Click the top-right `Publish` button.**

    **A dynamic discount, a different code per cart value**

    1. **Create one Shopify discount code per tier**, as *Before you start* describes.

    2. **Go to [Results Page Settings > Discounts](/reference/quiz-builder/results-page/#discounts-settings) and click `activate`.**

        ![how to add discount dynamic](/images/manual_quizbuilder_resultspage_settings_discount_dynamicdiscounts.png){width="300"}

    3. **Fill in the first discount.**

        `Discount code` - The code, as created in your Shopify discounts.

        `Discount percentage` - Shows on the results page products, and is redeemed at checkout.

        `Min. value in cart` - The cart total above which this discount applies.

    4. **Click `+ / add another discount` for each further tier.**

    5. **Decide what the customer is told.**

        `Enable notifications` - Shows a notification when the customer qualifies for a discount.

        `Encourage discounts` - Adds how close they are to the next discount up.

    6. **Click the top-right `Publish` button.**

        The bin icon deletes one tier, and `deactivate` turns dynamic discounts off again.

=== "WooCommerce"

    !!! info "This route needs the Advanced Coupons plugin"

        [Advanced Coupons for WooCommerce](https://wordpress.org/plugins/advanced-coupons-for-woocommerce-free/) turns a coupon into a URL, and the quiz sends the customer to that URL instead of to the plain cart.

    1. **Create a coupon code in Advanced Coupons.**

    2. **Open its `URL Coupons` section and point `Redirect To URL` at your cart page.**

    3. **Copy the URI, which is the part of the coupon URL after your domain.**

        ![how to add discount woo step 1](/images/how_to_add_discount_woo_step_1.png)

        From `https://yourdomain.com/coupon/codexyz/`, copy `/coupon/codexyz/`.

    4. **Go to [Results Page Settings > Checkout Settings](/reference/quiz-builder/results-page/) and paste it into `Cart URL`.**

        ![how to add discount woo step 2](/images/how_to_add_discount_woo_step_2.png)

    5. **Click the top-right `Publish` button.**

    A customer who finishes the quiz and goes to the cart now lands on that URL, and the coupon is applied for them.

=== "Magento"

    !!! note "Not part of this version"

        The quiz has no discount field here, so it cannot redeem a code for the customer.

        Instead, [show the code as text](#show-the-code-as-text) and let the customer paste it at checkout, or have a developer [apply it with custom JavaScript](#apply-the-code-with-custom-javascript).

=== "BigCommerce"

    !!! note "Not part of this version"

        The quiz has no discount field here, so it cannot redeem a code for the customer.

        Instead, [show the code as text](#show-the-code-as-text) and let the customer paste it at checkout, or have a developer [apply it with custom JavaScript](#apply-the-code-with-custom-javascript).

=== "Standalone"

    !!! note "Not part of this version"

        The quiz has no discount field here, so it cannot redeem a code for the customer.

        Instead, [show the code as text](#show-the-code-as-text) and let the customer paste it at checkout, or have a developer [apply it with custom JavaScript](#apply-the-code-with-custom-javascript).

### Show the code as text

=== "Shopify"

    Put the code in a [Text block](/reference/quiz-builder/results-page/#text) and the customer copies it at checkout.

    1. **Open the [Results page](/reference/quiz-builder/results-page/).**

    2. **Click `Add block` and select `Text`.**

    3. **Type the discount code into the text field.**

    4. **Click the top-right `Save` button.**

    ![how to add discount text block](/images/how_to_shopifyv2_add_discount_as_text.png)

    A question works the same way, if you would rather promise the discount before the customer finishes.

=== "Shopify (Legacy)"

    Put the code in a Content block on the Results Page and the customer copies it at checkout.

    1. **Open the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.**

    2. **Click `+ Add block` and select `Content`.**

    3. **Type the discount code into the text field.**

    4. **Click the top-right `Publish` button.**

    A question works the same way, if you would rather promise the discount before the customer finishes.

=== "WooCommerce"

    Put the code in a Content block on the Results Page and the customer copies it at checkout.

    1. **Open the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.**

    2. **Click `+ Add block` and select `Content`.**

    3. **Type the discount code into the text field.**

    4. **Click the top-right `Publish` button.**

    A question works the same way, if you would rather promise the discount before the customer finishes.

=== "Magento"

    Put the code in a Content block on the Results Page and the customer copies it at checkout.

    1. **Open the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.**

    2. **Click `+ Add block` and select `Content`.**

    3. **Type the discount code into the text field.**

    4. **Click the top-right `Publish` button.**

    A question works the same way, if you would rather promise the discount before the customer finishes.

=== "BigCommerce"

    Put the code in a Content block on the Results Page and the customer copies it at checkout.

    1. **Open the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.**

    2. **Click `+ Add block` and select `Content`.**

    3. **Type the discount code into the text field.**

    4. **Click the top-right `Publish` button.**

    A question works the same way, if you would rather promise the discount before the customer finishes.

=== "Standalone"

    Put the code in a Content block on the Results Page and the customer copies it at checkout.

    1. **Open the [Results Page](/reference/quiz-builder/results-page/) tab in the Quiz Builder.**

    2. **Click `+ Add block` and select `Content`.**

    3. **Type the discount code into the text field.**

    4. **Click the top-right `Publish` button.**

    A question works the same way, if you would rather promise the discount before the customer finishes.

### Apply the code with custom JavaScript

=== "Shopify"

    1. **Open the [Results page](/reference/quiz-builder/results-page/) and open its settings.**

    2. **Scroll to `Custom JavaScript`.**

    3. **Ask your developer to call `await Quiz.applyDiscountCode()` there.**

        !!! tip "Quiz Copilot can write it for you"

            Click `✨Get help with custom JavaScript` to open the Quiz Copilot chat.

    4. **Click the top-right `Save` button.**

    See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/) for what custom JavaScript can reach.

=== "Shopify (Legacy)"

    Your developer can set the code from the Results Page.

    ```javascript
    /* set specific discount code */
    prq.setDiscountCode('10-OFF');
    ```

    That applies the code to every recommended product. The code has to exist in your store first.

    See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/) for where this code goes.

=== "WooCommerce"

    Your developer can set the code from the Results Page.

    ```javascript
    /* set specific discount code */
    prq.setDiscountCode('10-OFF');
    ```

    That applies the code to every recommended product. The code has to exist in your store first.

    See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/) for where this code goes.

=== "Magento"

    Your developer can set the code from the Results Page.

    ```javascript
    /* set specific discount code */
    prq.setDiscountCode('10-OFF');
    ```

    That applies the code to every recommended product. The code has to exist in your store first.

    See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/) for where this code goes.

=== "BigCommerce"

    Your developer can set the code from the Results Page.

    ```javascript
    /* set specific discount code */
    prq.setDiscountCode('10-OFF');
    ```

    That applies the code to every recommended product. The code has to exist in your store first.

    See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/) for where this code goes.

=== "Standalone"

    Your developer can set the code from the Results Page.

    ```javascript
    /* set specific discount code */
    prq.setDiscountCode('10-OFF');
    ```

    That applies the code to every recommended product. The code has to exist in your store first.

    See [How to Add JavaScript to the Quiz](/how-to-guides/add-javascript/) for where this code goes.

## Include the code in a follow-up email

=== "Shopify"

    The result email can carry the discount code, for the customer to copy and paste at checkout.

    1. **Open [Quiz settings](/reference/quiz-builder/quiz-settings/).**

    2. **Go to the [Emails to respondents](/reference/quiz-builder/notifications/#to-respondent) tab.**

    3. **Write the discount code into the message.**

    !!! tip "Setting the email up in the first place"

        See [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "Shopify (Legacy)"

    The follow-up email can carry the discount code, for the customer to copy and paste at checkout.

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab.**

    3. **Write the discount code into the message.**

    !!! tip "Setting the email up in the first place"

        See [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "WooCommerce"

    The follow-up email can carry the discount code, for the customer to copy and paste at checkout.

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab.**

    3. **Write the discount code into the message.**

    !!! tip "Setting the email up in the first place"

        See [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "Magento"

    The follow-up email can carry the discount code, for the customer to copy and paste at checkout.

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab.**

    3. **Write the discount code into the message.**

    !!! tip "Setting the email up in the first place"

        See [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "BigCommerce"

    The follow-up email can carry the discount code, for the customer to copy and paste at checkout.

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab.**

    3. **Write the discount code into the message.**

    !!! tip "Setting the email up in the first place"

        See [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

=== "Standalone"

    The follow-up email can carry the discount code, for the customer to copy and paste at checkout.

    1. **Open the [Quiz Builder](/reference/quiz-builder/).**

    2. **Go to the [Notifications > TO RESPONDENT](/reference/quiz-builder/notifications/#to-respondent) tab.**

    3. **Write the discount code into the message.**

    !!! tip "Setting the email up in the first place"

        See [Setting Up Result Emails with Product Recommendation Quiz](/how-to-guides/send-result-emails/).

## Give the discount only to customers who leave an email

=== "Shopify"

    Send the customer to one of two results pages, depending on whether they answer the email question. The first page carries no discount, and the second carries the code.

    1. **Go to [`Results Page Settings -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`.** A second results page is added.

        ![Multiple Results Pages activated in the Results Page settings](/images/manual_shopifyV2_quizbuilder_quizbuilder_resultspage_resultspages_multipleresultspages.png)

    2. **Open *Results page 2* settings, go to `Discount code` and paste your Shopify code in.** Leave *Results page 1* without one. See [Apply the code automatically at checkout](#apply-the-code-automatically-at-checkout).

    3. **In the [Quiz builder](/reference/quiz-builder/), add a `Yes` or `No` question asking whether the customer wants a discount.**

        !!! example "Sample question"

            Question: Would you like a discount?

            - Choice 1: Yes
            - Choice 2: No

    4. **Add an email question after it.**

        ![Question types menu in the Quiz builder](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_questiontypes.png)

    5. **Open `Conditional logic` on the discount question and add two jump rules.**

        !!! example "Two rules on the discount question"

            - IF the answer to `Would you like a discount?` IS `Yes` THEN jump to the email question.
            - Click `+ Add another rule (OR)`, then IF the answer IS `No` THEN jump to `Results page 1`.

            Leave `Default destination` on the email question, so an unanswered question still moves the customer forward.

    6. **Set the email question to jump to *Results page 2*.**

        !!! example "One rule on the email question"

            Set `Default destination` to `Results page 2`. No condition is needed, because everyone who reaches this question goes to the same place.

    7. **Click `Save`, then test the whole flow with `Preview`.**

    !!! tip "A simpler alternative"

        The discount does not always have to be withheld completely. Put the code in a Text block on one results page, then show that block with [Display logic](/how-to-guides/use-display-logic/), based on how the customer answered.

=== "Shopify (Legacy)"

    Send the customer to one of two Results Pages, depending on whether they answer the email question. The first page carries no discount, and the second carries the code.

    1. **Go to [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`.** A second Results Page is added.

        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}

    2. **Click `edit` to rename and edit the new page.**

        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)

    3. **Open `Results Page 2 Settings -> Discount code settings -> Discount code`, click `add`, and enter the code and the `Visible % discount`.** Leave *Results Page 1* without one.

        !!! warning "Create the code in Shopify first"

            See [Apply the code automatically at checkout](#apply-the-code-automatically-at-checkout).

    4. **Go to the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a discount question.** Ask whether the customer wants a discount, with a `Yes` and a `No` choice.

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Click `+` again to add an email question after it.**

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    6. **Click `conditional logic` on the discount question, open `Jump Logic` and click `Add Jump Logic`.**

        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - A customer who answers `Yes` goes on to the email question.
        - A customer who answers `No` goes to *Results Page 1*, the one without the discount.

    7. **On the email question, set `Always Jump to...` to *Results Page 2*.** Everyone who leaves an address lands on the page with the code.

        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)

    8. **Click the top-right `Publish` button, then test the whole flow with `Preview`.**

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "WooCommerce"

    Send the customer to one of two Results Pages, depending on whether they answer the email question. The first page carries no discount, and the second carries the code.

    1. **Go to [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`.** A second Results Page is added.

        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}

    2. **Click `edit` to rename and edit the new page.**

        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)

    3. **Set the coupon `Cart URL` on *Results Page 2* only**, as [Apply the code automatically at checkout](#apply-the-code-automatically-at-checkout) describes. Leave *Results Page 1* pointing at your plain cart.

    4. **Go to the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a discount question.** Ask whether the customer wants a discount, with a `Yes` and a `No` choice.

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Click `+` again to add an email question after it.**

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    6. **Click `conditional logic` on the discount question, open `Jump Logic` and click `Add Jump Logic`.**

        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - A customer who answers `Yes` goes on to the email question.
        - A customer who answers `No` goes to *Results Page 1*, the one without the discount.

    7. **On the email question, set `Always Jump to...` to *Results Page 2*.** Everyone who leaves an address lands on the page with the code.

        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)

    8. **Click the top-right `Publish` button, then test the whole flow with `Preview`.**

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "Magento"

    Send the customer to one of two Results Pages, depending on whether they answer the email question. The first page carries no discount, and the second carries the code.

    1. **Go to [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`.** A second Results Page is added.

        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}

    2. **Click `edit` to rename and edit the new page.**

        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)

    3. **Write the discount code into a Content block on *Results Page 2*.** Leave *Results Page 1* without one, so only the customers who leave an address ever read the code.

    4. **Go to the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a discount question.** Ask whether the customer wants a discount, with a `Yes` and a `No` choice.

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Click `+` again to add an email question after it.**

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    6. **Click `conditional logic` on the discount question, open `Jump Logic` and click `Add Jump Logic`.**

        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - A customer who answers `Yes` goes on to the email question.
        - A customer who answers `No` goes to *Results Page 1*, the one without the discount.

    7. **On the email question, set `Always Jump to...` to *Results Page 2*.** Everyone who leaves an address lands on the page with the code.

        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)

    8. **Click the top-right `Publish` button, then test the whole flow with `Preview`.**

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "BigCommerce"

    Send the customer to one of two Results Pages, depending on whether they answer the email question. The first page carries no discount, and the second carries the code.

    1. **Go to [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`.** A second Results Page is added.

        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}

    2. **Click `edit` to rename and edit the new page.**

        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)

    3. **Write the discount code into a Content block on *Results Page 2*.** Leave *Results Page 1* without one, so only the customers who leave an address ever read the code.

    4. **Go to the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a discount question.** Ask whether the customer wants a discount, with a `Yes` and a `No` choice.

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Click `+` again to add an email question after it.**

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    6. **Click `conditional logic` on the discount question, open `Jump Logic` and click `Add Jump Logic`.**

        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - A customer who answers `Yes` goes on to the email question.
        - A customer who answers `No` goes to *Results Page 1*, the one without the discount.

    7. **On the email question, set `Always Jump to...` to *Results Page 2*.** Everyone who leaves an address lands on the page with the code.

        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)

    8. **Click the top-right `Publish` button, then test the whole flow with `Preview`.**

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

=== "Standalone"

    Send the customer to one of two Results Pages, depending on whether they answer the email question. The first page carries no discount, and the second carries the code.

    1. **Go to [`Results Page Settings -> Advanced -> Multiple Results Pages`](/reference/quiz-builder/results-page/#multiple-results-pages-settings) and click `Activate`.** A second Results Page is added.

        ![how to add discount multiple results pages](/images/manual_quizbuilder_resultspage_settings_multipleresultspages.png){width="300"}

    2. **Click `edit` to rename and edit the new page.**

        ![how to add discount results pages](/images/how_to_add_discount_result_pages.png)

    3. **Write the discount code into a Content block on *Results Page 2*.** Leave *Results Page 1* without one, so only the customers who leave an address ever read the code.

    4. **Go to the [Quiz Builder](/reference/quiz-builder/) and click `+` to add a discount question.** Ask whether the customer wants a discount, with a `Yes` and a `No` choice.

        ![how to add discount discount question](/images/how_to_add_discount_discount_question.png)

    5. **Click `+` again to add an email question after it.**

        ![how to add discount email question](/images/how_to_add_discount_email_question.png)

    6. **Click `conditional logic` on the discount question, open `Jump Logic` and click `Add Jump Logic`.**

        ![how to add discount jump logic 1](/images/how_to_add_discount_jump_logic_1.png)

        - A customer who answers `Yes` goes on to the email question.
        - A customer who answers `No` goes to *Results Page 1*, the one without the discount.

    7. **On the email question, set `Always Jump to...` to *Results Page 2*.** Everyone who leaves an address lands on the page with the code.

        ![how to add discount jump logic 2](/images/how_to_add_discount_jump_logic_2.png)

    8. **Click the top-right `Publish` button, then test the whole flow with `Preview`.**

    !!! tip "More on jump logic"

        See [How to Use Jump Logic](/how-to-guides/use-jump-logic/).

---

This article explains how to put a discount code on the results page or in a follow-up email. It also covers giving the code only to customers who leave an email address.