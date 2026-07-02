from datetime import datetime

from generate_employee_logs import Employee
from personnel import generate_person

from event_exporter import save_employees, save_events

from datetime import datetime, timedelta

def format_event(event):
    timestamp = event["timestamp"].strftime("%H:%M")
    employee_id = event["employee_id"]
    name = event.get("name", "")
    event_type = event["event_type"].upper()
    system = event.get("system", "")

    detail = (
        event.get("file")
        or event.get("document")
        or event.get("record")
        or event.get("action")
        or event.get("alert")
        or event.get("status")
        or event.get("instrument")
        or event.get("device")
        or event.get("recipient_department")
        or ""
    )

    return (
        f"{timestamp}  "
        f"{employee_id:<6}  "
        f"{name:<22}  "
        f"{event_type:<24}  "
        f"{system:<38}  "
        f"{detail}"
    )


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire_employees(self):
        hiring_plan = {
            "Research Scientist": {
                "prefix": "RS",
                "department": "Research",
                "count": 140,
            },
            "Laboratory Technician": {
                "prefix": "LT",
                "department": "Research",
                "count": 45,
            },
            "Regulatory Affairs Specialist": {
                "prefix": "RA",
                "department": "Regulatory Affairs",
                "count": 40,
            },
            "Finance Analyst": {
                "prefix": "FA",
                "department": "Finance",
                "count": 35,
            },
            "Human Resources Specialist": {
                "prefix": "HR",
                "department": "Human Resources",
                "count": 25,
            },
            "IT Security Administrator": {
                "prefix": "IT",
                "department": "Information Technology",
                "count": 35,
            },
            "Executive Leadership": {
                "prefix": "EX",
                "department": "Executive Leadership",
                "count": 10,
            },
        }

        for role, details in hiring_plan.items():
            for i in range(1, details["count"] + 1):
                employee_id = f'{details["prefix"]}-{i:03d}'
                person = generate_person(role)

                employee = Employee(
                    employee_id=employee_id,
                    role=role,
                    department=details["department"],
                    first_name=person["first_name"],
                    last_name=person["last_name"],
                    office=person["office"],
                    years_with_company=person["years_with_company"],
                    assigned_project=person["assigned_project"],
                    security_clearance=person["security_clearance"],
                )

                self.employees.append(employee)

        return self.employees

    def simulate_workday(self, workday_start):
        all_events = []

        for employee in self.employees:
            events = [employee.login(workday_start)]
            events.extend(employee.work(workday_start))
            events.append(employee.logout(workday_start))

            all_events.extend(events)

        return sorted(all_events, key=lambda event: event["timestamp"])


if __name__ == "__main__":
    company = Company("Gladney Pharmaceuticals")
    company.hire_employees()

    save_employees(company.employees)

    start_date = datetime(2026, 1, 5, 8, 15)
    number_of_days = 5

    total_events = 0

    for day in range(number_of_days):
        workday_start = start_date + timedelta(days=day)

        # Skip weekends for now
        if workday_start.weekday() >= 5:
            continue

        events = company.simulate_workday(workday_start)
        save_events(events)

        total_events += len(events)

        print(f"Saved {len(events)} events for {workday_start.date()}")

    print(f"\n{company.name}")
    print(f"Employees hired: {len(company.employees)}")
    print(f"Total events generated: {total_events}")