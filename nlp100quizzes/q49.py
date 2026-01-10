"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q49: Shortest dependency path between noun phrases
"""
import re
from itertools import combinations
from q41 import load_chunks


def get_masked_text(chunk, symbol):
    """文節内の名詞を記号(X/Y)に置換し、記号を除いた文字列を返す"""
    # 名詞を記号に置き換え
    text = "".join([
        symbol if m.pos == "名詞" else m.surface
        for m in chunk.morphs if m.pos not in ["補助記号", "記号"]
    ])
    # 連続する記号を1つにまとめる
    return re.sub(f"{symbol}+", symbol, text)


def get_full_text(chunk):
    """文節から記号を除いた全文字列を返す"""
    return "".join([
        m.surface for m in chunk.morphs
        if m.pos not in ["補助記号", "記号"]
    ])


def main():
    """メイン関数"""
    sentences = load_chunks()
    target_idx = 100
    if len(sentences) <= target_idx:
        return

    sentence = sentences[target_idx]
    # 名詞を含む文節のインデックスリスト
    noun_indices = [
        i for i, c in enumerate(sentence)
        if any(m.pos == "名詞" for m in c.morphs)
    ]

    for i_start, j_start in combinations(noun_indices, 2):
        path_i, path_j = [], []
        i, j = i_start, j_start

        # 合流点または直系関係を見つけるまでポインタを進める
        while i != j:
            if i < j:
                path_i.append(i)
                i = sentence[i].dst
            else:
                path_j.append(j)
                j = sentence[j].dst

        # path_i, path_j には合流点(i or j)直前までのインデックスが格納される
        if not path_j:
            # ケース1: 直系 (iから根へのパス上にjが存在する)
            # path_i[0]をXに、現在のi(すなわちj)をYに置換
            line = [get_masked_text(sentence[path_i[0]], "X")]
            line += [get_full_text(sentence[idx]) for idx in path_i[1:]]
            line.append(get_masked_text(sentence[i], "Y"))
            print(" -> ".join(line))
        else:
            # ケース2: 合流 (共通の文節 i(=j) で交わる)
            # path_i[0]をX、path_j[0]をYに置換
            p_i = [get_masked_text(sentence[path_i[0]], "X")]
            p_i += [get_full_text(sentence[idx]) for idx in path_i[1:]]

            p_j = [get_masked_text(sentence[path_j[0]], "Y")]
            p_j += [get_full_text(sentence[idx]) for idx in path_j[1:]]

            p_k = [get_full_text(sentence[i])]

            print(f"{' -> '.join(p_i)} | {' -> '.join(p_j)} | {''.join(p_k)}")


if __name__ == "__main__":
    main()
