ROLE_PROFILES = {
    "Research Scientist": {
        "login_hour": 8,
        "login_minute": 15,
        "login_variance": 20,
        "work_events": 4,
        "possible_events": [
            {"event_type": "file_access", "system": "Electronic Lab Notebook", "file": "GP217_Assay_Results.csv"},
            {"event_type": "file_access", "system": "LIMS", "file": "GP217_Sample_Tracking_Record.csv"},
            {"event_type": "teams_message", "system": "Microsoft Teams", "recipient_department": "Regulatory Affairs"},
            {"event_type": "file_access", "system": "Research Share", "file": "HELIX_Regulatory_Briefing_Package.docx"},
        ],
    },

    "Laboratory Technician": {
        "login_hour": 7,
        "login_minute": 5,
        "login_variance": 10,
        "work_events": 5,
        "possible_events": [
            {"event_type": "file_access", "system": "LIMS", "file": "GP217_Sample_Tracking_Record.csv"},
            {"event_type": "instrument_update", "system": "Instrument Control Software", "instrument": "Centrifuge-03"},
            {"event_type": "file_access", "system": "Sample Tracking System", "file": "GP217_Batch_014.csv"},
            {"event_type": "quality_check", "system": "Quality Assurance Portal", "record": "GP217_QC_Record.pdf"},
        ],
    },

    "Regulatory Affairs Specialist": {
        "login_hour": 7,
        "login_minute": 58,
        "login_variance": 5,
        "work_events": 3,
        "possible_events": [
            {"event_type": "file_access", "system": "Regulatory Document Management System", "file": "HELIX_Submission_Checklist.docx"},
            {"event_type": "file_access", "system": "Regulatory Submission Portal", "file": "HELIX_Briefing_Package.pdf"},
            {"event_type": "teams_message", "system": "Microsoft Teams", "recipient_department": "Research"},
            {"event_type": "document_review", "system": "Quality Management System", "document": "GP217_CMC_Documentation.pdf"},
        ],
    },

    "Finance Analyst": {
        "login_hour": 7,
        "login_minute": 50,
        "login_variance": 10,
        "work_events": 3,
        "possible_events": [
            {"event_type": "file_access", "system": "ERP", "file": "HELIX_Budget_Q2.xlsx"},
            {"event_type": "file_access", "system": "FP&A Platform", "file": "HELIX_Cost_Forecast.xlsx"},
            {"event_type": "payroll_review", "system": "Payroll System", "file": "Payroll_Reconciliation.csv"},
            {"event_type": "teams_message", "system": "Microsoft Teams", "recipient_department": "Executive Leadership"},
        ],
    },

    "Human Resources Specialist": {
        "login_hour": 8,
        "login_minute": 5,
        "login_variance": 15,
        "work_events": 3,
        "possible_events": [
            {"event_type": "file_access", "system": "HRIS", "file": "Employee_Record_Update.pdf"},
            {"event_type": "file_access", "system": "Recruiting Platform", "file": "Research_Scientist_Candidates.xlsx"},
            {"event_type": "benefits_update", "system": "Benefits Administration", "file": "Open_Enrollment_Form.pdf"},
            {"event_type": "teams_message", "system": "Microsoft Teams", "recipient_department": "Finance"},
        ],
    },

    "IT Security Administrator": {
        "login_hour": 8,
        "login_minute": 0,
        "login_variance": 60,
        "work_events": 6,
        "possible_events": [
            {"event_type": "admin_action", "system": "Active Directory", "action": "Group Membership Review"},
            {"event_type": "security_alert_review", "system": "SIEM", "alert": "Unusual VPN Location"},
            {"event_type": "endpoint_review", "system": "EDR", "device": "Laptop-042"},
            {"event_type": "firewall_update", "system": "Firewall Management", "change": "Rule Review"},
            {"event_type": "backup_check", "system": "Backup Infrastructure", "status": "Validation Complete"},
        ],
    },

    "Executive Leadership": {
        "login_hour": 8,
        "login_minute": 30,
        "login_variance": 90,
        "work_events": 2,
        "possible_events": [
            {"event_type": "file_access", "system": "Board Portal", "file": "HELIX_Board_Update.pdf"},
            {"event_type": "file_access", "system": "Executive Dashboard", "file": "Portfolio_Risk_Report.pdf"},
            {"event_type": "file_access", "system": "Financial Reporting", "file": "Quarterly_Forecast.pdf"},
            {"event_type": "teams_message", "system": "Microsoft Teams", "recipient_department": "All Departments"},
        ],
    },
}