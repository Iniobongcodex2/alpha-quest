// leaderboard.js

async function loadLeaderboard() {
    try {
        // Fetch the sorted players from our Python backend
        const response = await fetch('/api/leaderboard');
        const data = await response.json();
        
        const listContainer = document.getElementById('leaderboard-list');
        listContainer.innerHTML = ''; // Clear the "Loading..." text

        if (data.leaderboard.length === 0) {
            listContainer.innerHTML = '<p>No players yet. Be the first!</p>';
            return;
        }

        // Loop through the players and create an HTML row for each
        data.leaderboard.forEach((player, index) => {
            const row = document.createElement('div');
            row.className = 'player-row';
            
            // Add a medal emoji for the top 3
            let rankDisplay = `${index + 1}.`;
            if (index === 0) rankDisplay = '🥇';
            if (index === 1) rankDisplay = '🥈';
            if (index === 2) rankDisplay = '🥉';

            row.innerHTML = `
                <span><span class="rank">${rankDisplay}</span> ${player.nickname}</span>
                <span class="xp">${player.xp} XP</span>
            `;
            listContainer.appendChild(row);
        });

    } catch (error) {
        console.error("Error loading leaderboard:", error);
        document.getElementById('leaderboard-list').innerHTML = '<p>Error loading leaderboard.</p>';
    }
}

// Run the function when the page loads
loadLeaderboard();