from pathlib import Path

def main():
    in_dir = Path("../answers")
    col1 = (in_dir / "col1.txt").read_text(encoding="utf-8").splitlines()
    col2 = (in_dir / "col2.txt").read_text(encoding="utf-8").splitlines()

    merged = [f"{a}\t{b}" for a, b in zip(col1, col2)]

    out_path = in_dir / "col1_col2.txt"
    out_path.write_text("\n".join(merged) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
