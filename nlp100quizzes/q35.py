"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q35: Word frequency using pandas
"""
import pandas as pd
from q30 import load_sentences


def count_word_frequency(sentences):
    """
    文章中の単語(基本形)の出現頻度を数える。
    """
    words = [
        morph['base']
        for sentence in sentences
        for morph in sentence
        if morph['pos'] != '記号'
    ]

    # pandasのSeriesに変換してvalue_countsを実行 q19を参考にした
    return pd.Series(words).value_counts()


def main():
    """
    メイン関数：頻度上位10語を表示する。
    """
    sentences = load_sentences()
    word_counts = count_word_frequency(sentences)

    print(word_counts)


if __name__ == "__main__":
    main()
