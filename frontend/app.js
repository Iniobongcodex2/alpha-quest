// app.js

let currentQuestions = [];
let currentQuestionIndex = 0;
let score = 0;
let playerName = "Explorer"; 
let isBossBattle = false; 
let isBrainRush = false;
let selectedWorld = "All";
let selectedMode = "normal";
let wrongAnswersThisGame = []; // <-- NEW: Tracks mistakes for the Results screen

// Timer Variables
let timerInterval;
let timeLeft = 15;
const TIME_LIMIT = 15;

// --- AUDIO SYNTHESIZER ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSound(type) {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const oscillator = audioCtx.createOscillator();
    const gainNode = audioCtx.createGain();
    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);
    
    if (type === 'correct') {
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(880, audioCtx.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(1200, audioCtx.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.3);
    } else if (type === 'incorrect') {
        oscillator.type = 'sawtooth';
        oscillator.frequency.setValueAtTime(150, audioCtx.currentTime);
        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.4);
    }
}

// --- MISSION BRIEFING LOGIC ---
const stories = {
    "Math World": "The Great Number Dragon has scrambled the kingdom's equations! Solve these math puzzles to restore order to the Math World.",
    "English Kingdom": "The Royal Library's words have been scattered by a mischievous wizard. Master the language to rebuild the sentences!",
    "Science Lab": "A strange chemical reaction has locked the lab doors. Answer these science questions to synthesize the key and escape!",
    "Discovery World": "You've found an ancient map with missing landmarks. Travel the globe and answer correctly to reveal the hidden locations.",
    "Logic Temple": "The Temple Guardians only let those with sharp minds pass. Solve these riddles and logic puzzles to reach the inner sanctum.",
    "All": "A powerful force has mixed all the worlds together! Face a random challenge from across the land to prove you are a true Explorer.",
    "Boss": "The ultimate challenge! The Shadow Master awaits. Answer 15 mixed questions and score high to defeat him and earn bonus XP!",
    "Rush": "Think fast! The clock is ticking. You have 15 seconds per question. How many can you answer correctly before time runs out?"
};

function showMissionBriefing(world, mode) {
    selectedWorld = world;
    selectedMode = mode;
    
    const modal = document.getElementById('mission-modal');
    const title = document.getElementById('modal-title');
    const story = document.getElementById('modal-story');

    if (mode === 'boss') {
        title.innerText = "👹 Boss Battle!";
        story.innerText = stories["Boss"];
    } else if (mode === 'rush') {
        title.innerText = "⚡ Brain Rush!";
        story.innerText = stories["Rush"];
    } else {
        title.innerText = `${world} Mission`;
        story.innerText = stories[world] || stories["All"];
    }

    modal.style.display = 'flex';
}

function beginQuiz() {
    document.getElementById('mission-modal').style.display = 'none';
    startGame(selectedMode, selectedWorld);
}

// --- GAME LOGIC ---
async function startGame(mode = "normal", subject = "All") {
    isBossBattle = (mode === "boss");
    isBrainRush = (mode === "rush");
    wrongAnswersThisGame = []; // Reset mistake tracker for the new game
    
    const inputField = document.getElementById('nickname-input');
    const avatarField = document.getElementById('avatar-select');
    
    playerName = inputField ? inputField.value.trim() : "Explorer";
    if (!playerName) playerName = "Explorer";

    const response = await fetch(`/api/questions?nickname=${encodeURIComponent(playerName)}&subject=${encodeURIComponent(subject)}&mode=${mode}`);
    const data = await response.json();
    
    if (data.questions.length === 0) {
        alert("No questions available for this selection.");
        return;
    }

    currentQuestions = data.questions;
    currentQuestionIndex = 0;
    score = 0; 

    document.getElementById('start-btn').style.display = 'none';
    document.getElementById('boss-btn').style.display = 'none';
    document.getElementById('rush-btn').style.display = 'none'; // Hide rush button
    if(inputField) inputField.style.display = 'none'; 
    if(avatarField) avatarField.parentElement.style.display = 'none'; 
    
    const worldMap = document.querySelector('.world-map');
    if (worldMap) worldMap.style.display = 'none';
    
    document.getElementById('game-screen').style.display = 'block';

    // Show timer container if in Brain Rush
    if (isBrainRush) {
        document.getElementById('timer-container').style.display = 'block';
    } else {
        document.getElementById('timer-container').style.display = 'none';
    }

    showQuestion();
}

