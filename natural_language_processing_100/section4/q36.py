from collections import Counter

from q30 import load_mecab_data

filename = "neko.txt.mecab"
sentences = load_mecab_data(filename)


words = []
for sentence in sentences:
    for morph in sentence:
        words.append(morph["surface"])

c = Counter(words)

for word, count in c.most_common(10):
    print(f"{word}\t{count}")
print(f"総単語数: {len(c)}")
