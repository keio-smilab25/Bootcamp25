class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return f"{self.surface}\t{self.base}\t{self.pos}\t{self.pos1}"



def q40(FILE_NAME = "./ai.ja.txt.parsed"):
    sentences = []
    current_sentence = []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if line == "EOS":
            if current_sentence:
                sentences.append(current_sentence)
                current_sentence = []
            continue

        if line.startswith("*"):
            continue
        
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        
        surface = parts[0]
        features = parts[1].split(",")
        base = features[6] if len(features) > 6 else surface
        pos = features[0]
        pos1 = features[1] if len(features) > 1 else ""

        morph = Morph(surface, base, pos, pos1)
        current_sentence.append(morph)

    return sentences

def main():
    target = q40()

    # 形態素列の表示
    for morph in target[0]:
        print(morph)


if __name__ == "__main__":
    main()