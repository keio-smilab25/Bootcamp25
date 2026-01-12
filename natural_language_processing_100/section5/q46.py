from q41 import load_chunk_data


def get_last_particle(chunk):
    for morph in reversed(chunk.morphs):
        if morph.pos == "助詞":
            return morph.surface
    return None


def get_text_without_symbols(chunk):
    return "".join([m.surface for m in chunk.morphs if not "記号" in m.pos])


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)

    output_file = "q46_result.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in sentences:
            for chunk in sentence:
                predicate = None
                for m in chunk.morphs:
                    if m.pos == "動詞":
                        predicate = m.base
                        break

                if predicate is None:
                    continue

                particle_term_pairs = []
                for src_idx in chunk.srcs:
                    src_chunk = sentence[src_idx]
                    particle = get_last_particle(src_chunk)

                    if particle:
                        # 項（テキスト）を取得
                        term = get_text_without_symbols(src_chunk)
                        particle_term_pairs.append((particle, term))

                if len(particle_term_pairs) > 0:
                    # 辞書順にソート
                    particle_term_pairs.sort(key=lambda x: x[0])
                    particles = [x[0] for x in particle_term_pairs]
                    terms = [x[1] for x in particle_term_pairs]

                    output_line = (
                        f"{predicate}\t{' '.join(particles)}\t{' '.join(terms)}"
                    )

                    f.write(output_line + "\n")

    print(f"抽出完了！ '{output_file}' に保存しました。")
