# Technology Environment

This document defines the primary technology systems used by Gladney Pharmaceuticals. These systems serve as the digital environment where synthetic employee activity is generated for Project NAVIDSON.

NAVIDSON observes how employees interact with enterprise systems over time in order to detect behavioral changes, interpret those changes with context, and support human-centered cybersecurity analysis.

---

# System Categories

1. Identity & Access Management
2. Productivity & Collaboration
3. Research Systems
4. Clinical & Regulatory Systems
5. Finance Systems
6. Human Resources Systems
7. Security Infrastructure
8. Data Storage & Classification

---

# Identity & Access Management

## Active Directory

Purpose:
Manages internal employee accounts, groups, and access permissions.

Typical Users:
- IT Security Administrators

Log Types:
- Account logins
- Password resets
- Group membership changes
- Privileged access events

Sensitivity:
Restricted

---

## Microsoft Entra ID

Purpose:
Manages cloud identity, single sign-on, and multi-factor authentication.

Typical Users:
- All employees
- IT Security Administrators

Log Types:
- Cloud authentication
- MFA prompts
- Conditional access events
- Suspicious sign-in alerts

Sensitivity:
Restricted

---

## VPN

Purpose:
Provides secure remote access to Gladney systems.

Typical Users:
- Remote employees
- Traveling executives
- IT Security Administrators
- Regulatory Affairs Specialists

Log Types:
- VPN connection time
- VPN duration
- Source location
- Failed connection attempts

Sensitivity:
Confidential

---

# Productivity & Collaboration

## Microsoft 365

Purpose:
Provides email, calendars, documents, and collaboration tools.

Typical Users:
- All employees

Includes:
- Outlook
- Teams
- SharePoint
- OneDrive

Log Types:
- Email metadata
- File sharing
- Calendar activity
- Teams usage
- Document collaboration

Sensitivity:
Internal to Confidential

---

# Research Systems

## Electronic Lab Notebook (ELN)

Purpose:
Stores experimental notes, research observations, and laboratory documentation.

Typical Users:
- Research Scientists
- Laboratory Technicians

Log Types:
- Notebook entries
- Document edits
- Experiment updates
- Late entries

Sensitivity:
Confidential to Trade Secret

---

## Laboratory Information Management System (LIMS)

Purpose:
Tracks samples, laboratory workflows, and experimental results.

Typical Users:
- Research Scientists
- Laboratory Technicians

Log Types:
- Sample check-ins
- Sample status changes
- Instrument results
- Quality control records

Sensitivity:
Confidential to Restricted

---

## Research Share

Purpose:
Stores research documents, datasets, internal reports, and DYLAR-X project files.

Typical Users:
- Research Scientists
- Regulatory Affairs Specialists
- Executive Leadership

Log Types:
- File opens
- File downloads
- File uploads
- Permission changes

Sensitivity:
Confidential to Trade Secret

---

## Clinical Repository

Purpose:
Stores clinical trial data, patient-related research records, and study documentation.

Typical Users:
- Research Scientists
- Regulatory Affairs Specialists
- Clinical Sciences Division

Log Types:
- Data access
- Record exports
- Document downloads
- Cross-site collaboration

Sensitivity:
Restricted

---

# Clinical & Regulatory Systems

## Regulatory Document Management System

Purpose:
Stores controlled regulatory documents, submission drafts, and compliance evidence.

Typical Users:
- Regulatory Affairs Specialists
- Executive Leadership
- Research Scientists

Log Types:
- Document reviews
- Version updates
- Approval workflows
- Document exports

Sensitivity:
Confidential to Restricted

---

## FDA Submission Portal

Purpose:
Used to prepare and submit official regulatory materials.

Typical Users:
- Regulatory Affairs Specialists

Log Types:
- Submission uploads
- Document package access
- User authentication
- Approval events

Sensitivity:
Restricted

---

## Quality Management System

Purpose:
Tracks compliance events, audits, corrective actions, and controlled procedures.

Typical Users:
- Regulatory Affairs Specialists
- Laboratory Technicians
- Research Scientists

Log Types:
- Audit records
- CAPA updates
- Procedure acknowledgments
- Training confirmations

Sensitivity:
Confidential

---

# Finance Systems

## Enterprise Resource Planning System

Purpose:
Manages purchasing, vendor records, budgets, and financial operations.

