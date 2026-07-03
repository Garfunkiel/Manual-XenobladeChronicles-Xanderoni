from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_ColSanity_BionisLeg(XenobladeManualTest):
    game = game_name
    options = {
        "collectopaediasanity": True,
    }

    def test_BLVegetables(self):
        """Test Bionis' Leg Vegetable Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Vegetable Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Vegetable Category:2", "Hot Taro", "Juicy Broccoli", "Spicy Cabbage", "Hard Lotus"
        ])

    def test_BLFruit(self):
        """Test Bionis' Leg Fruit Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Fruit Category:3", "Sour Gooseberry", "Red Durian", "Walnut Grape", "Humming Plum"
        ])

    def test_BLBugs(self):
        """Test Bionis' Leg Bug Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Bug Category:3", "White Ladybird", "Hill Firefly", "Moth Crawler", "Queen Locust", "Fire Tarantula"
        ])

    def test_BLNature(self):
        """Test Bionis' Leg Nature Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Nature Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Nature Category:2", "Mat Ice", "Bluesky Bark", "Pione Stone"
        ])

    def test_BLParts(self):
        """Test Bionis' Leg Part Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Part Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Part Category:2", "Rusty Bolt", "Winding Gear"
        ])

    def test_BLStrange(self):
        """Test Bionis' Leg Strange Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Strange Category:3", "Gold Dust Illusion", "Devious Gravity", "White Songbird", "Death Bangle"
        ])

    def test_BLAll(self):
        """Test Bionis' Leg Collectopaedia Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Bionis' Leg Collectopaedia Page Completion",
            self.getRegionKeyRequirements("Bionis' Leg") + [
            "Progressive Vegetable Category:2", "Hot Taro", "Juicy Broccoli", "Spicy Cabbage", "Hard Lotus",
            "Progressive Fruit Category:3", "Sour Gooseberry", "Red Durian", "Walnut Grape", "Humming Plum",
            "Progressive Bug Category:3", "White Ladybird", "Hill Firefly", "Moth Crawler", "Queen Locust", "Fire Tarantula",
            "Progressive Nature Category:2", "Mat Ice", "Bluesky Bark", "Pione Stone",
            "Progressive Part Category:2", "Rusty Bolt", "Winding Gear",
            "Progressive Strange Category:3", "Gold Dust Illusion", "Devious Gravity", "White Songbird", "Death Bangle"
        ])