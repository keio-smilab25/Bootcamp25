"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q47: Mining of functional verb constructions
"""
from q41 import load_chunks


def get_text_without_symbol(chunk):
    """文節から記号を除いた文字列を返す"""
    return "".join([m.surface for m in chunk.morphs
                    if m.pos not in ["補助記号", "記号"]])


def main():
    """メイン関数"""
    sentences = load_chunks()

    with open("q47.txt", "w", encoding="utf-8") as f:
        for sentence in sentences:
            for chunk in sentence:
                # 文節内の最左の動詞を探す
                verb_m = next((m for m in chunk.morphs
                               if m.pos == "動詞"), None)
                if not verb_m:
                    continue

                # 係り元の中に「サ変接続名詞+を」があるか探す
                sw_idx = -1  # sahen_wo_index
                for idx, src_idx in enumerate(chunk.srcs):
                    src_c = sentence[src_idx]

                    if (len(src_c.morphs) == 2 and
                            src_c.morphs[0].pos1 == "サ変接続" and
                            src_c.morphs[1].surface == "を"):
                        sw_idx = idx
                        break

                if sw_idx != -1:
                    # 述語の構成
                    sw_chunk = sentence[chunk.srcs[sw_idx]]
                    # 述語: 「サ変名詞」+「を」+「動詞の基本形」
                    pred = f"{sw_chunk.morphs[0].surface}を{verb_m.base}"

                    case_items = []

                    others = (chunk.srcs[:sw_idx] +
                              chunk.srcs[sw_idx + 1:])

                    for src_idx in others:
                        src_c = sentence[src_idx]
                        particles = [m.surface for m in src_c.morphs
                                     if m.pos == "助詞"]
                        if particles:
                            case_items.append({
                                "p": particles[-1],
                                "t": get_text_without_symbol(src_c)
                            })

                    if case_items:
                        case_items.sort(key=lambda x: x["p"])
                        ps_str = " ".join([item["p"] for item in case_items])
                        ts_str = " ".join([item["t"] for item in case_items])
                        f.write(f"{pred}\t{ps_str}\t{ts_str}\n")


if __name__ == "__main__":
    main()
