import MeCab

FILENAME = "./neko.txt"

def q30():
    mecab = MeCab.Tagger()
    with open(FILENAME, "r", encoding="utf-8") as f:
        text = f.read()
    result = mecab.parse(text)

    sentences = []
    mophs = []

    for line in result.splitlines():
        if line == "EOS" or line.strip() == "":
            if mophs:
                sentences.append(mophs)
                mophs = []
            continue

        parts = line.split("\t")
        if len(parts) <5 :
            continue

        pos_info = parts[4].split("-")

        morph = {
            "surface": parts[0],
            "base": parts[3],
            "pos": pos_info[0],
            "pos1": pos_info[1] if len(pos_info) > 1 else ""
        }
        mophs.append(morph)

    return sentences

def main():
    print(q30())

if __name__ == "__main__":
    main()