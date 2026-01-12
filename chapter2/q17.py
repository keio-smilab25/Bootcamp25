import pandas as pd

df = pd.read_table('popular-names.txt', header=None)

names = df[0].unique()
names.sort()

print(names)