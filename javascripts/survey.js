document.addEventListener("DOMContentLoaded", function () {
    // Define the survey link
    const surveyLink = "https://revenuehunt.com/help-us-shape-the-future-of-our-product-recommendation-quiz-app/";

    // Create the survey link container
    const surveyContainer = document.createElement("div");
    surveyContainer.style.marginTop = "20px";
    surveyContainer.style.textAlign = "center";
    surveyContainer.style.fontSize = "16px";

    const surveyText = document.createElement("p");
    surveyText.textContent = "We value your feedback!";

    const surveyAnchor = document.createElement("a");
    surveyAnchor.href = surveyLink;
    surveyAnchor.target = "_blank"; // Open the link in a new tab
    surveyAnchor.textContent = "Take our quick survey";
    surveyAnchor.style.textDecoration = "underline";
    surveyAnchor.style.color = "#0078D4"; // Customize link color

    // Blank space for better formatting
    const blankSpace = document.createElement("div");
    blankSpace.style.height = "10px"; // Adjust space height as needed

    // Append text, link, and blank space to the container
    surveyContainer.appendChild(surveyText);
    surveyContainer.appendChild(surveyAnchor);
    surveyContainer.appendChild(blankSpace);

    // Append the survey container to each page's footer
    const mainContent = document.querySelector("main");
    if (mainContent) {
        mainContent.appendChild(surveyContainer);
    }
});

