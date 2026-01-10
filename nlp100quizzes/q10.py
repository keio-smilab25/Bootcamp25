"""
NLP100 Knock - Chapter 2: UNIX Commands
Q10: Line count

wc -l popular-names.txt
"""
import pandas as pd


def count_lines():
    """
    行数を数える
    """
    # lineterminatorは行の区切り sepは列の区切り
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    print(len(df))


def main():
    """
    メイン関数
    """
    count_lines()


if __name__ == "__main__":
    main()
