"""
NLP100 Knock - Chapter 2: UNIX Commands
Q19: Frequency of strings in the first column

cut -f 1 popular-names.txt | sort | uniq -c | sort -rn
"""
import pandas as pd


def count_frequency():
    """
    1列目の文字列の出現頻度を求め、降順に表示する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    # value_counts() 出現頻度のカウント&降順ソート
    counts = df[0].value_counts()

    for name, count in counts.items():
        print(f"{count:>4} {name}")


def main():
    """
    メイン関数
    """
    count_frequency()


if __name__ == "__main__":
    main()
