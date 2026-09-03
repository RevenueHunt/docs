---
icon: material/numeric-2
description: "Build a skincare routine quiz with RevenueHunt that recommends organized product recommendations in multiple categories."
---

# Recommending a Skincare Routine with RevenueHunt app


=== "Shopify"


    In this tutorial you will learn how to make and publish a short quiz. It recommends the best skincare products for a customer, organized into clear categories.

    !!! info "What you will learn"

        - how to build a funnel quiz based on a product matrix
        - how to build a quiz that recommends product based on multiple criteria
        - how to create hidden collections in Shopify
        - how to link products and collections to choices in the quiz
        - how the recommendation algorithm works
        - how to edit the results page
        - how to sort product recommendations into slots (clear steps)
        - how to publish the quiz on a dedicated page in your Shopify store
        - how to add a link to the quiz page to your website menu

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/uJJQ34BUcLg?si=9b1Aogh9_gaorp8G" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


=== "Shopify (Legacy)"

    In this tutorial you will learn how to make and publish a short quiz. It recommends the best skincare products for a customer, organized into clear categories.

    !!! info "What you will learn"

        - how to build a quiz from scratch
        - different question types and how to use them
        - how to recall information from the previous questions
        - how to customize quiz design
        - how to link products
        - how the recommendation algorithm works
        - how to edit the results page
        - how to use Markdown Language
        - how to publish the quiz

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "WooCommerce"


    In this tutorial you will learn how to make and publish a short quiz. It recommends the best skincare products for a customer, organized into clear categories.

    !!! info "What you will learn"

        - how to build a quiz from scratch
        - different question types and how to use them
        - how to recall information from the previous questions
        - how to customize quiz design
        - how to link products
        - how the recommendation algorithm works
        - how to edit the results page
        - how to use Markdown Language
        - how to publish the quiz

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Magento"


    In this tutorial you will learn how to make and publish a short quiz. It recommends the best skincare products for a customer, organized into clear categories.

    !!! info "What you will learn"

        - how to build a quiz from scratch
        - different question types and how to use them
        - how to recall information from the previous questions
        - how to customize quiz design
        - how to link products
        - how the recommendation algorithm works
        - how to edit the results page
        - how to use Markdown Language
        - how to publish the quiz

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "BigCommerce"


    In this tutorial you will learn how to make and publish a short quiz. It recommends the best skincare products for a customer, organized into clear categories.

    !!! info "What you will learn"

        - how to build a quiz from scratch
        - different question types and how to use them
        - how to recall information from the previous questions
        - how to customize quiz design
        - how to link products
        - how the recommendation algorithm works
        - how to edit the results page
        - how to use Markdown Language
        - how to publish the quiz

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

=== "Standalone"


    In this tutorial you will learn how to make and publish a short quiz. It recommends the best skincare products for a customer, organized into clear categories.

    !!! info "What you will learn"

        - how to build a quiz from scratch
        - different question types and how to use them
        - how to recall information from the previous questions
        - how to customize quiz design
        - how to link products
        - how the recommendation algorithm works
        - how to edit the results page
        - how to use Markdown Language
        - how to publish the quiz

    <div class="videoWrapper">
    <iframe src="https://www.youtube.com/embed/gfIwTn9hp8E?si=osTF2c3z9afF7IU1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>


## Intro

=== "Shopify"

    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, you can group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Take the quiz on the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site to see an example.

    **Objective**: Build a quiz that recommends a four-step skincare routine to your customers.

    - The quiz recommends a tailored skincare routine including a cleanser, toner, serum, and moisturizer.
    - Recommendations are based on two key factors: age group and skin type.
    - The logic is derived from a product matrix that categorizes products accordingly.

    !!! example "Skincare Product Matrix"

        | Age/Skin Type | Dry or Normal | Oily | Combination |
        |-----------|---------------|------|-------------|
        | **Teens** | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
        | **30–50** | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
        | **50+** | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |




=== "Shopify (Legacy)"

    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, you can group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Take the quiz on the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site to see an example.

    **Objective**: Build a quiz that recommends a four-step skincare routine to your customers.

    Get started below.


=== "WooCommerce"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, you can group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Take the quiz on the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site to see an example.

    **Objective**: Build a quiz that recommends a four-step skincare routine to your customers.

    Get started below.

=== "Magento"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, you can group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Take the quiz on the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site to see an example.

    **Objective**: Build a quiz that recommends a four-step skincare routine to your customers.

    Get started below.

