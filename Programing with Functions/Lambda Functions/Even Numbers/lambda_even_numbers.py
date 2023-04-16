# Christian Lira Spring 2023
'''This Code is to demonstrate the use of the LAMBDA function. In this case, the function is used to extract from a set of numbers all the even numbers'''

# Define a list of numbers (range 1:12)
number_list1 = [1,2,3,4,5,6,7,8,9,10,11,12]

# Ask the user to input a series of numbers separated with commas
numbers = input("Enter a series of numbers separated by commas: ")
number_list2 = [int(num) for num in numbers.split(',')]

# Define a function to filter even numbers from a list
def even_numbers(number):
    return list(filter(lambda x : x % 2 == 0, number))

# Get the even numbers from both input lists
first_list = even_numbers(number_list1)
sumA = sum(first_list)
second_list = even_numbers(number_list2)
sorted_second_list = sorted(second_list)
sumB = sum(second_list)

# Print the results
print()
print("This is the first list:", number_list1)
print("The even numbers in the first given list are:", first_list)
print("The sum of the even numbers in the first list is:", sumA)
print()
print("This is your list:", number_list2)
print("The even numbers in the input list are:", sorted_second_list)
print("The sum of the even numbers in the input list is:", sumB)
print()
print("Program completed successfully.")
