"""
Завершающий эшелон формул,
использующий в себе подстроенные значения для двух циклических переменных,
расчитанных в circle_echelon
"""

from math import exp
from Functions.Echelones import first_echelon_function, second_echelon_function, \
    third_echelon_function, circle_echelone_function
from Functions.abbreviation import abbreviation
from InputData.Constants import constants
from InputData.SourceWater import source_water
from InputData.ConstructionParameters import construction_parameters
from InputData.TechnologicalParameters import technological_parameters
from OutputData.Calculate.AnaerobicZone import anaerobic_results
from OutputData.PurifiedWaterQuality import purified_water_quality_results, requirements_for_purified_water
from OutputData.Calculate.AerobicZone.NitrficationVelocityCalculate import nitrification_velocity_calculate_results
from OutputData.Calculate.AerobicZone.OrganicSubstancesOxidation import organic_substances_oxidation_results
from OutputData.Calculate.AerobicZone.NitrificationFirstStage import nitrification_first_stage_result
from OutputData.Calculate.ActiveSiltIncrease import active_silt_increase_results
from OutputData.Calculate.AnoxideZone import anoxyde_results
from OutputData.Output import output_results


v, d = abbreviation()
pwqr = purified_water_quality_results.purified_water_quality_results
nvcr = nitrification_velocity_calculate_results.nitrification_velocity
nfsr = nitrification_first_stage_result.nitrification_first_stage_results
osor = organic_substances_oxidation_results.organic_substances_oxidation
asir = active_silt_increase_results.active_silt_increase_results
rpw = requirements_for_purified_water.requirements_for_purified_water
axr = anoxyde_results.anoxide_results
our = output_results.output_results
aar = anaerobic_results.anaerobic_results
sw = source_water.source_water
cp = construction_parameters.construction_parameters
tp = technological_parameters.technological_parameters
c = constants.constants


def fourth_echelon():
    axr['r_denitrification'][v] = (exp((sw['temperature'][v] - 20) * c['hi_denitrification'][v])) * \
                                      (((c['mu_max_d_20'][v] / c['y_d'][v]) *
                                        (pwqr['n_no3_out'][v] / (pwqr['n_no3_out'][v] + c['k_s_no3'][v])) *
                                        (axr['l_anoxide_diluted_out'][v] /
                                         (axr['l_anoxide_diluted_out'][v] + c['k_s_bod'][v])) *
                                        (c['k_s_o2_no3'][v] / (c['k_s_o2_no3'][v] + tp['c_0_anoxide'][v]))) -
                                       c['b_d_20'][v]) * axr['x_b'][v]
    axr['ro_denitrification'][v] = axr['r_denitrification'][v] * 1000 / 24 / tp['a_i'][v] / (1 - tp['s'][v])


    our['teta_a1'][v] = 1 / ((nfsr['mu_max_a1'][v] *
                             (rpw['n_ammonium_out_req'][v] / (rpw['n_ammonium_out_req'][v] + c['k_s_a1'][v])) *
                             (tp['c_0'][v] / (tp['c_0'][v] + c['k_s_o2_a1'][v])) *
                             (our['s_nitrification'][v] / (our['s_nitrification'][v] + c['k_s_alc_a1'][v]))) -
                             nfsr['b_a1'][v])  # Расхождение +0,1

    pwqr['ammonium_ion'][v] = pwqr['n_ammonium_out'][v] * c['s_metr_n_ammonium_ion'][v]
    pwqr['nitrate_ion'][v] = pwqr['n_no3_out'][v] * c['s_metr_n_nitrate_ion'][v]

    asir['k_g_common'][v] = asir['p_common'][v] * 1000 / (sw['l_in'][v] - pwqr['l_out'][v]) / sw['q'][v]



if __name__ == '__main__':
    first_echelon_function.first_echelon()
    second_echelon_function.second_echelon()
    third_echelon_function.third_echelon()
    circle_echelone_function.circle_echelone(10)
    fourth_echelon()

    print(f"{round(axr['r_denitrification'][v], 3) :<10}{axr['r_denitrification'][d]}")
    print(f"{round(axr['ro_denitrification'][v], 1):<10}{axr['ro_denitrification'][d]}")
    print(f"{round(our['teta_a1'][v], 2) :<10}{our['teta_a1'][d]}")
    print(f"{round(pwqr['ammonium_ion'][v], 2) :<10}{pwqr['ammonium_ion'][d]}")
    print(f"{round(pwqr['nitrate_ion'][v], 2) :<10}{pwqr['nitrate_ion'][d]}")
    print(f"{round(asir['k_g_common'][v], 2) :<10}{asir['k_g_common'][d]}")

