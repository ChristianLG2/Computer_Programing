#Christian Lira Spring 2023 
''' This code is a Python program that calculates fuel efficiency in two different units: Miles Per Gallon (MPG) and Liters per 100 kilometers (LPK100K). It does this using three functions: main(), miles_per_gallon(), and lpk100k_from_mpg().'''

def main ():
    start_odometer = float(input("Enter your Starting odometer value in miles: "))
    end_odometer = float(input("Enter your Ending odometer value in miles: "))
    fuel = float(input("Enter the amount of fuel in gallons: "))

    mpg = miles_per_gallon(start_odometer,end_odometer,fuel)
    lpk100k = lpk100k_from_mpg(mpg)
    print()
    print("Miles Per Gallon: ", mpg)
    print("Liters per 100 kilometers: ", lpk100k)
    pass 


def miles_per_gallon(start_odometer, end_odometer, fuel):
    mpg = (end_odometer - start_odometer) / fuel
    return mpg 

def lpk100k_from_mpg(mpg):
    lpk100k = 235.215/mpg 
    return lpk100k


main()



