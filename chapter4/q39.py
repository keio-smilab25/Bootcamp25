from q30 import load_mecab
import collections
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

sentences = load_mecab('neko.txt.mecab')
exclude_pos = ['補助記号', '記号', '空白']
words = []
for sentence in sentences:
    for morph in sentence:
        if morph['pos'] not in exclude_pos:
            words.append(morph['base'])

c = collections.Counter(words)
sorted_word_counts = c.most_common()

ranks = range(1, len(sorted_word_counts) + 1)

frequencies = [count for word, count in sorted_word_counts]

plt.figure(figsize=(10, 6))
plt.scatter(ranks, frequencies, s=10)
plt.xscale('log')
plt.yscale('log')
plt.title('単語の出現頻度順位と出現頻度の関係')
plt.xlabel('出現頻度順位 (Rank)')
plt.ylabel('出現頻度 (Frequency)')
plt.grid(which='both', linestyle='--', alpha=0.5)
plt.show()