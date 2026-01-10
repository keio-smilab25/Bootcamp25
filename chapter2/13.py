import pandas as pd

col1 = pd.read_table('col1.txt', header=None)
col2 = pd.read_table('col2.txt', header=None)

merged = pd.concat([col1, col2], axis=1)

merged.to_csv('merged.txt', sep='\t', index=False, header=False)
