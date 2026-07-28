from typing import Any

from ..Helpers import is_option_enabled
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

RACE_REQUIREMENTS = [
    {"Name": "NGP - Caterpile Circuit - Win with Shulk",        "Story": "Ether Mine"                   },
    {"Name": "NGP - Caterpile Circuit - Win with Reyn",         "Story": "Ether Mine"                   },
    {"Name": "NGP - Caterpile Circuit - Win with Sharla",       "Story": "Ether Mine"                   },
    {"Name": "NGP - Caterpile Circuit - Win with Dunban",       "Story": "Ether Mine"                   },
    {"Name": "NGP - Caterpile Circuit - Win with Riki",         "Story": "Frontier Village"             },
    {"Name": "NGP - Caterpile Circuit - Win with Melia",        "Story": "High Entia Tomb"              },
    {"Name": "NGP - Caterpile Circuit - Win with Fiora",        "Story": "Fallen Arm"                   },
    {"Name": "NGP - Twilight Speedway - Win with Shulk",        "Story": "Ether Mine"                   },
    {"Name": "NGP - Twilight Speedway - Win with Reyn",         "Story": "Ether Mine"                   },
    {"Name": "NGP - Twilight Speedway - Win with Sharla",       "Story": "Ether Mine"                   },
    {"Name": "NGP - Twilight Speedway - Win with Dunban",       "Story": "Ether Mine"                   },
    {"Name": "NGP - Twilight Speedway - Win with Riki",         "Story": "Frontier Village"             },
    {"Name": "NGP - Twilight Speedway - Win with Melia",        "Story": "High Entia Tomb"              },
    {"Name": "NGP - Twilight Speedway - Win with Fiora",        "Story": "Fallen Arm"                   },
    {"Name": "NGP - Jungle Rumble - Win with Shulk",            "Story": "Eryth Sea"                    },
    {"Name": "NGP - Jungle Rumble - Win with Reyn",             "Story": "Eryth Sea"                    },
    {"Name": "NGP - Jungle Rumble - Win with Sharla",           "Story": "Eryth Sea"                    },
    {"Name": "NGP - Jungle Rumble - Win with Dunban",           "Story": "Eryth Sea"                    },
    {"Name": "NGP - Jungle Rumble - Win with Riki",             "Story": "Eryth Sea"                    },
    {"Name": "NGP - Jungle Rumble - Win with Melia",            "Story": "High Entia Tomb"              },
    {"Name": "NGP - Jungle Rumble - Win with Fiora",            "Story": "Fallen Arm"                   },
    {"Name": "NGP - Midnight Forest - Win with Shulk",          "Story": "Eryth Sea"                    },
    {"Name": "NGP - Midnight Forest - Win with Reyn",           "Story": "Eryth Sea"                    },
    {"Name": "NGP - Midnight Forest - Win with Sharla",         "Story": "Eryth Sea"                    },
    {"Name": "NGP - Midnight Forest - Win with Dunban",         "Story": "Eryth Sea"                    },
    {"Name": "NGP - Midnight Forest - Win with Riki",           "Story": "Eryth Sea"                    },
    {"Name": "NGP - Midnight Forest - Win with Melia",          "Story": "High Entia Tomb"              },
    {"Name": "NGP - Midnight Forest - Win with Fiora",          "Story": "Fallen Arm"                   },
    {"Name": "NGP - Alcamoth at Dawn - Win with Shulk",         "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth at Dawn - Win with Reyn",          "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth at Dawn - Win with Sharla",        "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth at Dawn - Win with Dunban",        "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth at Dawn - Win with Riki",          "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth at Dawn - Win with Melia",         "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth at Dawn - Win with Fiora",         "Story": "Fallen Arm"                   },
    {"Name": "NGP - Alcamoth Orbital - Win with Shulk",         "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth Orbital - Win with Reyn",          "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth Orbital - Win with Sharla",        "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth Orbital - Win with Dunban",        "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth Orbital - Win with Riki",          "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth Orbital - Win with Melia",         "Story": "Prison Island (1st Visit)"    },
    {"Name": "NGP - Alcamoth Orbital - Win with Fiora",         "Story": "Fallen Arm"                   },
    {"Name": "NGP - Blizzard Rally - Win with Shulk",           "Story": "Valak Mountain"               },
    {"Name": "NGP - Blizzard Rally - Win with Reyn",            "Story": "Valak Mountain"               },
    {"Name": "NGP - Blizzard Rally - Win with Sharla",          "Story": "Valak Mountain"               },
    {"Name": "NGP - Blizzard Rally - Win with Dunban",          "Story": "Valak Mountain"               },
    {"Name": "NGP - Blizzard Rally - Win with Riki",            "Story": "Valak Mountain"               },
    {"Name": "NGP - Blizzard Rally - Win with Melia",           "Story": "Valak Mountain"               },
    {"Name": "NGP - Blizzard Rally - Win with Fiora",           "Story": "Fallen Arm"                   },
    {"Name": "NGP - Valak Slalom - Win with Shulk",             "Story": "Valak Mountain"               },
    {"Name": "NGP - Valak Slalom - Win with Reyn",              "Story": "Valak Mountain"               },
    {"Name": "NGP - Valak Slalom - Win with Sharla",            "Story": "Valak Mountain"               },
    {"Name": "NGP - Valak Slalom - Win with Dunban",            "Story": "Valak Mountain"               },
    {"Name": "NGP - Valak Slalom - Win with Riki",              "Story": "Valak Mountain"               },
    {"Name": "NGP - Valak Slalom - Win with Melia",             "Story": "Valak Mountain"               },
    {"Name": "NGP - Valak Slalom - Win with Fiora",             "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Shulk",       "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Reyn",        "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Sharla",      "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Dunban",      "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Riki",        "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Melia",       "Story": "Fallen Arm"                   },
    {"Name": "NGP - Colony 9 Wild Ride - Win with Fiora",       "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Shulk",               "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Reyn",                "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Sharla",              "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Dunban",              "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Riki",                "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Melia",               "Story": "Fallen Arm"                   },
    {"Name": "NGP - Rural Road - Win with Fiora",               "Story": "Fallen Arm"                   }
]

def canAccessRace(state: CollectionState, player: int, race: dict, postgame: bool) -> bool:
    if not state.has("Ether Jet", player, 1):
        return False

    if not postgame and not state.has(f"{race['Story']} Access", player, 1):
        return False

    return True

def setNoponGrandPrixRules(world: World, multiworld: MultiWorld, player: int, spoilers: bool):
    postgame = is_option_enabled(multiworld, player, "Post_Game")

    for race in RACE_REQUIREMENTS:
        name = race["Name"]
        if not spoilers:
            name = name.replace("Fiora", "Seven")

        multiworld.get_location(name, player).access_rule = lambda state, player=player, race=race, postgame=postgame: canAccessRace(state, player, race, postgame)