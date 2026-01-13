import re
import itertools
from collections import defaultdict, Counter
from graphviz import Digraph # pip install graphviz が必要です

# ==========================================
# 1. クラス定義 (問題40, 41)
# ==========================================

class Morph:
    """形態素クラス"""
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return f"Morph(surface='{self.surface}', base='{self.base}', pos='{self.pos}', pos1='{self.pos1}')"

class Chunk:
    """文節クラス"""
    def __init__(self, idx, dst):
        self.idx = idx      # 文節番号
        self.morphs = []    # 形態素リスト
        self.dst = dst      # 係り先インデックス
        self.srcs = []      # 係り元インデックスのリスト

    def get_text(self):
        """記号を除いたテキストを返す"""
        return "".join([m.surface for m in self.morphs if m.pos != "記号"])

    def get_full_text(self):
        """記号を含むそのままのテキストを返す"""
        return "".join([m.surface for m in self.morphs])

    def has_pos(self, pos):
        """指定された品詞が含まれるか判定"""
        return any(m.pos == pos for m in self.morphs)

    def get_morphs_by_pos(self, pos, pos1=None):
        """指定された品詞の形態素リストを返す"""
        if pos1:
            return [m for m in self.morphs if m.pos == pos and m.pos1 == pos1]
        return [m for m in self.morphs if m.pos == pos]

# ==========================================
# 2. データ読み込み関数
# ==========================================

def parse_cabocha_output(file_path):
    sentences = []
    current_sentence = []
    current_chunk = None
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip()
                # EOS: 文の終わり
                if line == 'EOS':
                    if current_chunk is not None:
                        current_sentence.append(current_chunk)
                    
                    # 文末でsrcs（係り元）を構築
                    if current_sentence:
                        for c in current_sentence:
                            if c.dst != -1:
                                current_sentence[c.dst].srcs.append(c.idx)
                        sentences.append(current_sentence)
                    
                    current_sentence = []
                    current_chunk = None
                    continue

                # * から始まる行: 文節情報
                if line.startswith('*'):
                    if current_chunk is not None:
                        current_sentence.append(current_chunk)
                    
                    # 例: * 0 2D 0/0 -0.764522
                    cols = line.split(' ')
                    idx = int(cols[1])
                    dst = int(cols[2].rstrip('D'))
                    current_chunk = Chunk(idx, dst)
                    continue

                # タブ区切りの行: 形態素情報
                cols = line.split('\t')
                if len(cols) < 2:
                    continue
                surface = cols[0]
                details = cols[1].split(',')
                base = details[6] if len(details) > 6 else surface
                pos = details[0]
                pos1 = details[1]
                
                morph = Morph(surface, base, pos, pos1)
                if current_chunk:
                    current_chunk.morphs.append(morph)
                    
    except FileNotFoundError:
        print(f"Error: ファイル '{file_path}' が見つかりません。")
        print("コマンド 'cabocha -f1 ai.ja.txt > ai.ja.txt.parsed' を実行してください。")
        return []

    return sentences

# ==========================================
# 3. 実行・解答パート
# ==========================================

# ファイル読み込み
sentences = parse_cabocha_output('ai.ja.txt.parsed')

if not sentences:
    exit()

print(f"読み込み完了: {len(sentences)} 文")


print("\n=== Problem 40: 形態素の表示 (冒頭の文) ===")
target_sent = sentences[0]
morphs_output = [morph for chunk in target_sent for morph in chunk.morphs]
# 表示が見にくくなるため、表層形のリストとして表示します（オブジェクト自体はMorphです）
print([m.surface for m in morphs_output])


print("\n=== Problem 41: 文節の表示 (冒頭の文) ===")
for chunk in target_sent:
    print(f"[{chunk.idx}] {chunk.get_text()} -> {chunk.dst}")


print("\n=== Problem 42: 係り元と係り先の抽出 (最初の3文) ===")
count = 0
for sent in sentences[:3]:
    for chunk in sent:
        if chunk.dst != -1:
            src_text = chunk.get_text()
            dst_text = sent[chunk.dst].get_text()
            if src_text and dst_text:
                print(f"{src_text}\t{dst_text}")


print("\n=== Problem 43: 名詞を含む文節が動詞を含む文節に係るものを抽出 (最初の3文) ===")
for sent in sentences[:3]:
    for chunk in sent:
        if chunk.dst != -1:
            dst_chunk = sent[chunk.dst]
            if chunk.has_pos("名詞") and dst_chunk.has_pos("動詞"):
                print(f"{chunk.get_text()}\t{dst_chunk.get_text()}")


