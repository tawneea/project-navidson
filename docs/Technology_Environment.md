# Technology Environment

This document defines the primary enterprise systems used throughout Gladney Pharmaceuticals.

These systems form the digital environment in which **PROJECT NAVIDSON** generates synthetic employee activity, enterprise telemetry, and behavioral observations.

By modeling how employees interact with these systems over time, NAVIDSON can distinguish expected behavioral variation from activity that may warrant additional investigation.

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

## Identity and Access Management (IAM)

Purpose:
Provides centralized identity, authentication, authorization, and multi-factor authentication services.

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
Stores research documents, datasets, laboratory reports, and documentation associated with GP-217 and HELIX.

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
Stores clinical study data, research documentation, and regulated clinical records associated with HELIX.

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

## Regulatory Submission Portal

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

## Financial Planning & Analysis (FP&A) Platform

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
- GP-217 laboratory research
- HELIX development documentation
- Proprietary experimental methods
- Patent strategy
- Unpublished scientific findings

Risk Level:
Critical

---

# NAVIDSON Relevance

These enterprise systems define the environment in which employee behavior is generated and observed.

Synthetic telemetry produced by these systems forms the foundation for behavioral feature engineering throughout PROJECT NAVIDSON.

Examples include:

- Authentication activity
- File access behavior
- Application usage
- VPN activity
- Device telemetry
- Data classification access
- Cross-department collaboration
- Organizational context

Rather than treating individual events as isolated indicators, NAVIDSON evaluates behavior across multiple enterprise systems while incorporating historical baselines and organizational context.

The objective is to support explainable behavioral analysis—not automated conclusions about employee intent.