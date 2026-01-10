from pathlib import Path

def main():
    lines = Path("../popular-names.txt").read_text(encoding="utf-8").splitlines()
    col1_set = sorted({line.split("\t")[0] for line in lines if line})

    out_path = Path("../answers/17.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(col1_set) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
