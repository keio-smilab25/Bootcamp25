""" tail -n 5 ./popular-names.txt """
import sys
import numpy as np

def main():
    if len(sys.argv) < 3: return
    n = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        lines = f.readlines()
        for line in lines[-n:]: print(line.strip())

if __name__ == "__main__":
    main()