# How to use Block Logic

Block logic is a feature of the Results Page that allows you to make blocks visible or hidden based on customer's responses.

## Results Page

In the [Results Page](https://docs.revenuehunt.com/reference/quiz-builder/#results-page) section, you can add content to the results page shown at the end of the quiz. You can adjust the results page settings and see the preview of how the results page looks like.

You can add different types of building blocks to your results page:

- **Heading Block** - Adds a new heading to your page, ideal for titles or section breaks.
- **Content Block** - Adds a new content block to your page, ideal for adding and formatting text, lists, and links.
- **HTML Block** - Adds a block where you can input custom HTML code for advanced content and styling.
- **Image Block** - Adds an embedded image block into your page. You can upload your own image. The image should be max 1000px x 1000px and max 2MB.
- **Products Block** - Adds a block specifically designed for displaying a list of recommended products.
- **Slots Block** - Adds a block specifically designed for displaying the recommended products sorted into slots. Slots allow you to group recommended products into different categories (e.g. cleanser, toner, serum, moisturizer...). Slots show the most voted products from a collection that's linked to the slot.

## Block Logic

With Block Logic you can make blocks visible or hidden based on customer's responses.

![quiz builder results page block menu](/images/manual_quizbuilder_resultspage_blockmenu.png)

**conditional logic** / **tree icon** - Opens the [Block Logic](#block-logic) menu.

![quiz builder resutls page block logic](/images/manual_quizbuilder_resultspage_blockmenu_blocklogic.png)

**Add Block Logic** - Adds a new block logic rule.

![quiz builder resutls page block logic example](/images/manual_quizbuilder_resultspage_blockmenu_blocklogic_example.png)

All the Block Logic rules follow the same format

**IF response to** pick the question from a dropdown list

**is**/ **is not** pick a choice from the dropdown list

**THEN block is** pick either **Visible** or **Hidden**

**IN ALL OTHER CASES this block is** pick pick either **Visible** or **Hidden**

*In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then this content block with text "This is content text." will be visible. If they give a different answer in Question 1 this content block will be hidden.*

- **+** - Adds another Block Logic rule. Adds a new OR logical rule.

- **bin** - Delete the current Block Logic rule.

- **+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

### Adding Block Logic to a Block

1. **Find a block**: Start by identifying or ading the block you wish to add Block Logic to. 
2. **Open Block Logic settings**: Look for a `conditional logic / tree icon` button and click it. Next, select `add Block Logic`.
3. **Add your rules**: Add you block logic rules for when the block should be visible or hidden. You can add multiple rules by clickng the `+` button.
4. **Preview and Adjust**: Publish the changes with the top-right Publish button to update the preview/live quiz and test the setup.

## Examples and Applications

### Customizing Content Based on Skin Type

You want to provide personalized advice based on the customer's skin type. Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different recommendation about their skincare is shown on the Results Page. This individualized response is made possible by Block Logic.

![how to use block logic example](/images/how to use block logic example.png)

To learn how to build such a quiz check this [step-by-step guide](https://docs.revenuehunt.com/how-to-guides/hide-content-with-logic/).


## Additional Resources

Understanding conditional logic can be challenging. Resources such as [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) offer tutorials on AND/OR logic, which can enhance your ability to create effective and complex quiz flows.