# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from typing import Any
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item
from Options import OptionError
from .Collectopaedia import COLLECTOPAEDIA_REQUIREMENTS, COLLECTOPAEDIA_LOCATIONS, PAGE_REQUIREMENTS
from .Rules import canAccessMemorySpace, canAccessRegion, questPaolaAndNarineReq
from .UniqueMonsters import SUPER_BOSSES, UNIQUE_MONSTERS
from .HeartToHearts import HEART_TO_HEARTS

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat, remove_specific_item

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

def before_generate_early(world: World, multiworld: MultiWorld, player: int) -> None:
    """
    This is the earliest hook called during generation, before anything else is done.
    Use it to check or modify incompatible options, or to set up variables for later use.
    """
    if world.options.Collectopaedia == False and world.options.collectopaediasanity == True:
        raise OptionError(
            "When Collectopaediasanity is set to True, Collectopaedia must also be set to True"
        )

    if world.options.Collectopaedia == False and get_option_value(multiworld, player, "goal") == "Collector Goal":
        raise OptionError(
            "When Collector Goal is the selected goal, Collectopaedia must be set to True"
        )

    pass

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove: list[str] = [] # List of location names

    # Add your code here to calculate which locations to remove

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
# Valid item_config key/values:
# {"Item Name": 5} <- This will create qty 5 items using all the default settings
# {"Item Name": {"useful": 7}} <- This will create qty 7 items and force them to be classified as useful
# {"Item Name": {"progression": 2, "useful": 1}} <- This will create 3 items, with 2 classified as progression and 1 as useful
# {"Item Name": {0b0110: 5}} <- If you know the special flag for the item classes, you can also define non-standard options. This setup
#       will create 5 items that are the "useful trap" class
# {"Item Name": {ItemClassification.useful: 5}} <- You can also use the classification directly
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove: list[str] = [] # List of item names

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        remove_specific_item(item_pool, item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # remove_specific_item(item_pool, item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

CollectopaediaCache = []

def getCollectopaediaValue(world: World, state: CollectionState, player: int, catName: str):
    cacheKey = f"{player}-{catName}"

    if cacheKey in CollectopaediaCache:
        return True

    val = state.has_all(world.item_name_groups[catName], player)

    if val:
        CollectopaediaCache.append(cacheKey)
    return val

def getColVal(state: CollectionState, area: str, cat: str, player: int):
    if (cat == "ALL"):
        for item in ["Vegetable", "Flower", "Fruit", "Animal", "Bug", "Nature", "Part", "Strange"]:
            if state.count(f"Progressive {item} Category", player) < COLLECTOPAEDIA_REQUIREMENTS[area][item]:
                return False
        return True
    else:
        return state.count(f"Progressive {cat} Category", player) >= COLLECTOPAEDIA_REQUIREMENTS[area][cat]

def playerHasPage(state: CollectionState, player: int, area: str, cat: str) -> bool:
    cacheKey = f"{player}-{area}-{cat}"
    if cacheKey in CollectopaediaCache:
        return True

    val = playerHasItems(state, player, PAGE_REQUIREMENTS.get(f"{area}|{cat}", []))
    if val:
        CollectopaediaCache.append(cacheKey)
    return val

def playerHasItems(state: CollectionState, player: int, items: list[str]) -> bool:
    for item in items:
        if not state.has(item, player):
            return False
    return True

def setRegionRules(world: World, multiworld: MultiWorld, player: int):
    for region in [
        "Tephra Cave",
        "Bionis' Leg",
        "Colony 6",
        "Ether Mine",
        "Satorl Marsh",
        "Bionis' Interior (1st Visit)",
        "Makna Forest",
        "Frontier Village",
        "Eryth Sea",
        "Alcamoth",
        "High Entia Tomb",
    ]:
        multiworld.get_region(region, player).access_rule = lambda state, region=region: canAccessRegion(state, player, region, 1, 0)

    region = "Sword Valley (MISSABLE)"
    multiworld.get_region(region, player).access_rule = lambda state, region=region: canAccessRegion(state, player, region, 2, 10)

    for region in [
        "Prison Island (1st Visit)",
        "Valak Mountain",
        "Galahad Fortress (MISSABLE)",
        "Fallen Arm",
        "Mechonis Field (MISSABLE)",
        "Central Factory (MISSABLE)",
    ]:
        multiworld.get_region(region, player).access_rule = lambda state, region=region: canAccessRegion(state, player, region, 2, 0)
    for region in [
        "Agniratha (MISSABLE)",
        "Mechonis Core",
        "Bionis' Interior (2nd Visit)",
        "Prison Island (2nd Visit)"
    ]:
        multiworld.get_region(region, player).access_rule = lambda state, region=region: canAccessRegion(state, player, region, 3, 0)

    multiworld.get_region("Memory Space", player).access_rule = lambda state: canAccessMemorySpace(state, player)


def setUniqueMonsterRules(world: World, multiworld: MultiWorld, player: int):
    for UM in UNIQUE_MONSTERS:
        multiworld.get_location(UM["Name"], player).access_rule = lambda state, licenses=UM["Licenses"]: state.has("Progressive Hunting License", player, licenses)

def setSuperBossRules(world: World, multiworld: MultiWorld, player: int):
    for SB in SUPER_BOSSES:
        multiworld.get_location(SB["Name"], player).access_rule = lambda state, licenses=SB["Licenses"]: state.has("Progressive Hunting License", player, licenses)

def canAccessH2H(state: CollectionState, player: int, H2H: dict) -> bool:
    if (H2H["Name"] == "The Colony Reborn"):
        if not state.has("Colony 6 Reconstruction Special Level", player, 5):
            return False

    for char in ["Shulk", "Reyn", "Fiora", "Sharla", "Dunban", "Melia", "Riki"]:
        if (H2H.get(char) is not None and not state.has(f"{char} Progressive Affinity Rank", player, H2H[char])):
            return False

    return True

def setHeartToHeartRules(world: World, multiworld: MultiWorld, player: int):
    for H2H in HEART_TO_HEARTS:
        multiworld.get_location(H2H["Name"], player).access_rule = lambda state, H2H=H2H: canAccessH2H(state, player, H2H)

def setAffinityQuestRules(world: World, multiworld: MultiWorld, player: int):
    QUESTS = [
        { "Name": "The Plan - Execution", "Licenses": 1 },
        { "Name": "The Blood of Bafalgar", "Licenses": 2 },
        { "Name": "The Path of Bafalgar", "Licenses": 2 },
        { "Name": "The Coffin of Bafalgar", "Licenses": 2 },
        { "Name": "The Gratitude of Bafalgar", "Licenses": 2 },
        { "Name": "Battling Brutes", "Licenses": 2 },
        { "Name": "Zazadan in Danger", "Licenses": 6 },
        { "Name": "Zazadan Still in Danger", "Licenses": 6 },
    ]

    for quest in QUESTS:
        multiworld.get_location(quest["Name"], player).access_rule = lambda state, licenses=quest["Licenses"]: state.has("Progressive Hunting License", player, licenses)

    multiworld.get_location("Paola and Narine", player).access_rule = lambda state: (questPaolaAndNarineReq())

    multiworld.get_location("The Gem Man's Invention", player).access_rule = lambda state: (
        state.has("Colony 6 Reconstruction Housing Level", player, 1)
        and state.has("Colony 6 Reconstruction Commerce Level", player, 1)
        and state.has("Colony 6 Reconstruction Nature Level", player, 1)
        and state.has("Colony 6 Reconstruction Special Level", player, 1)
    )

    multiworld.get_location("Nic's Training", player).access_rule = lambda state: (state.has("Colony 6 Reconstruction Housing Level", player, 5))
    multiworld.get_location("Nic's Final Test", player).access_rule = lambda state: (state.has("Colony 6 Reconstruction Housing Level", player, 5))

def setChallengeQuestRules(world: World, multiworld: MultiWorld, player: int):
    QUESTS = [
        { "Name": "Challenge 1 (Colony 9)", "Licenses": 1 },
        { "Name": "Challenge 2 (Colony 9)", "Licenses": 1 },
        { "Name": "Challenge 3 (Colony 9)", "Licenses": 1 },
        { "Name": "Challenge 1 - Part 1 (Bionis' Leg) (MISSABLE)", "Licenses": 3 },
        { "Name": "Challenge 1 - Part 2 (Bionis' Leg) (MISSABLE)", "Licenses": 3 },
        { "Name": "Challenge 2 - Part 1 (Bionis' Leg) (MISSABLE)", "Licenses": 3 },
        { "Name": "Challenge 2 - Part 2 (Bionis' Leg) (MISSABLE)", "Licenses": 3 },
        { "Name": "Challenge (Satorl Marsh)", "Licenses": 6 },
        { "Name": "Challenge (Makna Forest)", "Licenses": 7 },
        { "Name": "Challenge 1 (Frontier Village)", "Licenses": 7 },
        { "Name": "Challenge 2 (Frontier Village)", "Licenses": 7 },
        { "Name": "Challenge 3 (Frontier Village)", "Licenses": 7 },
        { "Name": "Challenge (Eryth Sea)", "Licenses": 8 },
        { "Name": "Challenge 1 (Alcamoth) (MISSABLE)", "Licenses": 8 },
        { "Name": "Challenge 2 (Alcamoth) (MISSABLE)", "Licenses": 8 },
        { "Name": "Challenge 3 (Alcamoth) (MISSABLE)", "Licenses": 8 },
        { "Name": "Challenge 4 (Alcamoth) (MISSABLE)", "Licenses": 8 },
        { "Name": "Military Status 1 - 1", "Licenses": 16 },
        { "Name": "Military Status 1 - 2", "Licenses": 16 },
        { "Name": "Military Status 2 - 1", "Licenses": 16 },
        { "Name": "Military Status 2 - 2", "Licenses": 16 },
    ]

    for quest in QUESTS:
        multiworld.get_location(quest["Name"], player).access_rule = lambda state, licenses=quest["Licenses"]: state.has("Progressive Hunting License", player, licenses)

    pass

def setAchievementRules(world: World, multiworld: MultiWorld, player: int):
    multiworld.get_location("Hunter-in-Training", player).access_rule = lambda state: state.has("Progressive Hunting License", player, 1)
    multiworld.get_location("Pro Hunter", player).access_rule = lambda state: state.has("Progressive Hunting License", player, 2)
    multiworld.get_location("Master Hunter", player).access_rule = lambda state: state.has("Progressive Hunting License", player, 16)
    multiworld.get_location("Good and Fixed", player).access_rule = lambda state: (
        state.has("Colony 6 Reconstruction Housing Level", player, 5)
        and state.has("Colony 6 Reconstruction Commerce Level", player, 5)
        and state.has("Colony 6 Reconstruction Nature Level", player, 5)
        and state.has("Colony 6 Reconstruction Special Level", player, 5)
    )

    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location
    CollectopaediaCache.clear()

    CollectopaediaEnabled = is_option_enabled(multiworld, player, "Collectopaedia")
    Goal = get_option_value(multiworld, player, "goal")

    setRegionRules(world, multiworld, player)

    if is_option_enabled(multiworld, player, "UniqueMonsters"):
        setUniqueMonsterRules(world, multiworld, player)

    if is_option_enabled(multiworld, player, "SuperBosses"):
        setSuperBossRules(world, multiworld, player)

    if is_option_enabled(multiworld, player, "HeartToHearts"):
        setHeartToHeartRules(world, multiworld, player)

    if is_option_enabled(multiworld, player, "AffinityQuests"):
        setAffinityQuestRules(world, multiworld, player)

    if is_option_enabled(multiworld, player, "ChallengeQuests"):
        setChallengeQuestRules(world, multiworld, player)

    if is_option_enabled(multiworld, player, "Achievements"):
        setAchievementRules(world, multiworld, player)

    multiworld.get_location("Disciple Dickson", player).access_rule = lambda state: (state.has("Memory Fragment", player, 20))

    match Goal:
        case "Sightseer":
            multiworld.get_location("Sightseer", player).access_rule = lambda state: (state.has("Memory Fragment", player, 20))
        case "Monster Hunter Goal":
            multiworld.get_location("Monster Hunter Goal", player).access_rule = lambda state: (state.has("Progressive Hunting License", player, 18))
        case "Super Monster Hunter Goal":
            multiworld.get_location("Super Monster Hunter Goal", player).access_rule = lambda state: (state.has("Progressive Hunting License", player, 18))
        case "Collector Goal":
            if is_option_enabled(multiworld, player, "collectopaediasanity"):
                multiworld.get_location("Collector Goal", player).access_rule = lambda state: (state.has_all(world.item_name_groups["Collectopaediasanity"], player))
            else:
                multiworld.get_location("Collector Goal", player).access_rule = lambda state: (state.has_all(world.item_name_groups["Collectopaedia Pages"], player))

    if CollectopaediaEnabled:
        if is_option_enabled(multiworld, player, "collectopaediasanity"):
            for loc in COLLECTOPAEDIA_LOCATIONS:
                location = multiworld.get_location(loc["name"], player)
                area = loc["area"]
                cat = loc["cat"]
                if cat == "ALL":
                    location.access_rule = lambda state, area=area: (getCollectopaediaValue(world, state, player, f"{area} Collectopaedia"))
                else:
                    location.access_rule = lambda state: (playerHasPage(state, player, area, cat))
        else:
            for loc in COLLECTOPAEDIA_LOCATIONS:
                location = multiworld.get_location(loc["name"], player)
                area = loc["area"]
                cat = loc["cat"]
                location.access_rule = lambda state, area=area, cat=cat: (getColVal(state, area, cat, player))

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you add to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] += 1
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you undo the addition to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] -= 1
    pass


# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:

    ### Example way to use this hook:
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string

    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass

def hook_interpret_slot_data(world: World, player: int, slot_data: dict[str, Any]) -> dict[str, Any]:
    """
        Called when Universal Tracker wants to perform a fake generation
        Use this if you want to use or modify the slot_data for passed into re_gen_passthrough
    """
    return slot_data
