import csv
import os


OUTPUT_DIR = "data/synthetic"


def ensure_output_directory():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_employees(employees):
    ensure_output_directory()

    filepath = os.path.join(OUTPUT_DIR, "employees.csv")

    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
            "employee_id",
            "first_name",
            "last_name",
            "role",
            "department",
            "office",
            "years_with_company",
            "assigned_project",
            "security_clearance"
        ])

        for employee in employees:
            writer.writerow([
                employee.employee_id,
                employee.first_name,
                employee.last_name,
                employee.role,
                employee.department,
                employee.office,
                employee.years_with_company,
                employee.assigned_project,
                employee.security_clearance
            ])

    print(f"Saved {filepath}")


def save_events(events):
    ensure_output_directory()

    filepath = os.path.join(
        OUTPUT_DIR,
        f"events_{events[0]['timestamp'].date()}.csv"
    )

    fieldnames = sorted(
        {key for event in events for key in event.keys()}
    )

    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for event in events:
            writer.writerow(event)

    print(f"Saved {filepath}")