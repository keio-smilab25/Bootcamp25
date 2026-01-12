from collections import Counter

import matplotlib.pyplot as plt
from q30 import load_mecab_data

filename = "neko.txt.mecab"
sentences = load_mecab_data(filename)

words = []
for sentence in sentences:
    for morph in sentence:
        words.append(morph["surface"])

c = Counter(words)

top10 = c.most_common(10)
labels, values = zip(*top10)

plt.rcParams["font.family"] = "Hiragino Sans"
plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.title("頻度上位10単語の棒グラフ")
plt.xlabel("単語")
plt.ylabel("出現頻度")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("q37_result.png")
plt.show()
