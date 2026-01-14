import sys
import shutil
import subprocess
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


def pick_intro_sentence_index(sentences):
    def sent_text(sent):
        return "".join(m.surface for c in sent for m in c.morphs)

    for i, s in enumerate(sentences):
        if "人工知能（" in sent_text(s):
            return i
    for i, s in enumerate(sentences):
        if "AI（" in sent_text(s):
            return i
    return 0


def dot_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def build_dot_text(sent):
    lines = []
    lines.append("digraph {")
    lines.append('\tnode [fontname="MS Gothic"]')

    for ch in sent:
        label = ch.text()
        lines.append(f'\t{ch.idx} [label="{dot_escape(label)}"]')

    for ch in sent:
        if ch.dst != -1:
            lines.append(f"\t{ch.idx} -> {ch.dst}")

    lines.append("}")
    return "\n".join(lines) + "\n"


def main():
    in_path = sys.argv[1] if len(sys.argv) >= 2 else "ai.ja.txt.parsed"
    sent_idx = int(sys.argv[2]) if len(sys.argv) >= 3 else None

    out_dir = Path("../answer")
    out_dir.mkdir(parents=True, exist_ok=True)

    sentences = parse_cabocha_output(in_path)
    if not sentences:
        return

    idx = sent_idx if (sent_idx is not None and 0 <= sent_idx < len(sentences)) else pick_intro_sentence_index(sentences)
    sent = sentences[idx]

    dot_text = build_dot_text(sent)

    dot_path = out_dir / "44.dot"
    png_path = out_dir / "44.png"

    print(dot_text, end="")
    dot_path.write_text(dot_text, encoding="utf-8")

    dot_cmd = shutil.which("dot")
    if dot_cmd is None:
        print("dot command not found. Install graphviz (e.g., `brew install graphviz`).")
        return

    subprocess.run([dot_cmd, "-Tpng", str(dot_path), "-o", str(png_path)], check=True)
    print(str(png_path))


if __name__ == "__main__":
    main()