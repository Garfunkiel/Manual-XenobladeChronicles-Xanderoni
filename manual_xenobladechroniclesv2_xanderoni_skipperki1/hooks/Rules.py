from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def questPaolaAndNarineReq():
    return "|Shulk Progressive Affinity Rank:4| AND |Reyn Progressive Affinity Rank:4|" \
                " AND ((|Sharla Progressive Affinity Rank:4| AND |Melia Progressive Affinity Rank:4|) " \
                " OR (|Sharla Progressive Affinity Rank:4| AND |Fiora Progressive Affinity Rank:4|)" \
                " OR (|Sharla Progressive Affinity Rank:4| AND |Seven Progressive Affinity Rank:4|)" \
                " OR (|Melia Progressive Affinity Rank:4| AND |Fiora Progressive Affinity Rank:4|)" \
                " OR (|Melia Progressive Affinity Rank:4| AND |Seven Progressive Affinity Rank:4|)" \
                ")"

REGION_LEVELS = [
    {"region": "Colony 9",                      "level":  1, "requires": ""},
    {"region": "Tephra Cave",                   "level": 12, "requires": "|Tephra Cave Key:1|"},
    {"region": "Bionis' Leg",                   "level": 25, "requires": "|Bionis' Leg Key:1|"},
    {"region": "Colony 6",                      "level": 26, "requires": "|Colony 6 Key:1|"},
    {"region": "Ether Mine",                    "level": 27, "requires": "|Ether Mine Key:1|"},
    {"region": "Satorl Marsh",                  "level": 28, "requires": "|Satorl Marsh Key:1|"},
    {"region": "Bionis' Interior (1st Visit)",  "level": 32, "requires": "|Bionis' Interior (1st Visit) Key:1|"},
    {"region": "Makna Forest",                  "level": 34, "requires": "|Makna Forest Key:1|"},
    {"region": "Frontier Village",              "level": 36, "requires": "|Frontier Village Key:1|"},
    {"region": "Eryth Sea",                     "level": 37, "requires": "|Eryth Sea Key:1|"},
    {"region": "Alcamoth",                      "level": 37, "requires": "|Alcamoth Key:1|"},
    {"region": "High Entia Tomb",               "level": 38, "requires": "|High Entia Tomb Key:1|"},
    {"region": "Prison Island (1st Visit)",     "level": 42, "requires": "|Prison Island (1st Visit) Key:2|"},
    {"region": "Valak Mountain",                "level": 48, "requires": "|Valak Mountain Key:2|"},
    {"region": "Sword Valley (MISSABLE)",       "level": 52, "requires": "|Sword Valley Key:2| AND |Progressive Hunting License:10|"},
    {"region": "Galahad Fortress (MISSABLE)",   "level": 55, "requires": "|Galahad Fortress Key:2|"},
    {"region": "Fallen Arm",                    "level": 58, "requires": "|Fallen Arm Key:2|"},
    {"region": "Mechonis Field (MISSABLE)",     "level": 60, "requires": "|Mechonis Field Key:2|"},
    {"region": "Central Factory (MISSABLE)",    "level": 65, "requires": "|Central Factory Key:2|"},
    {"region": "Agniratha (MISSABLE)",          "level": 70, "requires": "|Agniratha Key:3|"},
    {"region": "Mechonis Core",                 "level": 72, "requires": "|Mechonis Core Key:3| AND |Progressive Hunting License:16|"},
    {"region": "Bionis' Interior (2nd Visit)",  "level": 75, "requires": "|Bionis' Interior (2nd Visit) Key:3|"},
    {"region": "Prison Island (2nd Visit)",     "level": 80, "requires": "|Prison Island (2nd Visit) Key:3|"},
    {"region": "Memory Space",                  "level": 82, "requires": "|Memory Fragment:20|"}
]

def hasDangerTolerance(multiworld: MultiWorld, player: int, monsterLevel: int):
    DT = get_option_value(multiworld, player, "Danger_Tolerance")
    effectiveLevel = monsterLevel - DT

    requirements = ""

    for region in REGION_LEVELS:
        if requirements != "":
            requirements += " AND "
        requirements += region["requires"]

        if effectiveLevel < region["level"]:
            break

    if requirements != "":
        return requirements
    return True