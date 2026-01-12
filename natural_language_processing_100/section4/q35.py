from q30 import load_mecab_data

filename = "neko.txt.mecab"
sentences = load_mecab_data(filename)

noun_connections = []

for sentence in sentences:
    current_nouns = []

    for morph in sentence:
        if morph["pos"] == "名詞":
            current_nouns.append(morph["surface"])
        else:
            if len(current_nouns) > 1:
                noun_connections.append("".join(current_nouns))
            current_nouns = []

    if len(current_nouns) > 1:
        noun_connections.append("".join(current_nouns))

unique_connections = set(noun_connections)

sorted_conenctions = sorted(unique_connections, key=len, reverse=True)
for n in sorted_conenctions[:10]:
    print(n)
