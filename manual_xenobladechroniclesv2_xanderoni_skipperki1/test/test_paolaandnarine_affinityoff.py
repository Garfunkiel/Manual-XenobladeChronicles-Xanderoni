from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_PaolaAndNarine_AffinityOff(XenobladeManualTest):
    game = game_name
    options = {
        "GameOrder": 0,
        "Party_Affinity": False,
        "Post_Game": False
    }

    def test_PaolaAndNarine_AffinityOff(self):
        self.checkItemsForLocation("Paola and Narine",
            self.getRegionKeyRequirements("Makna Forest")
        )
