# How to Use Skip Logic

Skip Logic is a feature designed to streamline the experience of quiz or survey participants by tailoring the sequence of questions they encounter. This customization is achieved through conditional statements that govern whether a question is presented or skipped, based on the respondent's answers to preceding questions. Here's an overview on how to implement and use Skip Logic, along with examples of its application.

## Conditional Logic

![quiz builder conditional logic](/images/manual_quizbuilder_conditionallogic.png)

In the Conditional Logic tab you can branch your quiz or tell it to skip certain questions. The left menu allows you to add conditional logic rules to questions in the quiz. The right menu shows a logic tree of the quiz. Any branching you add will be reflected on the tree preview.

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

## Skip Logic

Skip Logic determines whether a question is presented or skipped based on responses to previous questions. By default, if no Skip Logic is added to a question, it will be shown.

**Add Skip Logic** - Click to add a new Skip Logic rule for the selected question.

![quiz builder conditional logic skip logic rule](/images/manual_quizbuilder_conditionallogic_skiplogicrule.png)

All the Skip Logic rules follow the same format

**IF response to** pick the question from a dropdown list

**is**/ **is not** pick a choice from the dropdown list

**THEN this question is skipped**

*In the example, if a user chooses a choice "A gift" in Question 1 "Who are you shopping for?" then Question 2 "What is your skin type?" will be skipped (it will not be shown).*

All slides that contain Skip Logic will be marked with "skip logic" text.

**+** - Adds another Skip Logic rule. Adds a new OR logical rule.

**bin** - Delete the current Skip Logic rule.

**+ add concurrent logic** - Adds a new AND logical statement to the same rule. AND conditional statements can be tricky, as both statements have to be true for the rule to take effect. For most quizzes, using the OR rule is enough.


### Adding Skip Logic to a Question

1. You can introduce Skip Logic into your quiz by accessing the [Conditional Logic settings](https://docs.revenuehunt.com/reference/quiz-builder/#conditional-logic) of a question.
2. Open the [Skip Logic](https://docs.revenuehunt.com/reference/quiz-builder/#skip-logic) tab. 
3. From here, you can create a new Skip Logic statement specifying the conditions under which the current question should be bypassed.These statements follow a simple format: 
    - IF the answer to `question X` IS EQUAL TO `choice Y`, THEN skip this question. 
    - An icon will appear next to questions with Skip Logic applied, indicating the presence of these conditional statements. 
    - Multiple Skip Logic rules can be added to any question if needed.
4. **Preview and Adjust:** Publish the changes with the top-right `Publish` button to update the preview/live quiz and test the setup.

## Examples and Applications

### Filtering Email Collection Based on Interest

**Scenario**

You want to collect emails from interested customers without deterring others.

**Implementation**

- Start with a Yes/No question asking if the customer is willing to leave their email.
- Follow up with an email input question.
- Apply Skip Logic to the email question: if the customer opts out in the previous step, they are directed straight to the results page, bypassing the email question.

### Customizing Content Based on Skin Type

**Scenario**

You want to provide personalized advice based on the customer's skin type.

**Implementation**

- Add a multiple-choice question about skin type (Dry, Normal, Oily, or Combination).
- Create separate statement questions for each skin type, detailing specific advice or information.
- Apply Skip Logic to ensure respondents see only the statement relevant to their skin type, creating a customized experience.

### Skip Logic vs. Jump Logic

The new app interface gives the option to use Jump Logic and Skip Logic. You shouldn’t combine both types of logic in the same quiz.

- **Jump Logic** creates diverging paths within a quiz based on respondent answers, allowing for a branched experience.
- **Skip Logic**, in contrast, customizes the path by omitting certain questions based on previous answers, keeping the overall sequence intact but personalized.


## Additional Resources

Understanding conditional logic, the foundation of Skip Logic, can be challenging. Resources such as [WolframAlpha](https://www.wolframalpha.com/input/?i=A+AND+%28B+OR+C%29) and [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/programming-101/boolean-logic/a/compound-booleans-with-logical-operators) offer tutorials on AND/OR logic, which can enhance your ability to create effective and complex quiz flows.

