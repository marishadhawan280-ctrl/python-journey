print("=== Daily Energy Check ===")
energy_level = int(input("What is your energy level today? (1-10): "))
streak_active = input("Is your Git streak on the line? (yes/no): ").strip().lower() == "yes"

if energy_level <= 3 and streak_active:
    print("Decision: Write a tiny script, push it immediately, and go rest.")
elif energy_level <= 3 and not streak_active:
    print("Decision: Close the laptop. You need sleep more than code today.")
elif energy_level > 3 and energy_level < 7:
    print("Decision: Review some notes, do 30 minutes, then log off.")
else:
    print("Decision: Let's build something complex!")