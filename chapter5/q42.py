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

    def __str__(self):
        return "".join([m.surface for m in self.morphs])

    def get_text_without_symbols(self):
        # 除外する品詞のリスト
        exclude_pos = ['記号', '補助記号', '空白']
        
        filtered_surfaces = [
            m.surface for m in self.morphs 
            if m.pos not in exclude_pos
        ]
        return "".join(filtered_surfaces)

def load_chunks_file(filename):
    sentences = []
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for sentence_data in data:
            chunks_in_sentence = []
            for chunk_dict in sentence_data:
                chunks_in_sentence.append(Chunk(chunk_dict))
            sentences.append(chunks_in_sentence)
    return sentences

sentences = load_chunks_file('ai.ja.txt.parsed')

line_count = 0
max_lines = 20  # 最初の20件だけ表示

for sentence in sentences:
    for chunk in sentence:
        # 係り先がある場合のみ処理 (dst != -1)
        if chunk.dst != -1:
            # 係り元 (自分) のテキスト（記号抜き）
            modifier = chunk.get_text_without_symbols()
            
            # 係り先 (相手) のテキスト（記号抜き）
            head_chunk = sentence[chunk.dst]
            head = head_chunk.get_text_without_symbols()
            
            # 記号除去の結果、空文字になった場合は出力しない
            if modifier != "" and head != "":
                print(f"{modifier}\t{head}")
                
                line_count += 1
                if line_count >= max_lines:
                    break
    if line_count >= max_lines:
        break