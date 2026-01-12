import json

import ginza
import spacy
from tqdm import tqdm  # 進捗表示用（なければ uv add tqdm）

# GiNZAモデルのロード
print("モデルをロード中...")
nlp = spacy.load("ja_ginza")

input_file = "ai.ja.txt"
output_file = "ai.ja.txt.parsed"

json_data = []

print("解析を開始します...")
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# メモリ節約のため、適度に改行で区切って処理するか、nlp.pipeを使う
# ここでは簡易的に段落ごと、あるいは全文を処理しますが、
# spacyのmax_length制限を回避するため行ごとに処理します。
lines = text.split("\n")

sentence_id_counter = 0

# tqdmがあればプログレスバーが出ます。なければ range(len(lines)) に変えてください
for line in tqdm(lines):
    line = line.strip()
    if not line:
        continue

    # 解析実行
    doc = nlp(line)

    # 1行の中に複数の文が含まれる場合があるので、sentsで回す
    for sent in doc.sents:
        chunks = []

        # GiNZAの文節(bunsetu)区切り機能を使用
        bunsetu_spans = ginza.bunsetu_spans(sent)

        # 文節ごとの情報を取得
        # まずは全文節をリスト化してインデックスを振る
        spans_list = list(bunsetu_spans)

        for i, span in enumerate(spans_list):
            # 係り先を探す
            # span.root.head が係り先の単語。その単語がどの文節(span)に含まれるかを探す
            dst = -1
            head_token = span.root.head

            # 係り先が自分自身なら「係り先なし(-1)」
            if head_token == span.root:
                dst = -1
            else:
                # head_tokenがどのspanに入っているか検索
                for j, target_span in enumerate(spans_list):
                    if head_token in target_span:
                        dst = j
                        break

            # 形態素情報の抽出
            morphs = []
            for token in span:
                # pos_detail (品詞細分類) の処理
                pos_list = token.tag_.split("-")
                pos = pos_list[0]
                pos1 = pos_list[1] if len(pos_list) > 1 else "*"

                morphs.append(
                    {
                        "surface": token.orth_,
                        "base": token.lemma_,
                        "pos": pos,
                        "pos1": pos1,
                    }
                )

            chunks.append({"id": i, "text": span.text, "dst": dst, "morphs": morphs})

        json_data.append(
            {"sentence_id": sentence_id_counter, "text": sent.text, "chunks": chunks}
        )
        sentence_id_counter += 1

# JSON書き出し
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"完了しました！ {output_file} を作成しました。")
