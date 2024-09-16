alert("If you like it, please upvote")
const chatInput = document.getElementById('chat-input');  
const sendButton = document.getElementById('send-button');  
const chatBox = document.getElementById('chat-box');  
const playerInput = document.getElementById('player-input');  
const addPlayerButton = document.getElementById('add-player-button');  
const playerList = document.getElementById('player-list');  

// Event listener to send chat messages  
sendButton.addEventListener('click', () => {  
    const message = chatInput.value.trim();  
    if (message) {  
        addMessage('You', message);  
        chatInput.value = ''; // Clear input field  
    }  
});  

// Function to add a message to the chat  
function addMessage(user, message) {  
    const messageElement = document.createElement('div');  
    messageElement.classList.add('message');  
    messageElement.textContent = `${user}: ${message}`;  
    chatBox.appendChild(messageElement);  
    chatBox.scrollTop = chatBox.scrollHeight; // Auto scroll to bottom  

    // Adding a simple animation for chat messages  
    messageElement.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300 });  
}  

// Optional: Send message on Enter key press  
chatInput.addEventListener('keyup', (event) => {  
    if (event.key === 'Enter') {  
        sendButton.click();  
    }  
});  

// Event listener to add a player  
addPlayerButton.addEventListener('click', () => {  
    const playerName = playerInput.value.trim();  
    if (playerName) {  
        addPlayer(playerName);  
        playerInput.value = ''; // Clear input field  
    }  
});  

// Function to add a player to the player list  
function addPlayer(name) {  
    const playerElement = document.createElement('li');  
    playerElement.textContent = name;  
    playerList.appendChild(playerElement);  
    
    // Trigger slide-in animation for new players  
    playerElement.animate([{ transform: 'translateY(20px)', opacity: 0 }, { transform: 'translateY(0)', opacity: 1 }], { duration: 500 });  
}
