from q41 import load_chunk_data


def get_text_without_symbols(chunk):
    text = ""
    for morph in chunk.morphs:
        if not "記号" in morph.pos:
            text += morph.surface
    return text


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)

    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst != -1:
                src_text = get_text_without_symbols(chunk)
                dst_chunk = sentence[chunk.dst]
                dst_text = get_text_without_symbols(dst_chunk)
                if src_text != "" and dst_text != "":
                    print(f"{src_text}\t{dst_text}")
