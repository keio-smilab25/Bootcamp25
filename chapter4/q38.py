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

# 単語ごとの出現回数をカウント
c = collections.Counter(words)

frequencies = list(c.values())

plt.figure(figsize=(10, 6))
plt.hist(frequencies, bins=100, range=(1, max(frequencies)))
plt.title('単語の出現頻度分布')
plt.xlabel('出現頻度')
plt.ylabel('単語の異なり数（種類数）')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()