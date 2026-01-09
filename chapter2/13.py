""" paste ./col1.txt ./col2.txt """
import sys
import numpy as np

def main():
    if len(sys.argv) < 3: return
    c1 = np.loadtxt(sys.argv[1], dtype=str, ndmin=1)
    c2 = np.loadtxt(sys.argv[2], dtype=str, ndmin=1)

    merged = np.column_stack((c1, c2))
    for row in merged:
        print(f"{row[0]}\t{row[1]}")

if __name__ == "__main__":
    main()