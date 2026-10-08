from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_PaolaAndNarine(XenobladeManualTest):
    game = game_name
    options = {
        "GameOrder": 0,
        "Party_Affinity": True,
        "Monster_Hunting": 0,
        "Post_Game": False,
        "Spoilers": False
    }

    def test_PaolaAndNarine(self):
        self.checkItemsForLocation("Paola and Narine",
            self.getRegionKeyRequirements("Makna Forest") + [
            "Shulk Progressive Affinity Rank:4",
            "Reyn Progressive Affinity Rank:4",
            "Sharla Progressive Affinity Rank:4",
            "Melia Progressive Affinity Rank:4"
        ])

    def test_PaolaAndNarine_Seven(self):
        self.checkItemsForLocation("Paola and Narine",
            self.getRegionKeyRequirements("Makna Forest") + [
            "Shulk Progressive Affinity Rank:4",
            "Reyn Progressive Affinity Rank:4",
            "Sharla Progressive Affinity Rank:4",
            "Seven Progressive Affinity Rank:4",
            "Frontier Village Key",
            "Eryth Sea Key",
            "Alcamoth Key",
            "High Entia Tomb Key",
            "Prison Island (1st Visit) Key:2",
            "Valak Mountain Key:2",
            "Sword Valley Key:2",
            "Galahad Fortress Key:2",
            "Fallen Arm Key:2"
        ])