# from InputData.SourceWater.source_water import source_water
import numpy as np
import pandas as pd
import os


generated_values = []
columns = []
df = pd.DataFrame()

for el in source_water:
    columns.append(el)
    delta = source_water[el]['value'] * 0.1
    new_value = np.random.uniform(source_water[el]['value']-delta, source_water[el]['value']+delta, 100)
    df[el] = new_value

print(os.getcwd())

df.to_csv('test_dynamics.csv')
writer = pd.ExcelWriter(f'{os.getcwd()}/test_dynamics.xlsx')
df.to_excel(excel_writer=writer)
writer.close()

new_df = pd.read_csv('test_dynamics.csv', index_col=0)
new_df.drop(index=0, axis=1, inplace=True)
print(new_df)
