    // =========================
// PERSISTENT TAB SELECTION
// =========================
const tabButtons = document.querySelectorAll('button[data-bs-toggle="tab"]');
tabButtons.forEach((btn) => {
  btn.addEventListener('show.bs.tab', function (e) {
    // e.target is the newly activated tab button
    // store the target's data-bs-target (the tab pane ID) in localStorage
    const newTabId = e.target.getAttribute('data-bs-target');
    localStorage.setItem('activeTabId', newTabId);

    // Console log the new tab selection as an object
    console.log('Tab changed:', { activeTabId: newTabId });
  });
});

// On page load, if there's a stored activeTabId, activate that tab
document.addEventListener('DOMContentLoaded', () => {
  const storedTabId = localStorage.getItem('activeTabId');
  if (storedTabId) {
    const tabTrigger = document.querySelector(`button[data-bs-target="${storedTabId}"]`);
    if (tabTrigger) {
      // Use Bootstrap's Tab API to show the stored tab
      const tab = new bootstrap.Tab(tabTrigger);
      tab.show();
    }
  } else {
    // If no tab is stored, default to the first tab (Submit Ticket)
    const defaultTab = document.getElementById('ticket-tab');
    if (defaultTab) {
      const tab = new bootstrap.Tab(defaultTab);
      tab.show();
    }
  }
});

// =====================================
// 1) STANDARD IT TICKET FORM SUBMISSION
// =====================================
const ticketForm = document.getElementById("ticketForm");
ticketForm.addEventListener("submit", function (event) {
  event.preventDefault();
  event.stopPropagation();

  if (!ticketForm.checkValidity()) {
    ticketForm.classList.add("was-validated");
    return;
  }

  const fileInput = document.getElementById("screenshot");
  const file = fileInput && fileInput.files[0];

  function finishTicketCreation(screenshotData) {
    const ticketData = {
      department: "IT (User Submission)",
      subDepartment: "N/A",
      issue: document.getElementById("text").value,
      priority: "N/A",
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      phone: document.getElementById("phone").value,
      address: document.getElementById("address").value,
      screenshot: screenshotData,
    };

    const ticketKey = `ticket-${Date.now()}`;
    localStorage.setItem(ticketKey, JSON.stringify(ticketData));

    // Console log the created ticketData object
    console.log("Standard IT Ticket Data Object:", ticketData);

    alert("Your IT Ticket has been submitted (standard form).");
    ticketForm.reset();
    ticketForm.classList.remove("was-validated");
  }

  // If a screenshot was uploaded, convert it to Base64
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      finishTicketCreation(e.target.result);
    };
    reader.readAsDataURL(file);
  } else {
    finishTicketCreation("");
  }
});

// ===========================
// 2) SIMPLE ADMIN LOGIN LOGIC
// ===========================
const adminLoginForm = document.getElementById("adminLoginForm");
const adminLoggedOutDiv = document.getElementById("adminLoggedOut");
const adminLoggedInDiv = document.getElementById("adminLoggedIn");

document.addEventListener("DOMContentLoaded", function () {
  // Check if admin is already logged in
  if (localStorage.getItem("isAdmin") === "true") {
    showAdminLoggedIn();
  } else {
    showAdminLoggedOut();
  }
});

function showAdminLoggedIn() {
  adminLoggedInDiv.style.display = "block";
  adminLoggedOutDiv.style.display = "none";
}

function showAdminLoggedOut() {
  adminLoggedInDiv.style.display = "none";
  adminLoggedOutDiv.style.display = "block";
}

adminLoginForm.addEventListener("submit", function (event) {
  event.preventDefault();
  event.stopPropagation();

  if (!adminLoginForm.checkValidity()) {
    adminLoginForm.classList.add("was-validated");
    return;
  }

  const username = document.getElementById("adminUsername").value;
  const password = document.getElementById("adminPassword").value;

  // Simple example: "admin"/"admin" as credentials
  if (username === "admin" && password === "admin") {
    localStorage.setItem("isAdmin", "true");
    alert("Administrator login successful.");
    showAdminLoggedIn();
    adminLoginForm.reset();
    adminLoginForm.classList.remove("was-validated");
  } else {
    alert("Invalid credentials. Please try again.");
  }
});

function adminLogout() {
  localStorage.setItem("isAdmin", "false");
  alert("You have logged out as Administrator.");
  showAdminLoggedOut();
}

// Expose the logout function globally so it can be called from button onclick
window.adminLogout = adminLogout;

// ===========================
// 3) HOSPITAL TROUBLE TICKET
// ===========================
function showHospitalSubDepartments() {
  const department = document.getElementById("hospitalDepartment").value;
  document.getElementById("hospitalMedicalSub").style.display =
    department === "Medical" ? "block" : "none";
  document.getElementById("hospitalAdminSub").style.display =
    department === "Administrative" ? "block" : "none";
  document.getElementById("hospitalSupportSub").style.display =
    department === "Support" ? "block" : "none";
}

