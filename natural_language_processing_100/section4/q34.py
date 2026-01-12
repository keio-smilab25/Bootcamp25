from q30 import load_mecab_data

filename = "neko.txt.mecab"
sentences = load_mecab_data(filename)

noun_phrases = []

for sentence in sentences:
    for i in range(len(sentence) - 2):
        w1 = sentence[i]
        w2 = sentence[i + 1]
        w3 = sentence[i + 2]

        if w1["pos"] == "名詞" and w2["surface"] == "の" and w3["pos"] == "名詞":
            phrase = w1["surface"] + w2["surface"] + w3["surface"]
            noun_phrases.append(phrase)

for phrase in noun_phrases:
    print(phrase)
print(f"抽出された総数: {len(noun_phrases)}")
