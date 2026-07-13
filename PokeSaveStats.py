"""
    PokeSaveStats.py
    Jack Verdin
    This program uses Path and json to read and write details about pokemon to a file. This allows the user to easily use a preset set of stats and typings for the main program.
    7/9/2026
"""

from pathlib import Path
import typechart

savefile = Path("saved_pokemon.txt")
pokelist = savefile.read_text().rstrip()

def addnewentry(name, hp, patk , pdef, satk, sdef, type1, type2):
    savefile = Path("saved_pokemon.txt")
    pokelist = savefile.read_text().rstrip()
    # Name HP PhAttack PhDefence SpAttack SpDefence Type1 Type2
    pokelist = f"{pokelist}\n{name} {hp} {patk} {pdef} {satk} {sdef} {type1} {type2}"
    savefile.write_text(pokelist)

def readpokelist(getvalues = False):
    """Reads from saved_pokemon.txt and outputs the stored information as a dict. Can optionally provide a key to get the values of the dict directly.

    Args:
        getvalues (str, optional): If provided acts as a key for the dict. Defaults to False.

    Returns:
        list/dict/bool: Returns the entire dict if getvalues is False, returns a list of values if getvalues is a valid key, returns False if a KeyError was triggered
    """
    savefile = Path("saved_pokemon.txt")
    pokelist = savefile.read_text().rstrip()
    biglist = []
    listnum = 0

    # Separate each line into their own strings, and split each line into a list
    for line in pokelist.splitlines():
        biglist.append([])
        for bit in line.split():
            biglist[listnum].append(bit)
        listnum +=1

    # Creates a dict with the name of the pokemon being the key and the value being a list containing all the stats and details
    outputdict = {}
    for chunks in biglist:
        outputdict[chunks[0]] = [int(chunks[1]), int(chunks[2]), int(chunks[3]), int(chunks[4]), int(chunks[5]), chunks[6], chunks[7]]

    # If getvalues is the default (False), then the entire dict is outputted
    # If a value is given and it triggers a KeyError, False is returned
    # If a value is given and it matches a key, it returns the corresponding value
    if getvalues:
        try:
            outputvalues = outputdict[getvalues]
        except KeyError:
            return False
        else:
            return outputvalues
    else:
        return outputdict

# BASIC IDEA: Subject To Change
# Ask user what to do: Simulate or Add New Pokemon
    # Adding a new Pokemon, get input for all the stats and a name
    # Save the details to a text file
    # Loop back to start
# Simulate battle
# Program extracts stats and names saved in file
# List of saved pokemon is given to user to choose from (Always lists all pokemon in file)
# Rest of PokeDamageCalc.py plays out as ususal