const hospitalTicketForm = document.getElementById("hospitalTicketForm");
hospitalTicketForm.addEventListener("submit", function (event) {
  event.preventDefault();
  event.stopPropagation();

  if (!hospitalTicketForm.checkValidity()) {
    alert("Please fill out all required fields before submitting.");
    return;
  }

  /*
  // Uncomment if you add a screenshot field with ID #hospitalScreenshot
  const hospitalScreenshot = document.getElementById("hospitalScreenshot");
  const file = hospitalScreenshot && hospitalScreenshot.files[0];
  */

  function finalizeHospitalTicket(screenshotData) {
    const department = document.getElementById("hospitalDepartment").value;
    let subDepartmentValue = "";
    if (department === "Medical") {
      subDepartmentValue = document.getElementById("hospitalMedicalDepartment").value;
    } else if (department === "Administrative") {
      subDepartmentValue = document.getElementById("hospitalAdminDepartment").value;
    } else if (department === "Support") {
      subDepartmentValue = document.getElementById("hospitalSupportDepartment").value;
    }

    const jsonObject = {
      department: department,
      subDepartment: subDepartmentValue,
      issue: document.getElementById("hospitalIssue").value,
      priority: hospitalTicketForm.querySelector(
        'input[name="hospitalPriority"]:checked'
      ).value,
      screenshot: screenshotData,
    };

    const ticketKey = `ticket-${Date.now()}`;
    localStorage.setItem(ticketKey, JSON.stringify(jsonObject));

    // Console log the hospital ticketData object
    console.log("Hospital Ticket Data Object:", jsonObject);

    alert("✅ Hospital ticket has been successfully saved locally.");
    hospitalTicketForm.reset();
  }

  // If screenshot field is present & a file is provided, convert to Base64
  /*
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      finalizeHospitalTicket(e.target.result);
    };
    reader.readAsDataURL(file);
  } else {
    finalizeHospitalTicket("");
  }
  */
  finalizeHospitalTicket("");
});

// ===========================
// 4) TICKET DASHBOARD LOGIC
// ===========================
function loadTickets() {
  const cardContainer = document.getElementById("cardContainer");
  cardContainer.innerHTML = "";
  const allKeys = Object.keys(localStorage).filter((key) =>
    key.startsWith("ticket-")
  );

  if (allKeys.length === 0) {
    cardContainer.innerHTML =
      '<p class="empty-message">No tickets found in local storage.</p>';
    return;
  }

  allKeys.forEach((key) => {
    const ticketData = JSON.parse(localStorage.getItem(key)) || {};

    // Console log the loaded ticket data as an object
    console.log("Loaded Ticket from LocalStorage:", { key, ...ticketData });

    const cardDiv = document.createElement("div");
    cardDiv.classList.add("ticket-card");

    const priorityClass = ticketData.priority
      ? "priority-" + ticketData.priority
      : "priority-Low";

    cardDiv.innerHTML = `
      ${
        ticketData.screenshot
          ? `<img src="${ticketData.screenshot}" class="img-fluid mb-2" alt="Attached Screenshot" />`
          : ""
      }
      <h2>Ticket ID: ${key}</h2>
      <div class="ticket-field"><strong>Department:</strong> ${
        ticketData.department || "N/A"
      }</div>
      <div class="ticket-field"><strong>Sub-Department:</strong> ${
        ticketData.subDepartment || "N/A"
      }</div>
      <div class="ticket-field"><strong>Issue:</strong> ${
        ticketData.issue || "N/A"
      }</div>
      <div class="ticket-field">
        <strong>Priority:</strong>
        <span class="priority-indicator ${priorityClass}">${
      ticketData.priority || "N/A"
    }</span>
      </div>
      ${
        ticketData.name
          ? `<div class="ticket-field"><strong>Name:</strong> ${ticketData.name}</div>`
          : ""
      }
      ${
        ticketData.email
          ? `<div class="ticket-field"><strong>Email:</strong> ${ticketData.email}</div>`
          : ""
      }
      ${
        ticketData.phone
          ? `<div class="ticket-field"><strong>Phone:</strong> ${ticketData.phone}</div>`
          : ""
      }
      ${
        ticketData.address
          ? `<div class="ticket-field"><strong>Address:</strong> ${ticketData.address}</div>`
          : ""
      }

      <div class="ticket-actions">
        <label for="prioritySelect-${key}"><strong>Change Priority:</strong></label>
        <select id="prioritySelect-${key}" class="form-control">
          <option value="Low" ${
            ticketData.priority === "Low" ? "selected" : ""
          }>Low</option>
          <option value="Medium" ${
            ticketData.priority === "Medium" ? "selected" : ""
          }>Medium</option>
          <option value="High" ${
            ticketData.priority === "High" ? "selected" : ""
          }>High</option>
          <option value="Critical" ${
            ticketData.priority === "Critical" ? "selected" : ""
          }>Critical</option>
        </select>
        <button
          class="save-btn btn btn-primary mt-2"
          onclick="saveNewPriority('${key}')"
        >
          Save Priority
        </button>
        <button
          class="delete-btn btn btn-danger mt-2"
          onclick="deleteTicket('${key}')"
        >
          Delete Ticket
        </button>
      </div>
    `;
    cardContainer.appendChild(cardDiv);
  });
}

