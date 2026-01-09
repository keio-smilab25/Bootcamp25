# 17.py
import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
# unique()で重複排除し、sort_values()でソート
unique_names = df[0].unique()
unique_names.sort()

for name in unique_names:
    print(name)