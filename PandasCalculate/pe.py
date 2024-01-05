import pandas as pd
from Configurations import config

df = pd.read_excel(config.EXCEL_PATH + '/test.xlsx')
print(type(df.keys()[0]))