from dataclasses import dataclass
from Options import Toggle, Range, Choice, FreeText, PerGameCommonOptions, DeathLink, TextChoice
import requests
import json
import os
import time
import logging
import re
import Utils

logger = logging.getLogger("SM64Hacks")


def _get_json_files_from_github():
    """Fetch list of JSON files from GitHub repository, with caching."""
    cache_path = os.path.join(Utils.local_path("data", "sm64hacks", "json_list_cache.json"))
    cache_duration = 86400
    
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r') as f:
                cache_data = json.load(f)
                if time.time() - cache_data.get('timestamp', 0) < cache_duration:
                    return cache_data.get('files', [])
        except Exception as e:
            logger.debug(f"Could not read cache: {e}")
    
    json_files = []
    api_base = "https://api.github.com/repos/DNVIC/sm64hack-archipelago-jsons/contents"
    
    try:
        root_response = requests.get(api_base, timeout=10)
        root_response.raise_for_status()
        folders = [item['name'] for item in root_response.json() if item.get('type') == 'dir']
        
        if not folders:
            logger.warning("No folders found in GitHub repository")
            return []
        
        for folder in folders:
            try:
                response = requests.get(f"{api_base}/{folder}", timeout=10)
                response.raise_for_status()
                for item in response.json():
                    if item.get('type') == 'file' and item.get('name', '').endswith('.json'):
                        json_files.append(item['name'])
            except requests.RequestException as e:
                logger.warning(f"Could not fetch {folder} folder from GitHub: {e}")
                continue
        
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, 'w') as f:
            json.dump({'timestamp': time.time(), 'files': json_files}, f)
        
        return json_files
    except Exception as e:
        logger.warning(f"Could not fetch JSON list from GitHub: {e}")
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r') as f:
                    return json.load(f).get('files', [])
            except Exception:
                pass
        return []


def _filename_to_option_name(filename: str) -> str:
    """Convert JSON filename to option attribute name."""
    name = filename.replace('.json', '').lower().replace('.', '_dot_')
    name = re.sub(r'[^a-z0-9_]', '_', name)
    name = re.sub(r'_+', '_', name).strip('_')
    return name


def _format_display_name(filename: str) -> str:
    """Format JSON filename for display, splitting before numbers, brackets, or uppercase letters."""
    display_name = filename.replace('.json', '')
    
    display_name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', display_name)
    display_name = re.sub(r'(?<!^)(?<![0-9.])(?=\.?\d)', ' ', display_name)
    display_name = re.sub(r'(?<!^)(?=[\[\](){}])', ' ', display_name)
    display_name = re.sub(r'(?<=\d)(?=[A-Za-z])', ' ', display_name)
    display_name = re.sub(r'(?<=[\[\](){}])(?=[A-Za-z])', ' ', display_name)
    
    display_name = re.sub(r'\.\s+(\d)', r'.\1', display_name)
    display_name = re.sub(r'\(\s+', '(', display_name)
    display_name = re.sub(r'\s+\)', ')', display_name)
    display_name = re.sub(r'\s+', ' ', display_name).strip()
    
    if display_name:
        display_name = display_name[0].upper() + display_name[1:]
    
    display_name = re.sub(r'(?i)\b([Ss][Mm])(\d)', r'SM\2', display_name)
    display_name = re.sub(r'(?i)\b([Ss][Mm])\b', 'SM', display_name)
    
    return display_name


