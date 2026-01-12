from nlp30 import parse_mecab

def main():
    sentences = parse_mecab("../neko.txt.mecab")

    for sent in sentences:
        for i in range(1, len(sent) - 1):
            if sent[i]["surface"] != "の":
                continue
            if sent[i-1]["pos"] == "名詞" and sent[i+1]["pos"] == "名詞":
                print(sent[i-1]["surface"] + "の" + sent[i+1]["surface"])

if __name__ == "__main__":
    main()