# Software Requirements Specification (SRS)
# Office Inventory Dashboard — User Module

---

# 1. Purpose

This document defines requirements for the User Module of the Office Inventory Dashboard system. It is intended for developers, testers, and stakeholders responsible for implementing employee request functionality.

---

# 2. Scope

The User Module allows employees to:

- Submit inventory requests
- Track request status
- View request history
- Receive approval/rejection notifications
- Submit improvement suggestions

The module does NOT allow:

- Approving requests
- Managing inventory stock
- Viewing analytics reports

---

# 3. User Roles

| Role | Description |
|------|-------------|
| Employee | Submits supply requests and tracks status |

---

# 4. Functional Requirements

## FR-U1 Submit Request

User can submit request with:

- Item name
- Quantity
- Purpose
- Urgency level

System auto-fills:

- Name
- Department
- Email

---

## FR-U2 Track Request Status

User can view:

- Pending
- Approved
- Rejected

Color codes:

Green → Approved  
Red → Rejected  
Yellow → Pending

---

## FR-U3 View Request History

User can:

- View previous requests
- Filter by date
- Filter by status

---

## FR-U4 Receive Notifications

User receives notification when:

- Request approved
- Request rejected

---

## FR-U5 Submit Suggestions

User can:

- Suggest new inventory items
- Upvote suggestions
- View popular suggestions

---

# 5. Non-Functional Requirements

Performance:

Response time < 2 seconds

Security:

Role-based login required

Usability:

Mobile responsive interface required

Availability:

Accessible during office hours minimum

---

# 6. Interface Requirements

User dashboard includes:

Navigation menu

Home  
Requests  
Inventory  
Reports  
Settings

Card layout displays:

Request status  
Progress tracker

---

# 7. Database Requirements

Stores:

User details  
Request details  
Suggestion entries  
Request status history

---

# 8. Future Improvements

Email notifications  
Mobile app version  
Request editing after submission