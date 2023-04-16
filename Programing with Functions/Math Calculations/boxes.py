#Christian Lira Spring 2023 
'''This is a Python script designed to help employees of a manufacturing company determine the number of boxes required to pack a specified number of items, taking into account a specified number of items per box. The program takes two integer inputs from the user: the total number of manufactured items and the number of items that will be packed in each box. Based on this information, the program calculates and displays the minimum number of boxes needed to accommodate all the items.'''

def main():
    # Ask for the number of manufactured items
    num_items = int(input("Enter the number of manufactured items: "))

    # Ask for the number of items per box
    items_per_box = int(input("Enter the number of items to pack per box: "))

    # Calculate the number of boxes needed
    num_boxes = num_items // items_per_box
    if num_items % items_per_box != 0:
        num_boxes += 1

    # Print the result
    print(f"The number of boxes needed for {num_items} items packed per box is: {num_boxes}")

if __name__ == "__main__":
    main()
