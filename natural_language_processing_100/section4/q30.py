def load_mecab_data(filename):
    """
    MeCabの解析結果ファイルを読み込み、辞書のリストのリストを返す関数
    """
    sentences = []
    morphs = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == "EOS":
                if len(morphs) > 0:
                    sentences.append(morphs)
                    morphs = []
                continue

            fields = line.split("\t")
            if len(fields) < 5:
                continue

            morph = {
                "surface": fields[0],
                "base": fields[3],
                "pos": fields[4].split("-")[0],
                "pos1": (
                    "-".join(fields[4].split("-")[1:])
                    if len(fields[4].split("-")) > 1
                    else "*"
                ),
            }
            morphs.append(morph)

    return sentences


if __name__ == "__main__":
    filename = "neko.txt.mecab"
    result = load_mecab_data(filename)

    # 確認用
    for i, sentence in enumerate(result[:2]):
        print(f"--- 文 {i} ---")
        for m in sentence:
            print(m)
