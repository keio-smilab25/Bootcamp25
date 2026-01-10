"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q36: Top 10 frequent words bar chart
"""
# 知能ロボティクス実験で学んだerror無効化を使ってみる
# pylint: disable=unused-import

import matplotlib.pyplot as plt
import japanize_matplotlib
from q35 import count_word_frequency
from q30 import load_sentences


def main():
    """
    メイン関数
    """
    sentences = load_sentences()
    word_counts = count_word_frequency(sentences)

    top10 = word_counts[:10]  # 上位10件を抽出する

    top10.plot.bar()
    plt.title('頻度上位10語')
    plt.xlabel('単語')
    plt.ylabel('出現頻度')

    # 画像として保存
    plt.savefig('q36.png')
    print("Graph saved as q36.png")
    plt.show()


if __name__ == "__main__":
    main()
