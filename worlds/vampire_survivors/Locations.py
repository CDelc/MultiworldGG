from typing import List
from .EnemyList import enemy_map

base_characters = ["Antonio Belpaese", "Imelda Belpaese", "Pasqualina Belpaese", "Gennaro Belpaese", "Arca Ladonna",
                   "Porta Ladonna", "Lama Ladonna", "Poe Ratcho", "Suor Clerici", "Dommario", "Krochi Freetto",
                   "Christine Davain", "Pugnala Provola", "Giovanna Grana", "Poppea Pecorina", "Concetta Caciotta",
                   "Mortaccio", "Yatta Cavallo", "Bianca Ramba", "O'Sole Meeo", "Sir Ambrojoe", "Iguana Gallo Valleto",
                   "Divano Thelma", "Zi'Assunta Belpaese", "Exdash Exiviiq", "Toastie", "Smith IV", "Random",
                   "Boon Marrabbio", "Avatar Infernas", "Minnah Mannarah", "Leda", "Cosmo Pavone", "Peppino",
                   "Big Trouser", "MissingN▯", "Gains Boros", "Gyorunton", "Mask of the Red Death", "Queen Sigma",
                   "Bat Robbert", "She-Moon Eeta", "Santa Ladonna", "Gazebo", "Space Dude", "Bats Bats Bats",
                   "Rose De Infernas", "Scorej-Oni", "Gyoruntin", "Space Dette"]

moonspell_characters = ["Miang Moonspell", "Menya Moonspell", "Syuuto Moonspell", "Babi-Onna", "McCoy-Oni",
                        "Megalo Menya Moonspell", "Megalo Syuuto Moonspell", "Gav'Et-Oni"]

foscari_characters = ["Eleanor Uziron", "Maruto Cuts", "Keitha Muort", "Luminaire Foscari", "Genevieve Gruyére",
                      "Je-Ne-Viv", "Sammy", "Rottin'Ghoul"]

amogus_characters = ["Crewmate Dino", "Engineer Gino", "Ghost Lino", "Shapeshifter Nino", "Guardian Pina",
                     "Impostor Rina", "Scientist Mina", "Horse", "Megalo Impostor Rina"]

guns_characters = ["Bill Rizer", "Lance Bean", "Ariana", "Lucia Zero", "Brad Fang", "Browny", "Sheena Etranzi",
                   "Probotector", "Stanley", "Newt Plissken", "Colonel Bahamut", "Simondo Belmont"]

castlevania_characters = ["Leon Belmont", "Sonia Belmont", "Trevor Belmont", "Christopher Belmont", "Simon Belmont",
                          "Juste Belmont", "Richter Belmont", "Julius Belmont", "Grant Danasty", "Quincy Morris",
                          "John Morris", "Jonathan Morris", "Maxim Kischine", "Henry", "Soma Cruz",
                          "Vlad Tepes Dracula", "Charlotte Aulin", "Sypha Belnades", "Julia Laforeze",
                          "Carrie Fernandez", "Yoko Belnades", "Rinaldo Gandolfi", "Mina Hakuba", "Elizabeth Bartley",
                          "Alucard", "Reinhardt Schneider", "Eric Lecarde", "Isaac", "Hector", "Sara Trantoul",
                          "Vincent Dorin", "Maria Renard", "Shanoa", "Albus", "Lisa Tepes", "Shaft", "Saint Germain",
                          "Nathan Graves", "Cornell", "Barlowe", "Young Maria Renard", "Familiar", "Innocent Devil",
                          "Blue Crescent Moon Cornell", "Ferryman", "Master Librarian", "Hammer", "Wind",
                          "Jonathan & Charlotte", "Charlotte & Jonathan", "Stella & Loretta Lecarde",
                          "Loretta & Stella Lecarde", "Stella Lecarde", "Loretta Lecarde", "Brauner", "Soleil Belmont",
                          "Dario Bossi", "Dmitrii Blinov", "Celia Fortner", "Graham Jones", "Joachim Armster",
                          "Walter Bernhard", "Carmilla", "Count Olrox", "Cave Troll", "Fleaman", "Axe Armor",
                          "Frozenshade", "Succubus", "Keremet", "Alamaric Sniper", "Blackmore", "Malphas", "Death",
                          "Galamoth", "Megalo Elizabeth Bartley", "Megalo Olrox", "Megalo Death", "Megalo Dracula",
                          "Chaos"]

