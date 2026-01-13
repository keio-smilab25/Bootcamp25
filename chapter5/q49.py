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

    def get_formatted_text(self, mask_char=None):
        exclude_pos = ['記号', '補助記号', '空白']
        
        tokens = []
        for m in self.morphs:
            if m.pos in exclude_pos:
                continue
            if mask_char and m.pos == '名詞':
                tokens.append(mask_char)
            else:
                tokens.append(m.surface)
        
        if mask_char:
            cleaned_tokens = []
            for t in tokens:
                if t == mask_char and len(cleaned_tokens) > 0 and cleaned_tokens[-1] == mask_char:
                    continue
                cleaned_tokens.append(t)
            return "".join(cleaned_tokens)
        else:
            return "".join(tokens)

def load_chunks_file(filename):
    sentences = []
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for sentence_data in data:
            chunks_in_sentence = [Chunk(c) for c in sentence_data]
            sentences.append(chunks_in_sentence)
    return sentences

def get_path_to_root(chunk_idx, sentence):
    path = []
    curr_idx = chunk_idx
    while curr_idx != -1:
        path.append(curr_idx)
        curr_idx = sentence[curr_idx].dst
    return path

input_file = 'ai.ja.txt.parsed'
output_file = 'ans49.txt'
sentences = load_chunks_file(input_file)

with open(output_file, mode='w', encoding='utf-8') as f:
    for sentence in sentences:
        noun_indices = []
        for idx, chunk in enumerate(sentence):
            if any(m.pos == '名詞' for m in chunk.morphs):
                noun_indices.append(idx)
        for k, idx_i in enumerate(noun_indices):
            for idx_j in noun_indices[k+1:]:
                path_i = get_path_to_root(idx_i, sentence)
                path_j = get_path_to_root(idx_j, sentence)
                
                if idx_j in path_i:
                    j_pos_in_path = path_i.index(idx_j)
                    path_indices = path_i[:j_pos_in_path + 1]
                    
                    path_texts = []
                    for p_idx in path_indices:
                        chunk = sentence[p_idx]
                        if p_idx == idx_i:
                            path_texts.append(chunk.get_formatted_text('X'))
                        elif p_idx == idx_j:
                            path_texts.append(chunk.get_formatted_text('Y'))
                        else:
                            path_texts.append(chunk.get_formatted_text())
                    
                    f.write(" -> ".join(path_texts) + "\n")
                
                else:
                    common_k = -1
                    for p_idx in path_i:
                        if p_idx in path_j:
                            common_k = p_idx
                            break
                    
                    if common_k != -1:
                        text_i_part = []
                        for p_idx in path_i:
                            if p_idx == common_k: break
                            chunk = sentence[p_idx]
                            mask = 'X' if p_idx == idx_i else None
                            text_i_part.append(chunk.get_formatted_text(mask))
                        
                        text_j_part = []
                        for p_idx in path_j:
                            if p_idx == common_k: break
                            chunk = sentence[p_idx]
                            mask = 'Y' if p_idx == idx_j else None
                            text_j_part.append(chunk.get_formatted_text(mask))
                        text_k = sentence[common_k].get_formatted_text()
                        
                        line = f"{' -> '.join(text_i_part)} | {' -> '.join(text_j_part)} | {text_k}"
                        f.write(line + "\n")