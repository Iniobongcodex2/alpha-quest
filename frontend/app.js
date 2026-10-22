// app.js

// This function runs when the "Start" button is clicked
async function startGame() {
    const response = await fetch('/api/questions');
    const data = await response.json();
    
    console.log("Questions loaded from server:", data);
    alert("Questions loaded! Check the browser console (F12) to see them.");
}