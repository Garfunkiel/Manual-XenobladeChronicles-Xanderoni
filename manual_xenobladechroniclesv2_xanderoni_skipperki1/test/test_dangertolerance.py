from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_DangerTolerance_Negative10(XenobladeManualTest):
    game = game_name
    options = {
        "Danger_Tolerance": -10
    }

    def test_DangerTolerance_GentleRodriguez(self):
        self.checkItemsForLocation("Gentle Rodriguez (Lv 40)",
            [ "Progressive Hunting License:10" ] + self.getRegionKeyRequirements("Sword Valley")
        )

class XenobladeManualTest_DangerTolerance_0(XenobladeManualTest):
    game = game_name
    options = {
        "Danger_Tolerance": 0
    }

    def test_DangerTolerance_GentleRodriguez(self):
        self.checkItemsForLocation("Gentle Rodriguez (Lv 40)",
            [ "Progressive Hunting License:1" ] + self.getRegionKeyRequirements("Prison Island (1st Visit)")
        )

class XenobladeManualTest_DangerTolerance_30(XenobladeManualTest):
    game = game_name
    options = {
        "Danger_Tolerance": 30
    }

    def test_DangerTolerance_GentleRodriguez(self):
        self.checkItemsForLocation("Gentle Rodriguez (Lv 40)",
            [ "Progressive Hunting License:1" ] + self.getRegionKeyRequirements("Tephra Cave")
        )

class XenobladeManualTest_DangerTolerance_119(XenobladeManualTest):
    game = game_name
    options = {
        "Danger_Tolerance": 119
    }

    def test_DangerTolerance_GentleRodriguez(self):
        self.checkItemsForLocation("Gentle Rodriguez (Lv 40)",
            [ "Progressive Hunting License:1" ] + self.getRegionKeyRequirements("Colony 9")
        )