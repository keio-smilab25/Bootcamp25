import sys
from itertools import combinations

from q41 import load_chunk_data


def get_path_to_root(chunk_idx, chunks):
    path = []
    curr = chunk_idx
    while curr != -1:
        path.append(curr)
        curr = chunks[curr].dst
    return path


def get_formatted_chunk(chunk, mask_char=None):
    res = ""
    is_masking = False

    for m in chunk.morphs:
        if "記号" in m.pos:
            continue

        if mask_char and m.pos == "名詞":
            if not is_masking:
                res += mask_char
                is_masking = True
        else:
            res += m.surface
            is_masking = False

    return res


def main():
    filename = "ai.ja.txt.parsed"
    try:
        sentences = load_chunk_data(filename)
    except Exception as e:
        print(f"データ読み込みエラー: {e}")
        return

    for chunks in sentences:

        noun_indices = [
            i for i, c in enumerate(chunks) if any(m.pos == "名詞" for m in c.morphs)
        ]

        for i, j in combinations(noun_indices, 2):
            path_i = get_path_to_root(i, chunks)
            path_j = get_path_to_root(j, chunks)

            if j in path_i:
                end_idx = path_i.index(j)
                path_nodes = path_i[: end_idx + 1]

                formatted_nodes = []
                for idx in path_nodes:
                    if idx == i:
                        formatted_nodes.append(get_formatted_chunk(chunks[idx], "X"))
                    elif idx == j:
                        formatted_nodes.append(get_formatted_chunk(chunks[idx], "Y"))
                    else:
                        formatted_nodes.append(get_formatted_chunk(chunks[idx]))

                print(" -> ".join(formatted_nodes))

            else:
                k = -1
                for node in path_i:
                    if node in path_j:
                        k = node
                        break

                if k != -1:
                    path_i_part = path_i[: path_i.index(k)]
                    path_j_part = path_j[: path_j.index(k)]

                    str_i = []
                    for idx in path_i_part:
                        txt = (
                            get_formatted_chunk(chunks[idx], "X")
                            if idx == i
                            else get_formatted_chunk(chunks[idx])
                        )
                        str_i.append(txt)

                    str_j = []
                    for idx in path_j_part:
                        txt = (
                            get_formatted_chunk(chunks[idx], "Y")
                            if idx == j
                            else get_formatted_chunk(chunks[idx])
                        )
                        str_j.append(txt)

                    str_k = get_formatted_chunk(chunks[k])

                    part_i_str = " -> ".join(str_i)
                    part_j_str = " -> ".join(str_j)
                    print(f"{part_i_str} | {part_j_str} | {str_k}")


if __name__ == "__main__":
    main()
