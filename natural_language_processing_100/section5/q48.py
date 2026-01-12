from q41 import load_chunk_data


def get_text_without_symbols(chunk):
    return "".join([m.surface for m in chunk.morphs if not "記号" in m.pos])


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)
    output_file = "q48_result.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for sentence in sentences:
            for chunk in sentence:
                has_noun = False
                for m in chunk.morphs:
                    if m.pos == "名詞":
                        has_noun = True
                        break

                if not has_noun:
                    continue

                path = []
                curr_chunk = chunk

                while True:
                    path.append(curr_chunk)

                    if curr_chunk.dst == -1:
                        break

                    curr_chunk = sentence[curr_chunk.dst]

                path_texts = [get_text_without_symbols(c) for c in path]

                clean_texts = list(filter(None, path_texts))

                if clean_texts:
                    output_line = " -> ".join(clean_texts)
                    f.write(output_line + "\n")

    print(f"抽出完了！ '{output_file}' に保存しました。")

    print("--- 結果の先頭10行 ---")
    with open(output_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i < 10:
                print(line.strip())
