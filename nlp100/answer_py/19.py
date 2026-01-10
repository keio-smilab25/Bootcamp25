from pathlib import Path
from collections import Counter

def main():
    lines = Path("../popular-names.txt").read_text(encoding="utf-8").splitlines()
    col1 = [line.split("\t")[0] for line in lines if line]

    counts = Counter(col1)
    ordered = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    out_path = Path("../answers/19.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(name for name, _ in ordered) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
