"""
NLP100 Knock - Chapter 5: Dependency Analysis
Q44: Visualization of dependency tree
"""
import pydot
from q41 import load_chunks


def get_text_without_symbol(chunk):
    """記号を除いたテキストを返す"""
    return "".join([m.surface for m in chunk.morphs
                    if m.pos not in ["補助記号", "記号"]])


def main():
    """メイン関数"""
    sentences = load_chunks()
    target_idx = 100

    if len(sentences) <= target_idx:
        return

    sentence = sentences[target_idx]
    edges = []

    for i, chunk in enumerate(sentence):
        if chunk.dst == -1:
            continue

        # 係り元と係り先のテキスト取得
        modifier = get_text_without_symbol(chunk)
        modifiee = get_text_without_symbol(sentence[chunk.dst])

        if modifier and modifiee:
            modifier_label = f"{modifier}_{i}"
            modifiee_label = f"{modifiee}_{chunk.dst}"
            edges.append((modifier_label, modifiee_label))

    # グラフの作成
    graph = pydot.Dot(graph_type='digraph')
    font = "Hiragino Sans"

    for src, dst in edges:
        node_src = pydot.Node(src, label=src.split('_')[0], fontname=font)
        node_dst = pydot.Node(dst, label=dst.split('_')[0], fontname=font)
        graph.add_node(node_src)
        graph.add_node(node_dst)
        graph.add_edge(pydot.Edge(node_src, node_dst))

    # 画像として保存
    output_path = "q44.png"
    graph.write_png(output_path)
    print(f"Graph saved as {output_path}")


if __name__ == "__main__":
    main()
