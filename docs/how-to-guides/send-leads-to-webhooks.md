---
description: "Learn how to send RevenueHunt quiz data to custom webhooks for automated data processing."
icon: material/webhook
---

# How to Send Leads to Webhooks

A webhook sends the full quiz data to any endpoint you choose: the answers, the recommended products and the customer's contact details.

This article explains how to link your quiz to a custom webhook, so another system can act on each response as it arrives.

!!! note "Before you start"

    You need:

    - A quiz in the RevenueHunt app to send the data from.
    - A webhook URL to receive the data. To test the feature, generate a temporary endpoint with a service such as [Webhook.site](https://webhook.site).

## Link quiz to webhooks

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/VE314AzvTbY?si=jCWb9ok0xAJAbTis" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Prepare your quiz**. Add every question you want, then open the [Quiz settings](/reference/quiz-builder/quiz-settings/).

    2. **Open the Webhooks integration**. Scroll to the [Integrations](/reference/quiz-builder/quiz-settings/#integrations) section and click `Webhooks`.

    3. **Add a webhook**. Click `+ Add Webhook`. You can use a service like [Webhook.site](https://webhook.site) to generate a temporary endpoint if you want to test the feature.

        ![how to webhook add](/images/how_to_shopifyv2_webhooks_add_webhook.png)

    4. **Enter the webhook URL**. Paste the generated URL into the field, and give the webhook a name such as `Skin Care Test Quiz`.

        ![how to webhook add](/images/how_to_shopifyv2_webhooks_connection.png)

    5. **Configure the webhook**. Toggle the options to choose which quiz data to send. You can also add HTTP headers as key-value pairs.

    6. **Save your changes**. Click `Save`.

    7. **Send a test webhook**. Click `Send Test` to trigger a sample payload, and check that your webhook receives it.

        ![how to webhook settings](/images/how_to_shopifyv2_webhooks_connection_successful.png)

    8. **Verify delivery**. Open your endpoint, such as Webhook.site, and confirm a POST request arrived. Check the JSON payload for the right quiz and customer data.

        ![how to webhook settings](/images/how_to_shopifyv2_webhooks_test_connection_result_post.png)

    9. **(Optional) Add more webhooks**. Click `+ Add Webhook` again for each extra URL, and repeat these steps.


=== "Shopify (Legacy)"

    To initiate the integration:

    1. **Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab of your quiz.**
    2. **Scroll to `Webhooks` and click `Connect`** to open the input field.
    3. **Paste your webhook URL into the new line.** It saves automatically.
    4. **Click the `...` menu next to the webhook entry and select `Test webhook`.**
    5. **Read the message the test returns.** What it says depends on how your webhook is configured.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. **If the test fails, work through the checks below.**
        - Check `Metrics -> Responses` for at least one response. If there are none, generate one by clicking `Preview`.
        - Check that the webhook URL is correct and active.

    7. **Configuring HTTP headers (optional)**: add HTTP headers when the receiving system expects them, or when you need them for security.

        1. **Click `+add new header`** once the connection test has passed.
        2. **Enter your HTTP headers.** They are sent with the quiz data in the POST request.

    8. **Activating your webhook**: use the toggle next to the webhook entry. The same toggle deactivates it later.

    From then on, the quiz sends all its data to your webhook URL in a POST request, headers included.

    ![how to webhook post](/images/how_to_webhook_post.png)

    To add another webhook, click `+add new webhook`, paste the new URL, then test and activate it the same way.

=== "WooCommerce"

    To initiate the integration:

    1. **Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab of your quiz.**
    2. **Scroll to `Webhooks` and click `Connect`** to open the input field.
    3. **Paste your webhook URL into the new line.** It saves automatically.
    4. **Click the `...` menu next to the webhook entry and select `Test webhook`.**
    5. **Read the message the test returns.** What it says depends on how your webhook is configured.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. **If the test fails, work through the checks below.**
        - Check `Metrics -> Responses` for at least one response. If there are none, generate one by clicking `Preview`.
        - Check that the webhook URL is correct and active.

    7. **Configuring HTTP headers (optional)**: add HTTP headers when the receiving system expects them, or when you need them for security.

        1. **Click `+add new header`** once the connection test has passed.
        2. **Enter your HTTP headers.** They are sent with the quiz data in the POST request.

    8. **Activating your webhook**: use the toggle next to the webhook entry. The same toggle deactivates it later.

    From then on, the quiz sends all its data to your webhook URL in a POST request, headers included.

    ![how to webhook post](/images/how_to_webhook_post.png)

    To add another webhook, click `+add new webhook`, paste the new URL, then test and activate it the same way.

=== "Magento"

    To initiate the integration:

    1. **Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab of your quiz.**
    2. **Scroll to `Webhooks` and click `Connect`** to open the input field.
    3. **Paste your webhook URL into the new line.** It saves automatically.
    4. **Click the `...` menu next to the webhook entry and select `Test webhook`.**
    5. **Read the message the test returns.** What it says depends on how your webhook is configured.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. **If the test fails, work through the checks below.**
        - Check `Metrics -> Responses` for at least one response. If there are none, generate one by clicking `Preview`.
        - Check that the webhook URL is correct and active.

    7. **Configuring HTTP headers (optional)**: add HTTP headers when the receiving system expects them, or when you need them for security.

        1. **Click `+add new header`** once the connection test has passed.
        2. **Enter your HTTP headers.** They are sent with the quiz data in the POST request.

    8. **Activating your webhook**: use the toggle next to the webhook entry. The same toggle deactivates it later.

    From then on, the quiz sends all its data to your webhook URL in a POST request, headers included.

    ![how to webhook post](/images/how_to_webhook_post.png)

    To add another webhook, click `+add new webhook`, paste the new URL, then test and activate it the same way.

=== "BigCommerce"

    To initiate the integration:

    1. **Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab of your quiz.**
    2. **Scroll to `Webhooks` and click `Connect`** to open the input field.
    3. **Paste your webhook URL into the new line.** It saves automatically.
    4. **Click the `...` menu next to the webhook entry and select `Test webhook`.**
    5. **Read the message the test returns.** What it says depends on how your webhook is configured.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. **If the test fails, work through the checks below.**
        - Check `Metrics -> Responses` for at least one response. If there are none, generate one by clicking `Preview`.
        - Check that the webhook URL is correct and active.

    7. **Configuring HTTP headers (optional)**: add HTTP headers when the receiving system expects them, or when you need them for security.

        1. **Click `+add new header`** once the connection test has passed.
        2. **Enter your HTTP headers.** They are sent with the quiz data in the POST request.

    8. **Activating your webhook**: use the toggle next to the webhook entry. The same toggle deactivates it later.

    From then on, the quiz sends all its data to your webhook URL in a POST request, headers included.

    ![how to webhook post](/images/how_to_webhook_post.png)

    To add another webhook, click `+add new webhook`, paste the new URL, then test and activate it the same way.

=== "Standalone"

    To initiate the integration:

    1. **Open the [`Connect`](/reference/quiz-builder/connect-integrations/) tab of your quiz.**
    2. **Scroll to `Webhooks` and click `Connect`** to open the input field.
    3. **Paste your webhook URL into the new line.** It saves automatically.
    4. **Click the `...` menu next to the webhook entry and select `Test webhook`.**
    5. **Read the message the test returns.** What it says depends on how your webhook is configured.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. **If the test fails, work through the checks below.**
        - Check `Metrics -> Responses` for at least one response. If there are none, generate one by clicking `Preview`.
        - Check that the webhook URL is correct and active.

    7. **Configuring HTTP headers (optional)**: add HTTP headers when the receiving system expects them, or when you need them for security.

        1. **Click `+add new header`** once the connection test has passed.
        2. **Enter your HTTP headers.** They are sent with the quiz data in the POST request.

    8. **Activating your webhook**: use the toggle next to the webhook entry. The same toggle deactivates it later.

    From then on, the quiz sends all its data to your webhook URL in a POST request, headers included.

    ![how to webhook post](/images/how_to_webhook_post.png)

    To add another webhook, click `+add new webhook`, paste the new URL, then test and activate it the same way.



## What data is sent to the webhook?

=== "Shopify"

    A webhook receives all of the quiz data:

    - The customer's name, email address and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    While setting up the webhook, toggle the available options to choose which data to send.

    ![how to webhook add](/images/how_to_shopifyv2_webhooks_connection.png)

    The data is sent as a JSON payload in a POST request, so another system can read it directly.

    ![how to webhook settings](/images/how_to_shopifyv2_webhooks_test_connection_result_post.png)

    !!! tip "Capture URL parameters in webhooks"
        Want to include UTM parameters or other URL data in your webhook? Use [custom JavaScript](/how-to-guides/add-javascript/) to set synthetic answers:
        ```javascript
        const urlParams = new URLSearchParams(window.location.search);
        actions.setAnswers({
          'hidden-utm-source': urlParams.get('utm_source') || '',
          'hidden-full-url': window.location.href
        });
        ```
        These values will appear in `answersByBlock` in your webhook payload.

    ??? example "Sample JSON payload for a skincare quiz"

        ```json
        {
          "responseId": "uB38Vp",
          "resultRef": "r-08450c04",
          "quizId": "3yS9Ky",
          "quizName": "Skincare Quiz (Basic)",
          "firstName": "Alex",
          "fullName": "Alex",
          "email": "alexa@revenuehunt.com",
          "answersByBlock": {
            "qbi-6c4248f5": {
              "type": "first_name",
              "value": "Alex",
              "choicesRefs": []
            },
            "qbc-dd744cf3": {
              "type": "multiple_choice",
              "value": "30's",
              "choicesRefs": [
                "qbcc-6671ad61"
              ]
            },
            "qbc-485600ce": {
              "type": "picture_choice",
              "value": "Not too oily and not too dry",
              "choicesRefs": [
                "qbcc-d6eca8f5"
              ]
            },
            "qbc-e8cf3180": {
              "type": "multiple_choice",
              "value": "Tight, flaky and dry skin, Fine lines and wrinkles and Hyperpigmentation and discoloration",
              "choicesRefs": [
                "qbcc-4b757ee6",
                "qbcc-f8ee8050",
                "qbcc-c9063062"
              ]
            },
            "qbc-329aaeff": {
              "type": "multiple_choice",
              "value": "Citrus Oils",
              "choicesRefs": [
                "qbcc-21ece637"
              ]
            },
            "qbi-29f016cf": {
              "type": "email",
              "value": "alexa@revenuehunt.com",
              "choicesRefs": []
            },
            "qbc-cb601cf6": {
              "type": "multiple_choice",
              "value": "I want to receive exclusive promos, custom skin and skincare tips and and more.",
              "choicesRefs": [
                "qbcc-102a66fc"
              ]
            }
          },
          "tags": [],
          "recommendationsBySlot": {
            "rsbss-bfeeade4": [
              {
                "id": "gid://shopify/Product/9207072948530",
                "title": "Organix Facial Moisturizer",
                "handle": "organix-facial-moisturizer",
                "vendor": "skincarequizstore",
                "variants": [
                  {
                    "id": "gid://shopify/ProductVariant/48355413492018",
                    "image": {
                      "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/age-moisturizer_1024x1024_2x_40012e11-78a7-408e-a10d-a839b05adcae.jpg?v=1713172689",
                      "altText": null
                    },
                    "price": {
                      "amount": 30,
                      "currencyCode": "USD"
                    },
                    "title": "Default Title"
                  }
                ],
                "dynamicMetafields": [],
                "type": "products",
                "image": {
                  "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/age-moisturizer_1024x1024_2x_40012e11-78a7-408e-a10d-a839b05adcae.jpg?v=1713172689",
                  "altText": null
                },
                "price": {
                  "amount": 30,
                  "currencyCode": "USD"
                }
              },
              {
                "id": "gid://shopify/Product/9207079534898",
                "title": "Vitamin C Serum",
                "handle": "vitamin-c-serum",
                "vendor": "skincarequizstore",
                "variants": [
                  {
                    "id": "gid://shopify/ProductVariant/48355422863666",
                    "image": {
                      "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/Screenshot2024-04-15112220.png?v=1713172967",
                      "altText": null
                    },
                    "price": {
                      "amount": 42,
                      "currencyCode": "USD"
                    },
                    "title": "Default Title"
                  }
                ],
                "dynamicMetafields": [
                  {
                    "key": "description",
                    "value": "This is a description",
                    "namespace": "custom"
                  }
                ],
                "type": "products",
                "image": {
                  "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/Screenshot2024-04-15112220.png?v=1713172967",
                  "altText": null
                },
                "price": {
                  "amount": 42,
                  "currencyCode": "USD"
                }
              },
              {
                "id": "gid://shopify/Product/9207069933874",
                "title": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                "handle": "the-ordinary-buffet-copper-peptides-1",
                "vendor": "skincarequizstore",
                "variants": [
                  {
                    "id": "gid://shopify/ProductVariant/48355410510130",
                    "image": {
                      "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/oily-serum_1024x1024_2x_d2d2cf84-cb98-4a86-b14c-9982d2b244a7.jpg?v=1713172560",
                      "altText": null
                    },
                    "price": {
                      "amount": 36,
                      "currencyCode": "USD"
                    },
                    "title": "Default Title"
                  }
                ],
                "dynamicMetafields": [],
                "type": "products",
                "image": {
                  "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/oily-serum_1024x1024_2x_d2d2cf84-cb98-4a86-b14c-9982d2b244a7.jpg?v=1713172560",
                  "altText": null
                },
                "price": {
                  "amount": 36,
                  "currencyCode": "USD"
                }
              },
              {
                "id": "gid://shopify/Product/9083881423154",
                "title": "Aloe Soothing Toner",
                "handle": "aloe-soothing-moist-toner",
                "vendor": "skincarequizstore",
                "variants": [
                  {
                    "id": "gid://shopify/ProductVariant/47940967334194",
                    "image": {
                      "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-green-lg_1024x1024_2x_ac1c442d-01b1-46aa-85d8-5bd28cb8434b.jpg?v=1709729891",
                      "altText": null
                    },
                    "price": {
                      "amount": 24,
                      "currencyCode": "USD"
                    },
                    "title": "Green"
                  },
                  {
                    "id": "gid://shopify/ProductVariant/47940967366962",
                    "image": {
                      "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-red-lg_1024x1024_2x_9c6061c1-7214-42e4-8dc7-bbb3a2f4ef4e.jpg?v=1709729901",
                      "altText": null
                    },
                    "price": {
                      "amount": 24,
                      "currencyCode": "USD"
                    },
                    "title": "Red"
                  },
                  {
                    "id": "gid://shopify/ProductVariant/47940967399730",
                    "image": {
                      "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-blue-lg_1024x1024_2x_18d2fc63-3f85-4660-bd56-8725ae651a77.jpg?v=1709729914",
                      "altText": null
                    },
                    "price": {
                      "amount": 24,
                      "currencyCode": "USD"
                    },
                    "title": "Blue"
                  }
                ],
                "dynamicMetafields": [],
                "type": "products",
                "image": {
                  "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-blue-lg_1024x1024_2x_b5666a02-7579-445c-aec3-6edd0eb0e909.jpg?v=1709729938",
                  "altText": null
                },
                "price": {
                  "amount": 24,
                  "currencyCode": "USD"
                }
              }
            ]
          },
          "variableScores": {
            "score": 0
          },
          "createdAt": "2025-07-10 14:22:34 UTC",
          "resultSections": [
            {
              "ref": "rs-f8409d3d",
              "blocks": [
                {
                  "ref": "rsbh-9829ca60",
                  "type": "heading",
                  "content": "<p>Your results are in!</p>"
                },
                {
                  "ref": "rsbt-ee9d95f5",
                  "type": "text",
                  "content": "<p>Please write a brief introductory text to explain why these recommended products are the perfect match for them.</p>"
                },
                {
                  "ref": "rsbs-023d3ae5",
                  "type": "products",
                  "slots": [
                    {
                      "ref": "rsbss-bfeeade4",
                      "items": [
                        {
                          "id": "gid://shopify/Product/9207072948530",
                          "title": "Organix Facial Moisturizer",
                          "handle": "organix-facial-moisturizer",
                          "vendor": "skincarequizstore",
                          "variants": [
                            {
                              "id": "gid://shopify/ProductVariant/48355413492018",
                              "image": {
                                "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/age-moisturizer_1024x1024_2x_40012e11-78a7-408e-a10d-a839b05adcae.jpg?v=1713172689",
                                "altText": null
                              },
                              "price": {
                                "amount": 30,
                                "currencyCode": "USD"
                              },
                              "title": "Default Title"
                            }
                          ],
                          "dynamicMetafields": [],
                          "type": "products",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/age-moisturizer_1024x1024_2x_40012e11-78a7-408e-a10d-a839b05adcae.jpg?v=1713172689",
                            "altText": null
                          },
                          "price": {
                            "amount": 30,
                            "currencyCode": "USD"
                          }
                        },
                        {
                          "id": "gid://shopify/Product/9207079534898",
                          "title": "Vitamin C Serum",
                          "handle": "vitamin-c-serum",
                          "vendor": "skincarequizstore",
                          "variants": [
                            {
                              "id": "gid://shopify/ProductVariant/48355422863666",
                              "image": {
                                "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/Screenshot2024-04-15112220.png?v=1713172967",
                                "altText": null
                              },
                              "price": {
                                "amount": 42,
                                "currencyCode": "USD"
                              },
                              "title": "Default Title"
                            }
                          ],
                          "dynamicMetafields": [
                            {
                              "key": "description",
                              "value": "This is a description",
                              "namespace": "custom"
                            }
                          ],
                          "type": "products",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/Screenshot2024-04-15112220.png?v=1713172967",
                            "altText": null
                          },
                          "price": {
                            "amount": 42,
                            "currencyCode": "USD"
                          }
                        },
                        {
                          "id": "gid://shopify/Product/9207069933874",
                          "title": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                          "handle": "the-ordinary-buffet-copper-peptides-1",
                          "vendor": "skincarequizstore",
                          "variants": [
                            {
                              "id": "gid://shopify/ProductVariant/48355410510130",
                              "image": {
                                "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/oily-serum_1024x1024_2x_d2d2cf84-cb98-4a86-b14c-9982d2b244a7.jpg?v=1713172560",
                                "altText": null
                              },
                              "price": {
                                "amount": 36,
                                "currencyCode": "USD"
                              },
                              "title": "Default Title"
                            }
                          ],
                          "dynamicMetafields": [],
                          "type": "products",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/oily-serum_1024x1024_2x_d2d2cf84-cb98-4a86-b14c-9982d2b244a7.jpg?v=1713172560",
                            "altText": null
                          },
                          "price": {
                            "amount": 36,
                            "currencyCode": "USD"
                          }
                        },
                        {
                          "id": "gid://shopify/Product/9083881423154",
                          "title": "Aloe Soothing Toner",
                          "handle": "aloe-soothing-moist-toner",
                          "vendor": "skincarequizstore",
                          "variants": [
                            {
                              "id": "gid://shopify/ProductVariant/47940967334194",
                              "image": {
                                "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-green-lg_1024x1024_2x_ac1c442d-01b1-46aa-85d8-5bd28cb8434b.jpg?v=1709729891",
                                "altText": null
                              },
                              "price": {
                                "amount": 24,
                                "currencyCode": "USD"
                              },
                              "title": "Green"
                            },
                            {
                              "id": "gid://shopify/ProductVariant/47940967366962",
                              "image": {
                                "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-red-lg_1024x1024_2x_9c6061c1-7214-42e4-8dc7-bbb3a2f4ef4e.jpg?v=1709729901",
                                "altText": null
                              },
                              "price": {
                                "amount": 24,
                                "currencyCode": "USD"
                              },
                              "title": "Red"
                            },
                            {
                              "id": "gid://shopify/ProductVariant/47940967399730",
                              "image": {
                                "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-blue-lg_1024x1024_2x_18d2fc63-3f85-4660-bd56-8725ae651a77.jpg?v=1709729914",
                                "altText": null
                              },
                              "price": {
                                "amount": 24,
                                "currencyCode": "USD"
                              },
                              "title": "Blue"
                            }
                          ],
                          "dynamicMetafields": [],
                          "type": "products",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-blue-lg_1024x1024_2x_b5666a02-7579-445c-aec3-6edd0eb0e909.jpg?v=1709729938",
                            "altText": null
                          },
                          "price": {
                            "amount": 24,
                            "currencyCode": "USD"
                          }
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ],
          "resultContentByBlock": {
            "rsbh-9829ca60": {
              "type": "heading",
              "content": "<p>Your results are in!</p>"
            },
            "rsbt-ee9d95f5": {
              "type": "text",
              "content": "<p>Please write a brief introductory text to explain why these recommended products are the perfect match for them.</p>"
            },
            "rsbs-023d3ae5": {
              "type": "products",
              "slots": {
                "rsbss-bfeeade4": {
                  "items": [
                    {
                      "id": "gid://shopify/Product/9207072948530",
                      "title": "Organix Facial Moisturizer",
                      "handle": "organix-facial-moisturizer",
                      "vendor": "skincarequizstore",
                      "variants": [
                        {
                          "id": "gid://shopify/ProductVariant/48355413492018",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/age-moisturizer_1024x1024_2x_40012e11-78a7-408e-a10d-a839b05adcae.jpg?v=1713172689",
                            "altText": null
                          },
                          "price": {
                            "amount": 30,
                            "currencyCode": "USD"
                          },
                          "title": "Default Title"
                        }
                      ],
                      "dynamicMetafields": [],
                      "type": "products",
                      "image": {
                        "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/age-moisturizer_1024x1024_2x_40012e11-78a7-408e-a10d-a839b05adcae.jpg?v=1713172689",
                        "altText": null
                      },
                      "price": {
                        "amount": 30,
                        "currencyCode": "USD"
                      }
                    },
                    {
                      "id": "gid://shopify/Product/9207079534898",
                      "title": "Vitamin C Serum",
                      "handle": "vitamin-c-serum",
                      "vendor": "skincarequizstore",
                      "variants": [
                        {
                          "id": "gid://shopify/ProductVariant/48355422863666",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/Screenshot2024-04-15112220.png?v=1713172967",
                            "altText": null
                          },
                          "price": {
                            "amount": 42,
                            "currencyCode": "USD"
                          },
                          "title": "Default Title"
                        }
                      ],
                      "dynamicMetafields": [
                        {
                          "key": "description",
                          "value": "This is a description",
                          "namespace": "custom"
                        }
                      ],
                      "type": "products",
                      "image": {
                        "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/Screenshot2024-04-15112220.png?v=1713172967",
                        "altText": null
                      },
                      "price": {
                        "amount": 42,
                        "currencyCode": "USD"
                      }
                    },
                    {
                      "id": "gid://shopify/Product/9207069933874",
                      "title": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                      "handle": "the-ordinary-buffet-copper-peptides-1",
                      "vendor": "skincarequizstore",
                      "variants": [
                        {
                          "id": "gid://shopify/ProductVariant/48355410510130",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/oily-serum_1024x1024_2x_d2d2cf84-cb98-4a86-b14c-9982d2b244a7.jpg?v=1713172560",
                            "altText": null
                          },
                          "price": {
                            "amount": 36,
                            "currencyCode": "USD"
                          },
                          "title": "Default Title"
                        }
                      ],
                      "dynamicMetafields": [],
                      "type": "products",
                      "image": {
                        "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/oily-serum_1024x1024_2x_d2d2cf84-cb98-4a86-b14c-9982d2b244a7.jpg?v=1713172560",
                        "altText": null
                      },
                      "price": {
                        "amount": 36,
                        "currencyCode": "USD"
                      }
                    },
                    {
                      "id": "gid://shopify/Product/9083881423154",
                      "title": "Aloe Soothing Toner",
                      "handle": "aloe-soothing-moist-toner",
                      "vendor": "skincarequizstore",
                      "variants": [
                        {
                          "id": "gid://shopify/ProductVariant/47940967334194",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-green-lg_1024x1024_2x_ac1c442d-01b1-46aa-85d8-5bd28cb8434b.jpg?v=1709729891",
                            "altText": null
                          },
                          "price": {
                            "amount": 24,
                            "currencyCode": "USD"
                          },
                          "title": "Green"
                        },
                        {
                          "id": "gid://shopify/ProductVariant/47940967366962",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-red-lg_1024x1024_2x_9c6061c1-7214-42e4-8dc7-bbb3a2f4ef4e.jpg?v=1709729901",
                            "altText": null
                          },
                          "price": {
                            "amount": 24,
                            "currencyCode": "USD"
                          },
                          "title": "Red"
                        },
                        {
                          "id": "gid://shopify/ProductVariant/47940967399730",
                          "image": {
                            "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-blue-lg_1024x1024_2x_18d2fc63-3f85-4660-bd56-8725ae651a77.jpg?v=1709729914",
                            "altText": null
                          },
                          "price": {
                            "amount": 24,
                            "currencyCode": "USD"
                          },
                          "title": "Blue"
                        }
                      ],
                      "dynamicMetafields": [],
                      "type": "products",
                      "image": {
                        "url": "https://cdn.shopify.com/s/files/1/0856/7652/3826/files/aloe-blue-lg_1024x1024_2x_b5666a02-7579-445c-aec3-6edd0eb0e909.jpg?v=1709729938",
                        "altText": null
                      },
                      "price": {
                        "amount": 24,
                        "currencyCode": "USD"
                      }
                    }
                  ]
                }
              }
            }
          }
        }
        ```


=== "Shopify (Legacy)"

    A webhook receives all of the quiz data:

    - The customer's name, email address and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    The data is sent as a JSON payload in a POST request, so another system can read it directly.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    ??? example "Sample JSON payload for a skincare quiz"

        ```json
        {
          "quiz_name": "Skincare Quiz (Basic Routine)",
          "quiz_id": "dbqHqN",
          "response_id": "NLTqvGqg",
          "first_name": "Paulina",
          "full_name": "Paulina",
          "email": "paulina@revenuehunt.fake",
          "emails": [
            "paulina@revenuehunt.fake"
          ],
          "products": [
            {
              "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
              "score": 2.102760090909091,
              "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
              "price": "27.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
              "position": 0,
              "sku": "RHSK-016",
              "id": 4095078301780,
              "variant_id": 30099568885844
            },
            {
              "name": "Organix Facial Moisturizer",
              "score": 2.1020920909090908,
              "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
              "price": "36.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
              "position": 1,
              "sku": "RHSK-012",
              "id": 4095721668692,
              "variant_id": 30104418451540
            },
            {
              "name": "All Natural Face Cleanser",
              "score": 2.101927090909091,
              "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
              "price": "32.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
              "position": 2,
              "sku": "RHSK-001",
              "id": 4095717834836,
              "variant_id": 30104403476564
            },
            {
              "name": "Fresh Rose Deep Hydration Toner",
              "score": 1.1010830909090907,
              "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
              "price": "48.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
              "position": 3,
              "sku": "RHSK-006",
              "id": 4095053168724,
              "variant_id": 30099364773972
            }
          ],
          "blocks": [
            {
              "id": "Q2wTvD",
              "type": "HeadingBlock",
              "position": 0,
              "content": "{{slide:ZMiXjj}}, here's what your skin wants!"
            },
            {
              "id": "Qm0T1V",
              "type": "ContentBlock",
              "position": 1,
              "content": "Applying your skin care products in the proper order ensures that your skin receives the full benefits of each product.↵↵Enter this coupon code at checkout to get a 10% discount:↵**QUIZ123**↵↵"
            },
            {
              "id": "Qp7T9x",
              "type": "SlotsBlock",
              "position": 2,
              "slots": [
                {
                  "id": "NXGuwK",
                  "title": "Step 1: Cleanser",
                  "position": 0,
                  "products": [
                    {
                      "name": "All Natural Face Cleanser",
                      "id": 4095717834836,
                      "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
                      "price": "32.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
                      "sku": "RHSK-001",
                      "variant_id": 30104403476564,
                      "position": 0,
                      "score": 2.101927090909091
                    }
                  ]
                },
                {
                  "id": "RV6u0R",
                  "title": "Step 2: Toner",
                  "position": 1,
                  "products": [
                    {
                      "name": "Fresh Rose Deep Hydration Toner",
                      "id": 4095053168724,
                      "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
                      "price": "48.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
                      "sku": "RHSK-006",
                      "variant_id": 30099364773972,
                      "position": 0,
                      "score": 1.1010830909090907
                    }
                  ]
                },
                {
                  "id": "K6MuvR",
                  "title": "Step 3: Serum",
                  "position": 2,
                  "products": [
                    {
                      "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                      "id": 4095078301780,
                      "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
                      "price": "27.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
                      "sku": "RHSK-016",
                      "variant_id": 30099568885844,
                      "position": 0,
                      "score": 2.102760090909091
                    }
                  ]
                },
                {
                  "id": "9OJulN",
                  "title": "Step 4: Moisturizer",
                  "position": 3,
                  "products": [
                    {
                      "name": "Organix Facial Moisturizer",
                      "id": 4095721668692,
                      "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
                      "price": "36.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
                      "sku": "RHSK-012",
                      "variant_id": 30104418451540,
                      "position": 0,
                      "score": 2.1020920909090908
                    }
                  ]
                }
              ]
            }
          ],
          "answers": [
            {
              "question_title": "Leave us your email to receive an exclusive 10% discount on your next purchase:",
              "question_id": "KGQi5e",
              "values": [
                "paulina@revenuehunt.fake"
              ]
            },
            {
              "question_title": "Is your skin sensitive to any of the following ingredients?",
              "question_id": "yYqiz5",
              "choice_label": "Witch Hazel"
            },
            {
              "question_title": "Which of the following best describes the climate in which you live?",
              "question_id": "pa2i8L",
              "choice_label": "Desert or High Altitude"
            },
            {
              "question_title": "What is your main skin concern?",
              "question_id": "ydDimb",
              "choice_label": "Fine lines and wrinkles"
            },
            {
              "question_title": "How does your skin feel on an average day?",
              "question_id": "K72iWW",
              "choice_label": "Dry and tight all over"
            },
            {
              "question_title": "Pleased to meet you {{slide:ZMiXjj}}, what is your age?",
              "question_id": "p5Vi02",
              "choice_label": "40's"
            },
            {
              "question_title": "Before we get started... what's your name?",
              "question_id": "ZMiXjj",
              "values": [
                "Paulina"
              ]
            }
          ],
          "tags": [
            "sensitive_witch_hazel",
            "desert_area",
            "fine_lines",
            "dry_skin",
            "40s"
          ],
          "permalink": "https://skincarequiz.myshopify.com/#results-dbqHqN-NLTqvGqg",
          "permalink_hash": "#results-dbqHqN-NLTqvGqg",
          "created_at": "2022-07-15T13:18:30Z"
        }
        ```

=== "WooCommerce"

    A webhook receives all of the quiz data:

    - The customer's name, email address and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    The data is sent as a JSON payload in a POST request, so another system can read it directly.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    ??? example "Sample JSON payload for a skincare quiz"

        ```json
        {
          "quiz_name": "Skincare Quiz (Basic Routine)",
          "quiz_id": "dbqHqN",
          "response_id": "NLTqvGqg",
          "first_name": "Paulina",
          "full_name": "Paulina",
          "email": "paulina@revenuehunt.fake",
          "emails": [
            "paulina@revenuehunt.fake"
          ],
          "products": [
            {
              "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
              "score": 2.102760090909091,
              "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
              "price": "27.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
              "position": 0,
              "sku": "RHSK-016",
              "id": 4095078301780,
              "variant_id": 30099568885844
            },
            {
              "name": "Organix Facial Moisturizer",
              "score": 2.1020920909090908,
              "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
              "price": "36.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
              "position": 1,
              "sku": "RHSK-012",
              "id": 4095721668692,
              "variant_id": 30104418451540
            },
            {
              "name": "All Natural Face Cleanser",
              "score": 2.101927090909091,
              "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
              "price": "32.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
              "position": 2,
              "sku": "RHSK-001",
              "id": 4095717834836,
              "variant_id": 30104403476564
            },
            {
              "name": "Fresh Rose Deep Hydration Toner",
              "score": 1.1010830909090907,
              "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
              "price": "48.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
              "position": 3,
              "sku": "RHSK-006",
              "id": 4095053168724,
              "variant_id": 30099364773972
            }
          ],
          "blocks": [
            {
              "id": "Q2wTvD",
              "type": "HeadingBlock",
              "position": 0,
              "content": "{{slide:ZMiXjj}}, here's what your skin wants!"
            },
            {
              "id": "Qm0T1V",
              "type": "ContentBlock",
              "position": 1,
              "content": "Applying your skin care products in the proper order ensures that your skin receives the full benefits of each product.↵↵Enter this coupon code at checkout to get a 10% discount:↵**QUIZ123**↵↵"
            },
            {
              "id": "Qp7T9x",
              "type": "SlotsBlock",
              "position": 2,
              "slots": [
                {
                  "id": "NXGuwK",
                  "title": "Step 1: Cleanser",
                  "position": 0,
                  "products": [
                    {
                      "name": "All Natural Face Cleanser",
                      "id": 4095717834836,
                      "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
                      "price": "32.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
                      "sku": "RHSK-001",
                      "variant_id": 30104403476564,
                      "position": 0,
                      "score": 2.101927090909091
                    }
                  ]
                },
                {
                  "id": "RV6u0R",
                  "title": "Step 2: Toner",
                  "position": 1,
                  "products": [
                    {
                      "name": "Fresh Rose Deep Hydration Toner",
                      "id": 4095053168724,
                      "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
                      "price": "48.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
                      "sku": "RHSK-006",
                      "variant_id": 30099364773972,
                      "position": 0,
                      "score": 1.1010830909090907
                    }
                  ]
                },
                {
                  "id": "K6MuvR",
                  "title": "Step 3: Serum",
                  "position": 2,
                  "products": [
                    {
                      "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                      "id": 4095078301780,
                      "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
                      "price": "27.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
                      "sku": "RHSK-016",
                      "variant_id": 30099568885844,
                      "position": 0,
                      "score": 2.102760090909091
                    }
                  ]
                },
                {
                  "id": "9OJulN",
                  "title": "Step 4: Moisturizer",
                  "position": 3,
                  "products": [
                    {
                      "name": "Organix Facial Moisturizer",
                      "id": 4095721668692,
                      "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
                      "price": "36.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
                      "sku": "RHSK-012",
                      "variant_id": 30104418451540,
                      "position": 0,
                      "score": 2.1020920909090908
                    }
                  ]
                }
              ]
            }
          ],
          "answers": [
            {
              "question_title": "Leave us your email to receive an exclusive 10% discount on your next purchase:",
              "question_id": "KGQi5e",
              "values": [
                "paulina@revenuehunt.fake"
              ]
            },
            {
              "question_title": "Is your skin sensitive to any of the following ingredients?",
              "question_id": "yYqiz5",
              "choice_label": "Witch Hazel"
            },
            {
              "question_title": "Which of the following best describes the climate in which you live?",
              "question_id": "pa2i8L",
              "choice_label": "Desert or High Altitude"
            },
            {
              "question_title": "What is your main skin concern?",
              "question_id": "ydDimb",
              "choice_label": "Fine lines and wrinkles"
            },
            {
              "question_title": "How does your skin feel on an average day?",
              "question_id": "K72iWW",
              "choice_label": "Dry and tight all over"
            },
            {
              "question_title": "Pleased to meet you {{slide:ZMiXjj}}, what is your age?",
              "question_id": "p5Vi02",
              "choice_label": "40's"
            },
            {
              "question_title": "Before we get started... what's your name?",
              "question_id": "ZMiXjj",
              "values": [
                "Paulina"
              ]
            }
          ],
          "tags": [
            "sensitive_witch_hazel",
            "desert_area",
            "fine_lines",
            "dry_skin",
            "40s"
          ],
          "permalink": "https://skincarequiz.myshopify.com/#results-dbqHqN-NLTqvGqg",
          "permalink_hash": "#results-dbqHqN-NLTqvGqg",
          "created_at": "2022-07-15T13:18:30Z"
        }
        ```

=== "Magento"

    A webhook receives all of the quiz data:

    - The customer's name, email address and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    The data is sent as a JSON payload in a POST request, so another system can read it directly.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    ??? example "Sample JSON payload for a skincare quiz"

        ```json
        {
          "quiz_name": "Skincare Quiz (Basic Routine)",
          "quiz_id": "dbqHqN",
          "response_id": "NLTqvGqg",
          "first_name": "Paulina",
          "full_name": "Paulina",
          "email": "paulina@revenuehunt.fake",
          "emails": [
            "paulina@revenuehunt.fake"
          ],
          "products": [
            {
              "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
              "score": 2.102760090909091,
              "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
              "price": "27.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
              "position": 0,
              "sku": "RHSK-016",
              "id": 4095078301780,
              "variant_id": 30099568885844
            },
            {
              "name": "Organix Facial Moisturizer",
              "score": 2.1020920909090908,
              "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
              "price": "36.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
              "position": 1,
              "sku": "RHSK-012",
              "id": 4095721668692,
              "variant_id": 30104418451540
            },
            {
              "name": "All Natural Face Cleanser",
              "score": 2.101927090909091,
              "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
              "price": "32.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
              "position": 2,
              "sku": "RHSK-001",
              "id": 4095717834836,
              "variant_id": 30104403476564
            },
            {
              "name": "Fresh Rose Deep Hydration Toner",
              "score": 1.1010830909090907,
              "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
              "price": "48.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
              "position": 3,
              "sku": "RHSK-006",
              "id": 4095053168724,
              "variant_id": 30099364773972
            }
          ],
          "blocks": [
            {
              "id": "Q2wTvD",
              "type": "HeadingBlock",
              "position": 0,
              "content": "{{slide:ZMiXjj}}, here's what your skin wants!"
            },
            {
              "id": "Qm0T1V",
              "type": "ContentBlock",
              "position": 1,
              "content": "Applying your skin care products in the proper order ensures that your skin receives the full benefits of each product.↵↵Enter this coupon code at checkout to get a 10% discount:↵**QUIZ123**↵↵"
            },
            {
              "id": "Qp7T9x",
              "type": "SlotsBlock",
              "position": 2,
              "slots": [
                {
                  "id": "NXGuwK",
                  "title": "Step 1: Cleanser",
                  "position": 0,
                  "products": [
                    {
                      "name": "All Natural Face Cleanser",
                      "id": 4095717834836,
                      "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
                      "price": "32.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
                      "sku": "RHSK-001",
                      "variant_id": 30104403476564,
                      "position": 0,
                      "score": 2.101927090909091
                    }
                  ]
                },
                {
                  "id": "RV6u0R",
                  "title": "Step 2: Toner",
                  "position": 1,
                  "products": [
                    {
                      "name": "Fresh Rose Deep Hydration Toner",
                      "id": 4095053168724,
                      "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
                      "price": "48.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
                      "sku": "RHSK-006",
                      "variant_id": 30099364773972,
                      "position": 0,
                      "score": 1.1010830909090907
                    }
                  ]
                },
                {
                  "id": "K6MuvR",
                  "title": "Step 3: Serum",
                  "position": 2,
                  "products": [
                    {
                      "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                      "id": 4095078301780,
                      "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
                      "price": "27.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
                      "sku": "RHSK-016",
                      "variant_id": 30099568885844,
                      "position": 0,
                      "score": 2.102760090909091
                    }
                  ]
                },
                {
                  "id": "9OJulN",
                  "title": "Step 4: Moisturizer",
                  "position": 3,
                  "products": [
                    {
                      "name": "Organix Facial Moisturizer",
                      "id": 4095721668692,
                      "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
                      "price": "36.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
                      "sku": "RHSK-012",
                      "variant_id": 30104418451540,
                      "position": 0,
                      "score": 2.1020920909090908
                    }
                  ]
                }
              ]
            }
          ],
          "answers": [
            {
              "question_title": "Leave us your email to receive an exclusive 10% discount on your next purchase:",
              "question_id": "KGQi5e",
              "values": [
                "paulina@revenuehunt.fake"
              ]
            },
            {
              "question_title": "Is your skin sensitive to any of the following ingredients?",
              "question_id": "yYqiz5",
              "choice_label": "Witch Hazel"
            },
            {
              "question_title": "Which of the following best describes the climate in which you live?",
              "question_id": "pa2i8L",
              "choice_label": "Desert or High Altitude"
            },
            {
              "question_title": "What is your main skin concern?",
              "question_id": "ydDimb",
              "choice_label": "Fine lines and wrinkles"
            },
            {
              "question_title": "How does your skin feel on an average day?",
              "question_id": "K72iWW",
              "choice_label": "Dry and tight all over"
            },
            {
              "question_title": "Pleased to meet you {{slide:ZMiXjj}}, what is your age?",
              "question_id": "p5Vi02",
              "choice_label": "40's"
            },
            {
              "question_title": "Before we get started... what's your name?",
              "question_id": "ZMiXjj",
              "values": [
                "Paulina"
              ]
            }
          ],
          "tags": [
            "sensitive_witch_hazel",
            "desert_area",
            "fine_lines",
            "dry_skin",
            "40s"
          ],
          "permalink": "https://skincarequiz.myshopify.com/#results-dbqHqN-NLTqvGqg",
          "permalink_hash": "#results-dbqHqN-NLTqvGqg",
          "created_at": "2022-07-15T13:18:30Z"
        }
        ```

=== "BigCommerce"

    A webhook receives all of the quiz data:

    - The customer's name, email address and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    The data is sent as a JSON payload in a POST request, so another system can read it directly.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    ??? example "Sample JSON payload for a skincare quiz"

        ```json
        {
          "quiz_name": "Skincare Quiz (Basic Routine)",
          "quiz_id": "dbqHqN",
          "response_id": "NLTqvGqg",
          "first_name": "Paulina",
          "full_name": "Paulina",
          "email": "paulina@revenuehunt.fake",
          "emails": [
            "paulina@revenuehunt.fake"
          ],
          "products": [
            {
              "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
              "score": 2.102760090909091,
              "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
              "price": "27.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
              "position": 0,
              "sku": "RHSK-016",
              "id": 4095078301780,
              "variant_id": 30099568885844
            },
            {
              "name": "Organix Facial Moisturizer",
              "score": 2.1020920909090908,
              "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
              "price": "36.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
              "position": 1,
              "sku": "RHSK-012",
              "id": 4095721668692,
              "variant_id": 30104418451540
            },
            {
              "name": "All Natural Face Cleanser",
              "score": 2.101927090909091,
              "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
              "price": "32.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
              "position": 2,
              "sku": "RHSK-001",
              "id": 4095717834836,
              "variant_id": 30104403476564
            },
            {
              "name": "Fresh Rose Deep Hydration Toner",
              "score": 1.1010830909090907,
              "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
              "price": "48.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
              "position": 3,
              "sku": "RHSK-006",
              "id": 4095053168724,
              "variant_id": 30099364773972
            }
          ],
          "blocks": [
            {
              "id": "Q2wTvD",
              "type": "HeadingBlock",
              "position": 0,
              "content": "{{slide:ZMiXjj}}, here's what your skin wants!"
            },
            {
              "id": "Qm0T1V",
              "type": "ContentBlock",
              "position": 1,
              "content": "Applying your skin care products in the proper order ensures that your skin receives the full benefits of each product.↵↵Enter this coupon code at checkout to get a 10% discount:↵**QUIZ123**↵↵"
            },
            {
              "id": "Qp7T9x",
              "type": "SlotsBlock",
              "position": 2,
              "slots": [
                {
                  "id": "NXGuwK",
                  "title": "Step 1: Cleanser",
                  "position": 0,
                  "products": [
                    {
                      "name": "All Natural Face Cleanser",
                      "id": 4095717834836,
                      "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
                      "price": "32.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
                      "sku": "RHSK-001",
                      "variant_id": 30104403476564,
                      "position": 0,
                      "score": 2.101927090909091
                    }
                  ]
                },
                {
                  "id": "RV6u0R",
                  "title": "Step 2: Toner",
                  "position": 1,
                  "products": [
                    {
                      "name": "Fresh Rose Deep Hydration Toner",
                      "id": 4095053168724,
                      "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
                      "price": "48.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
                      "sku": "RHSK-006",
                      "variant_id": 30099364773972,
                      "position": 0,
                      "score": 1.1010830909090907
                    }
                  ]
                },
                {
                  "id": "K6MuvR",
                  "title": "Step 3: Serum",
                  "position": 2,
                  "products": [
                    {
                      "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                      "id": 4095078301780,
                      "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
                      "price": "27.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
                      "sku": "RHSK-016",
                      "variant_id": 30099568885844,
                      "position": 0,
                      "score": 2.102760090909091
                    }
                  ]
                },
                {
                  "id": "9OJulN",
                  "title": "Step 4: Moisturizer",
                  "position": 3,
                  "products": [
                    {
                      "name": "Organix Facial Moisturizer",
                      "id": 4095721668692,
                      "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
                      "price": "36.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
                      "sku": "RHSK-012",
                      "variant_id": 30104418451540,
                      "position": 0,
                      "score": 2.1020920909090908
                    }
                  ]
                }
              ]
            }
          ],
          "answers": [
            {
              "question_title": "Leave us your email to receive an exclusive 10% discount on your next purchase:",
              "question_id": "KGQi5e",
              "values": [
                "paulina@revenuehunt.fake"
              ]
            },
            {
              "question_title": "Is your skin sensitive to any of the following ingredients?",
              "question_id": "yYqiz5",
              "choice_label": "Witch Hazel"
            },
            {
              "question_title": "Which of the following best describes the climate in which you live?",
              "question_id": "pa2i8L",
              "choice_label": "Desert or High Altitude"
            },
            {
              "question_title": "What is your main skin concern?",
              "question_id": "ydDimb",
              "choice_label": "Fine lines and wrinkles"
            },
            {
              "question_title": "How does your skin feel on an average day?",
              "question_id": "K72iWW",
              "choice_label": "Dry and tight all over"
            },
            {
              "question_title": "Pleased to meet you {{slide:ZMiXjj}}, what is your age?",
              "question_id": "p5Vi02",
              "choice_label": "40's"
            },
            {
              "question_title": "Before we get started... what's your name?",
              "question_id": "ZMiXjj",
              "values": [
                "Paulina"
              ]
            }
          ],
          "tags": [
            "sensitive_witch_hazel",
            "desert_area",
            "fine_lines",
            "dry_skin",
            "40s"
          ],
          "permalink": "https://skincarequiz.myshopify.com/#results-dbqHqN-NLTqvGqg",
          "permalink_hash": "#results-dbqHqN-NLTqvGqg",
          "created_at": "2022-07-15T13:18:30Z"
        }
        ```

=== "Standalone"

    A webhook receives all of the quiz data:

    - The customer's name, email address and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    The data is sent as a JSON payload in a POST request, so another system can read it directly.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    ??? example "Sample JSON payload for a skincare quiz"

        ```json
        {
          "quiz_name": "Skincare Quiz (Basic Routine)",
          "quiz_id": "dbqHqN",
          "response_id": "NLTqvGqg",
          "first_name": "Paulina",
          "full_name": "Paulina",
          "email": "paulina@revenuehunt.fake",
          "emails": [
            "paulina@revenuehunt.fake"
          ],
          "products": [
            {
              "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
              "score": 2.102760090909091,
              "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
              "price": "27.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
              "position": 0,
              "sku": "RHSK-016",
              "id": 4095078301780,
              "variant_id": 30099568885844
            },
            {
              "name": "Organix Facial Moisturizer",
              "score": 2.1020920909090908,
              "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
              "price": "36.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
              "position": 1,
              "sku": "RHSK-012",
              "id": 4095721668692,
              "variant_id": 30104418451540
            },
            {
              "name": "All Natural Face Cleanser",
              "score": 2.101927090909091,
              "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
              "price": "32.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
              "position": 2,
              "sku": "RHSK-001",
              "id": 4095717834836,
              "variant_id": 30104403476564
            },
            {
              "name": "Fresh Rose Deep Hydration Toner",
              "score": 1.1010830909090907,
              "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
              "price": "48.0",
              "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
              "position": 3,
              "sku": "RHSK-006",
              "id": 4095053168724,
              "variant_id": 30099364773972
            }
          ],
          "blocks": [
            {
              "id": "Q2wTvD",
              "type": "HeadingBlock",
              "position": 0,
              "content": "{{slide:ZMiXjj}}, here's what your skin wants!"
            },
            {
              "id": "Qm0T1V",
              "type": "ContentBlock",
              "position": 1,
              "content": "Applying your skin care products in the proper order ensures that your skin receives the full benefits of each product.↵↵Enter this coupon code at checkout to get a 10% discount:↵**QUIZ123**↵↵"
            },
            {
              "id": "Qp7T9x",
              "type": "SlotsBlock",
              "position": 2,
              "slots": [
                {
                  "id": "NXGuwK",
                  "title": "Step 1: Cleanser",
                  "position": 0,
                  "products": [
                    {
                      "name": "All Natural Face Cleanser",
                      "id": 4095717834836,
                      "url": "https://skincarequiz.myshopify.com/products/all-natural-face-cleanser",
                      "price": "32.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/cleanser.jpg?v=1568621187",
                      "sku": "RHSK-001",
                      "variant_id": 30104403476564,
                      "position": 0,
                      "score": 2.101927090909091
                    }
                  ]
                },
                {
                  "id": "RV6u0R",
                  "title": "Step 2: Toner",
                  "position": 1,
                  "products": [
                    {
                      "name": "Fresh Rose Deep Hydration Toner",
                      "id": 4095053168724,
                      "url": "https://skincarequiz.myshopify.com/products/fresh-rose-deep-hydration-toner",
                      "price": "48.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/fresh-rose-hydration.jpg?v=1568581379",
                      "sku": "RHSK-006",
                      "variant_id": 30099364773972,
                      "position": 0,
                      "score": 1.1010830909090907
                    }
                  ]
                },
                {
                  "id": "K6MuvR",
                  "title": "Step 3: Serum",
                  "position": 2,
                  "products": [
                    {
                      "name": "The Ordinary \"Buffet\" + Copper Peptides 1%",
                      "id": 4095078301780,
                      "url": "https://skincarequiz.myshopify.com/products/the-ordinary-buffet-copper-peptides-1",
                      "price": "27.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/oily-serum.jpg?v=1568583098",
                      "sku": "RHSK-016",
                      "variant_id": 30099568885844,
                      "position": 0,
                      "score": 2.102760090909091
                    }
                  ]
                },
                {
                  "id": "9OJulN",
                  "title": "Step 4: Moisturizer",
                  "position": 3,
                  "products": [
                    {
                      "name": "Organix Facial Moisturizer",
                      "id": 4095721668692,
                      "url": "https://skincarequiz.myshopify.com/products/organix-facial-moisturizer",
                      "price": "36.0",
                      "image_url": "https://cdn.shopify.com/s/files/1/0273/8113/7492/products/age-moisturizer.jpg?v=1568621334",
                      "sku": "RHSK-012",
                      "variant_id": 30104418451540,
                      "position": 0,
                      "score": 2.1020920909090908
                    }
                  ]
                }
              ]
            }
          ],
          "answers": [
            {
              "question_title": "Leave us your email to receive an exclusive 10% discount on your next purchase:",
              "question_id": "KGQi5e",
              "values": [
                "paulina@revenuehunt.fake"
              ]
            },
            {
              "question_title": "Is your skin sensitive to any of the following ingredients?",
              "question_id": "yYqiz5",
              "choice_label": "Witch Hazel"
            },
            {
              "question_title": "Which of the following best describes the climate in which you live?",
              "question_id": "pa2i8L",
              "choice_label": "Desert or High Altitude"
            },
            {
              "question_title": "What is your main skin concern?",
              "question_id": "ydDimb",
              "choice_label": "Fine lines and wrinkles"
            },
            {
              "question_title": "How does your skin feel on an average day?",
              "question_id": "K72iWW",
              "choice_label": "Dry and tight all over"
            },
            {
              "question_title": "Pleased to meet you {{slide:ZMiXjj}}, what is your age?",
              "question_id": "p5Vi02",
              "choice_label": "40's"
            },
            {
              "question_title": "Before we get started... what's your name?",
              "question_id": "ZMiXjj",
              "values": [
                "Paulina"
              ]
            }
          ],
          "tags": [
            "sensitive_witch_hazel",
            "desert_area",
            "fine_lines",
            "dry_skin",
            "40s"
          ],
          "permalink": "https://skincarequiz.myshopify.com/#results-dbqHqN-NLTqvGqg",
          "permalink_hash": "#results-dbqHqN-NLTqvGqg",
          "created_at": "2022-07-15T13:18:30Z"
        }
        ```


## Troubleshooting broken JSON responses in webhooks

=== "Shopify"

    If a webhook response holds broken or invalid JSON, work through the steps below.

    **What you see:** the response is badly formatted, with incomplete or misaligned JSON objects in your logs. An unexpected content type or header configuration usually causes it.

    1. **Check the `Content-Type` header on the payload.** Log the headers to see what is actually sent. An unexpected content type makes the receiver read the payload wrongly.

        !!! example

            ```text
            Content-Type: application/x-www-form-urlencoded
            ```

    2. **Compare that header with the one your endpoint expects.** If they differ, set it yourself in the webhook configuration.

        !!! example

            ```json
            "Content-Type": "application/json"
            ```

    3. **Set the `Content-Type` header explicitly**, to `application/json` in most cases.
    4. **Disconnect the webhook, then reconnect it and run the test again.** Check that it comes back active.
    5. **Validate the payload with a tool such as [JSONLint](https://jsonlint.com/).** Paste it in to confirm it is well-formed JSON.
    6. **Click the top-right `Save` button.** Your changes are not applied until you do.
    7. **Take the quiz all the way through with valid test data**, such as an email address and a phone number. Confirm the webhook receives the corrected payload.

=== "Shopify (Legacy)"

    If a webhook response holds broken or invalid JSON, work through the steps below.

    **What you see:** the response is badly formatted, with incomplete or misaligned JSON objects in your logs. An unexpected content type or header configuration usually causes it.

    1. **Check the `Content-Type` header on the payload.** Log the headers to see what is actually sent. An unexpected content type makes the receiver read the payload wrongly.

        !!! example

            ```text
            Content-Type: application/x-www-form-urlencoded
            ```

    2. **Compare that header with the one your endpoint expects.** If they differ, set it yourself in the webhook configuration.

        !!! example

            ```json
            "Content-Type": "application/json"
            ```

    3. **Set the `Content-Type` header explicitly**, to `application/json` in most cases.
    4. **Disconnect the webhook, then reconnect it and run the test again.** Check that it comes back active.
    5. **Validate the payload with a tool such as [JSONLint](https://jsonlint.com/).** Paste it in to confirm it is well-formed JSON.
    6. **Click the top-right `Publish` button.** Your changes are not applied until you do.
    7. **Take the quiz all the way through with valid test data**, such as an email address and a phone number. Confirm the webhook receives the corrected payload.

=== "WooCommerce"

    If a webhook response holds broken or invalid JSON, work through the steps below.

    **What you see:** the response is badly formatted, with incomplete or misaligned JSON objects in your logs. An unexpected content type or header configuration usually causes it.

    1. **Check the `Content-Type` header on the payload.** Log the headers to see what is actually sent. An unexpected content type makes the receiver read the payload wrongly.

        !!! example

            ```text
            Content-Type: application/x-www-form-urlencoded
            ```

    2. **Compare that header with the one your endpoint expects.** If they differ, set it yourself in the webhook configuration.

        !!! example

            ```json
            "Content-Type": "application/json"
            ```

    3. **Set the `Content-Type` header explicitly**, to `application/json` in most cases.
    4. **Disconnect the webhook, then reconnect it and run the test again.** Check that it comes back active.
    5. **Validate the payload with a tool such as [JSONLint](https://jsonlint.com/).** Paste it in to confirm it is well-formed JSON.
    6. **Click the top-right `Publish` button.** Your changes are not applied until you do.
    7. **Take the quiz all the way through with valid test data**, such as an email address and a phone number. Confirm the webhook receives the corrected payload.

=== "Magento"

    If a webhook response holds broken or invalid JSON, work through the steps below.

    **What you see:** the response is badly formatted, with incomplete or misaligned JSON objects in your logs. An unexpected content type or header configuration usually causes it.

    1. **Check the `Content-Type` header on the payload.** Log the headers to see what is actually sent. An unexpected content type makes the receiver read the payload wrongly.

        !!! example

            ```text
            Content-Type: application/x-www-form-urlencoded
            ```

    2. **Compare that header with the one your endpoint expects.** If they differ, set it yourself in the webhook configuration.

        !!! example

            ```json
            "Content-Type": "application/json"
            ```

    3. **Set the `Content-Type` header explicitly**, to `application/json` in most cases.
    4. **Disconnect the webhook, then reconnect it and run the test again.** Check that it comes back active.
    5. **Validate the payload with a tool such as [JSONLint](https://jsonlint.com/).** Paste it in to confirm it is well-formed JSON.
    6. **Click the top-right `Publish` button.** Your changes are not applied until you do.
    7. **Take the quiz all the way through with valid test data**, such as an email address and a phone number. Confirm the webhook receives the corrected payload.

=== "BigCommerce"

    If a webhook response holds broken or invalid JSON, work through the steps below.

    **What you see:** the response is badly formatted, with incomplete or misaligned JSON objects in your logs. An unexpected content type or header configuration usually causes it.

    1. **Check the `Content-Type` header on the payload.** Log the headers to see what is actually sent. An unexpected content type makes the receiver read the payload wrongly.

        !!! example

            ```text
            Content-Type: application/x-www-form-urlencoded
            ```

    2. **Compare that header with the one your endpoint expects.** If they differ, set it yourself in the webhook configuration.

        !!! example

            ```json
            "Content-Type": "application/json"
            ```

    3. **Set the `Content-Type` header explicitly**, to `application/json` in most cases.
    4. **Disconnect the webhook, then reconnect it and run the test again.** Check that it comes back active.
    5. **Validate the payload with a tool such as [JSONLint](https://jsonlint.com/).** Paste it in to confirm it is well-formed JSON.
    6. **Click the top-right `Publish` button.** Your changes are not applied until you do.
    7. **Take the quiz all the way through with valid test data**, such as an email address and a phone number. Confirm the webhook receives the corrected payload.

=== "Standalone"

    If a webhook response holds broken or invalid JSON, work through the steps below.

    **What you see:** the response is badly formatted, with incomplete or misaligned JSON objects in your logs. An unexpected content type or header configuration usually causes it.

    1. **Check the `Content-Type` header on the payload.** Log the headers to see what is actually sent. An unexpected content type makes the receiver read the payload wrongly.

        !!! example

            ```text
            Content-Type: application/x-www-form-urlencoded
            ```

    2. **Compare that header with the one your endpoint expects.** If they differ, set it yourself in the webhook configuration.

        !!! example

            ```json
            "Content-Type": "application/json"
            ```

    3. **Set the `Content-Type` header explicitly**, to `application/json` in most cases.
    4. **Disconnect the webhook, then reconnect it and run the test again.** Check that it comes back active.
    5. **Validate the payload with a tool such as [JSONLint](https://jsonlint.com/).** Paste it in to confirm it is well-formed JSON.
    6. **Click the top-right `Publish` button.** Your changes are not applied until you do.
    7. **Take the quiz all the way through with valid test data**, such as an email address and a phone number. Confirm the webhook receives the corrected payload.


---
This article explains how to send your quiz data to a webhook.

