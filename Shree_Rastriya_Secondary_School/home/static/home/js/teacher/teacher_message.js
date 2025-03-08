document.addEventListener('DOMContentLoaded', function () {
    const studentLinks = document.querySelectorAll('.student-list-ul a');
    const messageHistory = document.querySelector('.message_history');
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const sendButton = messageForm.querySelector('button');
    let selectedStudentId = null;

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrfToken = getCookie('csrftoken');

    studentLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            studentLinks.forEach(l => l.classList.remove('selected'));
            this.classList.add('selected');
            selectedStudentId = this.dataset.studentId;
            fetchMessages(selectedStudentId);
            messageInput.disabled = false;
            sendButton.disabled = false;
        });
    });

    function fetchMessages(studentId) {
        fetch(`/get_messages/${studentId}/`)
            .then(response => response.json())
            .then(data => {
                messageHistory.innerHTML = '';
                if (data.messages.length === 0) {
                    messageHistory.innerHTML = '<p>No messages yet.</p>';
                } else {
                    data.messages.forEach(msg => {
                        const messageDiv = document.createElement('div');
                        messageDiv.classList.add('message', msg.sender);
                        messageDiv.textContent = msg.content;
                        messageHistory.appendChild(messageDiv);
                    });
                    messageHistory.scrollTop = messageHistory.scrollHeight;
                }
            })
            .catch(error => console.error('Error fetching messages:', error));
    }

    messageForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const content = messageInput.value.trim();
        if (selectedStudentId && content) {
            fetch('/send_message/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ student_id: selectedStudentId, content: content })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        const messageDiv = document.createElement('div');
                        messageDiv.classList.add('message', 'sent');
                        messageDiv.textContent = data.message.content;
                        messageHistory.appendChild(messageDiv);
                        messageHistory.scrollTop = messageHistory.scrollHeight;
                        messageInput.value = '';
                    }
                })
                .catch(error => console.error('Error sending message:', error));
        }
    });

    const searchInput = document.getElementById('student-search');
    searchInput.addEventListener('input', function () {
        const filter = this.value.toLowerCase();
        document.querySelectorAll('.student-list-ul li').forEach(li => {
            const name = li.textContent.toLowerCase();
            li.style.display = name.includes(filter) ? '' : 'none';
        });
    });
});

