// profile.js
const urlParams = new URLSearchParams(window.location.search);
const nickname = urlParams.get('nickname') || 'Explorer';

async function loadProfile() {
    try {
        const response = await fetch(`/api/profile/${encodeURIComponent(nickname)}`);
        
        if (!response.ok) {
            alert("Player not found! Play a game first.");
            window.location.href = '/';
            return;
        }

        const data = await response.json();

        // Update basic info
        document.getElementById('profile-name').innerText = data.nickname;
        document.getElementById('profile-level').innerText = `Level ${data.level}`;
        
        // Calculate Accessory (Same logic as home screen)
        let accessory = "";
        if (data.level >= 10) accessory = "🧙";
        else if (data.level >= 5) accessory = "👑";
        else if (data.level >= 3) accessory = "🕶️";
        else if (data.level >= 2) accessory = "🧢";
        
        document.getElementById('profile-avatar').innerText = (data.avatar || '🦊') + accessory;

        // Update stats
        document.getElementById('stat-xp').innerText = data.xp;
        document.getElementById('stat-accuracy').innerText = `${data.accuracy}%`;
        document.getElementById('stat-questions').innerText = `${data.correct_attempts} / ${data.total_attempts}`;
        document.getElementById('stat-buildings').innerText = data.buildings_built;
        document.getElementById('stat-favorite').innerText = data.favorite_subject;

    } catch (error) {
        console.error("Error loading profile:", error);
    }
}

loadProfile();