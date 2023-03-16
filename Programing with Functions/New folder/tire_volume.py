# Christian Lira Spring 2023 
#This program reads the tire dimensions from the user, computes the volume using the given formula, and outputs the result to the console. Note that we use the math.pi constant for the value of pi and use the ** operator for exponentiation. We also use the f-string syntax to format the output to two decimal places.
 
import math

# read tire dimensions from user input
width = int(input("Enter tire width in millimeters: "))
aspect_ratio = int(input("Enter tire aspect ratio: "))
diameter = int(input("Enter wheel diameter in inches: "))

# compute tire volume
volume = math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

# output tire volume
print(f"The volume of the tire is {volume:.2f} liters.")
