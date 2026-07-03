from test.bases import WorldTestBase
from ..Game import game_name

regions = [
    # starting region:
    "Colony 9",
    # require 1 key each, specified as local/early:
    "Tephra Cave", "Bionis' Leg", "Colony 6", "Ether Mine", "Satorl Marsh",
    # require 1 key each:
    "Bionis' Interior (1st Visit)", "Makna Forest", "Frontier Village", "Eryth Sea", "Alcamoth", "High Entia Tomb",
    # require 2 keys each:
    "Prison Island (1st Visit)", "Valak Mountain", "Sword Valley", "Galahad Fortress", "Fallen Arm", "Mechonis Field", "Central Factory",
    # require 3 keys each:
    "Agniratha", "Mechonis Core", "Bionis' Interior (2nd Visit)", "Prison Island (2nd Visit)"
]

class XenobladeManualTest(WorldTestBase):
    game = game_name

    def getRegionKeyRequirements(self, region):
        keys = []
        keyReq = 1

        currentRegion = regions[0]
        while (currentRegion != region):
            currentRegion = regions[regions.index(currentRegion) + 1]
            if (currentRegion == "Prison Island (1st Visit)"):
                keyReq = 2
            elif (currentRegion == "Agniratha"):
                keyReq = 3
            keys.append(currentRegion + " Key:" + str(keyReq))

        return keys

    # Check that the location becomes reachable only after all specified items are collected
    def checkItemsForLocation(self, loc, items):
        itemsToCollect = []
        itemsCollected = []

        for item in items:
            if ":" in item:
                itemName, count = item.split(":")
                count = int(count)
                for _ in range(count):
                    itemsToCollect.append(itemName)
            else:
                itemsToCollect.append(item)

        for i in range(len(itemsToCollect)):
            item = itemsToCollect[i]
            index = 0

            if item in itemsCollected:
                index = itemsCollected.count(item)
            itemsCollected.append(item)

            thisItems = self.get_items_by_name(item)

            self.collect(thisItems[index])

            if i == len(itemsToCollect) - 1:
                self.assertTrue(self.can_reach_location(loc))
            else:
                self.assertFalse(self.can_reach_location(loc))