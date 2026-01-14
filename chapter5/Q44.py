from graphviz import Digraph
from Q41 import q41, Chunk

def q44(target_sentence_index = 0):
    sentences = q41()
    
    target_sentence = sentences[target_sentence_index]
    dot = Digraph(format='png')
    dot.attr('node', fontname='Hiragino Sans')
    
    for i, chunk in enumerate(target_sentence):
        node_text = chunk.text()

        dot.node(str(i), node_text)

        if chunk.dst != -1:
            dot.edge(str(i), str(chunk.dst))
    
    dot.view()

if __name__ == "__main__":
    q44()