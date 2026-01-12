from Q30 import q30

def main():
    k = 0
    settences = q30()
    for sentence in settences:
        for morph in sentence:
            if k == 1:
                if morph["pos"] == "名詞":
                    meishiku += morph["surface"]
                    print(meishiku)
                k = 0
                meishiku = ""

            if morph["surface"] == "の" and morph["pos"] == "助詞":
                k=1
                meishiku = morphA + morph["surface"]

            if morph["pos"] == "名詞":
                morphA = morph["surface"]

if __name__ == "__main__":
    main()