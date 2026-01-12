from Q30 import q30

def get_freq():
    sentences = q30()
    frequency = {}
    for sentence in sentences:
        for morph in sentence:
            if morph["pos"] in ["記号", "補助記号", "空白"]:
                continue
            if morph["surface"] in frequency:
                frequency[morph["surface"]] += 1
            else:
                frequency[morph["surface"]] = 1
    
    frequency_sorted = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return frequency_sorted

def main():
    frequency_sorted = get_freq()
    for word, freq in frequency_sorted:
        print(f"{freq}\t{word}")
            

if __name__ == "__main__":
    main()