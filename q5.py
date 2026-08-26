employees = {
    "E101": {"name": "Ali", "department": "IT", "salary": 85000, "title": "Developer"},
    "E102": {"name": "Sara", "department": "HR", "salary": 70000, "title": "Manager"}
}

eid = input("Enter Employee ID: ")

if eid in employees:
    print(employees[eid])

eid = input("Employee ID to update salary: ")
if eid in employees:
    employees[eid]["salary"] = int(input("New Salary: "))

eid = input("New Employee ID: ")
employees[eid] = {
    "name": input("Name: "),
    "department": input("Department: "),
    "salary": int(input("Salary: ")),
    "title": input("Job Title: ")
}

eid = input("Employee ID to remove: ")

if eid in employees:
    del employees[eid]

print(employees)
