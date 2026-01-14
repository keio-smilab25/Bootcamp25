from Q41 import q41, Chunk

def q46():
    sentences = q41()

    for sentence in sentences:
        for chunk in sentence:
            has_verb = [m for m in chunk.morphs if m.pos == "動詞"]
            if not has_verb:
                continue
            
            particles = []
            for src_idx in chunk.srcs:
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
                print(f"{has_verb[0].base}\t{particles_str}\t{items_str}")

if __name__ == "__main__":
    q46()