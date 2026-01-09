""" cut -f 1 ./popular-names.txt | sort | uniq """
import sys
import numpy as np

def main():
    if len(sys.argv) < 2: return
    n = int(sys.argv[1]) - 1
    col1 = np.loadtxt(sys.argv[2], delimiter='\t', dtype=str, usecols=n)
    for name in np.unique(col1):
        print(name)

if __name__ == "__main__":
    main()