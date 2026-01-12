import matplotlib.pyplot as plt
import japanize_matplotlib
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
    top10 = counts.most_common(10)

    labels = [w for w, _ in top10]
    values = [c for _, c in top10]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.xlabel("単語")
    plt.ylabel("出現頻度")
    plt.title("頻度上位10語")
    plt.tight_layout()
    plt.tight_layout()
    plt.savefig("../36.png", dpi=200, bbox_inches="tight")
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()