---
icon: material/sale
---

# How to Add a Discounts to Your Quiz

Incorporating discount coupons into your quiz allows customers to enjoy special offers on the results page or through a follow-up email. 

!!! note

    Please remember, that the management of these discounts is handled through Shopify, not directly within our app.

![how to add a discount example](/images/how to add a discount example.png){ width="300" }

This guide explains how to implement Discount Coupons for Checkout with the Shop Quiz app.

## Step 1: Generate a Discount Code in Shopify

To create a Shopify discount code, refer to [this helpful guide](https://help.shopify.com/en/manual/discounts/create-discount-codes#create-a-fixed-value-or-percentage-discount). Activation of this code is necessary before integrating it with your quiz to ensure functionality at checkout. 

It's essential to select the `manual` option for discount codes in Shopify, as our app can only synchronize with manually created codes.

## Step 2: Configure Your Discount Code on the Results Page

You can add Static or Dynamic discount codes to your quiz.

### Static Discount

1. Navigate to [Results Page Settings > Discount Settings](https://docs.revenuehunt.com/reference/quiz-builder/#discounts-settings) and access the Discount Code Settings section. 
2. Here, you'll find a `Code` field. This field is for entering the discount code that will be automatically applied at checkout.
    ![how to add discount static](/images/manual_quizbuilder_resultspage_settings_discount_discountcode.png){width="500"}


    **Visible discount** - Select the `discount %` from the dropdown. The percentage discount will be visible on the results page products. The discount code will be automatically redeemed at checkout.

    **Code** - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first.

### Dynamic Discount

Our system supports the addition of multiple Shopify discount codes on the results page, applied dynamically according to the cart's total value. 

1. Start by creating your Shopify discount codes as explained in [Step 1](#step-1-generating-a-discount-code-in-shopify). 
    
    !!! note

        Remember, only manual discount codes are compatible with our app.

2. Proceed to the quiz's Results Page tab. Within [Results Page Settings > Discounts](https://docs.revenuehunt.com/reference/quiz-builder/#discounts-settings), activate Dynamic Discounts. Click "activate" to open the discount menu.

    ![how to add discount dynamic](/images/manual_quizbuilder_resultspage_settings_discount_dynamicdiscounts.png){width="500"}

    **Enable notifications** - A toast notification will appear when a customer qualifies for a discount. Toggle to enable/disable.

    **Encourage discounts** - The notification will also include a message telling the customer how close they are to receiving the next highest discount. Toggle to enable/disable.

    **Discount [A] Settings**

    - **Discount code** - Type a discount code that corresponds to this discount. You have to set up this discount code in your store > Shopify Discounts first.

    - **Discount percentage** - Type the discount %. The percentage discount will be visible in the results page products. The discount code will be automatically redeemed at checkout.

    - **Min. value in cart** - Type the value of products added to the cart on the results page above which the discount will be applied.

    **+ / add another discount** - Adds a new dynamic discount (Discount [B]).

    **bin / delete this discount** - deletes this dynamic discount.

    **add a discount** - Adds a new dynamic discount below (Discount [B]).

    **deactivate** - Deactivates dynamic discounts.

## Step 3: Publish Changes

1. Click the top-right [`Publish` button](https://docs.revenuehunt.com/reference/quiz-builder/#quiz-builder_1) to apply your changes to the live quiz/preview.

## (Optional) Including Discount Codes in Follow-Up Emails

To further personalize the customer experience, you can incorporate the discount code within the follow-up email and results page. This allows customers to conveniently copy and paste the code at checkout.

Simply go to your quiz settings, find the [Notifications > TO RESPONDENT](https://docs.revenuehunt.com/reference/quiz-builder/#to-respondent) tab, and edit the message to include your discount code text.

---
By following these steps, you can effectively integrate discounts into your quiz, enhancing customer engagement and potentially increasing conversions.




