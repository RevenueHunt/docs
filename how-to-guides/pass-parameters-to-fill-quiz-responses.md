---
icon: material/slash-forward-box
description: "Learn how to enable pre-fill on retake for RevenueHunt quiz responses to streamline customer experience."
---

# How to Pass Parameters to Pre-fill Quiz Responses

A quiz can open with some answers already filled in, so a customer never retypes something you already hold.

That is worth doing when a logged-in customer's name and email are already on file. It helps too when you send people from a mailing list that holds their details. A pre-filled question is skipped, so the quiz is shorter as well.

## Pre-fill answers when a customer retakes the quiz

=== "Shopify"

    A customer who retakes the quiz gets their previous answers back, including choices, text fields and dates. They change only what is different.

    1. **Open [Quiz settings > General](/reference/quiz-builder/quiz-settings/#general).**

    2. **Under `Quiz behavior settings`, turn `Pre-fill answers on retake` on.**

    3. **Click the top-right `Save` button.**

    4. **Take the quiz through to the results page, then click `Retake quiz`.** Your answers should come back with you.

    !!! note "The default depends on the age of the quiz"

        A quiz created recently has this on already. A quiz that predates the setting has it off.

=== "Shopify (Legacy)"

    !!! note "Not part of this version"

        There is no retake setting here. Fill the answers in yourself, with [JavaScript variables](#pre-fill-with-javascript-variables) or [URL parameters](#pre-fill-with-url-parameters).

=== "WooCommerce"

    !!! note "Not part of this version"

        There is no retake setting here. Fill the answers in yourself, with [JavaScript variables](#pre-fill-with-javascript-variables) or [URL parameters](#pre-fill-with-url-parameters).

=== "Magento"

    !!! note "Not part of this version"

        There is no retake setting here. Fill the answers in yourself, with [JavaScript variables](#pre-fill-with-javascript-variables) or [URL parameters](#pre-fill-with-url-parameters).

=== "BigCommerce"

    !!! note "Not part of this version"

        There is no retake setting here. Fill the answers in yourself, with [JavaScript variables](#pre-fill-with-javascript-variables) or [URL parameters](#pre-fill-with-url-parameters).

=== "Standalone"

    !!! note "Not part of this version"

        There is no retake setting here. Fill the answers in yourself, with [JavaScript variables](#pre-fill-with-javascript-variables) or [URL parameters](#pre-fill-with-url-parameters).

## Pre-fill with JavaScript variables

=== "Shopify"

    !!! note "Not part of this version"

        `window.prq_vars` and the `prq_` URL parameters belong to the five older versions.

        Use [Pre-fill answers when a customer retakes the quiz](#pre-fill-answers-when-a-customer-retakes-the-quiz) instead.

=== "Shopify (Legacy)"

    Declare `window.prq_vars` in a `<script>` tag on the page that holds the quiz. This route needs a developer.

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    // a question ID, with its choice IDs separated by a semicolon
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    </script>
    ```

    `name`, `email` and `phone` fill the matching question types. For any other question, use its question ID as the key.

    **Recording which page the quiz was taken from**

    Say the quiz is embedded on every product page, and you want to know which one a customer started from.

    1. **Add a `Short Text` question to hold the value.** See [Question types](/reference/quiz-builder/questions/#question-types).

    2. **Copy its question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Set that ID on your product page, with the product ID as its value.**

        ```html
        <script>
        window.prq_vars = {};
        window.prq_vars.cdRDCc = 'PRODUCT-1234';
        </script>
        ```

    4. **Take the quiz from that page, then open [Responses](/reference/quiz-builder/metrics/#responses) and check the product ID arrived.**

    !!! warning "A pre-filled question is skipped"

        The customer never sees a question you fill in for them. If the same quiz also runs somewhere that has no script, pass an empty value for that question ID there, or the question appears.

=== "WooCommerce"

    Declare `window.prq_vars` in a `<script>` tag on the page that holds the quiz. This route needs a developer.

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    // a question ID, with its choice IDs separated by a semicolon
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    </script>
    ```

    `name`, `email` and `phone` fill the matching question types. For any other question, use its question ID as the key.

    **Recording which page the quiz was taken from**

    Say the quiz is embedded on every product page, and you want to know which one a customer started from.

    1. **Add a `Short Text` question to hold the value.** See [Question types](/reference/quiz-builder/questions/#question-types).

    2. **Copy its question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Set that ID on your product page, with the product ID as its value.**

        ```html
        <script>
        window.prq_vars = {};
        window.prq_vars.cdRDCc = 'PRODUCT-1234';
        </script>
        ```

    4. **Take the quiz from that page, then open [Responses](/reference/quiz-builder/metrics/#responses) and check the product ID arrived.**

    !!! warning "A pre-filled question is skipped"

        The customer never sees a question you fill in for them. If the same quiz also runs somewhere that has no script, pass an empty value for that question ID there, or the question appears.

=== "Magento"

    Declare `window.prq_vars` in a `<script>` tag on the page that holds the quiz. This route needs a developer.

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    // a question ID, with its choice IDs separated by a semicolon
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    </script>
    ```

    `name`, `email` and `phone` fill the matching question types. For any other question, use its question ID as the key.

    **Recording which page the quiz was taken from**

    Say the quiz is embedded on every product page, and you want to know which one a customer started from.

    1. **Add a `Short Text` question to hold the value.** See [Question types](/reference/quiz-builder/questions/#question-types).

    2. **Copy its question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Set that ID on your product page, with the product ID as its value.**

        ```html
        <script>
        window.prq_vars = {};
        window.prq_vars.cdRDCc = 'PRODUCT-1234';
        </script>
        ```

    4. **Take the quiz from that page, then open [Responses](/reference/quiz-builder/metrics/#responses) and check the product ID arrived.**

    !!! warning "A pre-filled question is skipped"

        The customer never sees a question you fill in for them. If the same quiz also runs somewhere that has no script, pass an empty value for that question ID there, or the question appears.

=== "BigCommerce"

    Declare `window.prq_vars` in a `<script>` tag on the page that holds the quiz. This route needs a developer.

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    // a question ID, with its choice IDs separated by a semicolon
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    </script>
    ```

    `name`, `email` and `phone` fill the matching question types. For any other question, use its question ID as the key.

    **Recording which page the quiz was taken from**

    Say the quiz is embedded on every product page, and you want to know which one a customer started from.

    1. **Add a `Short Text` question to hold the value.** See [Question types](/reference/quiz-builder/questions/#question-types).

    2. **Copy its question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Set that ID on your product page, with the product ID as its value.**

        ```html
        <script>
        window.prq_vars = {};
        window.prq_vars.cdRDCc = 'PRODUCT-1234';
        </script>
        ```

    4. **Take the quiz from that page, then open [Responses](/reference/quiz-builder/metrics/#responses) and check the product ID arrived.**

    !!! warning "A pre-filled question is skipped"

        The customer never sees a question you fill in for them. If the same quiz also runs somewhere that has no script, pass an empty value for that question ID there, or the question appears.

=== "Standalone"

    Declare `window.prq_vars` in a `<script>` tag on the page that holds the quiz. This route needs a developer.

    ```html
    <script>
    window.prq_vars = {};
    window.prq_vars.name = 'John Doe';
    window.prq_vars.email = 'john.doe@gmail.com';
    window.prq_vars.phone = '+15556219645';
    // a question ID, with its choice IDs separated by a semicolon
    window.prq_vars.cdRDCc = 'xDAwDe;aSEfBq';
    </script>
    ```

    `name`, `email` and `phone` fill the matching question types. For any other question, use its question ID as the key.

    **Recording which page the quiz was taken from**

    Say the quiz is embedded on every product page, and you want to know which one a customer started from.

    1. **Add a `Short Text` question to hold the value.** See [Question types](/reference/quiz-builder/questions/#question-types).

    2. **Copy its question ID from the [question settings](/reference/quiz-builder/questions/#question-settings).**

    3. **Set that ID on your product page, with the product ID as its value.**

        ```html
        <script>
        window.prq_vars = {};
        window.prq_vars.cdRDCc = 'PRODUCT-1234';
        </script>
        ```

    4. **Take the quiz from that page, then open [Responses](/reference/quiz-builder/metrics/#responses) and check the product ID arrived.**

    !!! warning "A pre-filled question is skipped"

        The customer never sees a question you fill in for them. If the same quiz also runs somewhere that has no script, pass an empty value for that question ID there, or the question appears.

## Pre-fill with URL parameters

=== "Shopify"

    !!! note "Not part of this version"

        `window.prq_vars` and the `prq_` URL parameters belong to the five older versions.

        Use [Pre-fill answers when a customer retakes the quiz](#pre-fill-answers-when-a-customer-retakes-the-quiz) instead.

=== "Shopify (Legacy)"

    A URL parameter is a value carried on the end of a link, after a `?`, with an `&` between one parameter and the next. Prefix each key with `prq_`.

    ```text
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    ```

    | Parameter | What it fills |
    |---|---|
    | `prq_name` | The name question |
    | `prq_email` | The email question |
    | `prq_phone` | The phone question |
    | `prq_` and a question ID | That question, with choice IDs separated by a semicolon |

    !!! info "A URL parameter beats a JavaScript variable"

        If the same value is set in `window.prq_vars` and in the URL, the URL wins.

    **Try it on your own quiz**

    1. **Open the page that holds your quiz and copy its address.**

    2. **Add `?prq_name=John%20Doe&prq_email=john.doe@gmail.com` to the end of it.**

    3. **Open that link and take the quiz.** The name and email questions should arrive filled in, and the quiz should skip past them.

=== "WooCommerce"

    A URL parameter is a value carried on the end of a link, after a `?`, with an `&` between one parameter and the next. Prefix each key with `prq_`.

    ```text
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    ```

    | Parameter | What it fills |
    |---|---|
    | `prq_name` | The name question |
    | `prq_email` | The email question |
    | `prq_phone` | The phone question |
    | `prq_` and a question ID | That question, with choice IDs separated by a semicolon |

    !!! info "A URL parameter beats a JavaScript variable"

        If the same value is set in `window.prq_vars` and in the URL, the URL wins.

    **Try it on your own quiz**

    1. **Open the page that holds your quiz and copy its address.**

    2. **Add `?prq_name=John%20Doe&prq_email=john.doe@gmail.com` to the end of it.**

    3. **Open that link and take the quiz.** The name and email questions should arrive filled in, and the quiz should skip past them.

=== "Magento"

    A URL parameter is a value carried on the end of a link, after a `?`, with an `&` between one parameter and the next. Prefix each key with `prq_`.

    ```text
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    ```

    | Parameter | What it fills |
    |---|---|
    | `prq_name` | The name question |
    | `prq_email` | The email question |
    | `prq_phone` | The phone question |
    | `prq_` and a question ID | That question, with choice IDs separated by a semicolon |

    !!! info "A URL parameter beats a JavaScript variable"

        If the same value is set in `window.prq_vars` and in the URL, the URL wins.

    **Try it on your own quiz**

    1. **Open the page that holds your quiz and copy its address.**

    2. **Add `?prq_name=John%20Doe&prq_email=john.doe@gmail.com` to the end of it.**

    3. **Open that link and take the quiz.** The name and email questions should arrive filled in, and the quiz should skip past them.

=== "BigCommerce"

    A URL parameter is a value carried on the end of a link, after a `?`, with an `&` between one parameter and the next. Prefix each key with `prq_`.

    ```text
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    ```

    | Parameter | What it fills |
    |---|---|
    | `prq_name` | The name question |
    | `prq_email` | The email question |
    | `prq_phone` | The phone question |
    | `prq_` and a question ID | That question, with choice IDs separated by a semicolon |

    !!! info "A URL parameter beats a JavaScript variable"

        If the same value is set in `window.prq_vars` and in the URL, the URL wins.

    **Try it on your own quiz**

    1. **Open the page that holds your quiz and copy its address.**

    2. **Add `?prq_name=John%20Doe&prq_email=john.doe@gmail.com` to the end of it.**

    3. **Open that link and take the quiz.** The name and email questions should arrive filled in, and the quiz should skip past them.

=== "Standalone"

    A URL parameter is a value carried on the end of a link, after a `?`, with an `&` between one parameter and the next. Prefix each key with `prq_`.

    ```text
    prq_name=John Doe
    prq_email=john.doe@gmail.com
    prq_phone=+15556219645
    prq_cdRDCc=xDAwDe;aSEfBq
    ```

    | Parameter | What it fills |
    |---|---|
    | `prq_name` | The name question |
    | `prq_email` | The email question |
    | `prq_phone` | The phone question |
    | `prq_` and a question ID | That question, with choice IDs separated by a semicolon |

    !!! info "A URL parameter beats a JavaScript variable"

        If the same value is set in `window.prq_vars` and in the URL, the URL wins.

    **Try it on your own quiz**

    1. **Open the page that holds your quiz and copy its address.**

    2. **Add `?prq_name=John%20Doe&prq_email=john.doe@gmail.com` to the end of it.**

    3. **Open that link and take the quiz.** The name and email questions should arrive filled in, and the quiz should skip past them.

---

This article explains the three ways a quiz can open with answers already filled in, and which one each version has.