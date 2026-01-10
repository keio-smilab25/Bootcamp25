"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q43: Extraction of noun-to-verb dependencies
"""
from q41 import load_chunks


def get_text_without_symbol(chunk):
    """
    文節から記号を除いた文字列を返す
    """
    return "".join([
        m.surface for m in chunk.morphs
        if m.pos not in ["補助記号", "記号"]
    ])


def has_pos(chunk, pos):
    """
    文節内に指定した品詞が含まれるか判定する
    """
    return any(m.pos == pos for m in chunk.morphs)


def main():
    """
    メイン関数
    """
    sentences = load_chunks()
    target_idx = 100

    if len(sentences) > target_idx:
        sentence = sentences[target_idx]
        for chunk in sentence:
            if chunk.dst == -1:
                continue

            modifier_chunk = chunk
            modifiee_chunk = sentence[chunk.dst]

            # 係り元が名詞を含み、かつ係り先が動詞を含む場合のみ抽出する
            if has_pos(modifier_chunk, "名詞") and has_pos(modifiee_chunk, "動詞"):
                modifier = get_text_without_symbol(modifier_chunk)
                modifiee = get_text_without_symbol(modifiee_chunk)

                if modifier and modifiee:
                    print(f"{modifier}\t{modifiee}")


if __name__ == "__main__":
    main()
