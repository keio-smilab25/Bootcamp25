import sys
import pandas as pd
import numpy as np

N = int(sys.argv[1])
df = pd.read_table('popular-names.txt', header=None)

index_chunks = np.array_split(df.index, N)

for i, idx in enumerate(index_chunks):
    chunk = df.iloc[idx]
    
    filename = f'split_{i}.txt'
    chunk.to_csv(filename, sep='\t', header=False, index=False)