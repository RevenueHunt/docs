
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

### Jump Logic

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

### Skip Logic

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