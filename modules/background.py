import random

fp = open('./data/backgrounds.txt')
background_data = fp.read().split("\n")
fp.close()

MAX_BACKGROUNDS = 4
MIN_BACKGROUNDS = 1

def main():
    backgrounds = background_data.copy()
    chosen_backgrounds = []

    num_backgrounds = random.randint(MIN_BACKGROUNDS, MAX_BACKGROUNDS)

    while len(chosen_backgrounds) <= num_backgrounds:
        index = random.randint(0, len(backgrounds)-1)
        background = backgrounds[index]
        # avoids duplicates
        del backgrounds[index]
        chosen_backgrounds.append(background)

    return chosen_backgrounds

if __name__ == "__main__":
    result = main()
    print(result)