function saveNewPriority(key) {
  const selectEl = document.getElementById(`prioritySelect-${key}`);
  if (!selectEl) return;

  const newPriority = selectEl.value;
  const ticketData = JSON.parse(localStorage.getItem(key)) || {};
  ticketData.priority = newPriority;

  localStorage.setItem(key, JSON.stringify(ticketData));
  loadTickets();
}

function deleteTicket(key) {
  if (confirm("Are you sure you want to delete this ticket?")) {
    localStorage.removeItem(key);
    loadTickets();
  }
}

function clearAllTickets() {
  if (confirm("Are you sure you want to clear ALL tickets?")) {
    Object.keys(localStorage).forEach((key) => {
      if (key.startsWith("ticket-")) {
        localStorage.removeItem(key);
      }
    });
    loadTickets();
  }
}

window.addEventListener("load", loadTickets);

// ==========================================
// 5) FANCY CURSOR TRAIL (JS ANIMATION)
// ==========================================
(function () {
  const TRAIL_CONFIG = {
    circleSize: 10,
    circleColor: "rgba(0, 120, 255, 0.7)",
    circleBlur: "10px",
    trailLength: 15,
    fadeSpeed: 0.02,
    showCursorRing: true,
    ringSize: 10,
    ringColor: "rgba(0, 0, 100, 0.15)",
  };

  let circles = [];
  let ringCircle = null;

  function createCircle() {
    const circle = document.createElement("div");
    circle.style.position = "fixed";
    circle.style.zIndex = 99999;
    circle.style.width = TRAIL_CONFIG.circleSize * 2 + "px";
    circle.style.height = TRAIL_CONFIG.circleSize * 2 + "px";
    circle.style.borderRadius = "50%";
    circle.style.backgroundColor = TRAIL_CONFIG.circleColor;
    circle.style.pointerEvents = "none";
    if (TRAIL_CONFIG.circleBlur) {
      circle.style.boxShadow = `0 0 ${TRAIL_CONFIG.circleBlur} ${TRAIL_CONFIG.circleColor}`;
    }
    document.body.appendChild(circle);
    return circle;
  }

  function createRingCircle() {
    const ring = document.createElement("div");
    ring.style.position = "fixed";
    ring.style.zIndex = 99998;
    ring.style.width = TRAIL_CONFIG.ringSize * 2 + "px";
    ring.style.height = TRAIL_CONFIG.ringSize * 2 + "px";
    ring.style.borderRadius = "50%";
    ring.style.border = `2px solid ${TRAIL_CONFIG.circleColor}`;
    ring.style.backgroundColor = TRAIL_CONFIG.ringColor;
    ring.style.pointerEvents = "none";
    ring.style.mixBlendMode = "lighten";
    document.body.appendChild(ring);
    return ring;
  }

  function onMouseMove(e) {
    const { clientX, clientY } = e;
    if (ringCircle) {
      const ringRadius = TRAIL_CONFIG.ringSize;
      ringCircle.style.left = clientX - ringRadius + "px";
      ringCircle.style.top = clientY - ringRadius + "px";
    }

    if (circles.length >= TRAIL_CONFIG.trailLength) {
      const oldest = circles.shift();
      oldest.x = clientX;
      oldest.y = clientY;
      oldest.alpha = 1;
      circles.push(oldest);
    } else {
      const circleElem = createCircle();
      circles.push({
        elem: circleElem,
        x: clientX,
        y: clientY,
        alpha: 1,
      });
    }
  }

  function animateCircles() {
    circles.forEach((circleData) => {
      const { elem, x, y } = circleData;
      const size = TRAIL_CONFIG.circleSize;
      elem.style.left = x - size + "px";
      elem.style.top = y - size + "px";
      circleData.alpha -= TRAIL_CONFIG.fadeSpeed;
      circleData.alpha = Math.max(circleData.alpha, 0);
      elem.style.opacity = circleData.alpha;
    });
    requestAnimationFrame(animateCircles);
  }

  function initCursorTrail() {
    if (TRAIL_CONFIG.showCursorRing) {
      ringCircle = createRingCircle();
    }
    window.addEventListener("mousemove", onMouseMove);
    animateCircles();
  }

  window.addEventListener("DOMContentLoaded", initCursorTrail);
})();