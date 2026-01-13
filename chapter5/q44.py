import json
from graphviz import Digraph

class Morph:
    def __init__(self, morph_dict):
        self.surface = morph_dict['surface']
        self.base = morph_dict['base']
        self.pos = morph_dict['pos']
        self.pos1 = morph_dict['pos1']

class Chunk:
    def __init__(self, chunk_dict):
        self.id = chunk_dict['id']
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

def visualize_sentence(sentence, filename='tree'):
    """
    1文(Chunkのリスト)を受け取り、Graphvizで有向グラフを作成して保存する
    """
    # 有向グラフの作成
    g = Digraph(format='png')
    g.attr('node', fontname='Hiragino Sans')
    g.attr('edge', fontname='Hiragino Sans')
    
    g.attr(rankdir='UT') 

    for chunk in sentence:
        # ノード（文節）の追加
        node_text = chunk.get_text_without_symbols()
        g.node(str(chunk.id), label=node_text)
        
        # 係り先がある場合のみ線を引く
        if chunk.dst != -1:
            g.edge(str(chunk.id), str(chunk.dst))

    # レンダリング（画像生成）
    output_path = g.render(filename, view=True)
    print(f"画像を保存しました: {output_path}")

sentences = load_chunks_file('ai.ja.txt.parsed')

target_index = 24
visualize_sentence(sentences[target_index], filename='dependency_tree')

