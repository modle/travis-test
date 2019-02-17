import random
import json

fp = open('./data/classes.txt')
classes = json.loads(fp.read())
fp.close()

def main():

    target_class = classes[random.randint(0, len(classes)-1)]

    abilities = list(set().union(target_race["ability"], target_class["ability"]))

    result = {
        "class": target_class["name"],
        "abilities": abilities
    }

    return result


if __name__ == "__main__":
    print(main())

