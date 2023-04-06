#CHristian Lira - Last Revised WInter 2023
#Define Functions 
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def wind_chill(fahrenheit, mph):
    p1 = 0.6215 * fahrenheit
    p2 = 35.75 * (mph ** 0.16)
    p3 = 0.4275 * fahrenheit * (mph ** 0.16)
    return 35.74 + p1 - p2 + p3

def print_wind_chill_table(fahrenheit):
    for speed in range(0, 61, 5):
        wind_chill_speed = wind_chill(fahrenheit, speed)
        print(f"At a temperature of {fahrenheit}°F and wind speed of {speed} mph, the wind chill is {wind_chill_speed:.2f}°F\n")

# Get temperature input in Celsius and convert to Fahrenheit
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius:.2f} Celsius is: {fahrenheit:.2f} Fahrenheit")
print(f"The current weather is {fahrenheit:.2f} Fahrenheit")

# Get wind speed input in mph
mph = int(input("What is the wind speed? (mph)"))

# Calculate the wind chill
current_wind_chill = wind_chill(fahrenheit, mph)
print(f"The current Wind Chill is equal to {current_wind_chill:.2f}")

# Calculate the wind chill for different wind speeds
print_wind_chill_table(fahrenheit)