print("\n=== Problem 44: 係り受け木の可視化 ===")
def visualize_sentence(sentence, filename):
    dot = Digraph(format='png')
    # 日本語フォント設定（環境に合わせて変更してください。Macなら'Hiragino Sans'など）
    dot.attr('node', fontname='MS Gothic') 
    
    for chunk in sentence:
        node_text = chunk.get_text()
        if not node_text: continue
        dot.node(str(chunk.idx), node_text)
        if chunk.dst != -1:
            dot.edge(str(chunk.idx), str(chunk.dst))
    
    # 画像生成コマンド (Graphvizがインストールされている必要があります)
    # dot.render(filename) 
    print(f"Graphvizの定義を生成しました。実際に出力するにはコード内の dot.render() を有効化してください。")

visualize_sentence(sentences[0], 'tree_p44')


print("\n=== Problem 45: 動詞の格パターンの抽出 ===")
# 全文を処理しファイル保存 + 頻出Top5を表示
patterns_45 = []
with open('ans_45.txt', 'w', encoding='utf-8') as f:
    for sent in sentences:
        for chunk in sent:
            verbs = chunk.get_morphs_by_pos("動詞")
            if not verbs: continue
            
            predicate = verbs[0].base # 最左の動詞
            
            particles = []
            for src_idx in chunk.srcs:
                src_chunk = sent[src_idx]
                # 文節内の最後の助詞を取得
                src_particles = src_chunk.get_morphs_by_pos("助詞")
                if src_particles:
                    particles.append(src_particles[-1].surface)
            
            if particles:
                particles.sort() # 辞書順
                line = f"{predicate}\t{' '.join(particles)}"
                patterns_45.append(line)
                f.write(line + "\n")

print("上位5件の格パターン:")
for line, count in Counter(patterns_45).most_common(5):
    print(f"回数: {count}, パターン: {line}")


print("\n=== Problem 46: 動詞の格フレーム情報の抽出 ===")
# 全文を処理しファイル保存 + 最初の5件を表示
display_count = 0
with open('ans_46.txt', 'w', encoding='utf-8') as f:
    for sent in sentences:
        for chunk in sent:
            verbs = chunk.get_morphs_by_pos("動詞")
            if not verbs: continue
            
            predicate = verbs[0].base
            particles_info = [] # (助詞, 項) のタプル
            
            for src_idx in chunk.srcs:
                src_chunk = sent[src_idx]
                src_particles = src_chunk.get_morphs_by_pos("助詞")
                if src_particles:
                    p = src_particles[-1].surface
                    term = src_chunk.get_text()
                    particles_info.append((p, term))
            
            if particles_info:
                particles_info.sort(key=lambda x: x[0])
                particles = [x[0] for x in particles_info]
                terms = [x[1] for x in particles_info]
                
                line = f"{predicate}\t{' '.join(particles)}\t{' '.join(terms)}"
                f.write(line + "\n")
                
                if display_count < 5:
                    print(line)
                    display_count += 1


print("\n=== Problem 47: 機能動詞構文のマイニング ===")
# 全文を処理しファイル保存 + 最初の5件を表示
display_count = 0
with open('ans_47.txt', 'w', encoding='utf-8') as f:
    for sent in sentences:
        for chunk in sent:
            verbs = chunk.get_morphs_by_pos("動詞")
            if not verbs: continue
            
            predicate_verb = verbs[0].base
            
            target_wo_chunk = None
            other_srcs = []
            
            # 係り元をチェック
            for src_idx in chunk.srcs:
                src_chunk = sent[src_idx]
                # 「サ変接続名詞 + を」を探す
                if len(src_chunk.morphs) >= 2:
                    m_prev = src_chunk.morphs[-2]
                    m_last = src_chunk.morphs[-1]
                    if (m_prev.pos == "名詞" and m_prev.pos1 == "サ変接続" and
                        m_last.pos == "助詞" and m_last.surface == "を"):
                        target_wo_chunk = src_chunk
                    else:
                        other_srcs.append(src_chunk)
                else:
                    other_srcs.append(src_chunk)
            
            if target_wo_chunk:
                pred_text = target_wo_chunk.get_full_text() + predicate_verb
                
                # 他の項を収集
                particles_info = []
                for sc in other_srcs:
                    s_particles = sc.get_morphs_by_pos("助詞")
                    if s_particles:
                        p = s_particles[-1].surface
                        term = sc.get_text()
                        particles_info.append((p, term))
                
                if particles_info:
                    particles_info.sort(key=lambda x: x[0])
                    p_str = ' '.join([x[0] for x in particles_info])
                    t_str = ' '.join([x[1] for x in particles_info])
                    
                    line = f"{pred_text}\t{p_str}\t{t_str}"
                    f.write(line + "\n")
                    
                    if display_count < 5:
                        print(line)
                        display_count += 1


