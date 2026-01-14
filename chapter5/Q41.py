from Q40 import Morph

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

    def __repr__(self):
        surface_text = "".join([m.surface for m in self.morphs])
        return f"{surface_text}\tdst={self.dst}\tsrcs={self.srcs}"
    def text(self):
        return "".join([m.surface for m in self.morphs if m.pos != "記号"])

def q41(FILE_NAME = "./ai.ja.txt.parsed"):
    sentences = []
    current_sentence = []
    current_chunk = None

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        
        if line == "EOS":
            if current_chunk is not None:
                current_sentence.append(current_chunk)

            if current_sentence:
                for i, chunk in enumerate(current_sentence):
                    if chunk.dst != -1:
                        current_sentence[chunk.dst].srcs.append(i)
                
                sentences.append(current_sentence)
            
            current_sentence = []
            current_chunk = None
            continue
        
        # *: 文節情報
        if line.startswith("*"):  
            if current_chunk is not None:
                current_sentence.append(current_chunk)
            
            parts = line.split(" ")
            dst = int(parts[2].rstrip("D"))

            current_chunk = Chunk([], dst)
            continue
        
        # 形態素情報
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        
        surface = parts[0]
        features = parts[1].split(",")
        base = features[6] if len(features) > 6 else surface
        pos = features[0]
        pos1 = features[1] if len(features) > 1 else ""

        morph = Morph(surface, base, pos, pos1)
        
        if current_chunk is not None:
            current_chunk.morphs.append(morph)

    return sentences

def main():
    sentences = q41()

    target_index = 0
    if target_index < len(sentences):
        for i, chunk in enumerate(sentences[target_index]):
            print(f"[{i}]\t{chunk}")

if __name__ == "__main__":
    main()