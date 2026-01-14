from Q41 import q41, Chunk

def q48():
    sentences = q41()

    for sentence in sentences:
        for chunk in sentence:
            if any(morph.pos == "名詞" for morph in chunk.morphs):
                path = []
                current = chunk
                while current is not None:
                    path.append(current.text())
                
                    if current.dst != -1:
                        current = sentence[current.dst]
                    else:
                        current = None
                
                if path:
                    print(" -> ".join(path))

if __name__ == "__main__":
    q48()