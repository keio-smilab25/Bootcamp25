from pathlib import Path

def main():
    lines = Path("../popular-names.txt").read_text(encoding="utf-8").splitlines()

    def key(line: str) -> int:
        return int(line.split("\t")[2])

    sorted_lines = sorted(lines, key=key, reverse=True)

    out_path = Path("../answers/18.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(sorted_lines) + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
