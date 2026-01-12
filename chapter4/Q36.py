from Q30 import q30
from Q35 import get_freq 
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"

def main():
    frequency_sorted = get_freq()
    top10 = frequency_sorted[:10]

    plt.bar([word for word, freq in top10], [freq for word, freq in top10])
    plt.xlabel("word")
    plt.ylabel("frequency")
    plt.title("Top 10 frequent words")
    plt.show()
            

if __name__ == "__main__":
    main()