emerald_characters = ["Tsunanori Mido", "Bonnie Blair", "Formina Franklyn", "Diva No. 5", "Ameya Aisling", "Siugnas",
                      "Final Emperor", "Dolores", "Macha Alter Ego", "Lita Caryx", "Kugutsu", "Mr. S",
                      "Lolo, Hiss, Meow, and Purr", "Kina", "Imakoo", "Malevolent Door Spirit"]

all_characters = base_characters + moonspell_characters + foscari_characters + amogus_characters + guns_characters + castlevania_characters + emerald_characters

normal_stages = ["Mad Forest", "Inlaid Library", "Dairy Plant", "Gallo Tower", "Cappella Magna"]
bonus_stages = ["Il Molise", "Moongolow", "Whiteout", "The Coop", "Space 54", "Carlo Cart"]

EUDAI = "Eudaimonia M."
challenge_stages = ["Green Acres", "The Bone Zone", "Boss Rash", "Laborratory", "Bat Country", "Astral Stair",
                    "Tiny Bridge", "Room 1665", EUDAI]

moonspell_stages = ["Mt.Moonspell"]
foscari_stages = ["Lake Foscari", "Abyss Foscari"]
amogus_stages = ["Polus Replica"]
guns_stages = ["Neo Galuga", "Hectic Highway"]
castlevania_stages = ["Ode to Castlevania"]
emerald_stages = ["Emerald Diorama"]

all_stages: List[
    str] = normal_stages + bonus_stages + challenge_stages + moonspell_stages + foscari_stages + amogus_stages + guns_stages + castlevania_stages + emerald_stages

# EXCLUDERS
secret_characters = ["Exdash Exiviiq", "Toastie", "Smith IV", "Random", "Boon Marrabbio", "Avatar Infernas",
                     "Minnah Mannarah", "Leda", "Cosmo Pavone", "Peppino", "Big Trouser", "MissingN▯", "Gains Boros",
                     "Gyorunton", "Mask of the Red Death", "Bats Bats Bats", "Rose De Infernas", "Scorej-Oni",
                     "Gyoruntin", "Space Dette", "Young Maria Renard", "Familiar", "Innocent Devil",
                     "Blue Crescent Moon Cornell", "Ferryman", "Master Librarian", "Hammer", "Wind",
                     "Jonathan & Charlotte", "Charlotte & Jonathan", "Stella & Loretta Lecarde",
                     "Loretta & Stella Lecarde", "Stella Lecarde", "Loretta Lecarde", "Brauner", "Soleil Belmont",
                     "Dario Bossi", "Dmitrii Blinov", "Celia Fortner", "Graham Jones", "Joachim Armster",
                     "Walter Bernhard", "Carmilla", "Count Olrox", "Cave Troll", "Fleaman", "Axe Armor", "Frozenshade",
                     "Succubus", "Keremet", "Alamaric Sniper", "Blackmore", "Malphas", "Death", "Galamoth",
                     "Megalo Elizabeth Bartley", "Megalo Olrox", "Megalo Death", "Megalo Dracula", "Chaos",
                     "Lolo, Hiss, Meow, and Purr", "Kina", "Imakoo", "Malevolent Door Spirit"]

megalo_characters = ["Megalo Menya Moonspell", "Megalo Syuuto Moonspell", "Je-Ne-Viv", "Megalo Impostor Rina",
                     "Megalo Elizabeth Bartley", "Megalo Olrox", "Megalo Death", "Megalo Dracula"]

unfair_characters = ["Peppino", "MissingN▯", "Space Dette", "Megalo Menya Moonspell", "Ghost Lino", "Fleaman",
                     "Megalo Death", "Sammy", "Chaos"]

location_dictionary: List[str] = [
    *[f"{stage} Beaten" for stage in all_stages],
    *[f"Beat with {character}" for character in all_characters],
    *[f"Open Chest #{i + 1} on {stage}" for i in range(10) for stage in all_stages],
    *[f"Kill {key}" for key, value in enemy_map.items()]
]

# Extra
non_special_characters = [character for character in all_characters if
                          character not in secret_characters and character not in megalo_characters and character not in unfair_characters]
