from typing import Optional, Any
from BaseClasses import MultiWorld


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Helpers import get_option_value
    if category_name == "DefinitiveEdition":
        return get_option_value(multiworld, player, "GameVersion") >= 1
    if category_name == "Switch2Version":
        return get_option_value(multiworld, player, "GameVersion") == 2

    if category_name in get_main_game_only_categories():
        return get_option_value(multiworld, player, "GameOrder") != 2
    if category_name.startswith("Future Connected"):
        return get_option_value(multiworld, player, "GameOrder") >= 1

    if get_option_value(multiworld, player, "Post_Game") == True:
        if category_name == "UnavailableInPostGame" or category_name in [
            "AffinityChart", "StoryQuests", "MonsterQuests", "CollectionQuests", "SearchQuests", "ChallengeQuests", "AffinityQuests", "MaterialQuests"
        ]:
            return False

    if category_name == "Collectopaedia Pages":
        return get_option_value(multiworld, player, "Collectopaedia") >= 1

    if category_name == "Collectopaedia":
        return get_option_value(multiworld, player, "Collectopaedia") >= 1

    if category_name == "Collectopaediasanity":
        return get_option_value(multiworld, player, "Collectopaedia") == 2

    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None

def get_main_game_only_categories() -> list[str]:
    return [
        "Colony 9 Landmarks",
        "Colony 9 Unique Monsters",
        "Colony 9 Bosses",
        "Colony 9 Affinity Chart",
        "Colony 9 Heart-to-Hearts",
        "Colony 9 Collectopaedia",
        "Colony 9 Development Level",
        "Colony 9 Quests",
        "Colony 9 Quests (Development Level 1)",
        "Colony 9 Quests (Development Level 2)",
        "Colony 9 Quests (Development Level 3)",
        "Colony 9 Quests (Development Level 4)",
        "Colony 9 Story Quests",
        "Colony 9 Locations",
        "Tephra Cave Landmarks",
        "Tephra Cave Unique Monsters",
        "Tephra Cave Bosses",
        "Tephra Cave Heart-to-Hearts",
        "Tephra Cave Collectopaedia",
        "Tephra Cave Quests",
        "Tephra Cave Locations",
        "Bionis' Leg Landmarks",
        "Bionis' Leg Unique Monsters",
        "Bionis' Leg Bosses",
        "Bionis' Leg/Colony 6 Affinity Chart",
        "Bionis' Leg Heart-to-Hearts",
        "Bionis' Leg Collectopaedia",
        "Bionis' Leg Quests",
        "Bionis' Leg Quests (Colony 6 Development Level 1)",
        "Bionis' Leg Quests (Colony 6 Development Level 2)",
        "Bionis' Leg Quests (Colony 6 Development Level 3)",
        "Bionis' Leg Quests (Colony 6 Development Level 4)",
        "Bionis' Leg Locations",
        "Colony 6 Landmarks",
        "Colony 6 Unique Monsters",
        "Colony 6 Bosses",
        "Colony 6 Heart-to-Hearts",
        "Colony 6 Collectopaedia",
        "Colony 6 Development Level",
        "Colony 6 Quests",
        "Colony 6 Quests (Development Level 1)",
        "Colony 6 Quests (Development Level 2)",
        "Colony 6 Quests (Development Level 3)",
        "Colony 6 Quests (Development Level 4)",
        "Colony 6 Quests (Reconstruction)",
        "Colony 6 Locations",
        "Ether Mine Landmarks",
        "Ether Mine Unique Monsters",
        "Ether Mine Bosses",
        "Ether Mine Heart-to-Hearts",
        "Ether Mine Collectopaedia",
        "Ether Mine Locations",
        "Satorl Marsh Landmarks",
        "Satorl Marsh Unique Monsters",
        "Satorl Marsh Bosses",
        "Satorl Marsh Affinity Chart",
        "Satorl Marsh Heart-to-Hearts",
        "Satorl Marsh Collectopaedia",
        "Satorl Marsh Quests",
        "Satorl Marsh Quests (Story)",
        "Satorl Marsh Locations",
        "Bionis' Interior Landmarks",
        "Bionis' Interior (1st Visit) Locations",
        "Bionis' Interior (2nd Visit) Locations",
        "Makna Forest Landmarks",
        "Makna Forest Unique Monsters",
        "Makna Forest Bosses",
        "Makna Forest Affinity Chart",
        "Makna Forest Heart-to-Hearts",
        "Makna Forest Collectopaedia",
        "Makna Forest Quests",
        "Makna Forest Quests (Story)",
        "Makna Forest Quests (Frontier Village Development Level 3)",
        "Makna Forest Locations",
        "Frontier Village Landmarks",
        "Frontier Village Affinity Chart",
        "Frontier Village Heart-to-Hearts",
        "Frontier Village Collectopaedia",
        "Frontier Village Development Level",
        "Frontier Village Quests",
        "Frontier Village Quests (Story)",
        "Frontier Village Quests (Development Level 1)",
        "Frontier Village Quests (Development Level 2)",
        "Frontier Village Quests (Development Level 3)",
        "Frontier Village Quests (Development Level 4)",
        "Frontier Village Locations",
        "Eryth Sea Landmarks",
        "Eryth Sea Unique Monsters",
        "Eryth Sea Bosses",
        "Eryth Sea Affinity Chart",
        "Eryth Sea Heart-to-Hearts",
        "Eryth Sea Collectopaedia",
        "Eryth Sea Quests",
        "Eryth Sea Quests (Story)",
        "Eryth Sea Quests (Alcamoth Development Level 2)",
        "Eryth Sea Locations",
        "Alcamoth Landmarks",
        "Alcamoth Affinity Chart",
        "Alcamoth Heart-to-Hearts",
        "Alcamoth Collectopaedia (Main Game)",
        "Alcamoth Development Level",
        "Alcamoth Quests",
        "Alcamoth Quests (Development Level 1)",
        "Alcamoth Quests (Development Level 2)",
        "Alcamoth Locations",
        "High Entia Tomb Landmarks",
        "High Entia Tomb Unique Monsters",
        "High Entia Tomb Bosses",
        "High Entia Tomb Heart-to-Hearts",
        "High Entia Tomb Collectopaedia",
        "High Entia Tomb Locations",
        "Prison Island (First Visit) Landmarks",
        "Prison Island (First Visit) Bosses",
        "Prison Island (1st Visit) Locations",
        "Prison Island (2nd Visit) Locations",
        "Valak Mountain Landmarks",
        "Valak Mountain Unique Monsters",
        "Valak Mountain Bosses",
        "Valak Mountain Affinity Chart",
        "Valak Mountain Heart-to-Hearts",
        "Valak Mountain Collectopaedia",
        "Valak Mountain Quests",
        "Valak Mountain Locations",
        "Sword Valley Landmarks",
        "Sword Valley Unique Monsters",
        "Sword Valley Bosses",
        "Sword Valley Collectopaedia",
        "Sword Valley Quests",
        "Sword Valley Locations",
        "Galahad Fortress Landmarks",
        "Galahad Fortress Unique Monsters",
        "Galahad Fortress Bosses",
        "Galahad Fortress Collectopaedia",
        "Galahad Fortress Quests",
        "Galahad Fortress Locations",
        "Fallen Arm Landmarks",
        "Fallen Arm Unique Monsters",
        "Fallen Arm Affinity Chart",
        "Fallen Arm Heart-to-Hearts",
        "Fallen Arm Collectopaedia",
        "Fallen Arm Development Level",
        "Fallen Arm Quests",
        "Fallen Arm Quests (Story)",
        "Fallen Arm Quests (Development Level 1)",
        "Fallen Arm Quests (Development Level 2)",
        "Fallen Arm Quests (Development Level 3)",
        "Fallen Arm Locations",
        "Mechonis Field Landmarks",
        "Mechonis Field Unique Monsters",
        "Mechonis Field Bosses",
        "Mechonis Field Affinity Chart",
        "Mechonis Field Collectopaedia",
        "Mechonis Field Quests",
        "Mechonis Field Quests (Story)",
        "Mechonis Field Locations",
        "Central Factory Landmarks",
        "Central Factory Unique Monsters",
        "Central Factory Bosses",
        "Central Factory Collectopaedia",
        "Central Factory Quests",
        "Central Factory Quests (Story)",
        "Central Factory Locations",
        "Agniratha Landmarks",
        "Agniratha Unique Monsters",
        "Agniratha Bosses",
        "Agniratha Collectopaedia",
        "Agniratha Quests",
        "Agniratha Quests (Story)",
        "Agniratha Locations",
        "Mechonis Core Bosses",
        "Mechonis Core Quests (Story)",
        "Mechonis Core Locations",
        "Bionis' Interior (2nd Visit) Landmarks",
        "Bionis' Interior (2nd Visit) Unique Monsters",
        "Bionis' Interior (2nd Visit) Bosses",
        "Bionis' Interior (2nd Visit) Heart-to-Hearts",
        "Bionis' Interior Collectopaedia",
        "Prison Island (2nd Visit) Landmarks",
        "Prison Island (2nd Visit) Unique Monsters",
        "Prison Island (2nd Visit) Bosses",
        "Prison Island (2nd Visit) Story Quests",
        "Prison Island Heart-to-Hearts",
        "Prison Island Collectopaedia",
        "Other Collectopaedia",
        "Memory Space Landmarks",
        "Achievements",
        "NoponGrandPrix",
        "CrystalMining",
        # ITEMS:
        "Area Keys",
        "Skill Trees",
        "Reyn Arts",
        "Fiora Arts",
        "Seven Arts",
        "Sharla Arts",
        "Dunban Arts",
        "Riki Arts",
        "Shulk Affinity",
        "Reyn Affinity",
        "Fiora Affinity",
        "Seven Affinity",
        "Sharla Affinity",
        "Dunban Affinity",
        "Melia Affinity",
        "Riki Affinity",
        "Colony 6 Reconstruction",
        "Memory Fragments",
        "Collectopaedia Pages",
        "Reyn Armor",
        "Fiora Armor",
        "Seven Armor",
        "Sharla Armor",
        "Dunban Armor",
        "Riki Armor",
        "Traps",
        "Hunting Licenses"
    ]