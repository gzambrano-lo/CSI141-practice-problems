Prompt the user with their name and age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

# Prompt the user for their name and age 
name = input ("What is your name?")
age = input("How old are you?")
# Calculate their age for next year 
next_year_age = int(age) + 1 
# Print the message using string concatenation 
print("Hello, " + name + "!You are " + age + " years old. Next year, you will be " + str(next_year_age) + " years old.") 
