from Functions.Echelones import fourth_echelon_function
from Functions.Echelones import circle_echelone_function
from Functions.Echelones import third_echelon_function
from Functions.Echelones import second_echelon_function
from Functions.Echelones import first_echelon_function
from Functions.abbreviation import abbreviation
from Functions.set_values import save_values
v, d = abbreviation()


def complete_calculate():

    first_echelon_function.first_echelon()
    second_echelon_function.second_echelon()
    third_echelon_function.third_echelon()
    circle_echelone_function.circle_echelone(10)
    fourth_echelon_function.fourth_echelon()


if __name__ == '__main__':
    print('Расчёт успешен')
