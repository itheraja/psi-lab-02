transactions = input("Enter transaction IDs separated by spaces: ").split()

duplicates = set()
unique = set()

for t in transactions:
    if t in unique:
        duplicates.add(t)
    else:
        unique.add(t)

print("Duplicate Transactions:", duplicates)
print("Unique Transactions:", unique)
