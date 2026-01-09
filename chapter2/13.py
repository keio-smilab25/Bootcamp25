# 13.py
import pandas as pd

c1 = pd.read_csv('col1.txt', header=None)
c2 = pd.read_csv('col2.txt', header=None)

# concatで横方向(axis=1)に結合
merged = pd.concat([c1, c2], axis=1)
merged.to_csv('merged.txt', sep='\t', index=False, header=False)

# 確認のため表示
print(merged.head())