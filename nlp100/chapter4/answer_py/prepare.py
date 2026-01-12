import MeCab

tagger = MeCab.Tagger()

with open("" \
"../neko.txt", "r", encoding="utf-8") as f_in, open("../neko.txt.mecab", "w", encoding="utf-8") as f_out:
    for line in f_in:
        f_out.write(tagger.parse(line))
