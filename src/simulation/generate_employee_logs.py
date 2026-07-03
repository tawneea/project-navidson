import random
from datetime import datetime, timedelta

from archetypes import ROLE_PROFILES


class Employee:
    def __init__(
        self,
        employee_id,
        role,
        department,
        first_name,
        last_name,
        office,
        years_with_company,
        assigned_project,
        security_clearance,
    ):
        self.employee_id = employee_id
        self.role = role
        self.department = department
        self.first_name = first_name
        self.last_name = last_name
        self.office = office
        self.years_with_company = years_with_company
        self.assigned_project = assigned_project
        self.security_clearance = security_clearance

    def login(self, start_time):
        profile = ROLE_PROFILES[self.role]

        baseline = start_time.replace(
            hour=profile["login_hour"],
            minute=profile["login_minute"],
        )

        login_time = baseline + timedelta(
            minutes=random.randint(
                -profile["login_variance"],
                profile["login_variance"],
            )
        )

        return {
            "employee_id": self.employee_id,
            "name": f"{self.first_name} {self.last_name}",
            "event_type": "login",
            "timestamp": login_time,
            "role": self.role,
            "department": self.department,
            "office": self.office,
            "assigned_project": self.assigned_project,
            "security_clearance": self.security_clearance,
        }

    def work(self, start_time, todays_events=None):
        profile = ROLE_PROFILES[self.role]

        # Start with this role's normal behavior
        possible_events = profile["possible_events"][:]

        # Base workload
        event_count = random.randint(
            max(1, profile["work_events"] - 1),
            profile["work_events"] + 1,
        )

        todays_events = todays_events or []

        # Modify behavior based on organizational events
        for org_event in todays_events:
            if self.department in org_event["departments"]:

                # Slightly busier day
                event_count += 1

                # Increase probability of certain event types
                for preferred in org_event.get("preferred_events", []):

                    matching_events = [
                        event
                        for event in profile["possible_events"]
                        if event["event_type"] == preferred
                    ]

                    possible_events.extend(matching_events)

        work_events = []

        for _ in range(event_count):

            event = random.choice(possible_events).copy()

            event_time = start_time + timedelta(
                minutes=random.randint(30, 480)
            )

            event.update(
                {
                    "employee_id": self.employee_id,
                    "name": f"{self.first_name} {self.last_name}",
                    "timestamp": event_time,
                    "role": self.role,
                    "department": self.department,
                    "office": self.office,
                    "assigned_project": self.assigned_project,
                    "security_clearance": self.security_clearance,
                }
            )

            work_events.append(event)

        return work_events

    def logout(self, start_time):
        logout_time = start_time + timedelta(
            hours=9,
            minutes=random.randint(-20, 20),
        )

        return {
            "employee_id": self.employee_id,
            "name": f"{self.first_name} {self.last_name}",
            "event_type": "logout",
            "timestamp": logout_time,
            "role": self.role,
            "department": self.department,
            "office": self.office,
            "assigned_project": self.assigned_project,
            "security_clearance": self.security_clearance,
        }


if __name__ == "__main__":
    employee = Employee(
        employee_id="RS-001",
        role="Research Scientist",
        department="Research",
        first_name="Jane",
        last_name="Doe",
        office="Research Building A",
        years_with_company=5,
        assigned_project="HELIX",
        security_clearance="Confidential",
    )

    workday_start = datetime(2026, 1, 5, 8, 15)

    events = [employee.login(workday_start)]
    events.extend(employee.work(workday_start))
    events.append(employee.logout(workday_start))

    events = sorted(events, key=lambda event: event["timestamp"])

    for event in events:
        print(event)