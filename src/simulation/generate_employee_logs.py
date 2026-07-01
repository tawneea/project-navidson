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
            "name": f"{self.first_name} {self.last_name}",
            "event_type": "login",
            "timestamp": login_time,
            "role": self.role,
            "department": self.department,
            "office": self.office,
            "assigned_project": self.assigned_project,
            "security_clearance": self.security_clearance,
         }

    def work(self, start_time):
        profile = ROLE_PROFILES[self.role]

        possible_events = profile["possible_events"]

        work_events = []

        for _ in range(profile["work_events"]):
            event_time = start_time + timedelta(
                hours=random.randint(1, 7),
                minutes=random.randint(0, 59)
            )

            event = random.choice(possible_events).copy()

            event.update({
                "employee_id": self.employee_id,
                "name": f"{self.first_name} {self.last_name}",
                "timestamp": event_time,
                "role": self.role,
                "department": self.department,
                "office": self.office,
                "assigned_project": self.assigned_project,
                "security_clearance": self.security_clearance,
})

            work_events.append(event)

        return work_events

    def logout(self, start_time):
        logout_time = start_time + timedelta(hours=9, minutes=random.randint(-20, 20))

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
        department="Research"
    )

    workday_start = datetime(2026, 1, 5, 8, 15)

    events = [employee.login(workday_start)]
    events.extend(employee.work(workday_start))
    events.append(employee.logout(workday_start))

    events = sorted(events, key=lambda event: event["timestamp"])

    for event in events:
        print(event)