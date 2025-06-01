#'''3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
# For example, water is very effective to fight fire.
# Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
# strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
# simple type effectiveness rules. Your solution only needs to work for these three sets of input:
# print(type_advantage("Water", "Fire")) # "Super Effective"
# print(type_advantage("Fire", "Water")) # "Not Very Effective"
# print(type_advantage("Electric", "Grass")) # "Neutral"'''

# Function: type_advantange(attacker, defender)
# Goal/Description: Determine if pokemon type is super effective, not very effective, or neutral.
# Input: Attacker, Defender
# Output: Super Effective, Not Very Effective, Neutral
# Test: Water + Fire = Super Effective, Fire + Water = Not Very Effective, Electric + Grass = Neutral

def type_advantage(attacker, defender):
    attacker = attacker.lower()
    defender = defender.lower()

    if attacker == 'water' and defender == "fire":
        return "Super Effective"
    elif attacker == "fire" and defender == "water":
        return "Not Very Effective"
    else:
        return "Neutral"

print(type_advantage("Water", "Fire"))      # Super Effective
print(type_advantage("Fire", "Water"))      # Not Very Effective
print(type_advantage("Electric", "Grass"))  # Neutral
