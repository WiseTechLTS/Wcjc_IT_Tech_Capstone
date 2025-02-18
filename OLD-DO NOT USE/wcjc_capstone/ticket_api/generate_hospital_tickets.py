import json
from datetime import datetime, timedelta

# Configuration
BASE_TIME = datetime(2025, 4, 2, 8, 0)
TOTAL_TICKETS = 120  # Number of ticket/hospitalticket pairs
STATUS_CYCLE = ["open", "in_progress", "closed"]
# List of 20 incident topics to cycle through
TOPICS = [
    "Patient Fall", "Medication Error", "Equipment Failure", "Staffing Shortage", "Diagnostic Delay",
    "Treatment Delay", "Record Discrepancy", "Facility Maintenance", "Infection Control Issue", "Data Entry Error",
    "Procedure Complication", "Resource Shortage", "Patient Complaint", "Communication Breakdown", "Billing Issue",
    "Lab Result Delay", "Emergency Response Delay", "Surgery Scheduling Conflict", "Medication Supply Shortage", "Equipment Calibration Issue"
]

# This list will hold 240 objects (120 tickets and 120 hospitaltickets)
fixture_objects = []

# Generate fixture objects for each ticket/hospitalticket pair
for i in range(1, TOTAL_TICKETS + 1):
    # Calculate the created time (each ticket 5 minutes apart)
    created_time = BASE_TIME + timedelta(minutes=5 * (i - 1))
    created_iso = created_time.isoformat() + "Z"
    
    # Cycle through statuses (open, in_progress, closed)
    status = STATUS_CYCLE[(i - 1) % len(STATUS_CYCLE)]
    # Cycle through topics
    topic = TOPICS[(i - 1) % len(TOPICS)]
    # Determine sub_department (simulate distribution among 15 medical sub-departments)
    sub_department = ((i - 1) % 15) + 1
    # For closed tickets, assume the updated time is 5 minutes later than created; otherwise, same as created
    updated_iso = (created_time + timedelta(minutes=5)).isoformat() + "Z" if status == "closed" else created_iso
    
    # Build the Ticket object
    ticket_obj = {
        "model": "ticket_api.ticket",
        "pk": i,
        "fields": {
            "subject": f"Incident {i}: {topic}",
            "description": f"This is a detailed description for incident {i} regarding {topic.lower()}.",
            "sub_department": sub_department,
            "status": status,
            "created_at": created_iso,
            "updated_at": updated_iso
        }
    }
    
    # Build the corresponding HospitalTicket object
    hospitalticket_obj = {
        "model": "ticket_api.hospitalticket",
        "pk": i,
        "fields": {
            "ticket": i,
            "patient_id": f"P{i:03d}",
            "room_number": f"Room {100 + ((i - 1) % 20) + 1}",
            "additional_info": f"Additional hospital-specific info for incident {i}."
        }
    }
    
    fixture_objects.append(ticket_obj)
    fixture_objects.append(hospitalticket_obj)

# Now, split the fixture_objects list into chunks of 45 pairs (i.e. 90 objects each),
# except the final chunk, which will have the remaining objects.
chunk_size = 90  # 45 pairs * 2 objects per pair
chunks = [fixture_objects[i:i + chunk_size] for i in range(0, len(fixture_objects), chunk_size)]

# Write each chunk to its own JSON file
for idx, chunk in enumerate(chunks, start=1):
    filename = f"hospital_tickets_part{idx}.json"
    with open(filename, "w") as f:
        json.dump(chunk, f, indent=2)
    print(f"Wrote {len(chunk)} objects to {filename}")
