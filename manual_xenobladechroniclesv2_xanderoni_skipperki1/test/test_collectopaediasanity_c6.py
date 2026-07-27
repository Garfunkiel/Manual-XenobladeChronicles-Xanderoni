from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_ColSanity_Colony6(XenobladeManualTest):
    game = game_name
    options = {
        "Collectopaedia": 2,
    }

    def test_C6Flowers(self):
        """Test Colony 6 Flower Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Flower Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Flower Category:3",
            "Cute Orchid",
            "Sirius Anemone",
            "Spirit Clematis",
        ])

    def test_C6Animals(self):
        """Test Colony 6 Animal Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Animal Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Animal Category:2",
            "Pyro Lizard",
            "Amblygon Turtle",
            "Dobercorgi",
        ])

    def test_C6Strange(self):
        """Test Colony 6 Strange Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Strange Category:4",
            "Verdant Eternity",
            "White Night Rod"
        ])

    def test_C6All(self):
        """Test Colony 6 Collectopaedia Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Colony 6 Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Colony 6") + [
            "Progressive Flower Category:3", "Cute Orchid", "Sirius Anemone", "Spirit Clematis",
            "Progressive Animal Category:2", "Pyro Lizard", "Amblygon Turtle", "Dobercorgi",
            "Progressive Strange Category:4", "Verdant Eternity", "White Night Rod"
        ])