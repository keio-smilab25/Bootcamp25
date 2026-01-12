from Q30 import q30

def main():
    sentences = q30()
    for sentence in sentences:
        for morph in sentence:
            if morph["pos"] == "動詞":
                print(morph["base"])

if __name__ == "__main__":
    main()