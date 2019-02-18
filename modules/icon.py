import random
import sys

fp = open('./data/icons.txt')
icon_data = fp.read().split("\n")
fp.close()

relations = ["positive", "conflicted", "negative"]

MAX_ICONS = 3
MIN_ICONS = 1

def main():
    # because we want to delete entries to avoid duplicates
    num_icons = random.randint(MIN_ICONS, MAX_ICONS)
    icons = icon_data.copy()
    chosen_icons = []

    while len(chosen_icons) < num_icons:
        icon_index = random.randint(0, len(icons)-1)
        relations_index = random.randint(0, len(relations)-1)
        icon = (icons[icon_index], relations[relations_index])
        # avoids duplicates
        del icons[icon_index]
        chosen_icons.append(icon)

    return chosen_icons

if __name__ == "__main__":
    result = main()
    print(result)
