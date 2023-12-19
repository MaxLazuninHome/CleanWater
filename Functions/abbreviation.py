from Functions.to_from_json import from_json

def abbreviation():
    d = 'description'
    v = 'value'
    return v, d


def load_input_data(mode='c'):
    c = from_json('constants', mode=mode)
    sw = from_json('source_water', mode=mode)
    tp = from_json('technological_parameters', mode=mode)
    cp = from_json('construction_parameters', mode=mode)
    return c, sw, tp, cp


def load_output_data(mode='c'):
    our = from_json('output_data', mode=mode)
    pwqr = from_json('purified_water_quality_results', mode=mode)
    return our, pwqr


