# Employee Archetypes

This document defines the behavioral profiles used to generate synthetic employee activity for Project NAVIDSON.

Each archetype represents the expected behavior of employees within Gladney Pharmaceuticals and serves as the behavioral baseline for anomaly detection.

Rather than comparing employees to one another, NAVIDSON compares each employee against their own historical behavior while incorporating organizational context and human-centered reasoning.

---

# Contents

1. Research Scientist
2. Laboratory Technician
3. Regulatory Affairs Specialist
4. Finance Analyst
5. Human Resources Specialist
6. IT Security Administrator
7. Executive Leadership

---

## Research Scientist

Department:
Research

Employees:
140

Typical Schedule:
8:00 AM – 5:30 PM

Remote Work:
Occasional

Travel:
Scientific conferences (Low)

VPN Usage:
Low

USB Usage:
Rare

Average Files Accessed:
120/day

Primary Systems:
- Electronic Lab Notebook (ELN)
- Laboratory Information Management System (LIMS)
- Research Share
- Clinical Repository

Typical Data Classification:
- Confidential
- Restricted
- Trade Secret

Behavioral Signature:

Typical Login Time:
8:15 AM ± 20 minutes

Average Session Length:
3.5 hours

Average Daily Logins:
2

Average Files Accessed:
120 ± 30

Average Weekly VPN Usage:
1 day

Peak Activity:
9:00 AM–12:00 PM

Primary Collaboration:
Regulatory Affairs

Expected Seasonal Variation:
Higher activity before FDA submissions and scientific conferences.

Behavior Notes:

Research Scientists routinely access DYLAR-X research data, laboratory notebooks, and experimental datasets. High document access is considered normal for this role.

Common Benign Anomalies:

- Late laboratory notebook entry
- Extended laboratory sessions
- Conference travel
- Temporary collaboration with outside researchers
- Increased document access before project milestones

---

# Laboratory Technician

Department:
Research

Employees:
45

Typical Schedule:
7:00 AM – 3:30 PM

Remote Work:
Rare

Travel:
Very Rare

VPN Usage:
Very Low

USB Usage:
Occasional (Laboratory Instruments)

Average Files Accessed:
45/day

Primary Systems:
- Laboratory Information Management System (LIMS)
- Instrument Control Software
- Quality Assurance Portal
- Sample Tracking System

Typical Data Classification:
- Internal
- Confidential
  
Behavioral Signature:

Typical Login Time:
7:05 AM ± 10 minutes

Average Session Length:
6.5 hours

Average Daily Logins:
1

Average Files Accessed:
45 ± 10

Average Weekly VPN Usage:
0 days

Peak Activity:
7:30 AM–11:30 AM

Primary Collaboration:
Research Scientists

Expected Seasonal Variation:
Higher activity during active laboratory study periods and sample processing deadlines.


Behavior Notes:

Laboratory Technicians manage laboratory workflows, specimen tracking, and laboratory equipment. Their work is highly procedural with predictable daily routines.

Common Benign Anomalies:

- Delayed sample logging
- Instrument calibration delays
- Extended laboratory sessions
- Missed equipment documentation
- Temporary equipment outages

---

# Regulatory Affairs Specialist

Department:
Regulatory Affairs

Employees:
40

Typical Schedule:
8:00 AM – 5:00 PM

Remote Work:
Frequent

Travel:
FDA meetings and conferences

VPN Usage:
Moderate

USB Usage:
Rare

Average Files Accessed:
60/day

Primary Systems:
- Regulatory Document Management System
- FDA Submission Portal
- Microsoft 365
- Quality Management System

Typical Data Classification:
- Confidential
- Restricted

Behavioral Signature

Typical Login Time:
7:58 AM ± 5 minutes

Average Session Length:
4.8 hours

Average Daily Logins:
1

Average Files Accessed:
62 ± 6

Average Weekly VPN Usage:
2 days

Peak Activity:
9:00 AM–4:00 PM

Primary Collaboration:
Research Scientists
Clinical Sciences Division
Quality Assurance

Expected Seasonal Variation:
Significant increases immediately preceding FDA submission deadlines.
Behavior Notes:

Regulatory Affairs Specialists prepare FDA submissions, maintain compliance documentation, and coordinate with research teams throughout clinical development.

Common Benign Anomalies:

- Increased document activity before FDA deadlines
- Weekend work before submissions
- Temporary access to research documents
- Increased VPN usage while traveling

---

# Finance Analyst

Department:
Finance

Employees:
35

Typical Schedule:
7:30 AM – 4:30 PM

Remote Work:
Occasional

Travel:
Rare

VPN Usage:
Low

USB Usage:
Very Rare

Average Files Accessed:
40/day

