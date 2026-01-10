"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q46: Extract verb case frames (with arguments)
"""
from q41 import load_chunks


def get_text_without_symbol(chunk):
    """文節から記号を除いた文字列を返す"""
    return "".join([m.surface for m in chunk.morphs
                    if m.pos not in ["補助記号", "記号"]])


def main():
    """メイン関数"""
    sentences = load_chunks()

    with open("q46.txt", "w", encoding="utf-8") as f:
        for sentence in sentences:
            for chunk in sentence:
                # 最左の動詞を探す
                verb = next((m.base for m in chunk.morphs
                             if m.pos == "動詞"), None)
                if not verb:
                    continue

                # 係り元から助詞と項のペアを収集する
                case_items = []
                for src_idx in chunk.srcs:
                    src_chunk = sentence[src_idx]
                    particles = [m.surface for m in src_chunk.morphs
                                 if m.pos == "助詞"]
                    if particles:
                        # 助詞と文節テキストをペアにする
                        case_items.append({
                            "particle": particles[-1],
                            "text": get_text_without_symbol(src_chunk)
                        })

                if case_items:
                    # 助詞の辞書順でソートする
                    case_items.sort(key=lambda x: x["particle"])

                    particles_str = " ".join([item["particle"]
                                              for item in case_items])
                    texts_str = " ".join([item["text"] for item in case_items])

                    f.write(f"{verb}\t{particles_str}\t{texts_str}\n")


if __name__ == "__main__":
    main()