Typical Users:
- Finance Analysts
- Executive Leadership

Log Types:
- Vendor updates
- Purchase approvals
- Budget changes
- Financial report access

Sensitivity:
Confidential

---

## Payroll System

Purpose:
Processes employee payroll and compensation records.

Typical Users:
- Finance Analysts
- Human Resources Specialists

Log Types:
- Payroll access
- Compensation changes
- Employee record views
- Payroll exports

Sensitivity:
Restricted

---

## Budget Forecasting Platform

Purpose:
Supports financial planning, scenario modeling, and annual budgeting.

Typical Users:
- Finance Analysts
- Executive Leadership

Log Types:
- Forecast edits
- Scenario exports
- Budget approvals
- Executive report access

Sensitivity:
Confidential to Restricted

---

# Human Resources Systems

## Human Resources Information System (HRIS)

Purpose:
Stores employee records, job information, status changes, and personnel documentation.

Typical Users:
- Human Resources Specialists
- Finance Analysts

Log Types:
- Employee record access
- Job change updates
- Personnel file downloads
- Manager changes

Sensitivity:
Restricted

---

## Benefits Administration System

Purpose:
Manages employee benefits, open enrollment, and dependent information.

Typical Users:
- Human Resources Specialists

Log Types:
- Benefits updates
- Enrollment activity
- Dependent record access
- Benefits document downloads

Sensitivity:
Restricted

---

## Recruiting Platform

Purpose:
Tracks job applicants, interviews, hiring workflows, and recruiting events.

Typical Users:
- Human Resources Specialists
- Department Managers

Log Types:
- Applicant record access
- Interview updates
- Hiring workflow changes
- Candidate document downloads

Sensitivity:
Confidential

---

## Learning Management System

Purpose:
Tracks employee training, compliance courses, and cybersecurity awareness completion.

Typical Users:
- All employees
- Human Resources Specialists
- IT Security Administrators

Log Types:
- Training completion
- Missed training deadlines
- Course access
- Compliance reminders

Sensitivity:
Internal to Confidential

---

# Security Infrastructure

## Security Information and Event Management (SIEM)

Purpose:
Aggregates security logs from identity, endpoint, network, and cloud systems.

Typical Users:
- IT Security Administrators

Log Types:
- Security alerts
- Authentication events
- Endpoint detections
- Correlated incidents

Sensitivity:
Restricted

---

## Endpoint Detection and Response

Purpose:
Monitors employee devices for suspicious activity and malware indicators.

Typical Users:
- IT Security Administrators

Log Types:
- Device health
- Malware alerts
- Process activity
- USB device connections

Sensitivity:
Restricted

---

## Firewall Management

Purpose:
Controls and monitors traffic between Gladney networks and external systems.

Typical Users:
- IT Security Administrators

Log Types:
- Network connections
- Blocked traffic
- Rule changes
- External destination access

Sensitivity:
Restricted

---

## Backup Infrastructure

Purpose:
Maintains backups of critical research, business, and operational data.

Typical Users:
- IT Security Administrators

Log Types:
- Backup jobs
- Restore requests
- Backup failures
- Administrative access

Sensitivity:
Restricted

---

# Data Storage & Classification

## Public

Examples:
- Marketing materials
- Public website content
- Press releases

Risk Level:
Low

---

## Internal

Examples:
- Internal policies
- General meeting notes
- Standard operating procedures

Risk Level:
Moderate

---

## Confidential

Examples:
- Financial reports
- Recruiting records
- Internal research documentation
- Vendor contracts

Risk Level:
High

---

## Restricted

Examples:
- Employee PII
- Payroll data
- Clinical trial data
- Patient-related research records
- FDA submission materials

Risk Level:
Very High

---

## Trade Secret

Examples:
- DYLAR-X formulation research
- Proprietary experimental methods
- Patent strategy
- Unpublished scientific findings

Risk Level:
Critical

---

# NAVIDSON Relevance

These systems define the environment in which employee behavior is observed.

NAVIDSON will use synthetic logs from these systems to model:

- Authentication behavior
- File access behavior
- Application usage
- VPN activity
- Device behavior
- Data classification access
- Organizational context

The goal is not to label employees as malicious, but to determine when activity differs meaningfully from a user's historical baseline and whether organizational context provides a reasonable explanation.