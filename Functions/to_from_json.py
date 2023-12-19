import json
from Configurations import config


def to_json(object_list, name, mode='c'):
    path = config.JSON_PATH + ('BaseJsons/' if mode == 'b' else 'CurrentJsons/')
    total_object = dict()
    for obj in object_list:
        total_object.update(obj)
    with open(f'{path}{name}.json', 'w') as file:
        json.dump(total_object, file)
    file.close()


def from_json(name, mode='c'):
    path = config.JSON_PATH + ('BaseJsons/' if mode == 'b' else 'CurrentJsons/')
    with open(path + name + '.json', 'r') as file:
        obj = json.load(file)
    file.close()
    return obj