function showQuestion() {
    clearInterval(timerInterval); // Clear any existing timer

    const question = currentQuestions[currentQuestionIndex];

    document.getElementById('progress-text').innerText = `Question ${currentQuestionIndex + 1} of ${currentQuestions.length}`;
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

    // Start the timer if in Brain Rush
    if (isBrainRush) {
        timeLeft = TIME_LIMIT;
        document.getElementById('time-left').innerText = timeLeft;
        
        timerInterval = setInterval(() => {
            timeLeft--;
            document.getElementById('time-left').innerText = timeLeft;
            
            if (timeLeft <= 0) {
                clearInterval(timerInterval);
                timeOut();
            }
        }, 1000);
    }
}

function timeOut() {
    const question = currentQuestions[currentQuestionIndex];
    const feedbackText = document.getElementById('feedback-text');
    
    playSound('incorrect');
    feedbackText.innerText = "⏰ Time's up! The correct answer was " + question.correct_answer + ". " + question.explanation;
    feedbackText.style.color = "#F44336";
    
    const allButtons = document.getElementById('options-container').children;
    for (let btn of allButtons) {
        btn.disabled = true;
        if(btn.innerText.match(/[A-D]/)[0] === question.correct_answer) {
            btn.style.backgroundColor = "#4CAF50"; // Highlight the correct answer
        }
    }

    // Add to mistake tracker
    wrongAnswersThisGame.push({
        prompt: question.prompt,
        correct_answer: question.correct_answer,
        explanation: question.explanation
    });

    // Save attempt as wrong
    fetch('/api/save-attempt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            nickname: playerName,
            question_id: question.id,
            is_correct: false
        })
    });

    document.getElementById('next-btn').style.display = 'inline-block';
}

function checkAnswer(selectedOption, clickedButton) {
    clearInterval(timerInterval); // Stop timer when they answer

    const question = currentQuestions[currentQuestionIndex];
    const selectedLetter = selectedOption.match(/[A-D]/)[0];
    const feedbackText = document.getElementById('feedback-text');

    const allButtons = document.getElementById('options-container').children;
    for (let btn of allButtons) btn.disabled = true;

    let isCorrect = false;

    if (selectedLetter === question.correct_answer) {
        playSound('correct'); 
        feedbackText.innerText = "✅ Correct! " + question.explanation;
        feedbackText.style.color = "#4CAF50";
        clickedButton.style.backgroundColor = "#4CAF50";
        clickedButton.classList.add("pop");
        score++;
        isCorrect = true;
    } else {
        playSound('incorrect'); 
        feedbackText.innerText = "❌ Incorrect. The correct answer was " + question.correct_answer + ". " + question.explanation;
        feedbackText.style.color = "#F44336";
        clickedButton.style.backgroundColor = "#F44336";
        clickedButton.classList.add("shake"); 
        
        // ADDED: Track the mistake for the Results screen
        wrongAnswersThisGame.push({
            prompt: question.prompt,
            correct_answer: question.correct_answer,
            explanation: question.explanation
        });
    }

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
        clearInterval(timerInterval); // Ensure timer stops
        
        let xpEarned = score * 20;
        
        if (isBossBattle && score >= 12) {
            xpEarned += 100; 
            alert("🏆 BOSS DEFEATED! You earned 100 Bonus XP!");
        }
        
        document.getElementById('question-text').innerText = "Saving progress...";
        document.getElementById('options-container').innerHTML = "";
        document.getElementById('feedback-text').innerText = "";
        document.getElementById('progress-text').innerText = "";
        document.getElementById('timer-container').style.display = 'none';
        document.getElementById('next-btn').style.display = 'none';

        const avatarField = document.getElementById('avatar-select');
        const selectedAvatar = avatarField ? avatarField.value : "🦊";

        fetch('/api/save-score', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nickname: playerName,
                xp: xpEarned,
                avatar: selectedAvatar
            })
        })
        .then(response => response.json())
        .then(data => {
            // ADDED: Save mistakes to sessionStorage before redirecting
            sessionStorage.setItem('gameMistakes', JSON.stringify(wrongAnswersThisGame));
            
            window.location.href = `results.html?nickname=${encodeURIComponent(playerName)}&score=${score}&total=${currentQuestions.length}&xp=${xpEarned}&boss=${isBossBattle}`;
        });
    }
}