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

    def get_text_without_symbols(self):
        exclude_pos = ['記号', '補助記号', '空白']
        filtered_surfaces = [m.surface for m in self.morphs if m.pos not in exclude_pos]
        return "".join(filtered_surfaces)

def load_chunks_file(filename):
    sentences = []
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for sentence_data in data:
            chunks_in_sentence = [Chunk(c) for c in sentence_data]
            sentences.append(chunks_in_sentence)
    return sentences

sentences = load_chunks_file('ai.ja.txt.parsed')
output_file = 'ans48.txt'

with open(output_file, mode='w', encoding='utf-8') as f:
    for sentence in sentences:
        for chunk in sentence:
            has_noun = False
            for m in chunk.morphs:
                if m.pos == '名詞':
                    has_noun = True
                    break
            
            if not has_noun:
                continue
            
            path_chunks = []
            curr_chunk = chunk
            
            while True:
                chunk_text = curr_chunk.get_text_without_symbols()
                
                path_chunks.append(chunk_text)
                
                if curr_chunk.dst == -1:
                    break
                
                curr_chunk = sentence[curr_chunk.dst]
            f.write(" -> ".join(path_chunks) + "\n")