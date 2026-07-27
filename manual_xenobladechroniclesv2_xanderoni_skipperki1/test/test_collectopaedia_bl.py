from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_NoColSanity_BionisLeg(XenobladeManualTest):
    game = game_name
    options = {
        "Collectopaedia": 1,
    }

    def test_BLVegetables(self):
        """Test Bionis' Leg Vegetable Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Vegetable Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Vegetable Category:2"
        ])

    def test_BLFruit(self):
        """Test Bionis' Leg Fruit Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Fruit Category:3"
        ])

    def test_BLBugs(self):
        """Test Bionis' Leg Bug Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Bug Category:3"
        ])

    def test_BLNature(self):
        """Test Bionis' Leg Nature Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Nature Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Nature Category:2"
        ])

    def test_BLParts(self):
        """Test Bionis' Leg Part Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Part Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Part Category:2"
        ])

    def test_BLStrange(self):
        """Test Bionis' Leg Strange Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Strange Category:3"
        ])

    def test_BLAll(self):
        """Test Bionis' Leg Collectopaedia Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Vegetable Category:2", "Progressive Fruit Category:3", "Progressive Bug Category:3", "Progressive Nature Category:2", "Progressive Part Category:2", "Progressive Strange Category:3"
        ])