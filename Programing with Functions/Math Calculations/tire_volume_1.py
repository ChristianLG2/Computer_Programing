#Christian Lira - Spring 2023 

# Import required modules
import math
import datetime

# Define the tire_volume function to calculate the volume of a tire
def tire_volume(w, a, d):
    return (math.pi * w**2 * a * w * a + 2540 * d) / 10000000000

# Define the main function that contains the core logic of the program
def main():
    # Get user input for tire width, aspect ratio, and wheel diameter
    print("Enter the tire width (e.g., 205):")
    w = float(input())
    
    print("Enter the aspect ratio (e.g., 60):")
    a = float(input())
    
    print("Enter the wheel diameter (e.g., 15):")
    d = float(input())

    # Calculate the tire volume using the tire_volume function
    volume = tire_volume(w, a, d)
    
    # Print the calculated tire volume
    print(f"The volume of the tire is approximately {volume:.2f} liters.")

    # Get the current date from the computer's operating system
    current_date = datetime.datetime.now().date()
 # Format the current date in the "YYYY-MM-DD" format
    formatted_date = current_date.strftime("%Y-%m-%d")

    # Open the text file named volumes.txt for appending
    with open("volumes.txt", "a") as file:
        # Append the values to the end of the volumes.txt file
        file.write(f"{formatted_date}, {w}, {a}, {d}, {volume:.2f}\n")

# Check if the script is being run directly or imported as a module
# If it is run directly, call the main function to execute the program
if __name__ == "__main__":
    main()
