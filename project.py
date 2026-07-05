# [vegetable, cost_price_per_kg, selling_price_per_kg, stock_in_kgs, sold_kgs]
inventory = [
    ["tomato", 20, 30, 100, 0],
    ["potato", 15, 25, 50, 0],
    ["brinjal", 30, 35, 100, 0],
    ["onion", 25, 35, 200, 0],
    ["carrot", 15, 20, 50, 0],
    ["cabbage", 20, 30, 75, 0]
]

transactions = []

while 1:   # main loop
    print("=== Management System ===")
    print("1. Shopkeeper View")
    print("2. Customer View")
    print("3. Exit")
    choice = input("Enter your required option: ")

    # SHOPKEEPER VIEW
    if choice == "1":
        while 1:
            print("=== Shopkeeper Menu ===")
            print("1. Add Vegetable")
            print("2. Update Vegetable Quantity")
            print("3. Delete Vegetable")
            print("4. Vegetable Report")
            print("5. Revenue Report")
            print("6. Profit Report (Total)")
            print("7. Back")
            print("8. Profit Report (Per Vegetable)")
            ch = input("Enter choice: ")

            if ch == "1":
                name = input("Enter vegetable name: ")
                cost = int(input("Enter cost_price per kg: "))
                price = int(input("Enter selling_price per kg: "))
                qty = int(input("Enter quantity in kgs: "))
                inventory.append([name, cost, price, qty, 0])
                print(name, "added successfully")

            elif ch == "2":
                name = input("Enter vegetable name to update: ")
                new_qty = int(input("Enter new quantity in kgs: "))
                for vegetable in inventory:
                    if vegetable[0] == name:
                        vegetable[3] = new_qty
                        print(name, "updated successfully")

            elif ch == "3":
                name = input("Enter vegetable name to remove: ")
                for vegetable in inventory:
                    if vegetable[0] == name:
                        inventory.remove(vegetable)
                        print(name, "removed successfully")

            elif ch == "4":
                print("=== Vegetable Report ===")
                for vegetable in inventory:
                    print(vegetable[0], ":", vegetable[3], "kg left",
                          "Selling_price =", vegetable[2], "per kg")

            elif ch == "5":
                total_revenue = 0
                for t in transactions:
                    total_revenue = total_revenue + t
                print("=== Revenue Report ===")
                print("Total Revenue =", total_revenue, "Rupees")

            elif ch == "6":
                print("=== Profit Report (Total) ===")
                total_profit = 0
                for vegetable in inventory:
                    profit = vegetable[4] * (vegetable[2] - vegetable[1])
                    total_profit = total_profit + profit
                print("Total Profit =", total_profit, "Rupees")

            elif ch == "8":
                print("=== Profit Report (Per Vegetable) ===")
                for vegetable in inventory:
                    profit = vegetable[4] * (vegetable[2] - vegetable[1])
                    print(vegetable[0], "sold", vegetable[4], "kg",
                          "Profit =", profit, "Rupees")

            elif ch == "7":
                break

    # CUSTOMER VIEW
    elif choice == "2":
        cart = []
        while 1:
            print("=== Customer Menu ===")
            print("1. Show Available Vegetables")
            print("2. Add Item to Cart")
            print("3. View Cart & Bill")
            print("4. Checkout")
            print("5. Back")
            ch = input("Enter choice: ")

            if ch == "1":
                print("=== Available Vegetables ===")
                for vegetable in inventory:
                    print(f"{vegetable[0]:<12}{vegetable[2]:<12}")

            elif ch == "2":
                name = input("Enter vegetable name: ")
                qty = int(input("Enter quantity in kgs: "))
                cart.append([name, qty])
                print(name, "added to cart")

            elif ch == "3":
                print("=== Cart Items ===")
                total = 0
                for name, qty in cart:
                    for vegetable in inventory:
                        if vegetable[0] == name:
                            cost = vegetable[2] * qty
                            print(name, qty, "kg  Rs.", cost)
                            total = total + cost
                print("Current Total =", total, "Rupees")

            elif ch == "4":
                bill = []
                total = 0
                for name, qty in cart:
                    found = 0
                    for vegetable in inventory:
                        if vegetable[0] == name:
                            found = 1
                            if vegetable[3] >= qty:
                                vegetable[3] = vegetable[3] - qty
                                vegetable[4] = vegetable[4] + qty
                                cost = vegetable[2] * qty
                                bill.append([name, qty, cost])
                                total = total + cost
                            else:
                                print("Sorry,", name, "only", vegetable[3], "kg available")
                    if found == 0:
                        print("Sorry,", name, "is not available in inventory")

                if total > 0:
                    transactions.append(total)

                if len(bill) > 0:
                    print("=== Final Bill ===")
                    for b in bill:
                        print(b[0], b[1], "kg   Rs.", b[2])
                    print("Total Bill = Rs.", total)
                else:
                    print("No valid purchases made.")
                cart = []  # empty cart after checkout

            elif ch == "5":
                break

    # EXIT
    elif choice == "3":
        print("Exited")
        break