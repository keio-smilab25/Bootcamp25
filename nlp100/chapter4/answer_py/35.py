from collections import Counter
from nlp30 import parse_mecab

def main():
    sentences = parse_mecab("../neko.txt.mecab")

    words = []
    for sent in sentences:
        for m in sent:
            if m["pos"] in ("空白", "補助記号"):
                continue
            words.append(m["surface"])

    counts = Counter(words)

    for word, cnt in counts.most_common():
        print(f"{word}\t{cnt}")

if __name__ == "__main__":
    main()