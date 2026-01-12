from Q30 import q30
from Q35 import get_freq
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"

def main():
    frequency_sorted = get_freq()
    freqs = [item[1] for item in frequency_sorted]

    plt.hist(freqs, bins=200, range=(1, freqs[0]))
    plt.xlabel("frequency")
    plt.ylabel("number of words")
    plt.title("Histogram of frequencies")
    plt.show()
            
if __name__ == "__main__":  
    main()