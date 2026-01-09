# 14.py
import sys
import pandas as pd

# コマンドライン引数がなければデフォルト5
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
print(df.head(n))