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

    def get_morphs_by_pos(self, pos: str):
        return [m for m in self.morphs if m.pos == pos]

    def last_particle(self):
        ps = self.get_morphs_by_pos("助詞")
        return ps[-1].surface if ps else None

    def is_sahen_wo_chunk(self):
        ms = [m for m in self.morphs if m.pos != "記号"]
        if len(ms) < 2:
            return False
        return (
            ms[-2].pos == "名詞"
            and ms[-2].pos1 == "サ変接続"
            and ms[-1].pos == "助詞"
            and ms[-1].surface == "を"
        )


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

    out_path = Path("../answer/47.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sentences = parse_cabocha_output(in_path)
    lines = []

    for sent in sentences:
        for chunk in sent:
            verbs = chunk.get_morphs_by_pos("動詞")
            if not verbs:
                continue
            verb_base = verbs[0].base
            sahen_wo_src = None
            other_srcs = []

            for src_idx in chunk.srcs:
                src_chunk = sent[src_idx]
                if src_chunk.is_sahen_wo_chunk():
                    if sahen_wo_src is None:
                        sahen_wo_src = src_chunk
                else:
                    other_srcs.append(src_chunk)

            if sahen_wo_src is None:
                continue

            predicate = sahen_wo_src.text() + verb_base

            pairs = []
            for sc in other_srcs:
                p = sc.last_particle()
                if p is None:
                    continue
                pairs.append((p, sc.text()))

            if not pairs:
                continue

            pairs.sort(key=lambda x: x[0])
            particles = [p for p, _ in pairs]
            terms = [t for _, t in pairs]

            lines.append(f"{predicate}\t{' '.join(particles)}\t{' '.join(terms)}")

    text_out = "\n".join(lines) + "\n"
    print(text_out, end="")
    out_path.write_text(text_out, encoding="utf-8")


if __name__ == "__main__":
    main()