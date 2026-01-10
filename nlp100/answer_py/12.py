from pathlib import Path

def main():
    in_path = Path("../popular-names.txt")
    out_dir = Path("../answers")
    out_dir.mkdir(parents=True, exist_ok=True)

    col1_lines = []
    col2_lines = []

    for line in in_path.read_text(encoding="utf-8").splitlines():
        cols = line.split("\t")
        col1_lines.append(cols[0] if len(cols) > 0 else "")
        col2_lines.append(cols[1] if len(cols) > 1 else "")

    (out_dir / "col1.txt").write_text("\n".join(col1_lines) + "\n", encoding="utf-8")
    (out_dir / "col2.txt").write_text("\n".join(col2_lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
