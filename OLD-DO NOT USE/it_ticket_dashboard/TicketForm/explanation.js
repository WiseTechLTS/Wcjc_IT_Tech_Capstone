/**
 * ==============================================
 * 📜 Fully Explained IT Ticket and Admin Login Script
 * ==============================================
 * 
 * This script manages two forms:
 * 1. IT Ticket Form - Saves ticket details locally in the browser.
 * 2. Admin Login Form - Saves login details locally in the browser.
 * 
 * 🚀 Why Local Storage?
 * - It allows us to temporarily store form data without needing a server.
 * - This is useful for offline use or basic testing before connecting to a backend.
 * 
 * 🛠️ Changeable Values:
 * - The form and field selectors are in `changeable_values.js`
 * - These can be modified to match different form structures.
 */

// 🎟️ Handling the IT Ticket Form Submission
document.getElementById('ticketForm').addEventListener('submit', function (event) {
    event.preventDefault(); // ⛔️ Prevents the form from reloading the page after submission
    event.stopPropagation(); // 🔇 Stops the event from affecting other elements on the page

    const form = event.target; // 📋            
    
    if (!form.checkValidity()) { // ✅ Checks if all required fields are filled correctly. The ! is a logical NOT operator; Meaning if the form is NOT valid, then...
        form.classList.add('was-validated'); // 🎨 Adds visual feedback for validation. form.classList.add() adds a class to the form element, which triggers the browser to show validation styles
        return; // 🛑 Stops the function if validation fails
    }

    const ticketData = new FormData(form); // 📩 Captures all form inputs
    const jsonObject = {}; // 🗄️ Creates an empty object to store form data

    // 🔄 Converts FormData to JSON format
    ticketData.forEach((value, key) => jsonObject[key] = value);

    // 💾 Saves ticket data to local storage (temporary storage in the browser)
    localStorage.setItem('savedTicket', JSON.stringify(jsonObject));

    console.log("📩 Ticket JSON Data Saved:", jsonObject);
    console.log("⚠️ No database synced."); // 🚨 This is just a local save, not a server sync
    
    alert('✅ Ticket saved locally. No database synced.'); // 📢 Alerts the user
    
    // 🧹 Clears the form after saving
    form.reset(); // 🆕 Resets all fields to blank
    form.classList.remove('was-validated'); // 🚀 Removes validation styles
});

// 🛠️ Handling the Admin Login Form Submission
document.getElementById('adminLoginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // ⛔️ Stops the form from reloading
    event.stopPropagation(); // 🔇 Prevents interference with other events

    const form = event.target; // 📋 Gets reference to the login form
    
    if (!form.checkValidity()) { // ✅ Ensures the form is properly filled
        form.classList.add('was-validated'); // 🎨 Adds validation feedback
        return; // 🛑 Stops execution if validation fails
    }

    // 🔑 Collects user login details
    const adminData = {
        username: document.getElementById('adminUsername').value, // 📛 Username input
        password: document.getElementById('adminPassword').value, // 🔑 Password input
    };

    // 💾 Saves login data in local storage (temporary browser memory)
    localStorage.setItem('adminLogin', JSON.stringify(adminData));

    console.log("🔐 Admin Login Data Saved:", adminData);
    console.log("⚠️ No database synced."); // 🚨 Not connected to a backend yet
    
    alert('✅ Login data saved locally. No database synced.'); // 📢 Notify user
    
    // 🧹 Clears the form after submission
    form.reset(); // 🆕 Clears input fields
    form.classList.remove('was-validated'); // 🚀 Removes validation indicators
});

/**
 * 🔎 Key Takeaways:
 * - `event.preventDefault()` ensures the form doesn’t reload the page.
 * - `event.stopPropagation()` prevents the event from affecting other parts of the page.
 * - `localStorage.setItem()` saves data so it persists when the page reloads.
 * - Forms are validated before saving data, ensuring users provide required details.
 * - Messages and alerts inform users that data is saved locally and not on a server.
 * 
 * 🏆 Next Steps:
 * - Connect this script to a backend API to process tickets and login credentials.
 * - Secure user credentials by hashing passwords before storage.
 * - Improve UX by displaying stored tickets and login attempts dynamically.
 */


// Changeable values without affecting function

const API_BASE_URL = 'http://your-vps-url.com/api'; // Change to match your server's URL

const SUCCESS_TICKET_MESSAGE = 'Ticket submitted successfully!'; // Change to customize user feedback
const ERROR_TICKET_MESSAGE = 'Failed to submit ticket. Please try again.';

const SUCCESS_LOGIN_MESSAGE = 'Login successful!'; // Customize login success message
const ERROR_LOGIN_MESSAGE = 'Login failed. Please check your credentials.';
const LOGIN_REDIRECT_URL = '/admin/dashboard'; // Change to match your actual dashboard URL

const FORM_SELECTOR = { 
    ticket: 'ticketForm', // Change if the form ID changes in HTML
    admin: 'adminLoginForm' // Change if the form ID changes in HTML
};

const FIELD_SELECTOR = {
    username: 'adminUsername', // Change if input field ID is different
    password: 'adminPassword'  // Change if input field ID is different
};

const API_ENDPOINTS = {
    submitTicket: `${API_BASE_URL}/tickets`, // Ticket submission URL
    adminLogin: `${API_BASE_URL}/admin/login` // Admin login URL
};

// These variables can be used throughout the script to maintain flexibility
