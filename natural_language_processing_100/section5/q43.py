from q41 import load_chunk_data


def get_text_without_symbols(chunk):
    text = ""
    for morph in chunk.morphs:
        if not "記号" in morph.pos:
            text += morph.surface
    return text


def has_pos(chunk, target_pos):
    for morph in chunk.morphs:
        if morph.pos == target_pos:
            return True
    return False


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)

    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                dst_chunk = sentence[chunk.dst]

                if has_pos(chunk, "名詞") and has_pos(dst_chunk, "動詞"):
                    src_text = get_text_without_symbols(chunk)
                    dst_text = get_text_without_symbols(dst_chunk)
                    print(f"{src_text}\t{dst_text}")
