import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import Counter
from nlp30 import parse_mecab

def main():
    sentences = parse_mecab("../neko.txt.mecab")

    words = [
        m["surface"]
        for sent in sentences
        for m in sent
        if m["pos"] not in ("空白", "補助記号")
    ]
    counts = Counter(words)

    freq_sorted = [c for _, c in counts.most_common()]
    ranks = list(range(1, len(freq_sorted) + 1))

    plt.figure(figsize=(8, 5))
    plt.scatter(ranks, freq_sorted, s=10)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("出現頻度順位")
    plt.ylabel("出現頻度")
    plt.title("Zipfの法則（両対数）")
    plt.tight_layout()

    plt.savefig("../39.png", dpi=200, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()