print("\n=== Problem 48: 名詞から根へのパスの抽出 (最初の5件) ===")
display_count = 0
for sent in sentences:
    if display_count >= 5: break
    for chunk in sent:
        if chunk.has_pos("名詞"):
            path = []
            curr = chunk
            while curr is not None:
                path.append(curr.get_text())
                if curr.dst != -1:
                    curr = sent[curr.dst]
                else:
                    curr = None
            if path:
                print(" -> ".join(path))
                display_count += 1
                if display_count >= 5: break


print("\n=== Problem 49: 名詞間の係り受けパスの抽出 (最初の5件) ===")
display_count = 0
for sent in sentences:
    if display_count >= 5: break
    noun_chunks = [c for c in sent if c.has_pos("名詞")]
    
    # 名詞句のペアを作成
    for i_chunk, j_chunk in itertools.combinations(noun_chunks, 2):
        if i_chunk.idx > j_chunk.idx:
            i_chunk, j_chunk = j_chunk, i_chunk # 念のため順番保証
        
        # 根までのパスを取得するヘルパー関数
        def get_path_to_root(c, s):
            path = []
            curr = c
            while curr is not None:
                path.append(curr)
                if curr.dst != -1:
                    curr = s[curr.dst]
                else:
                    curr = None
            return path

        path_i = get_path_to_root(i_chunk, sent)
        path_j = get_path_to_root(j_chunk, sent)
        ids_i = [c.idx for c in path_i]
        ids_j = [c.idx for c in path_j]
        
        # 名詞をマスクしてテキスト化するヘルパー関数
        def get_masked_text(chunk, mask_char):
            res = ""
            has_masked = False
            for m in chunk.morphs:
                if m.pos == "記号": continue
                if m.pos == "名詞":
                    if not has_masked:
                        res += mask_char
                        has_masked = True
                else:
                    res += m.surface
            return res

        line = ""
        # Case 1: j が i のパス上にある (直線型)
        if j_chunk.idx in ids_i:
            idx_of_j = ids_i.index(j_chunk.idx)
            sub_path = path_i[:idx_of_j+1]
            nodes = []
            for idx, node in enumerate(sub_path):
                if idx == 0:
                    nodes.append(get_masked_text(node, "X"))
                elif idx == len(sub_path) - 1:
                    nodes.append("Y") # 終端は名詞句Yとして表現（簡易的）
                else:
                    nodes.append(node.get_text())
            line = " -> ".join(nodes)
            
        # Case 2: 共通の祖先で交わる (合流型)
        else:
            common_k = None
            # 後ろ（根に近い方）から共通項を探す
            path_i_rev = path_i[::-1]
            path_j_rev = path_j[::-1]
            min_len = min(len(path_i), len(path_j))
            for k in range(min_len):
                if path_i_rev[k].idx == path_j_rev[k].idx:
                    common_k = path_i_rev[k]
                else:
                    break
            
            if common_k:
                idx_k_in_i = ids_i.index(common_k.idx)
                sub_i = path_i[:idx_k_in_i] # iからkの手前まで
                
                idx_k_in_j = ids_j.index(common_k.idx)
                sub_j = path_j[:idx_k_in_j] # jからkの手前まで
                
                str_i = []
                for idx, node in enumerate(sub_i):
                    if idx == 0: str_i.append(get_masked_text(node, "X"))
                    else: str_i.append(node.get_text())
                
                str_j = []
                for idx, node in enumerate(sub_j):
                    if idx == 0: str_j.append(get_masked_text(node, "Y"))
                    else: str_j.append(node.get_text())
                
                line = f"{' -> '.join(str_i)} | {' -> '.join(str_j)} | {common_k.get_text()}"
        
        if line:
            print(line)
            display_count += 1
            if display_count >= 5: break