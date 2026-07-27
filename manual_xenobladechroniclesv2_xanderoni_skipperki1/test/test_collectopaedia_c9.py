from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_NoColSanity_Colony9(XenobladeManualTest):
    game = game_name
    options = {
        "Collectopaedia": 1,
    }

    def test_C9Vegetables(self):
        """Test Colony 9 Vegetable Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Vegetable Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Vegetable Category:1",
        ])

    def test_C9Fruit(self):
        """Test Colony 9 Fruit Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Fruit Category:1",
        ])

    def test_C9Flowers(self):
        """Test Colony 9 Flower Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Flower Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Flower Category:1"
        ])

    def test_C9Bugs(self):
        """Test Colony 9 Bug Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Bug Category:1"
        ])

    def test_C9Parts(self):
        """Test Colony 9 Part Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Part Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Part Category:1"
        ])

    def test_C9Strange(self):
        """Test Colony 9 Strange Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Strange Category:1"
        ])

    def test_C9All(self):
        """Test Colony 9 Collectopaedia Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Vegetable Category:1", "Progressive Flower Category:1", "Progressive Fruit Category:1", "Progressive Bug Category:1", "Progressive Part Category:1", "Progressive Strange Category:1"
        ])