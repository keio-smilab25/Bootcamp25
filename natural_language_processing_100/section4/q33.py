from q30 import load_mecab_data

filename = "neko.txt.mecab"
sentences = load_mecab_data(filename)

sahen_nouns = set()

for sentence in sentences:
    for morph in sentence:
        if morph["pos"] == "名詞":
            if "サ変" in morph["pos1"]:
                sahen_nouns.add(morph["surface"])

for n in list(sahen_nouns):
    print(n)
print(f"サ変名詞の種類数: {len(sahen_nouns)}")
