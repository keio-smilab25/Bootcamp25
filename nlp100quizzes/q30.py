"""
NLP100 Knock - Chapter 4: Morphological Analysis
Q30: Reading the morphological analysis result
"""


def load_sentences(filename='neko.txt.mecab'):
    """
    MeCabの解析結果ファイルを読み込む
    """
    sentences = []
    morphs = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line == 'EOS\n':
                if morphs:
                    sentences.append(morphs)
                    morphs = []
                continue

            fields = line.split('\t')
            if len(fields) < 2:
                continue

            surface = fields[0]
            attr = fields[1].split(',')

            # surface: 表層形, base: 基本形, pos: 品詞, pos1: 品詞細分類1
            morph = {
                'surface': surface,
                'base': attr[6],
                'pos': attr[0],
                'pos1': attr[1]
            }
            morphs.append(morph)

    return sentences


def main():
    """
    メイン関数
    """
    sentences = load_sentences()

    # neko.txtを入手できなかった
    # 読み仮名のない原文で高品質のものを発見できなかったため読み仮名のある青空文庫からコピーした
    if sentences:
        for m in sentences[1]:
            print(m)


if __name__ == "__main__":
    main()
