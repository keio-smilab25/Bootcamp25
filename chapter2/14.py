""" head -n 5 ./popular-names.txt """
import sys
import numpy as np

def main():
    if len(sys.argv) < 3: return
    n = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        for i, line in enumerate(f):
            if i < n: print(line.strip())
            else: break

if __name__ == "__main__":
    main()