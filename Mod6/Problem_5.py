# '''5. Create a list of integers.
# Use a loop to build a new list where each element is the square of the corresponding element in the original list.
# Print the new list.'''

# Create a list of integers 
numbers = [2, 4, -3, 6, 0, 1] 

# Create a new list to store the squares 
squared_numbers = [] 

# Loop through the original list and add the square of each number 
for num in numbers:
    squared_numbers.append(num ** 2) 
    
# Print the new list 
print("Squared numbers:", squared_numbers)
