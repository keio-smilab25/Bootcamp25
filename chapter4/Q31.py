from Q30 import q30

def main():
    sentences = q30()
    for sentence in sentences:
        for morph in sentence:
            if morph["surface"] == "の":
                print(morph["surface"])

if __name__ == "__main__":
    main()