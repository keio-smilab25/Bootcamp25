"""
NLP100 Knock - Chapter 2: UNIX Commands
Q11: Replace tabs with spaces

sed 's/\t/ /g' popular-names.txt
"""
import pandas as pd


def replace_tabs():
    """
    タブをスペースに置換して表示する
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    # lineterminatorは行末文字 sepは区切り文字 indexは行番号 headerは列番号
    result = df.to_csv(
        lineterminator='\n',
        sep=' ', index=False,
        header=False
    )
    print(result, end='')


def main():
    """
    メイン関数
    """
    replace_tabs()


if __name__ == "__main__":
    main()
