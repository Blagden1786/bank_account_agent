const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

const sendBtnEnableColor = sendBtn.style.backgroundColor;  // Green color when enabled

function sendMessage(onload = false) {
    let message;

    // Get the user input if it isn't the function called when the page is loaded
    if (!onload) {
        message = userInput.value.trim();
        if (message === '') return;

        appendMessage(message, 'user-message');
        userInput.value = '';
    } else {
        // Onload message
        console.log("Onload message triggered");
        appendMessage("Hello, I am your helpful savings finder. Let's find you the account that best suits your needs.", 'bot-message');
        message = "Hello";
    }
    // Prevent user from sending multiple messages quickly
    console.log("Disabling input during processing");
    sendBtn.disabled = true;
    userInput.disabled = true;
    sendBtn.style.backgroundColor = '#ccc';

    // Call server-side agent
    console.log("Sending message to server:", message);
    fetch('agent/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')  // CSRF protection
        },
        body: `message=${encodeURIComponent(message)}`
    })
        .then(response => response.json())
        .then(data => {
            console.log("Received response from server:", data);
            if (data.reply) {
                appendMessage(data.reply, 'bot-message');
            }
        })
        .finally(() => {
            // Re-enable input after processing
            console.log("Re-enabling input after processing");
            sendBtn.disabled = false;
            userInput.disabled = false;
            sendBtn.style.backgroundColor = sendBtnEnableColor;
        });
}

// Function to get CSRF token from cookies (Django default)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function appendMessage(message, className) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', className);
    msgDiv.textContent = message;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Event listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
