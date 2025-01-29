// ============================
// 1) Standard IT Ticket Form
// ============================
document.getElementById("ticketForm").addEventListener("submit", function (event) {
    event.preventDefault();
    event.stopPropagation();
  
    const form = event.target;
    if (!form.checkValidity()) {
      form.classList.add("was-validated");
      return;
    }
  
    // Grab references
    const screenshotField = document.getElementById("screenshot");
    const file = screenshotField && screenshotField.files[0];
  
    // Callback after reading screenshot (or skipping if none)
    function finishTicketCreation(screenshotData) {
      const ticketData = {
        department: "IT (User Submission)", // So we know it's from the IT form
        subDepartment: "N/A",
        issue: document.getElementById("text").value,
        priority: "N/A",  // No priority field on the IT form
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        address: document.getElementById("address").value,
        screenshot: screenshotData // Base64 or ""
      };
  
      // Save to localStorage under a unique key
      const ticketKey = `ticket-${Date.now()}`;
      localStorage.setItem(ticketKey, JSON.stringify(ticketData));
      console.log("=== New IT Ticket Saved ===", ticketData);
  
      // Provide user feedback
      alert("Your IT Ticket has been submitted (standard form).");
      form.reset();
      form.classList.remove("was-validated");
    }
  
    // If a screenshot was uploaded, convert it to Base64
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        finishTicketCreation(e.target.result);
      };
      reader.readAsDataURL(file);
    } else {
      // No screenshot
      finishTicketCreation("");
    }
  });
  
  // ====================
  // 2) Admin Login Form
  // ====================
  document.getElementById("adminLoginForm").addEventListener("submit", function (event) {
    event.preventDefault();
    event.stopPropagation();
  
    const form = event.target;
    if (!form.checkValidity()) {
      form.classList.add("was-validated");
      return;
    }
  
    const username = document.getElementById("adminUsername").value;
    const password = document.getElementById("adminPassword").value;
    console.log("Admin Login Attempt:", { username, password });
  
    alert("Admin login submitted. (Demo only.)");
    form.reset();
    form.classList.remove("was-validated");
  });
  
  // ============================
  // 3) Hospital Trouble Ticket
  // ============================
  function showHospitalSubDepartments() {
    const department = document.getElementById("hospitalDepartment").value;
    document.getElementById("hospitalMedicalSub").style.display =
      (department === "Medical") ? "block" : "none";
    document.getElementById("hospitalAdminSub").style.display =
      (department === "Administrative") ? "block" : "none";
    document.getElementById("hospitalSupportSub").style.display =
      (department === "Support") ? "block" : "none";
  }
  
  const hospitalTicketForm = document.getElementById("hospitalTicketForm");
  hospitalTicketForm.addEventListener("submit", function (event) {
    event.preventDefault();
    event.stopPropagation();
  
    if (!hospitalTicketForm.checkValidity()) {
      alert("Please fill out all required fields before submitting.");
      return;
    }
  
    // Gather references
    const hospitalScreenshot = document.getElementById("hospitalScreenshot");
    const file = hospitalScreenshot && hospitalScreenshot.files[0];
  
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
        priority: hospitalTicketForm.querySelector('input[name="hospitalPriority"]:checked').value,
        // Include screenshot
        screenshot: screenshotData
      };
  
      const ticketKey = `ticket-${Date.now()}`;
      localStorage.setItem(ticketKey, JSON.stringify(jsonObject));
  
      console.log("=== New Hospital Ticket Saved ===", jsonObject);
  
      alert("✅ Hospital ticket has been successfully saved locally.");
      hospitalTicketForm.reset();
    }
  
    // If a screenshot is uploaded, convert to Base64
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        finalizeHospitalTicket(e.target.result);
      };
      reader.readAsDataURL(file);
    } else {
      finalizeHospitalTicket("");
    }
  });
  
  // =============================
  // 4) Ticket Dashboard Logic
  // =============================
  function loadTickets() {
    const cardContainer = document.getElementById("cardContainer");
    cardContainer.innerHTML = "";
    const allKeys = Object.keys(localStorage).filter(key => key.startsWith("ticket-"));
    
    if (allKeys.length === 0) {
      cardContainer.innerHTML = '<p class="empty-message">No tickets found in local storage.</p>';
      return;
    }
    
    allKeys.forEach((key) => {
      const ticketData = JSON.parse(localStorage.getItem(key)) || {};
      
      const cardDiv = document.createElement("div");
      cardDiv.classList.add("ticket-card");
      
      const priorityClass = ticketData.priority ? `priority-${ticketData.priority}` : "priority-Low";
      
      cardDiv.innerHTML = `
        ${
          ticketData.screenshot
            ? `<img src="${ticketData.screenshot}" class="img-fluid mb-2" alt="Attached Screenshot">`
            : ""
        }
        <h2>Ticket ID: ${key}</h2>
        <div class="ticket-field"><strong>Department:</strong> ${ticketData.department || "N/A"}</div>
        <div class="ticket-field"><strong>Sub-Department:</strong> ${ticketData.subDepartment || "N/A"}</div>
        <div class="ticket-field"><strong>Issue:</strong> ${ticketData.issue || "N/A"}</div>
        <div class="ticket-field">
          <strong>Priority:</strong>
          <span class="priority-indicator ${priorityClass}">${ticketData.priority || "N/A"}</span>
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
            <option value="Low" ${ticketData.priority === "Low" ? "selected" : ""}>Low</option>
            <option value="Medium" ${ticketData.priority === "Medium" ? "selected" : ""}>Medium</option>
            <option value="High" ${ticketData.priority === "High" ? "selected" : ""}>High</option>
            <option value="Critical" ${ticketData.priority === "Critical" ? "selected" : ""}>Critical</option>
          </select>
          <button class="save-btn btn btn-primary mt-2" onclick="saveNewPriority('${key}')">Save Priority</button>
          <button class="delete-btn btn btn-danger mt-2" onclick="deleteTicket('${key}')">Delete Ticket</button>
        </div>
      `;
      cardContainer.appendChild(cardDiv);
    });
  }
  
  function saveNewPriority(key) {
    console.log(`saveNewPriority called for: ${key}`);
    const selectEl = document.getElementById(`prioritySelect-${key}`);
    if (!selectEl) return;
  
    const newPriority = selectEl.value;
    const ticketData = JSON.parse(localStorage.getItem(key)) || {};
  
    console.log("Ticket data before update:", ticketData);
    ticketData.priority = newPriority;
    console.log("Ticket data after update:", ticketData);
  
    localStorage.setItem(key, JSON.stringify(ticketData));
    loadTickets();
  }
  
  function deleteTicket(key) {
    console.log(`Attempting to delete ticket: ${key}`);
    if (confirm("Are you sure you want to delete this ticket?")) {
      localStorage.removeItem(key);
      console.log(`Deleted ticket: ${key}`);
      loadTickets();
    } else {
      console.log(`Deletion canceled for ticket: ${key}`);
    }
  }
  
  function clearAllTickets() {
    console.log("clearAllTickets called...");
    if (confirm("Are you sure you want to clear ALL tickets?")) {
      Object.keys(localStorage).forEach((key) => {
        if (key.startsWith("ticket-")) {
          localStorage.removeItem(key);
          console.log(`Removed: ${key}`);
        }
      });
      loadTickets();
    } else {
      console.log("Clearing all tickets was canceled by user.");
    }
  }
  
  // Load tickets on page load
  window.addEventListener("load", loadTickets);
  
  // =============================
  // 5) Fancy Cursor Trail Effect
  // =============================
  (function () {
    const TRAIL_CONFIG = {
      // Circle styling
      circleSize: 10,           
      circleColor: 'rgba(0, 120, 255, 0.7)', 
      circleBlur: '10px',       
      // Animation / fade-out
      trailLength: 15,          
      fadeSpeed: 0.02,          
      // Optional ring that follows the cursor
      showCursorRing: true,
      ringSize: 10,
      ringColor: 'rgba(0, 0, 100, 0.15)',
    };
  
    let circles = [];
    let ringCircle = null;
  
    function createCircle() {
      const circle = document.createElement('div');
      circle.style.position = 'fixed';
      circle.style.zIndex = 99999;
      circle.style.width = (TRAIL_CONFIG.circleSize * 2) + 'px';
      circle.style.height = (TRAIL_CONFIG.circleSize * 2) + 'px';
      circle.style.borderRadius = '50%';
      circle.style.backgroundColor = TRAIL_CONFIG.circleColor;
      circle.style.pointerEvents = 'none';
      if (TRAIL_CONFIG.circleBlur) {
        circle.style.boxShadow = `0 0 ${TRAIL_CONFIG.circleBlur} ${TRAIL_CONFIG.circleColor}`;
      }
      document.body.appendChild(circle);
      return circle;
    }
  
    function createRingCircle() {
      const ring = document.createElement('div');
      ring.style.position = 'fixed';
      ring.style.zIndex = 99998;
      ring.style.width = (TRAIL_CONFIG.ringSize * 2) + 'px';
      ring.style.height = (TRAIL_CONFIG.ringSize * 2) + 'px';
      ring.style.borderRadius = '50%';
      ring.style.border = `2px solid ${TRAIL_CONFIG.circleColor}`;
      ring.style.backgroundColor = TRAIL_CONFIG.ringColor;
      ring.style.pointerEvents = 'none';
      ring.style.mixBlendMode = 'lighten';
      document.body.appendChild(ring);
      return ring;
    }
  
    function onMouseMove(e) {
      const { clientX, clientY } = e;
      if (ringCircle) {
        const ringRadius = TRAIL_CONFIG.ringSize;
        ringCircle.style.left = (clientX - ringRadius) + 'px';
        ringCircle.style.top = (clientY - ringRadius) + 'px';
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
  
    function animate() {
      circles.forEach((circleData) => {
        const { elem, x, y } = circleData;
        const size = TRAIL_CONFIG.circleSize;
        elem.style.left = (x - size) + 'px';
        elem.style.top = (y - size) + 'px';
        circleData.alpha -= TRAIL_CONFIG.fadeSpeed;
        if (circleData.alpha < 0) {
          circleData.alpha = 0;
        }
        elem.style.opacity = circleData.alpha;
      });
      requestAnimationFrame(animate);
    }
  
    function initCursorTrail() {
      if (TRAIL_CONFIG.showCursorRing) {
        ringCircle = createRingCircle();
      }
      window.addEventListener('mousemove', onMouseMove);
      animate();
    }
  
    window.addEventListener('DOMContentLoaded', initCursorTrail);
  })();
  