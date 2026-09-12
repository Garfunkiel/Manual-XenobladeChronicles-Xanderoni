# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from typing import Any
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item
from Options import OptionError
from ..Helpers import is_option_enabled, get_option_value, remove_specific_item

regions = [
        # 1 Key Each:
        "Colony 9", "Tephra Cave", "Bionis' Leg", "Colony 6", "Ether Mine", "Satorl Marsh", "Makna Forest", "Frontier Village", "Eryth Sea", "Alcamoth", "High Entia Tomb",
        # 2 Keys Each:
        "Valak Mountain", "Fallen Arm",
        # 3 Keys Each; give 1st visit keys too:
        "Bionis' Interior", "Prison Island"
]

def set_starting_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    starting_items: list[str] = [] # List of starting item names

    # 0 = Main Game Only
    # 1 = Main Game First
    # 2 = Future Connected Only
    # 3 = Future Connected First
    # 4 = Both Games Parallel
    order = get_option_value(multiworld, player, "GameOrder")

    give_base_key = (order == 0 or order == 1 or order == 4)
    give_fc_key = (order == 2 or order == 3 or order == 4)

    if give_base_key:
        if is_option_enabled(multiworld, player, "Post_Game"):
            # Give the player a random starting region from those available in Post-Game, and give them the appropriate number of keys for that region
            # Excluding Bionis' Interior (1st Visit) due to near immediate BK

            user_starting_region = get_option_value(multiworld, player, "Post_Game_Region")

            if not type(user_starting_region) is int:
                raise OptionError("Post_Game_Region must be an integer value")

            starting_region = regions[user_starting_region - 1]

            if starting_region in ["Prison Island"]:
                starting_items = [f"{starting_region} (2nd Visit) Key", f"{starting_region} (2nd Visit) Key", f"{starting_region} (2nd Visit) Key", f"{starting_region} (1st Visit) Key", f"{starting_region} (1st Visit) Key"]
            elif starting_region in ["Bionis' Interior"]:
                starting_items = [f"{starting_region} (2nd Visit) Key", f"{starting_region} (2nd Visit) Key", f"{starting_region} (2nd Visit) Key", f"{starting_region} (1st Visit) Key"]
            elif starting_region in ["Valak Mountain", "Fallen Arm"]:
                starting_items = [f"{starting_region} Key", f"{starting_region} Key"]
            else:
                starting_items = [f"{starting_region} Key"]

            for _ in range(18):
                starting_items.append("Progressive Hunting License")
        else:
            starting_items = ["Colony 9 Key"]

    if give_fc_key:
        if is_option_enabled(multiworld, player, "FC_Post_Game"):
            user_starting_region = get_option_value(multiworld, player, "FC_Post_Game_Region")

            if not type(user_starting_region) is int:
                raise OptionError("FC_Post_Game_Region must be an integer value")

            if user_starting_region == 1:
                starting_items.append("Bionis' Shoulder Key")
            elif user_starting_region == 2:
                starting_items.append("Melfica Road Key")
            elif user_starting_region == 3:
                starting_items.append("Gran Dell Key")
            elif user_starting_region == 4:
                starting_items.append("Monado EX+ Plans")
        else:
            starting_items.append("Bionis' Shoulder Key")


    for itemName in starting_items:
        item = next(i for i in item_pool if i.name == itemName)
        multiworld.push_precollected(item)
        remove_specific_item(item_pool, item)

    return item_pool