def load_mecab(filename):
    """
    UniDic形式のMeCab解析結果を読み込む関数
    """
    sentences = []
    morphs = []
    
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            if line.strip() == 'EOS':
                if len(morphs) > 0:
                    sentences.append(morphs)
                    morphs = []
                continue
            
            fields = line.split('\t')
            
            if len(fields) < 5:
                continue
            
            surface = fields[0]
            base = fields[3]
            pos_info = fields[4]
            
            pos_tokens = pos_info.split('-')
            pos = pos_tokens[0]
            pos1 = pos_tokens[1] if len(pos_tokens) > 1 else '*'
            
            morph = {
                'surface': surface,
                'base': base,
                'pos': pos,
                'pos1': pos1
            }
            morphs.append(morph)
            
    return sentences

sentences = load_mecab('neko.txt.mecab')
            