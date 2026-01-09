""" split -n l/3 ./popular-names.txt """
import sys
import numpy as np

def main():
    if len(sys.argv) < 3: return
    n = int(sys.argv[1])
    with open(sys.argv[2]) as f:
        lines = np.array(f.readlines())
    
    for i, chunk in enumerate(np.array_split(lines, n)):
        with open(f"split_{i:02d}.txt", "w") as f_out:
            f_out.writelines(chunk)

if __name__ == "__main__":
    main()