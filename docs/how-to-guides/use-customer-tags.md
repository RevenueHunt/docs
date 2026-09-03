---
icon: material/tag
description: "Learn how to use customer tags in RevenueHunt for audience segmentation and marketing."
---

# How to Add and Use Customer Tags

A customer tag is a label the quiz attaches to a customer when they select a certain choice. The tags travel with the quiz response to your mailing list or CRM.

Once the tags arrive there, you can group your contacts by what they answered, and write to each group separately.

This article explains how to add tags to choices, send them to a CRM, build segments from them, and write campaigns for those segments.

!!! info "Why segment your audience"

    A long email list is worth little on its own. What it is worth depends on how much you know about the people on it.

    - A highly segmented campaign can earn more than three times the revenue per recipient of an unsegmented one.
    - A healthy list earns around $1 per subscriber per month. Much less than that usually means the list needs finer segments.

    Customer tags give you that detail without asking anyone to fill in a profile. The customer answers the quiz, and the answers become tags.

## Add customer tags to your quiz

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/oo889rtufp0?si=ttwX_qBEEX3ARQ2S" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open your quiz in the [Quiz builder](/reference/quiz-builder/quiz-builder/).** Click `Customize` on the quiz you want to tag.

    2. **Click a choice to open its [Choice settings](/reference/quiz-builder/questions/#choice-settings).**

    3. **Find the `Customer Tags` section.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags.png)

    4. **Use the search bar to find a tag you already created.**

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags_createnew](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags_createnew.png)

    5. **To add a new tag, type the name and click `Create new tag`.** One choice can carry several tags.

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags_tags](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags_tags.png)

        ![manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags_tagsexample](/images/manual_shopifyV2_quizbuilder_quizbuilder_questions_choicesettings_customertags_tagsexample.png)

        !!! tip "Give every customer the same tag"

            To put one shared tag on every customer, add it to all the choices of a single question. Whichever choice they select, the tag follows.

    6. **Click `Save`.** The quiz adds the tag whenever a customer selects that choice.

    7. **Preview the quiz, and check that the tags appear on the response.**

        !!! note "The tags reach your integrations too"

            Every tag on a response is forwarded to the services connected in the [Integrations](/reference/quiz-builder/connect-integrations/) tab. Connect Shopify Customers and the tags land on the Shopify customer profile. Connect Klaviyo and they land on the Klaviyo profile.

