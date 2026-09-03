---
description: "Complete guide to integrate RevenueHunt quiz with Klaviyo for targeted email follow-up campaigns."
icon: material/email-newsletter
---

# How to Send Quiz Leads to Klaviyo

Connect your quiz to Klaviyo and every contact from the quiz is added to your Klaviyo account. You can then build email campaigns around what each customer answered.

This article explains how to connect your quiz to Klaviyo and set up a follow-up email flow. For a worked example, follow the tutorial [Sending Follow-up Emails with Klaviyo](/tutorials/follow-up-emails-klaviyo/).


=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=xQ5-t5vueGKlDL4q" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>



=== "Shopify (Legacy)"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


=== "WooCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


=== "Magento"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



=== "BigCommerce"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



=== "Standalone"

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=A3Q1Ly_hZqWCIXrx" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>



## Link your quiz to Klaviyo

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=CtsHul93EE3HbY8K&amp;start=38" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The Klaviyo integration uses OAuth to connect your store to Klaviyo. The connection is made once for the whole store. You then switch it on for each quiz separately.

    1. **Open the RevenueHunt app and navigate to any quiz.**
    2. **Go to `Quiz settings > Integrations` tab.**
    3. **Scroll to the `Mailing & CRMs` section and find the Klaviyo card.**
    4. **Click the `Connect` button.**
    5. **Log in to Klaviyo if prompted.** The app sends you to Klaviyo's authorization page.
    6. **Select the Klaviyo account you want to connect and review the permissions requested, then click `Allow` to authorize the connection.**
    7. **Check the Klaviyo card back in the app.** It shows `Connected`, with your account name and Site ID.
    8. **Turn Klaviyo on for your other quizzes.** The quiz you connected from is already on. For any other, open `Quiz settings > Integrations` and tick `Send Quiz Leads to Klaviyo Profiles`.

    9. **Publish the changes with the top `Save` button.**
    10. **Take the quiz all the way to the results.** Use a sample email that does not already exist in your Klaviyo account.
    11. **Open `Klaviyo > Audience > Profiles`.** If a new profile appeared, the integration works.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    !!! tip "Reconnecting"
        If you previously connected Klaviyo and need to refresh permissions or switch accounts, click `Reconnect` on the Klaviyo card. Use `Disconnect` to revoke the connection entirely.

    !!! info "Legacy API key setup"
        A store that set Klaviyo up before the OAuth integration still works on its saved Public and Private API keys. Reconnect through OAuth anyway: the setup is simpler, and the app then manages the tokens for you.

    **Custom properties**

    From now on, each customer's contact details, answers and product recommendations are sent to your Klaviyo account. They arrive as `custom properties` on the Klaviyo profile, and you use those properties to personalize an email template.

    ![Quiz data on a Klaviyo profile](/images/how_to_klaviyo_shopify_v2_customer_profile.png)


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you need your Klaviyo `Public API Key`. The app uses that key to write to your Klaviyo profiles.

    1. **Open the [Klaviyo API keys tab](https://www.klaviyo.com/account#api-keys-tab), under account `Settings`, and copy your `Public API Key`.**
        ![The Public API Key in Klaviyo account settings](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    2. **Go back to the RevenueHunt app.**
    3. **In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection.** Paste your Public API Key and save.
        ![Pasting the Public API Key into the app](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![The saved Klaviyo connection](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    4. **Publish the changes with the top-right `Publish` button.**
    5. **Take the quiz all the way to the results.** Use a sample email that does not already exist in your Klaviyo account.
    6. **Open `Klaviyo > Audience > Profiles`.** If a new profile appeared, the integration works.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom properties**

    From now on, each customer's contact details, answers and product recommendations are sent to your Klaviyo account. They arrive as `custom properties` on the Klaviyo profile, and you use those properties to personalize an email template.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you need your Klaviyo `Public API Key`. The app uses that key to write to your Klaviyo profiles.

    1. **Open the [Klaviyo API keys tab](https://www.klaviyo.com/account#api-keys-tab), under account `Settings`, and copy your `Public API Key`.**
        ![The Public API Key in Klaviyo account settings](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    2. **Go back to the RevenueHunt app.**
    3. **In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection.** Paste your Public API Key and save.
        ![Pasting the Public API Key into the app](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![The saved Klaviyo connection](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    4. **Publish the changes with the top-right `Publish` button.**
    5. **Take the quiz all the way to the results.** Use a sample email that does not already exist in your Klaviyo account.
    6. **Open `Klaviyo > Audience > Profiles`.** If a new profile appeared, the integration works.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    From now on, each customer's contact details, answers and product recommendations are sent to your Klaviyo account. They arrive as `custom properties` on the Klaviyo profile, and you use those properties to personalize an email template.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you need your Klaviyo `Public API Key`. The app uses that key to write to your Klaviyo profiles.

    1. **Open the [Klaviyo API keys tab](https://www.klaviyo.com/account#api-keys-tab), under account `Settings`, and copy your `Public API Key`.**
        ![The Public API Key in Klaviyo account settings](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    2. **Go back to the RevenueHunt app.**
    3. **In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection.** Paste your Public API Key and save.
        ![Pasting the Public API Key into the app](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![The saved Klaviyo connection](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    4. **Publish the changes with the top-right `Publish` button.**
    5. **Take the quiz all the way to the results.** Use a sample email that does not already exist in your Klaviyo account.
    6. **Open `Klaviyo > Audience > Profiles`.** If a new profile appeared, the integration works.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom properties**

    From now on, each customer's contact details, answers and product recommendations are sent to your Klaviyo account. They arrive as `custom properties` on the Klaviyo profile, and you use those properties to personalize an email template.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you need your Klaviyo `Public API Key`. The app uses that key to write to your Klaviyo profiles.

    1. **Open the [Klaviyo API keys tab](https://www.klaviyo.com/account#api-keys-tab), under account `Settings`, and copy your `Public API Key`.**
        ![The Public API Key in Klaviyo account settings](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    2. **Go back to the RevenueHunt app.**
    3. **In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection.** Paste your Public API Key and save.
        ![Pasting the Public API Key into the app](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![The saved Klaviyo connection](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    4. **Publish the changes with the top-right `Publish` button.**
    5. **Take the quiz all the way to the results.** Use a sample email that does not already exist in your Klaviyo account.
    6. **Open `Klaviyo > Audience > Profiles`.** If a new profile appeared, the integration works.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom properties**

    From now on, each customer's contact details, answers and product recommendations are sent to your Klaviyo account. They arrive as `custom properties` on the Klaviyo profile, and you use those properties to personalize an email template.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=MoMUJ1OTl-cmoBQo&amp;start=104" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    To connect the quiz to Klaviyo you need your Klaviyo `Public API Key`. The app uses that key to write to your Klaviyo profiles.

    1. **Open the [Klaviyo API keys tab](https://www.klaviyo.com/account#api-keys-tab), under account `Settings`, and copy your `Public API Key`.**
        ![The Public API Key in Klaviyo account settings](/images/how_to_send_leads_to_klaviyo_public_api_key.png)
    2. **Go back to the RevenueHunt app.**
    3. **In the [`Quiz > Connect`](/reference/quiz-builder/connect-integrations/) tab, scroll to Klaviyo and edit the connection.** Paste your Public API Key and save.
        ![Pasting the Public API Key into the app](/images/how_to_send_leads_to_klaviyo_public_api_key_provided1.png)
        ![The saved Klaviyo connection](/images/how_to_send_leads_to_klaviyo_public_api_key_provided2.png)

    4. **Publish the changes with the top-right `Publish` button.**
    5. **Take the quiz all the way to the results.** Use a sample email that does not already exist in your Klaviyo account.
    6. **Open `Klaviyo > Audience > Profiles`.** If a new profile appeared, the integration works.

    From now on all the contacts coming from the quiz will be added to your Klaviyo account.

    **Custom properties**

    From now on, each customer's contact details, answers and product recommendations are sent to your Klaviyo account. They arrive as `custom properties` on the Klaviyo profile, and you use those properties to personalize an email template.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

??? warning "Klaviyo limitations"

    **Processing Time**: Klaviyo may have some delay in displaying new leads.

    **Character Limitations**: Special characters (e.g., è, é, ê) may impede data transmission.

    **Missing or incomplete data?**: open the [Response Analysis](/reference/quiz-builder/metrics/#response-analysis) tool for any lead that does not arrive in Klaviyo, or any profile missing quiz data. It reports when optional data was dropped to fit the size limit, and when a response was too large to send. Your dashboard alerts report the same. These messages appear in your app's language.

## Custom properties sent to Klaviyo

Every completed response is sent to Klaviyo as `custom properties` on the customer's profile, and as event properties on the quiz completion event. Property names include your quiz ID, so two quizzes never overwrite each other's data on the same profile.

=== "Shopify"

    Property names use the quiz **Short ID** (`[SQID]`) and internal **references** (`[REF]`) of your questions, choices and tags.

    | Property | Value |
    | --- | --- |
    | `$email` | The customer's email address. |
    | `$first_name` | First name, from a Contact Info block. |
    | `$last_name` | Last name, from a Contact Info block. |
    | `$phone_number` | Phone number, from a Contact Info block. |
    | `QUIZ_NAME-[SQID]` | The name of the quiz. |
    | `RESPONSE_ID-[SQID]` | Unique ID of that quiz session. |
    | `MARKET_ID-[SQID]` | The market or locale, if you use multiple markets. |
    | `ANSWER_BY_BLOCK-[BLOCK_REF]-[SQID]` | The text of the answer given to that question. |
    | `CHOICE-[CHOICE_REF]-[SQID]` | `true` for every choice selected. Best option for segmenting. |
    | `TAG-[TAG_NAME]-[SQID]` | `true` for every [tag](/how-to-guides/use-customer-tags/) assigned. |
    | `VARIABLE_SCORES-[SQID]` | JSON with all [variable](/how-to-guides/set-up-scoring-quiz/) scores. |
    | `HIGHEST_VARIABLE_REF-[SQID]` | Reference of the top-scoring variable. |
    | `RESULT_REF-[SQID]` | Reference or URL of the results page shown. |
    | `RESULT_SECTIONS-[SQID]` | JSON with the result sections shown. |
    | `RESULT_CONTENT_BY_BLOCK-[SQID]` | JSON with the content shown in each result block. |
    | `RECOMMENDATIONS_BY_SLOT-[SQID]` | JSON with the recommended products per [slot](/reference/quiz-builder/results-page/). |

    !!! info "Inside `RECOMMENDATIONS_BY_SLOT`"
        Each recommended item carries: `id`, `handle`, `title`, `description`, `price`, `image`, `onlineStoreUrl` and `vendor`.

=== "Shopify (Legacy)"

    Property names use the quiz **Hash ID** (`[ID]`) and slide IDs.

    | Property | Value |
    | --- | --- |
    | `$email` | The customer's email address. |
    | `$first_name` | First name, from a Contact Info slide. |
    | `$last_name` | Last name, from a Contact Info slide. |
    | `$phone_number` | Phone number, from a Contact Info slide. |
    | `$consent` | Array like `["web", "email"]`, if Klaviyo consent is enabled. |
    | `PERMALINK-[ID]` | Direct link to the customer's results page. |
    | `PERMALINK-HASH-[ID]` | Unique hash of those results. |
    | `RESULT-PAGE-NAME-[ID]` | Name of the results page, for quizzes with multiple results. |
    | `Q-[ID] [SLIDE_ID]: [SLIDE_TITLE]` | The text of the selected answer. |
    | `TAGS-[ID]` | Comma-separated list of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `T-[ID]: [TAG_NAME]` | `true` for every individual tag assigned. |
    | `PRODUCTS-[ID]: product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `SLOT-[ID]: [SLOT_TITLE] - product_[INDEX]_[FIELD]` | The same product fields, grouped by [slot](/reference/quiz-builder/results-page/). |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `image_url`, `price`, `sku`, `id` and `variant_id`. `[INDEX]` starts at `0`.

=== "WooCommerce"

    Property names use the quiz **Hash ID** (`[ID]`) and slide IDs.

    | Property | Value |
    | --- | --- |
    | `$email` | The customer's email address. |
    | `$first_name` | First name, from a Contact Info slide. |
    | `$last_name` | Last name, from a Contact Info slide. |
    | `$phone_number` | Phone number, from a Contact Info slide. |
    | `$consent` | Array like `["web", "email"]`, if Klaviyo consent is enabled. |
    | `PERMALINK-[ID]` | Direct link to the customer's results page. |
    | `PERMALINK-HASH-[ID]` | Unique hash of those results. |
    | `RESULT-PAGE-NAME-[ID]` | Name of the results page, for quizzes with multiple results. |
    | `Q-[ID] [SLIDE_ID]: [SLIDE_TITLE]` | The text of the selected answer. |
    | `TAGS-[ID]` | Comma-separated list of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `T-[ID]: [TAG_NAME]` | `true` for every individual tag assigned. |
    | `PRODUCTS-[ID]: product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `SLOT-[ID]: [SLOT_TITLE] - product_[INDEX]_[FIELD]` | The same product fields, grouped by [slot](/reference/quiz-builder/results-page/). |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `image_url`, `price`, `sku`, `id` and `variant_id`. `[INDEX]` starts at `0`.

=== "Magento"

    Property names use the quiz **Hash ID** (`[ID]`) and slide IDs.

    | Property | Value |
    | --- | --- |
    | `$email` | The customer's email address. |
    | `$first_name` | First name, from a Contact Info slide. |
    | `$last_name` | Last name, from a Contact Info slide. |
    | `$phone_number` | Phone number, from a Contact Info slide. |
    | `$consent` | Array like `["web", "email"]`, if Klaviyo consent is enabled. |
    | `PERMALINK-[ID]` | Direct link to the customer's results page. |
    | `PERMALINK-HASH-[ID]` | Unique hash of those results. |
    | `RESULT-PAGE-NAME-[ID]` | Name of the results page, for quizzes with multiple results. |
    | `Q-[ID] [SLIDE_ID]: [SLIDE_TITLE]` | The text of the selected answer. |
    | `TAGS-[ID]` | Comma-separated list of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `T-[ID]: [TAG_NAME]` | `true` for every individual tag assigned. |
    | `PRODUCTS-[ID]: product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `SLOT-[ID]: [SLOT_TITLE] - product_[INDEX]_[FIELD]` | The same product fields, grouped by [slot](/reference/quiz-builder/results-page/). |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `image_url`, `price`, `sku`, `id` and `variant_id`. `[INDEX]` starts at `0`.

=== "BigCommerce"

    Property names use the quiz **Hash ID** (`[ID]`) and slide IDs.

    | Property | Value |
    | --- | --- |
    | `$email` | The customer's email address. |
    | `$first_name` | First name, from a Contact Info slide. |
    | `$last_name` | Last name, from a Contact Info slide. |
    | `$phone_number` | Phone number, from a Contact Info slide. |
    | `$consent` | Array like `["web", "email"]`, if Klaviyo consent is enabled. |
    | `PERMALINK-[ID]` | Direct link to the customer's results page. |
    | `PERMALINK-HASH-[ID]` | Unique hash of those results. |
    | `RESULT-PAGE-NAME-[ID]` | Name of the results page, for quizzes with multiple results. |
    | `Q-[ID] [SLIDE_ID]: [SLIDE_TITLE]` | The text of the selected answer. |
    | `TAGS-[ID]` | Comma-separated list of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `T-[ID]: [TAG_NAME]` | `true` for every individual tag assigned. |
    | `PRODUCTS-[ID]: product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `SLOT-[ID]: [SLOT_TITLE] - product_[INDEX]_[FIELD]` | The same product fields, grouped by [slot](/reference/quiz-builder/results-page/). |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `image_url`, `price`, `sku`, `id` and `variant_id`. `[INDEX]` starts at `0`.

=== "Standalone"

    Property names use the quiz **Hash ID** (`[ID]`) and slide IDs.

    | Property | Value |
    | --- | --- |
    | `$email` | The customer's email address. |
    | `$first_name` | First name, from a Contact Info slide. |
    | `$last_name` | Last name, from a Contact Info slide. |
    | `$phone_number` | Phone number, from a Contact Info slide. |
    | `$consent` | Array like `["web", "email"]`, if Klaviyo consent is enabled. |
    | `PERMALINK-[ID]` | Direct link to the customer's results page. |
    | `PERMALINK-HASH-[ID]` | Unique hash of those results. |
    | `RESULT-PAGE-NAME-[ID]` | Name of the results page, for quizzes with multiple results. |
    | `Q-[ID] [SLIDE_ID]: [SLIDE_TITLE]` | The text of the selected answer. |
    | `TAGS-[ID]` | Comma-separated list of all [tags](/how-to-guides/use-customer-tags/) assigned. |
    | `T-[ID]: [TAG_NAME]` | `true` for every individual tag assigned. |
    | `PRODUCTS-[ID]: product_[INDEX]_[FIELD]` | The recommended products, one property per field. |
    | `SLOT-[ID]: [SLOT_TITLE] - product_[INDEX]_[FIELD]` | The same product fields, grouped by [slot](/reference/quiz-builder/results-page/). |

    !!! info "Product `[FIELD]` values"
        `name`, `url`, `image_url`, `price`, `sku`, `id` and `variant_id`. `[INDEX]` starts at `0`.

!!! tip "Cannot find a property in Klaviyo?"

    Klaviyo only lists properties it has already received, so take a test quiz first and try again.

    In the Built for Shopify version, a property name holds the reference of the block, choice or tag, not its title. Find that reference in the Quiz Builder, under the `Advanced` tab of the block or choice. Renaming a question therefore does not break your Klaviyo segments.

??? info "Legacy vs Built for Shopify: property naming"

    If you migrated from the legacy app, your Klaviyo segments and email templates need updating because the property names changed.

    | Data | Legacy | Built for Shopify |
    | :--- | :--- | :--- |
    | Quiz ID | Hash ID, for example `LVPS1n` | Short ID, for example `YN5L9G` |
    | Answers | `Q-[ID] [SLIDE_ID]: [SLIDE_TITLE]` | `ANSWER_BY_BLOCK-[BLOCK_REF]-[SQID]` |
    | Tags | `TAGS-[ID]` (comma-separated) | `TAG-[TAG_NAME]-[SQID]` (boolean) |
    | Results page | `PERMALINK-[ID]` | `RESULT_REF-[SQID]` and `RESPONSE_ID-[SQID]` |
    | Products | `PRODUCTS-[ID]: product_0_name` | `RECOMMENDATIONS_BY_SLOT-[SQID]` |

## Sending follow-up emails via Klaviyo

You can send the product recommendation follow-up emails through Klaviyo, but this is not a one-click setup. Someone who knows Klaviyo has to build it.

The instructions here are written to be passed to a developer.

!!! tip "Go beyond the results email"

    This section covers the one email that delivers the results. [How to build post-quiz email flows in Klaviyo](/how-to-guides/send-klaviyo-post-quiz-email-flows/) covers five more: abandoned cart, browse, reorder, cross-sell and win-back, each segmented on the quiz answers and tags.

??? warning "What support can help with"

    The app sends the quiz data to Klaviyo. You build the flows and the email templates in Klaviyo, so ask Klaviyo support about that part of the setup.

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=KsRYtyVaGyDNuoSs&amp;start=187" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list.

        !!! tip

            You can [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [Link your quiz to Klaviyo](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo.

        1. **In Klaviyo, go to `Audience > Lists & Segments` and click `Create New > New Segment`.**
        2. **Name the segment and set up the definition.**
        3. **Segment definition: Select `Properties about someone` and add a property that will be unique for profiles coming from the quiz.** This can be any of the [custom properties](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates) that RevenueHunt sends to Klaviyo Profiles.

            !!! example "Example"

                - `ANSWERS_BY_BLOCK-QuizID` property is unique for profiles coming from the quiz.

                - If the `ANSWERS_BY_BLOCK-QuizID` property is not in the dropdown, take a test quiz and try again.

        4. **Build the rule as `Custom property from the Quiz` `is set` Type: `text`.**

            !!! example "Example"

                - `ANSWERS_BY_BLOCK-QuizID` `is set` Type: `text`.

        5. **Click `Create a segment` and wait for Klaviyo to load all the contacts that match the segment definition.** This may take a few minutes.
        6. **Once the segment finishes loading, all the profiles that already match the segment definition will be added to the segment.** New contacts coming from the quiz will be added to the segment automatically.

    4. **Create an Email Flow**: create a flow that starts when someone is added to the segment from the previous step. This is the hardest part, because the emails have to be built by hand in Klaviyo.

        **Trigger the Flow**

        1. **Open the `Flows` tab in Klaviyo.** The flow you build there reaches only customers who finished the quiz.
        2. **Click `Create flow` and then `Build from scratch`.**
        3. **Name the flow and click `Create flow`.**
        4. **Set up the flow trigger.** Klaviyo asks for one as soon as the flow is created.
        5. **Choose the trigger to be `Added to a segment` and select the segment created in the previous step.** Set the `Reentry criteria` to `Allow reentry`, so a customer gets an email every time they finish the quiz. Click `Confirm` and `Confirm and save`.

            !!! tip "Alternative: trigger from a Klaviyo list"
                You can start the flow when a contact is added to a Klaviyo list, rather than to a segment. Use this if the `Klaviyo list` selector in your email question block already sends contacts to a list. See [Adding quiz contacts to Klaviyo list](#adding-quiz-contacts-to-klaviyo-list).

        **Optional: Update Marketing Consent**

        If you [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), update it in the Klaviyo email flow:

        1. **Right below the flow trigger, add a `Profile property update` action.**
        2. **Click `+ Step`.**
        3. **Set up the profile property update in the menu that opens.**
        4. **Select `Update existing property`.** In the `Select property` dropdown choose `Accepts marketing`, then set the value to `true`.
        5. **Turn this action `LIVE`.**

    5. **Edit the email**: build the email the flow sends.

        ![Creating the email flow in Klaviyo](https://loom.com/i/01df24e93900407b9141998dfb070a2e?workflows_screenshot=true)

        1. **Grab the `EMAIL` action and drop it below the flow trigger.**
        2. **Edit the `Subject` in the `Email details` section.**
        3. **Click `Select template`.** Klaviyo opens the Templates section.
        4. **Click `Create` to make a new email template.** The Klaviyo email builder opens.
        5. **In the Klaviyo email builder, use the ready-made blocks to add images or text to your template.**
        6. **To add the quiz content and the recommended products, drag an `HTML` block into the email builder.**
        7. **The `Quiz settings > Integrations` section holds a button to download a `Klaviyo Template`.** Click the `Klaviyo Template` button and a new window will open. There, click `Copy code` to copy the existing template.

            !!! info "The ready-made Klaviyo template"

                ![The Klaviyo template button in the app](/images/how_to_shopifyv2_klaviyo_shopify_v2_get_template.png)
                ![Copying the template code](/images/how_to_shopifyv2_klaviyo_shopify_v2_copy_template.png)

                The code holds several ready-made snippets. They display:

                - **Dynamic Results page**: Display dynamic results page content that loops through sections and blocks. A Dynamic Results page content that contains all the elements of your results page and replaces content upon each quiz retake. This is the recommended approach for production templates as it adapts to quiz structure changes.
                - **Static Results page**: Display the complete results page content using static lookups. Static Results page content that contains all the elements of your results page and adds content upon each quiz retake. Use this approach for understanding the data structure and for simple implementations.
                - **Individual recommendations**: Display individual product recommendations by slot. Use this to show specific recommended items with their details like title, description, price, and images.
                - **Question answers**: Display quiz information and individual question answers. Use this to show personal data and specific responses from quiz questions.

        8. **Paste the code in the `HTML` block in Klaviyo email.**

            ![The ready-made template pasted into a Klaviyo HTML block](https://loom.com/i/04a9f5a3d3a040d2a97c2b393fc18c41?workflows_screenshot=true)
        9. **`Preview` the email as one of your segment subscribers, to check what it shows.**
        10. **Edit the template as you like.** You can delete the sections of code you do not need, and restyle the rest to match your branding.

            !!! tip "Let Quiz Copilot edit and style your Klaviyo template"
                You do not need a developer to customize the Klaviyo HTML template. Paste the template code into [Quiz Copilot](/how-to-guides/use-quiz-copilot/) and ask it to:

                - remove sections you do not need, for example to keep only the recommended products or only the question answers,
                - restyle the template to match your brand colors, fonts, and spacing,
                - rearrange blocks or change the layout,
                - explain what each part of the template does.

                Once Quiz Copilot returns the updated code, paste it back into the `HTML` block in your Klaviyo template.

            ??? info "Create your own email template"

                Check the [Use quiz data in Klaviyo email templates](/how-to-guides/send-leads-to-klaviyo/#use-quiz-data-in-klaviyo-email-templates) article to learn how to customize your Klaviyo email template with quiz properties.

        11. **When the template is ready, click `Exit`, then `Done`, and return to your flow.**
        12. **Turn your email `LIVE`.**

        From then on, every customer who leaves an email is added to your Klaviyo segment and sent the follow-up email.

    6. **Re-trigger the flow**: to send an email on every retake, set the **reentry criteria** on the flow trigger:

        1. **Open the flow trigger (`Added to a segment`).**
        2. **Set the `Reentry criteria` to `Allow reentry`.**
        3. **Save the trigger.**

        A customer then gets an email every time they finish the quiz.

        !!! tip "Alternative method"
            You can also achieve this by adding a `Profile property update` action at the end of the flow that **deletes** the segment property (for example, `ANSWERS_BY_BLOCK-QuizID`). Each time the customer finishes the quiz, the property is added again, they re-enter the segment, and the flow runs.

            ![Allowing reentry so a retake sends the email again](/images/how_to_shopifyv2_klaviyo_resend_email_with_each_quiz_retake.png)



=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [Link Your Quiz to Klaviyo](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo.

        1. **In Klaviyo, go to `Audience > Lists & Segments` and click `Create New > New Segment`.**
        2. **Name the segment and set up the definition.**
        3. **Pick `PERMALINK-QuizID`.** Only profiles that came from the quiz carry it.
        4. **Take a test quiz and try again if the permalink property is not in the dropdown.**
        5. **Click `Create a segment`.**

    4. **Create an Email Flow**: create a flow that starts when someone is added to the segment from the previous step. This is the hardest part, because the emails have to be built by hand in Klaviyo.

        **Trigger Flow**

        1. **Open the `Flows` tab in Klaviyo.** The flow you build there reaches only customers who finished the quiz.
        2. **Click `Create flow` and then `Build from scratch`.**
        3. **Name the flow and click `Create flow`.**
        4. **Set up the flow trigger.** Klaviyo asks for one as soon as the flow is created.
        5. **Choose the trigger to be `Added to a segment` and select the segment created in the [Create segment for quiz customers](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-customers).** Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.

        **Optional: Update Marketing Consent**

        If you [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), update it in the Klaviyo email flow:

        1. **Right below the flow trigger, add a `Profile property update` action.**
        2. **Click `+ Step`.**
        3. **Set up the profile property update in the menu that opens.**
        4. **Select `Update existing property`.** In the `Select property` dropdown choose `Accepts marketing`, then set the value to `true`.
        5. **Turn this action `LIVE`.**



    5. **Edit the email**: build the email the flow sends.

        1. **Click on the `three dots` and edit the email.**
        2. **Edit the name/subject/email to your liking and select the `HTML email template`.**
        3. **Download the ready-made email template from the `Connect > Klaviyo` tab.**

            ![The Klaviyo template button in the app](/images/how_to_send_leads_to_klaviyo_email_template_download1.png)
            ![Copying the template code](/images/how_to_send_leads_to_klaviyo_email_template_download2.png)

            !!! tip

                If you would rather create your own email template, check [Use quiz data in Klaviyo email templates](#use-quiz-data-in-klaviyo-email-templates) for more details.

        4. **Copy the code and go back to Klaviyo.**
        5. **Open the `HTML email template` and remove the existing code.**
        6. **Paste the new template code.**
        7. **`Preview` the email as one of your segment subscribers.**
        8. **Make sure to `Save` the changes and click `Done`.**
        9. **Return to your flow and turn your email `LIVE`.**

        From then on, every customer who leaves an email is added to your Klaviyo segment and sent the follow-up email.

    6. **Re-trigger the flow**: to send an email on every retake, add a `Profile property update` action at the end of the flow:

        1. **Add a `Profile property update` action at the end of the flow.**
        2. **Click `+ Step`.**
        3. **Select `Delete existing property`.**
        4. **From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps.**

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`.

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, build a segment on the `PERMALINK-{{quiz_id}}` property, so it holds only customers who finished the quiz. Then build a flow that starts when someone is added to that segment, emails them their results, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile**. Removing it lets them re-enter the segment when they retake the quiz.

                For example:

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. **Save the changes and turn the action `LIVE`.**

        Each time the customer takes the quiz again, they are added back to the segment, and the flow runs again.

    ??? tip "Deactivate the app emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up.



=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [Link Your Quiz to Klaviyo](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo.

        1. **In Klaviyo, go to `Audience > Lists & Segments` and click `Create New > New Segment`.**
        2. **Name the segment and set up the definition.**
        3. **Pick `PERMALINK-QuizID`.** Only profiles that came from the quiz carry it.
        4. **Take a test quiz and try again if the permalink property is not in the dropdown.**
        5. **Click `Create a segment`.**

    4. **Create an Email Flow**: create a flow that starts when someone is added to the segment from the previous step. This is the hardest part, because the emails have to be built by hand in Klaviyo.

        **Trigger Flow**

        1. **Open the `Flows` tab in Klaviyo.** The flow you build there reaches only customers who finished the quiz.
        2. **Click `Create flow` and then `Build from scratch`.**
        3. **Name the flow and click `Create flow`.**
        4. **Set up the flow trigger.** Klaviyo asks for one as soon as the flow is created.
        5. **Choose the trigger to be `Added to a segment` and select the segment created in the [Create segment for quiz customers](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-customers).** Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.

        **Optional: Update Marketing Consent**

        If you [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), update it in the Klaviyo email flow:

        1. **Right below the flow trigger, add a `Profile property update` action.**
        2. **Click `+ Step`.**
        3. **Set up the profile property update in the menu that opens.**
        4. **Select `Update existing property`.** In the `Select property` dropdown choose `Accepts marketing`, then set the value to `true`.
        5. **Turn this action `LIVE`.**



    5. **Edit the email**: build the email the flow sends.

        1. **Click on the `three dots` and edit the email.**
        2. **Edit the name/subject/email to your liking and select the `HTML email template`.**
        3. **Download the ready-made email template from the `Connect > Klaviyo` tab.**

            ![The Klaviyo template button in the app](/images/how_to_send_leads_to_klaviyo_email_template_download1.png)
            ![Copying the template code](/images/how_to_send_leads_to_klaviyo_email_template_download2.png)

            !!! tip

                If you would rather create your own email template, check [Use quiz data in Klaviyo email templates](#use-quiz-data-in-klaviyo-email-templates) for more details.

        4. **Copy the code and go back to Klaviyo.**
        5. **Open the `HTML email template` and remove the existing code.**
        6. **Paste the new template code.**
        7. **`Preview` the email as one of your segment subscribers.**
        8. **Make sure to `Save` the changes and click `Done`.**
        9. **Return to your flow and turn your email `LIVE`.**

        From then on, every customer who leaves an email is added to your Klaviyo segment and sent the follow-up email.

    6. **Re-trigger the flow**: to send an email on every retake, add a `Profile property update` action at the end of the flow:

        1. **Add a `Profile property update` action at the end of the flow.**
        2. **Click `+ Step`.**
        3. **Select `Delete existing property`.**
        4. **From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps.**

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`.

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, build a segment on the `PERMALINK-{{quiz_id}}` property, so it holds only customers who finished the quiz. Then build a flow that starts when someone is added to that segment, emails them their results, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile**. Removing it lets them re-enter the segment when they retake the quiz.

                For example:

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. **Save the changes and turn the action `LIVE`.**

        Each time the customer takes the quiz again, they are added back to the segment, and the flow runs again.

    ??? tip "Deactivate the app emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up.


=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [Link Your Quiz to Klaviyo](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo.

        1. **In Klaviyo, go to `Audience > Lists & Segments` and click `Create New > New Segment`.**
        2. **Name the segment and set up the definition.**
        3. **Pick `PERMALINK-QuizID`.** Only profiles that came from the quiz carry it.
        4. **Take a test quiz and try again if the permalink property is not in the dropdown.**
        5. **Click `Create a segment`.**

    4. **Create an Email Flow**: create a flow that starts when someone is added to the segment from the previous step. This is the hardest part, because the emails have to be built by hand in Klaviyo.

        **Trigger Flow**

        1. **Open the `Flows` tab in Klaviyo.** The flow you build there reaches only customers who finished the quiz.
        2. **Click `Create flow` and then `Build from scratch`.**
        3. **Name the flow and click `Create flow`.**
        4. **Set up the flow trigger.** Klaviyo asks for one as soon as the flow is created.
        5. **Choose the trigger to be `Added to a segment` and select the segment created in the [Create segment for quiz customers](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-customers).** Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.

        **Optional: Update Marketing Consent**

        If you [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), update it in the Klaviyo email flow:

        1. **Right below the flow trigger, add a `Profile property update` action.**
        2. **Click `+ Step`.**
        3. **Set up the profile property update in the menu that opens.**
        4. **Select `Update existing property`.** In the `Select property` dropdown choose `Accepts marketing`, then set the value to `true`.
        5. **Turn this action `LIVE`.**



    5. **Edit the email**: build the email the flow sends.

        1. **Click on the `three dots` and edit the email.**
        2. **Edit the name/subject/email to your liking and select the `HTML email template`.**
        3. **Download the ready-made email template from the `Connect > Klaviyo` tab.**

            ![The Klaviyo template button in the app](/images/how_to_send_leads_to_klaviyo_email_template_download1.png)
            ![Copying the template code](/images/how_to_send_leads_to_klaviyo_email_template_download2.png)

            !!! tip

                If you would rather create your own email template, check [Use quiz data in Klaviyo email templates](#use-quiz-data-in-klaviyo-email-templates) for more details.

        4. **Copy the code and go back to Klaviyo.**
        5. **Open the `HTML email template` and remove the existing code.**
        6. **Paste the new template code.**
        7. **`Preview` the email as one of your segment subscribers.**
        8. **Make sure to `Save` the changes and click `Done`.**
        9. **Return to your flow and turn your email `LIVE`.**

        From then on, every customer who leaves an email is added to your Klaviyo segment and sent the follow-up email.

    6. **Re-trigger the flow**: to send an email on every retake, add a `Profile property update` action at the end of the flow:

        1. **Add a `Profile property update` action at the end of the flow.**
        2. **Click `+ Step`.**
        3. **Select `Delete existing property`.**
        4. **From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps.**

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`.

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, build a segment on the `PERMALINK-{{quiz_id}}` property, so it holds only customers who finished the quiz. Then build a flow that starts when someone is added to that segment, emails them their results, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile**. Removing it lets them re-enter the segment when they retake the quiz.

                For example:

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. **Save the changes and turn the action `LIVE`.**

        Each time the customer takes the quiz again, they are added back to the segment, and the flow runs again.

    ??? tip "Deactivate the app emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up.


=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [Link Your Quiz to Klaviyo](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo.

        1. **In Klaviyo, go to `Audience > Lists & Segments` and click `Create New > New Segment`.**
        2. **Name the segment and set up the definition.**
        3. **Pick `PERMALINK-QuizID`.** Only profiles that came from the quiz carry it.
        4. **Take a test quiz and try again if the permalink property is not in the dropdown.**
        5. **Click `Create a segment`.**

    4. **Create an Email Flow**: create a flow that starts when someone is added to the segment from the previous step. This is the hardest part, because the emails have to be built by hand in Klaviyo.

        **Trigger Flow**

        1. **Open the `Flows` tab in Klaviyo.** The flow you build there reaches only customers who finished the quiz.
        2. **Click `Create flow` and then `Build from scratch`.**
        3. **Name the flow and click `Create flow`.**
        4. **Set up the flow trigger.** Klaviyo asks for one as soon as the flow is created.
        5. **Choose the trigger to be `Added to a segment` and select the segment created in the [Create segment for quiz customers](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-customers).** Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.

        **Optional: Update Marketing Consent**

        If you [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), update it in the Klaviyo email flow:

        1. **Right below the flow trigger, add a `Profile property update` action.**
        2. **Click `+ Step`.**
        3. **Set up the profile property update in the menu that opens.**
        4. **Select `Update existing property`.** In the `Select property` dropdown choose `Accepts marketing`, then set the value to `true`.
        5. **Turn this action `LIVE`.**



    5. **Edit the email**: build the email the flow sends.

        1. **Click on the `three dots` and edit the email.**
        2. **Edit the name/subject/email to your liking and select the `HTML email template`.**
        3. **Download the ready-made email template from the `Connect > Klaviyo` tab.**

            ![The Klaviyo template button in the app](/images/how_to_send_leads_to_klaviyo_email_template_download1.png)
            ![Copying the template code](/images/how_to_send_leads_to_klaviyo_email_template_download2.png)

            !!! tip

                If you would rather create your own email template, check [Use quiz data in Klaviyo email templates](#use-quiz-data-in-klaviyo-email-templates) for more details.

        4. **Copy the code and go back to Klaviyo.**
        5. **Open the `HTML email template` and remove the existing code.**
        6. **Paste the new template code.**
        7. **`Preview` the email as one of your segment subscribers.**
        8. **Make sure to `Save` the changes and click `Done`.**
        9. **Return to your flow and turn your email `LIVE`.**

        From then on, every customer who leaves an email is added to your Klaviyo segment and sent the follow-up email.

    6. **Re-trigger the flow**: to send an email on every retake, add a `Profile property update` action at the end of the flow:

        1. **Add a `Profile property update` action at the end of the flow.**
        2. **Click `+ Step`.**
        3. **Select `Delete existing property`.**
        4. **From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps.**

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`.

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, build a segment on the `PERMALINK-{{quiz_id}}` property, so it holds only customers who finished the quiz. Then build a flow that starts when someone is added to that segment, emails them their results, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile**. Removing it lets them re-enter the segment when they retake the quiz.

                For example:

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. **Save the changes and turn the action `LIVE`.**

        Each time the customer takes the quiz again, they are added back to the segment, and the flow runs again.

    ??? tip "Deactivate the app emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up.


=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=_NKZoiG-xGhV8IeO&amp;start=200" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Add Email Question**: To send contacts to Klaviyo your quiz needs to have an email question. You can add it to the quiz from the [Quiz Builder](/reference/quiz-builder/questions/) tab by clicking `+` and selecting `email` from the dropdown list. You can also [ask for marketing consent](/how-to-guides/ask-for-marketing-consent/) directly in the quiz.
    2. **Connect Quiz to Klaviyo**: Follow the instructions in [Link Your Quiz to Klaviyo](#link-your-quiz-to-klaviyo) to learn how to connect your quiz to Klaviyo correctly.
    3. **Create a Segment**: All quiz contacts can be grouped into a segment in Klaviyo.

        1. **In Klaviyo, go to `Audience > Lists & Segments` and click `Create New > New Segment`.**
        2. **Name the segment and set up the definition.**
        3. **Pick `PERMALINK-QuizID`.** Only profiles that came from the quiz carry it.
        4. **Take a test quiz and try again if the permalink property is not in the dropdown.**
        5. **Click `Create a segment`.**

    4. **Create an Email Flow**: create a flow that starts when someone is added to the segment from the previous step. This is the hardest part, because the emails have to be built by hand in Klaviyo.

        **Trigger Flow**

        1. **Open the `Flows` tab in Klaviyo.** The flow you build there reaches only customers who finished the quiz.
        2. **Click `Create flow` and then `Build from scratch`.**
        3. **Name the flow and click `Create flow`.**
        4. **Set up the flow trigger.** Klaviyo asks for one as soon as the flow is created.
        5. **Choose the trigger to be `Added to a segment` and select the segment created in the [Create segment for quiz customers](/tutorials/follow-up-emails-klaviyo/#create-segment-for-quiz-customers).** Click `Confirm` and `Confirm and save`. This way whenever someone enters the segment they will trigger the email flow.

        **Optional: Update Marketing Consent**

        If you [asked for marketing consent in the quiz](/how-to-guides/ask-for-marketing-consent/), update it in the Klaviyo email flow:

        1. **Right below the flow trigger, add a `Profile property update` action.**
        2. **Click `+ Step`.**
        3. **Set up the profile property update in the menu that opens.**
        4. **Select `Update existing property`.** In the `Select property` dropdown choose `Accepts marketing`, then set the value to `true`.
        5. **Turn this action `LIVE`.**



    5. **Edit the email**: build the email the flow sends.

        1. **Click on the `three dots` and edit the email.**
        2. **Edit the name/subject/email to your liking and select the `HTML email template`.**
        3. **Download the ready-made email template from the `Connect > Klaviyo` tab.**

            ![The Klaviyo template button in the app](/images/how_to_send_leads_to_klaviyo_email_template_download1.png)
            ![Copying the template code](/images/how_to_send_leads_to_klaviyo_email_template_download2.png)

            !!! tip

                If you would rather create your own email template, check [Use quiz data in Klaviyo email templates](#use-quiz-data-in-klaviyo-email-templates) for more details.

        4. **Copy the code and go back to Klaviyo.**
        5. **Open the `HTML email template` and remove the existing code.**
        6. **Paste the new template code.**
        7. **`Preview` the email as one of your segment subscribers.**
        8. **Make sure to `Save` the changes and click `Done`.**
        9. **Return to your flow and turn your email `LIVE`.**

        From then on, every customer who leaves an email is added to your Klaviyo segment and sent the follow-up email.

    6. **Re-trigger the flow**: to send an email on every retake, add a `Profile property update` action at the end of the flow:

        1. **Add a `Profile property update` action at the end of the flow.**
        2. **Click `+ Step`.**
        3. **Select `Delete existing property`.**
        4. **From the `Select property` dropdown menu select the property that was used to create a segment in earlier steps.**

            !!! example "Example"

                Select `Delete existing property` > `PERMALINK-QuizID`.

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)

            ??? info "How to send an email every time someone completes the quiz?"

                First, build a segment on the `PERMALINK-{{quiz_id}}` property, so it holds only customers who finished the quiz. Then build a flow that starts when someone is added to that segment, emails them their results, and then **removes the `PERMALINK-{{quiz_id}}` property from their profile**. Removing it lets them re-enter the segment when they retake the quiz.

                For example:

                ![Allowing reentry so a retake sends the email again](/images/how_to_klaviyo_resend_email_with_each_quiz_retake.png)
        5. **Save the changes and turn the action `LIVE`.**

        Each time the customer takes the quiz again, they are added back to the segment, and the flow runs again.

    ??? tip "Deactivate the app emails"
        Remember to deactivate the [email Notifications](/how-to-guides/send-result-emails/) from the Quiz Builder once the Klaviyo flow is set up.


## Adding quiz contacts to Klaviyo list

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/paS5z2nzTvU?si=G8fIYtPfLkZjmy8I&amp;start=114" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    With the OAuth connection in place, you can add contacts from the quiz straight to a Klaviyo list. You need no extra API keys, because the list selector sits inside the email question block.

    1. **Make sure you have a Klaviyo list ready.** To create one, go to `Klaviyo > Audience > Lists & Segments`. In the list settings, make sure to set it to `Single Opt-in`.

        !!! warning
            Quiz contacts can be added only to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) list in Klaviyo.

    2. **Make sure your RevenueHunt account is [connected to Klaviyo via OAuth](#link-your-quiz-to-klaviyo) and that the `Send Quiz Leads to Klaviyo Profiles` checkbox is enabled in the quiz's `Quiz settings > Integrations` section.**
    3. **In the RevenueHunt app, open the [Quiz builder](/reference/quiz-builder/) and select the `Email` block.** The `Email input settings` panel opens.
    4. **Scroll to `Klaviyo list` and pick your list from `Select a Klaviyo list`.**
    5. **Tick `Subscribed` below the list.** It stays greyed out until you pick a list.

        ![The Klaviyo list setting on the email block](/images/how_to_klaviyo_shopify_v2_email_question_settings.png)
    6. **Save your quiz changes with the top-right `Save` button.**

        !!! tip "Per-quiz lists"
            To feed a different Klaviyo list from each quiz, set the list on the email question block of each quiz separately.

    7. **`Preview` the quiz and complete it with a sample email to verify the connection.**
    8. **In Klaviyo, go to `Audience > Lists & Segments` and open the list to confirm the test contact was added as `Subscribed`.**


=== "Shopify (Legacy)"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The RevenueHunt app can add contacts from the quiz straight to a Klaviyo list.

    1. **Create a `Private API Key` in Klaviyo.** The app needs it to write to a list.
    2. **Log in to your Klaviyo account.**
    3. **In account `Settings` open the `API Keys` tab and create a new Private API Key.** For list-specific contact additions, you can get your Klaviyo Private API Key from the [Klaviyo API Keys tab](https://www.klaviyo.com/account#api-keys-tab).
        ![Creating a Private API Key in Klaviyo](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. **Allow `Full access`.**
    5. **Copy the private key.**
    6. **In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.**
    7. **Paste your Private API Key.**
    8. **Choose to `mark all profiles as true` and select a list that contacts should be added to.**

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    9. **Save the changes and publish them with the top-right `Publish` button.**
    10. **Take the quiz with a sample email, then check the list in Klaviyo.**

=== "WooCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The RevenueHunt app can add contacts from the quiz straight to a Klaviyo list.

    1. **Create a `Private API Key` in Klaviyo.** The app needs it to write to a list.
    2. **Log in to your Klaviyo account.**
    3. **In account `Settings` open the `API Keys` tab and create a new Private API Key.** For list-specific contact additions, you can get your Klaviyo Private API Key from the [Klaviyo API Keys tab](https://www.klaviyo.com/account#api-keys-tab).
        ![Creating a Private API Key in Klaviyo](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. **Allow `Full access`.**
    5. **Copy the private key.**
    6. **In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.**
    7. **Paste your Private API Key.**
    8. **Choose to `mark all profiles as true` and select a list that contacts should be added to.**

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    9. **Save the changes and publish them with the top-right `Publish` button.**
    10. **Take the quiz with a sample email, then check the list in Klaviyo.**

=== "Magento"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The RevenueHunt app can add contacts from the quiz straight to a Klaviyo list.

    1. **Create a `Private API Key` in Klaviyo.** The app needs it to write to a list.
    2. **Log in to your Klaviyo account.**
    3. **In account `Settings` open the `API Keys` tab and create a new Private API Key.** For list-specific contact additions, you can get your Klaviyo Private API Key from the [Klaviyo API Keys tab](https://www.klaviyo.com/account#api-keys-tab).
        ![Creating a Private API Key in Klaviyo](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. **Allow `Full access`.**
    5. **Copy the private key.**
    6. **In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.**
    7. **Paste your Private API Key.**
    8. **Choose to `mark all profiles as true` and select a list that contacts should be added to.**

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    9. **Save the changes and publish them with the top-right `Publish` button.**
    10. **Take the quiz with a sample email, then check the list in Klaviyo.**

=== "BigCommerce"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The RevenueHunt app can add contacts from the quiz straight to a Klaviyo list.

    1. **Create a `Private API Key` in Klaviyo.** The app needs it to write to a list.
    2. **Log in to your Klaviyo account.**
    3. **In account `Settings` open the `API Keys` tab and create a new Private API Key.** For list-specific contact additions, you can get your Klaviyo Private API Key from the [Klaviyo API Keys tab](https://www.klaviyo.com/account#api-keys-tab).
        ![Creating a Private API Key in Klaviyo](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. **Allow `Full access`.**
    5. **Copy the private key.**
    6. **In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.**
    7. **Paste your Private API Key.**
    8. **Choose to `mark all profiles as true` and select a list that contacts should be added to.**

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    9. **Save the changes and publish them with the top-right `Publish` button.**
    10. **Take the quiz with a sample email, then check the list in Klaviyo.**

=== "Standalone"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/iIl2njV-UkI?si=ZjTq4oGBKH8ovagW&amp;start=429" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    The RevenueHunt app can add contacts from the quiz straight to a Klaviyo list.

    1. **Create a `Private API Key` in Klaviyo.** The app needs it to write to a list.
    2. **Log in to your Klaviyo account.**
    3. **In account `Settings` open the `API Keys` tab and create a new Private API Key.** For list-specific contact additions, you can get your Klaviyo Private API Key from the [Klaviyo API Keys tab](https://www.klaviyo.com/account#api-keys-tab).
        ![Creating a Private API Key in Klaviyo](/images/how_to_send_leads_to_klaviyo_private_api_key.png)

    4. **Allow `Full access`.**
    5. **Copy the private key.**
    6. **In the Quiz [Connect](/reference/quiz-builder/connect-integrations/) tab scroll to Klaviyo and edit the connection.**
    7. **Paste your Private API Key.**
    8. **Choose to `mark all profiles as true` and select a list that contacts should be added to.**

        !!! warning
            Keep in mind that contacts from the quiz can be added only to a [Single Opt-in](https://help.klaviyo.com/hc/en-us/articles/115005251108) List in Klaviyo.

    9. **Save the changes and publish them with the top-right `Publish` button.**
    10. **Take the quiz with a sample email, then check the list in Klaviyo.**

??? tip "Segmented campaigns work better"

    Adding contacts to a Klaviyo list is not the only option. You can build **dynamic segments** from your customers' answers instead, and send each segment its own email. A segmented campaign earns more than 3X the revenue per recipient of an unsegmented one.

    With Klaviyo you can create segments to filter your leads and assign email flows to each segment. [Read more about sending follow-up emails via Klaviyo](#sending-follow-up-emails-via-klaviyo), including how to create and use segments on Klaviyo.

## Use quiz data in Klaviyo email templates

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/6650ebf870714d9eaf450ea51439b0af?sid=91c5c125-318f-4b07-8233-350d1c7272c5" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    A Klaviyo email template is built from HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) system, so you need a developer to restyle the supplied template to your brand.

    **Custom properties in Klaviyo**

    The app sends every answer, every recommended product and the contact details to the customer's Klaviyo profile, where they appear as `custom properties`.

    ![Quiz data on a Klaviyo profile](/images/how_to_klaviyo_shopify_v2_customer_profile.png)

    To add anything else to the email template, your developer pulls the matching `custom properties` off the profile.

    ??? info "Learn the person|lookup function"

        To build your own email template from these custom properties, read Klaviyo's [message personalization reference](https://help.klaviyo.com/hc/en-us/articles/4408802648731), which covers the `{{ person|lookup:"..." }}` function.

    ??? warning "Overwritten or appended properties"

        Some properties arrive as an array: `ANSWER_BY_BLOCK`, `CHOICE`, `RESPONSE_ID`, `RESULT_REF`, `RESULT_SECTIONS` and `TAG`. Each quiz completion overwrites the previous values.

        However, properties such as `RECOMMENDATIONS_BY_SLOT` or `RESULT_CONTENT_BY_BLOCK` are sent as a JSON object, meaning that their values are appended to the existing data on each quiz completion.

        The supplied Klaviyo email template, which you download from the [Integrations](/reference/quiz-builder/connect-integrations/) tab, contains more than one snippet. To have the values overwritten on each quiz completion, use only the snippet that starts with this comment:


        ```html
        {# ================================================================= #}
        {# DYNAMIC RESULT PAGE CONTENT (LOOPS THROUGH RESULT_SECTIONS-lBJ9bk) #}
        {# This template loops through the result sections and blocks          #}
        {# It will adapt if you change the results page structure in the quiz editor #}
        {# ================================================================= #}
        ```




=== "Shopify (Legacy)"

    A Klaviyo email template is built from HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) system, so you need a developer to restyle the supplied template to your brand.

    The app sends every answer, every recommended product and the contact details to the customer's Klaviyo profile, where they appear as `custom properties`.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    To add anything else to the email template, your developer pulls the matching `custom properties` off the profile.


=== "WooCommerce"

    A Klaviyo email template is built from HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) system, so you need a developer to restyle the supplied template to your brand.

    The app sends every answer, every recommended product and the contact details to the customer's Klaviyo profile, where they appear as `custom properties`.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    To add anything else to the email template, your developer pulls the matching `custom properties` off the profile.

=== "Magento"

    A Klaviyo email template is built from HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) system, so you need a developer to restyle the supplied template to your brand.

    The app sends every answer, every recommended product and the contact details to the customer's Klaviyo profile, where they appear as `custom properties`.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    To add anything else to the email template, your developer pulls the matching `custom properties` off the profile.

=== "BigCommerce"

    A Klaviyo email template is built from HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) system, so you need a developer to restyle the supplied template to your brand.

    The app sends every answer, every recommended product and the contact details to the customer's Klaviyo profile, where they appear as `custom properties`.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    To add anything else to the email template, your developer pulls the matching `custom properties` off the profile.


=== "Standalone"

    A Klaviyo email template is built from HTML, CSS and the [Django templating](https://docs.djangoproject.com/en/stable/ref/templates/builtins/) system, so you need a developer to restyle the supplied template to your brand.

    The app sends every answer, every recommended product and the contact details to the customer's Klaviyo profile, where they appear as `custom properties`.

    ![Quiz data on a Klaviyo profile](/images/how_to_send_leads_to_klaviyo_customer_profile.png)

    To add anything else to the email template, your developer pulls the matching `custom properties` off the profile.

### Example email templates

=== "Shopify"

    ### Use Copilot to generate Klaviyo email template

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.loom.com/embed/645cfa070ef5454f812d851908572cdb?sid=f8c3a497-b077-4c81-bfb6-863320a127cb" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    Quiz Copilot can build the Klaviyo email template for your quiz email flow.

    1. **[Open Quiz Copilot](/how-to-guides/use-quiz-copilot/).** To start fresh, click `New conversation` in the top-right corner of the popup. You can also open it from the [`Quiz settings > Integrations`](/reference/quiz-builder/connect-integrations/) page: find the `Klaviyo` integration and click `Edit template with AI`.
    2. **Paste your desired layout message, and Quiz Copilot will generate the template code.**

        ![Quiz Copilot building Klaviyo templates](https://loom.com/i/0bac7b225d8e44dbad1db2b7748c19f5?workflows_screenshot=true)
    3. **The generated code for the Klaviyo email template can be copied by clicking the `Copy` icon.**
    4. **Paste the generated code directly into an HTML block in your Klaviyo email template.**


    ### Example 1 - display recommended products

    In this example, a quiz with ID `YN5L9G` recommends a simple list of products.

    !!! example "Listing the recommended products"

        ![The recommended products code in the template](/images/how_to_shipifyv2_klaviyo_template_productlist1.png){width="300"}

    1. **To show the recommended products, use this code from the Klaviyo template in the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab:**

        ![The Klaviyo Template button in Quiz settings](/images/how_to_shopifyv2_klaviyo_shopify_v2_get_template.png)

        ??? example "The code from the Integrations tab"

            ```html
            {# ======================================== #}
            {# INDIVIDUAL ITEM RECOMMENDATIONS BY SLOT  #}
            {# ======================================== #}
            <p>
            <b>Display recommendation of item 0 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'image'|lookup:'url' }}
            </p>

            <p>
            <b>Display recommendation of item 1 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'image'|lookup:'url' }}
            </p>

            <p>
            <b>Display recommendation of item 2 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'image'|lookup:'url' }}
            </p>

            <p>
            <b>Display recommendation of item 3 for slot rsbss-ca4fba94 </b>
            <br>
            Title: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'title' }}
            <br>
            Description: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'description' }}
            <br>
            Price: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'currencyCode' }}
            <br>
            Online URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'onlineUrl' }}
            <br>
            Image URL: {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'image'|lookup:'url' }}
            </p>h3>
            ```
    2. **Paste this code into an HTML block in a Klaviyo template.** Previewed as one of the quiz subscribers, it shows the recommended products.

        ![The recommended products shown in a preview](/images/how_to_shipifyv2_klaviyo_template_productlist2.png)

    3. **To style the recommended products, your developer adds CSS classes to the HTML.**

        For example, this is a styled version of the code above:

        ??? example "A styled version of the code above"

            In Klaviyo, it will look like this:

            ![Styling the recommended products with CSS classes](/images/how_to_shipifyv2_klaviyo_template_productlist3.png)

            ```html
            <!-- Two-Column Product Grid for Klaviyo Email -->

            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" align="center" style="font-family: sans-serif;">
            <tr>
                <!-- Product 0 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'image'|lookup:'url' }}" alt="Product 0" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>

                <!-- Product 1 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'image'|lookup:'url' }}" alt="Product 1" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'1'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>
            </tr>

            <tr>
                <!-- Product 2 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'image'|lookup:'url' }}" alt="Product 2" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'2'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>

                <!-- Product 3 -->
                <td style="width: 50%; padding: 10px; vertical-align: top;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="border: 1px solid #ddd; border-radius: 8px; padding: 16px;">
                    <tr>
                    <td style="text-align: center;">
                        <img src="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'image'|lookup:'url' }}" alt="Product 3" style="width: 100%; max-width: 250px; border-radius: 6px; margin-bottom: 12px;">
                        <h3 style="font-size: 18px; color: #333; margin: 10px 0;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'title' }}
                        </h3>
                        <p style="font-size: 14px; color: #555; margin-bottom: 10px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'description' }}
                        </p>
                        <p style="font-size: 16px; color: #111; font-weight: bold; margin-bottom: 12px;">
                        {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'price'|lookup:'currencyCode' }}
                        </p>
                        <a href="{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'3'|lookup:'onlineUrl' }}" style="background-color: #1a73e8; color: #fff; padding: 10px 16px; text-decoration: none; border-radius: 4px; display: inline-block;">
                        View Product
                        </a>
                    </td>
                    </tr>
                </table>
                </td>
            </tr>
            </table>
            ```

        ??? tip "Use Quiz Copilot to style the code"

            You can use [Quiz Copilot](/how-to-guides/use-quiz-copilot/) or another AI agent like ChatGPT or Gemini to generate a styled version of the code.

    4. **You can use elements of the code in your Klaviyo template elements.**


        !!! example "Showing a product title in a text block"


            For example, you can use the `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}` to display the title of the first product in a text block.

            ![Reusing parts of the product code elsewhere](/images/how_to_shipifyv2_klaviyo_template_productlist4.png)

        !!! info "A sample product object"

            This is the product object the quiz sent to Klaviyo:

            - Display recommendation of **item 0** for slot `rsbss-ca4fba94`
            - Title: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'title' }}`
            - Description: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'description' }}`
            - Price: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'amount' }} {{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'price'|lookup:'currencyCode' }}`
            - Online URL: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'onlineUrl' }}`
            - Image URL: `{{ person|lookup:'RECOMMENDATIONS_BY_SLOT-YN5L9G'|lookup:'rsbss-ca4fba94'|lookup:'0'|lookup:'image'|lookup:'url' }}`


    ### Example 2 - display quiz answers


    A Skincare Quiz with ID `YN5L9G` wants to display all customer answers in the email.

    1. **To do this, you can use the following code copied from the Klaviyo template in the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab:**


        ![The Klaviyo Template button in Quiz settings](/images/how_to_shopifyv2_klaviyo_shopify_v2_get_template.png)


        ??? example "The code from the quiz Integrations tab"

            ```html
            {# ======================================= #}
            {# INFORMATION GATHERED FROM THE QUESTIONS #}
            {# ======================================= #}
            <p>
            <p>
            <b>Display quiz name</b>
            <br>
            Quiz name: {{ person|lookup:'QUIZ_NAME-YN5L9G' }}
            </p>
            <p>
            <b>Display personal information</b>
            <br>
            First name: {{ person.first_name }}
            <br>
            Last name: {{ person.last_name }}
            </p>
            </p><p><b>Display all answers for a specific block</b>
            <br>

            {# Display answer for a block of type input and ref qbi-6c4248f5 #}
            Q2: BEFORE WE BEGIN
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbi-6c4248f5-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-dd744cf3 #}
            Q3: AGE GROUP
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-dd744cf3-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-485600ce #}
            Q4: SKIN TYPE
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-485600ce-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-e8cf3180 #}
            Q9: SKIN CONCERNS
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-e8cf3180-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-329aaeff #}
            Q10: ALERGIES
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-329aaeff-YN5L9G' }}
            <br>

            {# Display answer for a block of type input and ref qbi-29f016cf #}
            Q11: WE'VE GOT YOUR RESULTS - #1 [email]
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbi-29f016cf-YN5L9G' }}
            <br>

            {# Display answer for a block of type choice and ref qbc-cb601cf6 #}
            Q11: WE'VE GOT YOUR RESULTS - #2 [multiple_choice]
            <br>
            {{ person|lookup:'ANSWER_BY_BLOCK-qbc-cb601cf6-YN5L9G' }}
            <br>
            </p>
            ```

    2. **Paste this code into an HTML block in a Klaviyo template.** Previewed as one of the quiz subscribers, it shows the full list of answers.

        ![The answers list code in the template](/images/how_to_shipifyv2_klaviyo_template_answerslist1.png)

    3. **If you want to show specific answers in your email template, you can copy parts of the code.**

        !!! example "Showing the answer to Q3, AGE GROUP"

            For example, you can use `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-dd744cf3-YN5L9G' }}` to  display the answer to Q3: AGE GROUP, whose reference is `qbc-dd744cf3`.

            To use it in a Klaviyo template text block:

            ![The answers list shown in a preview](/images/how_to_shipifyv2_klaviyo_template_answerslist2.png)

        !!! info "A sample answer object"

            To get the answer to one question:

            Quiz name: `{{ person|lookup:'QUIZ_NAME-YN5L9G' }}`

            First name: `{{ person.first_name }}`

            Last name: `{{ person.last_name }}`

            `Q2: BEFORE WE BEGIN`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbi-6c4248f5-YN5L9G' }}`

            `Q3: AGE GROUP`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-dd744cf3-YN5L9G' }}`

            `Q4: SKIN TYPE`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-485600ce-YN5L9G' }}`

            `Q9: SKIN CONCERNS`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-e8cf3180-YN5L9G' }}`

            `Q10: ALERGIES`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-329aaeff-YN5L9G' }}`

            `Q11: WE'VE GOT YOUR RESULTS - #1 [email]`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbi-29f016cf-YN5L9G' }}`

            `Q11: WE'VE GOT YOUR RESULTS - #2 [multiple_choice]`: `{{ person|lookup:'ANSWER_BY_BLOCK-qbc-cb601cf6-YN5L9G' }}`

    ### Example 3 - display link to quiz results

    Use the `RESPONSE_ID-QuizID` property to create a link to the quiz results page.

    The default link format adds `#response-{{ person|lookup:'RESPONSE_ID-QuizID' }}` to the end of the URL:

    !!! example "Linking to the quiz results"

        `<a href="https://yourwebsite.com/#response-{{ person|lookup:'RESPONSE_ID-Gli0KD' }}">View your quiz results</a>`

        Here, `Gli0KD` is the quiz ID and `{{ person|lookup:'RESPONSE_ID-Gli0KD' }}` fetches the dynamic response ID (for example, `eVgV0Y`).

    If Klaviyo tracking rewrites or loses the `#response-ID` fragment, the Built for Shopify version of the RevenueHunt quiz app also supports `response_id` as an alternative query parameter:

    !!! example "A tracked link using response_id"

        `<a href="https://yourwebsite.com/pages/quiz?response_id={{ person|lookup:'RESPONSE_ID-Gli0KD' }}">View your quiz results</a>`

    Replace the example URL with a storefront page where the **Link Popup Quiz** app embed is enabled. Normal Klaviyo click tracking can remain enabled for the query-parameter link. If the base URL already contains query parameters, append `&amp;response_id=...` instead of adding another `?`.

    For `#response-ID` links, adding `clicktracking="off"` to the `<a>` element can prevent Klaviyo from rewriting the link, but Klaviyo will not record click analytics for that link.




=== "Shopify (Legacy)"

    This example uses the quiz ID `dbqHqN`. Replace it with your own. Here is the code:

    ??? example "The basic slots template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example shows two things. You can print the custom properties the quiz sends to Klaviyo, and you can use `IF-ELSE` statements to show or hide content based on the answers.

    !!! note "Counting the products"

        When looping through the products, the **count starts at 0 (zero)**. To display the names of 3 products in a slot, write it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing).
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing).
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing).

    !!! warning "These templates will not work as they are"

        Unlike the template generated from the Connect > Klaviyo tab, these were written for a sample quiz, so they will not work as they are. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "WooCommerce"

    This example uses the quiz ID `dbqHqN`. Replace it with your own. Here is the code:

    ??? example "The basic slots template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example shows two things. You can print the custom properties the quiz sends to Klaviyo, and you can use `IF-ELSE` statements to show or hide content based on the answers.

    !!! note "Counting the products"

        When looping through the products, the **count starts at 0 (zero)**. To display the names of 3 products in a slot, write it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing).
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing).
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing).

    !!! warning "These templates will not work as they are"

        Unlike the template generated from the Connect > Klaviyo tab, these were written for a sample quiz, so they will not work as they are. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "Magento"

    This example uses the quiz ID `dbqHqN`. Replace it with your own. Here is the code:

    ??? example "The basic slots template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example shows two things. You can print the custom properties the quiz sends to Klaviyo, and you can use `IF-ELSE` statements to show or hide content based on the answers.

    !!! note "Counting the products"

        When looping through the products, the **count starts at 0 (zero)**. To display the names of 3 products in a slot, write it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing).
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing).
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing).

    !!! warning "These templates will not work as they are"

        Unlike the template generated from the Connect > Klaviyo tab, these were written for a sample quiz, so they will not work as they are. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "BigCommerce"

    This example uses the quiz ID `dbqHqN`. Replace it with your own. Here is the code:

    ??? example "The basic slots template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example shows two things. You can print the custom properties the quiz sends to Klaviyo, and you can use `IF-ELSE` statements to show or hide content based on the answers.

    !!! note "Counting the products"

        When looping through the products, the **count starts at 0 (zero)**. To display the names of 3 products in a slot, write it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing).
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing).
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing).

    !!! warning "These templates will not work as they are"

        Unlike the template generated from the Connect > Klaviyo tab, these were written for a sample quiz, so they will not work as they are. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

=== "Standalone"

    This example uses the quiz ID `dbqHqN`. Replace it with your own. Here is the code:

    ??? example "The basic slots template"

        ```html
        <h3>Hello {{ person|lookup:'Q-dbqHqN ZMiXjj: .Before we get started... what\'s your name?'|default:'' }}!</h3>
        <p>Here we are making sure the product exists:</p>
        {% if person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url' %}
        <p>Cleanser</p>
        <p><img alt="This is the cleanser image" src="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_image_url'|default:'' }}" /></p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_name'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_price'|default:'' }}</p>
        <p>{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_sku'|default:'' }}</p>
        <p><a href="{{ person|lookup:'SLOT-dbqHqN: Step 1: Cleanser - product_0_url'|default:'' }}">Buy now</a></p>
        {% endif %}
        {% if person|lookup:'T-dbqHqN: 40s' %}
        <p>You are in your forties</p>
        {% endif %}
        ```

    This example shows two things. You can print the custom properties the quiz sends to Klaviyo, and you can use `IF-ELSE` statements to show or hide content based on the answers.

    !!! note "Counting the products"

        When looping through the products, the **count starts at 0 (zero)**. To display the names of 3 products in a slot, write it like this:

            ```html
            <p>{{ person|lookup:'SLOT-dbqHqN - product_0_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_1_name'|default:'' }}</p>
            <p>{{ person|lookup:'SLOT-dbqHqN - product_2_name'|default:'' }}</p>
            ```

    Here are some other email templates that you can use as a reference:

    - [Basic Slots Template (4-Step Skincare Routine)](https://drive.google.com/file/d/1waa86eP6-Cd7GITOmXbFlvwDC9Nw0JsA/view?usp=sharing).
    - [Advanced Slots Template (Morning & Night Routine)](https://drive.google.com/file/d/1HawvV57Z2dma8XFWdRrmeh5DwGTcVyaM/view?usp=sharing).
    - [Products List Template (Coffee Recommendations)](https://drive.google.com/file/d/1x33l8q1LZuuzZcQ5F8vZAo8BXjywsGMO/view?usp=sharing).

    !!! warning "These templates will not work as they are"

        Unlike the template generated from the Connect > Klaviyo tab, these were written for a sample quiz, so they will not work as they are. Your developer will have to modify the `custom properties` to match the ones that are passed from the quiz to your Klaviyo account. The `quiz ID` is different, so are other property names.

### Pull product information from your catalog

=== "Shopify"

    Klaviyo's [Catalog Lookup Tag](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag) reads a product from the catalog Klaviyo already holds, given that product's id.

    Pass the product `id` from `RECOMMENDATIONS_BY_SLOT` instead of the `description` and `image` the quiz sends, and Klaviyo fills in the rest from the Shopify catalog it syncs.

=== "Shopify (Legacy)"

    Klaviyo's [Catalog Lookup Tag](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag) reads a product from the catalog Klaviyo already holds, given that product's id.

    Pass the product `id` from `PRODUCTS-[ID]` or `SLOT-[ID]` instead of the `description` and `image_url` the quiz sends, and Klaviyo fills in the rest from the Shopify catalog it syncs.

=== "WooCommerce"

    Klaviyo's [Catalog Lookup Tag](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag) reads a product from the catalog Klaviyo already holds, given that product's id.

    Pass the product `id` from `PRODUCTS-[ID]` or `SLOT-[ID]` instead of the `description` and `image_url` the quiz sends. This works only if your WooCommerce catalog is synced to Klaviyo.

=== "Magento"

    Klaviyo's [Catalog Lookup Tag](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag) reads a product from the catalog Klaviyo already holds, given that product's id.

    Pass the product `id` from `PRODUCTS-[ID]` or `SLOT-[ID]` instead of the `description` and `image_url` the quiz sends. This works only if your Magento catalog is synced to Klaviyo.

=== "BigCommerce"

    Klaviyo's [Catalog Lookup Tag](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag) reads a product from the catalog Klaviyo already holds, given that product's id.

    Pass the product `id` from `PRODUCTS-[ID]` or `SLOT-[ID]` instead of the `description` and `image_url` the quiz sends. This works only if your BigCommerce catalog is synced to Klaviyo.

=== "Standalone"

    Klaviyo's [Catalog Lookup Tag](https://help.klaviyo.com/hc/en-us/articles/360004785571-Overview-of-the-Catalog-Lookup-Tag) reads a product from the catalog Klaviyo already holds, given that product's id.

    A standalone quiz has no store catalog behind it, so there is nothing for Klaviyo to look up. Use the product fields the quiz sends.

## Disconnect Klaviyo

=== "Shopify"

    There are two ways to stop sending quiz data to Klaviyo: stop one quiz, or disconnect Klaviyo from your whole RevenueHunt account.

    **Option 1: Disconnect a single quiz**

    If you only want one specific quiz to stop sending data to Klaviyo (while other quizzes in your account keep working):

    1. **Open the [Quiz settings](/reference/quiz-builder/quiz-settings/) of the quiz you want to disconnect.**
    2. **Go to the `Integrations` tab, find the Klaviyo section, and uncheck the `Send Quiz Leads to Klaviyo Profiles` checkbox.**
    3. **Save your changes.**

    No more quiz data will flow from that specific quiz to Klaviyo. Other quizzes in your account will continue to send data normally.

    **Option 2: Disconnect Klaviyo from your entire RevenueHunt account**

    If you want to completely revoke the Klaviyo connection across your whole RevenueHunt account:

    1. **Open [Quiz settings](/reference/quiz-builder/quiz-settings/) and go to the [`Integrations`](/reference/quiz-builder/connect-integrations/) tab.**
    2. **Scroll to Klaviyo and click `Disconnect`.**
    3. **Confirm the action.**

    The change saves automatically, and no quiz in your account sends data to Klaviyo any more. To reconnect later, click `Connect` again and complete the OAuth flow.

=== "Shopify (Legacy)"

    In this version the Klaviyo connection is set on each quiz, so disconnecting one quiz leaves the others working.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**
    2. **Scroll to Klaviyo and click `Disconnect`.**
    3. **Publish the changes with the top-right `Publish` button.**

    That quiz stops sending contacts to Klaviyo. Contacts already in your Klaviyo account are not affected.

=== "WooCommerce"

    In this version the Klaviyo connection is set on each quiz, so disconnecting one quiz leaves the others working.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**
    2. **Scroll to Klaviyo and click `Disconnect`.**
    3. **Publish the changes with the top-right `Publish` button.**

    That quiz stops sending contacts to Klaviyo. Contacts already in your Klaviyo account are not affected.

=== "Magento"

    In this version the Klaviyo connection is set on each quiz, so disconnecting one quiz leaves the others working.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**
    2. **Scroll to Klaviyo and click `Disconnect`.**
    3. **Publish the changes with the top-right `Publish` button.**

    That quiz stops sending contacts to Klaviyo. Contacts already in your Klaviyo account are not affected.

=== "BigCommerce"

    In this version the Klaviyo connection is set on each quiz, so disconnecting one quiz leaves the others working.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**
    2. **Scroll to Klaviyo and click `Disconnect`.**
    3. **Publish the changes with the top-right `Publish` button.**

    That quiz stops sending contacts to Klaviyo. Contacts already in your Klaviyo account are not affected.

=== "Standalone"

    In this version the Klaviyo connection is set on each quiz, so disconnecting one quiz leaves the others working.

    1. **Open the [Quiz Builder](/reference/quiz-builder/) and go to the [`Connect`](/reference/quiz-builder/connect-integrations/) tab.**
    2. **Scroll to Klaviyo and click `Disconnect`.**
    3. **Publish the changes with the top-right `Publish` button.**

    That quiz stops sending contacts to Klaviyo. Contacts already in your Klaviyo account are not affected.

---
This article explains how to connect your quiz to Klaviyo, and how to build the follow-up email flow there.
