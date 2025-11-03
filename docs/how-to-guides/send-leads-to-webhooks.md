# How to Send Leads to Webhooks

Integrating thw quiz with webhooks allows you to automatically send all quiz data, including responses, recommended products, and participant information, to your specified endpoints. 

This guide will walk you through the steps to link your quiz to custom webhooks, enabling instant data integration for further processing or analysis.

Before you start, ensure you have:

- A RevenueHunt Product Recommendation Quiz from which you want to send data.
- A valid webhook URL to receive the data. You can use a service like [Webhook.site](https://webhook.site) to generate a temporary endpoint if you want to test the feature.

## Link Quiz to Webhooks

=== "Shopify"

    <div style="position: relative; padding-bottom: 56.34837355718783%; height: 0;"><iframe src="https://www.youtube.com/embed/VE314AzvTbY?si=jCWb9ok0xAJAbTis" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

    1. **Prepare Your Quiz**. Ensure your quiz is fully set up with all the questions you want. Open the [Quiz Settings](/reference/quiz-builder/quiz-settings/).
    
    2. **Access the Webhooks Integration**. Scroll down to the [Integrations](/reference/quiz-builder/quiz-settings/#integrations) section. Click on **Webhooks** to open the integration panel.
    
    3. **Add a New Webhook**. Click `+ Add Webhook`. You can use a service like [Webhook.site](https://webhook.site) to generate a temporary endpoint if you want to test the feature.

        ![how to webhook add](/images/how_to_shopifyv2_webhooks_add_webhook.png)
    
    4. **Enter the Webhook URL**. Paste the generated URL into the input field. Assign a name to the webhook (e.g., "Skin Care Test Quiz").

        ![how to webhook add](/images/how_to_shopifyv2_webhooks_connection.png)
    
    5. **Configure Webhook Settings**. Select the quiz data you want to send by toggling the available options. (Optional) Add HTTP headers by entering key-value pairs. 
    
    6. **Save Your Changes**. Click `Save` to apply the webhook configuration.
    
    7. **Send a Test Webhook**. Click `Send Test` to trigger a sample payload. This helps verify that your webhook is receiving data correctly.

        ![how to webhook settings](/images/how_to_shopifyv2_webhooks_connection_succesful.png)
    
    8. **Verify Delivery**. Open your endpoint (e.g., Webhook.site) and confirm that a POST request has been received. Review the JSON payload to ensure it contains the correct quiz and customer data.

        ![how to webhook settings](/images/how_to_shopifyv2_webhooks_test_connection_result_post.png)
    
    9. **(Optional) Add More Webhooks**. Click `+ Add Webhook` again to enter additional URLs. Repeat the setup steps for each additional webhook.


=== "Shopify (Legacy)"

    To initiate the integration:

    1. Navigate to the [Connect](/reference/quiz-builder/connect-integrations/) section of your quiz.
    2. Scroll down to the "Webhooks" option and click on `Connect` to expand the input field.
    3. In the newly opened line, paste your webhook URL. The system will automatically save the URL once entered.
    4. After adding the webhook URL, click on the three dots `…` next to the webhook entry and select `Test webhook` from the dropdown menu.
    5. A successful connection test will result in a message, the appearance of which may vary based on your webhook's configuration.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. If an error occurs during the test, perform the following checks:
        - Verify that your quiz has received responses by checking the `Metrics -> Responses` section. If no responses are present, generate test responses by selecting `Previewing` it.
        - Confirm the correctness of the webhook URL and its active status.

    7. **Configuring HTTP Headers (Optional)**: For enhanced security or specific data handling requirements, you can add HTTP headers to your webhook.

        1. After a successful connection test, select `+add new header` to open header fields.
        2. Enter the data for your HTTP headers, which will be sent along with the quiz data in a POST request.

    8. **Activating Your Webhook**: With testing and configuration complete, activate your webhook. Use the toggle button next to your webhook entry to activate it. This switch allows for easy deactivation should the need arise.

    Upon activation, all quiz data will be transmitted to your webhook URL via a POST request (including headers).

    ![how to webhook post](/images/how_to_webhook_post.png)

    If you want to add another webhook to the quiz, click `+add new webhook`, paste a new URL and follow the same steps to test and activate it.

=== "WooCommerce"

    To initiate the integration:

    1. Navigate to the [Connect](/reference/quiz-builder/connect-integrations/) section of your quiz.
    2. Scroll down to the "Webhooks" option and click on `Connect` to expand the input field.
    3. In the newly opened line, paste your webhook URL. The system will automatically save the URL once entered.
    4. After adding the webhook URL, click on the three dots `…` next to the webhook entry and select `Test webhook` from the dropdown menu.
    5. A successful connection test will result in a message, the appearance of which may vary based on your webhook's configuration.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. If an error occurs during the test, perform the following checks:
        - Verify that your quiz has received responses by checking the `Metrics -> Responses` section. If no responses are present, generate test responses by selecting `Previewing` it.
        - Confirm the correctness of the webhook URL and its active status.

    7. **Configuring HTTP Headers (Optional)**: For enhanced security or specific data handling requirements, you can add HTTP headers to your webhook.

        1. After a successful connection test, select `+add new header` to open header fields.
        2. Enter the data for your HTTP headers, which will be sent along with the quiz data in a POST request.

    8. **Activating Your Webhook**: With testing and configuration complete, activate your webhook. Use the toggle button next to your webhook entry to activate it. This switch allows for easy deactivation should the need arise.

    Upon activation, all quiz data will be transmitted to your webhook URL via a POST request (including headers).

    ![how to webhook post](/images/how_to_webhook_post.png)

    If you want to add another webhook to the quiz, click `+add new webhook`, paste a new URL and follow the same steps to test and activate it.

=== "Magento" 

    To initiate the integration:

    1. Navigate to the [Connect](/reference/quiz-builder/connect-integrations/) section of your quiz.
    2. Scroll down to the "Webhooks" option and click on `Connect` to expand the input field.
    3. In the newly opened line, paste your webhook URL. The system will automatically save the URL once entered.
    4. After adding the webhook URL, click on the three dots `…` next to the webhook entry and select `Test webhook` from the dropdown menu.
    5. A successful connection test will result in a message, the appearance of which may vary based on your webhook's configuration.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. If an error occurs during the test, perform the following checks:
        - Verify that your quiz has received responses by checking the `Metrics -> Responses` section. If no responses are present, generate test responses by selecting `Previewing` it.
        - Confirm the correctness of the webhook URL and its active status.

    7. **Configuring HTTP Headers (Optional)**: For enhanced security or specific data handling requirements, you can add HTTP headers to your webhook.

        1. After a successful connection test, select `+add new header` to open header fields.
        2. Enter the data for your HTTP headers, which will be sent along with the quiz data in a POST request.

    8. **Activating Your Webhook**: With testing and configuration complete, activate your webhook. Use the toggle button next to your webhook entry to activate it. This switch allows for easy deactivation should the need arise.

    Upon activation, all quiz data will be transmitted to your webhook URL via a POST request (including headers).

    ![how to webhook post](/images/how_to_webhook_post.png)

    If you want to add another webhook to the quiz, click `+add new webhook`, paste a new URL and follow the same steps to test and activate it.

=== "BigCommerce"

    To initiate the integration:

    1. Navigate to the [Connect](/reference/quiz-builder/connect-integrations/) section of your quiz.
    2. Scroll down to the "Webhooks" option and click on `Connect` to expand the input field.
    3. In the newly opened line, paste your webhook URL. The system will automatically save the URL once entered.
    4. After adding the webhook URL, click on the three dots `…` next to the webhook entry and select `Test webhook` from the dropdown menu.
    5. A successful connection test will result in a message, the appearance of which may vary based on your webhook's configuration.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. If an error occurs during the test, perform the following checks:
        - Verify that your quiz has received responses by checking the `Metrics -> Responses` section. If no responses are present, generate test responses by selecting `Previewing` it.
        - Confirm the correctness of the webhook URL and its active status.

    7. **Configuring HTTP Headers (Optional)**: For enhanced security or specific data handling requirements, you can add HTTP headers to your webhook.

        1. After a successful connection test, select `+add new header` to open header fields.
        2. Enter the data for your HTTP headers, which will be sent along with the quiz data in a POST request.

    8. **Activating Your Webhook**: With testing and configuration complete, activate your webhook. Use the toggle button next to your webhook entry to activate it. This switch allows for easy deactivation should the need arise.

    Upon activation, all quiz data will be transmitted to your webhook URL via a POST request (including headers).

    ![how to webhook post](/images/how_to_webhook_post.png)

    If you want to add another webhook to the quiz, click `+add new webhook`, paste a new URL and follow the same steps to test and activate it.

=== "Standalone"

    To initiate the integration:

    1. Navigate to the [Connect](/reference/quiz-builder/connect-integrations/) section of your quiz.
    2. Scroll down to the "Webhooks" option and click on `Connect` to expand the input field.
    3. In the newly opened line, paste your webhook URL. The system will automatically save the URL once entered.
    4. After adding the webhook URL, click on the three dots `…` next to the webhook entry and select `Test webhook` from the dropdown menu.
    5. A successful connection test will result in a message, the appearance of which may vary based on your webhook's configuration.
        ![how to webhook success](/images/how_to_webhook_success.png)

    6. If an error occurs during the test, perform the following checks:
        - Verify that your quiz has received responses by checking the `Metrics -> Responses` section. If no responses are present, generate test responses by selecting `Previewing` it.
        - Confirm the correctness of the webhook URL and its active status.

    7. **Configuring HTTP Headers (Optional)**: For enhanced security or specific data handling requirements, you can add HTTP headers to your webhook.

        1. After a successful connection test, select `+add new header` to open header fields.
        2. Enter the data for your HTTP headers, which will be sent along with the quiz data in a POST request.

    8. **Activating Your Webhook**: With testing and configuration complete, activate your webhook. Use the toggle button next to your webhook entry to activate it. This switch allows for easy deactivation should the need arise.

    Upon activation, all quiz data will be transmitted to your webhook URL via a POST request (including headers).

    ![how to webhook post](/images/how_to_webhook_post.png)

    If you want to add another webhook to the quiz, click `+add new webhook`, paste a new URL and follow the same steps to test and activate it.



## What Data is Sent to Webhook?

=== "Shopify"

    Webhooks will receive all data from the quiz, incluiding:

    - Participant's name, email, and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    You can select which data to send by toggling the checking the available options while setting up the webhook.

    ![how to webhook add](/images/how_to_shopifyv2_webhooks_connection.png)

    This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

    ![how to webhook settings](/images/how_to_shopifyv2_webhooks_test_connection_result_post.png)

    Below is a sample JSON payload sent on the POST request for a skincare quiz:

    ```html
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
          "value": "I want to recieve exclusive promos, custom skin and skincare tips and and more.",
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

    Webhooks will receive all data from the quiz, incluiding:

    - Participant's name, email, and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    Below is a sample JSON payload sent on the POST request for a skincare quiz:

    ```html
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

    Webhooks will receive all data from the quiz, incluiding:

    - Participant's name, email, and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    Below is a sample JSON payload sent on the POST request for a skincare quiz:

    ```html
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

    Webhooks will receive all data from the quiz, incluiding:

    - Participant's name, email, and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    Below is a sample JSON payload sent on the POST request for a skincare quiz:

    ```html
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

    Webhooks will receive all data from the quiz, incluiding:

    - Participant's name, email, and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    Below is a sample JSON payload sent on the POST request for a skincare quiz:

    ```html
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

    Webhooks will receive all data from the quiz, incluiding:

    - Participant's name, email, and phone number.
    - Details of recommended products.
    - Quiz questions and their respective answers.
    - Tags, quiz permalink, and the permalink to individual quiz responses.

    This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

    ![how to webhook sample](/images/how_to_webhook_sample.png)

    Below is a sample JSON payload sent on the POST request for a skincare quiz:

    ```html
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


## Troubleshooting Broken JSON Responses in Webhooks

If you're experiencing issues where a webhook response contains broken or invalid JSON, here's a step-by-step guide to help you identify and resolve the problem.

**Common Scenario**: When using webhooks to send quiz data, the response may appear broken or improperly formatted. For example, you may see incomplete or misaligned JSON objects in your logs. This could result from an unexpected content type or header configuration.

**Steps to Resolve the Issue**

1. **Check the Content-Type Header:**

    - Inspect the content-type of the webhook payload. 

    - Log the headers to verify the content type being sent. If it is unexpected, this could cause the payload to be interpreted incorrectly.

    Example:
    ```bash
    Content-Type: application/x-www-form-urlencoded
    ```

2. **Verify the Header Configuration**:

    - Compare the headers in your app's webhook configuration with the expected content type in the documentation.
    
    - If the content type differs, it may need to be overridden manually in your webhook configuration.

    Example:

    ```json
    "Content-Type": "application/json"
    ```

3. **Override the Content-Type in the App Config**:

    - Update the webhook configuration to explicitly set the correct `Content-Type` header.

    - For example, change the content type to `application/json`.

4. **Test the Webhook Connection**:

    After updating the configuration, test the connection:

    - Disconnect the webhook.

    - Reconnect the webhook and test it.

    - Ensure the webhook is properly activated.

5. **Validate the JSON**:

    - Use a tool like [JSONLint](https://jsonlint.com/) to validate the JSON payload.

    - Paste the payload into the tool to ensure it conforms to proper JSON formatting.

6. **Publish Your Changes**:

    - Ensure you click the `Publish` button in the top-right corner after making updates to the webhook configuration. 
    
    - Missing this step may result in the changes not being applied.

7. **Retest the Integration**:

    - Complete a full end-to-end test of the quiz, submitting valid test data (e.g., email address, phone number, etc.).

    - Confirm that the webhook receives the corrected JSON payload.


---
By following this article, you can set up your data flow with Webhooks.

