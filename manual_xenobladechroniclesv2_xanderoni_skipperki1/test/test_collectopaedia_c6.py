from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_NoColSanity_Colony6(XenobladeManualTest):
    game = game_name
    options = {
        "Collectopaedia": 1,
    }

    def test_C6Flowers(self):
        """Test Colony 6 Flower Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Flower Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Flower Category:3"
        ])

    def test_C6Animals(self):
        """Test Colony 6 Animal Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Animal Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Animal Category:2"
        ])

    def test_C6Strange(self):
        """Test Colony 6 Strange Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Strange Category:4"
        ])

    def test_C6All(self):
        """Test Colony 6 Collectopaedia Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Flower Category:3",
            "Progressive Animal Category:2",
            "Progressive Strange Category:4"
        ])