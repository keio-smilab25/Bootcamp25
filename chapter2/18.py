""" sort -rnk 3 ./popular-names.txt """
import sys
import numpy as np

def main():
    if len(sys.argv) < 3: return
    col_num = int(sys.argv[1]) - 1 
    input_file = sys.argv[2]
    data = np.loadtxt(input_file, delimiter='\t', dtype=str)
    indices = np.argsort(data[:, col_num].astype(int))[::-1]
    
    for row in data[indices]:
        print("\t".join(row))

if __name__ == "__main__":
    main()