#Christian Lira Spring 2023

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

def main():
    try:
        products_dict = read_dictionary(r'C:\Users\chris\OneDrive\Documents\Github Posted\Python Projects\Programing with Functions\Reading Text\products.csv', 0)
        print("")
        print("Lira's\n")
        total_items = 0
        subtotal = 0
        with open(r'C:\Users\chris\OneDrive\Documents\Github Posted\Python Projects\Programing with Functions\Reading Text\request.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                product = products_dict.get(product_number)
                if product:
                    print(f"{product[1]}: {quantity} at ${product[2]}")
                    total_items += quantity
                    subtotal += quantity * float(product[2])
                else:
                    raise KeyError(product_number)

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: ${round(subtotal, 2)}")
        tax = round(subtotal * 0.06, 2)
        print(f"Sales Tax: ${tax}")
        total = round(subtotal + tax, 2)
        print(f"Total: ${total}")

        print("\nThank you for shopping at the Lira's.")
        print(datetime.now().strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(str(e))
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(repr(e.args[0]))
    except Exception as e:
        print("Error: An unexpected error occurred.")
        print(str(e))

if __name__ == "__main__":
    main()
