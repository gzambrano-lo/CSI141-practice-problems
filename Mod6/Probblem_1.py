# '''1. Create a list of integers (you get to pick!).
# Write code to iterate through the list and calculate the sum of all even numbers.
# Print the resulting sum'''

# Create a list of integers 
my_numbers = [3, 6, 8, 11, 14, 17, 20]
even_sum = 0 
# Calculate the sum of all even numbers 
for num in my_numbers: 
    if num % 2 == 0: 
        even_sum += num 

# Print resulting sum 
print("The sum of all even numbers is:", even_sum)
