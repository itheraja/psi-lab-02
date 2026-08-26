products = {
    "P101": {"name": "Laptop", "category": "Electronics", "price": 80000, "quantity": 5},
    "P102": {"name": "Mouse", "category": "Electronics", "price": 1500, "quantity": 0},
    "P103": {"name": "Chair", "category": "Furniture", "price": 12000, "quantity": 8}
}

pid = input("Enter Product ID to search: ")

if pid in products:
    print(products[pid])
else:
    print("Product not found")

pid = input("Enter Product ID to update price: ")
if pid in products:
    products[pid]["price"] = float(input("New Price: "))

pid = input("Enter Product ID to update quantity: ")
if pid in products:
    products[pid]["quantity"] = int(input("New Quantity: "))

print("\nOut of Stock Products:")

for pid, details in products.items():
    if details["quantity"] == 0:
        print(details["name"])
