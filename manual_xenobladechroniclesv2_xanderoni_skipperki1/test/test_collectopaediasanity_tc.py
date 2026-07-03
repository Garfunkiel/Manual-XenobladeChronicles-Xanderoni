from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_ColSanity_TephraCave(XenobladeManualTest):
    game = game_name
    options = {
        "collectopaediasanity": True,
    }

    def test_TCFlower(self):
        """Test Tephra Cave Flower Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Flower Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Flower Category:2", "Insanity Mint", "Night Tulip"
        ])

    def test_TCFruit(self):
        """Test Tephra Cave Fruit Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Fruit Category:2", "Clear Almond", "Bright Fig", "Dark Grape"
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

    def test_TCNature(self):
        """Test Tephra Cave Nature Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Nature Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Nature Category:1", "Kneecap Rock", "Confusion Ivy", "Clarity Moss",
        ])

    def test_TCStrange(self):
        """Test Tephra Cave Strange Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Strange Category:2", "Leaf Mystery", "Steel Silk"
        ])

    def test_TCAll(self):
        """Test Tephra Cave Collectopaedia Completion with Collectopaediasanity ON"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Page Complete",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Flower Category:2", "Insanity Mint", "Night Tulip",
            "Progressive Fruit Category:2", "Clear Almond", "Bright Fig", "Dark Grape",
            "Progressive Animal Category:1", "Shin Newt", "Cave Rat", "Shin Gecko", "Happy Rabbit",
            "Progressive Bug Category:2", "Brown Butterfly", "Gold Caterpillar", "Rumble Stonefly",
            "Progressive Nature Category:1", "Kneecap Rock", "Confusion Ivy", "Clarity Moss",
            "Progressive Strange Category:2", "Leaf Mystery", "Steel Silk"
        ])