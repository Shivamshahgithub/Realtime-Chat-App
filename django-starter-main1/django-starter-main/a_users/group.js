const groupName = JSON.parse(document.getElementById('group-name').textContent);
const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/groups/' + groupName + '/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat_window').innerHTML += `<li><strong>${data.username}:</strong> ${data.message}</li>`;
};

document.querySelector('#chat_message_form').onsubmit = function(e) {
    e.preventDefault();
    const messageInput = document.querySelector('input[name="message"]');
    chatSocket.send(JSON.stringify({
        'message': messageInput.value
    }));
    messageInput.value = '';
};
