"""
    PokeSaveStats.py
    Jack Verdin
    This program uses Path and json to read and write details about pokemon to a file. This allows the user to easily use a preset set of stats and typings for the main program.
    7/9/2026
"""

from pathlib import Path
import json

# BASIC IDEA: Subject To Change
# Ask user what to do: Simulate or Add New Pokemon
    # Adding a new Pokemon, get input for all the stats and a name
    # Save the details to a json file
    # Loop back to start
# Simulate battle
# Program extracts stats and names saved in file
# List of saved pokemon is given to user to choose from (Always lists all pokemon in file)
# Rest of PokeDamageCalc.py plays out as ususal