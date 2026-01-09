# 16.py
import sys
import math

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3

with open('popular-names.txt', 'r') as f:
    lines = f.readlines()

total_lines = len(lines)
chunk_size = math.ceil(total_lines / n)

for i in range(n):
    start = i * chunk_size
    end = start + chunk_size
    with open(f'split_{i}.txt', 'w') as out_f:
        out_f.writelines(lines[start:end])
    print(f'Created split_{i}.txt (lines {start} to {min(end, total_lines)})')