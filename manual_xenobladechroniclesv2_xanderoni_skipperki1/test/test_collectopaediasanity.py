from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_ColSanity(XenobladeManualTest):
    game = game_name
    options = {
        "collectopaediasanity": True,
    }

    def test_PIFruit(self):
        """Test Prison Island Fruit Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Prison Island Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Prison Island (2nd Visit)") + [
            "Progressive Hunting License:16",
            "Progressive Fruit Category:11", "Dry Lemon", "Death Lychee", "Hell Raspberry", "Deadly Kiwi"
        ])