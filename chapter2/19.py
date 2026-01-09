""" cut -f 1 ./popular-names.txt | sort | uniq -c | sort -rn """
import sys
import numpy as np

def main():
    if len(sys.argv) < 2: return
    col1 = np.loadtxt(sys.argv[1], delimiter='\t', dtype=str, usecols=0)
    names, counts = np.unique(col1, return_counts=True)
    indices = np.argsort(counts)[::-1]
    for i in indices:
        print(f"{counts[i]:>4} {names[i]}")

if __name__ == "__main__":
    main()