cart = {}

while True:
    print("\n1.Add")
    print("2.Remove")
    print("3.Update Quantity")
    print("4.Total")
    print("5.Exit")

    choice = input("Choice: ")

    if choice == "1":
        product = input("Product: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        cart[product] = {"price": price, "quantity": quantity}

    elif choice == "2":
        product = input("Product to remove: ")
        if product in cart:
            del cart[product]

    elif choice == "3":
        product = input("Product: ")
        if product in cart:
            cart[product]["quantity"] = int(input("New Quantity: "))

    elif choice == "4":
        total = 0

        for item in cart.values():
            total += item["price"] * item["quantity"]

        print("Total =", total)

    elif choice == "5":
        break
