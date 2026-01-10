from pathlib import Path
import sys

def main():
    n = int(sys.argv[1])
    lines = Path("../popular-names.txt").read_text(encoding="utf-8").splitlines()

    out_dir = Path("../answers/split")
    out_dir.mkdir(parents=True, exist_ok=True)

    total = len(lines)
    q, r = divmod(total, n)

    idx = 0
    for i in range(n):
        size = q + (1 if i < r else 0)
        chunk = lines[idx:idx + size]
        (out_dir / f"split_{i:02d}.txt").write_text("\n".join(chunk) + "\n", encoding="utf-8")
        idx += size

if __name__ == "__main__":
    main()
