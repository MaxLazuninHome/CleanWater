from OutputData.Output import output_results
from Functions import functions, abbreviation
from OutputData.PurifiedWaterQuality import purified_water_quality_results
import pprint


functions.calculate_zones()

tmp_output_data = dict()
tmp_output_data.update(output_results.output_results)
tmp_output_data.update(purified_water_quality_results.purified_water_quality_results)

output_data = {
    'name': 'output_data',
    'value': tmp_output_data
}


# our, pwqr = abbreviation.load_output_data()
#
# output_results = {
#     'name': 'output_data',
#     'value': our
# }
# purified_water_quality_results = {
#     'name': 'purified_water_quality_results',
#     'value': pwqr
# }

# def set_output_values():


