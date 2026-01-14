from Q41 import q41, Chunk

def q47():
    sentences = q41()

    for sentence in sentences:
        for chunk in sentence:
            has_verb = [m for m in chunk.morphs if m.pos == "動詞"]
            if not has_verb:
                continue

            found_src_idx = -1

            for src_idx in chunk.srcs:
                src_chunk = sentence[src_idx]
                if len(src_chunk.morphs) >= 2:
                    noun = src_chunk.morphs[-2]
                    part = src_chunk.morphs[-1]

                    if (noun.pos == "名詞" and noun.pos1 =="サ変接続") and (part.pos == "助詞" and part.surface == "を"):
                        found_src_idx = src_idx
                        break
            if found_src_idx == -1:
                continue
            
            particles = []
            for src_idx in chunk.srcs:
                if src_idx == found_src_idx:
                    continue
                src_chunk = sentence[src_idx]
                parts = [m for m in src_chunk.morphs if m.pos == "助詞"]
                if parts:
                    particle = parts[-1].base
                    item = src_chunk.text()
                    particles.append((particle, item))

            if particles:
                particles.sort(key=lambda p: p[0])
                particles_str = " ".join([p[0] for p in particles])
                items_str = " ".join([p[1] for p in particles])
                print(f"{noun.base}を{has_verb[0].base}\t{particles_str}\t{items_str}")

if __name__ == "__main__":
    q47()