# Using string multiplication to create a quick visual border
print("=" * 25)
print("   SUNDAY NIGHT RESET   ")
print("=" * 25)

prep_status = input("Is your bag packed and laptop charged for tomorrow? (yes/no): ").strip().lower()

if prep_status == "yes":
    print("\nSystem: Excellent. You are set up for a strong start to the week.")
else:
    print("\nSystem: Action required. Take 5 minutes to prep now to save 20 minutes tomorrow morning.")

print("Git Streak: Day 7 Secured. Have a good night!")