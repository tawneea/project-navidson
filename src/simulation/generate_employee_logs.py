import random
from datetime import datetime, timedelta
from archetypes import ROLE_BASELINES


class Employee:
    def __init__(self, employee_id, role, department):
        self.employee_id = employee_id
        self.role = role
        self.department = department

    def login(self, start_time):
        profile = ROLE_BASELINES[self.role]

        baseline = start_time.replace(
            hour=profile["login_hour"],
            minute=profile["login_minute"]
        )

        login_time = baseline + timedelta(
            minutes=random.randint(
                -profile["login_variance"],
                profile["login_variance"]
            )
        )

        return {
            "employee_id": self.employee_id,
            "event_type": "login",
            "timestamp": login_time,
            "role": self.role,
            "department": self.department,
        }

    def work(self, start_time):
        profile = ROLE_BASELINES[self.role]

        possible_events = [
            {
                "event_type": "file_access",
                "system": "Electronic Lab Notebook",
                "file": "DYLAR-X_Experiment_Notes.md",
            },
            {
                "event_type": "file_access",
                "system": "LIMS",
                "file": "Sample_Tracking_Record.csv",
            },
            {
                "event_type": "teams_message",
                "system": "Microsoft Teams",
                "recipient_department": "Regulatory Affairs",
            },
            {
                "event_type": "file_access",
                "system": "Research Share",
                "file": "DYLAR-X_PhaseIII_Preparation.docx",
            },
        ]

        work_events = []

        for _ in range(profile["work_events"]):
            event_time = start_time + timedelta(
                hours=random.randint(1, 7),
                minutes=random.randint(0, 59)
            )

            event = random.choice(possible_events).copy()

            event.update({
                "employee_id": self.employee_id,
                "timestamp": event_time,
                "role": self.role,
                "department": self.department,
            })

            work_events.append(event)

        return work_events

    def logout(self, start_time):
        logout_time = start_time + timedelta(hours=9, minutes=random.randint(-20, 20))

        return {
            "employee_id": self.employee_id,
            "event_type": "logout",
            "timestamp": logout_time,
            "role": self.role,
            "department": self.department,
        }


if __name__ == "__main__":
    employee = Employee(
        employee_id="RS-001",
        role="Research Scientist",
        department="Research"
    )

    workday_start = datetime(2026, 1, 5, 8, 15)

    events = [employee.login(workday_start)]
    events.extend(employee.work(workday_start))
    events.append(employee.logout(workday_start))

    events = sorted(events, key=lambda event: event["timestamp"])

    for event in events:
        print(event)