from q30 import load_mecab
import collections
sentences = load_mecab('neko.txt.mecab')

exclude_pos = ['補助記号', '記号', '空白']
words = []
for sentence in sentences:
    for morph in sentence:
        # 品詞が除外リストに入っていないか確認
        if morph['pos'] not in exclude_pos:
            words.append(morph['base'])

c = collections.Counter(words)
word_freq = c.most_common()

print(word_freq)