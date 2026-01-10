"""
NLP100 Knock - Chapter 2: UNIX Commands
Q13: Merge col1.txt and col2.txt

paste col1.txt col2.txt
"""
import pandas as pd


def merge_columns():
    """
    col1.txtとcol2.txtを読み込み、タブ区切りで結合して保存する
    """
    df1 = pd.read_csv('col1.txt', header=None)
    df2 = pd.read_csv('col2.txt', header=None)

    merged_df = pd.concat([df1, df2], axis=1)

    merged_df.to_csv(
        'merged.txt',
        sep='\t',
        index=False,
        header=False,
        lineterminator='\n'
    )


def main():
    """
    メイン関数
    """
    merge_columns()


if __name__ == "__main__":
    main()
