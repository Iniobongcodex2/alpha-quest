// shop.js

const urlParams = new URLSearchParams(window.location.search);
const nickname = urlParams.get('nickname') || 'Explorer';

const xpElement = document.getElementById('player-xp');
const shopGrid = document.getElementById('shop-grid');
const backLink = document.querySelector('.back-link');

let currentXP = 0;
let currentAvatar = "🦊"; // Default

// The list of premium avatars for sale
const shopAvatars = [
    { id: "dragon", icon: "🐉", name: "Dragon", cost: 100 },
    { id: "robot", icon: "🤖", name: "Robot", cost: 150 },
    { id: "alien", icon: "👽", name: "Alien", cost: 200 },
    { id: "unicorn", icon: "🦄", name: "Unicorn", cost: 250 },
    { id: "ninja", icon: "🥷", name: "Ninja", cost: 300 },
    { id: "wizard", icon: "🧙‍♂️", name: "Wizard", cost: 400 }
];

async function loadShop() {
    // Update the back link to include the nickname
    backLink.href = `/?nickname=${encodeURIComponent(nickname)}`;

    try {
        // Fetch the player's data to get their XP and current avatar
        const response = await fetch(`/api/player/${encodeURIComponent(nickname)}`);
        
        if (response.ok) {
            const playerData = await response.json();
            currentXP = playerData.xp;
            currentAvatar = playerData.avatar;
            xpElement.innerText = currentXP;
        } else {
            // Player doesn't exist yet, start them at 0 XP
            currentXP = 0;
            xpElement.innerText = currentXP;
        }

        renderAvatars();
    } catch (error) {
        console.error("Error loading shop:", error);
        xpElement.innerText = "Error";
    }
}

function renderAvatars() {
    shopGrid.innerHTML = ''; // Clear loading state

    shopAvatars.forEach(avatar => {
        const card = document.createElement('div');
        card.className = 'avatar-card';

        // Check if the player already owns this avatar
        const isOwned = (currentAvatar === avatar.icon);
        // Check if they can afford it
        const canAfford = (currentXP >= avatar.cost);

        // Create the card HTML
        card.innerHTML = `
            <div class="avatar-icon">${avatar.icon}</div>
            <div class="avatar-name">${avatar.name}</div>
            <div class="avatar-cost">${avatar.cost} XP</div>
            <button class="buy-btn" 
                    id="btn-${avatar.id}" 
                    onclick="buyAvatar('${avatar.icon}', ${avatar.cost})"
                    ${isOwned || !canAfford ? 'disabled' : ''}>
                ${isOwned ? 'Owned' : (canAfford ? 'Buy' : 'Need XP')}
            </button>
        `;

        shopGrid.appendChild(card);
    });
}

async function buyAvatar(icon, cost) {
    if (currentXP < cost) {
        alert("You don't have enough XP!");
        return;
    }

    const confirmBuy = confirm(`Are you sure you want to buy this avatar for ${cost} XP?`);
    if (!confirmBuy) return;

    try {
        const response = await fetch('/api/buy-avatar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                nickname: nickname,
                avatar: icon,
                cost: cost
            })
        });

        const data = await response.json();

        if (response.ok) {
            // Update local data
            currentXP = data.new_xp;
            currentAvatar = icon;
            
            // Update UI
            xpElement.innerText = currentXP;
            renderAvatars(); // Re-render to update the buttons
            
            alert("🎉 Avatar purchased successfully! You can now use it on the home screen.");
        } else {
            alert(data.detail || "Failed to purchase avatar.");
        }
    } catch (error) {
        console.error("Error buying avatar:", error);
        alert("Server error while purchasing.");
    }
}

// Start loading when the page opens
loadShop();