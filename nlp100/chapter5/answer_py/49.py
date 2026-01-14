import sys
import itertools
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

    def has_pos(self, pos: str):
        return any(m.pos == pos for m in self.morphs)

    def masked_text(self, mask_char: str):
        res = []
        replaced = False
        for m in self.morphs:
            if m.pos == "記号":
                continue
            if m.pos == "名詞" and not replaced:
                res.append(mask_char)
                replaced = True
            elif m.pos == "名詞" and replaced:
                continue
            else:
                res.append(m.surface)
        return "".join(res)


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


def path_indices_to_root(sent, start_idx: int):
    path = []
    cur = start_idx
    visited = set()
    while cur != -1 and cur not in visited and 0 <= cur < len(sent):
        visited.add(cur)
        path.append(cur)
        cur = sent[cur].dst
    return path


def main():
    in_path = sys.argv[1] if len(sys.argv) >= 2 else "ai.ja.txt.parsed"

    out_path = Path("../answer/49.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sentences = parse_cabocha_output(in_path)
    lines = []

    for sent in sentences:
        noun_idxs = [c.idx for c in sent if c.has_pos("名詞")]
        for i, j in itertools.combinations(noun_idxs, 2):
            if i > j:
                i, j = j, i

            path_i = path_indices_to_root(sent, i)
            path_j = path_indices_to_root(sent, j)
            set_i = set(path_i)

            if j in set_i:
                end_pos = path_i.index(j)
                seq = path_i[: end_pos + 1]
                parts = []
                for t, idx in enumerate(seq):
                    if t == 0:
                        parts.append(sent[idx].masked_text("X"))
                    elif t == len(seq) - 1:
                        parts.append(sent[idx].masked_text("Y"))
                    else:
                        parts.append(sent[idx].text())
                lines.append(" -> ".join(parts))
                continue

            k = None
            pos_i = {idx: p for p, idx in enumerate(path_i)}
            for idx in path_j:
                if idx in pos_i:
                    k = idx
                    break
            if k is None:
                continue

            seq_i = path_i[: pos_i[k]]
            seq_j = path_j[: path_j.index(k)]

            left = []
            for t, idx in enumerate(seq_i):
                if t == 0:
                    left.append(sent[idx].masked_text("X"))
                else:
                    left.append(sent[idx].text())

            right = []
            for t, idx in enumerate(seq_j):
                if t == 0:
                    right.append(sent[idx].masked_text("Y"))
                else:
                    right.append(sent[idx].text())

            lines.append(f"{' -> '.join(left)} | {' -> '.join(right)} | {sent[k].text()}")

    text_out = "\n".join(lines) + "\n"
    print(text_out, end="")
    out_path.write_text(text_out, encoding="utf-8")


if __name__ == "__main__":
    main()