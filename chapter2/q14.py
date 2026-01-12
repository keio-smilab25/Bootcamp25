import sys
import pandas as pd

N = int(sys.argv[1])
df = pd.read_table('popular-names.txt', header=None)
print(df.head(N))