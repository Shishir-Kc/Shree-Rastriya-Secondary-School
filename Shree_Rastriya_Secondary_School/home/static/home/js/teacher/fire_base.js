// messaging.requestPermission()
//     .then(() => messaging.getToken())
//     .then((token) => {
//         console.log("FCM Token:", token);
//         // Send this token to your Django backend
//         fetch('/save_fcm_token/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': getCSRFToken()
//             },
//             body: JSON.stringify({ token: token })
//         });
//     })
//     .catch((error) => console.error("Permission denied", error));

//     // Function to get CSRF token from cookies (Django's default storage)
//     function getCSRFToken() {
//         let cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             let cookie = cookies[i].trim();
//             if (cookie.startsWith('csrftoken=')) {
//                 return cookie.substring('csrftoken='.length);
//             }
//         }
//         return '';
//     }

//     function sendTestNotification() {
//         fetch('/send_notification/', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': getCSRFToken()  // Attach CSRF token here
//             },
//             body: JSON.stringify({
//                 title: "Hello!",
//                 body: "This is a test notification.",
//                 token: localStorage.getItem("fcm_token") // Use the stored token
//             })
//         })
//         .then(response => response.json())
//         .then(data => console.log("Notification Response:", data))
//         .catch(error => console.error("Error sending notification:", error));
//     }
    

