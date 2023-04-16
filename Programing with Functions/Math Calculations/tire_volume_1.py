
import math

def tire_volume(w, a, d):
    return (math.pi * w**2 * a * w * a + 2540 * d) / 10000000000

def main():
    print("Enter the tire width (e.g., 205):")
    w = int(input())
    
    print("Enter the aspect ratio (e.g., 60):")
    a = int(input())
    
    print("Enter the wheel diameter (e.g., 15):")
    d = int(input())

    volume = tire_volume(w, a, d)
    print(f"The volume of the tire is approximately {volume:.2f} liters.")

if __name__ == "__main__":
    main()
