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


def load_pos_data(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    sentences = []

    for sent_data in data:
        morphs_in_sentence = []
        for chunk in sent_data["chunks"]:
            for m in chunk["morphs"]:
                morph = Morph(
                    surface=m["surface"], base=m["base"], pos=m["pos"], pos1=m["pos1"]
                )
                morphs_in_sentence.append(morph)
        sentences.append(morphs_in_sentence)

    return sentences


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_pos_data(filename)

    print("--- 3文目の形態素 ---")
    for morph in sentences[2]:
        print(morph)
