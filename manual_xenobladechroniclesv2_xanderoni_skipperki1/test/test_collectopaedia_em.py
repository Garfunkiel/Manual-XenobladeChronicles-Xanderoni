from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_NoColSanity_EtherMine(XenobladeManualTest):
    game = game_name
    options = {
        "Collectopaedia": 1,
    }

    def test_EMAnimals(self):
        """Test Ether Mine Animal Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Animal Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Animal Category:3"
        ])

    def test_EMBugs(self):
        """Test Ether Mine Bug Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Bug Category:4"
        ])

    def test_EMNature(self):
        """Test Ether Mine Nature Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Nature Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Nature Category:3"
        ])

    def test_EMParts(self):
        """Test Ether Mine Part Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Parts Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Part Category:3"
        ])

    def test_EMStrange(self):
        """Test Ether Mine Strange Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Strange Category:5"
        ])

    def test_EMAll(self):
        """Test Ether Mine Collectopaedia Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Animal Category:3",
            "Progressive Bug Category:4",
            "Progressive Nature Category:3",
            "Progressive Part Category:3",
            "Progressive Strange Category:5"
        ])