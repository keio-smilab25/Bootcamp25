"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q33: Extract noun phrases connected by 'no' (A no B)
"""
from q30 import load_sentences


def extract_noun_phrases(sentences):
    """
    「名詞+の+名詞」の形式の名詞句を抽出する。
    """
    noun_phrases = []
    for sentence in sentences:
        # 1~len(sentence)-1の範囲にする
        for i in range(1, len(sentence) - 1):
            if (sentence[i - 1]['pos'] == '名詞' and
                    sentence[i]['surface'] == 'の' and
                    sentence[i + 1]['pos'] == '名詞'):
                phrase = (sentence[i - 1]['surface'] +
                          sentence[i]['surface'] +
                          sentence[i + 1]['surface'])
                noun_phrases.append(phrase)
    return noun_phrases


def main():
    """
    メイン関数
    """
    sentences = load_sentences()
    noun_phrases = extract_noun_phrases(sentences)

    print(f"Total phrases found: {len(noun_phrases)}")
    for phrase in noun_phrases:
        print(phrase)


if __name__ == "__main__":
    main()
