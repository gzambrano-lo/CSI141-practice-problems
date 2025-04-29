# '''Create a program that prompts for the side lengths of a triangle and
# computes the area using Heron's formula. '''

import math  # We need this for the square root function

# Ask the user for the three side lengths
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Show the result
print("The area of the triangle is:", area)

