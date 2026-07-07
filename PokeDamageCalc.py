"""
    PokeDamageCalc.py
    Jack Verdin
    The main file for my Project 1 program. The program acts as a simplified Pokemon damage calculator.
    6/28/2026
"""

import typechart

# Function: Display a number as a percent of another number, rounded to two decimal places
def percentof(part=10, total=10):
    """ Calculates what percent one number is of another.

    Args:
        part (int, optional): The number to be converted into a percent. Defaults to 10.
        total (int, optional): The base value. Defaults to 10.

    Returns:
        float: The percent of part/total, rounded to 2 decimal places
    """
    if total == 0: return 100
    percent = part / total
    percent *= 100
    percent = round(percent, 2)
    return percent

# Function: While loop input validation in one function
def valid_input(message, allowed):
    """Uses a while loop and list to ensure an allowed input is submitted.

    Args:
        message (string): A message for the input() function
        allowed (list/tuple): A list of allowed inputs

    Returns:
        string: The input given from the user, but only if it is found in the allowed list
    """
    given_value = ""
    allowed = [str(a) for a in allowed]
    while len(given_value) < 1:
        given_value = input(message)
        if given_value not in allowed:
            given_value = ""
            print("Invalid input.")
    return given_value

# Function needed: Damage Calculator
def damage_calc(basepower=100, total_atk=100, total_def=100, type_mult=1, stab=1, rand_adjust=1):
    """A simplified version of the Pokemon damage formula.

    Args:
        basepower (int, optional): The base power of the used move. Defaults to 100.
        total_atk (int, optional): The effective attack stat, including changes due to stages. Defaults to 100.
        total_def (int, optional): The effective defence stat, including changes due to stages. Defaults to 100.
        type_mult (int, optional): The total multiplier due to type matchups. Defaults to 1.
        stab (int, optional): An additional multiplier for STAB. Defaults to 1.
        rand_adjust (int, optional): A manual adjustment used in the function. In the real formula is a random number from 0.85 to 1. Defaults to 1.

    Returns:
        int: The final amount of damage dealt.
    """
    if type_mult == 0: return 0 # If the type mult is 0, don't bother calculating the damage
    if basepower < 1: basepower = 1 # 1 Is the minimum for power
    if total_atk < 1: total_atk = 1 # 1 Is the minimum for attack
    if total_def < 1: total_def = 1 # 1 Is the minimum for defence, also avoids divide by zero error
    final_damage = (((22 * basepower * (total_atk / total_def)) / 50) + 2) * type_mult * stab * rand_adjust
    final_damage = round(final_damage)
    if final_damage < 1: final_damage = 1 # 1 Is the minimum for damage dealt
    return final_damage

# Function needed? Type effectiveness to message
def type_message(type_mult=1):
    """Takes a type effectiveness float and returns the appropriate message.

    Args:
        type_mult (float/int): The input type effectiveness. Defaults to 1.

    Returns:
        string: The matching message for the type effectiveness.
    """
    match type_mult:
        case 0:
            return "It had no effect!"
        case 0.25:
            return "It's barely effective!"
        case 0.5:
            return "It's not very effective."
        case 1:
            return "It's regularly effective"
        case 2:
            return "It's supereffective!"
        case 4:
            return "It's extremely effective!"
        case _:
            return "Unexpected Value"

# Function: Stage Multiplier
def stage_mult(value=10, stage=0):
    """Multiplies a value using pokemon's stage system

    Args:
        value (int, optional): the input value of the function. Defaults to 10.
        stage (int, optional): the stage multiplier, an int between -6 and 6. Defaults to 0.

    Returns:
        int: the output value, given as a rounded int
    """
    # Stages must be an integer
    stage = round(stage)
    # A stage of 0 results in no change to value, so it's skipped early
    if stage == 0:
        return value
    # Stages must be between -6 and 6
    if abs(stage) > 6:
        if stage > 0:
            stage = 6
        else:
            stage = -6
    # Stages begin with a fraction of 2/2
    stage_num = 2
    stage_den = 2
    # Positive stages add to numerator, negative stages add to denomenator
    if stage > 0:
        stage_num += stage
    else:
        stage_den += abs(stage)
    # Multiplier is calculated by the fraction
    mult = stage_num / stage_den
    return round(value * mult)

