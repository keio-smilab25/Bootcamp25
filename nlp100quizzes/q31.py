"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q31: Extract surface forms of verbs
"""
from q30 import load_sentences


def extract_verb_surfaces(sentences):
    """
    形態素情報のリストから動詞の表層形を抽出する。
    """
    return [
        morph['surface']
        for sentence in sentences
        for morph in sentence
        if morph['pos'] == '動詞'
    ]


def main():
    """
    メイン関数
    """
    sentences = load_sentences()
    verb_surfaces = extract_verb_surfaces(sentences)

    print(f"Total verbs found: {len(verb_surfaces)}")
    for surface in verb_surfaces:
        print(surface)


if __name__ == "__main__":
    main()
