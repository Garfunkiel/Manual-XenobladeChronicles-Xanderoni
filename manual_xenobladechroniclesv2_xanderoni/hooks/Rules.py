from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, is_option_enabled
from BaseClasses import MultiWorld, CollectionState

import re

CollectopaediaRequirements = {
    "Colony 9":         { "Vegetable": 1,  "Flower": 1,  "Fruit": 1,  "Animal": 0,  "Bug": 1,  "Nature": 0,  "Part": 1,  "Strange": 1 },
    "Tephra Cave":      { "Vegetable": 0,  "Flower": 2,  "Fruit": 2,  "Animal": 1,  "Bug": 2,  "Nature": 1,  "Part": 0,  "Strange": 2 },
    "Bionis' Leg":      { "Vegetable": 2,  "Flower": 0,  "Fruit": 3,  "Animal": 0,  "Bug": 3,  "Nature": 2,  "Part": 2,  "Strange": 3 },
    "Colony 6":         { "Vegetable": 0,  "Flower": 3,  "Fruit": 0,  "Animal": 2,  "Bug": 0,  "Nature": 0,  "Part": 0,  "Strange": 4 },
    "Ether Mine":       { "Vegetable": 0,  "Flower": 0,  "Fruit": 0,  "Animal": 3,  "Bug": 4,  "Nature": 3,  "Part": 3,  "Strange": 5 },
    "Satorl Marsh":     { "Vegetable": 3,  "Flower": 4,  "Fruit": 0,  "Animal": 4,  "Bug": 0,  "Nature": 4,  "Part": 4,  "Strange": 6 },
    "Bionis' Interior": { "Vegetable": 4,  "Flower": 0,  "Fruit": 0,  "Animal": 5,  "Bug": 0,  "Nature": 0,  "Part": 0,  "Strange": 7 },
    "Makna Forest":     { "Vegetable": 5,  "Flower": 5,  "Fruit": 4,  "Animal": 6,  "Bug": 5,  "Nature": 0,  "Part": 0,  "Strange": 8 },
    "Frontier Village": { "Vegetable": 0,  "Flower": 0,  "Fruit": 5,  "Animal": 0,  "Bug": 6,  "Nature": 0,  "Part": 0,  "Strange": 9 },
    "Eryth Sea":        { "Vegetable": 6,  "Flower": 6,  "Fruit": 0,  "Animal": 7,  "Bug": 0,  "Nature": 5,  "Part": 0,  "Strange": 10 },
    "Alcamoth":         { "Vegetable": 0,  "Flower": 7,  "Fruit": 6,  "Animal": 0,  "Bug": 0,  "Nature": 0,  "Part": 0,  "Strange": 11 },
    "High Entia Tomb":  { "Vegetable": 0,  "Flower": 0,  "Fruit": 0,  "Animal": 0,  "Bug": 7,  "Nature": 0,  "Part": 5,  "Strange": 12 },
    "Valak Mountain":   { "Vegetable": 7,  "Flower": 8,  "Fruit": 7,  "Animal": 8,  "Bug": 0,  "Nature": 6,  "Part": 0,  "Strange": 13 },
    "Sword Valley":     { "Vegetable": 8,  "Flower": 9,  "Fruit": 8,  "Animal": 0,  "Bug": 0,  "Nature": 0,  "Part": 6,  "Strange": 14 },
    "Galahad Fortress": { "Vegetable": 0,  "Flower": 0,  "Fruit": 0,  "Animal": 0,  "Bug": 8,  "Nature": 0,  "Part": 7,  "Strange": 15 },
    "Fallen Arm":       { "Vegetable": 9,  "Flower": 0,  "Fruit": 9,  "Animal": 9,  "Bug": 0,  "Nature": 7,  "Part": 8,  "Strange": 16 },
    "Mechonis Field":   { "Vegetable": 10, "Flower": 10, "Fruit": 0,  "Animal": 0,  "Bug": 9,  "Nature": 8,  "Part": 9,  "Strange": 17 },
    "Central Factory":  { "Vegetable": 11, "Flower": 0,  "Fruit": 0,  "Animal": 10, "Bug": 10, "Nature": 9,  "Part": 10, "Strange": 18 },
    "Agniratha":        { "Vegetable": 0,  "Flower": 11, "Fruit": 10, "Animal": 0,  "Bug": 11, "Nature": 10, "Part": 11, "Strange": 19 },
    "Prison Island":    { "Vegetable": 0,  "Flower": 0,  "Fruit": 11, "Animal": 11, "Bug": 12, "Nature": 11, "Part": 12, "Strange": 20 },
    "Other":            { "Vegetable": 0,  "Flower": 0,  "Fruit": 0,  "Animal": 0,  "Bug": 13, "Nature": 0,  "Part": 13, "Strange": 21 },
}

def getCollectopaediaValue(world: World, state: CollectionState, player: int, catName: str, cacheKey: str):
    val = state.has_all(world.item_name_groups[catName], player)
    return val

def collectopaediaComplete(world: World, multiworld: MultiWorld, state: CollectionState, player: int, area: str, cat: str):
    if (is_option_enabled(multiworld, player, "collectopaediasanity")):
        cacheKey = f"{str(player)}_{area}_{cat}"

        if (cat == "ALL"):
            return getCollectopaediaValue(world, state, player, f"{area} Collectopaedia", cacheKey)
        else:
            return getCollectopaediaValue(world, state, player, f"{area} Collection ({cat})", cacheKey)
    else:
        if (cat == "ALL"):
            for item in ["Vegetable", "Flower", "Fruit", "Animal", "Bug", "Nature", "Part", "Strange"]:
                if state.count(f"Progressive {item} Category", player) < CollectopaediaRequirements[area][item]:
                    return False
            return True
        else:
            return state.count(f"Progressive {cat} Category", player) >= CollectopaediaRequirements[area][cat]

def questPaolaAndNarineReq():
    return "|Shulk Progressive Affinity Rank:4| AND |Reyn Progressive Affinity Rank:4|" \
                " AND ((|Sharla Progressive Affinity Rank:4| AND |Melia Progressive Affinity Rank:4|) " \
                " OR (|Sharla Progressive Affinity Rank:4| AND |Fiora Progressive Affinity Rank:4|)" \
                " OR (|Melia Progressive Affinity Rank:4| AND |Fiora Progressive Affinity Rank:4|))"
