# Organizational Events

This document defines recurring and one-time organizational events that influence employee behavior throughout Gladney Pharmaceuticals.

Project NAVIDSON uses these events to introduce realistic behavioral variation into the synthetic dataset. Rather than generating random anomalies, employee behavior changes in response to meaningful organizational activity.

Organizational events provide context for behavioral analysis and help distinguish expected operational changes from potentially suspicious activity.

---

# Event Categories

1. Business Operations
2. Research & Development
3. Regulatory Affairs
4. Information Technology
5. Human Resources
6. Finance
7. Executive Leadership
8. Environmental & External Events

---
# Business Operations

## Quarterly Town Hall

Frequency:
Quarterly

Departments:
All

Expected Behavioral Changes:

- Increased calendar activity
- Higher Microsoft Teams usage
- Reduced research activity during presentations
- Temporary increases in executive communications

---

## Company Holiday

Frequency:
Annual

Departments:
All

Expected Behavioral Changes:

- Reduced login activity
- Increased PTO
- Lower network utilization
- Minimal document access

---

## Office Closure

Frequency:
Occasional

Departments:
All

Expected Behavioral Changes:

- Increased VPN usage
- Reduced badge access
- Increased remote collaboration

---

# Research & Development

## DYLAR-X Research Milestone

Frequency:
Quarterly

Departments:
Research
Clinical Sciences

Expected Behavioral Changes:

- Increased ELN usage
- Larger research file access
- Longer laboratory sessions
- Increased collaboration

---

## Scientific Conference

Frequency:
Several per year

Departments:
Research

Expected Behavioral Changes:

- Increased travel
- Hotel VPN logins
- Lower laboratory activity
- Increased collaboration with external researchers

---

# Regulatory Affairs

## FDA Submission Window

Frequency:
As Needed

Departments:
Regulatory Affairs
Research

Expected Behavioral Changes:

- Significant increase in document access
- Weekend work
- Longer working sessions
- Increased collaboration with Research

---

## Regulatory Audit

Frequency:
Occasional

Departments:
Regulatory Affairs
Quality
Executive Leadership

Expected Behavioral Changes:

- Increased document retrieval
- Temporary access to archived records
- Increased executive review

---

# Information Technology

## Software Deployment

Frequency:
Monthly

Departments:
IT

Expected Behavioral Changes:

- After-hours activity
- Elevated administrative access
- Increased PowerShell usage
- Company-wide system changes

---

## Security Patch Weekend

Frequency:
Monthly

Departments:
IT

Expected Behavioral Changes:

- Weekend logins
- Increased privileged access
- Firewall configuration changes
- Backup validation

---

## Security Incident

Frequency:
Rare

Departments:
IT
Executive Leadership

Expected Behavioral Changes:

- Emergency after-hours logins
- Elevated administrative activity
- Increased SIEM usage
- Cross-department communication

---

# Human Resources

## New Employee Onboarding

Frequency:
Monthly

Departments:
HR
IT
Hiring Department

Expected Behavioral Changes:

- HRIS activity
- Account creation
- Badge issuance
- Increased documentation

---

## Benefits Enrollment

Frequency:
Annual

Departments:
HR
Finance

Expected Behavioral Changes:

- Increased employee record access
- Higher document downloads
- Temporary workload increase

---

## Performance Review Season

Frequency:
Annual

Departments:
All Managers
HR

Expected Behavioral Changes:

- Increased HR activity
- Higher executive collaboration
- Increased document generation

---

# Finance

## Month-End Close

Frequency:
Monthly

Departments:
Finance

Expected Behavioral Changes:

- Increased ERP usage
- Longer working sessions
- Increased financial reporting

---

## Annual Budget Planning

Frequency:
Annual

Departments:
Finance
Executive Leadership

Expected Behavioral Changes:

- Executive collaboration
- Forecast modeling
- Financial scenario analysis

---

# Executive Leadership

## Board Meeting

Frequency:
Quarterly

Departments:
Executive Leadership

Expected Behavioral Changes:

- Increased travel
- Board portal access
- Financial report review
- Strategic document access

---

## Strategic Planning Retreat

Frequency:
Annual

Departments:
Executive Leadership

Expected Behavioral Changes:

- Increased VPN usage
- Travel
- Cross-department collaboration
- Increased executive communications

---

# Environmental & External Events

## Severe Weather

Frequency:
Rare

Expected Behavioral Changes:

- Increased remote work
- Increased VPN usage
- Reduced badge access

---

## Public Health Event

Frequency:
Rare

Expected Behavioral Changes:

- Company-wide remote work
- Increased virtual meetings
- Reduced laboratory occupancy

---

# NAVIDSON Notes

Organizational events should decrease anomaly confidence when employee behavior aligns with expected organizational changes.

Example:

Research Scientist

↓

Late-night document access

↓

FDA Submission Window Active

↓

Reduced anomaly confidence

Rather than asking:

"Why is this employee behaving differently?"

NAVIDSON first asks:

"What is happening within the organization?"