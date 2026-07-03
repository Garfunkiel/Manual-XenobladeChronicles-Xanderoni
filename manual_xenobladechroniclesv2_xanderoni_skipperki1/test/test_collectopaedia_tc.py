from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_NoColSanity_TephraCave(XenobladeManualTest):
    game = game_name
    options = {
        "collectopaediasanity": False,
    }

    def test_TCFlower(self):
        """Test Tephra Cave Flower Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Flower Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Flower Category:2"
        ])

    def test_TCFruit(self):
        """Test Tephra Cave Fruit Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Fruit Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Fruit Category:2"
        ])

    def test_TCAnimal(self):
        """Test Tephra Cave Animal Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Animal Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Animal Category:1"
        ])

    def test_TCBug(self):
        """Test Tephra Cave Bug Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Bug Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Bug Category:2"
        ])

    def test_TCNature(self):
        """Test Tephra Cave Nature Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Nature Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Nature Category:1"
        ])

    def test_TCStrange(self):
        """Test Tephra Cave Strange Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Strange Completion",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Strange Category:2"
        ])

    def test_TCAll(self):
        """Test Tephra Cave Collectopaedia Completion with Collectopaediasanity OFF"""
        self.checkItemsForLocation("Tephra Cave Collectopaedia Page Complete",
            self.getRegionKeyRequirements("Tephra Cave") + [
            "Progressive Flower Category:2", "Progressive Fruit Category:2", "Progressive Animal Category:1", "Progressive Bug Category:2", "Progressive Nature Category:1", "Progressive Strange Category:2"
        ])