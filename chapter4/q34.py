from q30 import load_mecab

sentences = load_mecab('neko.txt.mecab')

noun_connections = []
for sentence in sentences:
    current_nouns = []
    
    for morph in sentence:
        if morph['pos'] == '名詞':
            current_nouns.append(morph['surface'])
        else:
            if len(current_nouns) >= 2:
                noun_connections.append("".join(current_nouns))
            current_nouns = []
    if len(current_nouns) >= 2:
        noun_connections.append("".join(current_nouns))

print(noun_connections)
