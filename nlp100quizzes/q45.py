"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q45: Extract verb case patterns
"""
from q41 import load_chunks


def main():
    """
    メイン関数
    """
    sentences = load_chunks()

    with open("q45.txt", "w", encoding="utf-8") as f:
        for sentence in sentences:
            for chunk in sentence:
                # 文節内の最左の動詞を探す
                verb = None
                for morph in chunk.morphs:
                    if morph.pos == "動詞":
                        verb = morph.base
                        break

                if not verb:
                    continue

                # 動詞に係っている文節から助詞を抽出する
                particles = []
                for src_idx in chunk.srcs:
                    src_chunk = sentence[src_idx]
                    # 文節内の助詞をすべて取得
                    for morph in src_chunk.morphs:
                        if morph.pos == "助詞":
                            particles.append(morph.surface)

                # 助詞がある場合、辞書順に並べて出力する
                if particles:
                    particles = sorted(list(set(particles)))
                    f.write(f"{verb}\t{' '.join(particles)}\n")


if __name__ == "__main__":
    main()
