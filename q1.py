students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    subjects = int(input("Number of subjects: "))

    marks = []

    for j in range(subjects):
        mark = int(input("Enter marks: "))
        marks.append(mark)

    students[name] = marks

print("\nStudent Averages:")
highest_student = ""
highest_average = 0

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    print(name, "Average =", avg)

    if avg > highest_average:
        highest_average = avg
        highest_student = name

print("\nHighest Performing Student:", highest_student)

threshold = float(input("\nEnter average threshold: "))

print("Students above threshold:")

for name, marks in students.items():
    avg = sum(marks) / len(marks)
    if avg > threshold:
        print(name)
