import logging
from typing import List, Union
from dataclasses import dataclass
from Options import Range, Toggle, DefaultOnToggle, PerGameCommonOptions, OptionSet, OptionError, Choice, Accessibility
from settings import Group, Bool
from random import Random
from .Locations import base_characters, moonspell_characters, foscari_characters, amogus_characters, guns_characters, \
    castlevania_characters, emerald_characters, normal_stages, bonus_stages, challenge_stages, moonspell_stages, \
    foscari_stages, amogus_stages, guns_stages, castlevania_stages, emerald_stages, secret_characters, \
    megalo_characters, unfair_characters, EUDAI

class GoalRequirement(Choice):
    """
    0 = Stage hunt (beat/loop all stages)
    1 = Kill Director (required ~75% of stages beaten)
    """
    display_name = "Goal Requirement"
    default = 0
    option_stage_hunt = 0
    option_director = 1


class ChestChecksPerStage(Range):
    """
    how many chest checks per stage
    from 5 to 10
    default: 7
    """
    default = 7
    range_start = 5
    range_end = 10


class EggInclusion(Choice):
    """
    how to include eggs:
    0 = fully disabled
    1 = locked behind an item
    2 = fully unlocked
    """
    display_name = "Egg Inclusion"
    default = 1
    option_disabled = 0
    option_locked_behind_item = 1
    option_unlocked = 2


class LockHyperBehindItem(Toggle):
    """
    Lock the `Hyper` gamemode behind an item
    """
    display_name = "Lock Hyper Behind Item"


class LockHurryBehindItem(Toggle):
    """
    Lock the `Hurry` gamemode behind an item
    This will lock `Beat with [character]` and `[stage] beaten` checks until hurry is found
    """
    display_name = "Lock Hurry Behind Item"


class LockArcanasBehindItem(Toggle):
    """
    Lock the `Arcanas` gamemode behind an item
    """
    display_name = "Lock Arcanas Behind Item"


class Enemysanity(Toggle):
    """
    the first kill of an enemy is a check
    """
    display_name = "Enemysanity"


class AllowSecretCharacters(DefaultOnToggle):
    """
    Allow for the use of secret characters:
    Exdash Exiviiq, Toastie, Smith IV, Random, Boon Marrabbio, Avatar Infernas, Minnah Mannarah, Leda, Cosmo Pavone, Peppino, Big Trouser, MissingN▯, Gains Boros, Gyorunton, Mask of the Red Death, Bats Bats Bats, Rose De Infernas, Scorej-Oni, Gyoruntin, Space Dette, Young Maria Renard, Familiar, Innocent Devil, Blue Crescent Moon Cornell, Ferryman, Master Librarian, Hammer, Wind, Jonathan & Charlotte, Charlotte & Jonathan, Stella & Loretta Lecarde, Loretta & Stella Lecarde, Stella Lecarde, Loretta Lecarde, Brauner, Soleil Belmont, Dario Bossi, Dmitrii Blinov, Celia Fortner, Graham Jones, Joachim Armster, Walter Bernhard, Carmilla, Count Olrox, Cave Troll, Fleaman, Axe Armor, Frozenshade, Succubus, Keremet, Alamaric Sniper, Blackmore, Malphas, Death, Galamoth, Megalo Elizabeth Bartley, Megalo Olrox, Megalo Death, Megalo Dracula, Chaos, Lolo, Hiss, Meow, and Purr, Kina, Imakoo, Malevolent Door Spirit
    """
    display_name = "Allow Secret Characters"


class AllowMegaloCharacters(Toggle):
    """
    Allow the use of megalo characters:
    Megalo Menya Moonspell, Megalo Syuuto Moonspell, Je-Ne-Viv, Megalo Impostor Rina, Megalo Elizabeth Bartley, Megalo Olrox, Megalo Death, Megalo Dracula
    """
    display_name = "Allow Megalo Characters"


class AllowUnfairCharacters(Toggle):
    """
    Allow the use of unfair characters:
    note: this also requires the host setting to be enabled
    Peppino, MissingN▯, Space Dette, Megalo Menya Moonspell, Ghost Lino, Fleaman, Megalo Death, Chaos
    """
    display_name = "Allow Unfair Characters"


