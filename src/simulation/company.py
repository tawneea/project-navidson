from datetime import datetime
from generate_employee_logs import Employee


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

                employee = Employee(
                    employee_id=employee_id,
                    role=role,
                    department=details["department"],
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

        all_events = sorted(all_events, key=lambda event: event["timestamp"])

        return all_events


if __name__ == "__main__":
    company = Company("Gladney Pharmaceuticals")
    company.hire_employees()

    workday_start = datetime(2026, 1, 5, 8, 15)

    events = company.simulate_workday(workday_start)

    print(f"{company.name} generated {len(events)} events.")
    print("First 20 events:")

    for event in events[:20]:
        print(event)