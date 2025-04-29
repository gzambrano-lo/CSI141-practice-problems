# '''Create a program that prompts the user for their birth year
# and displays a message that says "You are ___ old"'''

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Get the current year
current_year = 2025

# Calculate the age
age = current_year - birth_year

# Display the result using an f-string
print(f"You are {age} years old.")
