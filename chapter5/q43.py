import json

class Morph:
    def __init__(self, morph_dict):
        self.surface = morph_dict['surface']
        self.base = morph_dict['base']
        self.pos = morph_dict['pos']
        self.pos1 = morph_dict['pos1']

    def __repr__(self):
        return f"Morph(surface='{self.surface}', base='{self.base}', pos='{self.pos}', pos1='{self.pos1}')"

class Chunk:
    def __init__(self, chunk_dict):
        self.morphs = [Morph(m) for m in chunk_dict['morphs']]
        self.dst = chunk_dict['dst']
        self.srcs = chunk_dict['srcs']

    def get_text_without_symbols(self):
        exclude_pos = ['記号', '補助記号', '空白']
        filtered_surfaces = [m.surface for m in self.morphs if m.pos not in exclude_pos]
        return "".join(filtered_surfaces)

    def has_pos(self, target_pos):
        for m in self.morphs:
            if m.pos == target_pos:
                return True
        return False

def load_chunks_file(filename):
    sentences = []
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for sentence_data in data:
            chunks_in_sentence = [Chunk(c) for c in sentence_data]
            sentences.append(chunks_in_sentence)
    return sentences

sentences = load_chunks_file('ai.ja.txt.parsed')

limit = 20
count = 0

for sentence in sentences:
    for chunk in sentence:
        if chunk.dst == -1:
            continue
        
        head_chunk = sentence[chunk.dst]
        
        if chunk.has_pos('名詞') and head_chunk.has_pos('動詞'):
            
            modifier_text = chunk.get_text_without_symbols()
            head_text = head_chunk.get_text_without_symbols()
            
            if modifier_text and head_text:
                print(f"{modifier_text}\t{head_text}")
                count += 1
                if count >= limit:
                    break

