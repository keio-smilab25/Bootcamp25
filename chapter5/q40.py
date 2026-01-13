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
        return f"surface='{self.surface}', base='{self.base}', pos='{self.pos}', pos1='{self.pos1}'"

def load_parsed_file(filename):
    sentences = []
    
    with open(filename, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        
        # 文ごとのループ
        for sentence_chunks in data:
            morphs_in_sentence = []
            # 文節ごとのループ
            for chunk in sentence_chunks:
                # 文節内の形態素ごとのループ
                for morph_data in chunk['morphs']:
                    morphs_in_sentence.append(Morph(morph_data))
            
            sentences.append(morphs_in_sentence)
            
    return sentences

sentences = load_parsed_file('ai.ja.txt.parsed')

if len(sentences) > 0:
    for i, morph in enumerate(sentences[24]):
        print(f"{morph}")
