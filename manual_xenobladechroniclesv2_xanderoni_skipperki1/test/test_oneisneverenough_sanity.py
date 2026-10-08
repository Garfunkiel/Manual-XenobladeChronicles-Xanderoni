from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_OneIsNeverEnough_Sanity(XenobladeManualTest):
    game = game_name
    options = {
        "Post_Game": False,
        "GameOrder": 0,
        "Achievements": True,
        "Collectopaedia": "collectopaediasanity"
    }

    def test_OneIsNeverEnough_Colony9_Sanity(self):
        self.checkItemsForLocation("One is Never Enough",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Fruit Category:1", "Dance Apple"
        ])
