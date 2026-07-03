from datetime import date

ORGANIZATIONAL_EVENTS = {
    date(2026, 1, 5): [
        {
            "name": "Research Weekly Sync",
            "departments": ["Research"],
            "effect": "collaboration"
        }
    ],

    date(2026, 1, 7): [
        {
            "name": "IT Infrastructure Maintenance",
            "departments": ["Information Technology"],
            "effect": "maintenance"
        }
    ],

    date(2026, 1, 9): [
        {
            "name": "Finance Month-End Preparation",
            "departments": ["Finance"],
            "effect": "financial_close"
        }
    ],

    date(2026, 1, 14): [
        {
            "name": "FDA Submission Planning",
            "departments": [
                "Research",
                "Regulatory Affairs"
            ],
            "effect": "regulatory_deadline"
        }
    ]
}


def get_events(current_date):
    """
    Return all organizational events scheduled for a given date.
    """
    return ORGANIZATIONAL_EVENTS.get(current_date.date(), [])