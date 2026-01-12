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

counts = list(c.values())

plt.rcParams["font.family"] = "Hiragino Sans"
plt.figure(figsize=(10, 6))
plt.hist(counts, bins=100, range=(1, 100))
plt.title("単語の出現頻度のヒストグラム（1〜100回）")
plt.xlabel("出現頻度")
plt.ylabel("単語の種類数")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("q38_result.png")
plt.show()
