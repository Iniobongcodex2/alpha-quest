// results.js
const urlParams = new URLSearchParams(window.location.search);
const nickname = urlParams.get('nickname') || 'Explorer';
const score = urlParams.get('score') || '0';
const total = urlParams.get('total') || '10';
const xp = urlParams.get('xp') || '0';
const isBoss = urlParams.get('boss') === 'true';

document.getElementById('player-name').innerText = nickname;
document.getElementById('score-display').innerText = `${score}/${total}`;
document.getElementById('xp-display').innerText = `+${xp} XP`;

// Update the button link to pass the nickname to the builder
document.getElementById('builder-link').href = `/builder.html?nickname=${encodeURIComponent(nickname)}`;

if (isBoss) {
    document.querySelector('h1').innerText = "👹 Boss Defeated!";
    document.querySelector('h1').style.color = "#E53E3E"; // Red
}

// NEW: Load mistakes from sessionStorage
const mistakesStr = sessionStorage.getItem('gameMistakes');
if (mistakesStr) {
    const mistakes = JSON.parse(mistakesStr);
    
    if (mistakes.length > 0) {
        document.getElementById('review-section').style.display = 'block';
        const list = document.getElementById('mistakes-list');
        
        mistakes.forEach(m => {
            const item = document.createElement('div');
            item.className = 'mistake-item';
            item.innerHTML = `
                <div class="mistake-prompt">${m.prompt}</div>
                <div class="mistake-answer">Correct Answer: ${m.correct_answer}</div>
                <div class="mistake-explanation">${m.explanation}</div>
            `;
            list.appendChild(item);
        });
    }
}