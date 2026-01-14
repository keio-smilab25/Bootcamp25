from Q41 import q41

def q45():
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
                    particles.append(parts[-1].base)
            
            if particles:
                particles.sort()
                particles_str = " ".join(particles)
                print(f"{has_verb[0].base}\t{particles_str}")

if __name__ == "__main__":
    q45()