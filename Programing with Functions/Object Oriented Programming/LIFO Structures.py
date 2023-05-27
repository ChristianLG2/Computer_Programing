import math

def square(x):
    return x ** 2

def multiply(a, b):
    return a * b

def calculate_correlation():
    x = float(input("Enter the value for x: "))
    y = float(input("Enter the value for y: "))

    operation_stack = []  # LIFO structure to store operations

    # Add operations to the operation_stack in the desired order
    operation_stack.append(lambda: multiply(x, y))
    operation_stack.append(lambda: square(y))
    operation_stack.append(lambda: square(x))

    # Perform operations in reverse order (LIFO)
    while operation_stack:
        current_operation = operation_stack.pop()
        result = current_operation()
        print(f"Operation: {current_operation.__name__}, Result: {result}")

# Example usage
calculate_correlation()
