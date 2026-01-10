from pathlib import Path

def main():
    text = Path("../popular-names.txt").read_text(encoding="utf-8").replace("\t", " ")
    out_path = Path("../answers/11.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()