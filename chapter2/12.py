""" cut -f 1 ./popular-names.txt > col1.txt """

import sys
import numpy as np

def main():
    if len(sys.argv) < 3: return
    input_file = sys.argv[1]
    col_idx = int(sys.argv[2]) - 1

    # loadtxtで読み込み、指定した列(usecols)のみ取得
    # usecolsを使うことでメモリ効率よく特定の列だけ抽出できます
    col_data = np.loadtxt(input_file, delimiter='\t', dtype=str, usecols=col_idx)
    
    for item in col_data:
        print(item)

if __name__ == "__main__":
    main()

"""
% uv run ./12.py ./popular-names.txt 1 > ./col1.txt
% cut -f 1 ./popular-names.txt > col1uni.txt
% diff ./col1.txt ./col1uni.txt
%
"""