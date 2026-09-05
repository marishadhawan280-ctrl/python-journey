print("=== Portal Registration Setup ===")
username = input("Create a username: ")

# Validation Engine
if len(username) < 4 or len(username) > 12:
    print("Error: Username must be between 4 and 12 characters long.")
elif username.count(" ") > 0: # Alternatively: username.find(" ") != -1
    print("Error: Username cannot contain spaces.")
elif not username.isalnum():
    print("Error: Username can only contain letters and numbers (no special characters).")
elif not username[0].isalpha():
    print("Error: Username must start with a letter, not a number.")
else:
    print(f"Success! The username '{username}' is valid and accepted.")