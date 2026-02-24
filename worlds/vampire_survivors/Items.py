from BaseClasses import Item, ItemClassification
from typing import Dict, List
from .Options import VampireSurvivorsOptions
from .Locations import all_characters, all_stages, EUDAI


class VampireSurvivorsItem(Item):
    game = "Vampire Survivors"

unlock_character_items = [f"Character Unlock: {character}" for character in all_characters]
unlock_stage_items = [f"Stage Unlock: {stage}" for stage in (all_stages + [EUDAI])]
unlock_gamemodes = [f"Gamemode Unlock: {gamemode}" for gamemode in ["Hyper", "Hurry", "Arcanas", "Eggs"]]
filler_items = ["Empty Coffins", "Floor Chickens", "Suspiciously Clean Skull", "Easter Eggs", "Progressive Nothing"]

item_table: Dict[str, ItemClassification] = {
    **{item: ItemClassification.progression for item in unlock_character_items},
    **{item: ItemClassification.progression for item in unlock_stage_items},
    **{item: ItemClassification.progression for item in unlock_gamemodes},
    **{item: ItemClassification.filler for item in filler_items},
}

raw_items = unlock_character_items + unlock_stage_items + unlock_gamemodes + filler_items

def create_items(world):
    options: VampireSurvivorsOptions = world.options
    pool = world.multiworld.itempool
    stages = world.final_included_stages_list
    characters = world.final_included_characters_list

    for stage in stages:
        if stage == world.starting_stage: continue
        pool.append(world.create_item(f"Stage Unlock: {stage}"))

    for character in characters:
        if character == world.starting_character: continue
        pool.append(world.create_item(f"Character Unlock: {character}"))

    if options.lock_hurry_behind_item:
        world.check_count -= 1
        pool.append(world.create_item("Gamemode Unlock: Hurry"))

    if options.lock_hyper_behind_item:
        world.check_count -= 1
        pool.append(world.create_item("Gamemode Unlock: Hyper"))

    if options.lock_arcanas_behind_item:
        world.check_count -= 1
        pool.append(world.create_item("Gamemode Unlock: Arcanas"))

    if options.egg_inclusion == 1:
        world.check_count -= 1
        pool.append(world.create_item("Gamemode Unlock: Eggs"))

    world.check_count -= (len(stages) - 1) + (len(characters) - 1)

    for _ in range(world.check_count):
        pool.append(world.create_item(world.random.choice(filler_items)))