=== "BigCommerce"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, you can group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Take the quiz on the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site to see an example.

    **Objective**: Build a quiz that recommends a four-step skincare routine to your customers.

    Get started below.

=== "Standalone"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, you can group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Take the quiz on the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site to see an example.

    **Objective**: Build a quiz that recommends a four-step skincare routine to your customers.

    Get started below.




## Create collections/categories

=== "Shopify"

    1. **Create a collection for each age group, skin type and product type.** The quiz works as a funnel, filtering products down by age and then skin type.

    2. **Create Manual Collections for Age Groups:** Go to `Shopify > Products > Collections > Add collection`. For each age group, create a `Manual` collection. Include only the products relevant to that age group, across all skin types.

        ??? example "`Teens` collection should include the following products:"

            | Age Group       | Dry or Normal                                                                                   | Oily                                                                                           | Combination                                                                                   |
            |------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
            | **🌟 Teens**     | **Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel**       | **Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** | **All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** |
            | **30–50**        | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | **50+**          | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |


        ??? example "`30 to 50` collection should include the following products:"

            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | **🌟30–50** | **Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream** | **Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion** | **Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |


        ??? example "`50+` collection should include the following products:"


            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | **🌟50+**   | **Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream** | **Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** | **Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel** |


        !!! tip
            Uncheck online store visibility to keep the collections hidden from your online storefront.

    3. **Create Manual Collections for Skin Types:** Go to `Shopify > Products > Collections > Add collection`. Create a `Manual` collection for each skin type that includes only the products that are relevant to that skin type.

        ??? example "`Dry or Normal Skin Type` collection should include the following products:"

            | Age Group | 🌟Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | **Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel** | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | **Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream** | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | **Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream** | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "`Oily Skin Type` collection should include the following products:"



            | Age Group | Dry or Normal | 🌟Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | **Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | **Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion** | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | **Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "`Combination Skin Type` collection should include the following products:"


            | Age Group | Dry or Normal | Oily | 🌟Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | **All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | **Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | **Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel** |



    4. **Create Smart Collections for Product Types Using Tags:** Go to `Shopify > Products > Collections > Add collection`. Create a `Smart` collection for each product type based on a product tag. For example, a *Cleansers* collection should include all the products with the *Cleanser* tag. A *Toners* collection should include all the products with the *Toner* tag, etc.

        ??? example "`Cleansers Quiz` collection should include the following products:"

            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | **Foaming Cream Cleanser**; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | **Neutrogena Oil-Free Acne Face Wash**; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | **All Natural Face Cleanser**; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | **Morning Cleanser**; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | **Redness-Relief Cleansing Lotion**; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | **Neutrogena Oil-Free Acne Face Wash**; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | **Foaming Cream Cleanser**; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | **Redness-Relief Cleansing Lotion**; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | **Morning Cleanser**; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "`Toners Quiz` collection should include the following products:"


            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; **Aloe Soothing Toner**; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; **Balancing Force Oil Control Toner**; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; **United State Balancing Tonic**; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; **Aloe Soothing Toner**; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; **Balancing Force Oil Control Toner**; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; **United State Balancing Tonic**; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | Foaming Cream Cleanser; **Ultra Facial Toner**; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; **United State Balancing Tonic**; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; **Balancing Force Oil Control Toner**; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "`Serums Quiz` collection should include the following products:"


            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; **Vitamin C Serum**; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; **Super Antioxidant Serum**; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; **The Ordinary "Buffet" + Copper Peptides 1%**; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; **The Ordinary "Buffet" + Copper Peptides 1%**; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; **Vitamin C Serum**; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; **Super Antioxidant Serum**; Oil-Free Moisture-Combination Skin |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; **Khadi Global Natural Hyaluronic Acid Serum**; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; **The Ordinary "Buffet" + Copper Peptides 1%**; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; **Super Antioxidant Serum**; Moisturizing Cream-Gel |



        ??? example "`Moisturizers Quiz` collection should include the following products:"



            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; **Moisturizing Cream-Gel** | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; **Oil-Free Moisture-Combination Skin** | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; **Oil-Free Moisture Lotion** |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; **Relaxing Night Cream** | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; **Oil-Free Moisture Lotion** | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; **Oil-Free Moisture-Combination Skin** |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; **Relaxing Night Cream** | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; **Oil-Free Moisture Lotion** | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; **Moisturizing Cream-Gel** |





