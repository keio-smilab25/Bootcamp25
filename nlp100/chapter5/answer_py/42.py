import sys
from pathlib import Path


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


class Chunk:
    def __init__(self, idx, dst):
        self.idx = idx
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def text(self):
        return "".join(m.surface for m in self.morphs if m.pos != "記号")


def parse_cabocha_output(file_path: str):
    sentences = []
    current_sentence = []
    current_chunk = None

    with open(file_path, mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()

            if line == "EOS":
                if current_chunk is not None:
                    current_sentence.append(current_chunk)

                if current_sentence:
                    for c in current_sentence:
                        if c.dst != -1 and 0 <= c.dst < len(current_sentence):
                            current_sentence[c.dst].srcs.append(c.idx)
                    sentences.append(current_sentence)

                current_sentence = []
                current_chunk = None
                continue

            if line.startswith("*"):
                if current_chunk is not None:
                    current_sentence.append(current_chunk)

                cols = line.split()
                idx = int(cols[1])
                dst = int(cols[2].rstrip("D"))
                current_chunk = Chunk(idx, dst)
                continue

            if "\t" not in line:
                continue

            surface, attr_str = line.split("\t", 1)
            details = attr_str.split(",")

            base = details[6] if len(details) > 6 else surface
            pos = details[0] if len(details) > 0 else ""
            pos1 = details[1] if len(details) > 1 else ""

            if current_chunk is not None:
                current_chunk.morphs.append(Morph(surface, base, pos, pos1))

    return sentences


def main():
    in_path = sys.argv[1] if len(sys.argv) >= 2 else "ai.ja.txt.parsed"

    out_path = Path("../answer/42.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sentences = parse_cabocha_output(in_path)

    lines = []
    for sent in sentences:
        for ch in sent:
            if ch.dst == -1:
                continue
            if not (0 <= ch.dst < len(sent)):
                continue

            src = ch.text()
            dst = sent[ch.dst].text()

            if src == "" or dst == "":
                continue

            lines.append(f"{src}\t{dst}")

    text_out = "\n".join(lines) + "\n"
    print(text_out, end="")
    out_path.write_text(text_out, encoding="utf-8")


if __name__ == "__main__":
    main()