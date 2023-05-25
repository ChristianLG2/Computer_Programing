import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


def main():
    # Call the read_dictionary function and store the compound dictionary in a variable named products_dict.
    products_dict = read_dictionary('products.csv', 0)
    # Print the products_dict.
    print(products_dict)

    # Open the request.csv file for reading.
    with open('request.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first line of the request.csv file because the first line contains column headings.

        # Use a loop that reads and processes each row from the request.csv file.
        for row in reader:
            product_number = row[0]
            quantity = row[1]

            # Use the requested product number to find the corresponding item in the products_dict.
            product = products_dict.get(product_number, None)
            if product:
                # Print the product name, requested quantity, and product price.
                print(f"Product Name: {product[1]}, Requested Quantity: {quantity}, Product Price: {product[2]}")


if __name__ == "__main__":
    main()
