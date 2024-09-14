function sendMessage() {
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value.trim();

    if (message) {
        const chatBody = document.querySelector('.chat-body');
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.innerText = message;
        chatBody.appendChild(messageElement);
        messageInput.value = '';
    }
}
