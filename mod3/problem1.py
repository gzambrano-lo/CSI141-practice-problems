#  Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.

# Prompt user for a word 
word = input("Enter a Word: ") 
# Prompt the user for how many times to repeat a word 
times = int(input("How many times would you like to repeat the word?"))
# Print the word the specified number of times 
for i in range(times): 
    print(word)
