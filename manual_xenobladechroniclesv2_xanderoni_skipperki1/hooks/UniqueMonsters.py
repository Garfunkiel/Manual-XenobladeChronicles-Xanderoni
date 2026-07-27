from typing import Any

from ..Helpers import is_option_enabled
from .Rules import hasDangerTolerance
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

UNIQUE_MONSTERS = [
    # Colony 9
    {   "Name": "Verdant Bluchal (Lv 5)",                       "Level": 5,             "Licenses":  1      },
    {   "Name": "Itinerant Dorothea (Lv 6)",                    "Level": 6,             "Licenses":  1      },
    {   "Name": "Evil Rhangrot (Lv 6)",                         "Level": 6,             "Licenses":  1,     "ChallengeQuest": "Challenge 1 (Colony 9)"      },
    {   "Name": "Lake Magdalena (Lv 6)",                        "Level": 6,             "Licenses":  1      },
    {   "Name": "Speedy Ramshyde (Lv 10)",                      "Level": 10,            "Licenses":  1      },
    {   "Name": "Enchanting Grune (Lv 13)",                     "Level": 13,            "Licenses":  1      },
    {   "Name": "Dark Murakmor (Lv 18)",                        "Level": 18,            "Licenses":  1      },
    {   "Name": "Gentle Mother Armu (Lv 37)",                   "Level": 37,            "Licenses":  1      },
    {   "Name": "Impenetrable Redrob (Lv 38)",                  "Level": 38,            "Licenses":  1      },
    {   "Name": "Roguish Frengel (Lv 39)",                      "Level": 39,            "Licenses":  1      },
    {   "Name": "Gentle Rodriguez (Lv 40)",                     "Level": 40,            "Licenses":  1      },
    {   "Name": "Shadeless Matrix (Lv 44)",                     "Level": 44,            "Licenses":  1      },
    {   "Name": "Flailing Bracken (Lv 73)",                     "Level": 73,            "Licenses":  1      },
    # Tephra Cave
    {   "Name": "Cellar Bugworm (Lv 10)",                       "Level": 10,            "Licenses":  2      },
    {   "Name": "Gluttonous Eugen (Lv 11)",                     "Level": 11,            "Licenses":  2      },
    {   "Name": "Mining Patrichev (Lv 8)",                      "Level":  8,            "Licenses":  2      },
    {   "Name": "Solid Konev (Lv 10)",                          "Level": 10,            "Licenses":  2      },
    {   "Name": "Wallslide Gwynry (Lv 9)",                      "Level":  9,            "Licenses":  2      },
    # Tephra Cave (Post-MC)
    {   "Name": "Erratic Goliante (Lv 97)",     "Story": "MC",  "Level": 97,            "Licenses":  2      },
    {   "Name": "Judicious Bunnitzol (Lv 94)",  "Story": "MC",  "Level": 94,            "Licenses":  2      },
    {   "Name": "Musical Vanflare (Lv 93)",     "Story": "MC",  "Level": 93,            "Licenses":  2      },
    {   "Name": "Plump Sprahda (Lv 92)",        "Story": "MC",  "Level": 92,            "Licenses":  2      },
    {   "Name": "Protective Torquidon (Lv 96)", "Story": "MC",  "Level": 96,            "Licenses":  2      },
    {   "Name": "Reckless Galdon (Lv 95)",      "Story": "MC",  "Level": 95,            "Licenses":  2      },
    {   "Name": "Dazzling Tolosnia (Lv 97)",    "Story": "MC",  "Level": 97,            "Licenses":  2      },
    {   "Name": "Firework Geldesia (Lv 98)",    "Story": "MC",  "Level": 98,            "Licenses":  2      },
    {   "Name": "Reckless Zanden (Lv 98)",      "Story": "MC",  "Level": 98,            "Licenses":  2      },
    # Bionis' Leg
    {   "Name": "Armoured Rockwell (Lv 82)",                    "Level": 82,            "Licenses":  3      },
    {   "Name": "Canyon Valencia (Lv 78)",                      "Level": 78,            "Licenses":  3      },
    {   "Name": "Clifftop Bayern (Lv 32)",                      "Level": 32,            "Licenses":  3      },
    {   "Name": "Field Altrich (Lv 76)",                        "Level": 76,            "Licenses":  3      },
    {   "Name": "Immovable Gonzalez (Lv 90)",                   "Level": 90,            "Licenses":  3      },
    {   "Name": "Mysterious Barnaby (Lv 75)",                   "Level": 75,            "Licenses":  3      },
    {   "Name": "Napping Volfen (Lv 17)",                       "Level": 17,            "Licenses":  3      },
    {   "Name": "Night Cardamon (Lv 18)",                       "Level": 18,            "Licenses":  3      },
    {   "Name": "Sniper Paramecia (Lv 15)",                     "Level": 15,            "Licenses":  3      },
    {   "Name": "Territorial Rotbart (Lv 81)",                  "Level": 81,            "Licenses":  3      },
    {   "Name": "Trainer Harmelon (Lv 15)",                     "Level": 15,            "Licenses":  3      },
    {   "Name": "Vagrant Alfead (Lv 16)",                       "Level": 16,            "Licenses":  3      },
    {   "Name": "Violent Andante (Lv 16)",                      "Level": 16,            "Licenses":  3      },
    {   "Name": "White Eduardo (Lv 17)",                        "Level": 17,            "Licenses":  3      },
    # Colony 6
    {   "Name": "Graceful Holand (Lv 19)",                      "Level": 19,            "Licenses":  4      },
    {   "Name": "Drifter Jutard (Lv 25)",       "Story": "EM",  "Level": 25,            "Licenses":  4      },
    # Ether Mine
    {   "Name": "Dark Kisling (Lv 20)",                         "Level": 20,            "Licenses":  5      },
    {   "Name": "Vengeful Daulton (Lv 22)",                     "Level": 22,            "Licenses":  5      },
    {   "Name": "Elegant Marin (Lv 29)",                        "Level": 29,            "Licenses":  5      },
    # Satorl Marsh
    {   "Name": "Aggressive Cornelius (Lv 28)",                 "Level": 28,            "Licenses":  6      },
    {   "Name": "Amber Fischer (Lv 27)",                        "Level": 27,            "Licenses":  6      },
    {   "Name": "Cautious Balteid (Lv 26)",                     "Level": 26,            "Licenses":  6      },
    {   "Name": "Eternal Palsadia (Lv 91)",                     "Level": 91,            "Licenses":  6      },
    {   "Name": "Indomitable Daulton (Lv 85)",                  "Level": 85,            "Licenses":  6      },
    {   "Name": "Reckless Godwin (Lv 31)",                      "Level": 31,            "Licenses":  6      },
    {   "Name": "Stormy Widardun (Lv 25)",                      "Level": 25,            "Licenses":  6      },
    {   "Name": "Sunlight Schvaik (Lv 30)",                     "Level": 30,            "Licenses":  6      },
    {   "Name": "Swift Zektol (Lv 28)",                         "Level": 28,            "Licenses":  6      },
    {   "Name": "Tumultuous Felix (Lv 27)",                     "Level": 27,            "Licenses":  6      },
    {   "Name": "Veteran Yozel (Lv 83)",                        "Level": 83,            "Licenses":  6      },
    # Makna Forest
    {   "Name": "Agile Albatro (Lv 33)",                        "Level": 33,            "Licenses":  7      },
    {   "Name": "Breezy Zolos (Lv 37)",                         "Level": 37,            "Licenses":  7      },
    {   "Name": "Brutal Gravar (Lv 46)",        "Story": "PI",  "Level": 46,            "Licenses":  7      },
    {   "Name": "Elder Gragus (Lv 34)",                         "Level": 34,            "Licenses":  7      },
    {   "Name": "Illustrious Golteus (Lv 98)",  "Story": "MC",  "Level": 98,            "Licenses":  7      },
    {   "Name": "Lazy Bluco (Lv 34)",                           "Level": 34,            "Licenses":  7      },
    {   "Name": "Magnificent Digalus (Lv 99)",  "Story": "MC",  "Level": 99,            "Licenses":  7      },
    {   "Name": "Obsessive Galgaron (Lv 35)",                   "Level": 35,            "Licenses":  7      },
    {   "Name": "Shimmering Forte (Lv 33)",                     "Level": 33,            "Licenses":  7      },
    {   "Name": "Unreliable Rezno (Lv 96)",     "Story": "MC",  "Level": 96,            "Licenses":  7      },
    # Eryth Sea
    {   "Name": "Bizarre Ragoel (Lv 88)",                       "Level": 88,            "Licenses":  8      },
    {   "Name": "Clamorous Dablon (Lv 92)",                     "Level": 92,            "Licenses":  8      },
    {   "Name": "Cumulus Danaemos (Lv 41)",     "Story": "AL",  "Level": 41,            "Licenses":  8      },
    {   "Name": "Deadly Medorlo (Lv 93)",       "Story": "MC",  "Level": 93,            "Licenses":  8      },
    {   "Name": "Flabbergasted Jerome (Lv 38)",                 "Level": 38,            "Licenses":  8      },
    {   "Name": "Funeral Gozra (Lv 42)",                        "Level": 42,            "Licenses":  8      },
    {   "Name": "Lightspeed Sonid (Lv 44)",                     "Level": 44,            "Licenses":  8      },
    {   "Name": "Peeling Kircheis (Lv 38)",     "Story": "AL",  "Level": 38,            "Licenses":  8      },
    {   "Name": "Proper Bandaz (Lv 39)",                        "Level": 39,            "Licenses":  8      },
    {   "Name": "Sacred Zagamei (Lv 89)",                       "Level": 89,            "Licenses":  8      },
    {   "Name": "Stormy Belagon (Lv 87)",                       "Level": 87,            "Licenses":  8      },
    {   "Name": "Subterranean Zomar (Lv 40)",   "Story": "AL",  "Level": 40,            "Licenses":  8      },
    {   "Name": "Tempestuous Edegia (Lv 39)",   "Story": "AL",  "Level": 39,            "Licenses":  8      },
    {   "Name": "Turbulent Belmo (Lv 36)",                      "Level": 36,            "Licenses":  8      },
    # High Entia Tomb
    {   "Name": "Calm Anzabi (Lv 38)",                          "Level": 38,            "Licenses":  9      },
    {   "Name": "Furious Jozan (Lv 96)",        "Story": "MC",  "Level": 96,            "Licenses":  9      },
    # Valak Mountain
    {   "Name": "Agile Barbatos (Lv 47)",                       "Level": 47,            "Licenses": 10      },
    {   "Name": "Barbaric Sitri (Lv 47)",                       "Level": 47,            "Licenses": 10      },
    {   "Name": "Exposure Wolfol (Lv 97)",                      "Level": 97,            "Licenses": 10      },
    {   "Name": "Glorious Buer (Lv 45)",                        "Level": 45,            "Licenses": 10      },
    {   "Name": "Hidden Gamigin (Lv 49)",                       "Level": 49,            "Licenses": 10      },
    {   "Name": "Moonlight Paimon (Lv 46)",                     "Level": 46,            "Licenses": 10      },
    {   "Name": "North Star Gusion (Lv 50)",                    "Level": 50,            "Licenses": 10      },
    {   "Name": "Vague Barbas (Lv 46)",                         "Level": 46,            "Licenses": 10      },
    {   "Name": "Wandering Amon (Lv 98)",                       "Level": 98,            "Licenses": 10      },
    {   "Name": "Banquet Vassago (Lv 48)",                      "Level": 48,            "Licenses": 10      },
    {   "Name": "Conflagrant Raxeal (Lv 45)",                   "Level": 45,            "Licenses": 10      },
    # Fallen Arm
    {   "Name": "Aged Leraje (Lv 56)",                          "Level": 56,            "Licenses": 13      },
    {   "Name": "Affluent Beleth (Lv 57)",                      "Level": 57,            "Licenses": 13      },
    {   "Name": "Evil Bathin (Lv 54)",                          "Level": 54,            "Licenses": 13      },
    {   "Name": "Powerful Eligos (Lv 80)",                      "Level": 80,            "Licenses": 13      },
    {   "Name": "Prosperous Zepar (Lv 56)",                     "Level": 56,            "Licenses": 13      },
    {   "Name": "Splendid Botis (Lv 58)",                       "Level": 58,            "Licenses": 13      },
    {   "Name": "Wicked Sallos (Lv 95)",                        "Level": 95,            "Licenses": 13      },
    # Bionis' Interior (2nd Visit)
    {   "Name": "Active Impulso (Lv 72)",                       "Level": 72,            "Licenses": 17      },
    {   "Name": "Clandestine Apety (Lv 74)",                    "Level": 74,            "Licenses": 17      },
    {   "Name": "Dark King Barbarus (Lv 77)",                   "Level": 77,            "Licenses": 17      },
    {   "Name": "Ghostly Mahatos (Lv 76)",                      "Level": 76,            "Licenses": 17      },
    {   "Name": "Mystical Klesida (Lv 72)",                     "Level": 72,            "Licenses": 17      },
    {   "Name": "Officer Robusto (Lv 75)",                      "Level": 75,            "Licenses": 17      },
    {   "Name": "Victorious Gross (Lv 73)",                     "Level": 73,            "Licenses": 17      },
    {   "Name": "Vivid Anstan (Lv 75)",                         "Level": 75,            "Licenses": 17      },
    # Prison Island (2nd Visit)
    {   "Name": "Abnormal Clone Barg (Lv 77)",                  "Level": 77,            "Licenses": 18      },
    {   "Name": "Ageless Moabit (Lv 75)",                       "Level": 75,            "Licenses": 18      },
    {   "Name": "Cold Ageshu (Lv 77)",                          "Level": 77,            "Licenses": 18      },
    {   "Name": "Fiendish Auburn (Lv 78)",                      "Level": 78,            "Licenses": 18      },
    {   "Name": "Inferno Heinrich (Lv 76)",                     "Level": 76,            "Licenses": 18      },
    {   "Name": "Majestic Clone Barg (Lv 77)",                  "Level": 77,            "Licenses": 18      },
    {   "Name": "Masterful Gigapur (Lv 77)",                    "Level": 77,            "Licenses": 18      },
    {   "Name": "Serene Imlaly (Lv 76)",                        "Level": 76,            "Licenses": 18      }
]

