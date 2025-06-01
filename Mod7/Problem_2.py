# 2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
# (reads the same forward and backward, ignoring case). The function should
# returns either True or False.
# Test: madam (True), butter (False), Level (True)
# Input: string (s)
# Output: boolean
# Function body: lowercase s, flip s and save to new variable (flipped_s) and then compare s & flipped_s

def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s

print(is_palindrome("madam"))
print(is_palindrome("butter"))
print(is_palindrome("Level"))
