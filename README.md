# Xenoblade Chronicles Manual APWorld
Credit for creating this Manual AP (and doing the vast majority of the work on it) belongs to Xanderoni, with additional work by skipperki1. I have added my name only to the version number; this is to ensure that blame is properly assigned to me if something goes wrong as a result of my changes.

## Changes from Xanderoni's version 2.0:
- Used the newest Manual Builder to regenerate everything using the newest stable Manual code
- Added Eijebong's Fuzz and Test Github Actions
- Reduced fuzzing failures from ~25% to ~0% (none in a local 1000 run test, but it's possible that there are very rare failure scenarios yet to be discovered)
- Reduced fuzzing timeouts from ~40% to <10%
- Reduced testing failures from 23 to 0; eliminated testing errors other than those relating to pickling options, which may be unfixable without changes to the standard Manual code
- Regions are no longer treated as optional because they are now linear
- Setting the Collectopaediasanity option to true now requires Collectopaedia to also be set to true (this prevents many fuzzing failures)
- Added the Blossoming Friendship achievement
- Requirements have been adjusted for the following locations (and categories of locations):
  - High level Unique Monsters (which mostly now require Mechonis Core access)
  - Art School
  - Chain Gang
  - Come On, Cheer Up!
  - Critical Thinking
  - Cylinder Hangar
  - Emergency Warehouse
  - Flattened Flowers
  - Go Team!
  - One Step Further
  - Right, Let's Do This!
  - And others; to see the full list, check the diff between the 2.0-xanderoni tag and the 2.0.1-garfunkiel tag
- Fixed typos:
  - Various categories (including Unique Monsters) are now properly included/excluded based on yaml options
  - Other typos have also been fixed, including a few that caused fuzzing and testing errors

## Known Errors:
- Landmarks and locations are still included regardless of yaml options (can be trivially fixed by adjusting casing in categories.json, but excluding these types tends to cause the number of items to be greater than the number of locations, causing fuzzing failures)