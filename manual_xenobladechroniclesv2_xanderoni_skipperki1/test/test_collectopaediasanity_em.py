from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_ColSanity_EtherMine(XenobladeManualTest):
    game = game_name
    options = {
        "Collectopaedia": 2,
    }

    def test_EMAnimals(self):
        """Test Ether Mine Animal Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Animal Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Animal Category:3",
            "Light Bat",
            "Black Frog",
            "Yellow Cat"
        ])

    def test_EMBugs(self):
        """Test Ether Mine Bug Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Bug Category:4",
            "Black Beetle",
            "Rubber Mantis",
            "Mystery Firefly"
        ])

    def test_EMNature(self):
        """Test Ether Mine Nature Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Nature Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Nature Category:3",
            "Charcoal Leg",
            "Ether Pebble",
            "Rumble Coal"
        ])

    def test_EMParts(self):
        """Test Ether Mine Part Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Parts Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Part Category:3",
            "Black Chip",
            "Ready Coil"
        ])

    def test_EMStrange(self):
        """Test Ether Mine Strange Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Strange Category:5",
            "Love Crane",
            "Fire Abron"
        ])

    def test_EMAll(self):
        """Test Ether Mine Collectopaedia Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Ether Mine Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Ether Mine") + [
            "Progressive Animal Category:3", "Light Bat", "Black Frog", "Yellow Cat",
            "Progressive Bug Category:4", "Black Beetle", "Rubber Mantis", "Mystery Firefly",
            "Progressive Nature Category:3", "Charcoal Leg", "Ether Pebble", "Rumble Coal",
            "Progressive Part Category:3", "Black Chip", "Ready Coil",
            "Progressive Strange Category:5", "Love Crane", "Fire Abron"
        ])