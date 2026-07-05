from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_NoColSanity(XenobladeManualTest):
    game = game_name
    options = {
        "collectopaediasanity": False,
    }

    def test_PIFruit(self):
        """Test Prison Island Fruit Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Prison Island Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Prison Island (2nd Visit)") + [
            "Progressive Hunting License:16",
            "Progressive Fruit Category:11",
        ])