=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/e35ea81f285f46c9b9e85bfd1576c710?sid=3e647cc1-752b-4ca3-a3d6-fd0b11a323d4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [`Customer Tags`](/reference/quiz-builder/customer-tags/) tab in the Quiz Builder.**

    2. **Type a tag name next to a choice and confirm with `Enter`.**

        ![manual_quizbuilder_customertags_addtag](/images/manual_quizbuilder_customertags_addtag.png)

    3. **Link that tag to any other choice that calls for it.** A tag you created once stays available for every choice in the quiz.

        !!! tip "Give every customer the same tag"

            To put one shared tag on every customer, add it to all the choices of a single question. Whichever choice they select, the tag follows.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz. From then on, a customer who selects the choice is tagged.

        !!! note "The tags reach your integrations too"

            Every tag on a response is forwarded to the services connected in the [Connect](/reference/quiz-builder/connect-integrations/) tab. Connect Shopify Customers and the tags land on the Shopify customer profile. Connect Klaviyo and they land on the Klaviyo profile.

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/e35ea81f285f46c9b9e85bfd1576c710?sid=3e647cc1-752b-4ca3-a3d6-fd0b11a323d4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [`Customer Tags`](/reference/quiz-builder/customer-tags/) tab in the Quiz Builder.**

    2. **Type a tag name next to a choice and confirm with `Enter`.**

        ![manual_quizbuilder_customertags_addtag](/images/manual_quizbuilder_customertags_addtag.png)

    3. **Link that tag to any other choice that calls for it.** A tag you created once stays available for every choice in the quiz.

        !!! tip "Give every customer the same tag"

            To put one shared tag on every customer, add it to all the choices of a single question. Whichever choice they select, the tag follows.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz. From then on, a customer who selects the choice is tagged.

        !!! note "The tags reach your integrations too"

            Every tag on a response is forwarded to the services connected in the [Connect](/reference/quiz-builder/connect-integrations/) tab. Connect Klaviyo and the tags land on the Klaviyo profile. Connect HubSpot and they land on the HubSpot contact.

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/e35ea81f285f46c9b9e85bfd1576c710?sid=3e647cc1-752b-4ca3-a3d6-fd0b11a323d4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [`Customer Tags`](/reference/quiz-builder/customer-tags/) tab in the Quiz Builder.**

    2. **Type a tag name next to a choice and confirm with `Enter`.**

        ![manual_quizbuilder_customertags_addtag](/images/manual_quizbuilder_customertags_addtag.png)

    3. **Link that tag to any other choice that calls for it.** A tag you created once stays available for every choice in the quiz.

        !!! tip "Give every customer the same tag"

            To put one shared tag on every customer, add it to all the choices of a single question. Whichever choice they select, the tag follows.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz. From then on, a customer who selects the choice is tagged.

        !!! note "The tags reach your integrations too"

            Every tag on a response is forwarded to the services connected in the [Connect](/reference/quiz-builder/connect-integrations/) tab. Connect Klaviyo and the tags land on the Klaviyo profile. Connect HubSpot and they land on the HubSpot contact.

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/e35ea81f285f46c9b9e85bfd1576c710?sid=3e647cc1-752b-4ca3-a3d6-fd0b11a323d4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [`Customer Tags`](/reference/quiz-builder/customer-tags/) tab in the Quiz Builder.**

    2. **Type a tag name next to a choice and confirm with `Enter`.**

        ![manual_quizbuilder_customertags_addtag](/images/manual_quizbuilder_customertags_addtag.png)

    3. **Link that tag to any other choice that calls for it.** A tag you created once stays available for every choice in the quiz.

        !!! tip "Give every customer the same tag"

            To put one shared tag on every customer, add it to all the choices of a single question. Whichever choice they select, the tag follows.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz. From then on, a customer who selects the choice is tagged.

        !!! note "The tags reach your integrations too"

            Every tag on a response is forwarded to the services connected in the [Connect](/reference/quiz-builder/connect-integrations/) tab. Connect Klaviyo and the tags land on the Klaviyo profile. Connect HubSpot and they land on the HubSpot contact.

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/e35ea81f285f46c9b9e85bfd1576c710?sid=3e647cc1-752b-4ca3-a3d6-fd0b11a323d4" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Open the [`Customer Tags`](/reference/quiz-builder/customer-tags/) tab in the Quiz Builder.**

    2. **Type a tag name next to a choice and confirm with `Enter`.**

        ![manual_quizbuilder_customertags_addtag](/images/manual_quizbuilder_customertags_addtag.png)

    3. **Link that tag to any other choice that calls for it.** A tag you created once stays available for every choice in the quiz.

        !!! tip "Give every customer the same tag"

            To put one shared tag on every customer, add it to all the choices of a single question. Whichever choice they select, the tag follows.

    4. **Click the top-right `Publish` button.** This updates both the preview and the live quiz. From then on, a customer who selects the choice is tagged.

        !!! note "The tags reach your integrations too"

            Every tag on a response is forwarded to the services connected in the [Connect](/reference/quiz-builder/connect-integrations/) tab. Connect Klaviyo and the tags land on the Klaviyo profile. Connect HubSpot and they land on the HubSpot contact.

## Send the tags to your CRM

=== "Shopify"

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab.**

    2. **Find the service you use and connect it.** The quiz connects directly to [Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/), [Klaviyo](/how-to-guides/send-leads-to-klaviyo/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/).

        !!! info "Any other service"

            [Zapier](/how-to-guides/send-leads-to-zapier/) and [Webhooks](/how-to-guides/send-leads-to-webhooks/) carry the same data anywhere else. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/) for the full list.

    3. **Follow the instructions the service shows on screen.**

    Every completed quiz then sends the contact details, the answers, the customer tags and the recommended products to that service.

=== "Shopify (Legacy)"

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**

    2. **Find the service you use and connect it.** The quiz connects directly to [Shopify Customers](/how-to-guides/send-leads-to-shopify-customers/), [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/).

        !!! info "Any other service"

            [Zapier](/how-to-guides/send-leads-to-zapier/) and [Webhooks](/how-to-guides/send-leads-to-webhooks/) carry the same data anywhere else. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/) for the full list.

    3. **Follow the instructions the service shows on screen.**

    Every completed quiz then sends the contact details, the answers, the customer tags and the recommended products to that service.

