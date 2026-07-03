from datetime import date

ORGANIZATIONAL_EVENTS = {
    date(2026, 1, 5): [
        {
            "name": "Research Weekly Sync",
            "departments": ["Research"],
            "effect": "collaboration",
            "preferred_events": [
                "teams_message",
                "file_access",
                "file_access"
            ]
        }
    ],

    date(2026, 1, 7): [
        {
            "name": "IT Infrastructure Maintenance",
            "departments": ["Information Technology"],
            "effect": "maintenance",
            "preferred_events": [
                "firewall_update",
                "backup_check",
                "admin_action",
                "endpoint_review"
            ]
        }
    ],

    date(2026, 1, 9): [
        {
            "name": "Finance Month-End Preparation",
            "departments": ["Finance"],
            "effect": "financial_close",
            "preferred_events": [
                "payroll_review",
                "file_access",
                "teams_message"
            ]
        }
    ],

    date(2026, 1, 14): [
        {
            "name": "FDA Submission Planning",
            "departments": [
                "Research",
                "Regulatory Affairs"
            ],
            "effect": "regulatory_deadline",
            "preferred_events": [
                "document_review",
                "file_access",
                "teams_message"
            ]
        }
    ]
}


def get_events(current_date):
    return ORGANIZATIONAL_EVENTS.get(current_date.date(), [])