UNIQUE_MONSTERS_MISSABLE = [
    #Sword Valley
    {   "Name": "Benevolent Aim (Lv 51)",                       "Level": 51,            "Licenses": 11      },
    {   "Name": "Defective Ipos (Lv 50)",                       "Level": 50,            "Licenses": 11      },
    {   "Name": "Fate Labolas (Lv 51)",                         "Level": 51,            "Licenses": 11      },
    {   "Name": "Prudent Purson (Lv 49)",                       "Level": 49,            "Licenses": 11      },
    {   "Name": "Kamikaze Bune (Lv 53)",                        "Level": 53,            "Licenses": 11      },
    {   "Name": "Lightning Ronove (Lv 55)",                     "Level": 55,            "Licenses": 11      },
    {   "Name": "Mischievious Naberius (Lv 57)",                "Level": 57,            "Licenses": 11      },
    {   "Name": "Tranquil Morax (Lv 50)",                       "Level": 50,            "Licenses": 11      },
    # Galahad Fortress
    {   "Name": "Glacier Acon (Lv 52)",                         "Level": 52,            "Licenses": 12      },
    {   "Name": "Glorious Jurom (Lv 55)",                       "Level": 55,            "Licenses": 12      },
    {   "Name": "Precious Retrato (Lv 53)",                     "Level": 53,            "Licenses": 12      },
    # Mechonis Field
    {   "Name": "Amorous Arca (Lv 57)",                         "Level": 57,            "Licenses": 14      },
    {   "Name": "Commander Oracion (Lv 61)",                    "Level": 61,            "Licenses": 14      },
    {   "Name": "Destroyer Salvacion (Lv 59)",                  "Level": 59,            "Licenses": 14      },
    {   "Name": "Infernal Crocell (Lv 58)",                     "Level": 58,            "Licenses": 14      },
    {   "Name": "Revolutionary Bifrons (Lv 60)",                "Level": 60,            "Licenses": 14      },
    # Central Factory
    {   "Name": "Balanced Palamedes (Lv 62)",                   "Level": 62,            "Licenses": 15      },
    {   "Name": "Beautiful Vagul (Lv 60)",                      "Level": 60,            "Licenses": 15      },
    {   "Name": "Faithful Lancelot (Lv 59)",                    "Level": 59,            "Licenses": 15      },
    {   "Name": "Magestic Mordred (Lv 70)",                     "Level": 70,            "Licenses": 15      },
    {   "Name": "Mild Florence (Lv 58)",                        "Level": 58,            "Licenses": 15      },
    {   "Name": "Sinful Lamorak (Lv 63)",                       "Level": 63,            "Licenses": 15      },
    {   "Name": "Synchronised Gaheris (Lv 61)",                 "Level": 61,            "Licenses": 15      },
    {   "Name": "Temporal Gawain (Lv 63)",                      "Level": 63,            "Licenses": 15      },
    {   "Name": "Venerable Focalor (Lv 64)",                    "Level": 64,            "Licenses": 15      },
    # Agniratha
    {   "Name": "Vagabond Allocer (Lv 63)",                     "Level": 63,            "Licenses": 16      },
    {   "Name": "Experienced Tristan (Lv 64)",                  "Level": 64,            "Licenses": 16      },
    {   "Name": "Destructive Bors (Lv 64)",                     "Level": 64,            "Licenses": 16      },
    {   "Name": "Soothed Aglovale (Lv 65)",                     "Level": 65,            "Licenses": 16      },
    {   "Name": "Meditative Varla (Lv 65)",                     "Level": 65,            "Licenses": 16      },
    {   "Name": "Sentimental Flamral (Lv 66)",                  "Level": 66,            "Licenses": 16      },
    {   "Name": "Wrathful Orobas (Lv 67)",                      "Level": 67,            "Licenses": 16      },
    {   "Name": "Wise Gremory (Lv 68)",                         "Level": 68,            "Licenses": 16      }
]

