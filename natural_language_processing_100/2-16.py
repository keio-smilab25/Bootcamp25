import math
import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 1

filename = "popular-names.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

total_lines = len(lines)
unit = math.ceil(total_lines / n)

for i in range(n):
    chunk = lines[i * unit : (i + 1) * unit]

    output_file = f"split_{i}.txt"
    with open(output_file, "w", encoding="utf-8") as f_out:
        f_out.writelines(chunk)

# UNIX command:
# split -n N popular-names.txt split_
