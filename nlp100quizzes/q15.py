"""
NLP100 Knock - Chapter 2: UNIX Commands
Q15: Output last N lines

tail -n 5 popular-names.txt
"""
import sys
import pandas as pd


def output_tail(n):
    """
    末尾のn行を表示する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    result = df.tail(n)

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
    if len(sys.argv) < 2:
        return

    n = int(sys.argv[1])
    output_tail(n)


if __name__ == "__main__":
    main()
