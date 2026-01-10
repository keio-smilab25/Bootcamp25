from pathlib import Path
import sys

def main():
    n = int(sys.argv[1])
    lines = Path("../popular-names.txt").read_text(encoding="utf-8").splitlines()
    print("\n".join(lines[:n]))

if __name__ == "__main__":
    main()


"""
(.venv) kayaharadaichi@Mac answer_py % python 14.py 5
Mary    F       7065    1880
Anna    F       2604    1880
Emma    F       2003    1880
Elizabeth       F       1939    1880
Minnie  F       1746    1880
"""