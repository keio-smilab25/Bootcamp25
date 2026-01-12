from q35 import c
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Hiragino Sans'

word_freq = c.most_common(10) 

labels, values = zip(*word_freq)

# グラフの作成
plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.rcParams['font.family'] = 'Hiragino Sans'
plt.title('頻出単語トップ10')
plt.xlabel('単語')
plt.ylabel('出現頻度')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()