=== "Shopify (Legacy)"

    1. **In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers.**
    2. **For the slots to work correctly, **create four collections** and put the matching products in them.** For example:
        - a *Cleansers* collection should have all the cleansing products,
        - a *Toners* collection should have all the toning products,
        - a *Serums* collection should have all the serums, etc.
    3. **To create a collection, click on the top-right button.** Check [create a collection in your Shopify store](https://help.shopify.com/en/manual/products/collections) for detailed instructions on managing collections in Shopify.
    4. **Give the collection a name and a description.**
    5. **Next, select how to add products to a collection.** Add them **manually**, one product at a time, or make an **automatic collection** based on a product tag.
    6. **To create a *Cleansers* collection, set the tag to `cleanser`.** Shopify then adds every product with that tag to the collection.
    7. **Create the toners, serums and moisturizer collections the same way.**
    8. **You can have more than one collection that includes some of the same products.** An *anti-aging* or *oily skin* collection can be composed of several cleansers, serums or moisturizers.

=== "WooCommerce"

    1. **In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers.**
    2. **For the slots to work correctly, **create four categories** and put the matching products in them.** For example:
        - a *Cleansers* category should have all the cleansing products,
        - a *Toners* category should have all the toning products,
        - a *Serums* category should have all the serums, etc.
    3. **To create a category, check [create a category in your WooCommerce store](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) for detailed instructions on managing categories in WooCommerce.**

=== "Magento"

    1. **In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers.**
    2. **For the slots to work correctly, **create four categories** and put the matching products in them.** For example:
        - a *Cleansers* category should have all the cleansing products,
        - a *Toners* category should have all the toning products,
        - a *Serums* category should have all the serums, etc.
    3. **To create a category, check [create a category in your Magento store](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) for detailed instructions on managing categories in Magento.**

=== "BigCommerce"

    1. **In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers.**
    2. **For the slots to work correctly, **create four categories** and put the matching products in them.** For example:
        - a *Cleansers* category should have all the cleansing products,
        - a *Toners* category should have all the toning products,
        - a *Serums* category should have all the serums, etc.
    3. **To create a category, check [create a category in your BigCommerce store](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) for detailed instructions on managing categories in BigCommerce.**

=== "Standalone"

    1. **In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers.**
    2. **For the slots to work correctly, **create four collections** and put the matching products in them.** For example:
        - a *Cleansers* collection should have all the cleansing products,
        - a *Toners* collection should have all the toning products,
        - a *Serums* collection should have all the serums, etc.
    3. **To create a collection, go to the [Success Checklist](/reference/dashboard/#success-checklist) and click `view products` to open the `Catalogue`.** Create a collection for each category, either in the Catalogue tab or through a Google Product Feed.

## Sync

=== "Shopify"


    Product data such as names, prices and images is pulled live from Shopify. It stays up to date on its own after you change a product or a collection.

    !!! tip

        If new tags, collections or vendors do not appear in the quiz builder, run a quick catalog import from the [App settings > Catalog](/reference/app-settings/#catalog) page.


=== "Shopify (Legacy)"

    After you change your products or collections, [sync them](/how-to-guides/sync-catalog/) with the app.

    1. **The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).**
    2. **The sync may take between 30 to 60 minutes.**
    3. **When the sync finishes, your products and collections are up to date in the app.**

    !!! info
        Your store is also fully synced every 24 hours.


=== "WooCommerce"


    After you change your products or collections and categories, [sync them](/how-to-guides/sync-catalog/) with the app.

    1. **The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).**
    2. **The sync may take between 30 to 60 minutes.**
    3. **When the sync finishes, your products and collections are up to date in the app.**

    !!! info
        Your store is also fully synced every 24 hours.

=== "Magento"


    After you change your products or collections and categories, [sync them](/how-to-guides/sync-catalog/) with the app.

    1. **The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).**
    2. **The sync may take between 30 to 60 minutes.**
    3. **When the sync finishes, your products and collections are up to date in the app.**

    !!! info
        Your store is also fully synced every 24 hours.

=== "BigCommerce"


    After you change your products or collections and categories, [sync them](/how-to-guides/sync-catalog/) with the app.

    1. **The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).**
    2. **The sync may take between 30 to 60 minutes.**
    3. **When the sync finishes, your products and collections are up to date in the app.**

    !!! info
        Your store is also fully synced every 24 hours.

=== "Standalone"

    After you change your products or collections and categories, [sync them](/how-to-guides/sync-catalog/) with the app.

    1. **The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).**
    2. **The sync may take between 30 to 60 minutes.**
    3. **When the sync finishes, your products and collections are up to date in the app.**

    !!! info
        Your store is also fully synced every 24 hours.



## Build the quiz

