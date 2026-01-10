"""
NLP100 Knock - Chapter 2: UNIX Commands
Q14: Output first N lines

head -n 5 popular-names.txt
"""
import sys
import pandas as pd


def output_head(n):
    """
    先頭のn行を表示する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    result = df.head(n)

    print(result.to_csv(
        sep='\t',
        index=False,
        header=False,
        lineterminator='\n'
    ), end='')


def main():
    """
    メイン関数
    """
    n = int(sys.argv[1])
    output_head(n)


if __name__ == "__main__":
    main()
