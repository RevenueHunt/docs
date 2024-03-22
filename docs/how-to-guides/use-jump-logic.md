# How to Use Jump Logic

Jump Logic is a tool designed to personalize the experience of quiz participants by guiding them down different paths based on their answers. Below, we provide a clear, step-by-step guide on how to use Jump Logic, its workings, and examples to illustrate its functionality.

## Understanding Jump Logic

Jump Logic operates on conditional statements, similar to the IF-THEN-ELSE logic found in programming. It enables the quiz creator to direct participants to different follow-up questions or content based on their responses to previous questions. This is particularly useful in creating quizzes that adapt to the user's input, offering a personalized path through the quiz.

For instance, in a skincare consult quiz, you may start with a question about the participant's skin type (Dry, Normal, Combination, or Oily). Based on the answer, Jump Logic can direct the participant to questions specifically relevant to their skin type, thereby skipping irrelevant questions and tailoring the quiz experience.

## Conditional Logic

![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

In the [Conditional Logic]() tab you can branch your quiz. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

By default, the quiz will progress from one question to another based on the question number. Conditional logic allows you to change this default behavior.

![quiz builder conditional logic preview options](/images/manual_quizbuilder_conditionallogic_previewoptions.png)

**+** - Zoom in on the logic tree preview.

**-** - Zoom out on the logic tree preview.

**[]** - Center the logic tree preview and fit into view.

Drag the logic tree with your mouse left button to navigate to specific branches.

![quiz builder quiz design switch question](/images/manual_quizbuilder_quizdesign_switchquestion.png)

The top menu allows you to switch between questions.

**arrow up** - Takes you to the question higher.

**arrow down** - Take you to the question lower.

## Jump Logic

Jump Logic allows you to route customers to different questions based on their responses.

**Add Jump Logic** - Click to add a new Jump Logic rule for the selected question.

![quiz builder conditional logic jump logic rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule.png)

All the Jump Logic rules follow the same format

**IF response to** pick the question from a dropdown list

**is**/ **is not** pick a choice from the dropdown list

**THEN go to:** pick a slide from the dropdown list or add a URL 

![quiz builder conditional logic jump logic rule go to](/images/manual_quizbuilder_conditionallogic_jumplogicrule_goto.png)

*In the example, if a user chooses a choice "Myself" in Question 1 "Who are you shopping for?" then they will be redirected to Question 2 "What is your skin type?".*

**+** - Add another Jump Logic rule. Adds a new OR logical rule.

![quiz builder conditional logic jump logic OR rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_or.png)

*In the example, if a user chooses a choice "Myself" in Question 1 "Who are you shopping for?" then they will be redirected to Question 2 "What is your skin type?" but if the user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then they will be redirected to Question 4 "What is their skin type?".*

**bin** - Delete the current Jump Logic rule.

**+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.

![quiz builder conditional logic jump logic AND rule](/images/manual_quizbuilder_conditionallogic_jumplogicrule_and.png)

*In the example, **only if** a user chooses a choice "Myself" in Question 1 "Who are you shopping for?" **and** a choice "Dry" in Question 2 "What is your skin type?" they will be redirected to Question 3 "What's your age?".*

**Always jump to:** - Select a slide or URL where the user will be always redirected after this slide.

### Adding Jump Logic to a Question

1. **Initiate Jump Logic:** Start by identifying the question you wish to add Jump Logic to. Look for a button or option labeled "add Jump Logic" or navigate to the Conditional Logic tab in your quiz setup menu.

2. **Configure the Logic:** Upon clicking the "add Jump Logic" button, you'll enter the logic configuration screen. Here, you'll define your conditional statement using the template:
    - IF the response to `question X`
    - IS EQUAL TO `choice Y`
    - THEN go to `question Z`

3. **Multiple Conditions:** You can add more than one Jump Logic rule to a single question by clicking on the big `+` button. This allows for complex paths that can direct participants to various follow-up questions based on their specific answers.

4. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

## Examples and Applications

### Quiz Flow Customization

Imagine creating a quiz that determines a personalized skincare routine. *Question 4* might ask about the participant's skin type, and depending on the answer, a different statement or recommendation about their skincare is shown. This individualized response is made possible by Jump Logic, which then continues the quiz based on the participant's specific path.

![how to use jump logic](/images/how to hide content with logic jump logic.png)

To learn how to build such a quiz check this [step-by-step guide](https://docs.revenuehunt.com/how-to-guides/hide-content-with-logic/).

### Jump Logic vs. Skip Logic

While Jump Logic and Skip Logic may seem similar, they serve distinct purposes. **Jump Logic** creates separate, divergent paths for participants based on their answers, effectively jumping to different questions or content. **Skip Logic**, on the other hand, determines if a question should be presented or skipped, maintaining a single path but customizing the questions seen by the participant. 

It's not recommended to use both Jump Logic and Skip Logic on one quiz.

## Additional Resources

Understanding conditional logic, the foundation of Jump Logic, can be challenging. Resources such as [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) offer tutorials on AND/OR logic, which can enhance your ability to create effective and complex quiz flows.

Jump Logic is a versatile tool that enriches quizzes by introducing customized paths based on participant responses. By setting up conditional statements, quiz creators can design interactive and personalized experiences, ensuring that each participant's journey through the quiz is relevant to their inputs.
