import json


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f"surface: {self.surface}, base: {self.base}, pos: {self.pos}, pos1: {self.pos1}"

    def __repr__(self):
        return self.__str__()


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

    def get_text(self):
        return "".join([morph.surface for morph in self.morphs])

    def __str__(self):
        return f"Chunk(text={self.get_text()}, dst={self.dst}, srcs={self.srcs})"


def load_chunk_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = []

    for sent_data in data:
        chunks = []
        for chunk_data in sent_data["chunks"]:
            morphs = []
            for m in chunk_data["morphs"]:
                morph = Morph(
                    surface=m["surface"], base=m["base"], pos=m["pos"], pos1=m["pos1"]
                )
                morphs.append(morph)
            chunk = Chunk(morphs=morphs, dst=chunk_data["dst"])
            chunks.append(chunk)

        for i, chunk in enumerate(chunks):
            if chunk.dst != -1:
                chunks[chunk.dst].srcs.append(i)

        sentences.append(chunks)

    return sentences


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)

    target_index = 7

    if len(sentences) > target_index:
        sentence = sentences[target_index]
        for i, chunk in enumerate(sentence):
            text = chunk.get_text()
            dst = chunk.dst
            print(f"文節 {i}: {text} -> 係り先: {dst}")
    else:
        print(f"文番号 {target_index} は存在しません。")
