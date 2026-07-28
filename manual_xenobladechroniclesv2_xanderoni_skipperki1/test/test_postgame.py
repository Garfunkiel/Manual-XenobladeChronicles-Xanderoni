from ..Game import game_name
from .manual_test import XenobladeManualTest

class XenobladeManualTest_PostGame_Off(XenobladeManualTest):
    game = game_name
    options = {
        "Post_Game": False
    }

    def test_PostGame(self):
        self.assertTrue(self.count("Colony 9 Key") == 1)
        self.assertTrue(self.count("Tephra Cave Key") == 0)
        self.assertTrue(self.count("Prison Island (1st Visit) Key") == 0)
        self.assertTrue(self.count("Prison Island (2nd Visit) Key") == 0)

class XenobladeManualTest_PostGame_C9(XenobladeManualTest):
    game = game_name
    options = {
        "Post_Game": True,
        "Post_Game_Region": 1
    }

    def test_PostGame(self):
        self.assertTrue(self.count("Colony 9 Key") == 1)
        self.assertTrue(self.count("Tephra Cave Key") == 0)
        self.assertTrue(self.count("Prison Island (1st Visit) Key") == 0)
        self.assertTrue(self.count("Prison Island (2nd Visit) Key") == 0)

class XenobladeManualTest_PostGame_TC(XenobladeManualTest):
    game = game_name
    options = {
        "Post_Game": True,
        "Post_Game_Region": 2
    }

    def test_PostGame(self):
        self.assertTrue(self.count("Colony 9 Key") == 0)
        self.assertTrue(self.count("Tephra Cave Key") == 1)
        self.assertTrue(self.count("Prison Island (1st Visit) Key") == 0)
        self.assertTrue(self.count("Prison Island (2nd Visit) Key") == 0)


class XenobladeManualTest_PostGame_PI(XenobladeManualTest):
    game = game_name
    options = {
        "Post_Game": True,
        "Post_Game_Region": 15
    }

    def test_PostGame(self):
        self.assertTrue(self.count("Colony 9 Key") == 0)
        self.assertTrue(self.count("Tephra Cave Key") == 0)
        self.assertTrue(self.count("Prison Island (1st Visit) Key") == 2)
        self.assertTrue(self.count("Prison Island (2nd Visit) Key") == 3)