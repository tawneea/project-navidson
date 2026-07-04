ROLE_PROFILES = {
    "Research Scientist": {
        "login_hour": 8,
        "login_minute": 15,
        "login_variance": 20,
        "work_events": 4,
        "possible_events": [
            {
                "event_type": "file_access",
                "action": "Open",
                "system": "Electronic Lab Notebook",
                "document": "HELIX Assay Protocol",
                "file": "GP217_Assay_Results.csv",
            },
            {
                "event_type": "file_access",
                "action": "Review",
                "system": "LIMS",
                "document": "GP-217 Sample Tracking Record",
                "file": "GP217_Sample_Tracking_Record.csv",
            },
            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Regulatory Affairs",
            },
            {
                "event_type": "file_access",
                "action": "Review",
                "system": "Research Share",
                "document": "HELIX Regulatory Briefing Package",
                "file": "HELIX_Regulatory_Briefing_Package.docx",
            },
        ],
    },

    "Laboratory Technician": {
        "login_hour": 7,
        "login_minute": 45,
        "login_variance": 15,
        "work_events": 5,
        "possible_events": [
            
            {
                "event_type":"instrument_use",
                "action":"Operate",
                "system":"Instrument Control Software", 
                "instrument": "Mass Spectrometer-02",
                "record": "Calibration Session",
            },

            {
                "event_type":"record_update",
                "action": "Update",
                "system": "LIMS",
                "record": "Sample GP217-104",
            },

            {
                "event_type":"file_access",
                "action":"Review",
                "system": "Quality Assurance Portal",
                "document": "Quality Control Checklist",
                "file": "QC_Checklist_v3.pdf",
            },

            {

                "event_type": "instrument_use",
                "action": "Calibrate",
                "system": "Instrument Control Software",
                "instrument": "Centrifuge-03",
                "record": "Calibration Record 556",
            },

            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Research",
            },

            {
                "event_type": "record_update",
                "action": "Approve",
                "system": "LIMS",
                "record": "Sample Processing Record",
            },
        ],
    },

    "Regulatory Affairs Specialist": {
        "login_hour": 8,
        "login_minute": 0,
        "login_variance": 15,
        "work_events": 4,
        "possible_events": [
            
            {
                "event_type": "document_review",
                "action": "Review",
                "system":"SharePoint",
                "document": "FDA Submission Draft",
                "file":"FDA_Submission_Draft_v5.docx",
            },

            {
                "event_type": "document_edit",
                "action": "Edit",
                "system": "SharePoint",
                "document": "HELIX Regulatory Briefing Package",
                "file": "HELIX_Regulatory_Briefing_Package.docx",
            },

            { 
                "event_type": "compliance_review",
                "action": "Approve",
                "system": "Regulatory Compliance Portal",
                "record": "Submission Review #1042",
            },

            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Research",
            },

            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Quality Assurance",
            },

            {
                "event_type":"document_upload",
                "action": "Upload",
                "system": "Regulatory Document Repository", 
                "document": "FDA Submission Package",
                "file": "FDA_Submission_Package_v1.zip",
            },

            {
                "event_type": "record_update",
                "action": "Update",
                "system": "Regulatory Compliance Portal",
                "record": "Submission Status",
            },
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