SUPER_BOSSES = [
    {   "Name": "SUPERBOSS Despotic Arsene (Lv 108)",    "Story": "MC",     "Level": 108,       "Licenses":  6      },
    {   "Name": "SUPERBOSS Avalanche Abaasy (Lv 120)",   "Story": "MC",     "Level": 120,       "Licenses": 10      },
    {   "Name": "SUPERBOSS Blizzard Belgazas (Lv 114)",  "Story": "MC",     "Level": 114,       "Licenses": 10      },
    {   "Name": "SUPERBOSS Final Marcus (Lv 100)",                          "Level": 100,       "Licenses": 10      },
    {   "Name": "SUPERBOSS Ancient Daedala (Lv 105)",    "Story": "MC",     "Level": 105,       "Licenses": 13      }
]

def UMRuleFunction(state, multiworld, player, licenses, level, addt_rule):
    if not state.has("Progressive Hunting License", player, licenses):
        return False

    if addt_rule is not None:
        if not state.has(addt_rule, player, 1):
            return False

    DT = hasDangerTolerance(multiworld, player, level)

    if not type(DT) is str:
        return DT

    return state.has(DT.replace("|", ""), player, 1)

def getEventForStoryRequirement(story_requirement):
    if story_requirement == "MC":
        return "Mechonis Core Access"
    elif story_requirement == "EM":
        return "Ether Mine Access"
    elif story_requirement == "PI":
        return "Prison Island (1st Visit) Access"
    elif story_requirement == "AL":
        return "Alcamoth Access"
    return None

