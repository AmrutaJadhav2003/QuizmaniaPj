// let selectedAnswers = [];
// let currentPageNumber = 1;

// function selectAnswer(buttonId, answer) {
//     const buttons = document.querySelectorAll('.answer-button');
//     buttons.forEach(button => {
//         button.classList.remove('selected');
//         button.innerHTML = button.dataset.optionText;
//     });

//     const selectedButton = document.getElementById(buttonId);
//     selectedButton.classList.add('selected');
//     selectedButton.innerHTML = `<div class="circle">&#10004;</div>${selectedButton.dataset.optionText}`;

//     selectedAnswers.push(answer);

//     updateProgressBar();
// }

// function goToNextPage(currentPageId, nextPageId) {
//     const currentPage = document.getElementById(currentPageId);
//     const nextPage = document.getElementById(nextPageId);

//     // Hide current page and show next page
//     currentPage.classList.add('hidden');
//     nextPage.classList.remove('hidden');

//     if (nextPageId === 'page3') {
//         displayResult();
//     }

//     currentPageNumber++;
//     updateProgressBar();
// }

// function displayResult() {
//     const scoreElement = document.getElementById('score');
//     const correctPredictionsElement = document.getElementById('correctPredictions');

//     const correctAnswers = selectedAnswers.filter(answer => answer === 'correct').length;
//     const totalScore = correctAnswers * 5; // Assuming 5 marks for each correct answer

//     scoreElement.textContent = `Score gained: ${totalScore}`;
//     correctPredictionsElement.textContent = `Correct predictions: ${correctAnswers}`;
// }

// function updateProgressBar() {
//     const progressBarFill = document.getElementById('progressFill');
//     const progressText = document.getElementById('progressText');
//     const totalPages = 2;

//     const progressPercentage = (currentPageNumber / totalPages) * 100;

//     if (currentPageNumber <= totalPages) {
//         progressBarFill.style.width = progressPercentage + '%';
//         progressBarFill.style.backgroundColor = '#4CAF50';
//         progressText.innerText = `${currentPageNumber}/${totalPages}`;
//     }
// }

// function updateProgressBarPage2() {
//     const currentPageNumber = 2;
//     const totalPages = 2;
//     const progressPercentage = parseFloat(localStorage.getItem('progressPercentage'));
//     const progressBarFill = document.getElementById('progressFillPage2');
//     const progressText = document.getElementById('progressTextPage2');

//     progressBarFill.style.setProperty('--totalProgress', progressPercentage);
//     progressText.innerText = `${currentPageNumber}/${totalPages}`;
// }

// function goToHomepage() {
//     window.location.href = 'quiz.html';
// }

// localStorage.clear();