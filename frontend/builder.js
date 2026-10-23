// builder.js

// Get the nickname from the URL (e.g., builder.html?nickname=Iniobong)
const urlParams = new URLSearchParams(window.location.search);
const nickname = urlParams.get('nickname') || 'Explorer';

const xpElement = document.getElementById('player-xp');
const buildBtn = document.getElementById('build-btn');
const buildArea = document.getElementById('build-area');

let currentXP = 0;

// 1. Load the player's XP from the database when the page opens
async function loadPlayerData() {
    try {
        const response = await fetch(`/api/player/${encodeURIComponent(nickname)}`);
        if (!response.ok) throw new Error("Player not found");
        
        const data = await response.json();
        currentXP = data.xp;
        xpElement.innerText = currentXP;
    } catch (error) {
        xpElement.innerText = "0 (Player not found)";
        console.error("Error loading player:", error);
    }
}

// 2. Build the library and spend XP in the database
async function buildStructure() {
    if (currentXP < 50) {
        alert("Not enough XP! Go play a quest to earn more.");
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
            // Update the UI with the new XP
            currentXP = data.new_xp;
            xpElement.innerText = currentXP;
            
            // Show the library
            buildArea.innerHTML = "<h2>📚 Library Built!</h2><p>Your knowledge grows.</p>";
            buildBtn.disabled = true;
            buildBtn.innerText = "Library Built";
        } else {
            alert(data.detail || "Failed to build");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Server error while building.");
    }
}

// Initialize the page
loadPlayerData();