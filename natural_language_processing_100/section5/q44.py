from graphviz import Digraph
from q41 import Chunk, load_chunk_data


def visualize_dependency(sentence, output_filename="q44_tree"):
    """
    文の係り受け構造を画像として保存する関数
    sentence: Chunkオブジェクトのリスト
    """
    # グラフオブジェクトの作成
    dg = Digraph(format="png")

    dg.attr("node", fontname="Hiragino Sans")
    dg.attr("edge", fontname="Hiragino Sans")
    dg.attr("graph", fontname="Hiragino Sans")

    # ノードとエッジの追加
    for i, chunk in enumerate(sentence):
        node_text = chunk.get_text()

        dg.node(str(i), label=node_text)

        # 係り先がある場合、エッジ（矢印）を追加
        if chunk.dst != -1:
            dg.edge(str(i), str(chunk.dst))

    # レンダリング（保存と表示）
    dg.render(output_filename, view=True)
    print(f"画像を保存しました: {output_filename}.png")


if __name__ == "__main__":
    filename = "ai.ja.txt.parsed"
    sentences = load_chunk_data(filename)

    target_sentence = sentences[50]

    print(f"対象文: {''.join([c.get_text() for c in target_sentence])}")
    visualize_dependency(target_sentence)
