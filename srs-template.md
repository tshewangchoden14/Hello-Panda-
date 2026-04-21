# Feature Spec:

Office Supplies Request System

---

## 1. Problem / Whys

Currently, users request services through informal channels like chat or email.
This causes delays, missing requests, and confusion in tracking status.
A structured system will improve efficiency and transparency.
---

## 2. User Story

As a employee at SELISE Bhutan,
I want to request office supplies though a form,
So that my request are properly tracked and approved quickly.
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
- **Product name:** 
Office Supplies Request System
- **What the product will do:** 
The system allows employees to submit office supply requests through a structured digital form. Administrators can review, approve, or reject requests and maintain tracking records.
- **What the product will NOT do:** 
The system will not manage supplier procurement workflows, inventory automation, payment processing, or logistics tracking. It only handles request submission and approval workflow within the organization.
- **Benefits / goals:** 
Reduce manual request handling, Improve tracking transparency, Speed up approval workflow, Maintain request history records, Improve communication between employees and administrators.
- **Applicability:** 
Target users include employees and administrators within an organization using a web-based interface accessible through modern browsers.

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
This document describes system overview, user roles, constraints, functional requirements, interface specifications, and verification criteria required to implement the Office Supplies Request System successfully.

---

## § 02 · Overall Description

### 2.1 · Product Perspective
The Office Supplies Request System is a standalone web-based internal organizational tool.

**System interfaces:**

- Organizational authentication system (optional future integration)

**User interfaces:**

- Web browser interface

**Hardware interfaces:**

- Desktop computers
- Laptops
- Mobile browsers (optional support)

**Software interfaces:**

- Web server
- Relational database (MySQL)

**Communication interfaces:**

- HTTP / HTTPS protocols

**Memory / storage constraints:**

Minimal storage required for request records.

**Operations:**

- Normal mode
- Maintenance mode

**Site adaptation:**

Admin configuration settings may differ between departments.

---

## 2.2 · Product Functions

Major system functions include:

- Employee submits supply request
- Admin views submitted requests
- Admin approves or rejects requests
- System stores request history
- Users track request status

---

## 2.3 · User Characteristics

| User Class | Description | Expertise | Frequency |
|-----------|-------------|-----------|-----------|
| Admin | Manages requests and approvals | Intermediate | Daily |
| Employee | Submits requests | Basic | Weekly |
| Auditor | Reviews request logs | Expert | Quarterly |

---

## 2.4 · Constraints

- Must operate in modern browsers
- Must follow organizational IT policies
- Must maintain audit logging capability
- Must ensure secure authentication
- Must support role-based access

---

## 2.5 · Assumptions and Dependencies

- Users already have login credentials
- Database server is available
- Stable internet connection exists
- Organization provides hosting infrastructure

---

## 2.6 · Apportioning of Requirements

Future versions may include:

- Email notifications
- Inventory integration
- Supplier management integration

---

# § 03 · Specific Requirements

## 3.1 · External Interface Requirements

### 3.1.1 · User Interfaces

The system includes:

Login screen  
Employee dashboard  
Request form  
Admin dashboard  
Approval interface  

Error messages display clearly with validation prompts.

---

### 3.1.2 · Hardware Interfaces

Supports:

Desktop computers  
Laptops  
Standard keyboard and mouse  

---

### 3.1.3 · Software Interfaces

Database: MySQL  
Server: Apache / Node.js environment  

---

### 3.1.4 · Communications Interfaces

Protocols used:

HTTPS  
REST-based internal communication  

Security:

TLS encryption required

---

## 3.2 · Functional Requirements

### FR-01 · Submit Request

**Description:** Employee submits supply request

**Inputs:**

Employee name  
Item name  
Quantity  

**Processing:**

Validate required fields  
Store request in database  

**Outputs:**

Confirmation message displayed

**Preconditions:**

User logged in

**Postconditions:**

Request stored successfully

**Error handling:**

Display validation message if fields missing

**Priority:** Must

**Traces to:** Employee request workflow requirement

---

### FR-02 · View Requests

**Description:** Admin views submitted requests

**Inputs:**

Request database records

**Processing:**

Retrieve request list

**Outputs:**

Display request table

**Preconditions:**

Admin logged in

**Postconditions:**

Requests visible

**Error handling:**

Display error if retrieval fails

**Priority:** Must

**Traces to:** Admin monitoring workflow

---

### FR-03 · Approve or Reject Request

**Description:** Admin approves or rejects requests

**Inputs:**

Request selection

**Processing:**

Update request status

**Outputs:**

Updated request status displayed

**Preconditions:**

Admin authenticated

**Postconditions:**

Request status updated

**Error handling:**

Prevent duplicate approvals

**Priority:** Must

**Traces to:** Approval workflow requirement

---

## 3.3 · Non-Functional Requirements

### 3.3.1 · Performance Requirements

Supports:

100 concurrent users  
Response time under 2 seconds  

---

### 3.3.2 · Safety Requirements

Prevent accidental deletion of request records

---

### 3.3.3 · Security Requirements

Secure login authentication  
Role-based access control  
Encrypted HTTPS communication  
Audit logging enabled  

---

### 3.3.4 · Software Quality Attributes

| Attribute | Requirement |
|----------|-------------|
| Reliability | System uptime 99% |
| Availability | 24/7 internal access |
| Maintainability | Modular architecture |
| Portability | Browser-based access |
| Usability | Minimal training required |
| Accessibility | Keyboard navigation supported |

---

### 3.3.5 · Business Rules

Only administrators can approve or reject requests

---

## 3.5 · Other Requirements

### 3.5.1 · Database Requirements

Stores:

User details  
Request details  
Approval status  
Timestamps  

---

### 3.5.2 · Internationalisation / Localisation

Supports English language initially

Future support:

Dzongkha language interface

---

### 3.5.3 · Legal, Regulatory, Compliance

Must comply with organizational IT security policies

---

# § 04 · Verification

| Req ID | Verification Method | Acceptance Criterion |
|-------|--------------------|---------------------|
| FR-01 | Test | Request saved successfully |
| FR-02 | Demonstration | Admin views request list |
| FR-03 | Test | Status updated correctly |
| Security | Inspection | HTTPS enabled |

---

# § 05 · Appendices

## A. Analysis Models

Future diagrams:

Use-case diagram  
Activity diagram  
ER diagram  

---

## B. Requirements Traceability Matrix

| Req ID | Source | Design Element | Test Case | Status |
|-------|--------|---------------|-----------|-------|
| FR-01 | Employee workflow | Request module | TC-01 | Pending |
| FR-02 | Admin workflow | Admin dashboard | TC-02 | Pending |

---

## C. Issues List

Pending:

Email notification integration decision

---

## D. Glossary

Admin: System manager  
Employee: Request creator  

---

# Changelog

v0.1 · initial draft · Author · 2026-04-21

---

# Sign-off

| Role | Name | Signature | Date |
|-----|------|-----------|------|
| Author (BA) | | | |
| Dev Lead | | | |
| QA Lead | | | |
| Architect | | | |
| Product Owner | | | |
| Compliance | | | |
| Customer Representative | | | |