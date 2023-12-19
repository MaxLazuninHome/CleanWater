"""
Функция третьего эшелона расчитывает значения,
для которых необходимы входные данные,
а также значения из первого и второго эшелонов.
"""

from Functions.Echelones import first_echelon_function, second_echelon_function
from Functions.abbreviation import abbreviation
from InputData.TechnologicalParameters import technological_parameters
from InputData.SourceWater import source_water
from InputData.Constants import constants
from InputData.ConstructionParameters import construction_parameters
from OutputData.Calculate.ActiveSiltIncrease import active_silt_increase_results
from OutputData.PurifiedWaterQuality import purified_water_quality_results
from OutputData.Calculate.AnaerobicZone import anaerobic_results
from OutputData.Calculate.PhosphorusRemoval.PhosphorusRemovalBiomassIncrease \
    import phosphorus_removal_bimass_increase_results
from OutputData.Calculate.PhosphorusRemoval import phosphorus_removal_results
from OutputData.Calculate.AnoxideZone import anoxyde_results
from OutputData.Output import output_results
from OutputData.Calculate.AerobicZone.NitrficationVelocityCalculate import nitrification_velocity_calculate_results
from OutputData.Calculate.AerobicZone.NitrificationSecondStage import nitrification_second_stage_results
from OutputData.PurifiedWaterQuality import requirements_for_purified_water
from OutputData.Calculate.AerobicZone.NitrificationFirstStage import nitrification_first_stage_result
from OutputData.Calculate.PhosphorusRemoval.PhosphorusRemovalFAO import phosphorus_removal_fao_results
from OutputData.Calculate.PhosphorusRemoval.ChemicalPhosphorusRemoval import chemical_phosphorus_removal_results

v, d = abbreviation()
c = constants.constants
tp = technological_parameters.technological_parameters
cp = construction_parameters.construction_parameters
sw = source_water.source_water
nfsr = nitrification_first_stage_result.nitrification_first_stage_results
asir = active_silt_increase_results.active_silt_increase_results
pwqr = purified_water_quality_results.purified_water_quality_results
nvcr = nitrification_velocity_calculate_results.nitrification_velocity
nssr = nitrification_second_stage_results.nitrification_second_stage_results
cprr = chemical_phosphorus_removal_results.chemical_phosphorus_removal_results
prfaor = phosphorus_removal_fao_results.phosphorus_removal_fao_results
aar = anaerobic_results.anaerobic_results
axr = anoxyde_results.anoxide_results
our = output_results.output_results
rpw = requirements_for_purified_water.requirements_for_purified_water
prbir = phosphorus_removal_bimass_increase_results.biomass_increase_results
prr = phosphorus_removal_results.phosphorus_removal_results


