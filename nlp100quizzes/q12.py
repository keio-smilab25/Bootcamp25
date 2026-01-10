"""
NLP100 Knock - Chapter 2: UNIX Commands
Q12: Extract column 1 and column 2 to separate files

cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt
"""
import pandas as pd


def extract_columns():
    """
    1列目と2列目を抽出してファイルに保存する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)

    # 1列目
    col1 = df[0]  # txtの行列とデータの行列は対応が逆になってる 文の行はdfの列に入ってる
    col1.to_csv(
        'col1.txt',
        index=False,
        header=False,
        lineterminator='\n'
    )

    # 2列目
    col2 = df[1]
    col2.to_csv(
        'col2.txt',
        index=False,
        header=False,
        lineterminator='\n'
    )


def main():
    """
    メイン関数
    """
    extract_columns()


if __name__ == "__main__":
    main()
