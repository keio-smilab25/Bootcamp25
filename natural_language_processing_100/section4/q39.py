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

freqs = [count for word, count in c.most_common()]
ranks = range(1, len(freqs) + 1)

plt.rcParams["font.family"] = "Hiragino Sans"
plt.figure(figsize=(10, 6))
plt.scatter(ranks, freqs, s=10)
plt.xscale("log")
plt.yscale("log")
plt.title("単語の出現頻度と順位の関係（Zipfの法則）")
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.savefig("q39_result.png")
plt.show()
