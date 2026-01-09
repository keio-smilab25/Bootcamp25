""" wc -l ./popular-names.txt """

import sys
import numpy as np

def main():
    if len(sys.argv) < 2: return
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        print(len(lines))

if __name__ == "__main__":
    main()

"""
% uv run ./10.py ./popular-names.txt
2780
% wc -l ./popular-names.txt      
    2779 ./popular-names.txt
"""