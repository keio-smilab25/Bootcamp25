import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import Counter
from nlp30 import parse_mecab

def main():
    sentences = parse_mecab("../neko.txt.mecab")

    target = "猫"
    co_words = []

    for sent in sentences:
        words = [m["surface"] for m in sent if m["pos"] not in ("空白", "補助記号")]

        if target in words:
            co_words.extend([w for w in words if w != target])

    counts = Counter(co_words)
    top10 = counts.most_common(10)

    labels = [w for w, _ in top10]
    values = [c for _, c in top10]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.xlabel("共起語")
    plt.ylabel("共起頻度")
    plt.title("「猫」と共起頻度の高い上位10語")
    plt.tight_layout()

    plt.savefig("../37.png", dpi=200, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()