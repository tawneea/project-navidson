import random
from faker import Faker

# --------------------------------------------------
# Reproducible synthetic personnel
# --------------------------------------------------

Faker.seed(217)
random.seed(217)

fake = Faker("en_US")

# --------------------------------------------------
# Office Locations
# --------------------------------------------------

OFFICES = [
    "Tucson",
    "Boston",
]

# --------------------------------------------------
# Projects
# --------------------------------------------------

PROJECTS = {
    "Research Scientist": [
        "HELIX",
        "Biomarker Discovery",
        "Analytical Chemistry",
        "Clinical Support",
    ],

    "Laboratory Technician": [
        "HELIX",
        "Laboratory Operations",
        "Sample Processing",
    ],

    "Regulatory Affairs Specialist": [
        "HELIX",
        "FDA Submission",
        "Quality Compliance",
    ],

    "Finance Analyst": [
        "Budget Planning",
        "Procurement",
        "Payroll",
    ],

    "Human Resources Specialist": [
        "Recruiting",
        "Benefits",
        "Learning & Development",
    ],

    "IT Security Administrator": [
        "Identity Modernization",
        "Endpoint Security",
        "Cloud Migration",
        "Infrastructure",
    ],

    "Executive Leadership": [
        "Corporate Strategy",
        "Research Portfolio",
        "Technology Modernization",
    ],
}

# --------------------------------------------------
# Security Clearance
# --------------------------------------------------

CLEARANCE = {
    "Research Scientist": "Trade Secret",
    "Laboratory Technician": "Restricted",
    "Regulatory Affairs Specialist": "Restricted",
    "Finance Analyst": "Confidential",
    "Human Resources Specialist": "Restricted",
    "IT Security Administrator": "Trade Secret",
    "Executive Leadership": "Trade Secret",
}

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def generate_person(role):
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "office": random.choice(OFFICES),
        "years_with_company": random.randint(0, 25),
        "assigned_project": random.choice(PROJECTS[role]),
        "security_clearance": CLEARANCE[role],
    }