=== "Shopify"

    Now you can build your quiz.

    1. **Start from scratch, or use one of the [pre-designed Skincare templates](/reference/dashboard/#new-quiz).**

        !!! tip
            To learn how to use the [Quiz builder](/reference/quiz-builder/), see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).

    2. **Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.**

        - Use a [`Multiple-choice question`](/reference/quiz-builder/questions/#multiple-choice) to find out the customer's **age** and **skin type**.
        - Use a [`Name question`](/reference/quiz-builder/questions/#name) to make the quiz personal.
        - Finish the quiz with an [`Email question`](/reference/quiz-builder/questions/#email-address). Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "Shopify (Legacy)"

    Now you can build your quiz.

    1. **Start from scratch, or use one of the [pre-designed Skincare templates](/reference/dashboard/#new-quiz).**

        !!! tip
            To learn how to use the [Quiz Builder](/reference/quiz-builder/), see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).

    2. **Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.**

        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the customer's age, skin type, skin concerns or the environment they live in.
        - Add a skin sensitivity question as well. [Exclude products](/how-to-guides/set-up-funnel-quiz/#exclusion) explains how to keep products containing allergens out of the recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "WooCommerce"


    Now you can build your quiz.

    1. **Start from scratch, or use one of the [pre-designed Skincare templates](/reference/dashboard/#new-quiz).**

        !!! tip
            To learn how to use the [Quiz Builder](/reference/quiz-builder/), see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).

    2. **Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.**

        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the customer's age, skin type, skin concerns or the environment they live in.
        - Add a skin sensitivity question as well. [Exclude products](/how-to-guides/set-up-funnel-quiz/#exclusion) explains how to keep products containing allergens out of the recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.



=== "Magento"


    Now you can build your quiz.

    1. **Start from scratch, or use one of the [pre-designed Skincare templates](/reference/dashboard/#new-quiz).**

        !!! tip
            To learn how to use the [Quiz Builder](/reference/quiz-builder/), see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).

    2. **Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.**

        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the customer's age, skin type, skin concerns or the environment they live in.
        - Add a skin sensitivity question as well. [Exclude products](/how-to-guides/set-up-funnel-quiz/#exclusion) explains how to keep products containing allergens out of the recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "BigCommerce"


    Now you can build your quiz.

    1. **Start from scratch, or use one of the [pre-designed Skincare templates](/reference/dashboard/#new-quiz).**

        !!! tip
            To learn how to use the [Quiz Builder](/reference/quiz-builder/), see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).

    2. **Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.**

        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the customer's age, skin type, skin concerns or the environment they live in.
        - Add a skin sensitivity question as well. [Exclude products](/how-to-guides/set-up-funnel-quiz/#exclusion) explains how to keep products containing allergens out of the recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "Standalone"


    Now you can build your quiz.

    1. **Start from scratch, or use one of the [pre-designed Skincare templates](/reference/dashboard/#new-quiz).**

        !!! tip
            To learn how to use the [Quiz Builder](/reference/quiz-builder/), see [Making Your First Product Recommendation Quiz](/tutorials/making-first-quiz/).

    2. **Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.**

        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the customer's age, skin type, skin concerns or the environment they live in.
        - Add a skin sensitivity question as well. [Exclude products](/how-to-guides/set-up-funnel-quiz/#exclusion) explains how to keep products containing allergens out of the recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.




## Quiz design

=== "Shopify"


    1. **In the [Quiz design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.**
    2. **You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#advanced-customizations-css) to make it pop.**


=== "Shopify (Legacy)"

    1. **In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.**
    2. **You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#advanced-customizations-css) to make it pop.**

=== "WooCommerce"


    1. **In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.**
    2. **You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#advanced-customizations-css) to make it pop.**

=== "Magento"


    1. **In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.**
    2. **You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#advanced-customizations-css) to make it pop.**

=== "BigCommerce"


    1. **In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.**
    2. **You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#advanced-customizations-css) to make it pop.**

=== "Standalone"


    1. **In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.**
    2. **You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#advanced-customizations-css) to make it pop.**



## Upvote collections/categories

=== "Shopify"


    Once your quiz is built and styled, you should add products or collections to individual choices.

    !!! warning
        Link either products **or** a collection to each choice. Do not mix them.

        A product can be upvoted in a choice and also sit in a collection linked to that choice. It then **receives 2 upvotes from the same choice**, which skews the results.

        So link either individual products to a choice, or one dedicated collection to a choice.

    1. **To do that, go to the [Questions](/reference/quiz-builder/questions/) tab and select a choice.** This will open the Choice settings.
    2. **Under [Choice settings](/reference/quiz-builder/questions/#choice-settings), find the `Upvoting` section and click `Upvote > Collections`.**
    3. **For the age question, you can link the `Teens`, `30-50` and `50+` collections created earlier to each respective choice.**
    4. **Then, link the `Skin type` collections to the choices in the Skin type question.** For example, link the `Dry or Normal` collection to the `Dry` and `Normal` choices. Link the `Combination` collection to the `Combination` choice. Link the `Oily` collection to the `Oily` choice.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [upvoting system](/how-to-guides/recommend-products/).

        - Products/Collections of products are linked to each choice.
        - When a customer picks that choice all the linked products receive one upvote.
        - This includes all the products inside the linked collection.
        - At the end, the results page will show slots with products sorted by the number of upvotes.



=== "Shopify (Legacy)"

    Once your quiz is built and styled, you should add products and collections to individual choices.

    1. **To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**
    2. **For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.**
    3. **Then link the *skin type* collections and categories.**
    4. **You can link one or more collections/categories to the same choice.**
    5. **Continue until every choice in the quiz has products, collections or categories linked.** A choice with nothing linked produces empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [upvoting system](/how-to-guides/recommend-products/).

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one upvote.
        - This includes all the products inside the linked collection.
        - At the end, the results page will show slots with products sorted by the number of upvotes.


=== "WooCommerce"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. **To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**
    2. **For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.**
    3. **Then link the *skin type* collections and categories.**
    4. **You can link one or more collections/categories to the same choice.**
    5. **Continue until every choice in the quiz has products, collections or categories linked.** A choice with nothing linked produces empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [upvoting system](/how-to-guides/recommend-products/).

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one upvote.
        - This includes all the products inside the linked collection.
        - At the end, the results page will show slots with products sorted by the number of upvotes.



=== "Magento"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. **To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**
    2. **For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.**
    3. **Then link the *skin type* collections and categories.**
    4. **You can link one or more collections/categories to the same choice.**
    5. **Continue until every choice in the quiz has products, collections or categories linked.** A choice with nothing linked produces empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [upvoting system](/how-to-guides/recommend-products/).

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one upvote.
        - This includes all the products inside the linked collection.
        - At the end, the results page will show slots with products sorted by the number of upvotes.



=== "BigCommerce"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. **To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**
    2. **For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.**
    3. **Then link the *skin type* collections and categories.**
    4. **You can link one or more collections/categories to the same choice.**
    5. **Continue until every choice in the quiz has products, collections or categories linked.** A choice with nothing linked produces empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [upvoting system](/how-to-guides/recommend-products/).

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one upvote.
        - This includes all the products inside the linked collection.
        - At the end, the results page will show slots with products sorted by the number of upvotes.



=== "Standalone"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. **To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab.**
    2. **For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.**
    3. **Then link the *skin type* collections and categories.**
    4. **You can link one or more collections/categories to the same choice.**
    5. **Continue until every choice in the quiz has products, collections or categories linked.** A choice with nothing linked produces empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [upvoting system](/how-to-guides/recommend-products/).

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one upvote.
        - This includes all the products inside the linked collection.
        - At the end, the results page will show slots with products sorted by the number of upvotes.





## Exclude products

=== "Shopify"

    No need to exclude products. The product matrix will recommend the correct products based on the customer's answers.


=== "Shopify (Legacy)"

    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/set-up-funnel-quiz/#exclusion) feature.

    1. **To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question.**
    2. **Tap on the greyed `exclude products` text and a white bar will appear.**
    3. **Add the products that contain an allergen.**

    When a customer says they are sensitive to *aloe vera*, every product that contains it is excluded from the recommendations.

    !!! warning

        Be careful with exclusions. Once a product is excluded it does not show on the results page, even if another question upvoted it.

=== "WooCommerce"



    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/set-up-funnel-quiz/#exclusion) feature.

    1. **To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question.**
    2. **Tap on the greyed `exclude products` text and a white bar will appear.**
    3. **Add the products that contain an allergen.**

    When a customer says they are sensitive to *aloe vera*, every product that contains it is excluded from the recommendations.

    !!! warning

        Be careful with exclusions. Once a product is excluded it does not show on the results page, even if another question upvoted it.


=== "Magento"


    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/set-up-funnel-quiz/#exclusion) feature.

    1. **To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question.**
    2. **Tap on the greyed `exclude products` text and a white bar will appear.**
    3. **Add the products that contain an allergen.**

    When a customer says they are sensitive to *aloe vera*, every product that contains it is excluded from the recommendations.

    !!! warning

        Be careful with exclusions. Once a product is excluded it does not show on the results page, even if another question upvoted it.


=== "BigCommerce"


    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/set-up-funnel-quiz/#exclusion) feature.

    1. **To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question.**
    2. **Tap on the greyed `exclude products` text and a white bar will appear.**
    3. **Add the products that contain an allergen.**

    When a customer says they are sensitive to *aloe vera*, every product that contains it is excluded from the recommendations.

    !!! warning

        Be careful with exclusions. Once a product is excluded it does not show on the results page, even if another question upvoted it.


=== "Standalone"


    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/set-up-funnel-quiz/#exclusion) feature.

    1. **To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question.**
    2. **Tap on the greyed `exclude products` text and a white bar will appear.**
    3. **Add the products that contain an allergen.**

    When a customer says they are sensitive to *aloe vera*, every product that contains it is excluded from the recommendations.

    !!! warning

        Be careful with exclusions. Once a product is excluded it does not show on the results page, even if another question upvoted it.



## Edit the results page

=== "Shopify"


    Now edit the [Results page](/reference/quiz-builder/results-page/).

    1. **Add a heading, a logo or a text block to customize the page.** For example, you can add a text block to include more information about the recommended skincare routine.

        !!! tip
            Check the [Making Your First Product Recommendation Quiz || Recommending the Best Cleanser](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. **Add Product block**: Include a `Product Block` to display the recommended routine. In `Slot settings` set the `Max. recommended items` to four.
    3. **Preview the quiz**: Click the top-right `Save` button to update the preview, then click `Preview`. Take the quiz a few times and check the recommendations against the product matrix.


=== "Shopify (Legacy)"

    Now edit the [Results Page](/reference/quiz-builder/results-page/).

    1. **Add a heading, a logo or a content block to customize the page.**

        !!! tip
            Check the [Making Your First Product Recommendation Quiz || Recommending the Best Cleanser](/tutorials/making-first-quiz/) to see examples of different blocks being used.

    2. **Add a `content block` to describe every step in the beauty routine.**
    3. **Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text.**

    The page is almost done.

=== "WooCommerce"


    Now edit the [Results Page](/reference/quiz-builder/results-page/).

    1. **Add a heading, a logo or a content block to customize the page.**

        !!! tip
            Check the [Making Your First Product Recommendation Quiz || Recommending the Best Cleanser](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. **Add a `content block` to describe every step in the beauty routine.**
    3. **Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text.**

    The page is almost done.

=== "Magento"


    Now edit the [Results Page](/reference/quiz-builder/results-page/).

    1. **Add a heading, a logo or a content block to customize the page.**

        !!! tip
            Check the [Making Your First Product Recommendation Quiz || Recommending the Best Cleanser](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. **Add a `content block` to describe every step in the beauty routine.**
    3. **Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text.**

    The page is almost done.

=== "BigCommerce"


    Now edit the [Results Page](/reference/quiz-builder/results-page/).

    1. **Add a heading, a logo or a content block to customize the page.**

        !!! tip
            Check the [Making Your First Product Recommendation Quiz || Recommending the Best Cleanser](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. **Add a `content block` to describe every step in the beauty routine.**
    3. **Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text.**

    The page is almost done.

=== "Standalone"


    Now edit the [Results Page](/reference/quiz-builder/results-page/).

    1. **Add a heading, a logo or a content block to customize the page.**

        !!! tip
            Check the [Making Your First Product Recommendation Quiz || Recommending the Best Cleanser](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. **Add a `content block` to describe every step in the beauty routine.**
    3. **Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text.**

    The page is almost done.







## Add slots

=== "Shopify"


    Now sort the recommended products into clear steps. A skincare routine is a cleanser, a toner, a serum and a moisturizer.

    1. **Use `+ Add slot` to add slots to the Product block on the Results page.** You need four slots in total.
    2. **In [Slot settings](/reference/quiz-builder/questions/#block-settings) you can:**
        - Edit the slot name,
        - Add a description,
        - And select how many products should be recommended in each slot. Set the `Max. recommended items` to 1 for each slot.
    3. **Slots need segments.** `Add segments` to each slot, so that it knows which products to choose.

        Open the [Slot settings](/reference/quiz-builder/questions/#block-settings), scroll down to the `Add segments` section and click `Add > Collection`.

        - Add the `Cleansers Quiz` smart collection in the Cleansers Slot
        - Add the `Toners Quiz` smart collection in the Toners Slot
        - Add the `Serums Quiz` smart collection in the Serum Slot,
        - Add the `Moisturizers Quiz` smart collection in the Moisturizer Slot.

    4. **Save the changes with the top-right `Save` button.**


=== "Shopify (Legacy)"

    Now add a space for products.

    1. **A skincare routine is a cleanser, a toner, a serum and a moisturizer.**
    2. **Use `+` to add a `Product Slots Block` and create four different slots for each of the products.**
    3. **In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:**
        - Edit the slot name,
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. **Slots need collections.** `include collections/categories` in each slot, so that it knows which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. **Make sure that the products in these collections/categories are [linked to the answers](#upvote-collectionscategories) in the quiz.** Otherwise, the slots will produce empty results.
    6. **Follow the same steps to create a morning routine.**

    You have created a dynamic results page for your beauty quiz.

=== "WooCommerce"


    Now add a space for products.

    1. **A skincare routine is a cleanser, a toner, a serum and a moisturizer.**
    2. **Use `+` to add a `Product Slots Block` and create four different slots for each of the products.**
    3. **In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:**
        - Edit the slot name,
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. **Slots need collections.** `include collections/categories` in each slot, so that it knows which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. **Make sure that the products in these collections/categories are [linked to the answers](#upvote-collectionscategories) in the quiz.** Otherwise, the slots will produce empty results.
    6. **Follow the same steps to create a morning routine.**

    You have created a dynamic results page for your beauty quiz.



=== "Magento"


    Now add a space for products.

    1. **A skincare routine is a cleanser, a toner, a serum and a moisturizer.**
    2. **Use `+` to add a `Product Slots Block` and create four different slots for each of the products.**
    3. **In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:**
        - Edit the slot name,
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. **Slots need collections.** `include collections/categories` in each slot, so that it knows which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. **Make sure that the products in these collections/categories are [linked to the answers](#upvote-collectionscategories) in the quiz.** Otherwise, the slots will produce empty results.
    6. **Follow the same steps to create a morning routine.**

    You have created a dynamic results page for your beauty quiz.



=== "BigCommerce"


    Now add a space for products.

    1. **A skincare routine is a cleanser, a toner, a serum and a moisturizer.**
    2. **Use `+` to add a `Product Slots Block` and create four different slots for each of the products.**
    3. **In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:**
        - Edit the slot name,
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. **Slots need collections.** `include collections/categories` in each slot, so that it knows which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. **Make sure that the products in these collections/categories are [linked to the answers](#upvote-collectionscategories) in the quiz.** Otherwise, the slots will produce empty results.
    6. **Follow the same steps to create a morning routine.**

    You have created a dynamic results page for your beauty quiz.



=== "Standalone"


    Now add a space for products.

    1. **A skincare routine is a cleanser, a toner, a serum and a moisturizer.**
    2. **Use `+` to add a `Product Slots Block` and create four different slots for each of the products.**
    3. **In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:**
        - Edit the slot name,
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. **Slots need collections.** `include collections/categories` in each slot, so that it knows which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. **Make sure that the products in these collections/categories are [linked to the answers](#upvote-collectionscategories) in the quiz.** Otherwise, the slots will produce empty results.
    6. **Follow the same steps to create a morning routine.**

    You have created a dynamic results page for your beauty quiz.


## Preview the quiz

=== "Shopify"


    1. **Update the preview with the top-right `Save` button.**
    2. **You can test the quiz again by clicking the `Preview` button.**
    3. **Take the quiz a few times to check if the correct products are recommended based on the product matrix.**


=== "Shopify (Legacy)"

    1. **Update the preview/live quiz with the top-right `Publish` button.**
    2. **You can test the quiz by clicking the `Preview`/`Test Quiz` button.**
    3. **Take the quiz a few times to check if the correct products are recommended.**


=== "WooCommerce"


    1. **Update the preview/live quiz with the top-right `Publish` button.**
    2. **You can test the quiz by clicking the `Preview`/`Test Quiz` button.**
    3. **Take the quiz a few times to check if the correct products are recommended.**

=== "Magento"

    1. **Update the preview/live quiz with the top-right `Publish` button.**
    2. **You can test the quiz by clicking the `Preview`/`Test Quiz` button.**
    3. **Take the quiz a few times to check if the correct products are recommended.**

=== "BigCommerce"


    1. **Update the preview/live quiz with the top-right `Publish` button.**
    2. **You can test the quiz by clicking the `Preview`/`Test Quiz` button.**
    3. **Take the quiz a few times to check if the correct products are recommended.**

=== "Standalone"


    1. **Update the preview/live quiz with the top-right `Publish` button.**
    2. **You can test the quiz by clicking the `Preview`/`Test Quiz` button.**
    3. **Take the quiz a few times to check if the correct products are recommended.**

## Publish


=== "Shopify"


    Now publish the quiz on your website. Add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Go to the [`Publish`](/reference/quiz-builder/share-publish/) section and check the instructions for `Add the quiz to a dedicated landing page`.**
    2. **Create a new page template**:
        - In Shopify go to `Online Store > Theme > Customize`.
        - Under Home page top menu select `Pages > Add new page template`. Give the template a name.
        - In the page template editor, add a section. From `Apps` menu select the `Inline Quiz` by RevenueHunt.
        - In the Inline Quiz settings, select the quiz formatting (for example, you can make the quiz full width).
        - Save the template with the top-right `Save` button.
    3. **Create a new page**:
        - Next, go to Shopify `Online Store > Pages` and create a new page.
        - Apply the quiz template to the page.
        - Set the page visibility to `Visible`.
    4. **Add the quiz to the menu**:
        - Next open Shopify `Content > Menus`.
        - Select the Main menu and add a new item.
        - Give it a name, for example `New Quiz Page`, and link it to the page you created in the previous step.
        - Save the changes with the top-right `Save` button.
    5. **From now on, the inline quiz will be visible on that page.**


=== "Shopify (Legacy)"

    Now publish the quiz on your website. Add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **To do that, go to the [`Share`](/reference/quiz-builder/share-publish/) tab and select the `Inline` publish option.**
    2. **Click `Show Instructions for Legacy Themes`.**
    3. **Adjust the quiz's width and height and click `Get code` to generate a code.**
    4. **Copy the code and navigate to your `Online Store > Pages` in Shopify.**
    5. **Add a new page and give it a name.**
    6. **Click the `Show HTML` button and paste the code copied from the app.**
    7. **Make sure to `save` the changes.**

=== "WooCommerce"


    Now publish the quiz on your website. Add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. **Edit the inline quiz settings and click `Get the code`.** Copy the HTML embed code.
    3. **In WordPress, open `Pages` and click `Add New Page`.**
    4. **In the editor, add a page title.** Then, find a `Custom HTML` element and add it to the page in a place where you want the quiz to show.
    5. **In the element, paste the code copied from the app.**
    6. **Save the changes and `update` the page.**
    7. **From now on, the inline quiz will be visible on that page.**

=== "Magento"


    Now publish the quiz on your website. Add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Add the following embed.js script before the `</head>` close tag in the header.**
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Edit the inline quiz settings and click `Get the code`.** Copy the HTML embed code.
    4. **In your Magento dashboard go to `Content` > `Pages`.** Click `Add New Page`.
    5. **Edit the Page Title and open the `Content` tab.** Click `Edit with Page Builder`.
    6. **Select `Elements` > `Rows` and drag a row into the canvas.**
    7. **Next open `Elements` and pick `HTML Code`.** Drag the `HTML Code` onto the Row.
    8. **Click the gear icon to open `HTML settings`.**
    9. **Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app.**
    10. **Remember to save the changes.**
    11. **From now on, the inline quiz will be visible on that page.**

=== "BigCommerce"


    Now publish the quiz on your website. Add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Add the following embed.js script before the `</head>` close tag in the header.**
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Edit the inline quiz settings and click `Get the code`.** Copy the HTML embed code.
    4. **In BigCommerce, go to `Storefront` > `Web Pages`.** Click `Create a Web Page`.
    5. **Under `Web Page Details` > `Page Content` switch to the `HTML` editor.** Paste the HTML code copied from the app.
    6. **Save the changes.**
    7. **From now on, the inline quiz will be visible on that page.**

=== "Standalone"


    Now publish the quiz on your website. Add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embed-an-inline-quiz-on-a-dedicated-landing-page).

    1. **Add the following embed.js script before the `</head>` close tag in the header.**
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz does not load on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. **Edit the inline quiz settings and click `Get the code`.** Copy the HTML embed code.
    4. **In your store customization options find the `Pages` menu and create a new page.**
    5. **In the page editor find a ` Custom HTML` element.** In the element settings paste the code copied from the app.
    6. **Save the changes.**
    7. **From now on, the inline quiz will be visible on that page.**


You have created and published your first skincare routine quiz.

---
This article has a step-by-step video tutorial. It shows how to create a skincare routine quiz with the RevenueHunt app.