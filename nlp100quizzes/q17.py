"""
NLP100 Knock - Chapter 2: UNIX Commands
Q17: Distinct strings in the first column

cut -f 1 popular-names.txt | sort | uniq
"""
import pandas as pd


def get_unique_names():
    """
    1列目の名前の種類を求め、ソートして表示する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    # df[0]は先頭の列
    unique_names = df[0].unique()
    unique_names.sort()

    for name in unique_names:
        print(name)


def main():
    """
    メイン関数
    """
    get_unique_names()


if __name__ == "__main__":
    main()
