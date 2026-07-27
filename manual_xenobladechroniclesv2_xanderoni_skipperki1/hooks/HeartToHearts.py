from typing import Any

from ..Helpers import is_option_enabled
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

HEART_TO_HEARTS = [
    {   "Name": "Enduring Friendship",         "Shulk": 2,         "Reyn": 2       },
    {   "Name": "Sunrise in the Park",         "Shulk": 1,         "Fiora": 1      },
    {   "Name": "Fiora's Cooking",             "Reyn": 2,          "Fiora": 2      },
    {   "Name": "Watching Over Them",          "Reyn": 5,          "Dunban": 5     },
    {   "Name": "Overlooking the Colony",      "Reyn": 4,          "Sharla": 4     },
    {   "Name": "Ancient Wreckage",            "Reyn": 4,          "Melia": 4      },
    {   "Name": "A Heropon's Perspective",     "Sharla": 2,        "Riki": 2       },
    {   "Name": "The Legend of the Spider",    "Shulk": 4,         "Reyn": 4       },
    {   "Name": "A Scene Revisited",           "Reyn": 5,          "Fiora": 5      },
    {   "Name": "Glowing in the Night",        "Dunban": 2,        "Riki": 2       },
    {   "Name": "Geography Lesson",            "Shulk": 4,         "Dunban": 4     },
    {   "Name": "What Visions May Bring",      "Shulk": 2,         "Sharla": 2     },
    {   "Name": "Heir to the Monado",          "Reyn": 2,          "Dunban": 2     },
    {   "Name": "What's On Reyn's Mind",       "Reyn": 2,          "Sharla": 2     },
    {   "Name": "Revisiting the Past",         "Sharla": 5,        "Dunban": 5     },
    {   "Name": "Renewed Determination",       "Shulk": 5,         "Reyn": 5       },
    {   "Name": "Strength of Heart",           "Shulk": 5,         "Dunban": 5     },
    {   "Name": "The Colony Reborn",           "Shulk": 5,         "Sharla": 5     },
    {   "Name": "One Year On",                 "Reyn": 4,          "Dunban": 4     },
    {   "Name": "Recovery and Reflection",     "Fiora": 4,         "Dunban": 4     },
    {   "Name": "Quiet Time",                  "Fiora": 4,         "Riki": 4       },
    {   "Name": "Dunban's Right Arm",          "Sharla": 4,        "Dunban": 4     },
    {   "Name": "A Broken Watch",              "Shulk": 4,         "Sharla": 4     },
    {   "Name": "A Wistful Glow",              "Reyn": 5,          "Sharla": 5     },
    {   "Name": "The Shimmering Marsh",        "Shulk": 2,         "Dunban": 2     },
    {   "Name": "High Entia History",          "Dunban": 4,        "Melia": 4      },
    {   "Name": "Atop the Crown Tree",         "Sharla": 5,        "Riki": 5       },
    {   "Name": "Fallen Brethren",             "Shulk": 2,         "Melia": 2      },
    {   "Name": "Riki's Crazy Crystal Plan",   "Reyn": 4,          "Riki": 4       },
    {   "Name": "No Boys Allowed",             "Sharla": 2,        "Melia": 2      },
    {   "Name": "At the Pollen Works",         "Shulk": 2,         "Riki": 2       },
    {   "Name": "Reawakened Memories",         "Fiora": 4,         "Sharla": 4     },
    {   "Name": "A Day Like Any Other",        "Fiora": 4,         "Melia": 4      },
    {   "Name": "Life's Hard for a Heropon",   "Dunban": 5,        "Riki": 5       },
    {   "Name": "True Natures",                "Dunban": 2,        "Melia": 2      },
    {   "Name": "A Mysterious Sanctuary",      "Melia": 2,         "Riki": 2       },
    {   "Name": "Fish Fly! Fish Fly!",         "Reyn": 2,          "Riki": 2       },
    {   "Name": "Riki Have Question",          "Fiora": 5,         "Riki": 5       },
    {   "Name": "A Gift for a Loved One",      "Sharla": 2,        "Dunban": 2     },
    {   "Name": "Flowers of Eryth Sea",        "Sharla": 2,        "Riki": 2       },
    {   "Name": "So Close, Yet So Far",        "Shulk": 4,         "Melia": 4      },
    {   "Name": "A Breathtaking Sight",        "Reyn": 5,          "Melia": 5      },
    {   "Name": "Brother and Sister",          "Fiora": 2,         "Dunban": 2     },
    {   "Name": "The Forefathers",             "Fiora": 2,         "Riki": 2       },
    {   "Name": "Melia's Imperial Villa",      "Fiora": 2,         "Melia": 2      },
    {   "Name": "Ancient Astrology",           "Sharla": 4,        "Melia": 4      },
    {   "Name": "Hopes and Plans",             "Shulk": 5,         "Melia": 5      },
    {   "Name": "Echoes of Ancient Times",     "Reyn": 2,          "Melia": 2      },
    {   "Name": "A Snowy Hot Spring",          "Shulk": 4,         "Riki": 4       },
    {   "Name": "First Sight of Snow",         "Reyn": 4,          "Fiora": 4      },
    {   "Name": "In Ose Tower",                "Dunban": 2,        "Riki": 2       },
    {   "Name": "Just Like Old Times",         "Shulk": 4,         "Fiora": 4      },
    {   "Name": "A Family of Two",             "Fiora": 5,         "Dunban": 5     },
    {   "Name": "A Night-Time Chat",           "Fiora": 2,         "Sharla": 2     },
    {   "Name": "Overcoming the Pain",         "Fiora": 5,         "Melia": 5      },
    {   "Name": "Those Waiting for You",       "Shulk": 5,         "Riki": 5       },
    {   "Name": "Eternal Scars",               "Dunban": 5,        "Melia": 5      },
    {   "Name": "Camping Spot",                "Melia": 4,         "Riki": 4       },
    {   "Name": "Fiora's Body",                "Fiora": 5,         "Sharla": 5     },
    {   "Name": "Kind Words",                  "Melia": 5,         "Riki": 5       },
    {   "Name": "Untold Feelings",             "Sharla": 5,        "Melia": 5      },
    {   "Name": "Journey's End",               "Reyn": 5,          "Riki": 5       },
    {   "Name": "Before the Final Battle",     "Shulk": 5,         "Fiora": 5      }
]

