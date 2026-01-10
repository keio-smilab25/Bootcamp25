from pathlib import Path

def main():
    data = Path("../popular-names.txt").read_bytes()
    print(data.count(b"\n"))

if __name__ == "__main__":
    main()


"""
(.venv) kayaharadaichi@Mac answer_py % python 10.py
2779
"""