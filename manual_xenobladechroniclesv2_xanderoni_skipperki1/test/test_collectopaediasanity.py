from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_ColSanity(XenobladeManualTest):
    game = game_name
    options = {
        "collectopaediasanity": True,
    }

    def test_C9Vegetables(self):
        """Test Colony 9 Vegetable Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Colony 9 Collectopaedia Vegetable Completion",
            self.getRegionKeyRequirements("Colony 9") + [
            "Progressive Vegetable Category:1", "Sweet Wasabi", "Cool Potato", "Red Lettuce", "Chewy Radish"
        ])

    def test_TCAnimal(self):
        """Test Tephra Cave Animal Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Animal Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Animal Category:1", "Shin Newt", "Cave Rat", "Shin Gecko", "Happy Rabbit"
        ])

    def test_TCBug(self):
        """Test Tephra Cave Bug Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Bug Category:2", "Brown Butterfly", "Gold Caterpillar", "Rumble Stonefly"
        ])

    def test_TCFruit(self):
        """Test Tephra Cave Fruit Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Fruit Category:2", "Clear Almond", "Bright Fig", "Dark Grape"
        ])

    def test_TCFlower(self):
        """Test Tephra Cave Flower Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Flower Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Flower Category:2", "Insanity Mint", "Night Tulip"
        ])

    def test_PIFruit(self):
        """Test Prison Island Fruit Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Prison Island Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Prison Island (2nd Visit)") + [
            "Progressive Hunting License:16",
            "Progressive Fruit Category:11", "Dry Lemon", "Death Lychee", "Hell Raspberry", "Deadly Kiwi"
        ])