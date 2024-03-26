# How to Send Leads to Webhooks

Integrating thw quiz with webhooks allows you to automatically send all quiz data, including responses, recommended products, and participant information, to your specified endpoints. This guide will walk you through the steps to link your quiz to custom webhooks, enabling seamless data integration for further processing or analysis.

Before you start, ensure you have:

- A Shop quiz from which you want to send data.
- A valid webhook URL to receive the data.

## Link Quiz to Webhooks

To initiate the integration:

1. Navigate to the [Connect](https://docs.revenuehunt.com/reference/quiz-builder/#connect) section of your quiz.
2. Scroll down to the "Webhooks" option and click on `Connect` to expand the input field.
3. In the newly opened line, paste your webhook URL. The system will automatically save the URL once entered.
4. After adding the webhook URL, click on the three dots `…` next to the webhook entry and select `Test webhook` from the dropdown menu.
5. A successful connection test will result in a message, the appearance of which may vary based on your webhook's configuration.
    ![how to webhook success](/images/how to webhook success.png)

6. If an error occurs during the test, perform the following checks:
    - Verify that your quiz has received responses by checking the `Metrics -> Responses` section. If no responses are present, generate test responses by selecting `Previewing` it.
    - Confirm the correctness of the webhook URL and its active status.

7. **Configuring HTTP Headers (Optional)**: For enhanced security or specific data handling requirements, you can add HTTP headers to your webhook.

    1. After a successful connection test, select `+add new header` to open header fields.
    2. Enter the data for your HTTP headers, which will be sent along with the quiz data in a POST request.

8. **Activating Your Webhook**: With testing and configuration complete, activate your webhook. Use the toggle button next to your webhook entry to activate it. This switch allows for easy deactivation should the need arise.

Upon activation, all quiz data will be transmitted to your webhook URL via a POST request (including headers).

![how to webhook post](/images/how to webhook post.png)

If you want to add another webhook to the quiz, click `+add new webhook`, paste a new URL and follow the same steps to test and activate it.

## What Data is Sent to Webhook?

Webhooks will receive all data from the quiz, incluiding:

- Participant's name, email, and phone number.
- Details of recommended products.
- Quiz questions and their respective answers.
- Tags, quiz permalink, and the permalink to individual quiz responses.

This data is packaged and sent as a JSON payload in a POST request, ensuring a structured and accessible format for automated processing or integration into other systems.

![how to webhook sample](/images/how to webhook sample.png)

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

