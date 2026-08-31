# Collect user inputs
name = input("Please enter your name: ")
print(f"Hello {name}! Welcome to your personalized study tracker.")

# Collect user inputs
age = int(input("Please enter your age: "))
hours = float(input("Please enter your weekly study time in HOURS: "))
per_day = hours / 7
per_month = per_day * 30

# Generate and print the final track
print(f"\nYou are currently {age} years old.\nYour total monthly study time is {per_month:.2f} hours, considering a 30-day average month. Keep up the hard work!")