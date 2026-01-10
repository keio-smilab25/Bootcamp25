"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q38: Histogram of word frequencies
"""
# pylint: disable=unused-import

import matplotlib.pyplot as plt
import japanize_matplotlib
from q35 import count_word_frequency
from q30 import load_sentences


def main():
    """
    メイン関数：単語の出現頻度のヒストグラムを表示する。
    """
    sentences = load_sentences()
    word_counts = count_word_frequency(sentences)

    # 頻度の値だけを抽出する
    counts = word_counts.values

    # ヒストグラムの作成
    plt.figure(figsize=(10, 6))
    plt.hist(counts, bins=100)
    plt.title('単語の出現頻度のヒストグラム')
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')

    plt.savefig('q38.png')
    print("Graph saved as q38.png")
    plt.show()


if __name__ == "__main__":
    main()