=== "WooCommerce"

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**

    2. **Find the service you use and connect it.** The quiz connects directly to [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/).

        !!! info "Any other service"

            [Zapier](/how-to-guides/send-leads-to-zapier/) and [Webhooks](/how-to-guides/send-leads-to-webhooks/) carry the same data anywhere else. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/) for the full list.

    3. **Follow the instructions the service shows on screen.**

    Every completed quiz then sends the contact details, the answers, the customer tags and the recommended products to that service.

=== "Magento"

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**

    2. **Find the service you use and connect it.** The quiz connects directly to [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/).

        !!! info "Any other service"

            [Zapier](/how-to-guides/send-leads-to-zapier/) and [Webhooks](/how-to-guides/send-leads-to-webhooks/) carry the same data anywhere else. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/) for the full list.

    3. **Follow the instructions the service shows on screen.**

    Every completed quiz then sends the contact details, the answers, the customer tags and the recommended products to that service.

=== "BigCommerce"

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**

    2. **Find the service you use and connect it.** The quiz connects directly to [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/).

        !!! info "Any other service"

            [Zapier](/how-to-guides/send-leads-to-zapier/) and [Webhooks](/how-to-guides/send-leads-to-webhooks/) carry the same data anywhere else. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/) for the full list.

    3. **Follow the instructions the service shows on screen.**

    Every completed quiz then sends the contact details, the answers, the customer tags and the recommended products to that service.

=== "Standalone"

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**

    2. **Find the service you use and connect it.** The quiz connects directly to [Klaviyo](/how-to-guides/send-leads-to-klaviyo/), [HubSpot](/how-to-guides/send-leads-to-hubspot/) and [Omnisend](/how-to-guides/send-leads-to-omnisend/).

        !!! info "Any other service"

            [Zapier](/how-to-guides/send-leads-to-zapier/) and [Webhooks](/how-to-guides/send-leads-to-webhooks/) carry the same data anywhere else. See [how to send quiz leads to your CRM](/how-to-guides/send-leads-to-crm/) for the full list.

    3. **Follow the instructions the service shows on screen.**

    Every completed quiz then sends the contact details, the answers, the customer tags and the recommended products to that service.

## Create segments in your CRM

Your CRM now holds a list of tags for every contact who finished the quiz. A segment is a rule over those tags, and the CRM keeps it up to date on its own.

For example, contacts tagged `dry_skin` can receive a campaign for a moisturizing product, and contacts tagged `oily_skin` a campaign for a cleanser.

!!! example "A segment definition"

    If the custom property `tags` contains `dry_skin`, include the contact in the segment.

    ![example klaviyo segment](https://revenuehunt.com/wp-content/uploads/2024/06/kalviyo-segement-768x450.png)

The wording differs from one CRM to the next, but the shape of the rule is the same everywhere. Every profile carrying the tag joins the segment on its own, including the profiles that arrive later.

!!! warning "A retake replaces the earlier tags"

    In most integrations, a customer who takes the quiz again overwrites the tags from the previous attempt. To keep the tags from every attempt, [contact support](/how-to-guides/contact-customer-support/).

## Send targeted emails

A segment earns nothing until something is sent to it. Build one flow or campaign per segment, and write it around what that group told you.

1. **Read the tags in a segment and name what the group wants.** The tags come from the customer's own answers, so they say it plainly.

2. **Write the email around that need.** Personalize the subject line and the body, and feature the products the quiz recommends for those tags.

3. **Plan the schedule.** Keep the group engaged, but not so often that people unsubscribe.

4. **Automate the sends.** Let the CRM trigger each email from what the customer does, instead of sending them by hand.

!!! example "Two segments, two campaigns"

    - **Curly hair.** Curl-enhancing shampoos, conditioners and styling creams, with tips on maintaining curls and an offer on a curl care bundle.
    - **Dry hair.** Moisturizing shampoos, conditioners and deep-conditioning treatments, with tips on treating dry hair and a discount on a hydrating set.

!!! tip "More on the strategy"

    [How to use customer tags in product quizzes to maximize sales](/customer-success/use-customer-tags-in-quiz/) covers how to plan the segments and the campaigns around them.

---

This article explains how to add customer tags to a quiz, and how to use them to segment your audience and send targeted emails.