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
    word_counts = Counter(words)
    freqs = list(word_counts.values())

    max_freq = max(freqs)

    freq_of_freq = Counter(freqs)

    x = list(range(1, max_freq + 1))
    y = [freq_of_freq.get(i, 0) for i in x]

    plt.figure(figsize=(10, 5))
    plt.bar(x, y)
    plt.xlabel("出現頻度")
    plt.ylabel("単語の種類数")
    plt.title("単語出現頻度のヒストグラム")
    plt.tight_layout()

    plt.savefig("../38.png", dpi=200, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()