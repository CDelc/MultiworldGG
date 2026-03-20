# Setup Guide for Dark Souls Remastered for MWGG

## Required Software

* [Dark Souls Remastered](https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/)
* [Latest DSAP Client](https://github.com/ArsonAssassin/DSAP/releases/)

## Join a Multiworld Room

1. When you start up the game, ensure you are **disconnected from the network**. It is recommended to configure Dark Souls Remastered's settings in System->Network Settings->Launch Setting="Start Offline", to avoid accidentally starting online.
**WARNING: You should never connect to the FromSoft network while using this mod or its saves. If you are connected to the online Servers while using this mod, or with a save in which this mod was used, you will likely face account restrictions (bans) by FromSoft!!**
2. Run Dark Souls Remastered.
3. Load into your save file created specifically for this seed/multiworld, or start a New Game, create your character, and proceed to the point where you are able to control and move your character.
    * **Be careful not load into a wrong save** - if it has locations checked that have not been checked in your save for this seed, you will end up sending checks you have not yet made, which would be a bummer and not fun.
4. Verify you loaded into the correct save.
5. With both the MultiworldGG server and game running, Unzip the client file you downloaded earlier and run DSAP.Desktop.exe.
6. Click on the three-horizontal-line icon at the top left of the DSAP client window.
7. Fill in your host, slot and password (if required) and press Connect.
    * You can click in the DSAP client window outside of the left-hand-side menu to show the Log.
8. This will cause your game to reload as if you had used a homeward bone. This is necessary to update the items that are in the game.
9. You should now be ready to play.


# Troubleshooting

* If you encounter issues, first make sure your Dark Souls Remastered game is up to date (Main menu should show the text "App ver. 1.03.1" & "Regulation ver. 1.04"). If it is not, use the "verify game files" in Steam. It is recommended to also make sure any other residual mods are removed before doing so.
* Then, check the known issues listed below. If your issue is in the list for your version, the issue you have may be resolved by updating to a later version.
* If item lots are not replaced, or the client cannot connect, **try running DSAP.client.exe as administrator**. This program requires authorization to modify the memory of another process, so it may require elevated permissions depending on your system configuration.
* If none of the above resolve your issues, you may be able to search for answers in the AP Discord channel for dark-souls-1.
  * First check the pins. Then try searching the channel specifically to see if others have encountered your issue.
  * If you don't find anything, please comment in the channel and include the version number of DSAP that you are using, the MWGG/AP version you are using, and a description of the issue, including context.
  * If either DSAP or DSR crashed, note the time of the error, then open "Event Viewer" from the start menu, go to Windows Logs->Application, and look for an "Error" level log entry. Right click the relevant entry to copy the details as text, and provide the file with your report. If there are multiple Error entries at the time of error, provide both.
