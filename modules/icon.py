import random
import sys

icons = [
    "archmage",
    "crusader",
    "diabolist",
    "dwarf king",
    "elf queen",
    "emperor",
    "great gold wyrm",
    "high druid",
    "lich king",
    "orc lord",
    "priestess",
    "prince of shadows",
    "three"
]

relations = [
    "positive",
    "conflicted",
    "negative"
]

def main(num_icons):
    chosen_icons = []
    max_icons = 3

    if num_icons < 1:
        num_icons = 1

    if num_icons > max_icons:
        num_icons = 3

    while len(chosen_icons) < num_icons:
        icon_index = random.randint(0, len(icons)-1)
        relations_index = random.randint(0, len(relations)-1)
        icon = {"name": icons[icon_index], "relationship": relations[relations_index]}
        del icons[icon_index]
        chosen_icons.append(icon)

    return chosen_icons

if __name__ == "__main__":
    result = main(int(sys.argv[1]))
    print(result)

