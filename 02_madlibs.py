print("Welcome to the Mad Libs Generator!")

# Collect user inputs
adj = input("Enter an adjective: ")
place = input("Enter a place of your choice: ")
time = input("Enter a suitable time (e.g., 8 PM, midnight): ")
adj2 = input("Enter a second adjective: ")
adj3 = input("Enter a third adjective (e.g., best, worst): ")
option = input("Choose between 'do' or 'do not': ")

# Generate and print the final story
print(f"\nToday was a {adj} day. I went to {place} at {time}. I had a few of my friends along. It was a {adj2} decision to come upon but mutually agreed and for the {adj3}. It will be better if we {option} talk about it when we meet.")