""" expand -t 1 ./popular-names.txt """

import sys
import numpy as np

def main():
    if len(sys.argv) < 2: return
    with open(sys.argv[1]) as f:
        for line in f:
            print(line.replace('\t', ' '), end='')

if __name__ == "__main__":
    main()

"""
% uv run ./11.py ./popular-names.txt > 11py.txt
% expand -t 1 ./popular-names.txt > 11uni.txt  
% diff ./11py.txt ./11uni.txt
% 
"""