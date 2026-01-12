from q30 import load_mecab
import collections
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

sentences = load_mecab('neko.txt.mecab')
target_word = '猫'
exclude_pos = ['補助記号', '記号', '空白']
co_occurrence_words = []

for sentence in sentences:
    words_in_sentence = [m['base'] for m in sentence if m['pos'] not in exclude_pos]
    
    if target_word in words_in_sentence:
        for w in words_in_sentence:
            if w != target_word:
                co_occurrence_words.append(w)

c = collections.Counter(co_occurrence_words)
top10_words = c.most_common(10)

labels, values = zip(*top10_words)

plt.figure(figsize=(10, 6))
plt.bar(labels, values)

plt.title(f'「{target_word}」と共起する頻度の高い単語トップ10')
plt.xlabel('単語')
plt.ylabel('共起頻度')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()