courseA = set(input("Enter Course A IDs: ").split())
courseB = set(input("Enter Course B IDs: ").split())

print("Both Courses:", courseA & courseB)
print("Only Course A:", courseA - courseB)
print("Only Course B:", courseB - courseA)
print("All Students:", courseA | courseB)
