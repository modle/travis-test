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

MAX_ICONS = 3
MIN_ICONS = 1

def main(num_icons):
    chosen_icons = []

    if num_icons < MIN_ICONS:
        num_icons = MIN_ICONS

    if num_icons > MAX_ICONS:
        num_icons = MAX_ICONS

    while len(chosen_icons) < num_icons:
        icon_index = random.randint(0, len(icons)-1)
        relations_index = random.randint(0, len(relations)-1)
        icon = {icons[icon_index]: {"relationship": relations[relations_index]}}
        # avoids duplicates
        del icons[icon_index]
        chosen_icons.append(icon)

    return chosen_icons

if __name__ == "__main__":
    result = main(int(sys.argv[1]))
    print(result)

