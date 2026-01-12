from Q30 import q30
from Q35 import get_freq
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"

def main():
    frequency_sorted = get_freq()
    freqs = [item[1] for item in frequency_sorted]
    ranks = range(1, len(freqs) + 1)

    plt.scatter(ranks, freqs)
    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("rank")
    plt.ylabel("frequency")
    plt.title("Zipf's law")
    plt.show()
            
if __name__ == "__main__":  
    main()