from q41 import load_chunk_data


def get_last_particle(chunk):
    for morph in reversed(chunk.morphs):
        if morph.pos == "助詞":
            return morph.surface
    return None


def get_text_without_symbols(chunk):
    return "".join([m.surface for m in chunk.morphs if not "記号" in m.pos])


def find_sahen_wo_connection(chunk, sentence):
    for src_idx in chunk.srcs:
        src_chunk = sentence[src_idx]

        if len(src_chunk.morphs) >= 2:
            last_morph = src_chunk.morphs[-1]
            second_last_morph = src_chunk.morphs[-2]

            if (last_morph.pos == "助詞" and last_morph.surface == "を") and (
                second_last_morph.pos == "名詞"
            ):
                return src_idx, second_last_morph.surface

    return None, None


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)
    output_file = "q47_result.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in sentences:
            for chunk in sentence:
                verb_base = None
                for m in chunk.morphs:
                    if m.pos == "動詞":
                        verb_base = m.base
                        break

                if verb_base is None:
                    continue

                sahen_idx, sahen_noun = find_sahen_wo_connection(chunk, sentence)

                if sahen_idx is not None:
                    predicate = f"{sahen_noun}を{verb_base}"

                    particle_term_pairs = []

                    for src_idx in chunk.srcs:
                        if src_idx == sahen_idx:
                            continue

                        src_chunk = sentence[src_idx]
                        particle = get_last_particle(src_chunk)

                        if particle:
                            term = get_text_without_symbols(src_chunk)
                            particle_term_pairs.append((particle, term))

                    if len(particle_term_pairs) > 0:
                        particle_term_pairs.sort(key=lambda x: x[0])

                        particles = [x[0] for x in particle_term_pairs]
                        terms = [x[1] for x in particle_term_pairs]

                        output_line = (
                            f"{predicate}\t{' '.join(particles)}\t{' '.join(terms)}"
                        )
                        f.write(output_line + "\n")

    print(f"抽出完了！ '{output_file}' に保存しました。")
