---
icon: material/numeric-2
---

# Recommending a Skincare Routine with RevenueHunt app


=== "Shopify"


    In this tutorial, you’ll learn how to make and publish a short quiz that recommends the best cosmetic (skincare) products to your customers organized into near categories.

    !!! info "You’ll learn:"

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

    In this tutorial, you’ll learn how to make and publish a short quiz that recommends the best cosmetic (skincare) products to your customers organized into near categories.

    !!! info "You’ll learn:"

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


    In this tutorial, you’ll learn how to make and publish a short quiz that recommends the best cosmetic (skincare) products to your customers organized into near categories.

    !!! info "You’ll learn:"

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


    In this tutorial, you’ll learn how to make and publish a short quiz that recommends the best cosmetic (skincare) products to your customers organized into near categories.

    !!! info "You’ll learn:"

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


    In this tutorial, you’ll learn how to make and publish a short quiz that recommends the best cosmetic (skincare) products to your customers organized into near categories.

    !!! info "You’ll learn:"

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


    In this tutorial, you’ll learn how to make and publish a short quiz that recommends the best cosmetic (skincare) products to your customers organized into near categories.

    !!! info "You’ll learn:"

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

    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, it is possible to group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Check out our [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site and take the quiz to see an example.

    **Objective**: In this tutorial, you’ll learn how to build a quiz that recommends a four-step skincare routine to your customers.

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

    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, it is possible to group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Check out our [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site and take the quiz to see an example.

    **Objective**: In this tutorial, you’ll learn how to build a quiz that recommends a four-step skincare routine to your customers.

    Let’s get started.


=== "WooCommerce"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, it is possible to group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Check out our [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site and take the quiz to see an example.

    **Objective**: In this tutorial, you’ll learn how to build a quiz that recommends a four-step skincare routine to your customers.

    Let’s get started.

=== "Magento"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, it is possible to group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Check out our [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site and take the quiz to see an example.

    **Objective**: In this tutorial, you’ll learn how to build a quiz that recommends a four-step skincare routine to your customers.

    Let’s get started.

=== "BigCommerce"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, it is possible to group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Check out our [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site and take the quiz to see an example.

    **Objective**: In this tutorial, you’ll learn how to build a quiz that recommends a four-step skincare routine to your customers.

    Let’s get started.

=== "Standalone"


    If you run a cosmetics shop you may want to recommend a full routine to your customers instead of singular products. With the RevenueHunt app, it is possible to group products into slots and recommend a product for each step in your beauty routine.

    !!! tip
        Check out our [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) site and take the quiz to see an example.

    **Objective**: In this tutorial, you’ll learn how to build a quiz that recommends a four-step skincare routine to your customers.

    Let’s get started.




## Create Collections/Categories

=== "Shopify"

    1. For the quiz to work as a funnel and filter products based on the age and skin type, you need to create collections for each age group and skin type and product type.

    2. **Create Manual Collections for Age Groups:** Go to `Shopify > Products > Collections > Add collection`. Create a `Manual` collection for each age group that includes only the products that are relevant to that age group for all skin types.

        ??? example "--Teens-- Collection should include the following products:"

            | Age Group       | Dry or Normal                                                                                   | Oily                                                                                           | Combination                                                                                   |
            |------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
            | **🌟 Teens**     | **Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel**       | **Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** | **All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** |
            | **30–50**        | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | **50+**          | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |


        ??? example "--30 to 50-- Collection should include the following products:"

            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | **🌟30–50** | **Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream** | **Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion** | **Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |


        ??? example "--50+-- Collection should include the following products:"


            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | **🌟50+**   | **Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream** | **Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** | **Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel** |


        !!! tip
            Uncheck online store visibility to keep the collections hidden from your online storefront.

    3. **Create Manual Collections for Skin Types:** Go to `Shopify > Products > Collections > Add collection`. Create a `Manual` collection for each skin type that includes only the products that are relevant to that skin type.

        ??? example "--Dry or Normal Skin Type-- Collection should include the following products:"

            | Age Group | 🌟Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | **Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel** | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | **Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream** | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | **Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream** | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "--Oily Skin Type-- Collection should include the following products:"



            | Age Group | Dry or Normal | 🌟Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | **Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | **Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion** | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | **Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "--Combination Skin Type-- Collection should include the following products:" 


            | Age Group | Dry or Normal | Oily | 🌟Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | **All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion** |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | **Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin** |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | **Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel** |



    4. **Create Smart Collections for Product Types Using Tags:** Go to `Shopify > Products > Collections > Add collection`. Create a `Smart` collection for each product type based on a product tag. For example, a *Cleansers* collection should include all the products with the *Cleanser* tag. A *Toners* collection should include all the products with the *Toner* tag, etc.

        ??? example "--Cleansers Quiz-- Collection should include the following products:"

            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | **Foaming Cream Cleanser**; Aloe Soothing Toner; Vitamin C Serum; Moisturizing Cream-Gel | **Neutrogena Oil-Free Acne Face Wash**; Balancing Force Oil Control Toner; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | **All Natural Face Cleanser**; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | **Morning Cleanser**; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | **Redness-Relief Cleansing Lotion**; Balancing Force Oil Control Toner; Vitamin C Serum; Oil-Free Moisture Lotion | **Neutrogena Oil-Free Acne Face Wash**; United State Balancing Tonic; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | **Foaming Cream Cleanser**; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | **Redness-Relief Cleansing Lotion**; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | **Morning Cleanser**; Balancing Force Oil Control Toner; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "--Toners Quiz-- Collection should include the following products:"


            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; **Aloe Soothing Toner**; Vitamin C Serum; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; **Balancing Force Oil Control Toner**; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; **United State Balancing Tonic**; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; **Aloe Soothing Toner**; The Ordinary "Buffet" + Copper Peptides 1%; Relaxing Night Cream | Redness-Relief Cleansing Lotion; **Balancing Force Oil Control Toner**; Vitamin C Serum; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; **United State Balancing Tonic**; Super Antioxidant Serum; Oil-Free Moisture-Combination Skin |
            | 50+       | Foaming Cream Cleanser; **Ultra Facial Toner**; Khadi Global Natural Hyaluronic Acid Serum; Relaxing Night Cream | Redness-Relief Cleansing Lotion; **United State Balancing Tonic**; The Ordinary "Buffet" + Copper Peptides 1%; Oil-Free Moisture Lotion | Morning Cleanser; **Balancing Force Oil Control Toner**; Super Antioxidant Serum; Moisturizing Cream-Gel |

        ??? example "--Serums Quiz-- Collection should include the following products:"


            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; **Vitamin C Serum**; Moisturizing Cream-Gel | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; **Super Antioxidant Serum**; Oil-Free Moisture-Combination Skin | All Natural Face Cleanser; United State Balancing Tonic; **The Ordinary "Buffet" + Copper Peptides 1%**; Oil-Free Moisture Lotion |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; **The Ordinary "Buffet" + Copper Peptides 1%**; Relaxing Night Cream | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; **Vitamin C Serum**; Oil-Free Moisture Lotion | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; **Super Antioxidant Serum**; Oil-Free Moisture-Combination Skin |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; **Khadi Global Natural Hyaluronic Acid Serum**; Relaxing Night Cream | Redness-Relief Cleansing Lotion; United State Balancing Tonic; **The Ordinary "Buffet" + Copper Peptides 1%**; Oil-Free Moisture Lotion | Morning Cleanser; Balancing Force Oil Control Toner; **Super Antioxidant Serum**; Moisturizing Cream-Gel |



        ??? example "--Moisturizers Quiz-- Collection should include the following products:"            



            | Age Group | Dry or Normal | Oily | Combination |
            |-----------|---------------|------|-------------|
            | Teens     | Foaming Cream Cleanser; Aloe Soothing Toner; Vitamin C Serum; **Moisturizing Cream-Gel** | Neutrogena Oil-Free Acne Face Wash; Balancing Force Oil Control Toner; Super Antioxidant Serum; **Oil-Free Moisture-Combination Skin** | All Natural Face Cleanser; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; **Oil-Free Moisture Lotion** |
            | 30–50     | Morning Cleanser; Aloe Soothing Toner; The Ordinary "Buffet" + Copper Peptides 1%; **Relaxing Night Cream** | Redness-Relief Cleansing Lotion; Balancing Force Oil Control Toner; Vitamin C Serum; **Oil-Free Moisture Lotion** | Neutrogena Oil-Free Acne Face Wash; United State Balancing Tonic; Super Antioxidant Serum; **Oil-Free Moisture-Combination Skin** |
            | 50+       | Foaming Cream Cleanser; Ultra Facial Toner; Khadi Global Natural Hyaluronic Acid Serum; **Relaxing Night Cream** | Redness-Relief Cleansing Lotion; United State Balancing Tonic; The Ordinary "Buffet" + Copper Peptides 1%; **Oil-Free Moisture Lotion** | Morning Cleanser; Balancing Force Oil Control Toner; Super Antioxidant Serum; **Moisturizing Cream-Gel** |





=== "Shopify (Legacy)"

    1. In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers. 
    2. For the slots to work correctly, you’ll have to **create four collections** and include all the corresponding products in them. For example:
        - a *Cleansers* collection should have all the cleansing products, 
        - a *Toners* collection should have all the toning products, 
        - a *Serums* collection should have all the serums, etc.
    3. To create a collection, click on the top-right button. Check [this article](https://help.shopify.com/en/manual/products/collections) for detailed instructions on managing collections in Shopify.
    4. Give it a name and a description. 
    5. Next, you’ll select how to add products to a collection. You can do that **manually**, selecting each product one by one, or you can make an **automatic collection** based on a product tag. 
    6. To create a *Cleansers* collection, we’ll choose the tag to be equal to the word `cleanser`. Shopify will automatically add all the products with this tag to the collection. 
    7. You can create the toners, serums and moisturizer collections the same way.
    8. You can have more than one collection that includes some of the same products. An *anti-aging* or *oily skin* collection can be composed of several cleansers, serums or moisturizers.

=== "WooCommerce"

    1. In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers. 
    2. For the slots to work correctly, you’ll have to **create four categories** and include all the corresponding products in them. For example:
        - a *Cleansers* category should have all the cleansing products, 
        - a *Toners* category should have all the toning products, 
        - a *Serums* category should have all the serums, etc.
    3. To create a category, check [this article](https://woocommerce.com/document/managing-product-taxonomies/#product-categories) for detailed instructions on managing categories in WooCommerce.

=== "Magento"

    1. In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers. 
    2. For the slots to work correctly, you’ll have to **create four categories** and include all the corresponding products in them. For example:
        - a *Cleansers* category should have all the cleansing products, 
        - a *Toners* category should have all the toning products, 
        - a *Serums* category should have all the serums, etc.
    3. To create a category, check [this article](https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/categories/categories) for detailed instructions on managing categories in Magento.

=== "BigCommerce"

    1. In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers. 
    2. For the slots to work correctly, you’ll have to **create four categories** and include all the corresponding products in them. For example:
        - a *Cleansers* category should have all the cleansing products, 
        - a *Toners* category should have all the toning products, 
        - a *Serums* category should have all the serums, etc.
    3. To create a category, check [this article](https://support.bigcommerce.com/s/article/Product-Categories?language=en_US) for detailed instructions on managing categories in BigCommerce.

=== "Standalone"

    1. In the [Skincare Quiz Demo](https://skincarequiz.myshopify.com/) shop, there are four types of skincare products: cleansers, toners, serums, and moisturizers. 
    2. For the slots to work correctly, you’ll have to **create four collections** and include all the corresponding products in them. For example:
        - a *Cleansers* collection should have all the cleansing products, 
        - a *Toners* collection should have all the toning products, 
        - a *Serums* collection should have all the serums, etc.
    3. To create a collection, go to the [Success Checklist](/reference/dashboard/#success-checklist) and open the `Catalogue` by clicking `view products`. For each category, create a collection in your Standalone account via the Catalogue tab or a Google Product Feed with the right products.

## Sync

=== "Shopify"


    Once you’ve made changes to your products and collections in Shopify, the RevenueHunt app will automatically detect the changes and sync them with the app.

    !!! tip

        If you don't see the new items in the app catalog, you can run quick catalog import from the [App Settings > Catalogue](/reference/app-settings/#catalogue) page.


=== "Shopify (Legacy)"

    Once you’ve made changes to your products and collections, you should [sync them](/how-to-guides/sync-catalog/) with the app. 

    1. The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).
    2. The sync may take between 30 to 60 minutes.
    3. Once it’s finished, all your products and collections will be up to date in the app.

    !!! info
        Your store is also fully synced every 24 hours.


=== "WooCommerce"


    Once you’ve made changes to your products and collections/categories, you should [sync them](/how-to-guides/sync-catalog/) with the app. 

    1. The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).
    2. The sync may take between 30 to 60 minutes.
    3. Once it’s finished, all your products and collections will be up to date in the app.

    !!! info
        Your store is also fully synced every 24 hours.

=== "Magento"


    Once you’ve made changes to your products and collections/categories, you should [sync them](/how-to-guides/sync-catalog/) with the app. 

    1. The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).
    2. The sync may take between 30 to 60 minutes.
    3. Once it’s finished, all your products and collections will be up to date in the app.

    !!! info
        Your store is also fully synced every 24 hours.

=== "BigCommerce"


    Once you’ve made changes to your products and collections/categories, you should [sync them](/how-to-guides/sync-catalog/) with the app. 

    1. The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).
    2. The sync may take between 30 to 60 minutes.
    3. Once it’s finished, all your products and collections will be up to date in the app.

    !!! info
        Your store is also fully synced every 24 hours.

=== "Standalone"

    Once you’ve made changes to your products and collections/categories, you should [sync them](/how-to-guides/sync-catalog/) with the app. 

    1. The process is done automatically in the background but to make it faster, you can hit the [sync button](/how-to-guides/sync-catalog/) in the [Success Checklist](/reference/dashboard/#success-checklist).
    2. The sync may take between 30 to 60 minutes.
    3. Once it’s finished, all your products and collections will be up to date in the app.

    !!! info
        Your store is also fully synced every 24 hours.



## Build the Quiz

=== "Shopify"

    Now you can build your quiz. 

    1. You can start from scratch or use one of our [pre-designed Skincare templates](/reference/dashboard/#new-quiz).

        !!! tip
            Check out our [previous step-by-step tutorial](/tutorials/making-first-quiz/) to learn how to use the [Quiz Builder](/reference/quiz-builder/).

    2. Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.

        - Use a [`Multiple-choice question`](/reference/quiz-builder/questions/#multiple-choice) to find out the client’s **age** and **skin type**.
        - Use a [`Name question`](/reference/quiz-builder/questions/#name) to make the quiz personal.
        - Finish the quiz with an [`Email question`](/reference/quiz-builder/questions/#email). Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "Shopify (Legacy)"

    Now you can build your quiz. 

    1. You can start from scratch or use one of our [pre-designed Skincare templates](/reference/dashboard/#new-quiz).
    
        !!! tip
            Check out our [previous step-by-step tutorial](/tutorials/making-first-quiz/) to learn how to use the [Quiz Builder](/reference/quiz-builder/).
    
    2. Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.
    
        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the client’s age, skin type, skin concerns or the environment they live in.
        - Additionally, a skin sensitivity question will be added. In the [next section](#exclude-products) of this tutorial, you’ll learn how to [exclude products](/how-to-guides/recommend-products/#exclusion) containing allergens from your recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "WooCommerce"


    Now you can build your quiz. 

    1. You can start from scratch or use one of our [pre-designed Skincare templates](/reference/dashboard/#new-quiz).
    
        !!! tip
            Check out our [previous step-by-step tutorial](/tutorials/making-first-quiz/) to learn how to use the [Quiz Builder](/reference/quiz-builder/).
    
    2. Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.
    
        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the client’s age, skin type, skin concerns or the environment they live in.
        - Additionally, a skin sensitivity question will be added. In the [next section](#exclude-products) of this tutorial, you’ll learn how to [exclude products](/how-to-guides/recommend-products/#exclusion) containing allergens from your recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.



=== "Magento"


    Now you can build your quiz. 

    1. You can start from scratch or use one of our [pre-designed Skincare templates](/reference/dashboard/#new-quiz).
    
        !!! tip
            Check out our [previous step-by-step tutorial](/tutorials/making-first-quiz/) to learn how to use the [Quiz Builder](/reference/quiz-builder/).
    
    2. Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.
    
        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the client’s age, skin type, skin concerns or the environment they live in.
        - Additionally, a skin sensitivity question will be added. In the [next section](#exclude-products) of this tutorial, you’ll learn how to [exclude products](/how-to-guides/recommend-products/#exclusion) containing allergens from your recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "BigCommerce"


    Now you can build your quiz. 

    1. You can start from scratch or use one of our [pre-designed Skincare templates](/reference/dashboard/#new-quiz).
    
        !!! tip
            Check out our [previous step-by-step tutorial](/tutorials/making-first-quiz/) to learn how to use the [Quiz Builder](/reference/quiz-builder/).
    
    2. Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.
    
        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the client’s age, skin type, skin concerns or the environment they live in.
        - Additionally, a skin sensitivity question will be added. In the [next section](#exclude-products) of this tutorial, you’ll learn how to [exclude products](/how-to-guides/recommend-products/#exclusion) containing allergens from your recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.


=== "Standalone"


    Now you can build your quiz. 

    1. You can start from scratch or use one of our [pre-designed Skincare templates](/reference/dashboard/#new-quiz).
    
        !!! tip
            Check out our [previous step-by-step tutorial](/tutorials/making-first-quiz/) to learn how to use the [Quiz Builder](/reference/quiz-builder/).
    
    2. Start building the quiz by [adding simple questions](/reference/quiz-builder/questions/#question-types) relevant to the customer.
    
        - Use a `Name question` to make the quiz personal.
        - `Multiple-choice questions` can be useful in finding out the client’s age, skin type, skin concerns or the environment they live in.
        - Additionally, a skin sensitivity question will be added. In the [next section](#exclude-products) of this tutorial, you’ll learn how to [exclude products](/how-to-guides/recommend-products/#exclusion) containing allergens from your recommendations.
        - Finish the quiz with an `email question`. Quiz responses can be sent to your mailing list or CRM for segmented retargeting.




## Quiz Design

=== "Shopify"


    1. In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.
    2. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make it pop.


=== "Shopify (Legacy)"

    1. In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.
    2. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make it pop.

=== "WooCommerce"


    1. In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.
    2. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make it pop.

=== "Magento"


    1. In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.
    2. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make it pop.

=== "BigCommerce"


    1. In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.
    2. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make it pop.

=== "Standalone"


    1. In the [Quiz Design](/reference/quiz-builder/quiz-design/) tab, you can change the look and feel of the quiz.
    2. You can even [add custom CSS code](/how-to-guides/customize-quiz-design/#add-custom-css-code) to make it pop.



## Upvote Collections/Categories

=== "Shopify"


    Once your quiz is built and styled, you should add products or collections to individual choices.

    !!! warning
        It's recommended to either link products **or** a collection to each choice. Don't mix them. 
        
        If a product is upvoted in a choice but it is also in a collection that is linked to that choice, it **will receive 2 votes from the same choice**, which can skew the results. 
        
        For that reason, we recommend either linking individual products to a choice or a dedicated **single** collection to a choice.

    1. To do that, go to the [Questions](/reference/quiz-builder/questions/) tab and select a choice. This will open the Choice settings.
    2. Under [Choice settings](/reference/quiz-builder/questions/#choice-settings), find the `Upvoting` section and click `Upvote > Collections`.
    3. For the age question, you can link the `Teens`, `30-50` and `50+` collections created earlier to each respective choice.
    4. Then, link the `Skin type` collections to the choices in the Skin type question. For example, link the `Dry or Normal` collection to the `Dry` and `Normal` choices. Link the `Combination` collection to the `Combination` choice. Link the `Oily` collection to the `Oily` choice.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 

        - Products/Collections of products are linked to each choice.
        - When a customer picks that choice all the linked products receive one vote.
        - This includes all the products inside the linked collection. 
        - At the end, the results page will show slots with products sorted by the number of votes.



=== "Shopify (Legacy)"

    Once your quiz is built and styled, you should add products and collections to individual choices.

    1. To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab. 
    2. For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.
    3. Then, let’s link the *skin type* collections/categories.
    4. You can link one or more collections/categories to the same choice.
    5. Continue like this and make sure that each choice in the quiz has products or collections/categories linked, otherwise you may end up with empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one vote.
        - This includes all the products inside the linked collection. 
        - At the end, the results page will show slots with products sorted by the number of votes.


=== "WooCommerce"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab. 
    2. For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.
    3. Then, let’s link the *skin type* collections/categories.
    4. You can link one or more collections/categories to the same choice.
    5. Continue like this and make sure that each choice in the quiz has products or collections/categories linked, otherwise you may end up with empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one vote.
        - This includes all the products inside the linked collection. 
        - At the end, the results page will show slots with products sorted by the number of votes.



=== "Magento"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab. 
    2. For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.
    3. Then, let’s link the *skin type* collections/categories.
    4. You can link one or more collections/categories to the same choice.
    5. Continue like this and make sure that each choice in the quiz has products or collections/categories linked, otherwise you may end up with empty results.

    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one vote.
        - This includes all the products inside the linked collection. 
        - At the end, the results page will show slots with products sorted by the number of votes.



=== "BigCommerce"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab. 
    2. For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.
    3. Then, let’s link the *skin type* collections/categories.
    4. You can link one or more collections/categories to the same choice.
    5. Continue like this and make sure that each choice in the quiz has products or collections/categories linked, otherwise you may end up with empty results.
    
    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one vote.
        - This includes all the products inside the linked collection. 
        - At the end, the results page will show slots with products sorted by the number of votes.



=== "Standalone"


    Once your quiz is built and styled, you should add products and categories to individual choices.

    1. To do that, go to the [Quiz Builder](/reference/quiz-builder/) and open the [Link Collections/Categories](/reference/quiz-builder/link-collections/) tab. 
    2. For the age question, you can link the *youth* and *anti-aging* collections/categories created earlier.
    3. Then, let’s link the *skin type* collections/categories.
    4. You can link one or more collections/categories to the same choice.
    5. Continue like this and make sure that each choice in the quiz has products or collections/categories linked, otherwise you may end up with empty results.
    
    !!! info "Product recommendation algorithm"

        The product recommendation algorithm works like a [voting system](/how-to-guides/recommend-products/). 

        - Products are linked to each choice.
        - When a customer picks that choice all the linked products receive one vote.
        - This includes all the products inside the linked collection. 
        - At the end, the results page will show slots with products sorted by the number of votes.





## Exclude Products

=== "Shopify"

    No need to exclude products. The product matrix will recommend the correct products based on the customer's answers.


=== "Shopify (Legacy)"

    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/recommend-products/#exclusion) feature. 

    1. To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question. 
    2. Tap on the greyed `exclude products` text and a white bar will appear. 
    3. Simply add the products that contain an allergen.

    Now, when a customer says he’s sensitive to *aloe vera*, all the products that contain it will be excluded from the possible recommendations. 

    !!! warning

        ❗Be careful when using exclusions. Once a product has been excluded it won't show on the results page, even if it was upvoted in another question.

=== "WooCommerce"



    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/recommend-products/#exclusion) feature. 

    1. To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question. 
    2. Tap on the greyed `exclude products` text and a white bar will appear. 
    3. Simply add the products that contain an allergen.

    Now, when a customer says he’s sensitive to *aloe vera*, all the products that contain it will be excluded from the possible recommendations. 

    !!! warning

        ❗Be careful when using exclusions. Once a product has been excluded it won't show on the results page, even if it was upvoted in another question.


=== "Magento"


    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/recommend-products/#exclusion) feature. 

    1. To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question. 
    2. Tap on the greyed `exclude products` text and a white bar will appear. 
    3. Simply add the products that contain an allergen.

    Now, when a customer says he’s sensitive to *aloe vera*, all the products that contain it will be excluded from the possible recommendations. 

    !!! warning

        ❗Be careful when using exclusions. Once a product has been excluded it won't show on the results page, even if it was upvoted in another question.


=== "BigCommerce"


    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/recommend-products/#exclusion) feature. 

    1. To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question. 
    2. Tap on the greyed `exclude products` text and a white bar will appear. 
    3. Simply add the products that contain an allergen.

    Now, when a customer says he’s sensitive to *aloe vera*, all the products that contain it will be excluded from the possible recommendations. 

    !!! warning

        ❗Be careful when using exclusions. Once a product has been excluded it won't show on the results page, even if it was upvoted in another question.


=== "Standalone"


    Remember the sensitivity question asked at the end of the quiz? To remove harmful products from the recommendations use the [`exclude products`](/how-to-guides/recommend-products/#exclusion) feature. 

    1. To exclude a product go to the [Link Products](/reference/quiz-builder/link-products/) tab and select a question. 
    2. Tap on the greyed `exclude products` text and a white bar will appear. 
    3. Simply add the products that contain an allergen.

    Now, when a customer says he’s sensitive to *aloe vera*, all the products that contain it will be excluded from the possible recommendations. 

    !!! warning

        ❗Be careful when using exclusions. Once a product has been excluded it won't show on the results page, even if it was upvoted in another question.



## Edit the Results Page

=== "Shopify"


    It’s time to edit the [Results Page](/reference/quiz-builder/results-page/). 

    1. Add a heading, a logo or a text block to customize the page. For example, you can add a text block to include more information about the recommended skincare routine.

        !!! tip
            Check the [previous tutorial](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. **Add Product Block**: Include a `Product Block` to display the recommended routine. In `Slot settings` set the `Max. recommended items` to four.
    3. **Preview the quiz**: Update the preview/with the top-right `Save` button and click `Preview` to test the quiz. Take the quiz a few times to check if the recommended products are displayed in accordance with the product matrix.


=== "Shopify (Legacy)"

    It’s time to edit the [Results Page](/reference/quiz-builder/results-page/). 

    1. Add a heading, a logo or a content block to customize the page.

        !!! tip
            Check the [previous tutorial](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    
    2. To make the page more attractive, let’s add a `content block`. In this block, we’ll describe every step in the beauty routine. 
    3. Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text. 

    The page is almost done. 

=== "WooCommerce"


    It’s time to edit the [Results Page](/reference/quiz-builder/results-page/). 

    1. Add a heading, a logo or a content block to customize the page.  

        !!! tip
            Check the [previous tutorial](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. To make the page more attractive, let’s add a `content block`. In this block, we’ll describe every step in the beauty routine. 
    3. Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text. 

    The page is almost done. 

=== "Magento"


    It’s time to edit the [Results Page](/reference/quiz-builder/results-page/). 

    1. Add a heading, a logo or a content block to customize the page.
    
        !!! tip
            Check the [previous tutorial](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. To make the page more attractive, let’s add a `content block`. In this block, we’ll describe every step in the beauty routine. 
    3. Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text. 

    The page is almost done. 

=== "BigCommerce"


    It’s time to edit the [Results Page](/reference/quiz-builder/results-page/). 

    1. Add a heading, a logo or a content block to customize the page.
    
        !!! tip
            Check the [previous tutorial](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. To make the page more attractive, let’s add a `content block`. In this block, we’ll describe every step in the beauty routine. 
    3. Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text. 

    The page is almost done. 

=== "Standalone"


    It’s time to edit the [Results Page](/reference/quiz-builder/results-page/). 

    1. Add a heading, a logo or a content block to customize the page.
    
        !!! tip
            Check the [previous tutorial](/tutorials/making-first-quiz/) to see examples of different blocks being used.
    2. To make the page more attractive, let’s add a `content block`. In this block, we’ll describe every step in the beauty routine. 
    3. Remember to use [Markdown language](/how-to-guides/use-markdown/) to style your text. 

    The page is almost done. 







## Add Slots

=== "Shopify"


    Now let’s sort the recommended products into clear steps/categories. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.

    1. Use `+ Add slot` to add extra slots to your Product Block on the Results page. You'll need 4 slots in total.    
    2. In [Slot settings](/reference/quiz-builder/questions/#block-settings) you can:
        - Edit the slot name, 
        - Add a description,
        - And select how many products should be recommended in each slot. Set the `Max. recommended items` to 1 for each slot.
    3. Slots won’t work as expected unless you `Add segments` to each of them. It’s how they know which products to choose. 

        Open the [Slot settings](/reference/quiz-builder/questions/#block-settings), scroll down to the `Add segments` section and click `Add > Collection`.

        - Add the `Cleansers Quiz` smart collection in the Cleansers Slot
        - Add the `Toners Quiz` smart collection in the Toners Slot
        - Add the `Serums Quiz` smart collection in the Serum Slot,
        - Add the `Moisturizers Quiz` smart collection in the Moisturizer Slot.

    4. Save the changes with the top-right `Save` button.


=== "Shopify (Legacy)"

    Now let’s add a space for products.

    1. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.
    2. Use `+` to add a `Product Slots Block` and create four different slots for each of the products. 
    3. In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:
        - Edit the slot name, 
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. Slots won’t work unless you `include collections/categories` to each of them. It’s how they know which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. Make sure that the products in these collections/categories are [linked to the answers](#link-collections) in the quiz. Otherwise, the slots will produce empty results.
    6. Follow the same steps to create a morning routine.

    Et voila! You’ve just created a dynamic result page for your beauty quiz!

=== "WooCommerce"


    Now let’s add a space for products.

    1. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.
    2. Use `+` to add a `Product Slots Block` and create four different slots for each of the products. 
    3. In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:
        - Edit the slot name, 
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. Slots won’t work unless you `include collections/categories` to each of them. It’s how they know which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. Make sure that the products in these collections/categories are [linked to the answers](#link-collections) in the quiz. Otherwise, the slots will produce empty results.
    6. Follow the same steps to create a morning routine.

    Et voila! You’ve just created a dynamic result page for your beauty quiz!



=== "Magento"


    Now let’s add a space for products.

    1. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.
    2. Use `+` to add a `Product Slots Block` and create four different slots for each of the products. 
    3. In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:
        - Edit the slot name, 
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. Slots won’t work unless you `include collections/categories` to each of them. It’s how they know which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. Make sure that the products in these collections/categories are [linked to the answers](#link-collections) in the quiz. Otherwise, the slots will produce empty results.
    6. Follow the same steps to create a morning routine.

    Et voila! You’ve just created a dynamic result page for your beauty quiz!



=== "BigCommerce"


    Now let’s add a space for products.

    1. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.
    2. Use `+` to add a `Product Slots Block` and create four different slots for each of the products. 
    3. In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:
        - Edit the slot name, 
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. Slots won’t work unless you `include collections/categories` to each of them. It’s how they know which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. Make sure that the products in these collections/categories are [linked to the answers](#link-collections) in the quiz. Otherwise, the slots will produce empty results.
    6. Follow the same steps to create a morning routine.

    Et voila! You’ve just created a dynamic result page for your beauty quiz!



=== "Standalone"


    Now let’s add a space for products.

    1. As a skincare store, you’d like to recommend a routine composed of a cleanser, a toner, a serum, and a moisturizer.
    2. Use `+` to add a `Product Slots Block` and create four different slots for each of the products. 
    3. In [product slot settings](/reference/quiz-builder/questions/#block-settings) you can:
        - Edit the slot name, 
        - Add a description,
        - And select how many products should be recommended in each slot.
    4. Slots won’t work unless you `include collections/categories` to each of them. It’s how they know which products to choose.
        - Include the *Cleansers* collection/category in the Cleansers Slot
        - Include the *Toners* collection/category in the Toners Slot
        - Include the *Serums* collection/category in the Serum Slot, etc.
    5. Make sure that the products in these collections/categories are [linked to the answers](#link-collections) in the quiz. Otherwise, the slots will produce empty results.
    6. Follow the same steps to create a morning routine.

    Et voila! You’ve just created a dynamic result page for your beauty quiz!


## Preview the quiz

=== "Shopify"


    1. Update the preview with the top-right `Save` button.
    2. You can test the quiz again by clicking the `Preview` button.
    3. Take the quiz a few times to check if the correct products are recommended based on the product matrix.


=== "Shopify (Legacy)"

    1. Update the preview/live quiz with the top-right `Publish` button.
    2. You can test the quiz by clicking the `Preview`/`Test Quiz` button.
    3. Take the quiz a few times to check if the correct products are recommended.


=== "WooCommerce"


    1. Update the preview/live quiz with the top-right `Publish` button.
    2. You can test the quiz by clicking the `Preview`/`Test Quiz` button.
    3. Take the quiz a few times to check if the correct products are recommended.

=== "Magento"

    1. Update the preview/live quiz with the top-right `Publish` button.
    2. You can test the quiz by clicking the `Preview`/`Test Quiz` button.
    3. Take the quiz a few times to check if the correct products are recommended.

=== "BigCommerce"


    1. Update the preview/live quiz with the top-right `Publish` button.
    2. You can test the quiz by clicking the `Preview`/`Test Quiz` button.
    3. Take the quiz a few times to check if the correct products are recommended.

=== "Standalone"


    1. Update the preview/live quiz with the top-right `Publish` button.
    2. You can test the quiz by clicking the `Preview`/`Test Quiz` button.
    3. Take the quiz a few times to check if the correct products are recommended.

## Publish


=== "Shopify"


    Now you’re ready to publish the quiz on your website. Let’s add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page). 

    1. Go to the [`Publish`](/reference/quiz-builder/share-publish/) section and check the instructions for `Add the quiz to a dedicated landing page`.
    2. **Create a new page template**: 
        - In Shopify go to `Online Store > Theme > Customize`. 
        - Under Home page top menu select `Pages > Add new page template`. Give the template a name. 
        - In the page template editor, add a section. From `Apps` menu select the `Inline Quiz` by RevenueHunt. 
        - In the Inline Quiz settings, select the quiz formatting (for example, you can make the quiz full width). 
        - Save the template with the top-right `Save` button.
    3. **Create a new page**: 
        - Next, head over to Shopify `Online Store > Pages` and create a new page.
        - Apply the quiz template to the page.
        - Set the page visibility to `Visibe
    4. **Add the quiz to the menu**: 
        - Next open Shopify `Content > Menus`. 
        - Select the Main menu and add a new item. 
        Give it a name (for example `New Quiz Page`) and add a link to the page created in the previous step.
        - Save the changes with the top-right `Save` button.
    5. From now on, the inline quiz will be visible on that page.


=== "Shopify (Legacy)"

    Now you’re ready to publish the quiz on your website. Let’s add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page). 

    1. To do that, go to the [`Share`](/reference/quiz-builder/share-publish/) tab and select the `Inline` publish option.
    2. Click `Show Instructions for Legacy Themes`.
    3. Adjust the quiz’s width and height and click `Get code` to generate a code. 
    3. Copy the code and navigate to your `Online Store > Pages` in Shopify. 
    4. Add a new page and give it a name. 
    5. Click the `Show HTML` button and paste the code copied from the app.
    6. Make sure to `save` the changes.

=== "WooCommerce"


    Now you’re ready to publish the quiz on your website. Let’s add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page). 

    1. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    2. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    3. In WordPress, open `Pages` and click `Add New Page`.
    4. In the editor, add a page title. Then, find a `Custom HTML` element and add it to the page in a place where you want the quiz to show.
    5. In the element, paste the code copied from the app.
    6. Save the changes and `update` the page.
    7. From now on, the inline quiz will be visible on that page.

=== "Magento"


    Now you’re ready to publish the quiz on your website. Let’s add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page). 

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your Magento dashbaord go to `Content` > `Pages`. Click `Add New Page`.
    5. Edit the Page Title and open the `Content` tab. Click `Edit with Page Builder`. 
    6. Select `Elements` > `Rows` and drag a row into the canvas. 
    7. Next open `Elements` and pick `HTML Code`. Drag the `HTML Code` onto the Row.
    8. Click the gear icon to open `HTML settings`.
    9. Under `Enter HTML, CSS or JavaScript code` paste the HTML code copied from the app. 
    10. Remember to save the changes.
    11. From now on, the inline quiz will be visible on that page.

=== "BigCommerce"


    Now you’re ready to publish the quiz on your website. Let’s add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page). 

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In BigCommerce, go to `Storefront` > `Web Pages`. Click `Create a Web Page`.
    5. Under `Web Page Details` > `Page Content` switch to the `HTML` editor. Paste the HTML code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that page.

=== "Standalone"


    Now you’re ready to publish the quiz on your website. Let’s add it [inline with a new page](/how-to-guides/publish-quiz-inline/#embedding-an-inline-quiz-on-a-new-page). 

    1. Add the following embed.js script before the `</head>` close tag in the header.
        ```html
        <script src="https://admin.revenuehunt.com/embed.js" async></script>
        ```
        Without it, the quiz won't be loaded on your website.
    2. **Obtain Inline Embed Code**: From the quiz builder, click [`Share`](/reference/quiz-builder/share-publish/), select [`Inline`](/reference/quiz-builder/share-publish/#inline) mode.
    3. Edit the inline quiz settings and click `Get the code`. Copy the HTML embed code.
    4. In your store customization options find the `Pages` menu and create a new page.
    5. In the page editor find a ` Custom HTML` element. In the element settings paste the code copied from the app.
    6. Save the changes.
    7. From now on, the inline quiz will be visible on that page.


Congratulations! You’ve just created and published your first skincare routine quiz!

---
This article explains provides a step by step video tutorial on how to create a skincare routine quiz with the Revenue Hunt app.