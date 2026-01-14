from Q41 import q41, Chunk

def main():
    sentences = q41()
    
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            dst_chunk = sentence[chunk.dst]

            src_text = chunk.text()
            dst_text = dst_chunk.text()

            if src_text and dst_text:
                print(f"{src_text}\t{dst_text}")

if __name__ == "__main__":
    main()

    