/*
==========================================
❌ Old Incomplete Version of scripts.js
==========================================
This script had multiple issues that were fixed in the final version.
*/

// 🚨 Issue #1: Tried to send form data to an invalid API endpoint
// ❌ The fetch request below attempts to send data to 'http://your-vps-url.com',
//    which is a placeholder and does not actually exist. This resulted in a 'net::ERR_NAME_NOT_RESOLVED' error.
document.getElementById('ticketForm').addEventListener('submit', function(event) {
    event.preventDefault(); // ⛔️ Prevents the page from reloading
    event.stopPropagation(); // 🔇 Stops event bubbling

    const form = event.target;
    if (!form.checkValidity()) {
        form.classList.add('was-validated'); // 🎨 Adds validation styles
        return;
    }

    const ticketData = new FormData(form);

    console.log('Ticket Data:');
    for (let [key, value] of ticketData.entries()) {
        console.log(`${key}:`, value); // 📝 Logs the form data but doesn't store it properly
    }

    // ❌ Issue #2: Data was not stored locally
    // The script only logs form data, but does not save it for future use.
    
    fetch('http://your-vps-url.com/api/tickets', {
        method: 'POST',
        body: ticketData,
    })
    .then(response => {
        if (response.ok) {
            alert('Ticket submitted successfully!');
            form.reset(); // ✅ This part correctly resets the form
            form.classList.remove('was-validated');
        } else {
            alert('Failed to submit ticket. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error); // ❌ Issue #3: No error handling for failed network requests
        alert('An error occurred. Please try again later.');
    });
});

// 🚨 Issue #4: Incomplete admin login submission function
document.getElementById('adminLoginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // ⛔️ Prevents default behavior
    event.stopPropagation();

    const form = event.target;
    if (!form.checkValidity()) {
        form.classList.add('was-validated'); // 🎨 Adds validation styles
        return;
    }

    // ❌ Issue #5: Syntax error in storing admin login data
    // The object below is missing proper syntax, causing a script failure.
    const adminData = {} // Missing proper object structure
        username: document.get // ❌ This line is incomplete and causes a syntax error

    // ❌ Issue #6: No local storage for login credentials
    // The script does not store admin login data anywhere, meaning the login is lost on refresh.
});