import json

class Morph:
    """
    形態素を表すクラス
    """
    def __init__(self, morph_dict):
        self.surface = morph_dict['surface']
        self.base = morph_dict['base']
        self.pos = morph_dict['pos']
        self.pos1 = morph_dict['pos1']

    def __repr__(self):
        return f"Morph(surface='{self.surface}', base='{self.base}', pos='{self.pos}', pos1='{self.pos1}')"


class Chunk:
    """
    文節を表すクラス
    """
    def __init__(self, chunk_dict):
        self.morphs = [Morph(m) for m in chunk_dict['morphs']]
        self.dst = chunk_dict['dst']
        self.srcs = chunk_dict['srcs']

    def __str__(self):
        return "".join([m.surface for m in self.morphs])

    def __repr__(self):
        return f"Chunk(dst={self.dst}, srcs={self.srcs}, text='{self}')"

def load_chunks_file(filename):
    sentences = []
    
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        
        # 文ごとのループ
        for sentence_data in data:
            chunks_in_sentence = []
            # 文節ごとのループ
            for chunk_dict in sentence_data:
                chunks_in_sentence.append(Chunk(chunk_dict))
            sentences.append(chunks_in_sentence)
            
    return sentences

sentences = load_chunks_file('ai.ja.txt.parsed')
if len(sentences) > 0:
    target_sentence = sentences[24]
    
    for i, chunk in enumerate(target_sentence):
        # 係り先の文節を取得
        dst_chunk_text = target_sentence[chunk.dst] if chunk.dst != -1 else "None"
        
        print(f"[{i}] {chunk}  \t---> 係り先[{chunk.dst}]: {dst_chunk_text}")