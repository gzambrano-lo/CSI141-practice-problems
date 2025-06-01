# 1. Write a function called count_vowels(input) that takes a string
# and returns the number of vowels (a, e, i, o, u) in it.

def count_vowels(input):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello, world!"))