# Code needed: User input
print("- Pokemon Damage Calculator -\n")

# input block for stats and stages
given_atk = int(valid_input("Please input the attacking Pokemon's Attack stat: ", list(range(1,740))))
if given_atk < 1: given_atk = 1
given_atkst = int(valid_input("Please input the attacking Pokemon's Attack stage: ", list(range(-6,7))))
given_def = int(valid_input("Please input the defending Pokemon's Defence stat: ", list(range(1,740))))
if given_def < 1: given_def = 1
given_defst = int(valid_input("Please input the defending Pokemon's Defence stage: ", list(range(-6,7))))
given_hp = int(valid_input("Please input the defending Pokemon's max HP: ", list(range(1,740))))
if given_hp < 1: given_hp = 1
given_power = int(valid_input("Please input the base power of the move used: ", list(range(1,256))))
if given_power < 1: given_power = 1

# input block for type-related values
given_typeatk = valid_input("Please input the type of the move used: ", typechart.type_list)
given_typeatk = typechart.type_list.index(given_typeatk)
given_typedef1 = valid_input("Please input the first type of the defending Pokemon: ", typechart.type_list)
given_typedef1 = typechart.type_list.index(given_typedef1)
given_typedef2 = valid_input("Please input the second type of the defending Pokemon: ", typechart.type_list)
given_typedef2 = typechart.type_list.index(given_typedef2)
total_typemult = typechart.type_calc(given_typeatk, given_typedef1) * typechart.type_calc(given_typeatk, given_typedef2)

given_stab = valid_input("Does the move used benefit from the Same Type Attack Bonus?(Y/N) ", ["Y", "N"])
if given_stab == "Y": given_stab = 1.5
else: given_stab = 1

# Calculates the total stats based on the given value and stage
total_atk = stage_mult(given_atk, given_atkst)
print(f"With an Attack stat of {given_atk} at stage {given_atkst},\nthe attacking Pokemon has an effective Attack stat of {total_atk}")
total_def = stage_mult(given_def, given_defst)
print(f"With an Defence stat of {given_def} at stage {given_defst},\nthe defending Pokemon has an effective Defence stat of {total_def}")

# Outputs the type matchup info for the user
print(f"Using a {typechart.type_list[given_typeatk]}-type move against a {typechart.type_list[given_typedef1]}/{typechart.type_list[given_typedef2]} Pokemon results in a type multiplier of {total_typemult}")
print(type_message(total_typemult))

if total_typemult == 0:
    # If total_typemult is 0, then the move will never deal damage
    # No need to bother calculating
    print("This move will not deal any damage!")
else:
    damage_min = damage_calc(given_power, total_atk, total_def, total_typemult, given_stab, 0.85)
    damage_max = damage_calc(given_power, total_atk, total_def, total_typemult, given_stab, 1)
    # Code needed: Output message to terminal
    print(f"On a low roll, this move will deal {damage_min} damage, or {percentof(damage_min, given_hp)}% of the opposing Pokemon's health.")
    print(f"On a high roll, this move will deal {damage_max} damage, or {percentof(damage_max, given_hp)}% of the opposing Pokemon's health.")

    # Calcs number of hits for all low rolls
    num_hits = 0
    hp_left = given_hp
    while hp_left > 0:
        num_hits += 1
        hp_left -= damage_min
    print(f"When landing all low rolls, it takes {num_hits} hit(s) to KO the opponent from full health.")
    
    # Calcs number of hits for all high rolls
    num_hits = 0
    hp_left = given_hp
    while hp_left > 0:
        num_hits += 1
        hp_left -= damage_max
    print(f"When landing all high rolls, it takes {num_hits} hit(s) to KO the opponent from full health.")

input("Input anything to close program.")