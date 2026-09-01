print("--- Interactive Smart Calculator ---")

# Collect inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose an operator (+, -, *, /): ")

# 1. Validation using Logical Operators (not, or, ==)
if not (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
    print("Error: Invalid operator selected. Please restart and use +, -, *, or /.")
else:
    print("\n--- Number Analysis ---")
    
    # 2. Number analysis using Comparison Operators (==, !=, >, <, >=, <=) and Logical (and)
    if num1 == num2:
        print("Note: The two numbers are perfectly equal.")
        
    if num1 != num2:
        if (num1 > num2) and (num1 >= 0):
            print(f"Note: {num1} is strictly greater than {num2} and is a positive number (or zero).")
        if (num1 < num2) and (num2 <= 1000):
            print(f"Note: {num1} is strictly less than {num2}, and {num2} is 1000 or below.")

    print("\n--- Calculation Result ---")
    
    # 3. Execution using if-elif-else structure
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == '/':
        # Safe handling of division by zero
        if num2 == 0:
            print("Math Error: Cannot divide by zero! Safe termination triggered.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")