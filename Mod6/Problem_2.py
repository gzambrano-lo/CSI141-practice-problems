'''2. Create a list of strings. Write code
# that counts how many times the word "Olympic" appears in the list, and then print the count.'''

# Create a list of strings 
word_list = ["Olympic","games", "Olympic", "torch", "Olympic", "medal", "sport"]

# Count how many times "Olympic" appears 
count = 0 
for word in word_list:
    if word == "Olympic":
        count += 1 
        
# Print the count 
print("The word 'Olympic' appears", count, "times in the list.")
