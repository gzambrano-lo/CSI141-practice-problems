# '''3. Create a list of strings.
# Write code to create a new list that includes only the strings longer than three characters.
# Print the resulting filtered list.'''

# Create a list of strings 
words = ["collosal", "jaw", "cart", "armed", "founding", "vs", "warhammer"] 

# Create a new list with only strings longer than 3 characters 
filtered_words = [] 
for word in words: 
    if len(word) > 3: 
        filtered_words.append(word) 
        
# Print the resulting list 
print("Filtered list(words longer than 3 characters):", filtered_words)
