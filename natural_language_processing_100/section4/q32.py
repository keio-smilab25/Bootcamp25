from q30 import load_mecab_data

filename = "neko.txt.mecab"


sentences = load_mecab_data(filename)

verbs = set()
for sentence in sentences:
    for morph in sentence:
        if morph["pos"] == "動詞":
            verbs.add(morph["base"])

for v in verbs:
    print(v)
