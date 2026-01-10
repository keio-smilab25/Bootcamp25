"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q37: Co-occurrence of '猫' (Cat)
"""
# pylint: disable=unused-import

import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd
from q30 import load_sentences


def get_co_occurrence(sentences, target_word='猫'):
    """
    指定した単語が含まれる文から、共起語を抽出する。
    """
    co_occurring_words = []

    for sentence in sentences:
        # 文中に target_word が含まれているか確認
        surfaces = [morph['surface'] for morph in sentence]
        if target_word in surfaces:
            # その文に含まれる単語(記号とターゲット自身を除く)を収集
            for morph in sentence:
                if morph['pos'] != '記号' and morph['surface'] != target_word:
                    co_occurring_words.append(morph['base'])

    return pd.Series(co_occurring_words).value_counts()


def main():
    """
    メイン関数
    """
    sentences = load_sentences()
    co_counts = get_co_occurrence(sentences)

    top10 = co_counts[:10]  # 上位10件を抽出する
    top10.plot.bar()
    plt.title('「猫」と共起頻度の高い上位10語')
    plt.xlabel('単語')
    plt.ylabel('出現頻度')

    plt.savefig('q37.png')
    print("Graph saved as q37.png")
    plt.show()


if __name__ == "__main__":
    main()
