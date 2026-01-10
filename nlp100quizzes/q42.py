"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q42: Display modifier and modifiee chunks
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

            # 係り元
            modifier = get_text_without_symbol(chunk)
            # 係り先
            modifiee = get_text_without_symbol(sentence[chunk.dst])

            if modifier and modifiee:
                print(f"{modifier}\t{modifiee}")


if __name__ == "__main__":
    main()
