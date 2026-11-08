// app.js

let currentQuestions = [];
let currentQuestionIndex = 0;
let score = 0;
let playerName = "Explorer"; 
let isBossBattle = false; // <-- NEW: Tracks if they are in a boss battle

// --- AUDIO SYNTHESIZER ---
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playSound(type) {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
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

// --- GAME LOGIC ---
async function startGame(mode = "normal") {
    isBossBattle = (mode === "boss");
    
    const inputField = document.getElementById('nickname-input');
    const avatarField = document.getElementById('avatar-select');
    const subjectField = document.getElementById('subject-select');
    
    playerName = inputField ? inputField.value.trim() : "Explorer";
    if (!playerName) playerName = "Explorer";
    
    const selectedSubject = subjectField ? subjectField.value : "All";

    // Send the mode (normal or boss) to the backend
    const response = await fetch(`/api/questions?nickname=${encodeURIComponent(playerName)}&subject=${encodeURIComponent(selectedSubject)}&mode=${mode}`);
    const data = await response.json();
    
    if (data.questions.length === 0) {
        alert("No questions available for this selection.");
        return;
    }

    currentQuestions = data.questions;
    currentQuestionIndex = 0;
    score = 0; 

    // Hide the start screen elements
    document.getElementById('start-btn').style.display = 'none';
    document.getElementById('boss-btn').style.display = 'none';
    if(inputField) inputField.style.display = 'none'; 
    if(avatarField) avatarField.parentElement.style.display = 'none'; 
    if(subjectField) subjectField.parentElement.style.display = 'none'; 
    
    document.getElementById('game-screen').style.display = 'block';

    showQuestion();
}

function showQuestion() {
    const question = currentQuestions[currentQuestionIndex];

    // Update the progress tracker!
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
        // Game Over - Save score and Redirect
        let xpEarned = score * 20;
        
        // Boss Battle Bonus!
        if (isBossBattle && score >= 12) {
            xpEarned += 100; // 100 Bonus XP for defeating the boss!
            alert("🏆 BOSS DEFEATED! You earned 100 Bonus XP!");
        }
        
        document.getElementById('question-text').innerText = "Saving progress...";
        document.getElementById('options-container').innerHTML = "";
        document.getElementById('feedback-text').innerText = "";
        document.getElementById('progress-text').innerText = "";
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
            // Redirect to Results Page with boss data!
            window.location.href = `results.html?nickname=${encodeURIComponent(playerName)}&score=${score}&total=${currentQuestions.length}&xp=${xpEarned}&boss=${isBossBattle}`;
        });
    }
}