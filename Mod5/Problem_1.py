#'''1. Prompt the user for a positive integer n.
# Use a while loop to sum all the integers from 1 up to n. Print the final sum.'''

# Promp the user for a postive integer 
n = int(input("Entera positive integer: "))
total = 0 
i = 1 
# Use a while loop to sum all the integers from 1 up to n. 
while i <= n: 
    total += i 
    i += 1 
# Print the final sum     
print("The sum from 1 to", n, "is", total)
