"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q32: Extract base forms of verbs
"""
from q30 import load_sentences


def extract_verb_bases(sentences):
    """
    形態素情報のリストから動詞の原形を抽出する。
    """
    return [
        morph['base']
        for sentence in sentences
        for morph in sentence
        if morph['pos'] == '動詞'
    ]


def main():
    """
    メイン関数
    """
    sentences = load_sentences()
    verb_bases = extract_verb_bases(sentences)

    print(f"Total verb bases found: {len(verb_bases)}")
    for base in verb_bases:
        print(base)


if __name__ == "__main__":
    main()
