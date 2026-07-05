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
            {
                "event_type": "budget_review",
                "action": "Review",
                "system": "ERP",
                "document": "HELIX Budget Review",
                "file": "HELIX_Budget_Q2.xlsx",
            },
            {
                "event_type": "forecast_update",
                "action":"Update",
                "system": "FP&A Platform",
                "document": "HELIX Cost Forecast",
                "file": "HELIX_Cost_Forecast.xlsx",
            },
            {
                "event_type": "payroll_review",
                "action": "Review", 
                "system": "Payroll System",
                "document": "Payroll Reconciliation",
                "file": "Payroll_Reconciliation.csv",
            },
            {
                "event_type": "procurement_review",
                "action": "Approve",
                "system": "ERP",
                "record": "Purchase Order PO-1048",
                "status": "Approved",
            },
            {
                "event_type": "financial_report_access",
                "action": "Open",
                "system": "Financial Reporting",
                "document": "Quarterly Forecast",
                "file": "Quarterly_Forecast_Q2.pdf",
            },
            {
                "event_type": "teams_message", 
                "action": "Send", 
                "system": "Microsoft Teams",
                "recipient_department": "Executive Leadership",
            },
            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Human Resources",
            },
        ],
    },

    "Human Resources Specialist": {
        "login_hour": 8,
        "login_minute": 5,
        "login_variance": 15,
        "work_events": 3,
        "possible_events": [
            {
                "event_type": "employee_record_update",
                "action": "Update",
                "system": "HRIS",
                "document": "Employee Record Update",
                "file": "Employee_Record_Update.pdf",
                "record": "Employee Profile HR-2041",
            },
            {
                "event_type": "candidate_review",
                "action": "Review",
                "system": "Recruiting Platform",
                "document": "Research Scientist Candidate List",
                "file": "Research_Scientist_Candidates.xlsx",
            },
            {
                "event_type": "benefits_update",
                "action": "Update",
                "system": "Benefits Administration",
                "document": "Open Enrollment Form",
                "file": "Open_Enrolment_Form.pdf",
                "record": "Benefits Case BE-1182",
            },
            {
                "event_type": "onboarding_task",
                "action": "Create",
                "system": "HRIS",
                "document": "New Hire Onboarding Checklist",
                "status": "In Progress",
            },
            {
                "event_type": "training_review",
                "action": "Review",
                "system": "Learning Management System", 
                "document": "Cybersecurity Awareness Completion Report",
                "file": "Security_Awareness_Completion.csv",
            },
            {  
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Finance",
            },
            {
                "event_type": "teams_message", 
                "action": "Send", 
                "system": "Microsoft Teams",
                "recipient_department": "Information Technology",
            },      
                
        ],
    },

    "IT Security Administrator": {
        "login_hour": 8,
        "login_minute": 0,
        "login_variance": 60,
        "work_events": 6,
        "possible_events": [
            
            {
                "event_type": "identity_management",
                "action": "Review Group Membership",
                "system": "Microsoft Active Directory",
                "record": "Research Scientists Security Group",
            },

            {
                "event_type": "identity_management",
                "action": "Reset Password",
                "system": "Microsoft Active Directory",
                "record": "Employee Account",
            },

            {
                "event_type": "security_alert_review",
                "action": "Investigate",
                "system": "Microsoft Sentinel",
                "alert": "Unusual VPN Location",
                "status": "Under Review",
            },

            {
                "event_type": "endpoint_review",
                "action": "Review Endpoint Health",
                "system": "Microsoft Defender for Endpoint",
                "device": "Research-Laptop-042",
                "status": "Healthy",
            },

            {
                "event_type": "firewall_update",
                "action": "Approve Rule Change",
                "system": "Palo Alto Panorama",
                "change": "Research VLAN Rule UPdate",
                "status": "Approved",
            },

            {
                "event_type": "vulnerability_review",
                "action": "Review Findings", 
                "system": "Qualys VMDR",
                "record": "Weekly Vulnerability Scan",
                "status": "Open",
            },

            {
                "event_type": "patch_management",
                "action": "Approve Patch Deployment",
                "system": "Microsoft Intune", 
                "record": "Windows Security Updates",
                "status": "Scheduled", 
            },

            {
                "event_type": "vpn_review",
                "action": "Review Remote Login",
                "system": "VPN Gateway",
                "device": "Remote-Laptop-017",
                "status": "Verified",
            },

            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "Research",
            },

        ]
    },
                
                 

    "Executive Leadership": {
        "login_hour": 8,
        "login_minute": 30,
        "login_variance": 90,
        "work_events": 2,
        "possible_events": [
            
            {
                "event_type": "executive_dashboard",
                "action": "Review",
                "system": "Executive Dashboard",
                "document": "Enterprise Performance Dashboard",
                "file": "Enterprise_KPI_Dashboard.pdf",
            },

            {
                "event_type": "board_report",
                "action": "Review",
                "system": "Board Portal",
                "document": "Board Meeting Briefing",
                "file": "Board_Meeting_Briefing_Q1.pdf",
            },

            {
                "event_type": "financial_report_access",
                "action": "Review",
                "system": "Financial Reporting",
                "document": "Quarterly Financial Forecast",
                "file": "Quarterly_Forecast_Q1.pdf",
            },

            {
                "event_type": "risk_review",
                "action": "Review",
                "system": "Enterprise Risk Management",
                "document": "Enterprise Risk Assessment",
                "file": "Enterprise_Risk_Assessment.pdf",
            },

            {
                "event_type": "strategy_review",
                "action": "Review",
                "system": "Strategy Portal",
                "document": "HELIX Strategic Roadmap",
                "file": "HELIX_Strategic_Roadmap.pdf",
            },

            {
                "event_type": "approval",
                "action": "Approve",
                "system": "Executive Approval Portal",
                "record": "Capital Expenditure Request",
                "status": "Approved",
            },
                
            {
                "event_type": "teams_message",
                "action": "Send",
                "system": "Microsoft Teams",
                "recipient_department": "All Departments",
            },

            {
                "event_type": "executive_meeting",
                "action": "Attend",
                "system": "Microsoft Teams",
                "document": "Executive Leadership Agenda",
        },

    ],
},
}