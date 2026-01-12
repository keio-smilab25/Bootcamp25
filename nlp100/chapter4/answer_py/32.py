from nlp30 import parse_mecab

def main():
    sentences = parse_mecab("../neko.txt.mecab")
    for sent in sentences:
        for m in sent:
            if m["pos"] == "動詞":
                print(m["base"])

if __name__ == "__main__":
    main()