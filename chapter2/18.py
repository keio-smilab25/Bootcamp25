# 18.py
import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
# 3列目(インデックス2)で降順(ascending=False)ソート
sorted_df = df.sort_values(by=2, ascending=False)

print(sorted_df.head()) # 全量は多いので先頭のみ表示