from q41 import load_chunk_data


def get_last_particle(chunk):
    for morph in reversed(chunk.morphs):
        if morph.pos == "助詞":
            return morph.surface
    return None


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)

    output_file = "q45_result.txt"

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

                particles = []
                for src_idx in chunk.srcs:
                    src_chunk = sentence[src_idx]
                    particle = get_last_particle(src_chunk)

                    if particle:
                        particles.append(particle)

                if len(particles) > 0:
                    # 辞書順にソート
                    particles.sort()

                    output_line = f"{predicate}\t{' '.join(particles)}"

                    f.write(output_line + "\n")

    print(f"抽出完了！ '{output_file}' に保存しました。")
