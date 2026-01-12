import pandas as pd

df = pd.read_table('popular-names.txt', header=None)

counts = df[0].value_counts()

print(counts)