def setUniqueMonsterRules(world: World, multiworld: MultiWorld, player: int):
    Challenge_Quests_Enabled = is_option_enabled(multiworld, player, "ChallengeQuests")

    uniques = UNIQUE_MONSTERS + UNIQUE_MONSTERS_MISSABLE


    for UM in uniques:
        name = UM["Name"]
        licenses = UM["Licenses"]
        level = UM["Level"]
        associated_challenge_quest = UM.get("ChallengeQuest", None)

        addt_rule = getEventForStoryRequirement(UM.get("Story", None))


        multiworld.get_location(name, player).access_rule = lambda state, multiworld=multiworld, player=player, licenses=licenses, level=level, addt_rule=addt_rule: \
            UMRuleFunction(state, multiworld, player, licenses, level, addt_rule)

        if Challenge_Quests_Enabled and associated_challenge_quest is not None:
            multiworld.get_location(associated_challenge_quest, player).access_rule = lambda state, multiworld=multiworld, player=player, licenses=licenses, level=level, addt_rule=addt_rule: \
                UMRuleFunction(state, multiworld, player, licenses, level, addt_rule)

def setSuperBossRules(world: World, multiworld: MultiWorld, player: int):

    for UM in SUPER_BOSSES:
        addt_rule = getEventForStoryRequirement(UM.get("Story", None))


        multiworld.get_location(UM["Name"], player).access_rule = lambda state, multiworld=multiworld, player=player, licenses=UM["Licenses"], level=UM["Level"], addt_rule=addt_rule: \
            UMRuleFunction(state, multiworld, player, licenses, level, addt_rule)
