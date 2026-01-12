import MeCab

# 2. MeCabで形態素解析してファイルに保存
# コマンドラインで `mecab neko.txt -o neko.txt.mecab` を実行するのと同義です
tagger = MeCab.Tagger()
with open('neko.txt', 'r', encoding='utf-8') as f_in, \
     open('neko.txt.mecab', 'w', encoding='utf-8') as f_out:
    f_out.write(tagger.parse(f_in.read()))

print("neko.txt.mecab を作成しました。")