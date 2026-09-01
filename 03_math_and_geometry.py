import math

def run_calculator():
    print("--- Geometry & Math Calculator ---")
    
    # Circle Calculations (*, **, math.pi, round)
    print("\n[1] Circle Calculations")
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    
    print(f"Area: {round(area, 2)}")
    print(f"Circumference: {round(circumference, 2)}")
    
    # Pythagorean Theorem (+, **, math.sqrt)
    print("\n[2] Right Triangle Calculations")
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    
    hypotenuse = math.sqrt((side_a ** 2) + (side_b ** 2))
    print(f"Hypotenuse (Side C): {round(hypotenuse, 2)}")
    
    # Arithmetic Demonstrations (-, /)
    print("\n[3] Advanced Analytics")
    difference = area - circumference
    half_hypotenuse = hypotenuse / 2
    
    print(f"Difference between circle area and circumference (-): {round(difference, 2)}")
    print(f"Half of the hypotenuse length (/): {round(half_hypotenuse, 2)}")
    
    # Unit Conversion (//, %)
    print("\n[4] Integer Math Demonstration")
    cm = int(input("Enter a total distance in centimeters (integer): "))
    meters = cm // 100
    remaining_cm = cm % 100
    
    print(f"{cm} cm is equal to {meters} meters and {remaining_cm} centimeters.")

if __name__ == "__main__":
    run_calculator()