def third_echelon():

    asir['p_common'][v] = tp['q_i'][v] * tp['a_extra'][v] + pwqr['a_t'][v] * sw['q'][v] / 1000

    asir['d_common'][v] = asir['p_common'][v] * (1 - tp['s'][v]) / sw['q'][v]

    prbir['p_not_fao'][v] = asir['p_common'][v] * (1 - tp['s'][v]) * c['k_p'][v] / 100
    prbir['delta_p_not_fao'][v] = 1000 * prbir['p_not_fao'][v] / sw['q'][v]
    prbir['p_out_b'][v] = prr['p_common'][v] - prfaor['delta_p_acetate'][v] - prbir['delta_p_not_fao'][v]

    axr['n_increase'][v] = asir['d_common'][v] * c['k_n'][v] * 1000

    nvcr['delta_n'][v] = axr['tkn'][v] - axr['n_increase'][v]
    nvcr['d_n'][v] = \
        (our['t_aerobic'][v] / nvcr['z_n'][v] - nvcr['delta_n'][v] + c['k_m_nh4'][v]) ** 2 + \
        4 * c['k_m_nh4'][v] * nvcr['delta_n'][v]        # TODO расхождение с эксель из за delta_n
    nvcr['x_1'][v] = (-(our['t_aerobic'][v] / nvcr['z_n'][v] - nvcr['delta_n'][v] + c['k_m_nh4'][v]) +
                      nvcr['d_n'][v] ** 0.5) / 2     #
    nvcr['x_2'][v] = (-(our['t_aerobic'][v] / nvcr['z_n'][v] - nvcr['delta_n'][v] + c['k_m_nh4'][v]) -
                      nvcr['d_n'][v] ** 0.5) / 2     #

    our['teta_aerobic'][v] = \
        cp['w_aerobic'][v] * tp['a_i'][v] / (tp['q_i'][v] * tp['a_extra'][v] + sw['q'][v] * pwqr['a_t'][v] / 1000)

    pwqr['n_no2_out'][v] = (tp['q_i'][v] * tp['a_extra'][v] * c['k_s_a2'][v] + pwqr['a_t'][v] /
                            1000 * sw['q'][v] * c['k_s_a2'][v] +
                            nssr['b_a2'][v] * cp['w_aerobic'][v] * tp['a_i'][v] * c['k_s_a2'][v]) / \
                           (nssr['mu_max_a2'][v] * tp['c_0'][v] / (tp['c_0'][v] + c['k_s_o2_a2'][v]) *
                            cp['w_aerobic'][v] * tp['a_i'][v] - tp['q_i'][v] * tp['a_extra'][v] - pwqr['a_t'][v] /
                            1000 * sw['q'][v] - nssr['b_a2'][v] * cp['w_aerobic'][v] * tp['a_i'][v])
    pwqr['nitrite_ion'][v] = pwqr['n_no2_out'][v] * c['s_metr_n_nitrite_ion'][v]

    if (prr['p_common'][v] - prfaor['delta_p_acetate'][v] -
       prbir['delta_p_not_fao'][v] - cprr['delta_p_chemical'][v]) > 0.2:
        pwqr['p_po4_out'][v] = prr['p_common'][v] - prfaor['delta_p_acetate'][v] - \
                               prbir['delta_p_not_fao'][v] - cprr['delta_p_chemical'][v]
    else:
        pwqr['p_po4_out'][v] = 0.2


if __name__ == '__main__':
    first_echelon_function.first_echelon()
    second_echelon_function.second_echelon()
    third_echelon()

    print(f"{round(asir['p_common'][v]) :<10}{asir['p_common'][d]}")
    print(f"{round(asir['d_common'][v], 2) :<10}{asir['d_common'][d]}")
    print(f"{round(prbir['p_not_fao'][v]) :<10}{prbir['p_not_fao'][d]}")
    print(f"{round(prbir['delta_p_not_fao'][v], 2) :<10}{prbir['delta_p_not_fao'][d]}")
    print(f"{round(prbir['p_out_b'][v], 2) :<10}{prbir['p_out_b'][d]}")
    print(f"{round(axr['n_increase'][v], 1) :<10}{axr['n_increase'][d]}")
    print(f"{round(nvcr['delta_n'][v], 4) :<10}{nvcr['delta_n'][d]}")
    print(f"{round(nvcr['d_n'][v], 3) :<10}{nvcr['d_n'][d]}")
    print(f"{round(nvcr['x_1'][v], 2) :<10}{nvcr['x_1'][d]}")
    print(f"{round(nvcr['x_2'][v], 2) :<10}{nvcr['x_2'][d]}")
    print(f"{round(our['teta_aerobic'][v], 1) :<10}{nssr['teta_aerobic'][d]}")
    print(f"{round(pwqr['n_no2_out'][v], 2) :<10}{pwqr['n_no2_out'][d]}")
    print(f"{round(pwqr['nitrite_ion'][v], 2) :<10}{pwqr['nitrite_ion'][d]}")
    print(f"{round(pwqr['p_po4_out'][v], 2) :<10}{pwqr['p_po4_out'][d]}")
