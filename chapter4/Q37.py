from Q30 import q30
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"

"""
「猫」が含まれる文のその他の単語を共起語とし，その頻度を求める
"""

def get_kyouki_freq(target="猫"):
    sentences = q30()
    frequency = {}
    for sentence in sentences:
        if target in [morph["surface"] for morph in sentence]:
            for morph in sentence:
                if morph["surface"] == target:
                    continue
                if morph["pos"] in ["記号", "補助記号", "空白"]:
                    continue
                if morph["surface"] in frequency:
                    frequency[morph["surface"]] += 1
                else:
                    frequency[morph["surface"]] = 1
    
    frequency_sorted = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return frequency_sorted

def main():
    frequency_sorted = get_kyouki_freq()
    top10 = frequency_sorted[:10]

    plt.bar([word for word, freq in top10], [freq for word, freq in top10])
    plt.xlabel("word")
    plt.ylabel("co-occurrence frequency")
    plt.title("Top 10 co-occurring words with '猫'")
    plt.show()
            

if __name__ == "__main__":
    main()