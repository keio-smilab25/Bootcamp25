import json

class Morph:
    def __init__(self, morph_dict):
        self.surface = morph_dict['surface']
        self.base = morph_dict['base']
        self.pos = morph_dict['pos']
        self.pos1 = morph_dict['pos1']

class Chunk:
    def __init__(self, chunk_dict):
        self.morphs = [Morph(m) for m in chunk_dict['morphs']]
        self.dst = chunk_dict['dst']
        self.srcs = chunk_dict['srcs']

def load_chunks_file(filename):
    sentences = []
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for sentence_data in data:
            chunks_in_sentence = [Chunk(c) for c in sentence_data]
            sentences.append(chunks_in_sentence)
    return sentences

sentences = load_chunks_file('ai.ja.txt.parsed')
output_file = 'ans46.txt'

with open(output_file, mode='w', encoding='utf-8') as f:
    for sentence in sentences:
        for chunk in sentence:
            predicate = None
            for m in chunk.morphs:
                if m.pos == '動詞':
                    predicate = m.base 
                    break
            
            # 動詞がない文節はスキップ
            if predicate is None:
                continue
            
            particles = []
            for src_idx in chunk.srcs:
                src_chunk = sentence[src_idx]
                
                # 係り元の文節内にある助詞を探す
                for m in reversed(src_chunk.morphs):
                    if m.pos == '助詞':
                        particles.append(m.surface)
                        break
            
            if len(particles) > 0:
                particles.sort()
                f.write(f"{predicate}\t{' '.join(particles)}\n")
