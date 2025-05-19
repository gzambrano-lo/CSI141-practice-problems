# Prompt the user for a word
word = input("Enter a word: ")
# Prompt the user for the first and last index
first_index = int(input("Enter the first index: "))
last_index = int(input("Enter the last index: "))
# Slice the word using the provided indexes and print the result
print("Sliced word:", word[first_index:last_index])
