Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)

# Prompt the user for a sentence 
sentence = input("Enter a sentence: ")
# Prompt the user for a word to find 
word = input ("Enter a word to find in the sentence: ") 
# Check if the word is in the sentence and print the result
print(word in sentence)
