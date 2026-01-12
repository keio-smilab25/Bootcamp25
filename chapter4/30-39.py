import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示用ライブラリ
from collections import Counter

# ==========================================
# 30. 形態素解析結果の読み込み
# ==========================================
def parse_mecab(filename):
    sentences = []
    sentence = []
    
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            # 文末（EOS）の処理
            if line.strip() == 'EOS':
                if sentence:
                    sentences.append(sentence)
                    sentence = []
                continue
            
            # タブ区切りで分割
            fields = line.split('\t')
            
            # データ形式のチェック（要素数が足りない行はスキップ）
            if len(fields) < 5:
                continue
            
            # ご提示いただいたフォーマットに基づくインデックス指定
            # 0:表層形, 1:?, 2:?, 3:基本形, 4:品詞-細分類...
            surface = fields[0]
            base = fields[3]
            pos_full = fields[4]
            
            # 品詞情報をハイフンで分割
            pos_parts = pos_full.split('-')
            pos = pos_parts[0]
            pos1 = pos_parts[1] if len(pos_parts) > 1 else '*'
            
            # 辞書を作成
            morph = {
                'surface': surface,
                'base': base,
                'pos': pos,
                'pos1': pos1
            }
            sentence.append(morph)
            
    return sentences

# 読み込み実行
sentences = parse_mecab('neko.txt.mecab')
print(f"30. 読み込み完了: 全{len(sentences)}文を確認しました。")
print("-" * 20)


# ==========================================
# 31. 動詞の表層形
# ==========================================
verbs_surface = []
for sent in sentences:
    for morph in sent:
        if morph['pos'] == '動詞':
            verbs_surface.append(morph['surface'])  # リストに追加して順序を保持

print(f"31. 動詞の表層形（最初の5つ）: {verbs_surface[:5]}")


# ==========================================
# 32. 動詞の基本形
# ==========================================
verbs_base = []
for sent in sentences:
    for morph in sent:
        if morph['pos'] == '動詞':
            verbs_base.append(morph['base'])  # リストに追加して順序を保持

print(f"32. 動詞の基本形（最初の5つ）: {verbs_base[:5]}")


# ==========================================
# 33. 「AのB」
# ==========================================
noun_phrase_no = []
for sent in sentences:
    for i in range(1, len(sent) - 1):
        prev_m = sent[i-1]
        curr_m = sent[i]
        next_m = sent[i+1]
        
        # 名詞 + の + 名詞
        if (prev_m['pos'] == '名詞' and 
            curr_m['surface'] == 'の' and 
            next_m['pos'] == '名詞'):
            phrase = prev_m['surface'] + curr_m['surface'] + next_m['surface']
            noun_phrase_no.append(phrase)

print(f"33. 「AのB」（最初の5つ）: {noun_phrase_no[:5]}")


# ==========================================
# 34. 名詞の連接
# ==========================================
longest_nouns = []
for sent in sentences:
    current_noun_chain = []
    for morph in sent:
        if morph['pos'] == '名詞':
            current_noun_chain.append(morph['surface'])
        else:
            # 名詞以外が来たら、これまで溜めた名詞チェーンを確認
            if len(current_noun_chain) > 1:
                longest_nouns.append("".join(current_noun_chain))
            current_noun_chain = [] # リセット
            
    # 文末の処理
    if len(current_noun_chain) > 1:
        longest_nouns.append("".join(current_noun_chain))

# 一番長いものを探す
max_len_noun = max(longest_nouns, key=len) if longest_nouns else "なし"

print(f"34. 名詞の連接（最初の5つ）: {longest_nouns[:5]}")
print(f"34. 最長の名詞連接: {max_len_noun}")


# ==========================================
# 35. 単語の出現頻度
# ==========================================
# 分析対象とする単語のリスト（記号や空白は除外してカウントします）
all_words = []
for sent in sentences:
    for morph in sent:
        if morph['pos'] not in ('記号', '空白'):
            all_words.append(morph['surface'])

word_counts = Counter(all_words)
sorted_word_counts = word_counts.most_common()

print(f"35. 出現頻度上位5語: {sorted_word_counts[:5]}")


# ==========================================
# 36. 頻度上位10語（グラフ）
# ==========================================
def plot_top10_words(counter):
    top10 = counter.most_common(10)
    words, counts = zip(*top10)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title('36. 頻度上位10語')
    plt.xlabel('単語')
    plt.ylabel('出現頻度')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

print("36. グラフを表示中...")
plot_top10_words(word_counts)

# ==========================================
# 文の再分割処理（前処理）
# ==========================================
# 現在の sentences が「巨大な1文」になっている可能性があるため、
# 「。」を区切りとしてリストを再構築します。

new_sentences = []
current_sentence = []

# ネストされたリストを一度フラットにしてから回す
all_morphemes = [m for sent in sentences for m in sent]

for morph in all_morphemes:
    current_sentence.append(morph)
    # 表層形が「。」なら文の区切りとみなす
    if morph['surface'] == '。':
        new_sentences.append(current_sentence)
        current_sentence = []

# 残りがあれば追加（「。」で終わらない末尾など）
if current_sentence:
    new_sentences.append(current_sentence)

# デバッグ用：分割後の文の数を確認
print(f"再分割後の文の数: {len(new_sentences)}")
print(new_sentences[:3])


# ==========================================
# 37. 「猫」と共起頻度の高い上位10語（修正版）
# ==========================================
co_occurrence_words = []
target_word = '猫'

# 再分割した new_sentences を使用してループ
for sent in new_sentences:
    # 1文の中にある単語リスト（表層形）を作成（記号・空白は除く）
    surfaces = [m['surface'] for m in sent if m['pos'] not in ('記号', '空白')]
    
    # その文に「猫」が含まれているか判定
    if target_word in surfaces:
        # その文に含まれる単語を集計用リストに追加
        for w in surfaces:
            # 「猫」自身は共起語としてカウントしない
            if w != target_word:
                co_occurrence_words.append(w)

# 集計
co_occurrence_counts = Counter(co_occurrence_words)

# グラフ描画関数
def plot_co_occurrence(counter):
    if not counter:
        print(f"「{target_word}」と共起する単語が見つかりませんでした。")
        return
        
    top10 = counter.most_common(10)
    words, counts = zip(*top10)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='orange')
    plt.title(f'37. 「{target_word}」と共起頻度の高い上位10語')
    plt.xlabel('単語')
    plt.ylabel('共起頻度')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

print("37. グラフを表示中...")
plot_co_occurrence(co_occurrence_counts)

# ==========================================
# 38. ヒストグラム
# ==========================================
def plot_histogram(counter):
    counts = list(counter.values())
    
    plt.figure(figsize=(10, 6))
    # 見やすくするために範囲を1〜20回程度に絞って表示するのが一般的です
    plt.hist(counts, bins=20, range=(1, 20)) 
    plt.title('38. 単語の出現頻度のヒストグラム')
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()

print("38. グラフを表示中...")
plot_histogram(word_counts)


# ==========================================
# 39. Zipfの法則
# ==========================================
def plot_zipf(counter):
    # 出現頻度順に並べたリストを作成
    counts = [count for word, count in counter.most_common()]
    ranks = range(1, len(counts) + 1)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(ranks, counts)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('39. Zipfの法則')
    plt.xlabel('出現頻度順位 (log)')
    plt.ylabel('出現頻度 (log)')
    plt.grid(which="both", linestyle='--', alpha=0.5)
    plt.show()

print("39. グラフを表示中...")
plot_zipf(word_counts)