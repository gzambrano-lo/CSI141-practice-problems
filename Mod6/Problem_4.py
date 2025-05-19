# '''4.  Create a list of integers.
# Write code that counts how many numbers are positive and how many are negative,
# then print both counts.'''

# Create a list of integers 
numbers = [5, -3, 0, 12, -8, -1, 7, -6, 4]

# Initialize counters 
positive_count = 0 
negative_count = 0 

# Loop through the list and count positives and negatives 
for num in numbers: 
    if num > 0: 
        positive_count += 1 
    elif num < 0:
        negative_count += 1 
        
# Print the results 
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
