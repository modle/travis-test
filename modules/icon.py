import random
import sys

fp = open('./data/icons.txt')
icon_data = fp.read().split("\n")
fp.close()

relations = ["positive", "conflicted", "negative"]

MAX_ICONS = 3
MIN_ICONS = 2
POINTS = 3

def main():
    # because we want to delete entries to avoid duplicates
    num_icons = random.randint(MIN_ICONS, MAX_ICONS)
    icons = icon_data.copy()
    chosen_icons = []

    assigned_points = 0

    while len(chosen_icons) < num_icons:
        icon_index = random.randint(0, len(icons)-1)
        relations_index = random.randint(0, len(relations)-1)
        icon_points = get_points(len(chosen_icons), num_icons, assigned_points)
        assigned_points += icon_points
        icon = (icons[icon_index], relations[relations_index], 'points: {}'.format(icon_points))
        # avoids duplicates
        del icons[icon_index]
        chosen_icons.append(icon)

    return chosen_icons

def get_points(current_icon, total_icons, assigned_points):
    if total_icons == 3:
        return 1
    if total_icons == 2:
        if current_icon == 0:
            return random.randint(1, 2)
        else:
            return POINTS - assigned_points

if __name__ == "__main__":
    result = main()
    print(result)
