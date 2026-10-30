---
description: "Give customers Growave loyalty points when they complete your RevenueHunt quiz, using Shopify Flow and a customer metafield."
icon: material/gift-outline
---

# How to Reward Quiz Completions with Growave

=== "Shopify"

    Growave is a Shopify loyalty and rewards app. You can give a customer Growave points when they complete your quiz.

    The quiz does not connect to Growave directly. The connection runs through Shopify Flow and a customer metafield:

    - **The quiz** - When a customer completes it, the RevenueHunt app sends the **Quiz Completed** trigger to Shopify Flow.
    - **Shopify Flow** - A workflow sets a quiz completed customer metafield to **True**.
    - **Growave** - It sees the new metafield value and gives the customer the reward.

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/fOZdkzdkptM?si=Ei-O-iiGk80bKVbG" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    !!! info "What you need"

        - A Growave **Growth** plan or higher. The **Customer metafield** earning action is not available on lower plans.
        - A Shopify plan that includes Shopify Flow.
        - The RevenueHunt app, installed and active.

    ## Prepare your quiz

    The **Quiz Completed** trigger runs on a Shopify customer record. RevenueHunt finds that record by the email address the customer types into the quiz.

    1. **Add an email question to your quiz, and make it required.** Without an email address, no customer record is created and no reward is given. A phone number is not enough.
    2. **In the RevenueHunt app, open `App settings > Shopify Customers`.**
    3. **Turn on `Enable pushing quiz leads to Shopify Customers`, then click `Save`.**

        ![RevenueHunt App settings, Shopify Customers page, with Enable pushing quiz leads to Shopify Customers turned on and the Shopify Flow section below it](/images/manual_shopifyV2_appsettings_shopifycustomers.png)

    4. **Publish the quiz.**

    For more on customer syncing, see [How to Send Leads to Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/).

    ## Create the customer metafield in Shopify

    This metafield marks that a customer has completed the quiz. Growave reads it in the next section.

    1. **In Shopify Admin, go to `Settings > Metafields and metaobjects > Customers`.**
    2. **Click `Add definition`.**
    3. **In `Name`, type a name you will recognize, for example `Skin type set`.**
    4. **In `Namespace and key`, type a unique key, for example `custom.skin_type_set`.** Write this key down. You need it again in Growave and in Flow.
    5. **Under `Select type`, choose `True or false`.**
    6. **Under `Customer Account API access`, choose `Read and write`.**
    7. **Click `Save`.**

    ![Shopify customer metafield definition named Skin type set, with the key custom.skin_type_set, type True or false, and Customer Account API access set to Read and write](/images/how_to_reward_quiz_completions_with_growave_shopify_metafield.png)

    ## Add the earning rule in Growave

    1. **In the Growave admin, go to `Rewards > Points > Ways to earn`.**
    2. **Click `Add ways to earn` and choose `Customer metafield`.**
    3. **In `Reward`, choose the reward, for example `Points`.**
    4. **In `Point Value`, type the number of points to give.**
    5. **In `Metafield namespace`, type the first part of your Shopify key, for example `custom`.**
    6. **In `Metafield key`, type the second part, for example `skin_type_set`.**
    7. **Set `Metafield value type` to `Boolean`.**
    8. **Set `Metafield condition` to `Equals`.**
    9. **Set `Metafield value` to `True`.**
    10. **In `Title`, type the name customers see for this reward, for example `Complete our Skincare Quiz`.**
    11. **Click `Save`.**

    ![Growave Customer metafield earning rule with 100 points, namespace custom, key skin_type_set, value type Boolean, condition Equals, value True, and the title Complete our Skincare Quiz](/images/how_to_reward_quiz_completions_with_growave_growave_earning_rule.png)

    The `How it will work` panel shows the reward frequency limit, for example `1 per lifetime`. With that limit, each customer earns the reward once, even if they take the quiz again.

    ## Build the workflow in Shopify Flow

    1. **In Shopify Admin, go to `Apps > Flow` and click `Create workflow`.**
    2. **Click `Select a trigger`, choose `Product Recommendation Quiz`, then choose `Quiz Completed`.**
    3. **Add a condition on the customer's `Email address`, set to `Not empty and exists`.** This makes sure the workflow only runs for a customer with an email address.

        ![Shopify Flow condition on customer.defaultEmailAddress.emailAddress set to Not empty and exists, under the Quiz Completed trigger](/images/how_to_reward_quiz_completions_with_growave_flow_email_condition.png)

    4. **To reward only one quiz, add a second condition on `Quiz name`, set to `Equal to` and the exact name of your quiz.** Skip this step to reward a completion of any quiz.

        ![Shopify Flow condition on quizCompletion.quizName set to Equal to Skincare quiz, added on the True branch of the email condition](/images/how_to_reward_quiz_completions_with_growave_flow_quiz_name_condition.png)

        !!! warning "Match on the quiz name, not the quiz ID"

            A condition on `quizId` can cause a validation error. Always match on `quizName`, and copy the quiz name exactly as it appears in the RevenueHunt app.

    5. **On the `True` branch, add the action `Update customer metafield`.**
    6. **Select the metafield you created, and set `Value` to `True`.** The `Type` is filled in from the metafield, as `True or false`.

        ![Shopify Flow Update customer metafield action with the Skin type set metafield, type True or false, and value True, at the end of the workflow](/images/how_to_reward_quiz_completions_with_growave_flow_metafield_action.png)

    7. **Give the workflow a name, then click `Turn on workflow`.**

    !!! tip

        For every field the trigger sends, see [Automate Quiz Completions with Shopify Flow](/how-to-guides/automate-quiz-completions-with-shopify-flow/).

    !!! tip "A metafield is simpler than customer tags"

        You can also start a Growave reward from customer tags. A dedicated metafield is simpler to set up, and it is easier to maintain when you change the quiz.

    ## Test the reward

    1. **Complete the published quiz with a test email address.**
    2. **In Shopify Admin, open `Customers` and select the test customer.**
    3. **Check that your metafield, for example `Skin type set`, shows `True`.**
    4. **In the Growave admin, go to `Rewards > Customers` and select the test customer.**
    5. **Check that the reward appears in their activity history.**

        ![Growave customer page showing the Complete our Skincare Quiz action with points added in the Activity list](/images/how_to_reward_quiz_completions_with_growave_growave_activity.png)

    If the metafield is not `True`, open the workflow in Shopify Flow and review its recent runs. Check that the test included an email address, that customer syncing is on, and that the workflow is turned on.

    If the metafield is `True` but no reward appears, check the earning rule in Growave. The namespace and key must match the Shopify metafield exactly.

    !!! tip

        Growave's own guide is the [Growave Help Center article on integrating Growave with RevenueHunt](https://help.growave.io/en/articles/17714905-integrating-growave-with-revenuehunt-quiz-builder).

=== "Shopify (Legacy)"

    !!! note "This version has no Quiz Completed trigger"

        The Growave setup uses the **Quiz Completed** trigger, which only the `💎Built for Shopify` version of the RevenueHunt app sends.

        In the legacy app, a Flow workflow can start on Shopify's `Customer created` trigger and check customer tags instead. See the **Shopify (Legacy)** tab of [Automate Quiz Completions with Shopify Flow](/how-to-guides/automate-quiz-completions-with-shopify-flow/).

        To use the setup on this page, see [Migrate a Legacy Quiz to Built for Shopify](/how-to-guides/migrate-shopify-legacy-quiz/).

=== "WooCommerce"

    !!! note "This integration needs Shopify Flow"

        This integration is not available in this version.

=== "Magento"

    !!! note "This integration needs Shopify Flow"

        This integration is not available in this version.

=== "BigCommerce"

    !!! note "This integration needs Shopify Flow"

        This integration is not available in this version.

=== "Standalone"

    !!! note "This integration needs Shopify Flow"

        This integration is not available in this version.

---
This article explains how to give customers Growave loyalty points when they complete your quiz.
