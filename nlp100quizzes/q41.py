"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q41: Reading the dependency analysis result (Chunks)
"""
from q40 import Morph


class Chunk:
    """
    文節情報を保持するクラス
    """
    def __init__(self, dst):
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def __str__(self):
        surface = "".join([m.surface for m in self.morphs])
        return f"surface: {surface}, dst: {self.dst}, srcs: {self.srcs}"


def load_chunks(filename='ai.ja.txt.parsed'):
    """
    解析済みファイルを読み込み、文ごとにChunkオブジェクトのリストを返す
    """
    sentences = []
    chunks = []
    current_chunk = None

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('*'):
                cols = line.split(' ')
                dst = int(cols[2].rstrip('D'))
                current_chunk = Chunk(dst)
                chunks.append(current_chunk)
                continue

            if line == 'EOS\n':
                if chunks:
                    for i, chunk in enumerate(chunks):
                        if chunk.dst != -1 and chunk.dst < len(chunks):
                            chunks[chunk.dst].srcs.append(i)
                    sentences.append(chunks)
                    chunks = []
                continue

            # 形態素情報をパースして現在の文節に追加
            if '\t' not in line:
                continue
            parts = line.split('\t', 1)
            surface, attr_str = parts
            attr = attr_str.split(',')

            base = attr[6] if len(attr) >= 7 else surface

            current_chunk.morphs.append(Morph(
                surface=surface,
                base=base,
                pos=attr[0],
                pos1=attr[1]
            ))

    return sentences


def main():
    """
    メイン処理：特定の文の文節と係り先を表示
    """
    sentences = load_chunks()

    target_idx = 100
    if len(sentences) > target_idx:
        print(f"--- Sentence {target_idx} ---")
        for i, chunk in enumerate(sentences[target_idx]):
            surface = "".join([m.surface for m in chunk.morphs])
            # print内容が長くてpycodestyleに引っかかったため分割する
            output = (
                f"Chunk {i}: {surface}\t"
                f"-> dst: {chunk.dst}\t"
                f"| srcs: {chunk.srcs}"
            )
            print(output)


if __name__ == "__main__":
    main()
