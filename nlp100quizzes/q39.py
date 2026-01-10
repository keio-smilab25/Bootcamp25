"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q39: Zipf's Law
"""
# pylint: disable=unused-import

import matplotlib.pyplot as plt
import japanize_matplotlib
from q35 import count_word_frequency
from q30 import load_sentences


def main():
    """
    メイン関数：単語の出現頻度順位と頻度の関係を両対数グラフで表示する。
    """
    sentences = load_sentences()
    word_counts = count_word_frequency(sentences)

    counts = word_counts.values

    # 1位から始まる順位のリスト
    ranks = range(1, len(counts) + 1)

    # グラフの作成
    plt.figure(figsize=(10, 6))
    plt.scatter(ranks, counts)

    # 両対数スケールに設定
    plt.xscale('log')
    plt.yscale('log')

    plt.title("Zipfの法則 (両対数グラフ)")
    plt.xlabel("出現頻度順位")
    plt.ylabel("出現頻度")
    plt.grid(True, which="both", ls="-", alpha=0.5)

    plt.savefig('q39.png')
    print("Graph saved as q39.png")
    plt.show()


if __name__ == "__main__":
    main()