def canAccessH2H(state: CollectionState, player: int, H2H: dict, spoilers: bool) -> bool:
    if (H2H["Name"] == "The Colony Reborn"):
        if not state.has("Colony 6 Reconstruction Special Level", player, 5):
            return False
    elif (H2H["Name"] == "Quiet Time"):
            if not state.has("Colony 6 Reconstruction Special Level", player, 3):
                return False

    for char in ["Shulk", "Reyn", "Sharla", "Dunban", "Melia", "Riki"]:
        if (H2H.get(char) is not None and not state.has(f"{char} Progressive Affinity Rank", player, H2H[char])):
            return False

    if H2H.get("Fiora") is not None:
        if spoilers:
            if not state.has(f"Fiora Progressive Affinity Rank", player, H2H["Fiora"]):
                return False
        else:
            if not state.has(f"Seven Progressive Affinity Rank", player, H2H["Fiora"]):
                return False

    return True

def setHeartToHeartRules(world: World, multiworld: MultiWorld, player: int, spoilers: bool):
    for H2H in HEART_TO_HEARTS:
        h2hname = H2H["Name"]
        if h2hname in ["Fiora's Body", "Fiora's Cooking"] and not spoilers:
            h2hname = h2hname.replace("Fiora", "Seven")

        multiworld.get_location(h2hname, player).access_rule = lambda state, player=player, H2H=H2H, spoilers=spoilers: canAccessH2H(state, player, H2H, spoilers)
