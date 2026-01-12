def parse_mecab(filename: str):
    sentences = []
    sentence = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")

            if not line or line == "EOS":
                continue

            fields = line.split("\t")
            if len(fields) < 5:
                continue

            surface = fields[0]
            base = fields[3] if fields[3] else surface

            pos_full = fields[4]              # 例: "動詞-非自立可能"
            pos_parts = pos_full.split("-")
            pos = pos_parts[0]
            pos1 = pos_parts[1] if len(pos_parts) > 1 else "*"

            sentence.append({
                "surface": surface,
                "base": base,
                "pos": pos,
                "pos1": pos1,
            })

            # 「。」で文を確定
            if surface == "。":
                sentences.append(sentence)
                sentence = []

    if sentence:
        sentences.append(sentence)

    return sentences


if __name__ == "__main__":
    sentences = parse_mecab("../neko.txt.mecab")
    print(f"30: 読み込み完了（{len(sentences)}文）")