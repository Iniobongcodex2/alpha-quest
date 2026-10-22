// app.js

let currentQuestions = [];
let currentQuestionIndex = 0;
let score = 0;

async function startGame() {
    const response = await fetch('/api/questions');
    const data = await response.json();
    
    currentQuestions = data.questions;
    currentQuestionIndex = 0;
    score = 0; // Reset score

    document.getElementById('start-btn').style.display = 'none';
    document.getElementById('game-screen').style.display = 'block';

    showQuestion();
}

function showQuestion() {
    const question = currentQuestions[currentQuestionIndex];

    // Reset UI
    document.getElementById('question-text').innerText = question.prompt;
    document.getElementById('feedback-text').innerText = "";
    document.getElementById('next-btn').style.display = 'none';

    const optionsContainer = document.getElementById('options-container');
    optionsContainer.innerHTML = '';

    question.options.forEach(option => {
        const button = document.createElement('button');
        button.innerText = option;
        button.style.padding = '10px 20px';
        button.style.fontSize = '1.1rem';
        button.style.cursor = 'pointer';
        button.style.width = '300px';
        
        button.onclick = () => checkAnswer(option, button);
        optionsContainer.appendChild(button);
    });
}

function checkAnswer(selectedOption, clickedButton) {
    const question = currentQuestions[currentQuestionIndex];
    const selectedLetter = selectedOption.charAt(0);
    const feedbackText = document.getElementById('feedback-text');

    // Disable all option buttons so they can't click twice
    const allButtons = document.getElementById('options-container').children;
    for (let btn of allButtons) {
        btn.disabled = true;
    }

    if (selectedLetter === question.correct_answer) {
        feedbackText.innerText = "✅ Correct! " + question.explanation;
        feedbackText.style.color = "#4CAF50"; // Green
        clickedButton.style.backgroundColor = "#4CAF50";
        score++;
    } else {
        feedbackText.innerText = "❌ Incorrect. The correct answer was " + question.correct_answer + ". " + question.explanation;
        feedbackText.style.color = "#F44336"; // Red
        clickedButton.style.backgroundColor = "#F44336";
    }

    // Show the Next button
    document.getElementById('next-btn').style.display = 'inline-block';
}

function nextQuestion() {
    currentQuestionIndex++;
    
    if (currentQuestionIndex < currentQuestions.length) {
        showQuestion();
    } else {
        // Game Over
        document.getElementById('question-text').innerText = "Quest Complete!";
        document.getElementById('options-container').innerHTML = "";
        document.getElementById('feedback-text').innerText = `You scored ${score} out of ${currentQuestions.length}!`;
        document.getElementById('feedback-text').style.color = "#C9A84C"; // Gold
        document.getElementById('next-btn').style.display = 'none';
    }
}