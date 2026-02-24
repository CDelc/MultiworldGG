import math
from typing import Dict, Any, ClassVar, List, Set, Optional, Callable
from Options import OptionError
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Location, Region, Item, ItemClassification, LocationProgressType, MultiWorld, CollectionState, Tutorial
from .Options import VampireSurvivorsOptions, VampireSurvivorsSettings, check_options
from .Locations import location_dictionary, non_special_characters, secret_characters, megalo_characters, \
	unfair_characters, normal_stages, bonus_stages, challenge_stages, EUDAI
from .Items import raw_items, VampireSurvivorsItem, item_table, create_items, unlock_stage_items, \
	unlock_character_items, unlock_gamemodes
from .EnemyList import enemy_map
from .EnemyHurryList import enemy_hurry_map

class VampireSurvivorsWeb(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Vampire Survivors for a MultiworldGG Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["SW_CreeperKing"]
    )
    
    tutorials = [setup_en]

class VampireSurvivors(World):
	"""
	Vampire Survivors is a 2022 independent roguelike shoot 'em up video game where players control an automatically attacking character while battling continuous waves of monsters, 
	aiming to survive the onslaught for as long as possible and unlock additional characters, weapons, and relics for future sessions.
	"""
	game = "Vampire Survivors"
	author: str = "SW_CreeperKing"
	options_dataclass = VampireSurvivorsOptions
	options: VampireSurvivorsOptions
	settings: ClassVar[VampireSurvivorsSettings]
	location_name_to_id = {value: location_dictionary.index(value) + 1 for value in location_dictionary}
	item_name_to_id = {value: raw_items.index(value) + 1 for value in raw_items}
	item_name_groups = {
		"unlocks": unlock_character_items + unlock_stage_items + unlock_gamemodes
	}
	ut_can_gen_without_yaml = True
	gen_puml = False
	web = VampireSurvivorsWeb()

	def __init__(self, multiworld: "MultiWorld", player: int):
		super().__init__(multiworld, player)
		self.starting_character = ""
		self.starting_stage = ""
		self.check_count = 0
		self.stage_goal_amount = 0
		self.final_included_characters_list: List[str] = []
		self.final_included_stages_list: List[str] = []
		self.ending_character_count = 0
		self.ending_stage_count = 0

	def generate_early(self) -> None:
		if hasattr(self.multiworld, "re_gen_passthrough"): # If UT then
			if "Vampire Survivors" not in self.multiworld.re_gen_passthrough: return
			passthrough = self.multiworld.re_gen_passthrough["Vampire Survivors"]
			# UT yaml-less support
			self.options.enemysanity.value = passthrough["enemysanity"]
			self.options.chest_checks_per_stage.value = passthrough["chest_checks_per_stage"]
			self.options.goal_requirement.value = passthrough["goal_requirement"]
			self.options.egg_inclusion.value = passthrough["egg_inclusion"]
			self.options.lock_hyper_behind_item.value = passthrough["is_hyper_locked"]
			self.options.lock_hurry_behind_item.value = passthrough["is_hurry_locked"]
			self.options.lock_arcanas_behind_item.value = passthrough["is_arcanas_locked"]

			# simple UT support
			self.starting_character = passthrough["starting_character"]
			self.starting_stage = passthrough["starting_stage"]
			self.final_included_stages_list = passthrough["final_stages"]
			self.final_included_characters_list = passthrough["final_chars"]
			self.ending_stage_count = passthrough["ending_stage_count"]

			self.multiworld.push_precollected(self.create_item(f"Stage Unlock: {self.starting_stage}"))
			self.multiworld.push_precollected(self.create_item(f"Character Unlock: {self.starting_character}"))
			return

		check_options(self)

		stages = [stage for stage in self.final_included_stages_list if stage != EUDAI]
		characters = self.final_included_characters_list

		if len(stages) > 1:
			stages_to_choose_from = [stage for stage in stages if stage in normal_stages]

			if len(stages_to_choose_from) == 0:
				stages_to_choose_from = [stage for stage in stages if stage in bonus_stages]

			if len(stages_to_choose_from) == 0:
				stages_to_choose_from = [stage for stage in stages if stage in challenge_stages]

			if len(stages_to_choose_from) == 0:
				self.starting_stage = self.random.choice(stages)
			else:
				self.starting_stage = self.random.choice(stages_to_choose_from)
		else:
			self.starting_stage = stages[0]

		if len(characters) > 1:  # choose lesser powerful characters to start with
			characters_to_choose_from = [character for character in characters if character in non_special_characters]

			if self.options.allow_secret_characters and len(characters_to_choose_from) == 0:
				characters_to_choose_from = [character for character in characters if character in secret_characters]

			if self.options.allow_megalo_characters and len(characters_to_choose_from) == 0:
				characters_to_choose_from = [character for character in characters if character in megalo_characters]

			if self.options.allow_unfair_characters and self.settings.allow_unfair_characters and len(
					characters_to_choose_from) == 0:
				characters_to_choose_from = [character for character in characters if character in unfair_characters]

			self.starting_character = self.random.choice(characters_to_choose_from)
		else:
			self.starting_character = characters[0]
		self.stage_goal_amount = len(stages) - 1

		self.multiworld.push_precollected(self.create_item(f"Stage Unlock: {self.starting_stage}"))
		self.multiworld.push_precollected(self.create_item(f"Character Unlock: {self.starting_character}"))

		if not self.options.lock_hurry_behind_item.value:
			self.multiworld.push_precollected(self.create_item("Gamemode Unlock: Hurry"))

	def create_regions(self) -> None:
		stages = self.final_included_stages_list
		characters = self.final_included_characters_list
		chest_checks = self.options.chest_checks_per_stage

		menu_region = Region("Menu", self.player, self.multiworld)
		character_region = Region("Characters", self.player, self.multiworld)

		for stage in stages:
			stage_region = Region(stage, self.player, self.multiworld)

			beaten_location = self.make_location(f"{stage} Beaten", stage_region)
			event_location = Location(self.player, f"Event: [{stage} Beaten]", None, stage_region)
			event_location.place_locked_item(Item("Beat a Stage", ItemClassification.progression, None, self.player))

			if self.options.lock_hurry_behind_item.value:
				beaten_location.access_rule = lambda state: state.has("Gamemode Unlock: Hurry", self.player)
				event_location.access_rule = lambda state: state.has("Gamemode Unlock: Hurry", self.player)

			stage_region.locations.append(event_location)

			if stage != EUDAI:
				for i in range(chest_checks):
					self.make_location(f"Open Chest #{i + 1} on {stage}", stage_region)

			stage_item_name = f"Stage Unlock: {stage}"
			menu_region.connect(stage_region, f"Menu FISH -> {stage}",
				lambda state, stage_item=stage_item_name: state.has(stage_item, self.player))

			self.multiworld.regions.append(stage_region)

		for character in characters:
			character_location = self.make_location(f"Beat with {character}", character_region)

			character_item_name = f"Character Unlock: {character}"

			if self.options.lock_hurry_behind_item.value:
				character_location.access_rule = lambda state, character_item=character_item_name: \
					state.has(character_item, self.player) and state.has("Gamemode Unlock: Hurry", self.player)
			else:
				character_location.access_rule = lambda state, character_item=character_item_name: \
					state.has(character_item, self.player)

		if self.options.enemysanity:
			enemy_region = Region("Enemies", self.player, self.multiworld)

			for enemy, raw_find_locs in enemy_map.items():
				if enemy == "Death" and ("Ode to Castlevania" not in stages or "Richter Belmont" not in characters):
					continue

				if not any(loc in stages for loc in raw_find_locs):
					continue

				hurry_map = enemy_hurry_map[enemy] if enemy in enemy_hurry_map else []
				find_locs = [loc for loc in raw_find_locs if loc not in hurry_map]
				find_locs_hurry = [loc for loc in raw_find_locs if loc in hurry_map]

				enemy_location = self.make_location(f"Kill {enemy}", enemy_region)
				enemy_stage_items = [f"Stage Unlock: {stage}" for stage in find_locs]
				enemy_stage_items_hurry = [f"Stage Unlock: {stage}" for stage in find_locs_hurry]

				if enemy != "Death":
					enemy_location.access_rule = lambda state, items=enemy_stage_items, items_hurry=enemy_stage_items_hurry:\
						state.has_any(items, self.player) or (state.has_any(items_hurry, self.player) and state.has("Gamemode Unlock: Hurry", self.player))
				else:
					enemy_location.access_rule = lambda state: state.has("Stage Unlock: Ode to Castlevania",
						self.player) and state.has("Character Unlock: Richter Belmont", self.player) and state.has("Gamemode Unlock: Hurry", self.player)

				self.check_count += 1

			menu_region.connect(enemy_region)
			self.multiworld.regions.append(enemy_region)

		self.check_count += len(characters) + len(stages) * (chest_checks + 1)

		if EUDAI in stages:
			self.check_count -= chest_checks

		menu_region.connect(character_region)
		self.multiworld.regions.append(character_region)
		self.multiworld.regions.append(menu_region)

	def create_item(self, name: str) -> VampireSurvivorsItem:
		return VampireSurvivorsItem(name, item_table[name], self.item_name_to_id[name], self.player)

	def create_items(self) -> None:
		create_items(self)

	def set_rules(self) -> None:
		if self.options.goal_requirement == 0:
			self.multiworld.completion_condition[self.player] = lambda state: state.has("Beat a Stage", self.player,
				self.stage_goal_amount)
		elif self.options.goal_requirement == 1:
			if self.ending_stage_count == 0:
				self.ending_stage_count = int(len(self.final_included_stages_list) * .75)
			self.multiworld.completion_condition[self.player] = \
				lambda state: \
					state.has(f"Stage Unlock: {EUDAI}", self.player) and \
					state.has("Beat a Stage", self.player, self.ending_stage_count)

	def generate_output(self, output_directory: str) -> None:
		if not self.gen_puml: return
		from Utils import visualize_regions
		state = self.multiworld.get_all_state(False)
		state.update_reachable_regions(self.player)
		visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml",
			show_entrance_names=True,
			regions_to_highlight=state.reachable_regions[self.player])

	def fill_slot_data(self) -> Dict[str, Any]:
		slot_data: Dict[str, Any] = {
			"goal_requirement": int(self.options.goal_requirement),
			"egg_inclusion": int(self.options.egg_inclusion.value),
			"starting_character": str(self.starting_character),
			"starting_stage": str(self.starting_stage),
			"stages_to_beat": str(self.final_included_stages_list),
			"is_hyper_locked": bool(self.options.lock_hyper_behind_item),
			"is_hurry_locked": bool(self.options.lock_hurry_behind_item),
			"is_arcanas_locked": bool(self.options.lock_arcanas_behind_item),
			"chest_checks_per_stage": int(self.options.chest_checks_per_stage),
			"enemysanity": bool(self.options.enemysanity),
			"final_stages": self.final_included_stages_list,
			"final_chars": self.final_included_characters_list,
			"ending_stage_count": int(self.ending_stage_count),
		}

		return slot_data

	def make_location(self, location_name, region) -> Location:
		location = Location(self.player, location_name, self.location_name_to_id[location_name], region)
		region.locations.append(location)
		return location

	# for the universal tracker, doesn't get called in standard gen
	# docs: https://github.com/FarisTheAncient/Archipelago/blob/tracker/worlds/tracker/docs/re-gen-passthrough.md
	@staticmethod
	def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
		# returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
		# we are using re_gen_passthrough over modifying the world here due to complexities with ER
		return slot_data
