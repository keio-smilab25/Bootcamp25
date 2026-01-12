from nlp30 import parse_mecab

def main():
    sentences = parse_mecab("../neko.txt.mecab")

    for sent in sentences:
        chain = []
        for m in sent:
            if m["pos"] == "名詞":
                chain.append(m["surface"])
            else:
                if len(chain) >= 2:
                    print("".join(chain))
                chain = []
        if len(chain) >= 2:
            print("".join(chain))

if __name__ == "__main__":
    main()
