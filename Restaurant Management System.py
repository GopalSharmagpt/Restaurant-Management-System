menu = {
    'Pizza': 60,
    'Pasta': 40,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

print("Welcome to Gopal Sharma Restaurant")
print("Pizza: 60 Rs\nPasta: 40 Rs\nBurger: 60 Rs\nSalad: 70 Rs\nCoffee: 80 Rs")

order_total = 0

item_1 = input("Enter the item you want to order: ")
if item_1 in menu:
     order_total += menu[item_1]
     print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == 'Yes':
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Ordered item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount to pay is {order_total} Rs")