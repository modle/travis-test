import random

races = [
    {"name": "Human", "ability": ["any"]},
    {"name": "Dwarf", "ability": ["con", "wis"]},
    {"name": "Dark Elf", "ability": ["dex", "cha"]},
    {"name": "High Elf", "ability": ["int", "cha"]},
    {"name": "Wood Elf", "ability": ["dex", "wis"]},
    {"name": "Gnome", "ability": ["dex", "int"]},
    {"name": "Half-elf", "ability": ["con", "cha"]},
    {"name": "Half-orc", "ability": ["str", "dex"]},
    {"name": "Halfling", "ability": ["con", "dex"]},
    {"name": "Dragonic/Dragonspawn", "ability": ["str", "cha"]},
    {"name": "Holy One/Aasimar", "ability": ["wis", "cha"]},
    {"name": "Forgeborn/Dwarf-forged", "ability": ["str", "con"]},
    {"name": "Tiefling/Demontouched", "ability": ["str", "int"]},
]

classes = [
    {"name": "barbarian", "ability": ["str", "con"]},
    {"name": "bard", "ability": ["dex", "cha"]},
    {"name": "chaos mage", "ability": ["int", "cha"]},
    {"name": "cleric", "ability": ["str", "wis"]},
    {"name": "commander", "ability": ["str", "cha"]},
    {"name": "druid", "ability": ["str", "dex", "wis"]},
    {"name": "fighter", "ability": ["str", "con"]},
    {"name": "monk", "ability": ["str", "dex", "wis"]},
    {"name": "necromancer", "ability": ["int", "cha"]},
    {"name": "occultist", "ability": ["int", "wis"]},
    {"name": "paladin", "ability": ["str", "cha"]},
    {"name": "ranger", "ability": ["str", "dex"]},
    {"name": "rogue", "ability": ["dex", "cha"]},
    {"name": "sorcerer", "ability": ["cha", "con"]},
    {"name": "wizard", "ability": ["int", "wis"]}
]


def main():
    target_race = races[random.randint(0, len(races)-1)]
    target_class = classes[random.randint(0, len(classes)-1)]

    abilities = list(set().union(target_race["ability"], target_class["ability"]))

    result = {
        "race": target_race["name"],
        "class": target_class["name"],
        "abilities": abilities
    }

    return result


if __name__ == "__main__":
    print(main())

