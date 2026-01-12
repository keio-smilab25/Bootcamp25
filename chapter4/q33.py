from q30 import load_mecab

sentences = load_mecab('neko.txt.mecab')

noun_phrases = []

for sentence in sentences:
    for i in range(len(sentence) - 2):
        morph_a = sentence[i]     
        morph_b = sentence[i+1]   
        morph_c = sentence[i+2]
        
        # 条件チェック: 名詞 + の + 名詞
        if (morph_a['pos'] == '名詞' and 
            morph_b['surface'] == 'の' and morph_b['pos'] == '助詞' and 
            morph_c['pos'] == '名詞'):
            
            phrase = morph_a['surface'] + morph_b['surface'] + morph_c['surface']
            noun_phrases.append(phrase)

print(noun_phrases)
