import json
from Configurations import config


def to_json(object_list, name, path='', mode='c'):
    if mode == "b":
        path = config.JSON_PATH + 'BaseJsons/'
    elif mode == 'c':
        path = config.JSON_PATH + 'CurrentJsons/'
    elif mode == 's':
        path = config.JSON_PATH + path
    total_object = dict()
    for obj in object_list:
        total_object.update(obj)
    # print(f'{path}{name}.json')
    with open(f'{path}{name}.json', 'w') as file:
        json.dump(total_object, file)
    file.close()


def from_json(name, path='', mode='c'):
    if mode == "b":
        path = config.JSON_PATH + 'BaseJsons/'
    elif mode == 'c':
        path = config.JSON_PATH + 'CurrentJsons/'
    elif mode == 'l':
        path = config.JSON_PATH + path
    with open(path + name + '.json', 'r') as file:
        obj = json.load(file)
    file.close()
    return obj
