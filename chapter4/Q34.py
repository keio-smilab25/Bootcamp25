from Q30 import q30

def main():
    k = 0
    maxk = 0
    maxrenstsu = ""
    rensetsu = ""
    settences = q30()
    for sentence in settences:
        for morph in sentence:
            if morph["pos"] == "名詞":
                k += 1
                rensetsu += morph["surface"]
            else:
                if maxk < k:
                    maxk = k
                    maxrenstsu = rensetsu
                k = 0
                rensetsu = ""

    print(maxrenstsu)

if __name__ == "__main__":
    main()