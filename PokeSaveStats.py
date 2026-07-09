"""
    PokeSaveStats.py
    Jack Verdin
    This program uses Path and json to read and write details about pokemon to a file. This allows the user to easily use a preset set of stats and typings for the main program.
    7/9/2026
"""

from pathlib import Path

savefile = Path("saved_pokemon.txt")
pokelist = savefile.read_text()
# Name HP Attack Defence SpAttack SpDefence Type1 Type2
print(pokelist)


given_name = input("Name: ")
given_hp = input("HP: ")
given_atk = input("Attack: ")
given_def = input("Defence: ")
given_satk = input("Special Attack: ")
given_sdef = input("Special Defence: ")
given_type1 = input("Type1: ")
given_type2 = input("Type2: ")

pokelist = f"{pokelist}\n{given_name} {given_hp} {given_atk} {given_def} {given_satk} {given_sdef} {given_type1} {given_type2}"

savefile.write_text(pokelist)

# BASIC IDEA: Subject To Change
# Ask user what to do: Simulate or Add New Pokemon
    # Adding a new Pokemon, get input for all the stats and a name
    # Save the details to a text file
    # Loop back to start
# Simulate battle
# Program extracts stats and names saved in file
# List of saved pokemon is given to user to choose from (Always lists all pokemon in file)
# Rest of PokeDamageCalc.py plays out as ususal