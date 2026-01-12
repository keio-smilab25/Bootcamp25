from q30 import load_mecab

sentences = load_mecab('neko.txt.mecab') 

verbs_surface = [morph['surface'] for sentence in sentences for morph in sentence if morph['pos'] == '動詞']
print(verbs_surface)