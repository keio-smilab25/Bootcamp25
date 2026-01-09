# 19.py
import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
# value_counts() はデフォルトで頻度降順になる
counts = df[0].value_counts()

print(counts.head())