def _populate_json_file_options():
    """Dynamically populate JsonFile class with options from GitHub."""
    json_files = _get_json_files_from_github()

    if not json_files:
        logger.warning("No JSON files found from GitHub, using fallback list")
        json_files = [
            "Super Mario 64.json",
            "24 Hour Hack.json",
            "Aventure Alpha Redone.json",
            "Cursed Castles.json",
            "Despair Marios Gambit 64.json",
            "Eureka.json",
            "Grand Star.json",
            "Kaizo Mario 64.json",
            "Koopa Power.json",
            "Lugs Delightful Dioramas.json",
            "Marios New Earth.json",
            "Peachs Memory.json",
            "Phenomena.json",
            "Plutonium Mario 64.json",
            "Sapphire.json",
            "Shining Stars Repainted.json",
            "SM64 The Green Stars.json",
            "SM74 TYA.json",
            "Star Revenge 0.json",
            "Star Revenge 1.5.json",
            "Star Revenge 2 TTM.json",
            "Star Revenge 3.json",
            "Star Revenge 3.5.json",
            "Star Revenge 4.json",
            "Star Revenge 4.5.json",
            "Star Revenge 5.json",
            "Star Revenge 5.5.json",
            "Star Revenge 6.json",
            "Star Revenge 6.25.json",
            "Star Revenge 6.5.json",
            "Star Revenge 7.json",
            "Star Revenge 7.5.json",
            "Star Revenge 7.5 Expert.json",
            "Star Revenge 8.json",
            "Star Revenge 8 Advanced.json",
            "Super Donkey Kong 64.json",
            "Super Mario 74.json",
            "Super Mario Fantasy 64.json",
            "Super Mario Star Road.json",
            "Super Mario Treasure World.json",
            "Timeless Rendezvous.json",
            "Unoriginal Cringe Meme Hack.json",
            "Ztar Attack 2.json",
            "Ztar Attack Rebooted.json",
        ]

    option_value = 1
    new_options = {}
    new_name_lookup = {}
    for json_file in sorted(json_files):
        option_name = _filename_to_option_name(json_file)
        setattr(JsonFile, f"option_{option_name}", option_value)
        new_options[json_file.lower()] = option_value
        new_name_lookup[option_value] = json_file
        option_value += 1

    JsonFile.options.update(new_options)
    JsonFile.name_lookup.update(new_name_lookup)

    default_value = None
    for json_file in sorted(json_files):
        normalized = re.sub(r'[^a-z0-9]', '', json_file.lower().replace('.json', ''))
        if normalized == "supermario64" or "supermario64" in normalized:
            default_value = new_options.get(json_file.lower())
            break

    if default_value is not None:
        JsonFile.default = default_value
    elif option_value > 1:
        JsonFile.default = 1
        logger.warning("Could not find Super Mario 64, using first option as default")
    else:
        logger.error("No options were populated, cannot set default")


class ProgressiveKeys(Choice):
    """Makes the keys progressive items

    Off - Keys are not progressive items

    On - Keys are progressive items, you get Key 1 first and then Key 2
    May make generation impossible if there's only Key 2
    
    Reverse - Keys are progressive items, you get Key 2 first, and then Key 1
    May make generation impossible if there's only Key 1
    
    JSON - Go with the recommended value for the hack you are playing in the JSON
    Will only work with newer JSONs"""
    display_name = "Make keys progressive"
    option_off = 0
    option_on = 1
    option_reverse = 2
    option_json = 3
    default = 3

class TrollStars(Choice):
    """Enables checks for grabbing troll stars, if the JSON supports it. But beware! Every new check created by troll stars adds one trap to the pool!
    In asyncs, traps received while you are not playing will not be received all immediately but will activate randomly while you are playing the game
    Note: Each world has 1 check shared among all its troll stars, not one check per troll star.
    
    Off - Troll stars are not randomized
    
    On - Troll stars are randomized and traps are added to the pool
    
    On (no traps) - Troll stars are randomized and traps are not added into the pool. Instead singular coins will be added"""
    option_off = 0
    option_on = 1
    option_on_no_traps = 2
    display_name = "Troll Stars"

class RandomizeMoat(Toggle):
    """Shuffles the moat as a check in logic. If off, the moat will instead be placed in the vanilla location."""
    display_name = "Randomize Moat"

class JsonFile(TextChoice):
    """Name of the hack to use. Set to the JSON filename, e.g. 'Star Revenge 7.json'.
    For custom JSONs, place the file in data/sm64hacks/custom_jsons/ and use its filename here.
    Note that custom values are not supported in web generation."""
    auto_display_name = True
    display_name = "Hack to Use"
    default = 1  # Will be set by _populate_json_file_options()

    @classmethod
    def get_option_name(cls, value) -> str:
        if isinstance(value, str):
            return _format_display_name(value)
        return _format_display_name(cls.name_lookup[value])

class FillerTrapPercentage(Range):
    """Decides what percent chance of filler items should be traps, compared to coins. This only matters if some items need to be created outside of the APWorld (for example, due to item_links), not for internal junk (i.e. Troll Stars)
    
    0 - All filler is coins
    
    100 - All filler is traps"""

    display_name = "Filler Trap Percentage"
    range_start = 0
    default = 30
    range_end = 100

# Populate JsonFile options from GitHub on module import
_populate_json_file_options()

@dataclass
class SM64HackOptions(PerGameCommonOptions):
    progressive_keys: ProgressiveKeys
    troll_stars: TrollStars
    json_file: JsonFile
    randomize_moat: RandomizeMoat
    death_link: DeathLink
    filler_trap_percentage: FillerTrapPercentage
