"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q34: Extract the longest sequence of nouns
"""
from q30 import load_sentences


def extract_noun_sequences(sentences):
    """
    名詞が連続する部分を最長一致で抽出する。
    """
    sequences = []  # sequencesとsentencesは見分けづらい
    for sentence in sentences:
        current_nouns = []
        for morph in sentence:
            if morph['pos'] == '名詞':
                current_nouns.append(morph['surface'])
            else:
                # 名詞以外が出てきたタイミングで、これまでの蓄積をチェック
                if len(current_nouns) >= 2:  # 名詞の連続が2個以上なら有効
                    sequences.append("".join(current_nouns))
                current_nouns = []

        # 文末が名詞だった場合の処理
        if len(current_nouns) >= 2:
            sequences.append("".join(current_nouns))

    return sequences


def main():
    """
    メイン関数
    """
    sentences = load_sentences()
    noun_sequences = extract_noun_sequences(sentences)

    print(f"Total sequences found: {len(noun_sequences)}")
    for seq in noun_sequences:
        print(seq)


if __name__ == "__main__":
    main()
