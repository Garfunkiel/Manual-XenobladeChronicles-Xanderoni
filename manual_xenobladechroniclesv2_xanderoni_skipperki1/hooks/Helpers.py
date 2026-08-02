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

    if category_name.startswith("Future Connected"):
        return get_option_value(multiworld, player, "Future_Connected") == True

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
