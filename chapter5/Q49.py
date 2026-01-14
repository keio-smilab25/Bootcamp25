from Q41 import q41, Chunk

def mask_chunk(chunk, char):
    """
    文節をマスク化する（名詞句をX/Yに置換し、助詞などは残す）。
    """
    others = "".join([m.surface for m in chunk.morphs if m.pos != "名詞" and m.pos != "記号"])
    return char + others

def get_path_to_root(chunk_idx, sentence):
    """
    指定された文節インデックスから根までのパス（インデックスのリスト）を返す
    """
    path = []
    curr_idx = chunk_idx
    while curr_idx != -1:
        path.append(curr_idx)
        curr_idx = sentence[curr_idx].dst
    return path

def main():
    sentences = q41()

    for sentence in sentences:
        # 名詞を含む文節のインデックスを取得
        noun_indices = [i for i, chunk in enumerate(sentence) 
                        if any(m.pos == "名詞" for m in chunk.morphs)]
        
        # 名詞句のペア (i, j) を作成 (i < j)
        n = len(noun_indices)
        for x in range(n):
            for y in range(x + 1, n):
                i = noun_indices[x]
                j = noun_indices[y]
                
                path_i = get_path_to_root(i, sentence)
                path_j = get_path_to_root(j, sentence)
                
                # パターンA: j が i のパス上にある
                if j in path_i:
                    # i から j までのパスを抽出
                    j_index_in_path = path_i.index(j)
                    path_nodes = path_i[:j_index_in_path + 1]
                    
                    # 文字列リストを作成
                    path_strs = []
                    for idx in path_nodes:
                        chunk = sentence[idx]
                        if idx == i:
                            path_strs.append(mask_chunk(chunk, "X"))
                        elif idx == j:
                            path_strs.append(mask_chunk(chunk, "Y"))
                        else:
                            path_strs.append(chunk.text())
                    
                    print(" -> ".join(path_strs))

                # パターンB: 共通の文節kで合流する
                else:
                    #　kを探す
                    common_k = -1
                    for node in path_i:
                        if node in path_j:
                            common_k = node
                            break
                    
                    if common_k != -1:
                        # X: iからkの直前まで
                        path_i_strs = []
                        for idx in path_i:
                            if idx == common_k: break
                            chunk = sentence[idx]
                            if idx == i:
                                path_i_strs.append(mask_chunk(chunk, "X"))
                            else:
                                path_i_strs.append(chunk.text())
                        
                        # Y: jからkの直前まで
                        path_j_strs = []
                        for idx in path_j:
                            if idx == common_k: break
                            chunk = sentence[idx]
                            if idx == j:
                                path_j_strs.append(mask_chunk(chunk, "Y"))
                            else:
                                path_j_strs.append(chunk.text())
                        
                        # k
                        k_str = sentence[common_k].text()
                        
                        # X | Y | k
                        print(f"{' -> '.join(path_i_strs)} | {' -> '.join(path_j_strs)} | {k_str}")

if __name__ == "__main__":
    main()