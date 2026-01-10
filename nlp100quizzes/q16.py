"""
NLP100 Knock - Chapter 2: UNIX Commands
Q16: Split a file into N pieces

split -l 200 -d ./popular-names.txt sp
"""
import sys
import math
import pandas as pd


def split_file(n):
    """
    ファイルをn分割して保存する

    splitはn分割ではなくl行ごとの分割になる
    本問はsplitの機能をそのまま再現するものではなく
    参考コマンドの「split -l 200 -d ./popular-names.txt sp」とは
    内容が整合しないように思えるがここでは設問のn分割を素直に実装することにする
    """
    df = pd.read_csv('popular-names.txt', sep='\t', header=None)
    total_lines = len(df)

    # 切り上げ処理
    unit = math.ceil(total_lines / n)

    for i in range(n):
        start = i * unit
        end = start + unit

        df_split = df[start:end]

        # 空のファイルは作成しないようにする
        if df_split.empty:
            break

        filename = f"sp{i:02d}.txt"
        df_split.to_csv(
            filename,
            sep='\t',
            index=False,
            header=False,
            lineterminator='\n'
        )


def main():
    """
    メイン関数
    """
    n = int(sys.argv[1])
    split_file(n)


if __name__ == "__main__":
    main()
