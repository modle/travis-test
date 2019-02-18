import random
import json

fp = open('./data/races.txt')
races = json.loads(fp.read())
fp.close()

fp2 = open('./data/classes.txt')
classes = json.loads(fp2.read())
fp2.close()

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
