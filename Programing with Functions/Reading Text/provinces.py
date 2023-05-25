
def main():
    # Open the provinces.txt file for reading.
    with open('provinces.txt', 'r') as f:
        # Read the contents of the file into a list where each line of text
        # in the file is stored in a separate element in the list.
        provinces = f.read().splitlines()

    # Print the entire list.
    print(f"Original list: {provinces}")

    # Remove the first element from the list.
    if provinces:
        provinces.pop(0)

    # Remove the last element from the list.
    if provinces:
        provinces.pop(-1)

    # Replace all occurrences of "AB" in the list with "Alberta".
    for i in range(len(provinces)):
        if provinces[i] == 'AB':
            provinces[i] = 'Alberta'

    # Print the modified list.
    print(f"Modified list: {provinces}")

    # Count the number of elements that are "Alberta" and print that number.
    alberta_count = provinces.count('Alberta')
    print(f"Number of 'Alberta': {alberta_count}")

if __name__ == "__main__":
    main()
