import sys
from pathlib import Path


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def load_sentences(filename="ai.ja.txt.parsed"):
    sentences = []
    morphs = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("*"):
                continue

            if line == "EOS\n":
                if morphs:
                    sentences.append(morphs)
                    morphs = []
                continue

            if "\t" not in line:
                continue

            surface, attr_str = line.split("\t", 1)
            attr = attr_str.split(",")

            base = attr[6] if len(attr) >= 7 else surface
            pos = attr[0] if len(attr) >= 1 else ""
            pos1 = attr[1] if len(attr) >= 2 else ""

            morphs.append(Morph(surface, base, pos, pos1))

    return sentences


def sentence_text(morphs):
    return "".join(m.surface for m in morphs)


def pick_intro_sentence_index(sentences):
    for i, ms in enumerate(sentences):
        if "人工知能（" in sentence_text(ms):
            return i
    for i, ms in enumerate(sentences):
        if "AI（" in sentence_text(ms):
            return i
    return 0


def main():
    in_path = sys.argv[1] if len(sys.argv) >= 2 else "ai.ja.txt.parsed"

    out_path = Path("../answer/40.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sentences = load_sentences(in_path)
    if not sentences:
        out_path.write_text("", encoding="utf-8")
        return

    idx = pick_intro_sentence_index(sentences)

    surfaces = [m.surface for m in sentences[idx]]
    text = str(surfaces) + "\n"

    print(text, end="")
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()