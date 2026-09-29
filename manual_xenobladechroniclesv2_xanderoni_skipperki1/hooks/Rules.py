from Options import OptionError
from typing import Optional, TYPE_CHECKING
from worlds.AutoWorld import World
from .Collectopaedia import COLLECTOPAEDIA_REQUIREMENTS, GROUP_COUNTS
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

if TYPE_CHECKING:
    from .. import ManualWorld

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

def questPaolaAndNarineReq(state: CollectionState, player: int) -> bool|str:
    shulkAt4 = state.count("Shulk Progressive Affinity Rank", player) >= 4
    reynAt4 = state.count("Reyn Progressive Affinity Rank", player) >= 4
    sharlaAt4 = state.count("Sharla Progressive Affinity Rank", player) >= 4
    meliaAt4 = state.count("Melia Progressive Affinity Rank", player) >= 4
    sevenAt4 = state.has("Seven's Affinity Rank 4", player)

    shulkAndReynAt4 = shulkAt4 and reynAt4
    sharlaAndMeliaAt4 = sharlaAt4 and meliaAt4
    sharlaAndSevenAt4 = sharlaAt4 and sevenAt4
    meliaAndSevenAt4 = meliaAt4 and sevenAt4
    anyTwoWomenAt4 = sharlaAndMeliaAt4 or sharlaAndSevenAt4 or meliaAndSevenAt4

    return shulkAndReynAt4 and anyTwoWomenAt4

def questPaolaAndNarineReqRule(player: int, world: "ManualWorld") -> str:
    value = questPaolaAndNarineReq(world.multiworld.state, player)
    if (value == True):
        return ""
    return value

REGION_LEVELS = [
    {"region": "Colony 9",                      "level":  7, "requires": "|Colony 9 Access|"},
    {"region": "Tephra Cave",                   "level": 12, "requires": "|Tephra Cave Access|"},
    {"region": "Bionis' Leg",                   "level": 25, "requires": "|Bionis' Leg Access|"},
    {"region": "Colony 6",                      "level": 26, "requires": "|Colony 6 Access|"},
    {"region": "Ether Mine",                    "level": 27, "requires": "|Ether Mine Access|"},
    {"region": "Satorl Marsh",                  "level": 28, "requires": "|Satorl Marsh Access|"},
    {"region": "Bionis' Interior (1st Visit)",  "level": 32, "requires": "|Bionis' Interior (1st Visit) Access|"},
    {"region": "Makna Forest",                  "level": 34, "requires": "|Makna Forest Access|"},
    {"region": "Frontier Village",              "level": 36, "requires": "|Frontier Village Access|"},
    {"region": "Eryth Sea",                     "level": 37, "requires": "|Eryth Sea Access|"},
    {"region": "Alcamoth",                      "level": 37, "requires": "|Alcamoth Access|"},
    {"region": "High Entia Tomb",               "level": 38, "requires": "|High Entia Tomb Access|"},
    {"region": "Prison Island (1st Visit)",     "level": 42, "requires": "|Prison Island (1st Visit) Access|"},
    {"region": "Valak Mountain",                "level": 48, "requires": "|Valak Mountain Access|"},
    {"region": "Sword Valley (MISSABLE)",       "level": 52, "requires": "|Sword Valley Access|"},
    {"region": "Galahad Fortress (MISSABLE)",   "level": 55, "requires": "|Galahad Fortress Access|"},
    {"region": "Fallen Arm",                    "level": 58, "requires": "|Fallen Arm Access|"},
    {"region": "Mechonis Field (MISSABLE)",     "level": 60, "requires": "|Mechonis Field Access|"},
    {"region": "Central Factory (MISSABLE)",    "level": 65, "requires": "|Central Factory Access|"},
    {"region": "Agniratha (MISSABLE)",          "level": 70, "requires": "|Agniratha Access|"},
    {"region": "Mechonis Core",                 "level": 72, "requires": "|Mechonis Core Access|"},
    {"region": "Bionis' Interior (2nd Visit)",  "level": 75, "requires": "|Bionis' Interior (2nd Visit) Access|"},
    {"region": "Prison Island (2nd Visit)",     "level": 80, "requires": "|Prison Island (2nd Visit) Access|"}
]

def hasDangerTolerance(multiworld: MultiWorld, player: int, monsterLevel: int) -> bool|str:
    DT = get_option_value(multiworld, player, "Danger_Tolerance")

    if not type(DT) is int:
        raise OptionError("Danger Tolerance must be an integer value")

    if get_option_value(multiworld, player, "Post_Game") == True:
        return True

    effectiveLevel = monsterLevel - DT

    requirements = ""

    for region in REGION_LEVELS:
        requirements = region["requires"]

        if effectiveLevel < region["level"]:
            break

    if requirements != "":
        return requirements
    return True

def hasDangerToleranceRule(player: int, monsterLevel: int, world: "ManualWorld") -> str:
    value = hasDangerTolerance(world.multiworld, player, monsterLevel)
    if (value == True):
        return ""
    return value

def stateHasAreaCategory(state: CollectionState, player: int, area: str, category: str):
    if area == "Alcamoth - FC":
        return state.has("Alcamoth - FC All Categories", player)
    elif area == "Bionis' Shoulder":
        if category == "Vegetable":
            return state.has("Bionis' Shoulder Vegetable Category", player)
        elif category == "Animal":
            return state.has("Bionis' Shoulder Animal Category", player)
        elif category == "Part":
            return state.has("Bionis' Shoulder Part Category", player)
        elif category == "Strange":
            return state.has("Bionis' Shoulder Strange Category", player)
        else:
            return True

    requiredProgCats = COLLECTOPAEDIA_REQUIREMENTS[area][category]
    return requiredProgCats == 0 or state.count(f"Progressive {category} Category", player) >= requiredProgCats

def collectopaediaAvailable(state: CollectionState, player: int, area: str, category: str):
    if category != "ALL":
        return stateHasAreaCategory(state, player, area, category)

    for cat in ["Vegetable", "Flower", "Fruit", "Animal", "Bug", "Nature", "Part", "Strange"]:
        if not stateHasAreaCategory(state, player, area, cat):
            return False

    return True

def collectopaediaItemsCollected(state: CollectionState, player: int, area: str, category: str):
    if category == "ALL":
        grp = (f"Alcamoth Collectopaedia" if area == "Alcamoth - FC" else f"{area} Collectopaedia")
        return state.has_group(grp, player, GROUP_COUNTS[area][category])

    if area not in GROUP_COUNTS:
        return True

    count = GROUP_COUNTS[area][category]
    if count == 0:
        return True

    if area == "Alcamoth - FC":
        area = "Alcamoth"

    return state.has_group(f"{area} Collection ({category})", player, count)

def collectopaediaComplete(multiworld: MultiWorld, state: CollectionState, player: int, area: str, category: str):
    colOption = get_option_value(multiworld, player, "Collectopaedia")

    return (
        # NO COLLECTOPAEDIA
        (colOption == 0)
        # CATEGORIES REQUIRED BUT NOT INDIVIDUAL ITEMS
        or (
            colOption == 1
            and collectopaediaAvailable(state, player, area, category)
        )
        # CATEGORIES AND INDIVIDUAL ITEMS REQUIRED
        or (
            colOption >= 2
            and collectopaediaAvailable(state, player, area, category)
            and collectopaediaItemsCollected(state, player, area, category)
        )
    )