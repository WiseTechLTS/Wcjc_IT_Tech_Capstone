/*
==========================================
🚀 Final Fixed Version of scripts.js
==========================================
This script correctly saves form data locally and fixes all issues from the previous version.
*/

// 🎟️ Handling the IT Ticket Form Submission
document.getElementById('ticketForm').addEventListener('submit', function (event) {
    event.preventDefault(); // ⛔️ Stop the form from reloading the page
    event.stopPropagation(); // 🔇 Stop the event from affecting other parts of the page

    const form = event.target;
    if (!form.checkValidity()) {
        form.classList.add('was-validated'); // 🎨 Adds validation styles
        return;
    }

    const ticketData = new FormData(form);
    const jsonObject = {}; // 🗄️ Create an empty object to store form data

    // 🔄 Convert FormData to JSON format
    ticketData.forEach((value, key) => jsonObject[key] = value);

    // 💾 Save ticket data in local storage
    localStorage.setItem('savedTicket', JSON.stringify(jsonObject));

    console.log("📩 Ticket JSON Data Saved:", jsonObject);
    console.log("⚠️ No database synced."); // Inform user that no database is used
    
    alert('✅ Ticket saved locally. No database synced.');
    
    // 🧹 Reset form after saving
    form.reset();
    form.classList.remove('was-validated');
});

// 🛠️ Handling the Admin Login Form Submission
document.getElementById('adminLoginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // ⛔️ Stop the form from reloading the page
    event.stopPropagation(); // 🔇 Stop event propagation

    const form = event.target;
    if (!form.checkValidity()) {
        form.classList.add('was-validated'); // 🎨 Adds validation styles
        return;
    }

    // 🔑 Gather the login details
    const adminData = {
        username: document.getElementById('adminUsername').value, // 🏷️ Get username
        password: document.getElementById('adminPassword').value, // 🔒 Get password
    };

    // 💾 Save login data in local storage
    localStorage.setItem('adminLogin', JSON.stringify(adminData));

    console.log("🔐 Admin Login Data Saved:", adminData);
    console.log("⚠️ No database synced."); // Inform user that no database is used
    
    alert('✅ Login data saved locally. No database synced.');
    
    // 🧹 Reset form
    form.reset();
    form.classList.remove('was-validated');
});
