from typing import Any

from ..Helpers import is_option_enabled
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item


MINING_SPOTS = [
    # Tephra Cave
    { "Name": "Ether Crystal Deposit - Spring of Grief",                                    "Pickaxe": "Tephra Ice Ether Pickaxe"       },
    { "Name": "Ether Crystal Deposit - Vilia Lake NE",                                      "Pickaxe": "Tephra Earth Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Vilia Lake S",                                       "Pickaxe": "Tephra Water Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Forgotten Cave",                     "Story": "MC",  "Pickaxe": "Tephra Earth Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - North-West 2F",                      "Story": "MC",  "Pickaxe": "Tephra Fire Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Heavenly Window",                    "Story": "MC",  "Pickaxe": "Tephra Fire Ether Pickaxe"      },
    # Bionis' Leg
    { "Name": "Ether Crystal Deposit - Jabos Rock Rest Area",                               "Pickaxe": "Leg Wind Ether Pickaxe"         },
    { "Name": "Ether Crystal Deposit - Volff Lair",                                         "Pickaxe": "Leg Electric Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Kisk Cave",                                          "Pickaxe": "Leg Electric Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Tranquil Grotto",                                    "Pickaxe": "Leg Water Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Daksha Shrine",                                      "Pickaxe": "Leg Wind Ether Pickaxe"         },
    { "Name": "Ether Crystal Deposit - Windy Cave",                                         "Pickaxe": "Leg Electric Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Viliera Hill",                                       "Pickaxe": "Leg Wind Ether Pickaxe"         },
    { "Name": "Ether Crystal Deposit - Traveller's Rest",                                   "Pickaxe": "Leg Water Ether Pickaxe"        },
    # Colony 6
    { "Name": "Ether Crystal Deposit - Drainage Outlet",                                    "Pickaxe": "Colony Wind Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Southern Entrance",                  "Story": "EM",  "Pickaxe": "Colony Water Ether Pickaxe"     },
    # Ether Mine
    { "Name": "Ether Crystal Deposit - Drainage Control Room",                              "Pickaxe": "Mine Earth Ether Pickaxe"       },
    { "Name": "Ether Crystal Deposit - Test Pit 3",                                         "Pickaxe": "Mine Wind Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Test Pit 2",                                         "Pickaxe": "Mine Fire Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Glowmoss Lake",                                      "Pickaxe": "Mine Water Ether Pickaxe"       },
    { "Name": "Ether Crystal Deposit - Central Terminal",                                   "Pickaxe": "Mine Electric Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - Test Pit 4",                                         "Pickaxe": "Mine Ice Ether Pickaxe"         },
    { "Name": "Ether Crystal Deposit - Personnel Lift 2 (MISSABLE)",                        "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Central Pit - Entrance (MISSABLE)",                  "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - North-East B1F (MISSABLE)",                          "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - North B1F (MISSABLE)",                               "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Regulation Piston (MISSABLE)",                       "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - East B2F (MISSABLE)",                                "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - North B2F (MISSABLE)",                               "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - North-West B2F (MISSABLE)",                          "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - West B2F (MISSABLE)",                                "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Personnel Lift 3 (MISSABLE)",                        "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - North B3F (MISSABLE)",                               "Pickaxe": "Ephemeral Ether Pickaxe"        },
    # Satorl Marsh
    { "Name": "Ether Crystal Deposit - Nopon Merchant Camp",                                "Pickaxe": "Marsh Electric Ether Pickaxe"   },
    { "Name": "Ether Crystal Deposit - Poison Swamp",                                       "Pickaxe": "Marsh Earth Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Soter Ruins",                                        "Pickaxe": "Marsh Water Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Zaldania Waterfall",                                 "Pickaxe": "Marsh Water Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Dark Swamp",                                         "Pickaxe": "Marsh Earth Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Sororal Statues",                                    "Pickaxe": "Marsh Electric Ether Pickaxe"   },
    # Makna Forest
    { "Name": "Ether Crystal Deposit - Lakeside",                                           "Pickaxe": "Forest Water Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Divine Sanctuary",                                   "Pickaxe": "Forest Wind Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Sap Cave",                                           "Pickaxe": "Forest Electric Ether Pickaxe"  },
    { "Name": "Ether Crystal Deposit - Bridge Two",                                         "Pickaxe": "Forest Earth Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Glowmoss Trihenge",                                  "Pickaxe": "Forest Wind Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Abyss Basin",                                        "Pickaxe": "Forest Fire Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Pod Landing Site",                                   "Pickaxe": "Forest Fire Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Decayed Forest",                                     "Pickaxe": "Forest Fire Ether Pickaxe"      },
    { "Name": "Ether Crystal Deposit - Eks Watering Hole",                                  "Pickaxe": "Forest Earth Ether Pickaxe"     },
    # Eryth Sea
    { "Name": "Ether Crystal Deposit - Showdown Cliff",                                     "Pickaxe": "Sea Wind Ether Pickaxe"         },
    { "Name": "Ether Crystal Deposit - Anu Shore",                                          "Pickaxe": "Sea Electric Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Secluded Island",                                    "Pickaxe": "Sea Water Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Sleeping Dragon Isle",                               "Pickaxe": "Sea Water Ether Pickaxe"        },
    { "Name": "Ether Crystal Deposit - Hovering Reef 7",                    "Story": "AL",  "Pickaxe": "Sea Wind Ether Pickaxe"         },
    { "Name": "Ether Crystal Deposit - Hovering Reef 10",                   "Story": "AL",  "Pickaxe": "Sea Electric Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Ether Crystal Deposit",                              "Pickaxe": "Sea Electric Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Below Hovering Reef 9",                              "Pickaxe": "Sea Wind Ether Pickaxe"         },
    # Valak Mountain
    { "Name": "Ether Crystal Deposit - Serik Waterfall",                                    "Pickaxe": "Mountain Water Ether Pickaxe"   },
    { "Name": "Ether Crystal Deposit - Kana Peak",                                          "Pickaxe": "Mountain Wind Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - Nagul Waterfall",                                    "Pickaxe": "Mountain Ice Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Nopon Camp",                                         "Pickaxe": "Mountain Wind Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - West Lava Cave",                                     "Pickaxe": "Mountain Fire Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - East Lava Cave",                                     "Pickaxe": "Mountain Fire Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - Harict Chapel",                                      "Pickaxe": "Mountain Water Ether Pickaxe"   },
    { "Name": "Ether Crystal Deposit - Ignia Hill",                                         "Pickaxe": "Mountain Ice Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Bionis' Right Elbow",                                "Pickaxe": "Mountain Water Ether Pickaxe"   },
    { "Name": "Ether Crystal Deposit - Great Glacier",                                      "Pickaxe": "Mountain Ice Ether Pickaxe"     },
    # Sword Valley
    { "Name": "Ether Gear - Supply Convoy",                                                 "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ged Fortress",                                                  "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Dolgan Outpost",                                                "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - 5th Gate",                                                      "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Storage Area",                                            "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Enalda Control Base",                                           "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Port Maintenance Bay",                                          "Pickaxe": "Ephemeral Ether Pickaxe"        },
    # Galahad Fortress
    { "Name": "Ether Gear - Main Maintenance Bay",                                          "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - 1st Turbine Room",                                              "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Blast Furnace - South-West",                              "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Blast Furnace - South-East",                              "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Blast Furnace - North-East",                              "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Blast Furnace - North-West",                              "Pickaxe": "Ephemeral Ether Pickaxe"        },
    # Fallen Arm
    { "Name": "Ether Gear - Silver Wreckage",                                               "Pickaxe": "Fallen Earth Ether Pickaxe"     },
    { "Name": "Ether Gear - Power Pipe Ruins",                                              "Pickaxe": "Fallen Ice Ether Pickaxe"       },
    { "Name": "Ether Gear - 5th Pulse Zone",                                                "Pickaxe": "Fallen Earth Ether Pickaxe"     },
    { "Name": "Ether Gear - Giant Mechon Debris",                                           "Pickaxe": "Fallen Ice Ether Pickaxe"       },
    { "Name": "Ether Gear - Ether Exhaust System",                                          "Pickaxe": "Fallen Earth Ether Pickaxe"     },
    { "Name": "Ether Gear - Digit 2",                                                       "Pickaxe": "Fallen Ice Ether Pickaxe"       },
    # Mechonis Field
    { "Name": "Ether Gear - 1st Lift - GF",                                                 "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - 2nd Lift - 1F",                                                 "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Bulkhead Controls",                                             "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Gear Store - Fire",                                       "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Ether Gear Store - Earth",                                      "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Machina Refuge",                                                "Pickaxe": "Ephemeral Ether Pickaxe"        },
    # Central Factory
    { "Name": "Ether Gear - 1F - South",                                                    "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Control Tower",                                                 "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Storage Depot",                                                 "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - 1F - West",                                                     "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Tower Boarding Gate - Water",                                   "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Tower Boarding Gate - Earth",                                   "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Regeneration Control",                                          "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Face Maintenance Bay",                                          "Pickaxe": "Ephemeral Ether Pickaxe"        },
    # Agniratha
    { "Name": "Ether Gear - Central Tower",                                                 "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Seven Sage Cloister",                                           "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Helas Pillar",                                                  "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - East Central",                                                  "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Cleas Pillar",                                                  "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Telethia Bridge",                                               "Pickaxe": "Ephemeral Ether Pickaxe"        },
    { "Name": "Ether Gear - Judicial District",                                             "Pickaxe": "Ephemeral Ether Pickaxe"        },
    # Bionis' Interior
    { "Name": "Ether Crystal Deposit - First Lung",                                         "Pickaxe": "Interior Water Ether Pickaxe"   },
    { "Name": "Ether Crystal Deposit - Second Lung - North",                                "Pickaxe": "Interior Electric Ether Pickaxe"},
    { "Name": "Ether Crystal Deposit - Second Lung - East",                                 "Pickaxe": "Interior Fire Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - Terminal Nerve Tower",                               "Pickaxe": "Interior Ice Ether Pickaxe"     },
    { "Name": "Ether Crystal Deposit - Pars Sympathica Tower",                              "Pickaxe": "Interior Wind Ether Pickaxe"    },
    { "Name": "Ether Crystal Deposit - Terminal Vein",                                      "Pickaxe": "Interior Earth Ether Pickaxe"   }
]

def canMineDeposit(state: CollectionState, player: int, spot: dict, postgame: bool) -> bool:
    if not state.has(spot["Pickaxe"], player, 1):
        return False

    if not postgame:
        story = spot.get("Story", "")

        if story == "EM" and not state.has("Ether Mine Access", player, 1):
            return False
        if story == "AL" and not state.has("Alcamoth Access", player, 1):
            return False
        if story == "MC" and not state.has("Mechonis Core Access", player, 1):
            return False

    return True

def setCrystalMiningRules(world: World, multiworld: MultiWorld, player: int):
    postgame = is_option_enabled(multiworld, player, "Post_Game")
    excludeMissable = postgame or not is_option_enabled(multiworld, player, "UnavailableInPostGame")

    for spot in MINING_SPOTS:
        name = spot["Name"]

        if excludeMissable and spot["Pickaxe"] == "Ephemeral Ether Pickaxe":
            continue

        multiworld.get_location(name, player).access_rule = lambda state, player=player, spot=spot, postgame=postgame: canMineDeposit(state, player, spot, postgame)