# Feature Spec:

Office Supplies Request System

---

## 1. Problem / Whys

Currently, users request services through informal channels like chat or email.
This causes delays, missing requests, and confusion in tracking status.
A structured system will improve efficiency and transparency.
---

## 2. User Story

As a <employee at SELISE Bhutan>,
I want to <request office supplies though a form>,
So that <my request are properly tracked and approved quickly>.
---

## 3. Acceptance Criteria


- User can open the request form
- User can submit a request successfully
- Admin can approve or reject requests
- User receives status updates
- System stores request details in database

Tip:
Write measurable and testable conditions only.

---

## 4. UI Notes / Sketch


Screen 1: Login Page
- Username field
- Password field
- Login button

Screen 2: Dashboard
- Request button
- Request history list
- Status display

Screen 3: Admin Panel
- View all requests
- Approve / Reject button

(Optional)
Attach wireframe image if available:
Example: ui-sketch.png

---

## 5. Data Sketch

Define what data system stores.

Example table structure:

| Field Name | Data Type | Description |
|-----------|-----------|-------------|
| request_id | INT | Unique request ID |
| user_name | VARCHAR(100) | Name of requester |
| item_name | VARCHAR(100) | Requested item |
| quantity | INT | Number of items |
| status | ENUM | Pending / Approved / Rejected |
| created_at | DATETIME | Request timestamp |

---

## 6. Edge Cases

List unusual situations system must handle.

Example:

- User submits empty form
- User enters invalid quantity
- Duplicate request submission
- Internet disconnect during submission
- Admin approves already-approved request

---

## 7. Out of Scope

Clearly mention what this feature will NOT include.

Example:

- Payment integration
- SMS notification system
- Inventory automation
- Mobile app version

These may be future improvements.

---

## Assumptions (Optional but recommended)

Example:

- Users already have login credentials
- Admin role exists in system
- Database connection is available

---

## Future Improvements (Optional)

Example:

- Email notifications
- Mobile-friendly UI
- Export request report as PDF
- Analytics dashboard

> **Software Requirements Specification** — structured per **ISO/IEC/IEEE 29148:2018** (supersedes IEEE 830-1998).
> Used when: regulated industries (banking, medical, aviation, defence), government RFPs, long-lifecycle systems, formal contracts.
> Target length: 30–100+ pages. This template gives you the full skeleton — fill every subsection; if truly N/A, state so.

---

## § 01 · Introduction

### 1.1 · Purpose
State the purpose of this SRS and the intended readership (developers, testers, auditors, regulators, customer).

### 1.2 · Scope of the Product
- **Product name:** `<Office Supplies Request System>`
- **What the product will do:** `<The system allows employees to submit office supply requests through a structured digital form. Administrators can review, approve, or reject requests and maintain tracking records>`
- **What the product will NOT do:** `<The system will not manage supplier procurement workflows, inventory automation, payment processing, or logistics tracking. It only handles request submission and approval workflow within the organization>`
- **Benefits / goals:** 
`< Reduce manual request handling
- Improve tracking transparency
- Speed up approval workflow
- Maintain request history records
- Improve communication between employees and administrators>`
- **Applicability:** `<Target users include employees and administrators within an organization using a web-based interface accessible through modern browsers>`

### 1.3 · Definitions, Acronyms, Abbreviations
| Term | Meaning |
|------|---------|
| SRS | Software Requirements Specification |
| Admin | System administrator managing requests |
| UI | User Interface |
| DB | Database |

### 1.4 · References
1.ISO/IEC/IEEE 29148:2018 · Requirements Engineering Standard
2.Organization Internal IT Policy Manual
3.Web Browser Compatibility Standards (ECMAScript 2020+)

### 1.5 · Overview of this Document
One short paragraph: what each remaining section contains. Readers use this as a navigation map.
This document describes system overview, user roles, constraints, functional requirements, interface specifications, and verification criteria required to implement the Office Supplies Request System successfully.
---

## § 02 · Overall Description

*The "big picture" section. Non-specialists read this and specialists skim it.*

### 2.1 · Product Perspective
