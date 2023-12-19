from Functions import to_from_json
import os


construction_parameters = {
    "w_anaerobic":
        {
            'value': 2798,
            'description': 'Wанаэр - объем анаэробной зоны, м3',
            'mod': 'in'
        },
    "w_anoxide":
        {
            'value': 8373,
            'description': 'Wанокс - объем аноксидной зоны, м3',
            'mod': 'in'
        },
    "w_aerobic":
        {
            'value': 10969,
            'description': 'Wаэр - объем аэробной зоны, м3',
            'mod': 'in'
        },
    "beta":
        {
            'value': 3,
            'description': 'b - b-фактор для реагентного удаления фосфора',
            'mod': 'in'
        },
    "f_tot":
        {
            'value': 2290,
            'description': 'Ftot - суммарная площадь поверхности вторичных отстойников, м2',
            'mod': 'in'
        },
    "h_set":
        {
            'value': 4.29,
            'description': 'Hset - глубина зоны отстаивания во вторичном отстойнике, м',
            'mod': 'in'
        },
    "k_ss":
        {
            'value': 0.4,
            'description': 'Kss - коэффициент использования объема вторичного отстойника',
            'mod': 'in'
        },
}
construction_parameters = to_from_json.from_json('construction_parameters')


if __name__ == '__main__':
    to_from_json.to_json([construction_parameters], 'construction_parameters', mode='b')
