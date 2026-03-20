# Dark Souls Remastered

## Where is the options page?

The [player options page for this game](../player-options) contains all the options you need to configure and export a config file.

## How Randomization Works

* Every loose item on the ground, and potentially fog walls, are "locations" or "checks". Some guaranteed drops are also locations, in addition to the White Sign Soapstone location from the first Solaire encounter.
* All items in those locations will be shuffled into the randomized multiworld Item Pool. This means they can be found elsewhere, and that the items at those locations will themselves be replaced by other items in the Item Pool.
* All keys and progression items (e.g. Lordvessel) will be forced into the Item Pool, unless they drop or are shoppable from non-randomized locations.
* Undead Asylum is mostly not randomized. This is intended behavior so as to not put the player into BK mode immediately. The only randomized item is the one by the stairs to the exit.
* Enemy loot and shop items are not yet randomized. Some bosses are exceptions to this.
* Item Pool is currently constructed as follows:
    1. First all items in locations which were randomized are added to the pool.
    2. Then, key items and embers will replace any filler items. This includes any "Fog Wall Keys", if either `fogwall_sanity` option is on. This includes the three living Firekeepers' Souls.
    3. Then, Guaranteed items are added to the pool.
    4. If there are any Filler or Junk items left over, they are replaced with Souls of a Proud Knight (2000 souls each).
* If locations are excluded and excluded_locations_behavior is set to "do_not_randomize", then the items in those locations will not be added to the pool, and those locations will have their vanilla items. Even with `fogwall_sanity` on, fog walls excluded in this manner this will provide no item, as fog walls do not provide items in the base game.

## How Fogwall Sanity Works

* Fogwalls in DSR will be locked, and will require an item from the Item Pool to unlock them. Passing through them will also count as a location or "check". This is called "fogwall sanity", and it is on by default.
* This includes the Fog Wall near the beginning of the Upper Undead Burg. If it's blocked - you'll have to go somewhere else! (e.g. check the skeleton courtyard, and part of Upper New Londo Ruins)
* This does not include the fogwall in the Northern Undead Asylum.
* This `fogwall_sanity` option can be disabled, but doing so is not recommended. Without this option, about 60% of the locations in your game would be consdiered in logic immediately - this is also considered a big "Sphere 1". With a big Sphere 1, you might need to get to the last check in the immediately available 60% of your game, in order to find an item that unlocks your friend who is stuck at 10% of their game. Because of how large Dark Souls is, it could take a long time to do that many checks - and make your friends have to wait on you, for quite a while.
* There is an additional `boss_fogwall_sanity` option that can be turned on, which makes most boss' arena fogs be similarly locked.
* The `Catacombs` and `Lower New Londo Ruins` fogwalls can be bypassed by basic platforming & elevator usage repsecitvely. As a result, they do not logically block access to their other sides.

## Compatibility

* This version has been tested with Dark Souls Remastered, Steam version (App ver. 1.03.1 & Regulation ver. 1.04) on Windows 11, with Archipelago Launcher version 0.6.5. 
* Linux, even through Proton/Wine, is not yet supported

## Frequently Asked Questions (FAQ)

* Q: Can I use this with seamless co-op?
  * A: Toleration has been added for multiple players, but not thoroughly tested. See [Co-op Toleration](Co-op-Toleration) section below.
* Q: Can I use this to randomize enemies?
  * A: This mod will not randomize enemies, but some players have had success with external enemy and boss randomizers. That said, we cannot guarantee they will continue to work, and that future updates won't break compatibility.
* Q: Does this work with Prepare to Die edition?
  * A: No, The current release only works with Dark Souls Remastered. There may be potential to make it compatible with PTDE but not until we are feature-complete on remastered, as there isn't a way to legally obtain a new copy of PTDE anymore.
* Q: Does this work on Linux?
  * A: Not yet. We plan to enable it by having DSAP and DSR run together within Proton, but **critical parts of that setup are not yet working**.
* Q: Can I randomized starting gear? 
  * A: Not yet - this is planned for the future. Currently, it is recommended to create your character before connecting with the DSAP client.
* Q: Is there a tracker?
  * There is a poptracker pack available at https://github.com/routhken/Dark_Souls_Remastered_tracker/releases (poptracker download itself at https://github.com/black-sliver/PopTracker/releases)
  * Universal Tracker (UT) also works, and in it you can import the maps from the poptracker pack. UT download can be found at https://github.com/FarisTheAncient/Archipelago/releases

## Known issues

* Master Key chosen from character creation (whether as a gift or thief starting item) is not considered to be in-logic, regardless of your yaml settings. Randomized starting gear, and potentially gifts, is planned for the future.

## Co-op Toleration

As of v0.0.22.0, using the Seamless Co-op mod may work with DSAP. It has not been very thoroughly tested, and if there are any crashes or instability caused by the Seamless Co-op mod itself, we cannot do much about it. Please read the information below.
* Q: How to set it up?
  * A: **Both players should always connect with the DSAP client to the same slot** once they load into the game after creating their characters.
        This must be done before doing any checks, so it is recommended to do so **before hosting or joining** the host's session.
        On first connect, you will need to head to the Undead Asylum bonfire and get your co-op items before joining the other's session.
* Q: What items are shared?
  * A: Any items sent by other slots will be sent to both players. Any fog wall keys found in this slot's own world will be sent to both players. Any checks the co-op players get for other slots will be sent immediately when the first player picks it up or makes the check.
* Q: What items aren't shared?
  * A: Everything else - any items that the player would normally get the item popup for in-game will need to be received by each player. For boss kills, when the boss is killed with both players in the session, they will both get the item. For items on the ground, each player will have to pick them up individually.

## Contributors:

* ArsonAssassin - Creator and Maintainer
* tathxo (aka noka) - Contributor
* Nave - Contributor