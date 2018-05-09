import json


def random():
    print("Hi")


def abc():
    with open('new.json','r') as r:
        print(json.load(r))

