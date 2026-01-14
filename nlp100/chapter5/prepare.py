from dataclasses import dataclass, field
from typing import List, Iterator, Optional

@dataclass
class Morph:
    surface: str
    base: str
    pos: str
    pos1: str

@dataclass
class Chunk:
    morphs: List[Morph] = field(default_factory=list)
    dst: int = -1
    srcs: List[int] = field(default_factory=list)

    def text(self, exclude_symbols: bool = True) -> str:
        if exclude_symbols:
            return "".join(m.surface for m in self.morphs if m.pos != "記号")
        return "".join(m.surface for m in self.morphs)

@dataclass
class Sentence:
    chunks: List[Chunk] = field(default_factory=list)

def read_cabocha_parsed(path: str) -> List[Sentence]:
    sentences: List[Sentence] = []
    chunks: List[Chunk] = []
    cur_chunk: Optional[Chunk] = None

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line == "EOS":
                if cur_chunk is not None:
                    chunks.append(cur_chunk)
                    cur_chunk = None
                if chunks:
                    for i, ch in enumerate(chunks):
                        if ch.dst != -1:
                            chunks[ch.dst].srcs.append(i)
                    sentences.append(Sentence(chunks=chunks))
                chunks = []
                continue

            if line.startswith("* "):
                if cur_chunk is not None:
                    chunks.append(cur_chunk)
                parts = line.split()
                dst = int(parts[2][:-1])
                cur_chunk = Chunk(dst=dst)
                continue
            if "\t" not in line:
                continue
            surface, rest = line.split("\t", 1)
            cols = rest.split(",")
            pos = cols[0]
            pos1 = cols[1] if len(cols) > 1 else ""
            base = cols[6] if len(cols) > 6 else surface
            if cur_chunk is None:
                cur_chunk = Chunk(dst=-1)
            cur_chunk.morphs.append(Morph(surface=surface, base=base, pos=pos, pos1=pos1))

    return sentences

if __name__ == "__main__":
    parsed_path = "./ai.ja.txt.parsed"
    sentences = read_cabocha_parsed(parsed_path)
    if sentences:
        for i, ch in enumerate(sentences[0].chunks):
            print(i, ch.dst, ch.text())
