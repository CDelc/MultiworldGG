# Portal 2 Setup Guide

## Required Software

- [MultiworldGG](https://github.com/MultiworldGG/MultiworldGG/releases/latest)
- Unless you use MWGG: [Portal 2 apworld](https://github.com/GlassToadstool/Archipelago/releases)
- [Portal 2 Archipelago Mod](https://github.com/GlassToadstool/Portal2ArchipelagoMod)

## Portal 2 Client Setup

Portal 2 Archipelago requires a dedicated client that is packaged with the apworld and will be accessible from the MultiworldGG launcher when you install the apworld (preinstalled on MWGG).

## Portal 2 Archipelago Mod Setup 

To use this mod you must first have a copy of Portal 2 downloaded in your Steam library.

1. Download and install [Steam](https://store.steampowered.com/about/), and download and install [Portal 2](https://store.steampowered.com/app/620/Portal_2/).
2. Download the [latest Zip archive release of the Portal 2 mod's source code from this repository](https://github.com/GlassToadstool/Portal2ArchipelagoMod/archive/refs/heads/main.zip)
3. Extract the top-level folder from the Zip file (named `Portal2ArchipelagoMod-main`)
4. Place the `Portal2ArchipelagoMod-main` folder in the `sourcemods` Steam folder.
    - On Windows, this may be found at:
        - `C:\Program Files (x86)\Steam\steamapps\sourcemods`
    - On Linux, this may be found at:
        - `~/.local/share/Steam/steamapps/sourcemods/`
5. Rename the folder from `Portal2ArchipelagoMod-main` to `Portal2Archipelago`.

The folder structure should look like this:
```
sourcemods
|   
└─── Portal2Archipelago
    |  GameInfo.txt
    |   ...
    └─── cfg
    └─── ...
```

6. Open Steam, and you should see a new game named "Portal 2 Archipelago Mod" in your game library.
> [!NOTE]
> If the game does not appear in your Steam game library, please exit (completely closing) Steam and re-launch Steam.
7. We need to change the properties of the game in order to connect to the Archipelago Portal 2 APWorld client. Right-click the "Portal 2 Archipelago Mod" game in your Library, and select the "Properties..." menu option.
8. In the dialog that appears, navigate to the "General" menu item, then in the right pane of the dialog navigate to "Launch Options". In the text input:
    - On Windows, put:
        - `-netconport 3000`
    - On Linux, put: 
        - `%command% -netconport 3000`
> [!TIP]
> If on Linux, and you cannot get the game to open as expected, you may need to run the game using Proton, following the Windows install steps.


## How to play

Setting up a game is the same as all other MultiworldGG multiworlds. You can find instuctions for generating a game [here](/tutorial/Archipelago/setup_en#generating-a-game). Hosting a game can be done on [multiworld.gg](https://multiworld.gg) or locally from the Host app in the launcher (mostly for single player games).

1. Open the "Portal 2 Client" from the MultiworldGG launcher
2. Input the multiworld server adress into the "Server" field at the top of the new window and press connect
3. Input your slot name into the command field and press enter
4. Launch the sourcemod (Portal 2 Archipelago Mod) from steam
5. From the game main menu select "Play Portal Archipelago"

You must have the Portal 2 Client connected to a server and the Portal 2 Archipelago Mod open in order to play. When you have both of these open and you are connected to a MultiworldGG game you are ready to play!