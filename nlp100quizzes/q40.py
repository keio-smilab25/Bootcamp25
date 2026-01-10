"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q40: Reading the morphological analysis result (Morphs)
"""


class Morph:
    """
    形態素情報を保持するクラス
    """
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return (f"surface: {self.surface}, base: {self.base}, "
                f"pos: {self.pos}, pos1: {self.pos1}")


def load_sentences(filename='ai.ja.txt.parsed'):
    """
    解析済みファイルを読み込み、文ごとにMorphオブジェクトのリストを返す
    """
    sentences = []
    morphs = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('*'):
                continue

            if line == 'EOS\n':
                if morphs:
                    sentences.append(morphs)
                    morphs = []
                continue

            # タブが含まれていない行や、空行をスキップ
            # ai.ja.txtを入手できずwikiからコピペしたためデータの質が低い
            if '\t' not in line:
                continue

            # 最初のタブでのみ分割（maxsplit=1）
            parts = line.split('\t', 1)
            if len(parts) < 2:
                continue

            surface, attr_str = parts
            attr = attr_str.split(',')

            # クラスの生成（attrの要素数が足りない場合のガード）
            if len(attr) >= 7:
                base = attr[6]
            else:
                base = surface  # 基本形が取れない場合は表層形で代用

            morphs.append(Morph(
                surface=surface,
                base=base,
                pos=attr[0],
                pos1=attr[1]
            ))

    return sentences


def main():
    """
    メイン関数
    """
    sentences = load_sentences()

    # ai.ja.txtの最初の方はwikiのタイトルなどで長い文がないためsentences[100]を指定する
    if sentences:
        for m in sentences[100]:
            print(f"surface: {m.surface}, base: {m.base}, "
                  f"pos: {m.pos}, pos1: {m.pos1}")


if __name__ == "__main__":
    main()
