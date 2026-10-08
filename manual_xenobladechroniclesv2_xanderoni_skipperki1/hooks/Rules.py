from Options import OptionError
from typing import Optional, TYPE_CHECKING
from typing_extensions import override
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState
from rule_builder.rules import HasFromListUnique, Rule, And, Or, Has
from Utils import version_tuple
use_rulebuilder = version_tuple >= (0, 6, 7)

from ..Helpers import get_option_value, is_option_enabled
from ..Game import game_name
from .Collectopaedia import COLLECTOPAEDIA_REQUIREMENTS, GROUP_COUNTS
from .DangerTolerance import REGION_LEVELS

import dataclasses
import logging

if TYPE_CHECKING:
    from .. import ManualWorld

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

# FUNCTIONS TO REMOVE ONCE 0.6.6- SUPPORT HAS BEEN DROPPED:
# (add more once they've been converted to Rule Builder rule format)
def PaolaAndNarine(state: CollectionState, player: int) -> bool:
    shulkAt4 = state.has("Shulk's Affinity Rank 4", player)
    reynAt4 = state.has("Reyn's Affinity Rank 4", player)
    sharlaAt4 = state.has("Sharla's Affinity Rank 4", player)
    meliaAt4 = state.has("Melia's Affinity Rank 4", player)
    sevenAt4 = state.has("Seven's Affinity Rank 4", player)

    shulkAndReynAt4 = shulkAt4 and reynAt4
    sharlaAndMeliaAt4 = sharlaAt4 and meliaAt4
    sharlaAndSevenAt4 = sharlaAt4 and sevenAt4 and state.has("Fallen Arm Access", player)
    meliaAndSevenAt4 = meliaAt4 and sevenAt4 and state.has("Fallen Arm Access", player)
    anyTwoWomenAt4 = sharlaAndMeliaAt4 or sharlaAndSevenAt4 or meliaAndSevenAt4

    return shulkAndReynAt4 and anyTwoWomenAt4
# END OF FUNCTIONS TO REMOVE

def hasFullRaceAccess(multiworld: MultiWorld, player: int) -> bool|str:
    gameVersion = get_option_value(multiworld, player, "GameVersion")
    if gameVersion == 0 or gameVersion == 1: # Not the Switch 2 version -> assume full race access so all locations are reachable
        return True

    gameOrder = get_option_value(multiworld, player, "GameOrder")
    if gameOrder == 2: # Future Connected Only -> assume full race access so all locations are reachable
        return True

    postGame = get_option_value(multiworld, player, "Post_Game")

    rule = "|Ether Jet| AND "
    if postGame:
        rule += "|Colony 9 Access| AND |Bionis' Leg Access| AND |Makna Forest Access| AND |Alcamoth Access| AND |Valak Mountain Access|"
    else:
        rule += "|Fallen Arm Access|" # implies access to every area before it and all party members

    return rule

def hasFullRaceAccessRule(player: int, world: "ManualWorld") -> str:
    value = hasFullRaceAccess(world.multiworld, player)
    if (value == True):
        return ""
    if (value == False):
        raise Exception("hasFullRaceAccess returned False")
    return value

def hasDangerTolerance(multiworld: MultiWorld, player: int, monsterLevel: int) -> bool|str:
    DT = get_option_value(multiworld, player, "Danger_Tolerance")

    if not type(DT) is int:
        raise OptionError("Danger Tolerance must be an integer value")

    if get_option_value(multiworld, player, "Post_Game") == True:
        return True

    effectiveLevel = monsterLevel - DT

    requirements = ""

    for region in REGION_LEVELS:
        requirements = region["requires"]

        if effectiveLevel < region["level"]:
            break

    if requirements != "":
        return requirements
    return True

def hasDangerToleranceRule(player: int, monsterLevel: int, world: "ManualWorld") -> str:
    value = hasDangerTolerance(world.multiworld, player, monsterLevel)
    if (value == True):
        return ""
    if (value == False):
        raise Exception("hasDangerTolerance returned False")
    return value

