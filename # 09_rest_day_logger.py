print("=== Weekend Commit Saver ===")
journal_entry = input("How was your day? (in one sentence): ").strip().lower()

# Using the 'in' keyword to check for specific words inside the string
if "tired" in journal_entry or "long" in journal_entry or "exhausted" in journal_entry:
    print("\nSystem: You showed up anyway to keep the streak. That is raw discipline.")
    print("Action: Close the laptop and go to sleep immediately.")
else:
    print("\nSystem: Streak secured! Rest up for tomorrow.")