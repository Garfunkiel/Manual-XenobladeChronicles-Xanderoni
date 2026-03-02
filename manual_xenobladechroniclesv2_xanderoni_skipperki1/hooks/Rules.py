from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, is_option_enabled
from BaseClasses import MultiWorld, CollectionState
from functools import cache

import re

@cache
def questPaolaAndNarineReq() -> str:
    return "|Shulk Progressive Affinity Rank:4| AND |Reyn Progressive Affinity Rank:4|" \
                " AND ((|Sharla Progressive Affinity Rank:4| AND |Melia Progressive Affinity Rank:4|) " \
                " OR (|Sharla Progressive Affinity Rank:4| AND |Fiora Progressive Affinity Rank:4|)" \
                " OR (|Melia Progressive Affinity Rank:4| AND |Fiora Progressive Affinity Rank:4|))"

def canAccessRegion(state: CollectionState, player: int, region: str, keysRequired: int, licensesRequired: int) -> bool:
    return state.has(region + " Key", player, keysRequired) and state.has("Progressive Hunting License", player, licensesRequired)

def canAccessMemorySpace(state: CollectionState, player: int) -> bool:
    return state.has("Memory Fragment", player, 20)