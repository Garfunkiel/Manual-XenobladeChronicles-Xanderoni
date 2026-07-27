from ..Game import game_name
from .manual_test import XenobladeManualTest, regions, region_keys, hunting_regions
from ..Helpers import load_data_file as helpers_load_data_file

class XenobladeManualTest_Availability(XenobladeManualTest):
    game = game_name
    options = {
        "Danger_Tolerance": 119,
    }

    def test_availability(self):
        data = helpers_load_data_file("playthrough_data.json")

        locations_by_region = []

        self.collect(self.get_items_by_name("Colony 6 Reconstruction Housing Level")[0])
        self.collect(self.get_items_by_name("Colony 6 Reconstruction Commerce Level")[0])
        self.collect(self.get_items_by_name("Colony 6 Reconstruction Nature Level")[0])
        self.collect(self.get_items_by_name("Colony 6 Reconstruction Special Level")[0])

        self.collect_by_name("Shulk Progressive Affinity Rank")
        self.collect_by_name("Reyn Progressive Affinity Rank")
        self.collect_by_name("Sharla Progressive Affinity Rank")
        self.collect_by_name("Melia Progressive Affinity Rank")

        for region_name, region_data in data.items():
            region_locs = []

            types = ["Bosses", "Landmarks", "Locations", "People", "Quests", "Unique Monsters"]

            for type in types:
                for location in region_data.get(type, []):
                    location_name = location #["Name"]
                    region_locs.append(str(location_name))

            locations_by_region.append(region_locs)

        for region_num in range(len(locations_by_region)):
            if regions[region_num] in hunting_regions:
                self.collect(self.get_items_by_name("Progressive Hunting License")[hunting_regions.index(regions[region_num])])

            keys_to_collect = region_keys[regions[region_num]]
            for i in range(keys_to_collect):
                self.collect(self.get_items_by_name(regions[region_num] + " Key")[i])

            locations = locations_by_region[region_num]
            for loc in locations:
                with self.subTest(msg="Checking " + loc + " pre-keys"):
                    self.assertTrue(self.can_reach_location(loc), "Location " + loc + " should be reachable after collecting all keys for region " + regions[region_num])

            for later_region_num in range(region_num + 1, len(locations_by_region)):
                locations = locations_by_region[later_region_num]
                for loc in locations:
                    with self.subTest(msg="Checking " + loc + " post-keys"):
                        self.assertFalse(self.can_reach_location(loc), "Location " + loc + " should not be reachable before collecting all keys for region " + regions[later_region_num])

        pass