"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q48: Extraction of paths from nouns to the root
"""
from q41 import load_chunks


def get_text_without_symbol(chunk):
    """文節から記号を除いた文字列を返す"""
    return "".join([m.surface for m in chunk.morphs
                    if m.pos not in ["補助記号", "記号"]])


def has_noun(chunk):
    """文節に名詞が含まれるか判定"""
    return any(m.pos == "名詞" for m in chunk.morphs)


def main():
    """メイン関数"""
    sentences = load_chunks()

    # 例として Sentence 2 (「人工知能（じんこうちのう）とは...」) を処理
    if len(sentences) > 2:
        sentence = sentences[100]
        for chunk in sentence:
            if not has_noun(chunk):
                continue

            # パスの開始
            path = []
            current = chunk
            while current:
                path.append(get_text_without_symbol(current))
                # 係り先がある場合は次の文節へ、ない場合は終了
                if current.dst != -1:
                    current = sentence[current.dst]
                else:
                    current = None

            # 結果を " -> " で連結して表示
            print(" -> ".join(path))


if __name__ == "__main__":
    main()
