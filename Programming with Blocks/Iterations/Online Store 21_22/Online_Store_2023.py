# Christian Lira - Winter 2023
# Define items and their prices
items = {

    "milk": 2.50,
    "bread": 1.25,
    "juice": 5,
    "oranges": 2,
    "eggs": 2,
    "butter": 1.25,
    "peanut butter": 2,
    "bananas": 1.25
}

# Initialize counters to 0
counts = dict.fromkeys(items.keys(), 0)

# Define function to add an item to the cart
def add_item(item):
    counts[item] += 1
    print(f"You have {counts[item]} {item} in your cart")
    print(f"Total items in cart: {sum(counts.values())}")
    print(f"Total: {sum(counts[item] * price for item, price in items.items())}")
    print()

# Define function to remove an item from the cart
def remove_item(item):
    if counts[item] == 0:
        print(f"There are no {item}s in your cart")
    else:
        counts[item] -= 1
        print(f"You have {counts[item]} {item} in your cart")
        print(f"Total items in cart: {sum(counts.values())}")
        print(f"Total: {sum(counts[item] * price for item, price in items.items())}")
        print()

# Welcome message and menu loop
print("Welcome to our store!")
while True:
    print("What would you like to do? ")
    print("")
    print("A. Add item to cart")
    print("R. Remove item from cart")
    print("V. View cart")
    print("T. Compute total")
    print("Q. Quit")

    option = input("Please select an option (A, R, V, T, Q): ").upper()

    if option == "A":
        print("")
        print("We have the following items in storage: ")
        print("")
        for x in items:
         print(x)
        print("")
        item = input("What item would you like to add to your cart? ").lower()
        if item in items:
            add_item(item)
        else:
            print("Invalid item")
    elif option == "R":
        print("")
        item = input("What item would you like to remove from your cart? ").lower()
        if item in items:
            remove_item(item)
        else:
            print("Invalid item")
    elif option == "V":
        print("")
        print("Items in cart:")
        for item, count in counts.items():
            if count > 0:
                print(f"{item}: {count}")
    elif option == "T":
        print("")
        print(f"Total: {sum(counts[item] * price for item, price in items.items())}")
    elif option == "Q":
        print("")
        print(f"Your Total was: ${sum(counts[item] * price for item, price in items.items())}")
        print("We apprecite your Business, Thank you for choosing us")
        break
        
    else:
        print("Invalid option")

# Add indexes for the items and be able to use it in the cart. add the prices with correct formating. 
# be able to use index to remove item. 