if use_rulebuilder:
    # Rule to simplify Collectopaedia checks for categories
    @dataclasses.dataclass()
    class HasFromCategoryUniqueRule(Rule["ManualWorld"], game=game_name):
        category: str
        count: int
        def _instantiate(self, world: "ManualWorld") -> Rule.Resolved:
            requested_count = self.count
            requested_list = world.item_and_event_name_groups[self.category.strip()]
            return HasFromListUnique(*requested_list, count=requested_count).resolve(world)
        @override
        def __str__(self) -> str:
            count = f"count={self.count}"
            category = f", category={self.category}"
            return f"{self.__class__.__name__}({count}{category})"

    # Rule for the "One is Never Enough" achievement - requires the player to submit an item to the Collectopaedia
    # Which in this APWorld, requires:
    #   * Nothing (Collectopaedia = 0) [if story, Colony 9 access is sufficient; if post game, every starting area has a collectopaedia so any area can be used]
    #   * A single category unlock (Collectopaedia = 1)
    #   * A category unlock along with an item for that category (Collectopaedia = 2)
    @dataclasses.dataclass()
    class OneIsNeverEnoughRule(Rule["ManualWorld"], game=game_name):
        def _instantiate(self, world: "ManualWorld") -> Rule.Resolved:
            from ..Rules import YamlCompareRule

            areasToCombineCatsOnly = []
            areasToCombineSanity = []

            for area in COLLECTOPAEDIA_REQUIREMENTS.keys():
                if (
                    area == "Bionis' Shoulder" or area == "Alcamoth - FC" # FC areas are not eligible for the achievement
                    or area == "Other"                                    # TODO: Other is eligible but needs special handling
                ):
                    continue

                categoriesToCombineCatsOnly = []
                categoriesToCombineSanity = []

                for category in ["Vegetable", "Flower", "Fruit", "Animal", "Bug", "Nature", "Part", "Strange"]:
                    count = COLLECTOPAEDIA_REQUIREMENTS[area][category]
                    if count == 0:
                        continue

                    categoriesToCombineCatsOnly.append(
                        Has(item_name=f"Progressive {category} Category", count=count)
                    )

                    categoriesToCombineSanity.append(And(
                        Has(item_name=f"Progressive {category} Category", count=count),
                        HasFromCategoryUniqueRule(category=f"{area} Collection ({category})", count=1)
                    ))

                areasToCombineCatsOnly.append(And(
                    Has(item_name=f"{area} Access", count=1),
                    Or(*categoriesToCombineCatsOnly)
                ))

                areasToCombineSanity.append(And(
                    Has(item_name=f"{area} Access", count=1),
                    Or(*categoriesToCombineSanity)
                ))

            return Or(
                YamlCompareRule(yaml_comparison="Collectopaedia == 0"),
                And(
                    YamlCompareRule(yaml_comparison="Collectopaedia == 1"),
                    Or(*areasToCombineCatsOnly)
                ),
                And(
                    YamlCompareRule(yaml_comparison="Collectopaedia == 2"),
                    Or(*areasToCombineSanity)
                )
            ).resolve(world)

    # Rule for the "Collector's Mentality" achievement - requires the player to submit every item in an area to the Collectopaedia
    # Which in this APWorld, requires:
    #   * Nothing (Collectopaedia = 0) [if story, Colony 9 access is sufficient; if post game, every starting area has a collectopaedia so any area can be used]
    #   * Every category unlock for an area (Collectopaedia = 1)
    #   * Every category unlock for an area along with every item for that category/area (Collectopaedia = 2)
    @dataclasses.dataclass()
    class CollectorsMentalityRule(Rule["ManualWorld"], game=game_name):
        def _instantiate(self, world: "ManualWorld") -> Rule.Resolved:
            from ..Rules import YamlCompareRule

            areasToCombineCatsOnly = []
            areasToCombineSanity = []

            for area in COLLECTOPAEDIA_REQUIREMENTS.keys():
                if (
                    area == "Bionis' Shoulder" or area == "Alcamoth - FC" # FC areas are not eligible for the achievement
                    or area == "Other"                                    # TODO: Other is eligible but needs special handling
                ):
                    continue

                categoriesToCombineCatsOnly = []
                categoriesToCombineSanity = []

                for category in ["Vegetable", "Flower", "Fruit", "Animal", "Bug", "Nature", "Part", "Strange"]:
                    count = COLLECTOPAEDIA_REQUIREMENTS[area][category]
                    if count == 0:
                        continue

                    itemCount = GROUP_COUNTS[area][category]

                    categoriesToCombineCatsOnly.append(
                        Has(item_name=f"Progressive {category} Category", count=count)
                    )

                    categoriesToCombineSanity.append(And(
                        Has(item_name=f"Progressive {category} Category", count=count),
                        HasFromCategoryUniqueRule(category=f"{area} Collection ({category})", count=itemCount)
                    ))

                areasToCombineCatsOnly.append(And(
                    Has(item_name=f"{area} Access", count=1),
                    And(*categoriesToCombineCatsOnly)
                ))

                areasToCombineSanity.append(And(
                    Has(item_name=f"{area} Access", count=1),
                    And(*categoriesToCombineSanity)
                ))

            return Or(
                YamlCompareRule(yaml_comparison="Collectopaedia == 0"),
                And(
                    YamlCompareRule(yaml_comparison="Collectopaedia == 1"),
                    Or(*areasToCombineCatsOnly)
                ),
                And(
                    YamlCompareRule(yaml_comparison="Collectopaedia == 2"),
                    Or(*areasToCombineSanity)
                )
            ).resolve(world)

    # Rule to help simplify other rules
    #  - checks if two party members have an affinity rank at the specified value or higher
    @dataclasses.dataclass()
    class PartyMembersHaveAffinityRule(Rule["ManualWorld"], game=game_name):
        partyMemberA: str
        partyMemberB: str
        rank: str
        def _instantiate(self, world: "ManualWorld") -> Rule.Resolved:
            return And(
                Has(item_name=f"{self.partyMemberA}'s Affinity Rank {self.rank}", count=1),
                Has(item_name=f"{self.partyMemberB}'s Affinity Rank {self.rank}", count=1)
            ).resolve(world)

    # Rule for the "Paola and Narine" quest
    #  - requires Shulk and Reyn to have Affinity Rank 4+ and any two of the female party members (Sharla, Melia, Seven) to have Affinity Rank 4+
    @dataclasses.dataclass()
    class PaolaAndNarineRule(Rule["ManualWorld"], game=game_name):
        def _instantiate(self, world: "ManualWorld") -> Rule.Resolved:
            sevenInParty = Has(item_name="Seven in Party", count=1)
            shulkAndReynAt4 = PartyMembersHaveAffinityRule(partyMemberA="Shulk", partyMemberB="Reyn", rank="4")
            sharlaAndMeliaAt4 = PartyMembersHaveAffinityRule(partyMemberA="Sharla", partyMemberB="Melia", rank="4")
            sharlaAndSevenAt4 = And(sevenInParty, PartyMembersHaveAffinityRule(partyMemberA="Sharla", partyMemberB="Seven", rank="4"))
            meliaAndSevenAt4 = And(sevenInParty, PartyMembersHaveAffinityRule(partyMemberA="Melia", partyMemberB="Seven", rank="4"))
            anyTwoWomenAt4 = Or(sharlaAndMeliaAt4, sharlaAndSevenAt4, meliaAndSevenAt4)

            return And(shulkAndReynAt4, anyTwoWomenAt4).resolve(world)