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
output_file = 'ans47.txt'

with open(output_file, mode='w', encoding='utf-8') as f:
    for sentence in sentences:
        for chunk in sentence:
            predicate_verb = None
            for m in chunk.morphs:
                if m.pos == '動詞':
                    predicate_verb = m.base
                    break
            
            if predicate_verb is None:
                continue
            
            sahen_wo_part = None
            other_args = []

            for src_idx in chunk.srcs:
                src_chunk = sentence[src_idx]
                
                is_sahen_wo = False
                sahen_noun = ""
                
                for i in range(len(src_chunk.morphs) - 1):
                    curr_m = src_chunk.morphs[i]
                    next_m = src_chunk.morphs[i+1]
                    
                    if (curr_m.pos == '名詞' and (curr_m.pos1 == 'サ変接続' or curr_m.pos1 == '普通名詞')) and \
                       (next_m.pos == '助詞' and next_m.surface == 'を'):
                        is_sahen_wo = True
                        sahen_noun = curr_m.surface
                        break 
                
                particle = None
                for m in reversed(src_chunk.morphs):
                    if m.pos == '助詞':
                        particle = m.surface
                        break
                
                if particle:
                    argument_text = "".join([m.surface for m in src_chunk.morphs])
                    
                    if is_sahen_wo and particle == 'を':
                        if sahen_wo_part is None:
                            sahen_wo_part = (sahen_noun, src_idx)
                        else:
                            other_args.append((particle, argument_text))
                    else:
                        other_args.append((particle, argument_text))

            if sahen_wo_part:
                sahen_noun, sahen_idx = sahen_wo_part
                new_predicate = f"{sahen_noun}を{predicate_verb}"
                
                if len(other_args) > 0:
                    other_args.sort(key=lambda x: x[0])
                    formatted_particles = [p[0] for p in other_args]
                    formatted_args = [p[1] for p in other_args]
                    f.write(f"{new_predicate}\t{' '.join(formatted_particles)}\t{' '.join(formatted_args)}\n")
                else:
                    f.write(f"{new_predicate}\t\t\n")