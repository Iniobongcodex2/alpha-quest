// builder.js
const urlParams = new URLSearchParams(window.location.search);
const nickname = urlParams.get('nickname') || 'Explorer';

const xpElement = document.getElementById('player-xp');
const buildBtn = document.getElementById('build-btn');
const buildArea = document.getElementById('build-area');

let currentXP = 0;

async function loadPlayerData() {
    try {
        // 1. Get XP
        const playerRes = await fetch(`/api/player/${encodeURIComponent(nickname)}`);
        const playerData = await playerRes.json();
        currentXP = playerData.xp;
        xpElement.innerText = currentXP;

        // 2. Check if they already have buildings
        const buildRes = await fetch(`/api/buildings/${encodeURIComponent(nickname)}`);
        const buildData = await buildRes.json();
        
        if (buildData.buildings.includes("Library")) {
            buildArea.innerHTML = "<h2>📚 Library Built!</h2><p>Your knowledge grows.</p>";
            buildBtn.disabled = true;
            buildBtn.innerText = "Library Built";
        }

    } catch (error) {
        xpElement.innerText = "0 (Player not found)";
    }
}

async function buildStructure() {
    if (currentXP < 50) {
        alert("Not enough XP!");
        return;
    }

    try {
        const response = await fetch('/api/spend-xp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ nickname: nickname, amount: 50 })
        });

        const data = await response.json();

        if (response.ok) {
            currentXP = data.new_xp;
            xpElement.innerText = currentXP;
            buildArea.innerHTML = "<h2>📚 Library Built!</h2><p>Your knowledge grows.</p>";
            buildBtn.disabled = true;
            buildBtn.innerText = "Library Built";
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert("Server error.");
    }
}

loadPlayerData();