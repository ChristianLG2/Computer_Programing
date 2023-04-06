import csv

items = {}
with open('foods.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    for row in csvreader:
        item, price, *_ = row
        items[item.strip().lower()] = float(price)

counts = dict.fromkeys(items.keys(), 0)
transactions = []
deleted_transactions = []

transaction_counter = 1

def add_item(item):
    global transaction_counter
    counts[item] += 1
    price = items[item]
    transactions.append((transaction_counter, item, price))
    transaction_counter += 1
    print(f"You have {counts[item]} {item} in your cart")
    print(f"Total items in cart: {sum(counts.values())}")
    print(f"Total: ${sum(counts[item] * price for item, price in items.items()):.2f}")
    print()

def remove_item(transaction_index):
    try:
        transaction = transactions.pop(transaction_index - 1)
        deleted_transactions.append(transaction)
        item = transaction[1]
        counts[item] -= 1
        print(f"Transaction {transaction_index} removed from the cart.")
        print(f"Total items in cart: {sum(counts.values())}")
        print(f"Total: ${sum(counts[item] * price for item, price in items.items()):.2f}")
        print()
    except IndexError:
        print("Invalid transaction index")

print("Welcome to our store!")
while True:
    print("What would you like to do?")
    print("")
    print("A. Add item to cart")
    print("R. Remove item from cart")
    print("V. View cart")
    print("T. Compute total")
    print("Q. Quit")

    option = input("Please select an option (A, R, V, T, Q): ").upper()

    if option == "A":
        print("")
        print("We have the following items in storage:")
        print("")
        for x in items:
            print(x)
        print("")
        item = input("What item would you like to add to your cart? ").strip().lower()
        if item in items:
            add_item(item)
        else:
            print("Invalid item")
    elif option == "R":
        print("")
        transaction_index = int(input("Enter the transaction index you want to remove: "))
        remove_item(transaction_index)
    elif option == "V":
        print("")
        print("Transactions in cart:")
        for transaction in transactions:
            print(f"Transaction {transaction[0]}: {transaction[1]} - ${transaction[2]:.2f}")
    elif option == "T":
        print("")
        print("Transactions:")
        for transaction in transactions + deleted_transactions:
            if transaction in transactions:
                print(f"Transaction {transaction[0]}: {transaction[1]} - ${transaction[2]:.2f}")
            else:
                print(f"Transaction {transaction[0]}: {transaction[1]} - (${transaction[2]:.2f}) (Deleted)")
        print(f"Total: ${sum(counts[item] * price for item, price in items.items()):.2f}")
    elif option == "Q":
        print("")
        print(f"Your Total was: ${sum(counts[item] * price for item, price in items.items()):.2f}")
        print("We appreciate your business, Thank you for choosing us")
        break
    else:
        print("Invalid option")



