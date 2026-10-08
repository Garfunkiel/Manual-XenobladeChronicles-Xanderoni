from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_OneIsNeverEnough_Off(XenobladeManualTest):
    game = game_name
    options = {
        "Post_Game": False,
        "GameOrder": 0,
        "Achievements": True,
        "Collectopaedia": "no collectopaedia"
    }

    def test_OneIsNeverEnough_Colony9_Off(self):
        self.checkItemsForLocation("One is Never Enough",
            self.getRegionKeyRequirements("Colony 9")
        )
