import pandas as pd
import sys

N = int(sys.argv[1])
df = pd.read_table('popular-names.txt', header=None)

print(df.tail(N))