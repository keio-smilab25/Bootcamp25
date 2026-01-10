from pathlib import Path
import sys

def main():
    n = int(sys.argv[1])
    lines = Path("../popular-names.txt").read_text(encoding="utf-8").splitlines()
    print("\n".join(lines[-n:]))

if __name__ == "__main__":
    main()


"""
(.venv) kayaharadaichi@Mac answer_py % python 15.py 5
Benjamin        M       13381   2018
Elijah  M       12886   2018
Lucas   M       12585   2018
Mason   M       12435   2018
Logan   M       12352   2018
"""