Primary Systems:
- Enterprise Resource Planning (ERP)
- Financial Planning Software
- Payroll System
- Budget Forecasting Platform

Typical Data Classification:
- Confidential

Behavioral Signature:

Typical Login Time:
7:50 AM ± 10 minutes

Average Session Length:
4.5 hours

Average Daily Logins:
1

Average Files Accessed:
42 ± 8

Average Weekly VPN Usage:
1–2 days

Peak Activity:
8:30 AM–4:30 PM

Primary Collaboration:
Executive Leadership
Human Resources
Procurement

Expected Seasonal Variation:
Increased activity during month-end close, quarterly reporting, annual budgeting, external audits, and financial planning meetings.

Behavior Notes:

Finance Analysts manage budgeting, forecasting, payroll reconciliation, purchasing, and financial reporting.

Common Benign Anomalies:

- Month-end reporting spikes
- Budget planning season
- Audit preparation
- Temporary overtime during quarterly close

---

# Human Resources Specialist

Department:
Human Resources

Employees:
25

Typical Schedule:
8:00 AM – 5:00 PM

Remote Work:
Occasional

Travel:
Recruiting events

VPN Usage:
Low

USB Usage:
Rare

Average Files Accessed:
35/day

Primary Systems:
- Human Resources Information System (HRIS)
- Benefits Administration
- Payroll
- Recruiting Platform

Typical Data Classification:
- Confidential
- Restricted

Behavioral Signature:

Typical Login Time:
8:05 AM ± 15 minutes

Average Session Length:
4.2 hours

Average Daily Logins:
2

Average Files Accessed:
35 ± 10

Average Weekly VPN Usage:
1 day

Peak Activity:
9:00 AM–3:00 PM

Primary Collaboration:
Executive Leadership
Finance
Department Managers

Expected Seasonal Variation:
Increased activity during recruiting cycles, onboarding periods, annual performance reviews, benefits enrollment, and organizational restructuring.

Behavior Notes:

Human Resources Specialists manage employee records, recruiting, onboarding, benefits administration, and personnel documentation.

Common Benign Anomalies:

- Large hiring cycles
- Benefits enrollment periods
- Open enrollment document spikes
- New employee onboarding
- Missing HR documentation requiring follow-up

---

# IT Security Administrator

Department:
Information Technology

Employees:
35

Typical Schedule:
8:00 AM – 5:00 PM

On-Call:
Yes

Remote Work:
Frequent

Travel:
Occasional

VPN Usage:
Very High

USB Usage:
Occasional

Average Files Accessed:
Variable

Primary Systems:
- Active Directory
- Microsoft Entra ID
- VPN
- Security Information and Event Management (SIEM)
- Endpoint Detection and Response (EDR)
- Backup Infrastructure
- Firewall Management

Typical Data Classification:
- Confidential
- Restricted
- Trade Secret

Behavioral Signature:

Typical Login Time:
Highly Variable

Average Session Length:
2–8 hours

Average Daily Logins:
4

Average Files Accessed:
Variable

Average Weekly VPN Usage:
5 days

Peak Activity:
Maintenance windows and incident response periods

Primary Collaboration:
All Departments

Expected Seasonal Variation:
Increased activity during software deployments, security incidents, patch cycles, and infrastructure upgrades.

Behavior Notes:

IT Security Administrators maintain enterprise infrastructure, perform privileged administrative tasks, deploy software, respond to incidents, and routinely work outside normal business hours.

Common Benign Anomalies:

- Late-night maintenance
- Weekend patching
- Company-wide password resets
- Software deployments
- Emergency incident response

---

# Executive Leadership

Department:
Executive Leadership

Employees:
10

Typical Schedule:
Variable

Remote Work:
Frequent

Travel:
Frequent

VPN Usage:
Moderate

USB Usage:
Rare

Average Files Accessed:
25/day

Primary Systems:
- Executive Dashboard
- Microsoft 365
- Financial Reporting
- Board Portal

Typical Data Classification:
- Confidential
- Restricted
- Trade Secret

Behavioral Signature:

Typical Login Time:
Highly Variable

Average Session Length:
2–6 hours

Average Daily Logins:
3

Average Files Accessed:
25 ± 15

Average Weekly VPN Usage:
3–4 days

Peak Activity:
Highly variable based on travel, board meetings, investor meetings, and strategic initiatives.

Primary Collaboration:
All Departments

Expected Seasonal Variation:
Increased activity during quarterly board meetings, budgeting, mergers and acquisitions, investor presentations, and major research milestones.

Behavior Notes:

Executive Leadership accesses strategic planning documents, financial forecasts, board materials, merger discussions, and executive-level research updates.

Common Benign Anomalies:

- Extensive business travel
- After-hours document review
- Board meeting preparation
- Temporary cross-department access
- Strategic planning periods