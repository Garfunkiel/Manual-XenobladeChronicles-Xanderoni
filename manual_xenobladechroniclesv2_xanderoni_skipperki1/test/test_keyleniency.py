from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_KeyLeniency(XenobladeManualTest):
    game = game_name
    options = {
        "Key_Leniency": 3
    }

    def test_KeyLeniency_Colony6(self):
        self.assertTrue("Tephra Cave Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Tephra Cave Key"] == 1)
        self.assertTrue("Bionis' Leg Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Bionis' Leg Key"] == 1)
        self.assertTrue("Colony 6 Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Colony 6 Key"] == 1)
        self.assertFalse("Ether Mine Key" in self.multiworld.local_early_items[self.player])
        self.assertFalse("Satorl Marsh Key" in self.multiworld.local_early_items[self.player])


class XenobladeManualTest_KeyLeniency_Full(XenobladeManualTest):
    game = game_name
    options = {
        "Key_Leniency": 12
    }

    def test_KeyLeniency_Full(self):
        self.assertTrue("Tephra Cave Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Tephra Cave Key"] == 1)
        self.assertTrue("Bionis' Leg Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Bionis' Leg Key"] == 1)
        self.assertTrue("Colony 6 Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Colony 6 Key"] == 1)
        self.assertTrue("Prison Island (1st Visit) Key" in self.multiworld.local_early_items[self.player])
        self.assertTrue(self.multiworld.local_early_items[self.player]["Prison Island (1st Visit) Key"] == 2)