class IncludedBaseCharacters(OptionSet):
    """
    Base characters to be randomized
    possible options:
    ["Antonio Belpaese", "Imelda Belpaese", "Pasqualina Belpaese", "Gennaro Belpaese", "Arca Ladonna", "Porta Ladonna", "Lama Ladonna", "Poe Ratcho", "Suor Clerici", "Dommario", "Krochi Freetto", "Christine Davain", "Pugnala Provola", "Giovanna Grana", "Poppea Pecorina", "Concetta Caciotta", "Mortaccio", "Yatta Cavallo", "Bianca Ramba", "O'Sole Meeo", "Sir Ambrojoe", "Iguana Gallo Valleto", "Divano Thelma", "Zi'Assunta Belpaese", "Exdash Exiviiq", "Toastie", "Smith IV", "Random", "Boon Marrabbio", "Avatar Infernas", "Minnah Mannarah", "Leda", "Cosmo Pavone", "Peppino", "Big Trouser", "MissingN▯", "Gains Boros", "Gyorunton", "Mask of the Red Death", "Queen Sigma", "Bat Robbert", "She-Moon Eeta", "Santa Ladonna", "Gazebo", "Space Dude", "Bats Bats Bats", "Rose De Infernas", "Scorej-Oni", "Gyoruntin", "Space Dette"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Base Characters"
    valid_keys = frozenset(base_characters + ["All"])
    default = "All"


class IncludedMoonspellCharacters(OptionSet):
    """
    Legacy of the Moonspell DLC characters to be randomized
    possible options:
    ["Miang Moonspell", "Menya Moonspell", "Syuuto Moonspell", "Babi-Onna", "McCoy-Oni", "Megalo Menya Moonspell", "Megalo Syuuto Moonspell", "Gav'Et-Oni"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Moonspell Characters"
    valid_keys = frozenset(moonspell_characters + ["All", "Random"])
    default = []


class IncludedFoscariCharacters(OptionSet):
    """
    Tides of the Foscari DLC characters to be randomized
    possible options:
    ["Eleanor Uziron", "Maruto Cuts", "Keitha Muort", "Luminaire Foscari", "Genevieve Gruyére", "Je-Ne-Viv", "Sammy", "Rottin'Ghoul"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Foscari Characters"
    valid_keys = frozenset(foscari_characters + ["All", "Random"])
    default = []


class IncludedAmongusCharacters(OptionSet):
    """
    Emergency Meeting DLC characters to be randomized
    possible options:
    ["Crewmate Dino", "Engineer Gino", "Ghost Lino", "Shapeshifter Nino", "Guardian Pina", "Impostor Rina", "Scientist Mina", "Horse", "Megalo Impostor Rina"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Amongus Characters"
    valid_keys = frozenset(amogus_characters + ["All", "Random"])
    default = []


class IncludedOperationGunsCharacters(OptionSet):
    """
    Operation Guns DLC characters to be randomized
    possible options:
    ["Bill Rizer", "Lance Bean", "Ariana", "Lucia Zero", "Brad Fang", "Browny", "Sheena Etranzi", "Probotector", "Stanley", "Newt Plissken", "Colonel Bahamut", "Simondo Belmont"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Operation Guns Characters"
    valid_keys = frozenset(guns_characters + ["All", "Random"])
    default = []


class IncludedCastlevaniaCharacters(OptionSet):
    """
    Ode to Castlevania DLC characters to be randomized
    possible options:
    ["Leon Belmont", "Sonia Belmont", "Trevor Belmont", "Christopher Belmont", "Simon Belmont", "Juste Belmont", "Richter Belmont", "Julius Belmont", "Grant Danasty", "Quincy Morris", "John Morris", "Jonathan Morris", "Maxim Kischine", "Henry", "Soma Cruz", "Vlad Tepes Dracula", "Charlotte Aulin", "Sypha Belnades", "Julia Laforeze", "Carrie Fernandez", "Yoko Belnades", "Rinaldo Gandolfi", "Mina Hakuba", "Elizabeth Bartley", "Alucard", "Reinhardt Schneider", "Eric Lecarde", "Isaac", "Hector", "Sara Trantoul", "Vincent Dorin", "Maria Renard", "Shanoa", "Albus", "Lisa Tepes", "Shaft", "Saint Germain", "Nathan Graves", "Cornell", "Barlowe", "Young Maria Renard", "Familiar", "Innocent Devil", "Blue Crescent Moon Cornell", "Ferryman", "Master Librarian", "Hammer", "Wind", "Jonathan & Charlotte", "Charlotte & Jonathan", "Stella & Loretta Lecarde", "Loretta & Stella Lecarde", "Stella Lecarde", "Loretta Lecarde", "Brauner", "Soleil Belmont", "Dario Bossi", "Dmitrii Blinov", "Celia Fortner", "Graham Jones", "Joachim Armster", "Walter Bernhard", "Carmilla", "Count Olrox", "Cave Troll", "Fleaman", "Axe Armor", "Frozenshade", "Succubus", "Keremet", "Alamaric Sniper", "Blackmore", "Malphas", "Death", "Galamoth", "Megalo Elizabeth Bartley", "Megalo Olrox", "Megalo Death", "Megalo Dracula", "Chaos"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Castlevania Characters"
    valid_keys = frozenset(castlevania_characters + ["All", "Random"])
    default = []


class IncludedEmeraldCharacters(OptionSet):
    """
    Emerald Diorama DLC characters to be randomized
    possible options:
    ["Tsunanori Mido", "Bonnie Blair", "Formina Franklyn", "Diva No. 5", "Ameya Aisling", "Siugnas", "Final Emperor", "Dolores", "Macha Alter Ego", "Lita Caryx", "Kugutsu", "Mr. S", "Lolo, Hiss, Meow, and Purr", "Kina", "Imakoo", "Malevolent Door Spirit"]
    "All" - adds all locations above
    "Random" - picks a random # of characters b/t list's max size / 2 and list's max size
    """
    display_name = "Included Emerald Characters"
    valid_keys = frozenset(emerald_characters + ["All", "Random"])
    default = []


class IncludedNormalStages(OptionSet):
    """
    Normal stages to be randomized
    possible options:
    ["Mad Forest", "Inlaid Library", "Dairy Plant", "Gallo Tower", "Cappella Magna"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Normal Stages"
    valid_keys = frozenset(normal_stages + ["All", "Random"])
    default = "All"


class IncludedBonusStages(OptionSet):
    """
    Bonus stages to be randomized
    possible options:
    ["Il Molise", "Moongolow", "Whiteout", "The Coop", "Space 54", "Carlo Cart"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Bonus Stages"
    valid_keys = frozenset(bonus_stages + ["All", "Random"])
    default = "All"


class IncludedChallengeStages(OptionSet):
    """
    Challenge stages to be randomized
    possible options:
    ["Green Acres", "The Bone Zone", "Boss Rash", "Eudaimonia M.", "Laborratory", "Bat Country", "Astral Stair", "Tiny Bridge", "Room 1665"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Challenge Stages"
    valid_keys = frozenset(challenge_stages + ["All", "Random"])
    default = "All"


class IncludedMoonspellStages(OptionSet):
    """
    Legacy of the Moonspell DLC stages to be randomized
    possible options:
    ["Mt.Moonspell"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Moonspell Stages"
    valid_keys = frozenset(moonspell_stages + ["All", "Random"])
    default = []


class IncludedFoscariStages(OptionSet):
    """
    Tides of the Foscari DLC stages to be randomized
    possible options:
    ["Lake Foscari", "Abyss Foscari"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Foscari Stages"
    valid_keys = frozenset(foscari_stages + ["All", "Random"])
    default = []


class IncludedAmongusStages(OptionSet):
    """
    Emergency Meeting DLC stages to be randomized
    possible options:
    ["Polus Replica"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Amongus Stages"
    valid_keys = frozenset(amogus_stages + ["All", "Random"])
    default = []


class IncludedOperationGunsStages(OptionSet):
    """
    Operation Guns DLC stages to be randomized
    possible options:
    ["Neo Galuga", "Hectic Highway"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Operation Guns Stages"
    valid_keys = frozenset(guns_stages + ["All", "Random"])
    default = []


class IncludedCastlevaniaStages(OptionSet):
    """
    Ode to Castlevania DLC stages to be randomized
    possible options:
    ["Ode to Castlevania"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Castlevania Stages"
    valid_keys = frozenset(castlevania_stages + ["All", "Random"])
    default = []


class IncludedEmeraldStages(OptionSet):
    """
    Emerald Diorama DLC stages to be randomized
    possible options:
    ["Emerald Diorama"]
    "All" - adds all locations above
    "Random" - picks a random # of stages b/t list's max size / 2 and list's max size
    """
    display_name = "Included Emerald Stages"
    valid_keys = frozenset(emerald_stages + ["All", "Random"])
    default = []


@dataclass
class VampireSurvivorsOptions(PerGameCommonOptions):
    goal_requirement: GoalRequirement
    chest_checks_per_stage: ChestChecksPerStage
    egg_inclusion: EggInclusion
    lock_hyper_behind_item: LockHyperBehindItem
    lock_hurry_behind_item: LockHurryBehindItem
    lock_arcanas_behind_item: LockArcanasBehindItem
    enemysanity: Enemysanity
    allow_secret_characters: AllowSecretCharacters
    allow_megalo_characters: AllowMegaloCharacters
    allow_unfair_characters: AllowUnfairCharacters
    included_base_characters: IncludedBaseCharacters
    included_moonspell_characters: IncludedMoonspellCharacters
    included_foscari_characters: IncludedFoscariCharacters
    included_amongus_characters: IncludedAmongusCharacters
    included_operation_guns_characters: IncludedOperationGunsCharacters
    included_castlevania_characters: IncludedCastlevaniaCharacters
    included_emerald_characters: IncludedEmeraldCharacters
    included_normal_stages: IncludedNormalStages
    included_bonus_stages: IncludedBonusStages
    included_challenge_stages: IncludedChallengeStages
    included_moonspell_stages: IncludedMoonspellStages
    included_foscari_stages: IncludedFoscariStages
    included_amongus_stages: IncludedAmongusStages
    included_operation_guns_stages: IncludedOperationGunsStages
    included_castlevania_stages: IncludedCastlevaniaStages
    included_emerald_stages: IncludedEmeraldStages

    def get_included_characters(self, world) -> List[str]:
        return (self.flatten_locations(world, base_characters, self.included_base_characters)
                + self.flatten_locations(world, moonspell_characters, self.included_moonspell_characters)
                + self.flatten_locations(world, foscari_characters, self.included_foscari_characters)
                + self.flatten_locations(world, amogus_characters, self.included_amongus_characters)
                + self.flatten_locations(world, guns_characters, self.included_operation_guns_characters)
                + self.flatten_locations(world, castlevania_characters, self.included_castlevania_characters)
                + self.flatten_locations(world, emerald_characters, self.included_emerald_characters))

    def get_included_stages(self, world) -> List[str]:
        return (self.flatten_locations(world, normal_stages, self.included_normal_stages)
                + self.flatten_locations(world, bonus_stages, self.included_bonus_stages)
                + self.flatten_locations(world, challenge_stages, self.included_challenge_stages)
                + self.flatten_locations(world, moonspell_stages, self.included_moonspell_stages)
                + self.flatten_locations(world, foscari_stages, self.included_foscari_stages)
                + self.flatten_locations(world, amogus_stages, self.included_amongus_stages)
                + self.flatten_locations(world, guns_stages, self.included_operation_guns_stages)
                + self.flatten_locations(world, castlevania_stages, self.included_castlevania_stages)
                + self.flatten_locations(world, emerald_stages, self.included_emerald_stages))

    def flatten_locations(self, world, list, self_list) -> List[str]:
        if "Random" in self_list:
            return world.random.sample(list, world.random.randint(int(len(list) / 2), len(list)))

        return list if "All" in self_list else [loc for loc in self_list if loc != "Random"]


class VampireSurvivorsSettings(Group):
    class AllowUnfairCharacters(Bool):
        """Allow the use of unfair characters"""

    allow_unfair_characters: Union[AllowUnfairCharacters, bool] = False


def check_options(world):
    options: VampireSurvivorsOptions = world.options
    settings: VampireSurvivorsSettings = world.settings
    characters = options.get_included_characters(world)
    stages = options.get_included_stages(world)

    if not options.allow_secret_characters:
        characters = [character for character in characters if character not in secret_characters]

    if not options.allow_megalo_characters:
        characters = [character for character in characters if character not in megalo_characters]

    if not settings.allow_unfair_characters and options.allow_unfair_characters:
        options.allow_unfair_characters = AllowUnfairCharacters(False)
        raise_yaml_error(world.player_name,
                         "`allow_unfair_characters` can not be enabled unless the host,yaml setting 'allow_unfair_characters' is also enabled")

    if not options.allow_unfair_characters:
        characters = [character for character in characters if character not in unfair_characters]

    if len(stages) == 0:
        raise_yaml_error(world.player_name, "You must have more than 0 stages included")

    if len(characters) == 0:
        raise_yaml_error(world.player_name, "You must have more than 0 eligible characters included")

    if EUDAI not in stages and options.goal_requirement == 1:
        stages.append(EUDAI)

    if len(stages) == 1 and stages[0] == EUDAI:
        raise_yaml_error(world.player_name, f"{EUDAI} CAN NOT BE YOUR ONLY STAGE")

    world.random.shuffle(characters)
    world.random.shuffle(stages)
    world.final_included_characters_list = characters
    world.final_included_stages_list = stages


def raise_yaml_error(player_name, error):
    raise OptionError(
        f"\n\n=== Vampire Survivors YAML ERROR ===\nVampire Survivors: {player_name} {error}, PLEASE FIX YOUR YAML\n\n")
