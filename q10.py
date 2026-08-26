employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]

# Dictionary for fast lookup
employee_dict = {}

for emp in employees:
    employee_dict[emp[0]] = emp

print("IT Employees:")
for emp in employees:
    if emp[2] == "IT":
        print(emp)

total = 0

for emp in employees:
    total += emp[3]

print("\nAverage Salary:", total / len(employees))

highest = employees[0]

for emp in employees:
    if emp[3] > highest[3]:
        highest = emp

print("Highest Salary:", highest)

departments = set()

for emp in employees:
    departments.add(emp[2])

print("Departments:", departments)

dept_count = {}

for emp in employees:
    dept = emp[2]

    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1

print("Employees in each Department:", dept_count)

eid = input("Enter Employee ID: ")

if eid in employee_dict:
    print(employee_dict[eid])
else:
    print("Employee not found.")
