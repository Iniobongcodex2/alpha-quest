// app.js

let currentQuestions = [];
let currentQuestionIndex = 0;
let score = 0;
let playerName = "Explorer"; 

async function startGame() {
    // 1. Get the name from the input box
    const inputField = document.getElementById('nickname-input');
    if (inputField && inputField.value.trim() !== "") {
        playerName = inputField.value.trim();
    }

    // 2. Send the nickname to the backend so the Memory Vault can find their past mistakes!
    const response = await fetch(`/api/questions?nickname=${encodeURIComponent(playerName)}`);
    const data = await response.json();
    
    if (data.questions.length === 0) {
        alert("No questions available right now.");
        return;
    }

    currentQuestions = data.questions;
    currentQuestionIndex = 0;
    score = 0; 

    // 3. Hide the start screen and show the game
    document.getElementById('start-btn').style.display = 'none';
    if (inputField) inputField.style.display = 'none';
    document.getElementById('game-screen').style.display = 'block';

    showQuestion();
}

function showQuestion() {
    const question = currentQuestions[currentQuestionIndex];

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
        button.style.width = '100%';
        button.style.maxWidth = '300px';
        
        button.onclick = () => checkAnswer(option, button);
        optionsContainer.appendChild(button);
    });
}

function checkAnswer(selectedOption, clickedButton) {
    const question = currentQuestions[currentQuestionIndex];
    const selectedLetter = selectedOption.match(/[A-D]/)[0];
    const feedbackText = document.getElementById('feedback-text');

    const allButtons = document.getElementById('options-container').children;
    for (let btn of allButtons) {
        btn.disabled = true;
    }

    let isCorrect = false;

    if (selectedLetter === question.correct_answer) {
        feedbackText.innerText = "✅ Correct! " + question.explanation;
        feedbackText.style.color = "#4CAF50";
        clickedButton.style.backgroundColor = "#4CAF50";
        score++;
        isCorrect = true;
    } else {
        feedbackText.innerText = "❌ Incorrect. The correct answer was " + question.correct_answer + ". " + question.explanation;
        feedbackText.style.color = "#F44336";
        clickedButton.style.backgroundColor = "#F44336";
    }

    // SAVE ATTEMPT TO MEMORY VAULT
    fetch('/api/save-attempt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            nickname: playerName,
            question_id: question.id,
            is_correct: isCorrect
        })
    });

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
        document.getElementById('feedback-text').innerText = `You scored ${score} out of ${currentQuestions.length}! Saving progress...`;
        document.getElementById('feedback-text').style.color = "#C9A84C";
        document.getElementById('next-btn').style.display = 'none';

        const xpEarned = score * 20;
        
        // No more prompt! We already have the playerName from the start of the game.
        fetch('/api/save-score', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nickname: playerName,
                xp: xpEarned
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('feedback-text').innerText = `You scored ${score}/${currentQuestions.length}! ${data.message}`;
            
            setTimeout(() => {
                window.location.href = `builder.html?nickname=${encodeURIComponent(playerName)}`;
            }, 2000);
        })
        .catch(error => {
            console.error('Error saving score:', error);
            document.getElementById('feedback-text').innerText = `You scored ${score}/${currentQuestions.length}! (Could not save score)`;
        });
    }
}