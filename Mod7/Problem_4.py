#'''#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
#State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
#* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
#* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
#* Children (0-18): Free.'''

# Function: ferry_fare(age, vehicle)
# Goal: Calculate and return the correct Washington State Ferry fare based on the persons age
# and wether they have a vehicle.
# Input: Age (int), Vehicle (boolean)
# Output: A number (float or int representing the fair in dollars)
# Function body: Check age group (child, adult or senior), inside each group, check if
# vehicle is true or false
# Return the correct fare accordingly

def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif 19 <= age <= 64:
        if vehicle:
            return 20
        else:
            return 10
    elif age >= 65:
        if vehicle:
            return 15
        else:
            return 5

#print(ferry_fare(30, False))  # 10
#print(ferry_fare(30, True))   # 20
#print(ferry_fare(70, False))  # 5
#print(ferry_fare(70, True))   # 15
#print(ferry_fare(12, False))  # 0
#print(ferry_fare(17, True))   # 0
