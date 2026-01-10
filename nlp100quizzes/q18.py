"""
NLP100 Knock - Chapter 2: UNIX Commands
Q18: Sort lines by the third column in descending order

sort -rnk 3 popular-names.txt
"""
import pandas as pd


def sort_by_column3():
    """
    3列目の数値の降順でソートして表示する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    # by=2 3列目
    # ascending=False 降順
    sorted_df = df.sort_values(by=2, ascending=False)

    print(sorted_df.to_csv(
        sep='\t',
        index=False,
        header=False,
        lineterminator='\n'
    ), end='')


def main():
    """
    メイン関数
    """
    sort_by_column3()


if __name__ == "__main__":
    main()
